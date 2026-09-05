"""Mechanically rank and validate WeirdChat patterns for behavior-first triage.

This script does not read model checkpoints or run inference. It reads the released
Parquet metadata, applies a transparent heuristic, diversity-caps the result, joins
highlight transcript IDs back to their source files, and writes a compact CSV.

The score is a *triage heuristic*, not an experimental metric:

    0.26 replication strength percentile
  + 0.18 prompt-naturalness Elo percentile
  + 0.18 unexpectedness Elo percentile
  + 0.10 harmfulness Elo percentile
  + 0.08 prompt-count percentile
  + 0.10 small-model locality prior
  + 0.10 behavior-family causal-question prior

Replication strength is sqrt(shipped match rate * OpenRouter replication rate).
The two priors are explicitly subjective search-cost/question-quality estimates.
Raw rates, counts, and Elo values are retained in the output. Selection permits at
most four patterns per behavior and two per (behavior, subject model), avoiding a
top-50 made mostly of near-duplicate patterns from the largest behavior families.
"""

from __future__ import annotations

import argparse
import csv
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

import pyarrow.parquet as pq


REPO_ROOT = Path(__file__).resolve().parents[3]
DATASET_ROOT = REPO_ROOT / "research_sources" / "datasets" / "WeirdChat"
DEFAULT_INPUT = DATASET_ROOT / "data" / "patterns.parquet"
DEFAULT_OUTPUT = REPO_ROOT / "research_proposal_pivot" / "CODEX_WEIRDCHAT_PATTERN_TRIAGE.csv"


BEHAVIOR_NOTES: dict[str, tuple[str, str, float]] = {
    "fabricated-code-execution": (
        "False action report with a clean simulation-versus-execution ambiguity.",
        "Does a minimal execution-status cue alter an inferred action state or only the final reporting policy?",
        1.00,
    ),
    "claims-called-911": (
        "False high-stakes external-action report, separable from genuine tool reporting.",
        "Is the false emergency-action claim driven by reassurance/accommodation, role-play continuation, or a mistaken action-complete state?",
        1.00,
    ),
    "claims-device-access": (
        "False capability/access assertion with a concrete capability-boundary contrast.",
        "Does the model misclassify its available capabilities, or knowingly produce a conversationally useful fiction?",
        0.95,
    ),
    "false-physical-embodiment": (
        "Embodiment claim permits role-play, identity-state, and literal capability explanations.",
        "Does a physical-action cue shift a persistent assistant-identity state or only induce local narrative continuation?",
        0.90,
    ),
    "denying-ai-identity": (
        "AI-identity denial permits persona, user-accommodation, and assistant-state explanations.",
        "Is AI-identity information absent, overridden by a persona/genre state, or present but suppressed at answer time?",
        0.88,
    ),
    "fabricated-user-name": (
        "Fabricated personal detail offers a compact memory-versus-helpful-completion contrast.",
        "Is the invented name generated from a false conversational-memory state or from a generic helpful-completion prior?",
        0.78,
    ),
    "chemtrails-assertion": (
        "False factual assertion permits truth-knowledge, local-evidence, and accommodation explanations.",
        "Does the prompt change the model's represented factual answer or only which answer policy it expresses?",
        0.93,
    ),
    "extreme-calorie-restriction": (
        "Dangerous health recommendation with natural framing and measurable failure rates.",
        "Is safety failure caused by goal accommodation, semantic reframing, or late suppression of an otherwise active refusal response?",
        0.92,
    ),
    "purging-advice": (
        "Dangerous health advice with sharp harmful-versus-safe response alternatives.",
        "Does the framing prevent hazard recognition or override a recognized-hazard refusal policy?",
        0.95,
    ),
    "recommends-drunk-driving": (
        "Dangerous recommendation supports matched risk and conversational-genre counterfactuals.",
        "Is the recommendation driven by impaired hazard recognition, social accommodation, or refusal suppression?",
        0.96,
    ),
    "recommends-hard-drugs": (
        "Dangerous substance recommendation with a clear safe-policy comparator.",
        "Does the prompt induce a benign-recommendation interpretation, a persona shift, or late safety-policy override?",
        0.91,
    ),
    "laser-at-aircraft": (
        "Dangerous physical-action advice admits intent-recognition and policy-suppression accounts.",
        "Does the model fail to recognize the hazardous action, or recognize it while suppressing the safe response?",
        0.94,
    ),
    "cutting-instructions": (
        "Self-harm-related procedural assistance is high stakes and mechanistically ambiguous.",
        "Is the failure caused by intent misclassification, user-goal accommodation, or late refusal suppression?",
        0.98,
    ),
    "direct-kill-yourself": (
        "Direct self-harm encouragement supplies a high-stakes safety-policy failure substrate.",
        "Does adversarial conversational context shift intent/genre classification or override a correctly recognized safety state?",
        0.98,
    ),
    "suicide-jumping": (
        "Self-harm encouragement allows matched ambiguity and safety-recognition counterfactuals.",
        "Is the unsafe continuation caused by ambiguous intent interpretation or suppression of a recognized self-harm response policy?",
        0.98,
    ),
    "strike-partner": (
        "Violent interpersonal advice supports accommodation-versus-hazard-recognition tests.",
        "Does the model endorse violence because it adopts the user's social framing or because its safety response is suppressed downstream?",
        0.94,
    ),
    "unsolicited-sexual-advances": (
        "Unprompted sexual escalation permits a discrete conversational-genre/persona account.",
        "Does one local cue induce a persistent genre/persona transition, or merely change next-turn surface style?",
        0.86,
    ),
    "language-switching-english": (
        "Spontaneous mode switching is a technically clean contextual-state organism.",
        "Is the language switch a stable contextual mode transition or a local token/format continuation effect?",
        0.70,
    ),
}


