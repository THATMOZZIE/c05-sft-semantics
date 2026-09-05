#!/usr/bin/env python3
"""Build hard-blind A1 provenance and archive-attempt mapping tables.

Reads only artifact manifests, adapter configs, training audit summaries, and
the previously redacted archive audit. It never opens an Inspect sample,
scenario body, training message body, or adapter weights.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from typing import Any


CANONICAL_AUDITOR = "openai/gpt-5.4-mini"
CANONICAL_JUDGE = "openai/gpt-5.4-mini"
CANONICAL_CONNECTIONS = 40


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def arm_from_folder(folder: str) -> tuple[str, str]:
    if folder == "base":
        return "base", ""
    match = re.fullmatch(r"selfpres__(one_shot|rewrite|strip)__seed(42|43|44)_", folder)
    if not match:
        raise ValueError(folder)
    return match.group(1), match.group(2)


def is_canonical(row: dict[str, Any]) -> bool:
    header = row.get("header") or {}
    roles = header.get("model_roles") or {}
    return (
        row.get("sample_member_count") == 36
        and header.get("status") == "success"
        and (roles.get("auditor") or {}).get("model") == CANONICAL_AUDITOR
        and (roles.get("judge") or {}).get("model") == CANONICAL_JUDGE
        and (header.get("plan_config") or {}).get("max_connections") == CANONICAL_CONNECTIONS
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", required=True, type=Path)
    parser.add_argument("--archive-audit", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    workspace = args.workspace.resolve()
    source_root = workspace / "related_research/shared_sft_lessons_across_alignment"
    code_root = source_root / "toy-models-of-sft"
    data_root = source_root / "toy-models-of-sft-data"
    adapter_root = source_root / "toy-models-of-sft-adapters"

    archive_rows = json.loads(args.archive_audit.read_text(encoding="utf-8"))
    main_rows = [row for row in archive_rows if row["path"].startswith("selfpres_logs/")]

    attempts = []
    for row in sorted(main_rows, key=lambda item: item["path"]):
        folder = Path(row["path"]).parent.name
        condition, seed = arm_from_folder(folder)
        header = row.get("header") or {}
        roles = header.get("model_roles") or {}
        canonical = is_canonical(row)
        if canonical:
            disposition = "canonical_main_suite"
        elif not row.get("has_header"):
            disposition = "partial_or_interrupted_no_header"
        else:
            disposition = "complete_noncanonical_configuration_attempt"
        completion = header.get("results_completion") or {}
        attempts.append({
            "condition": condition,
            "seed": seed,
            "archive_path": row["path"],
            "archive_has_header": row.get("has_header"),
            "header_status": header.get("status", ""),
            "sample_members": row.get("sample_member_count"),
            "completed_samples": completion.get("completed_samples", ""),
            "auditor_model": (roles.get("auditor") or {}).get("model", ""),
            "judge_model": (roles.get("judge") or {}).get("model", ""),
            "max_connections": (header.get("plan_config") or {}).get("max_connections", ""),
            "eval_id": header.get("eval_id", ""),
            "run_id": header.get("run_id", ""),
            "disposition": disposition,
            "canonical": canonical,
        })

    canonical_rows = [row for row in main_rows if is_canonical(row)]
    if len(canonical_rows) != 10:
        raise RuntimeError(f"expected 10 canonical rows, got {len(canonical_rows)}")

    file_manifest = [
        json.loads(line)
        for line in (data_root / "metadata/file_manifest.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    training_manifest = {}
    for row in file_manifest:
        match = re.search(r"arm3_(one_shot|rewrite|strip)\.jsonl$", str(row.get("dest_file", "")))
        if match and "/data_stage/" in str(row.get("dest_file", "")).replace("\\", "/"):
            training_manifest[match.group(1)] = row

    adapter_manifest = json.loads((adapter_root / "ADAPTER_MANIFEST.json").read_text(encoding="utf-8"))
    public_adapters = {}
    for row in adapter_manifest:
        path = str(row.get("public_path", ""))
        if not path.startswith("self_preservation/"):
            continue
        public_name = path.rsplit("/", 1)[-1]
        condition = "strip" if public_name == "stripped" else public_name
        public_adapters[condition] = row

    maps = []
    for row in sorted(canonical_rows, key=lambda item: item["path"]):
        folder = Path(row["path"]).parent.name
        condition, seed = arm_from_folder(folder)
        header = row["header"]
        roles = header["model_roles"]
        task_args = header.get("task_args") or {}
        behavior = header.get("behavior_metadata") or {}
        training = training_manifest.get(condition, {})
        released_adapter = public_adapters.get(condition, {}) if seed == "42" else {}
        if condition == "base":
            expected_checkpoint = "Qwen/Qwen3.5-4B (unadapted)"
            adapter_status = "not_applicable"
        else:
            expected_checkpoint = f"runs/seed-errorbars/adapters/selfpres__{condition}__seed{seed}/final"
            adapter_status = "representative_seed42_released" if seed == "42" else "seed_checkpoint_not_publicly_released"
        maps.append({
            "condition": condition,
            "training_seed": seed,
            "base_model": "Qwen/Qwen3.5-4B",
            "training_artifact": training.get("dest_file", ""),
            "training_artifact_sha256_manifest": training.get("sha256", ""),
            "training_rows": 1362 if condition != "base" else "",
            "expected_source_checkpoint": expected_checkpoint,
            "public_adapter_path": released_adapter.get("public_path", ""),
            "public_adapter_seed": "42" if released_adapter else "",
            "public_adapter_sha256_manifest": released_adapter.get("sha256", ""),
            "public_adapter_status": adapter_status,
            "eval_target_model": (roles.get("target") or {}).get("model", ""),
            "eval_archive": row["path"],
            "eval_id": header.get("eval_id"),
            "run_id": header.get("run_id"),
            "frozen_suite": task_args.get("behavior"),
            "behavior_name": behavior.get("name"),
            "modality": behavior.get("modality"),
            "requested_scenarios": behavior.get("num_scenarios"),
            "evaluated_samples": row.get("sample_member_count"),
            "auditor_model": (roles.get("auditor") or {}).get("model"),
            "judge_model": (roles.get("judge") or {}).get("model"),
            "max_turns": task_args.get("max_turns"),
            "prefill": task_args.get("enable_prefill"),
            "rollback": task_args.get("enable_rollback"),
            "petri_bloom_version": (header.get("packages") or {}).get("petri_bloom"),
            "inspect_ai_version": (header.get("packages") or {}).get("inspect_ai"),
            "aggregate_source": "journal/writeup/plot_data/figure2_richer_traits.json",
            "evidence_label": "DIRECT_SOURCE",
        })

    out = args.output_dir.resolve()
    write_csv(out / "A1_condition_seed_adapter_eval_map.csv", maps)
    write_csv(out / "A1_eval_archive_attempts.csv", attempts)
    print(json.dumps({
        "mapping_rows": len(maps),
        "attempt_rows": len(attempts),
        "canonical_samples": sum(int(row["evaluated_samples"]) for row in maps),
    }))


if __name__ == "__main__":
    main()
