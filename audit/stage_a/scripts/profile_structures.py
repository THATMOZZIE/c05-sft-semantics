#!/usr/bin/env python3
"""Content-suppressing structural profiler for Stage A artifacts.

The profiler parses supported structured files but emits only key paths, value
types, null counts, container lengths, row counts, and column names. It never
emits string or numeric record values. Weight files and notebooks are refused.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


REFUSED_SUFFIXES = {".safetensors", ".bin", ".pt", ".pth", ".ipynb"}


class Profile:
    def __init__(self) -> None:
        self.types: dict[str, Counter[str]] = defaultdict(Counter)
        self.nulls: Counter[str] = Counter()
        self.list_lengths: dict[str, Counter[int]] = defaultdict(Counter)

    def visit(self, value: Any, path: str = "$") -> None:
        kind = type(value).__name__
        self.types[path][kind] += 1
        if value is None:
            self.nulls[path] += 1
        elif isinstance(value, dict):
            for key, child in value.items():
                self.visit(child, f"{path}.{key}")
        elif isinstance(value, list):
            self.list_lengths[path][len(value)] += 1
            for child in value:
                self.visit(child, f"{path}[]")

    def export(self) -> dict[str, Any]:
        return {
            "paths": {
                path: {
                    "types": dict(sorted(counts.items())),
                    "null_count": self.nulls[path],
                    "list_lengths": dict(sorted(self.list_lengths[path].items())),
                }
                for path, counts in sorted(self.types.items())
            }
        }


def profile_json(path: Path) -> dict[str, Any]:
    profile = Profile()
    with path.open("r", encoding="utf-8") as handle:
        profile.visit(json.load(handle))
    result = profile.export()
    result["record_count"] = 1
    return result


def profile_jsonl(path: Path) -> dict[str, Any]:
    profile = Profile()
    count = 0
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                value = json.loads(line)
            except Exception as exc:
                raise ValueError(f"parse failure at record {line_number}: {type(exc).__name__}") from None
            profile.visit(value)
            count += 1
    result = profile.export()
    result["record_count"] = count
    return result


def profile_delimited(path: Path, delimiter: str) -> dict[str, Any]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle, delimiter=delimiter)
        try:
            columns = next(reader)
        except StopIteration:
            return {"record_count": 0, "column_count": 0, "columns": []}
        rows = sum(1 for _ in reader)
    return {"record_count": rows, "column_count": len(columns), "columns": columns}


def profile_file(path: Path) -> dict[str, Any]:
    suffix = path.suffix.lower()
    if suffix in REFUSED_SUFFIXES:
        raise ValueError(f"refused suffix: {suffix}")
    if suffix == ".json":
        result = profile_json(path)
    elif suffix == ".jsonl":
        result = profile_jsonl(path)
    elif suffix == ".csv":
        result = profile_delimited(path, ",")
    elif suffix == ".tsv":
        result = profile_delimited(path, "\t")
    else:
        raise ValueError(f"unsupported suffix: {suffix}")
    return {"path": path.as_posix(), "size_bytes": path.stat().st_size, **result}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    results = []
    for path in args.paths:
        try:
            results.append({"status": "ok", **profile_file(path)})
        except Exception as exc:
            results.append({
                "status": "error",
                "path": path.as_posix(),
                "error_class": type(exc).__name__,
                "error": str(exc),
            })

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        json.dump(results, handle, indent=2, sort_keys=True)
        handle.write("\n")

    print(json.dumps({
        "files": len(results),
        "ok": sum(r["status"] == "ok" for r in results),
        "errors": sum(r["status"] == "error" for r in results),
    }))


if __name__ == "__main__":
    main()