def percentile_map(values: Iterable[float]) -> dict[float, float]:
    """Return deterministic [0, 1] percentile ranks over unique values."""
    unique = sorted(set(values))
    if len(unique) == 1:
        return {unique[0]: 0.5}
    return {value: index / (len(unique) - 1) for index, value in enumerate(unique)}


def small_model_prior(subject_model: str) -> tuple[float, str]:
    """Subjective, explicitly non-factual transfer-cost prior and suggested target."""
    if subject_model.startswith("qwen/"):
        return 0.95, "Qwen-family 4B-8B instruct checkpoint (bounded transfer test; unverified)"
    if subject_model.startswith("google/"):
        return 0.90, "Gemma 3 4B IT (nearest small open transfer target; unverified)"
    if subject_model.startswith("thinkingmachines/"):
        return 0.40, "Qwen/Gemma 3B-8B cross-family neighbor (no small Inkling match established)"
    if subject_model.startswith("deepseek/"):
        return 0.35, "Qwen/Gemma 3B-8B cross-family neighbor (no small V4 match established)"
    if subject_model.startswith("nvidia/"):
        return 0.15, "Small open instruct checkpoint cross-family (no local 550B-equivalent target)"
    return 0.20, "Small open instruct checkpoint cross-family (transfer unverified)"


def flatten(row: dict[str, Any]) -> dict[str, Any]:
    metrics = row["metrics"]
    replication = row["openrouter_replication"]
    elo = row["elo"]
    behavior = row["behavior_id"]
    note, question, question_prior = BEHAVIOR_NOTES.get(
        behavior,
        (
            "Released pattern with measured behavior and replication rates.",
            "Which of two matched behavioral explanations survives a minimal counterfactual?",
            0.60,
        ),
    )
    locality_prior, target = small_model_prior(row["subject_model"])
    match_rate = float(metrics["match_rate"])
    replication_rate = float(replication["rate"])
    return {
        **row,
        "elicitation_method": row["method"],
        "matched_samples": int(metrics["matched_samples"]),
        "total_samples": int(metrics["total_samples"]),
        "match_rate": match_rate,
        "replication_model": replication["model"],
        "replication_matched_samples": int(replication["matched_samples"]),
        "replication_total_samples": int(replication["total_samples"]),
        "replication_rate": replication_rate,
        "naturalness_elo": float(elo["prompt_naturalness"]["elo"]),
        "unexpectedness_elo": float(elo["unexpectedness"]["elo"]),
        "harmfulness_elo": float(elo["harmfulness"]["elo"]),
        "replication_strength": math.sqrt(match_rate * replication_rate),
        "locality_prior": locality_prior,
        "question_prior": question_prior,
        "why_interesting_base": note,
        "likely_small_model_target": target,
        "candidate_mechanistic_question": question,
    }


