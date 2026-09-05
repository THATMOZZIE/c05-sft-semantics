#!/usr/bin/env python3
"""Hard-blind channel/storage audit for the canonical self-preservation runs.

The script deliberately emits no message, reasoning, scenario, judge-rationale,
or score values.  It records only role/model identifiers, structural block
types, timeline names, and presence/count indicators. Embedded Inspect event
JSON is parsed in memory so the writer's actual serialized representation can
be checked without dumping an Inspect log.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import zipfile
from collections import Counter
from pathlib import Path
from typing import Any


TARGET_MODEL_PREFIX = "openai-api/local/"
CANONICAL_AUDITOR = "openai/gpt-5.4-mini"
CANONICAL_JUDGE = "openai/gpt-5.4-mini"
CANONICAL_CONNECTIONS = 40
THINK_TAGS = re.compile(
    r"</?(?:think|thinking)(?:\s[^>]*)?>|"
    r"<\|(?:channel|analysis|final|message|end)\|>",
    re.IGNORECASE,
)


def extract_json(archive: Path, member: str) -> Any:
    proc = subprocess.run(
        ["tar", "-xOf", str(archive), member],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"tar extraction failed: {archive.name}:{member}")
    return json.loads(proc.stdout)


def embedded_json(value: Any) -> Any | None:
    if not isinstance(value, str):
        return None
    stripped = value.lstrip()
    if not stripped.startswith(("{", "[")):
        return None
    try:
        return json.loads(value)
    except (json.JSONDecodeError, TypeError):
        return None


def walk(value: Any, path: str = "$"):
    """Yield dictionaries, including dictionaries inside serialized events."""
    if isinstance(value, dict):
        yield path, value
        for key, child in value.items():
            parsed = embedded_json(child) if key == "event" else None
            if parsed is not None:
                yield from walk(parsed, f"{path}.{key}<json>")
            elif isinstance(child, (dict, list)):
                yield from walk(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, f"{path}[{index}]")


def contains_think_markup(value: Any) -> bool:
    if isinstance(value, str):
        return bool(THINK_TAGS.search(value))
    if isinstance(value, dict):
        return any(contains_think_markup(child) for child in value.values())
    if isinstance(value, list):
        return any(contains_think_markup(child) for child in value)
    return False


def block_signature(content: Any) -> tuple[str, tuple[str, ...], bool]:
    """Return representation, block-type set, and markup presence only."""
    if isinstance(content, list):
        types = []
        for block in content:
            if isinstance(block, dict):
                types.append(str(block.get("type", "dict")))
            else:
                types.append(type(block).__name__)
        return "list", tuple(sorted(set(types))), contains_think_markup(content)
    if isinstance(content, str):
        return "str", (), bool(THINK_TAGS.search(content))
    return type(content).__name__, (), False


def stable_message_key(obj: dict[str, Any]) -> tuple[Any, ...]:
    """Deduplicate copies of the same stored message without retaining text."""
    content = obj.get("content")
    rep, types, markup = block_signature(content)
    return (
        obj.get("id"), obj.get("role"), obj.get("model"), obj.get("source"),
        rep, types, markup,
        len(content) if isinstance(content, (str, list)) else None,
    )


def classify_sample(sample: dict[str, Any], target_model: str, auditor_model: str, judge_model: str) -> dict[str, Any]:
    messages: dict[tuple[Any, ...], dict[str, Any]] = {}
    locations: Counter[str] = Counter()
    event_classes: Counter[str] = Counter()
    for path, obj in walk(sample):
        event_class = obj.get("event")
        if isinstance(event_class, str) and not event_class.lstrip().startswith(("{", "[")):
            event_classes[event_class] += 1
        if "role" in obj and "content" in obj:
            key = stable_message_key(obj)
            messages.setdefault(key, obj)
            locations[path.split(".", 2)[1] if "." in path else path] += 1

    events_data = sample.get("events_data") if isinstance(sample, dict) else None
    stored_messages = events_data.get("messages", []) if isinstance(events_data, dict) else []
    stored_messages = [obj for obj in stored_messages if isinstance(obj, dict)]

    stored_model_role_counts: Counter[tuple[str, str, str]] = Counter()
    for obj in stored_messages:
        stored_model_role_counts[(
            str(obj.get("role") or ""),
            str(obj.get("model") or ""),
            str(obj.get("source") or ""),
        )] += 1

    def timeline_messages(name: str) -> tuple[list[dict[str, Any]], int]:
        found: dict[tuple[Any, ...], dict[str, Any]] = {}
        refs: set[str] = set()
        timelines_value = sample.get("timelines") if isinstance(sample, dict) else None
        if not isinstance(timelines_value, list):
            return [], 0
        for timeline in timelines_value:
            if not isinstance(timeline, dict) or timeline.get("name") != name:
                continue
            for _, obj in walk(timeline):
                ref = obj.get("event")
                if isinstance(ref, str):
                    refs.add(ref)
        for obj in stored_messages:
            candidate_ids = {str(obj.get("id") or "")}
            content = obj.get("content")
            if isinstance(content, list):
                for block in content:
                    if not isinstance(block, dict):
                        continue
                    internal = block.get("internal")
                    if isinstance(internal, dict) and internal.get("message_id"):
                        candidate_ids.add(str(internal["message_id"]))
            if refs.intersection(candidate_ids):
                found.setdefault(stable_message_key(obj), obj)
        return list(found.values()), len(refs)

    # Inspect Petri serializes separate named auditor and target timelines.  The
    # ChatMessage objects themselves do not reliably retain a model identifier,
    # so timeline membership—not a guessed field name—is the primary classifier.
    target_timeline_messages, target_timeline_ref_count = timeline_messages("target")
    auditor_timeline_messages, auditor_timeline_ref_count = timeline_messages("auditor")
    # Inspect's OpenAI-compatible writer stores the served model name (the
    # final path component) on each generated ChatMessageAssistant.
    target_served_name = target_model.rsplit("/", 1)[-1]
    auditor_served_name = auditor_model.rsplit("/", 1)[-1]
    target = [
        obj for obj in stored_messages
        if str(obj.get("role") or "") == "assistant"
        and str(obj.get("model") or "") == target_served_name
    ]
    auditor = [
        obj for obj in stored_messages
        if str(obj.get("role") or "") == "assistant"
        and str(obj.get("model") or "") == auditor_served_name
    ]
    judge = []

    def explicit_event_models(event: dict[str, Any]) -> set[str]:
        values: set[str] = set()
        for value in (event.get("model"),):
            if isinstance(value, str):
                values.add(value)
        output_value = event.get("output")
        if isinstance(output_value, dict) and isinstance(output_value.get("model"), str):
            values.add(output_value["model"])
        call = event.get("call")
        if isinstance(call, dict):
            for side in ("request", "response"):
                side_value = call.get(side)
                if isinstance(side_value, dict) and isinstance(side_value.get("model"), str):
                    values.add(side_value["model"])
        return values

    def value_present(value: Any) -> bool:
        return value not in (None, "", [], {})

    raw_target_calls = 0
    raw_target_calls_with_reasoning = 0
    raw_target_calls_with_content = 0
    raw_target_calls_with_both = 0
    raw_target_calls_with_tool_calls = 0
    raw_target_reasoning_types: Counter[str] = Counter()
    raw_target_content_types: Counter[str] = Counter()
    raw_target_response_block_types: Counter[str] = Counter()
    normalized_target_output_block_types: Counter[str] = Counter()
    target_request_configs: Counter[str] = Counter()
    event_model_counts: Counter[str] = Counter()
    events_value = sample.get("events") if isinstance(sample, dict) else None
    for event in events_value if isinstance(events_value, list) else []:
        if not isinstance(event, dict):
            continue
        models = explicit_event_models(event)
        event_model_counts.update(models)
        target_event = any(
            model == target_served_name
            or model.endswith("/" + target_served_name)
            or target_served_name in model.split("/")[-1]
            for model in models
        )
        if not target_event:
            continue
        call = event.get("call")
        request = call.get("request") if isinstance(call, dict) else None
        if isinstance(request, dict):
            tools_value = request.get("tools", []) or []
            tool_parameter_counts = []
            for tool in tools_value if isinstance(tools_value, list) else []:
                if not isinstance(tool, dict):
                    continue
                function = tool.get("function") if isinstance(tool.get("function"), dict) else tool
                parameters = function.get("parameters") if isinstance(function, dict) else None
                properties = parameters.get("properties") if isinstance(parameters, dict) else None
                tool_parameter_counts.append(len(properties) if isinstance(properties, dict) else 0)
            config = {
                key: request.get(key)
                for key in (
                    "temperature", "top_p", "max_tokens", "max_completion_tokens",
                    "max_output_tokens", "seed", "tool_choice", "reasoning",
                    "frequency_penalty", "presence_penalty",
                )
                if key in request
            }
            config["tools_count"] = len(tools_value) if isinstance(tools_value, list) else None
            config["tool_parameter_counts"] = sorted(tool_parameter_counts)
            config["request_keys"] = sorted(request)
            target_request_configs[json.dumps(config, sort_keys=True, default=str)] += 1
        response = call.get("response") if isinstance(call, dict) else None
        choices = response.get("choices") if isinstance(response, dict) else None
        if isinstance(choices, list):
            for choice in choices:
                message = choice.get("message") if isinstance(choice, dict) else None
                if not isinstance(message, dict):
                    continue
                raw_target_calls += 1
                reasoning = message.get("reasoning")
                content = message.get("content")
                tool_calls = message.get("tool_calls")
                has_reasoning = value_present(reasoning)
                has_content = value_present(content)
                raw_target_calls_with_reasoning += int(has_reasoning)
                raw_target_calls_with_content += int(has_content)
                raw_target_calls_with_both += int(has_reasoning and has_content)
                if has_reasoning:
                    raw_target_reasoning_types[type(reasoning).__name__] += 1
                if has_content:
                    raw_target_content_types[type(content).__name__] += 1
                if isinstance(tool_calls, list) and tool_calls:
                    raw_target_calls_with_tool_calls += 1
        response_output = response.get("output") if isinstance(response, dict) else None
        if isinstance(response_output, list):
            for item in response_output:
                if not isinstance(item, dict):
                    continue
                for block in item.get("content", []) if isinstance(item.get("content"), list) else []:
                    if isinstance(block, dict):
                        raw_target_response_block_types[str(block.get("type", "dict"))] += 1
        normalized = event.get("output")
        normalized_choices = normalized.get("choices") if isinstance(normalized, dict) else None
        if isinstance(normalized_choices, list):
            for choice in normalized_choices:
                message = choice.get("message") if isinstance(choice, dict) else None
                content = message.get("content") if isinstance(message, dict) else None
                if isinstance(content, list):
                    for block in content:
                        if isinstance(block, dict):
                            normalized_target_output_block_types[str(block.get("type", "dict"))] += 1

    block_counts: Counter[str] = Counter()
    representation_counts: Counter[str] = Counter()
    reasoning_messages = 0
    text_messages = 0
    separate_reasoning_and_text_messages = 0
    markup_messages = 0
    auxiliary_reasoning_messages = 0
    target_message_key_sets: Counter[tuple[str, ...]] = Counter()
    target_block_key_sets: Counter[tuple[str, ...]] = Counter()
    for obj in target:
        target_message_key_sets[tuple(sorted(str(key) for key in obj))] += 1
        rep, types, markup = block_signature(obj.get("content"))
        representation_counts[rep] += 1
        block_counts.update(types)
        for block in obj.get("content", []) if isinstance(obj.get("content"), list) else []:
            if isinstance(block, dict):
                target_block_key_sets[tuple(sorted(str(key) for key in block))] += 1
        auxiliary_reasoning = any(
            key in obj and obj.get(key) not in (None, "", [], {})
            for key in ("reasoning", "reasoning_content", "analysis", "thinking")
        )
        has_reasoning = any(t in {"reasoning", "thinking", "analysis"} for t in types) or auxiliary_reasoning
        has_text = any(t in {"text", "output_text"} for t in types)
        reasoning_messages += int(has_reasoning)
        text_messages += int(has_text)
        separate_reasoning_and_text_messages += int(has_reasoning and has_text)
        markup_messages += int(markup)
        auxiliary_reasoning_messages += int(auxiliary_reasoning)

    timelines = sample.get("timelines") if isinstance(sample, dict) else None
    timeline_names = []
    timeline_root_content_counts = []
    if isinstance(timelines, list):
        for timeline in timelines:
            if not isinstance(timeline, dict):
                continue
            timeline_names.append(str(timeline.get("name")))
            root = timeline.get("root")
            content = root.get("content") if isinstance(root, dict) else None
            timeline_root_content_counts.append(len(content) if isinstance(content, list) else None)

    return {
        "unique_message_count": len(messages),
        "target_assistant_message_count": len(target),
        "auditor_model_message_count": len(auditor),
        "judge_model_message_count": len(judge),
        "target_content_representations": dict(sorted(representation_counts.items())),
        "target_content_block_types": dict(sorted(block_counts.items())),
        "target_messages_with_reasoning_block": reasoning_messages,
        "target_messages_with_text_block": text_messages,
        "target_messages_with_separate_reasoning_and_text_blocks": separate_reasoning_and_text_messages,
        "target_string_messages_with_think_markup": markup_messages,
        "target_messages_with_auxiliary_reasoning_field": auxiliary_reasoning_messages,
        "target_message_key_sets": [
            {"keys": list(keys), "count": count}
            for keys, count in sorted(target_message_key_sets.items())
        ],
        "target_content_block_key_sets": [
            {"keys": list(keys), "count": count}
            for keys, count in sorted(target_block_key_sets.items())
        ],
        "timeline_names": sorted(timeline_names),
        "timeline_root_content_counts": timeline_root_content_counts,
        "event_class_counts": dict(sorted(event_classes.items())),
        "target_timeline_event_ref_count": target_timeline_ref_count,
        "auditor_timeline_event_ref_count": auditor_timeline_ref_count,
        "stored_message_model_role_counts": [
            {"role": role, "model": model, "source": source, "count": count}
            for (role, model, source), count in sorted(stored_model_role_counts.items())
        ],
        "event_model_counts": dict(sorted(event_model_counts.items())),
        "raw_target_call_structure": {
            "choice_message_count": raw_target_calls,
            "with_reasoning": raw_target_calls_with_reasoning,
            "with_content": raw_target_calls_with_content,
            "with_both": raw_target_calls_with_both,
            "with_tool_calls": raw_target_calls_with_tool_calls,
            "reasoning_value_types": dict(sorted(raw_target_reasoning_types.items())),
            "content_value_types": dict(sorted(raw_target_content_types.items())),
            "response_output_block_types": dict(sorted(raw_target_response_block_types.items())),
            "normalized_output_block_types": dict(sorted(normalized_target_output_block_types.items())),
            "request_config_counts": [
                {"config": json.loads(config), "count": count}
                for config, count in sorted(target_request_configs.items())
            ],
        },
    }


def select_canonical(audit_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    selected = []
    for row in audit_rows:
        path = row.get("path", "")
        header = row.get("header") or {}
        roles = header.get("model_roles") or {}
        if "selfpres_logs/" not in path:
            continue
        if row.get("sample_member_count") != 36 or header.get("status") != "success":
            continue
        if (roles.get("auditor") or {}).get("model") != CANONICAL_AUDITOR:
            continue
        if (roles.get("judge") or {}).get("model") != CANONICAL_JUDGE:
            continue
        if (header.get("plan_config") or {}).get("max_connections") != CANONICAL_CONNECTIONS:
            continue
        selected.append(row)
    if len(selected) != 10:
        raise RuntimeError(f"expected 10 canonical main-suite archives, found {len(selected)}")
    return sorted(selected, key=lambda row: row["path"])


def summarize_run(archive: Path, row: dict[str, Any]) -> dict[str, Any]:
    header = row["header"]
    roles = header["model_roles"]
    target_model = roles["target"]["model"]
    auditor_model = roles["auditor"]["model"]
    judge_model = roles["judge"]["model"]
    with zipfile.ZipFile(archive) as zipped:
        members = sorted(name for name in zipped.namelist() if name.startswith("samples/") and name.endswith(".json"))

    samples = [classify_sample(extract_json(archive, member), target_model, auditor_model, judge_model) for member in members]
    totals: Counter[str] = Counter()
    target_reps: Counter[str] = Counter()
    target_blocks: Counter[str] = Counter()
    timeline_sets: Counter[tuple[str, ...]] = Counter()
    samples_with_target = 0
    samples_with_reasoning = 0
    samples_with_visible_text = 0
    samples_with_separate_channels = 0
    samples_with_markup = 0
    samples_with_raw_target_reasoning = 0
    samples_with_raw_target_content = 0
    samples_with_raw_target_both = 0
    raw_target_call_totals: Counter[str] = Counter()
    raw_reasoning_types: Counter[str] = Counter()
    raw_content_types: Counter[str] = Counter()
    raw_response_blocks: Counter[str] = Counter()
    normalized_output_blocks: Counter[str] = Counter()
    request_configs: Counter[str] = Counter()
    target_call_count_distribution: Counter[int] = Counter()
    for sample in samples:
        for key in (
            "unique_message_count", "target_assistant_message_count",
            "auditor_model_message_count", "judge_model_message_count",
            "target_messages_with_reasoning_block", "target_messages_with_text_block",
            "target_messages_with_separate_reasoning_and_text_blocks",
            "target_string_messages_with_think_markup",
            "target_messages_with_auxiliary_reasoning_field",
        ):
            totals[key] += sample[key]
        target_reps.update(sample["target_content_representations"])
        target_blocks.update(sample["target_content_block_types"])
        timeline_sets[tuple(sample["timeline_names"])] += 1
        samples_with_target += int(sample["target_assistant_message_count"] > 0)
        samples_with_reasoning += int(sample["target_messages_with_reasoning_block"] > 0)
        samples_with_visible_text += int(sample["target_messages_with_text_block"] > 0)
        samples_with_separate_channels += int(sample["target_messages_with_separate_reasoning_and_text_blocks"] > 0)
        samples_with_markup += int(sample["target_string_messages_with_think_markup"] > 0)
        raw = sample["raw_target_call_structure"]
        samples_with_raw_target_reasoning += int(raw["with_reasoning"] > 0)
        samples_with_raw_target_content += int(raw["with_content"] > 0)
        samples_with_raw_target_both += int(raw["with_both"] > 0)
        for key in ("choice_message_count", "with_reasoning", "with_content", "with_both", "with_tool_calls"):
            raw_target_call_totals[key] += raw[key]
        raw_reasoning_types.update(raw["reasoning_value_types"])
        raw_content_types.update(raw["content_value_types"])
        raw_response_blocks.update(raw["response_output_block_types"])
        normalized_output_blocks.update(raw["normalized_output_block_types"])
        target_call_count_distribution[raw["choice_message_count"]] += 1
        for item in raw["request_config_counts"]:
            request_configs[json.dumps(item["config"], sort_keys=True)] += item["count"]

    rel = row["path"]
    folder = Path(rel).parent.name
    if folder == "base":
        condition, seed = "base", ""
    else:
        match = re.fullmatch(r"selfpres__(one_shot|rewrite|strip)__seed(42|43|44)_", folder)
        if not match:
            raise RuntimeError(f"unexpected canonical folder: {folder}")
        condition, seed = match.groups()

    return {
        "path": rel,
        "condition": condition,
        "seed": seed,
        "eval_id": header.get("eval_id"),
        "run_id": header.get("run_id"),
        "sample_count": len(samples),
        "target_model": target_model,
        "auditor_model": auditor_model,
        "judge_model": judge_model,
        "sample_presence": {
            "with_target_assistant_message": samples_with_target,
            "with_reasoning_block": samples_with_reasoning,
            "with_visible_text_block": samples_with_visible_text,
            "with_separate_reasoning_and_text_blocks": samples_with_separate_channels,
            "with_string_think_markup": samples_with_markup,
            "with_raw_target_reasoning": samples_with_raw_target_reasoning,
            "with_raw_target_content": samples_with_raw_target_content,
            "with_raw_target_reasoning_and_content": samples_with_raw_target_both,
        },
        "message_totals": dict(sorted(totals.items())),
        "target_content_representations": dict(sorted(target_reps.items())),
        "target_content_block_types": dict(sorted(target_blocks.items())),
        "timeline_name_sets": [
            {"names": list(names), "sample_count": count}
            for names, count in sorted(timeline_sets.items())
        ],
        "raw_target_call_structure": {
            **dict(sorted(raw_target_call_totals.items())),
            "reasoning_value_types": dict(sorted(raw_reasoning_types.items())),
            "content_value_types": dict(sorted(raw_content_types.items())),
            "response_output_block_types": dict(sorted(raw_response_blocks.items())),
            "normalized_output_block_types": dict(sorted(normalized_output_blocks.items())),
            "request_config_counts": [
                {"config": json.loads(config), "count": count}
                for config, count in sorted(request_configs.items())
            ],
        },
        "target_call_count_per_sample_distribution": {
            str(count): sample_count
            for count, sample_count in sorted(target_call_count_distribution.items())
        },
        "_sample_target_call_counts": {
            member: sample["raw_target_call_structure"]["choice_message_count"]
            for member, sample in zip(members, samples)
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive-root", required=True, type=Path)
    parser.add_argument("--archive-audit", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    root = args.archive_root.resolve()
    audit_rows = json.loads(args.archive_audit.read_text(encoding="utf-8"))
    selected = select_canonical(audit_rows)
    runs = [summarize_run(root / row["path"], row) for row in selected]
    member_sets = [set(run["_sample_target_call_counts"]) for run in runs]
    identical_member_sets = all(members == member_sets[0] for members in member_sets[1:])
    different_turn_counts = 0
    if identical_member_sets:
        for member in member_sets[0]:
            counts = {run["_sample_target_call_counts"][member] for run in runs}
            different_turn_counts += int(len(counts) > 1)
    for run in runs:
        run.pop("_sample_target_call_counts")
    output = {
        "guardrail": "No substantive content or score values emitted.",
        "selection": "success; 36 samples; GPT-5.4-mini auditor and judge; max_connections=40",
        "canonical_run_count": len(runs),
        "canonical_sample_count": sum(run["sample_count"] for run in runs),
        "matched_suite_structure": {
            "identical_sample_member_sets": identical_member_sets,
            "sample_members_per_run": len(member_sets[0]) if member_sets else 0,
            "scenarios_with_nonidentical_target_turn_count_across_runs": different_turn_counts,
        },
        "runs": runs,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"runs": len(runs), "samples": output["canonical_sample_count"]}))


if __name__ == "__main__":
    main()
