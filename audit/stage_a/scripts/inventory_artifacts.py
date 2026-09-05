#!/usr/bin/env python3
"""Metadata-only inventory for the C-05 Stage A audit.

This script never opens artifact files. It records filesystem metadata and an
access policy inferred conservatively from paths and suffixes.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
from collections import Counter
from pathlib import Path


SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache"}
WEIGHT_SUFFIXES = {".safetensors", ".bin", ".pt", ".pth"}
NOTEBOOK_SUFFIXES = {".ipynb"}


def classify(rel: str, suffix: str) -> tuple[str, str]:
    low = rel.lower().replace("\\", "/")
    if suffix in WEIGHT_SUFFIXES:
        return "adapter_weight", "LIST_STAT_ONLY_NEVER_OPEN"
    if suffix in NOTEBOOK_SUFFIXES:
        return "notebook", "LIST_ONLY_NO_RAW_JSON_NO_EXECUTION"
    if "adapter_config.json" in low:
        return "adapter_metadata", "TEXT_ALLOWED"
    if any(token in low for token in ("manifest", "provenance", "schema", "readme")):
        return "metadata", "TEXT_ALLOWED_SUBJECT_TO_GRANULARITY_CHECK"
    if any(token in low for token in ("scenario", "questions", "seed_prompts")):
        return "scenario_or_eval_input", "STRUCTURE_ONLY_A1_NO_SCENARIO_TEXT"
    if any(token in low for token in ("eval", "result", "rollout", "transcript", "log")):
        return "possible_evaluation_output", "STRUCTURE_ONLY_NO_RECORD_VALUES"
    if any(token in low for token in ("train", "rewrite", "stripped", "one_shot", "oneshot")):
        return "training_or_recipe", "PROVENANCE_AND_CODE_ONLY_A1"
    if suffix in {".py", ".sh", ".ps1", ".yaml", ".yml", ".toml", ".md", ".txt"}:
        return "source_or_documentation", "TEXT_ALLOWED_AFTER_CLASSIFICATION"
    if suffix in {".json", ".jsonl", ".csv", ".parquet"}:
        return "structured_unknown", "STRUCTURE_ONLY_UNTIL_CLASSIFIED"
    return "other", "LIST_ONLY_UNTIL_CLASSIFIED"


def walk(root: Path):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        base = Path(dirpath)
        for name in sorted(filenames):
            path = base / name
            stat = path.stat()
            rel = path.relative_to(root).as_posix()
            suffix = path.suffix.lower()
            category, policy = classify(rel, suffix)
            yield {
                "root": root.name,
                "relative_path": rel,
                "suffix": suffix,
                "size_bytes": stat.st_size,
                "category": category,
                "access_policy": policy,
            }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", action="append", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--summary", required=True, type=Path)
    args = parser.parse_args()

    records = []
    for root in args.root:
        if not root.is_dir():
            raise SystemExit(f"Missing artifact root: {root}")
        records.extend(walk(root.resolve()))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, sort_keys=True) + "\n")

    counts = Counter((r["root"], r["category"], r["access_policy"]) for r in records)
    args.summary.parent.mkdir(parents=True, exist_ok=True)
    with args.summary.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["root", "category", "access_policy", "file_count"])
        for (root, category, policy), count in sorted(counts.items()):
            writer.writerow([root, category, policy, count])

    print(json.dumps({"files": len(records), "roots": [str(r) for r in args.root]}))


if __name__ == "__main__":
    main()