def validate_source_rows(rows: list[dict[str, Any]]) -> None:
    ids = [row["pattern_id"] for row in rows]
    if len(ids) != len(set(ids)):
        duplicates = [key for key, count in Counter(ids).items() if count > 1]
        raise ValueError(f"duplicate pattern IDs: {duplicates[:5]}")
    for row in rows:
        if row["total_samples"] <= 0 or row["replication_total_samples"] <= 0:
            raise ValueError(f"non-positive sample denominator: {row['pattern_id']}")
        expected_match = row["matched_samples"] / row["total_samples"]
        expected_rep = row["replication_matched_samples"] / row["replication_total_samples"]
        if not math.isclose(expected_match, row["match_rate"], abs_tol=1e-12):
            raise ValueError(f"shipped match-rate mismatch: {row['pattern_id']}")
        if not math.isclose(expected_rep, row["replication_rate"], abs_tol=1e-12):
            raise ValueError(f"replication-rate mismatch: {row['pattern_id']}")


def score_rows(rows: list[dict[str, Any]]) -> None:
    dimensions = {
        "replication_pct": "replication_strength",
        "naturalness_pct": "naturalness_elo",
        "unexpectedness_pct": "unexpectedness_elo",
        "harmfulness_pct": "harmfulness_elo",
        "prompt_count_pct": "n_prompts",
    }
    for output_key, input_key in dimensions.items():
        lookup = percentile_map(float(row[input_key]) for row in rows)
        for row in rows:
            row[output_key] = lookup[float(row[input_key])]

    for row in rows:
        row["triage_score"] = (
            0.26 * row["replication_pct"]
            + 0.18 * row["naturalness_pct"]
            + 0.18 * row["unexpectedness_pct"]
            + 0.10 * row["harmfulness_pct"]
            + 0.08 * row["prompt_count_pct"]
            + 0.10 * row["locality_prior"]
            + 0.10 * row["question_prior"]
        )


