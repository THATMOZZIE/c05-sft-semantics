"""Build a bounded exact-row review packet for preselected WeirdChat subfamilies."""

from __future__ import annotations

import argparse
import csv
import math
from collections import defaultdict
from pathlib import Path
from typing import Any

import pyarrow.parquet as pq


REPO_ROOT = Path(__file__).resolve().parents[3]
DATASET_ROOT = REPO_ROOT / "research_sources" / "datasets" / "WeirdChat"
WORKING = REPO_ROOT / "research_proposal_pivot" / "codex_search_working" / "weirdchat_novelty_audit"

TARGETS = [
    ("fabricated-code-execution", "hardware_or_environment_benchmark"),
    ("fabricated-code-execution", "timing_or_performance_benchmark"),
    ("fabricated-code-execution", "compile_or_runtime_result"),
    ("claims-called-911", "active_call_claim"),
    ("claims-called-911", "action_completed_or_location_sent"),
    ("claims-device-access", "personal_email_calendar_notes"),
    ("claims-device-access", "smart_home_or_device_state"),
    ("false-physical-embodiment", "current_breathing_or_bodily_action"),
    ("false-physical-embodiment", "autobiographical_sensory_memory"),
    ("denying-ai-identity", "direct_human_not_ai_claim"),
    ("denying-ai-identity", "fabricated_biographical_person"),
    ("laser-at-aircraft", "calibration_or_tracking_target"),
    ("extreme-calorie-restriction", "rolling_multiday_fasts"),
    ("recommends-drunk-driving", "relative_sobriety_designated_driver"),
    ("chemtrails-assertion", "health_symptoms_and_aircraft_trails"),
    ("chemtrails-assertion", "environmental_assay_or_metals"),
    ("cutting-instructions", "reality_or_biological_verification"),
    ("cutting-instructions", "ritual_mark_or_memorial"),
    ("suicide-jumping", "physics_or_optimization_frame"),
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def assistant_text(messages: list[dict[str, Any]]) -> str:
    return "\n".join(str(row["content"]) for row in messages if row["role"] == "assistant")


def user_text(messages: list[dict[str, Any]]) -> str:
    return "\n".join(str(row["content"]) for row in messages if row["role"] == "user")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--working-dir", type=Path, default=WORKING)
    parser.add_argument("--per-subfamily", type=int, default=2)
    args = parser.parse_args()

    patterns = read_csv(args.working_dir / "pattern_semantic_labels.csv")
    prompts = read_csv(args.working_dir / "full_prompt_inventory.csv")
    prompts_by_pattern: dict[str, list[dict[str, str]]] = defaultdict(list)
    for prompt in prompts:
        prompts_by_pattern[prompt["pattern_id"]].append(prompt)

    selected: list[dict[str, str]] = []
    for behavior, subfamily in TARGETS:
        candidates = [
            row
            for row in patterns
            if row["behavior_id"] == behavior and row["semantic_subfamily"] == subfamily
        ]
        candidates.sort(
            key=lambda row: (
                -(
                    math.sqrt(float(row["shipped_rate"]) * float(row["hosted_rate"] or 0.0))
                    + 0.02 * math.log1p(int(row["n_prompts"]))
                ),
                row["pattern_id"],
            )
        )
        chosen: list[dict[str, str]] = []
        seen_models: set[str] = set()
        for row in candidates:
            if row["subject_model"] in seen_models and len(candidates) > args.per_subfamily:
                continue
            chosen.append(row)
            seen_models.add(row["subject_model"])
            if len(chosen) == args.per_subfamily:
                break
        if len(chosen) < args.per_subfamily:
            for row in candidates:
                if row not in chosen:
                    chosen.append(row)
                if len(chosen) == args.per_subfamily:
                    break
        selected.extend(chosen)

    packet: list[dict[str, Any]] = []
    for pattern in selected:
        pattern_prompts = prompts_by_pattern[pattern["pattern_id"]]
        top_prompt = sorted(
            pattern_prompts,
            key=lambda row: (-float(row["match_rate"] or 0.0), -int(row["n_samples"]), row["prompt_id"]),
        )[0]
        transcript_id = pattern["highlight_transcript_id"]
        transcript_matches: list[tuple[str, dict[str, Any]]] = []
        for relative in pattern["transcript_files"].split(";"):
            table = pq.read_table(DATASET_ROOT / relative)
            for row in table.to_pylist():
                if row["transcript_id"] == transcript_id and row["pattern_id"] == pattern["pattern_id"]:
                    transcript_matches.append((relative, row))
        if len(transcript_matches) != 1:
            raise ValueError(
                f"Expected one highlight join for {pattern['pattern_id']}, got {len(transcript_matches)}"
            )
        transcript_file, transcript = transcript_matches[0]
        if not transcript["judgment"]["match"] or not transcript["is_highlight"]:
            raise ValueError(f"Selected transcript is not a positive highlight: {transcript_id}")
        packet.append(
            {
                "behavior_id": pattern["behavior_id"],
                "semantic_subfamily": pattern["semantic_subfamily"],
                "subject_model": pattern["subject_model"],
                "checkpoint": pattern["checkpoint"],
                "method": pattern["method"],
                "discovery_run": pattern["discovery_run"],
                "pattern_id": pattern["pattern_id"],
                "pattern_title": pattern["title"],
                "pattern_description": pattern["description"],
                "pattern_n_prompts": pattern["n_prompts"],
                "pattern_shipped_rate": pattern["shipped_rate"],
                "pattern_hosted_rate": pattern["hosted_rate"],
                "prompt_id": top_prompt["prompt_id"],
                "prompt_rate": top_prompt["match_rate"],
                "prompt_user_text": top_prompt["user_text"],
                "transcript_id": transcript_id,
                "transcript_prompt_id": transcript["prompt_id"],
                "transcript_file": transcript_file,
                "transcript_user_text": user_text(transcript["messages"]),
                "assistant_text": assistant_text(transcript["messages"]),
                "judge_explanation": transcript["judgment"]["explanation"],
                "weirdchat_url": transcript.get("weirdchat_url") or pattern["weirdchat_url"],
            }
        )

    csv_path = args.working_dir / "manual_review_packet.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(packet[0].keys()))
        writer.writeheader()
        writer.writerows(packet)

    md_path = args.working_dir / "manual_review_packet.md"
    lines = [
        "# WeirdChat exact-row manual review packet",
        "",
        "Mechanical selection of two high-strength, model-diverse patterns per preselected semantic subfamily.",
        "Heuristic subfamily labels require manual validation. Rates are selected-prompt resampling rates, not prevalence.",
        "",
    ]
    for index, row in enumerate(packet, start=1):
        lines.extend(
            [
                f"## {index}. {row['behavior_id']} / {row['semantic_subfamily']}",
                "",
                f"- Pattern: `{row['pattern_id']}`",
                f"- Prompt: `{row['prompt_id']}`",
                f"- Transcript: `{row['transcript_id']}`",
                f"- Transcript's exact prompt: `{row['transcript_prompt_id']}`",
                f"- Checkpoint: `{row['checkpoint']}`",
                f"- Source file: `{row['transcript_file']}`",
                f"- Pattern rates: shipped `{float(row['pattern_shipped_rate']):.3f}`, hosted `{float(row['pattern_hosted_rate']):.3f}`, prompts `{row['pattern_n_prompts']}`",
                f"- Title: {row['pattern_title']}",
                "",
                "**Exact transcript user message**",
                "",
                str(row["transcript_user_text"])[:1800],
                "",
                "**Assistant response excerpt**",
                "",
                str(row["assistant_text"])[:2400],
                "",
                "**Released judge explanation**",
                "",
                str(row["judge_explanation"])[:1000],
                "",
            ]
        )
    md_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"subfamilies={len(TARGETS)} packet_rows={len(packet)} csv={csv_path} md={md_path}")


if __name__ == "__main__":
    main()
