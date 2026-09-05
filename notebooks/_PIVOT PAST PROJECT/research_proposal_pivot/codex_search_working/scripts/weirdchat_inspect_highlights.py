"""Print exact WeirdChat pattern records and highlight transcripts for manual review.

The script selects the highest triage-score pattern for each requested behavior,
then performs an exact transcript-id/pattern-id join against the referenced local
Parquet shard. It is an extraction utility only; interpretation remains manual.
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any

import pyarrow.parquet as pq

import weirdchat_triage as triage


def find_highlight(pattern: dict[str, Any]) -> tuple[str, dict[str, Any]]:
    hits: list[tuple[str, dict[str, Any]]] = []
    for relative_file in pattern["transcript_files"]:
        path = triage.DATASET_ROOT / relative_file
        for row in pq.read_table(path).to_pylist():
            if (
                row["transcript_id"] == pattern["highlight_transcript_id"]
                and row["pattern_id"] == pattern["pattern_id"]
                and row["is_highlight"]
            ):
                hits.append((relative_file, row))
    if len(hits) != 1:
        raise ValueError(
            f"expected one exact highlight for {pattern['pattern_id']}, got {len(hits)}"
        )
    return hits[0]


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "behaviors",
        help="Comma-separated behavior IDs, or 'all' for one top-scoring pattern per behavior",
    )
    args = parser.parse_args()

    rows = [triage.flatten(row) for row in pq.read_table(triage.DEFAULT_INPUT).to_pylist()]
    triage.validate_source_rows(rows)
    triage.score_rows(rows)
    ordered = sorted(rows, key=lambda row: (-row["triage_score"], row["pattern_id"]))
    best: dict[str, dict[str, Any]] = {}
    for row in ordered:
        best.setdefault(row["behavior_id"], row)

    requested = sorted(best) if args.behaviors == "all" else args.behaviors.split(",")
    missing = [behavior for behavior in requested if behavior not in best]
    if missing:
        raise ValueError(f"unknown/no-pattern behavior IDs: {missing}")

    for behavior in requested:
        pattern = best[behavior]
        transcript_file, transcript = find_highlight(pattern)
        record = {
            "behavior_id": behavior,
            "pattern": {
                "pattern_id": pattern["pattern_id"],
                "title": pattern["title"],
                "description": pattern["description"],
                "cluster_label": pattern["cluster_label"],
                "representative_user_text": pattern["representative_user_text"],
                "subject_model": pattern["subject_model"],
                "checkpoint": pattern["checkpoint"],
                "method": pattern["method"],
                "metrics": pattern["metrics"],
                "openrouter_replication": pattern["openrouter_replication"],
                "elo": pattern["elo"],
                "n_prompts": pattern["n_prompts"],
                "n_transcripts": pattern["n_transcripts"],
                "prompt_file": pattern["prompt_file"],
                "transcript_file": transcript_file,
                "weirdchat_url": pattern["weirdchat_url"],
                "triage_score": pattern["triage_score"],
            },
            "highlight": transcript,
        }
        print(json.dumps(record, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