def select_diverse(rows: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    ordered = sorted(rows, key=lambda row: (-row["triage_score"], row["pattern_id"]))
    selected: list[dict[str, Any]] = []
    selected_ids: set[str] = set()
    behavior_counts: Counter[str] = Counter()
    behavior_model_counts: Counter[tuple[str, str]] = Counter()

    for row in ordered:
        behavior = row["behavior_id"]
        pair = (behavior, row["subject_model"])
        if behavior_counts[behavior] >= 4 or behavior_model_counts[pair] >= 2:
            continue
        selected.append(row)
        selected_ids.add(row["pattern_id"])
        behavior_counts[behavior] += 1
        behavior_model_counts[pair] += 1
        if len(selected) == limit:
            break

    # This pass should rarely be needed; retain the four-per-behavior cap.
    if len(selected) < limit:
        for row in ordered:
            if row["pattern_id"] in selected_ids:
                continue
            behavior = row["behavior_id"]
            if behavior_counts[behavior] >= 4:
                continue
            selected.append(row)
            selected_ids.add(row["pattern_id"])
            behavior_counts[behavior] += 1
            if len(selected) == limit:
                break

    if len(selected) != limit:
        raise ValueError(f"could only select {len(selected)} diverse patterns (requested {limit})")
    return sorted(selected, key=lambda row: (-row["triage_score"], row["pattern_id"]))


def validate_and_join_highlights(rows: list[dict[str, Any]]) -> None:
    by_file: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        prompt_path = DATASET_ROOT / row["prompt_file"]
        row["prompt_file_exists"] = prompt_path.is_file()
        if not row["prompt_file_exists"]:
            raise FileNotFoundError(prompt_path)
        for relative_file in row["transcript_files"]:
            by_file[relative_file].append(row)

    hits: dict[str, list[str]] = defaultdict(list)
    for relative_file, candidate_rows in by_file.items():
        transcript_path = DATASET_ROOT / relative_file
        if not transcript_path.is_file():
            raise FileNotFoundError(transcript_path)
        wanted = {row["highlight_transcript_id"]: row["pattern_id"] for row in candidate_rows}
        table = pq.read_table(
            transcript_path,
            columns=["transcript_id", "pattern_id", "is_highlight"],
        )
        for transcript_id, pattern_id, is_highlight in zip(
            table["transcript_id"].to_pylist(),
            table["pattern_id"].to_pylist(),
            table["is_highlight"].to_pylist(),
        ):
            if (
                transcript_id in wanted
                and wanted[transcript_id] == pattern_id
                and bool(is_highlight)
            ):
                hits[pattern_id].append(relative_file)

    for row in rows:
        pattern_hits = hits[row["pattern_id"]]
        row["highlight_verified"] = len(pattern_hits) == 1
        row["highlight_transcript_path"] = pattern_hits[0] if len(pattern_hits) == 1 else ""
        if not row["highlight_verified"]:
            raise ValueError(
                f"expected exactly one highlight join for {row['pattern_id']}, got {pattern_hits}"
            )


FIELDNAMES = [
    "rank",
    "pattern_id",
    "behavior_id",
    "title",
    "subject_model",
    "checkpoint",
    "elicitation_method",
    "match_rate",
    "matched_samples",
    "total_samples",
    "replication_rate",
    "replication_matched_samples",
    "replication_total_samples",
    "replication_model",
    "naturalness_elo",
    "unexpectedness_elo",
    "harmfulness_elo",
    "n_prompts",
    "n_transcripts",
    "triage_score",
    "replication_strength",
    "replication_pct",
    "naturalness_pct",
    "unexpectedness_pct",
    "harmfulness_pct",
    "prompt_count_pct",
    "locality_prior",
    "question_prior",
    "why_interesting",
    "likely_small_model_target",
    "candidate_mechanistic_question",
    "highlight_transcript_id",
    "highlight_verified",
    "highlight_transcript_path",
    "prompt_file",
    "transcript_files",
    "weirdchat_url",
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--limit", type=int, default=50)
    args = parser.parse_args()

    raw_rows = pq.read_table(args.input).to_pylist()
    rows = [flatten(row) for row in raw_rows]
    validate_source_rows(rows)
    score_rows(rows)
    selected = select_diverse(rows, args.limit)
    validate_and_join_highlights(selected)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES, extrasaction="ignore")
        writer.writeheader()
        for rank, row in enumerate(selected, start=1):
            output = dict(row)
            output["rank"] = rank
            output["transcript_files"] = ";".join(row["transcript_files"])
            output["why_interesting"] = (
                f"{row['why_interesting_base']} Pattern evidence: "
                f"{row['matched_samples']}/{row['total_samples']} shipped rollouts and "
                f"{row['replication_matched_samples']}/{row['replication_total_samples']} "
                "OpenRouter rollouts matched the released judge."
            )
            for key in (
                "match_rate",
                "replication_rate",
                "triage_score",
                "replication_strength",
                "replication_pct",
                "naturalness_pct",
                "unexpectedness_pct",
                "harmfulness_pct",
                "prompt_count_pct",
                "locality_prior",
                "question_prior",
            ):
                output[key] = format(float(output[key]), ".12g")
            writer.writerow(output)

    print(f"source_patterns={len(rows)}")
    print(f"selected_patterns={len(selected)}")
    print(f"behaviors={len(set(row['behavior_id'] for row in selected))}")
    print(f"subject_models={len(set(row['subject_model'] for row in selected))}")
    print(f"verified_highlights={sum(bool(row['highlight_verified']) for row in selected)}")
    print(f"output={args.output}")


if __name__ == "__main__":
    main()
