#!/usr/bin/env python3
"""Hard-blind structural audit of Inspect ``.eval`` archives.

Uses the system ``tar`` implementation solely to decompress named JSON members.
No substantive message text, reasoning text, judge rationale, scenario text, or
score value is emitted. Only configuration/provenance allowlists and structural
counts are retained.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import zipfile
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable


CONTENT_KEYS = {
    "content", "text", "reasoning", "reasoning_content", "analysis",
    "answer", "target", "explanation", "rationale", "input", "prompt",
    "system_message", "seed_instructions", "completion", "output_text",
}


def extract_json(archive: Path, member: str) -> Any:
    proc = subprocess.run(
        ["tar", "-xOf", str(archive), member],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"tar extraction failed for member {member}")
    try:
        return json.loads(proc.stdout)
    except Exception as exc:
        raise RuntimeError(f"JSON parse failed for member {member}: {type(exc).__name__}") from None


def get(obj: Any, path: Iterable[str], default: Any = None) -> Any:
    for key in path:
        if not isinstance(obj, dict) or key not in obj:
            return default
        obj = obj[key]
    return obj


def safe_header(header: dict[str, Any]) -> dict[str, Any]:
    eval_obj = header.get("eval", {})
    task_args = eval_obj.get("task_args", {})
    dataset = eval_obj.get("dataset", {})
    config = eval_obj.get("config", {})
    plan = header.get("plan", {})
    results = header.get("results", {})
    stats = header.get("stats", {})

    roles = {}
    for role, details in eval_obj.get("model_roles", {}).items():
        if isinstance(details, dict):
            roles[role] = {
                "model": details.get("model"),
                "base_url_present": bool(details.get("base_url")),
                "config_keys": sorted((details.get("config") or {}).keys()),
                "arg_keys": sorted((details.get("args") or {}).keys()),
            }

    solver_steps = []
    for step in plan.get("steps", []) if isinstance(plan, dict) else []:
        if not isinstance(step, dict):
            continue
        params = step.get("params", {}) or {}
        auditor = params.get("auditor", {}) if isinstance(params, dict) else {}
        auditor_params = auditor.get("params", {}) if isinstance(auditor, dict) else {}
        tools = []
        for tool in auditor_params.get("tools", []) if isinstance(auditor_params, dict) else []:
            if isinstance(tool, dict):
                tools.append({
                    "name": tool.get("name"),
                    "param_keys": sorted((tool.get("params") or {}).keys()),
                })
        solver_steps.append({
            "solver": step.get("solver"),
            "auditor_type": auditor.get("type") if isinstance(auditor, dict) else None,
            "auditor_name": auditor.get("name") if isinstance(auditor, dict) else None,
            "max_turns": auditor_params.get("max_turns") if isinstance(auditor_params, dict) else None,
            "compaction": auditor_params.get("compaction") if isinstance(auditor_params, dict) else None,
            "realism_filter": auditor_params.get("realism_filter") if isinstance(auditor_params, dict) else None,
            "turn_counter": auditor_params.get("turn_counter") if isinstance(auditor_params, dict) else None,
            "auditor_tools": tools,
        })

    score_completion = []
    for score in results.get("scores", []) if isinstance(results, dict) else []:
        if isinstance(score, dict):
            score_completion.append({
                "name": score.get("name"),
                "scorer": score.get("scorer"),
                "scored_samples": score.get("scored_samples"),
                "unscored_samples": score.get("unscored_samples"),
            })

    return {
        "archive_version": header.get("version"),
        "status": header.get("status"),
        "eval_id": eval_obj.get("eval_id"),
        "run_id": eval_obj.get("run_id"),
        "created": eval_obj.get("created"),
        "task": eval_obj.get("task"),
        "task_id": eval_obj.get("task_id"),
        "task_version": eval_obj.get("task_version"),
        "task_registry_name": eval_obj.get("task_registry_name"),
        "task_args": {
            key: task_args.get(key)
            for key in (
                "behavior", "max_turns", "enable_prefill", "enable_rollback",
                "compaction", "realism_filter", "approval", "turn_counter",
            )
        },
        "dataset": {
            "name": dataset.get("name"),
            "samples": dataset.get("samples"),
            "sample_id_count": len(dataset.get("sample_ids", []) or []),
            "shuffled": dataset.get("shuffled"),
        },
        "model": eval_obj.get("model"),
        "model_generate_config": eval_obj.get("model_generate_config"),
        "model_arg_keys": sorted((eval_obj.get("model_args") or {}).keys()),
        "model_roles": roles,
        "eval_config": {
            key: config.get(key)
            for key in (
                "epochs", "epochs_reducer", "fail_on_error", "continue_on_fail",
                "score_on_error", "log_samples", "log_realtime", "log_shared",
            )
        },
        "packages": eval_obj.get("packages", {}),
        "behavior_metadata": {
            "name": get(eval_obj, ("metadata", "behavior", "name")),
            "num_scenarios": get(eval_obj, ("metadata", "behavior", "num_scenarios")),
            "modality": get(eval_obj, ("metadata", "behavior", "modality")),
            "variation_keys": sorted((get(eval_obj, ("metadata", "behavior", "variations"), {}) or {}).keys()),
            "instruction_keys": sorted((get(eval_obj, ("metadata", "behavior", "instructions"), {}) or {}).keys()),
            "example_count": len(get(eval_obj, ("metadata", "behavior", "examples"), []) or []),
        },
        "solver_steps": solver_steps,
        "plan_config": {
            "max_connections": get(plan, ("config", "max_connections")),
        },
        "results_completion": {
            "total_samples": results.get("total_samples") if isinstance(results, dict) else None,
            "completed_samples": results.get("completed_samples") if isinstance(results, dict) else None,
            "score_completion": score_completion,
        },
        "stats": {
            "started_at": stats.get("started_at") if isinstance(stats, dict) else None,
            "completed_at": stats.get("completed_at") if isinstance(stats, dict) else None,
            "connection_limit_event_count": len(stats.get("connection_limit_history", []) or []) if isinstance(stats, dict) else None,
        },
        "invalidated": header.get("invalidated"),
        "tags": header.get("tags"),
    }


def walk_schema(value: Any, path: str, counts: dict[str, Counter[str]]) -> None:
    counts[path][type(value).__name__] += 1
    if isinstance(value, dict):
        for key, child in value.items():
            next_path = f"{path}.{key}"
            if key in CONTENT_KEYS:
                counts[next_path]["REDACTED_VALUE"] += 1
                if isinstance(child, list):
                    for item in child:
                        walk_schema(item, next_path + "[]", counts)
                elif isinstance(child, dict):
                    walk_schema(child, next_path, counts)
                continue
            walk_schema(child, next_path, counts)
    elif isinstance(value, list):
        for child in value:
            walk_schema(child, path + "[]", counts)


def message_metadata(value: Any, out: Counter[tuple[str, str, str, str]]) -> None:
    if isinstance(value, dict):
        if "role" in value and "content" in value:
            role = str(value.get("role"))
            source = str(value.get("source")) if value.get("source") is not None else ""
            content = value.get("content")
            content_kind = type(content).__name__
            blocks = ""
            if isinstance(content, list):
                block_types = []
                for block in content:
                    if isinstance(block, dict):
                        block_types.append(str(block.get("type", "dict")))
                    else:
                        block_types.append(type(block).__name__)
                blocks = ",".join(sorted(set(block_types)))
            out[(role, source, content_kind, blocks)] += 1
        for child in value.values():
            message_metadata(child, out)
    elif isinstance(value, list):
        for child in value:
            message_metadata(child, out)


def score_names(value: Any, out: Counter[str]) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "scores" and isinstance(child, dict):
                for name in child:
                    out[str(name)] += 1
            score_names(child, out)
    elif isinstance(value, list):
        for child in value:
            score_names(child, out)


def audit_archive(path: Path, root: Path) -> dict[str, Any]:
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        sample_names = [name for name in names if name.startswith("samples/") and name.endswith(".json")]
        compression = dict(Counter(str(info.compress_type) for info in archive.infolist()))

    result: dict[str, Any] = {
        "path": path.relative_to(root).as_posix(),
        "size_bytes": path.stat().st_size,
        "archive_member_count": len(names),
        "sample_member_count": len(sample_names),
        "compression_methods": compression,
        "has_header": "header.json" in names,
        "has_summaries": "summaries.json" in names,
        "has_reductions": "reductions.json" in names,
        "journal_member_count": sum(name.startswith("_journal/") for name in names),
    }

    if "header.json" in names:
        result["header"] = safe_header(extract_json(path, "header.json"))
    else:
        result["header"] = None

    schema: dict[str, Counter[str]] = defaultdict(Counter)
    messages: Counter[tuple[str, str, str, str]] = Counter()
    scores: Counter[str] = Counter()
    top_statuses: Counter[str] = Counter()
    top_errors: Counter[str] = Counter()
    for member in sample_names:
        sample = extract_json(path, member)
        walk_schema(sample, "$", schema)
        message_metadata(sample, messages)
        score_names(sample, scores)
        if isinstance(sample, dict):
            top_statuses[str(sample.get("status"))] += 1
            error = sample.get("error")
            if error:
                if isinstance(error, dict):
                    top_errors[str(error.get("type") or error.get("error_type") or "dict")] += 1
                else:
                    top_errors[type(error).__name__] += 1

    result["sample_structure"] = {
        "top_status_counts": dict(top_statuses),
        "top_error_class_counts": dict(top_errors),
        "score_name_presence_counts": dict(scores),
        "message_metadata_counts": [
            {
                "role": key[0],
                "source": key[1],
                "content_container": key[2],
                "content_block_types": key[3],
                "count": count,
            }
            for key, count in sorted(messages.items())
        ],
        "schema_paths": {
            key: dict(sorted(value.items()))
            for key, value in sorted(schema.items())
        },
    }
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    root = args.root.resolve()
    archives = [audit_archive(path, root) for path in sorted(root.rglob("*.eval"))]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        json.dump(archives, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(json.dumps({"archives": len(archives), "sample_members": sum(a["sample_member_count"] for a in archives)}))


if __name__ == "__main__":
    main()
