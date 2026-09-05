#!/usr/bin/env python3
"""Extract only A1-authorized aggregate anchors from Inspect headers.

The allowlist is intentionally restricted to base-model runs and the three
published evaluator-noise repeats. Treatment seed aggregates and every sample
member are out of scope and are never opened.
"""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
import zipfile
from pathlib import Path
from typing import Any


def extract_header(path: Path) -> dict[str, Any] | None:
    with zipfile.ZipFile(path) as archive:
        if "header.json" not in archive.namelist():
            return None
    proc = subprocess.run(
        ["tar", "-xOf", str(path), "header.json"],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"failed to extract header: {path}")
    return json.loads(proc.stdout)


def aggregate_value(header: dict[str, Any], score_name: str) -> float | None:
    for score in (header.get("results") or {}).get("scores", []):
        if not isinstance(score, dict) or score.get("name") != score_name:
            continue
        value = (((score.get("metrics") or {}).get("mean") or {}).get("value"))
        return float(value) if value is not None else None
    return None


def classify(rel: str) -> str | None:
    if rel.startswith("selfpres_logs/base/"):
        return "main_suite_base_attempt"
    if rel.startswith("2x2_shutdown_logs/base/"):
        return "figure4_2x2_base_attempt"
    if rel.startswith("noisefloor/"):
        return "published_noise_repeat"
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    rows = []
    for path in sorted(root.rglob("*.eval")):
        rel = path.relative_to(root).as_posix()
        group = classify(rel)
        if group is None:
            continue
        header = extract_header(path)
        if header is None:
            rows.append({
                "group": group, "path": rel, "status": "no_header",
                "eval_id": "", "run_id": "", "completed_samples": "",
                "aggregate_self_preservation_behavior": "",
            })
            continue
        results = header.get("results") or {}
        rows.append({
            "group": group,
            "path": rel,
            "status": header.get("status"),
            "eval_id": (header.get("eval") or {}).get("eval_id"),
            "run_id": (header.get("eval") or {}).get("run_id"),
            "completed_samples": results.get("completed_samples"),
            "aggregate_self_preservation_behavior": aggregate_value(header, "self_preservation_behavior"),
        })
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(json.dumps({"authorized_header_rows": len(rows)}))


if __name__ == "__main__":
    main()
