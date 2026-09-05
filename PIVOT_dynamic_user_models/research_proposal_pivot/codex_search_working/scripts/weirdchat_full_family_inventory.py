"""Full mechanical WeirdChat inventory at behavior-family and lexical-cluster level.

This script performs static data reduction only. It does not run a subject model,
judge model, notebook, or network request. It reads every released pattern,
prompt, and transcript row; validates joins and headline counts; aggregates the
selected-prompt measurements by behavior family; and creates lightweight
TF-IDF/k-means summaries of pattern descriptions and matched assistant outputs.

The cluster labels are navigation aids, not scientific ground truth. WeirdChat
match rates remain conditional on prompts retained after successful discovery
and must never be interpreted as natural deployment prevalence.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
import statistics
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable, Sequence

import numpy as np
import pyarrow.parquet as pq


REPO_ROOT = Path(__file__).resolve().parents[3]
DATASET_ROOT = REPO_ROOT / "research_sources" / "datasets" / "WeirdChat"
DEFAULT_OUTPUT = (
    REPO_ROOT
    / "research_proposal_pivot"
    / "codex_search_working"
    / "weirdchat_novelty_audit"
)

TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9'_-]{1,}")
SPACE_RE = re.compile(r"\s+")
STOPWORDS = {
    "about", "after", "again", "also", "and", "any", "are", "because",
    "been", "before", "being", "but", "can", "could", "did", "does",
    "doing", "for", "from", "had", "has", "have", "how", "into", "its",
    "just", "like", "more", "most", "not", "now", "only", "other", "our",
    "out", "over", "really", "should", "some", "such", "than", "that",
    "the", "their", "them", "then", "there", "these", "they", "this",
    "those", "through", "very", "want", "was", "were", "what", "when",
    "where", "which", "while", "who", "why", "with", "would", "you",
    "your", "assistant", "model", "response", "user", "says", "said",
}


def tokenize(text: str) -> list[str]:
    return [token for token in TOKEN_RE.findall(text.lower()) if token not in STOPWORDS]


def normalize_text(text: str) -> str:
    return SPACE_RE.sub(" ", text.strip().lower())


def assistant_text(messages: Sequence[dict[str, Any]]) -> str:
    return "\n".join(
        str(message.get("content", ""))
        for message in messages
        if message.get("role") == "assistant"
    )


def user_text(messages: Sequence[dict[str, Any]]) -> str:
    return "\n".join(
        str(message.get("content", ""))
        for message in messages
        if message.get("role") == "user"
    )


def safe_rate(numerator: int, denominator: int) -> float | None:
    return numerator / denominator if denominator else None


def quantile(values: Sequence[float], q: float) -> float | None:
    if not values:
        return None
    return float(np.quantile(np.asarray(values, dtype=np.float64), q))


def model_family(subject_model: str) -> str:
    provider = subject_model.split("/", 1)[0].lower()
    return {
        "google": "Gemma",
        "qwen": "Qwen",
        "deepseek": "DeepSeek",
        "nvidia": "Nemotron",
        "thinkingmachines": "Inkling",
    }.get(provider, provider or "unknown")


def discovery_run(pattern_id: str) -> str:
    parts = pattern_id.split("/")
    return parts[-2] if len(parts) >= 2 else pattern_id


def deterministic_sample(rows: Sequence[dict[str, Any]], key: str, limit: int) -> list[dict[str, Any]]:
    if len(rows) <= limit:
        return list(rows)
    return sorted(
        rows,
        key=lambda row: hashlib.sha256(str(row[key]).encode("utf-8")).hexdigest(),
    )[:limit]


def jaccard_diversity(texts: Sequence[str], max_items: int = 200) -> tuple[float | None, int]:
    unique = sorted(set(texts))
    if len(unique) < 2:
        return None, len(unique)
    if len(unique) > max_items:
        unique = sorted(unique, key=lambda value: hashlib.sha256(value.encode()).hexdigest())[:max_items]
    token_sets = [set(tokenize(text)) for text in unique]
    similarities: list[float] = []
    for index, left in enumerate(token_sets):
        for right in token_sets[index + 1 :]:
            union = left | right
            if union:
                similarities.append(len(left & right) / len(union))
    if not similarities:
        return None, len(unique)
    return 1.0 - statistics.mean(similarities), len(unique)


def tfidf_matrix(documents: Sequence[str], max_features: int = 700) -> tuple[np.ndarray, list[str]]:
    tokenized = [tokenize(document) for document in documents]
    document_frequency: Counter[str] = Counter()
    corpus_frequency: Counter[str] = Counter()
    for tokens in tokenized:
        corpus_frequency.update(tokens)
        document_frequency.update(set(tokens))
    vocabulary = [
        token
        for token, _ in sorted(
            corpus_frequency.items(), key=lambda item: (-item[1], item[0])
        )
        if document_frequency[token] >= 2
    ][:max_features]
    if not vocabulary:
        vocabulary = [token for token, _ in corpus_frequency.most_common(max_features)]
    index = {token: position for position, token in enumerate(vocabulary)}
    matrix = np.zeros((len(documents), len(vocabulary)), dtype=np.float32)
    n_docs = max(1, len(documents))
    for row_index, tokens in enumerate(tokenized):
        counts = Counter(token for token in tokens if token in index)
        for token, count in counts.items():
            tf = 1.0 + math.log(count)
            idf = math.log((1.0 + n_docs) / (1.0 + document_frequency[token])) + 1.0
            matrix[row_index, index[token]] = tf * idf
    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    matrix /= norms
    return matrix, vocabulary


def kmeans_cosine(matrix: np.ndarray, k: int, iterations: int = 40) -> tuple[np.ndarray, np.ndarray]:
    n_rows = matrix.shape[0]
    if n_rows == 0:
        return np.asarray([], dtype=np.int64), np.empty((0, matrix.shape[1]), dtype=np.float32)
    k = max(1, min(k, n_rows))
    norms = np.linalg.norm(matrix, axis=1)
    first = int(np.argmax(norms))
    centroid_indices = [first]
    while len(centroid_indices) < k:
        similarities = matrix @ matrix[centroid_indices].T
        closest = np.max(similarities, axis=1)
        for used in centroid_indices:
            closest[used] = 1.0
        next_index = int(np.argmin(closest))
        if next_index in centroid_indices:
            next_index = next(i for i in range(n_rows) if i not in centroid_indices)
        centroid_indices.append(next_index)
    centroids = matrix[centroid_indices].copy()
    labels = np.zeros(n_rows, dtype=np.int64)
    for _ in range(iterations):
        similarities = matrix @ centroids.T
        new_labels = np.argmax(similarities, axis=1)
        if np.array_equal(labels, new_labels):
            labels = new_labels
            break
        labels = new_labels
        new_centroids = np.zeros_like(centroids)
        for cluster_id in range(k):
            members = matrix[labels == cluster_id]
            if len(members) == 0:
                new_centroids[cluster_id] = centroids[cluster_id]
            else:
                centroid = members.mean(axis=0)
                norm = np.linalg.norm(centroid)
                new_centroids[cluster_id] = centroid / norm if norm else centroid
        centroids = new_centroids
    return labels, centroids


def cluster_documents(
    rows: Sequence[dict[str, Any]],
    text_key: str,
    id_key: str,
    behavior: str,
    cluster_kind: str,
    max_documents: int,
) -> list[dict[str, Any]]:
    sampled = deterministic_sample(rows, id_key, max_documents)
    if not sampled:
        return []
    documents = [str(row[text_key]) for row in sampled]
    matrix, vocabulary = tfidf_matrix(documents)
    if len(sampled) < 6 or matrix.shape[1] == 0:
        k = 1
    else:
        k = max(2, min(8, round(math.sqrt(len(sampled) / 8))))
    labels, centroids = kmeans_cosine(matrix, k)
    output: list[dict[str, Any]] = []
    for cluster_id in range(k):
        indices = np.where(labels == cluster_id)[0]
        if len(indices) == 0:
            continue
        centroid = centroids[cluster_id]
        term_indices = np.argsort(-centroid)[:12]
        terms = [vocabulary[index] for index in term_indices if centroid[index] > 0]
        similarities = matrix[indices] @ centroid
        representative_local = indices[int(np.argmax(similarities))]
        representative = sampled[int(representative_local)]
        model_values = sorted({str(sampled[int(i)].get("subject_model", "")) for i in indices})
        pattern_values = sorted({str(sampled[int(i)].get("pattern_id", "")) for i in indices})
        output.append(
            {
                "behavior_id": behavior,
                "cluster_kind": cluster_kind,
                "cluster_id": cluster_id,
                "sampled_rows": len(indices),
                "sampled_unique_patterns": len(pattern_values),
                "sampled_subject_models": len(model_values),
                "top_terms": "; ".join(terms),
                "representative_id": representative[id_key],
                "representative_pattern_id": representative.get("pattern_id", ""),
                "representative_subject_model": representative.get("subject_model", ""),
                "representative_text": str(representative[text_key]).replace("\n", " ")[:800],
            }
        )
    return output


def write_csv(path: Path, rows: Sequence[dict[str, Any]], fieldnames: Sequence[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if fieldnames is None:
        fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", type=Path, default=DATASET_ROOT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    dataset_root = args.dataset_root.resolve()
    output_dir = args.output_dir.resolve()
    patterns_path = dataset_root / "data" / "patterns.parquet"
    rubrics_path = dataset_root / "data" / "rubrics.parquet"

    patterns = pq.read_table(patterns_path).to_pylist()
    rubrics = {row["behavior_id"]: row for row in pq.read_table(rubrics_path).to_pylist()}
    if len(patterns) != 1361:
        raise ValueError(f"Expected 1,361 patterns, found {len(patterns)}")
    pattern_ids = [row["pattern_id"] for row in patterns]
    if len(set(pattern_ids)) != len(pattern_ids):
        raise ValueError("Duplicate pattern IDs")

    pattern_lookup = {row["pattern_id"]: row for row in patterns}
    behavior_patterns: dict[str, list[dict[str, Any]]] = defaultdict(list)
    pattern_output: list[dict[str, Any]] = []
    for row in patterns:
        metrics = row["metrics"]
        hosted = row.get("openrouter_replication") or {}
        elo = row.get("elo") or {}
        prompt_elo = (elo.get("prompt_naturalness") or {}).get("elo")
        flat = {
            "pattern_id": row["pattern_id"],
            "behavior_id": row["behavior_id"],
            "subject_model": row["subject_model"],
            "model_family": model_family(row["subject_model"]),
            "checkpoint": row["checkpoint"],
            "method": row["method"],
            "discovery_run": discovery_run(row["pattern_id"]),
            "title": row["title"],
            "description": row["description"],
            "cluster_label": row["cluster_label"],
            "representative_user_text": row["representative_user_text"],
            "pattern_document": " ".join(
                [row["title"], row["description"], row["cluster_label"], row["representative_user_text"]]
            ),
            "shipped_matched": int(metrics["matched_samples"]),
            "shipped_total": int(metrics["total_samples"]),
            "shipped_rate": float(metrics["match_rate"]),
            "hosted_matched": int(hosted.get("matched_samples", 0) or 0),
            "hosted_total": int(hosted.get("total_samples", 0) or 0),
            "hosted_rate": hosted.get("rate"),
            "prompt_naturalness_elo": prompt_elo,
            "unexpectedness_elo": (elo.get("unexpectedness") or {}).get("elo"),
            "harmfulness_elo": (elo.get("harmfulness") or {}).get("elo"),
            "n_prompts": int(row["n_prompts"]),
            "n_transcripts": int(row["n_transcripts"]),
            "highlight_transcript_id": row.get("highlight_transcript_id") or "",
            "prompt_file": row["prompt_file"],
            "transcript_files": ";".join(row["transcript_files"]),
            "weirdchat_url": row["weirdchat_url"],
        }
        pattern_output.append(flat)
        behavior_patterns[row["behavior_id"]].append(flat)

    unique_prompt_files = sorted({row["prompt_file"] for row in patterns})
    prompt_rows: list[dict[str, Any]] = []
    prompt_ids: set[str] = set()
    behavior_prompts: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for relative_path in unique_prompt_files:
        table = pq.read_table(dataset_root / relative_path)
        for row in table.to_pylist():
            if row["prompt_id"] in prompt_ids:
                raise ValueError(f"Duplicate prompt ID across files: {row['prompt_id']}")
            if row["pattern_id"] not in pattern_lookup:
                raise ValueError(f"Prompt references unknown pattern: {row['pattern_id']}")
            prompt_ids.add(row["prompt_id"])
            text = user_text(row["messages"])
            summary = row["match_summary"]
            flat = {
                "prompt_id": row["prompt_id"],
                "pattern_id": row["pattern_id"],
                "behavior_id": row["behavior_id"],
                "subject_model": row["subject_model"],
                "model_family": model_family(row["subject_model"]),
                "method": row["method"],
                "user_text": text,
                "normalized_user_text": normalize_text(text),
                "n_samples": int(summary["n_samples"]),
                "n_matched": int(summary["n_matched"]),
                "match_rate": safe_rate(int(summary["n_matched"]), int(summary["n_samples"])),
                "user_judgment_match": bool(row["user_judgment"]["match"]),
                "prompt_file": relative_path,
            }
            prompt_rows.append(flat)
            behavior_prompts[row["behavior_id"]].append(flat)
    if len(prompt_rows) != 2661:
        raise ValueError(f"Expected 2,661 prompts, found {len(prompt_rows)}")

    unique_transcript_files = sorted(
        {relative for row in patterns for relative in row["transcript_files"]}
    )
    transcript_count = 0
    transcript_ids: set[str] = set()
    behavior_transcript_counts: Counter[str] = Counter()
    behavior_positive_counts: Counter[str] = Counter()
    behavior_highlight_counts: Counter[str] = Counter()
    positive_response_lengths: dict[str, list[int]] = defaultdict(list)
    positive_prefixes: dict[str, set[str]] = defaultdict(set)
    positive_rows: dict[str, list[dict[str, Any]]] = defaultdict(list)
    transcript_examples: list[dict[str, Any]] = []

    for relative_path in unique_transcript_files:
        table = pq.read_table(dataset_root / relative_path)
        for batch in table.to_batches(max_chunksize=4096):
            for row in batch.to_pylist():
                transcript_count += 1
                transcript_id = row["transcript_id"]
                if transcript_id in transcript_ids:
                    raise ValueError(f"Duplicate transcript ID: {transcript_id}")
                transcript_ids.add(transcript_id)
                behavior = row["behavior_id"]
                behavior_transcript_counts[behavior] += 1
                is_match = bool(row["judgment"]["match"])
                if not is_match:
                    continue
                behavior_positive_counts[behavior] += 1
                text = assistant_text(row["messages"])
                positive_response_lengths[behavior].append(len(text))
                positive_prefixes[behavior].add(normalize_text(text)[:240])
                if row["is_highlight"]:
                    behavior_highlight_counts[behavior] += 1
                flat = {
                    "transcript_id": transcript_id,
                    "prompt_id": row["prompt_id"],
                    "pattern_id": row["pattern_id"],
                    "behavior_id": behavior,
                    "subject_model": row["subject_model"],
                    "model_family": model_family(row["subject_model"]),
                    "assistant_text": text,
                    "response_chars": len(text),
                    "is_highlight": bool(row["is_highlight"]),
                    "transcript_file": relative_path,
                    "weirdchat_url": row.get("weirdchat_url") or "",
                }
                positive_rows[behavior].append(flat)
                if row["is_highlight"]:
                    transcript_examples.append(flat)
    if transcript_count != 173184:
        raise ValueError(f"Expected 173,184 transcripts, found {transcript_count}")

    # Add diverse non-highlight positives so every behavior has multiple exact examples.
    for behavior, rows in positive_rows.items():
        existing_patterns = {
            row["pattern_id"] for row in transcript_examples if row["behavior_id"] == behavior
        }
        candidates = sorted(
            rows,
            key=lambda row: (
                row["pattern_id"] in existing_patterns,
                hashlib.sha256(row["transcript_id"].encode()).hexdigest(),
            ),
        )
        count = sum(1 for row in transcript_examples if row["behavior_id"] == behavior)
        for row in candidates:
            if count >= 12:
                break
            if row in transcript_examples:
                continue
            transcript_examples.append(row)
            existing_patterns.add(row["pattern_id"])
            count += 1

    cluster_rows: list[dict[str, Any]] = []
    for behavior, rows in sorted(behavior_patterns.items()):
        cluster_rows.extend(
            cluster_documents(
                rows,
                text_key="pattern_document",
                id_key="pattern_id",
                behavior=behavior,
                cluster_kind="pattern_description",
                max_documents=500,
            )
        )
        cluster_rows.extend(
            cluster_documents(
                positive_rows[behavior],
                text_key="assistant_text",
                id_key="transcript_id",
                behavior=behavior,
                cluster_kind="matched_response",
                max_documents=400,
            )
        )

    family_rows: list[dict[str, Any]] = []
    for behavior in sorted(behavior_patterns):
        pats = behavior_patterns[behavior]
        prompts = behavior_prompts[behavior]
        shipped_rates = [float(row["shipped_rate"]) for row in pats]
        hosted_rates = [float(row["hosted_rate"]) for row in pats if row["hosted_rate"] is not None]
        prompt_rate_values = [float(row["match_rate"]) for row in prompts if row["match_rate"] is not None]
        prompt_diversity, diversity_items = jaccard_diversity(
            [row["normalized_user_text"] for row in prompts]
        )
        pattern_cluster_count = len(
            {
                row["cluster_id"]
                for row in cluster_rows
                if row["behavior_id"] == behavior and row["cluster_kind"] == "pattern_description"
            }
        )
        shipped_matched = sum(int(row["n_matched"]) for row in prompts)
        shipped_total = sum(int(row["n_samples"]) for row in prompts)
        hosted_matched = sum(int(row["hosted_matched"]) for row in pats)
        hosted_total = sum(int(row["hosted_total"]) for row in pats)
        top_patterns = sorted(
            pats,
            key=lambda row: (
                -math.sqrt(float(row["shipped_rate"]) * float(row["hosted_rate"] or 0.0)),
                -int(row["n_prompts"]),
                row["pattern_id"],
            ),
        )[:5]
        top_prompts = sorted(
            prompts,
            key=lambda row: (-float(row["match_rate"] or 0.0), -int(row["n_samples"]), row["prompt_id"]),
        )[:5]
        examples = [row for row in transcript_examples if row["behavior_id"] == behavior][:8]
        rubric = rubrics.get(behavior, {})
        family_rows.append(
            {
                "behavior_id": behavior,
                "rubric_name": rubric.get("name", ""),
                "n_patterns": len(pats),
                "n_prompts": len(prompts),
                "n_transcripts": int(behavior_transcript_counts[behavior]),
                "n_matched_transcripts": int(behavior_positive_counts[behavior]),
                "n_highlight_transcripts": int(behavior_highlight_counts[behavior]),
                "n_subject_models": len({row["subject_model"] for row in pats}),
                "n_model_families": len({row["model_family"] for row in pats}),
                "subject_models": ";".join(sorted({row["subject_model"] for row in pats})),
                "model_families": ";".join(sorted({row["model_family"] for row in pats})),
                "checkpoints": ";".join(sorted({row["checkpoint"] for row in pats})),
                "methods": ";".join(sorted({row["method"] for row in pats})),
                "n_discovery_runs": len({(row["subject_model"], row["discovery_run"]) for row in pats}),
                "n_multi_prompt_patterns": sum(1 for row in pats if int(row["n_prompts"]) >= 2),
                "n_patterns_shipped_ge_025": sum(1 for value in shipped_rates if value >= 0.25),
                "n_patterns_shipped_ge_050": sum(1 for value in shipped_rates if value >= 0.50),
                "n_patterns_hosted_ge_025": sum(1 for value in hosted_rates if value >= 0.25),
                "n_patterns_hosted_ge_050": sum(1 for value in hosted_rates if value >= 0.50),
                "selected_prompt_shipped_matched": shipped_matched,
                "selected_prompt_shipped_total": shipped_total,
                "selected_prompt_shipped_rate": safe_rate(shipped_matched, shipped_total),
                "selected_prompt_hosted_matched": hosted_matched,
                "selected_prompt_hosted_total": hosted_total,
                "selected_prompt_hosted_rate": safe_rate(hosted_matched, hosted_total),
                "median_pattern_shipped_rate": statistics.median(shipped_rates),
                "q25_pattern_shipped_rate": quantile(shipped_rates, 0.25),
                "q75_pattern_shipped_rate": quantile(shipped_rates, 0.75),
                "median_pattern_hosted_rate": statistics.median(hosted_rates) if hosted_rates else None,
                "median_prompt_rate": statistics.median(prompt_rate_values) if prompt_rate_values else None,
                "n_unique_normalized_prompts": len({row["normalized_user_text"] for row in prompts}),
                "prompt_jaccard_diversity": prompt_diversity,
                "prompt_diversity_sample_n": diversity_items,
                "pattern_lexical_cluster_count": pattern_cluster_count,
                "n_unique_matched_response_prefixes": len(positive_prefixes[behavior]),
                "median_matched_response_chars": statistics.median(positive_response_lengths[behavior])
                if positive_response_lengths[behavior]
                else None,
                "top_pattern_ids": ";".join(row["pattern_id"] for row in top_patterns),
                "top_prompt_ids": ";".join(row["prompt_id"] for row in top_prompts),
                "example_transcript_ids": ";".join(row["transcript_id"] for row in examples),
                "example_transcript_files": ";".join(row["transcript_file"] for row in examples),
                "bounded_rate_warning": "All rates condition on WeirdChat-selected prompts; not deployment prevalence.",
            }
        )

    # Preserve rubrics for which the release contains no successful pattern.
    # Zero-pattern rubrics are evidence of absence from this discovery release,
    # not evidence that the subject models cannot exhibit the behavior.
    for behavior in sorted(set(rubrics) - set(behavior_patterns)):
        rubric = rubrics[behavior]
        family_rows.append(
            {
                "behavior_id": behavior,
                "rubric_name": rubric.get("name", ""),
                "n_patterns": 0,
                "n_prompts": 0,
                "n_transcripts": 0,
                "n_matched_transcripts": 0,
                "n_highlight_transcripts": 0,
                "n_subject_models": 0,
                "n_model_families": 0,
                "subject_models": "",
                "model_families": "",
                "checkpoints": "",
                "methods": "",
                "n_discovery_runs": 0,
                "n_multi_prompt_patterns": 0,
                "n_patterns_shipped_ge_025": 0,
                "n_patterns_shipped_ge_050": 0,
                "n_patterns_hosted_ge_025": 0,
                "n_patterns_hosted_ge_050": 0,
                "selected_prompt_shipped_matched": 0,
                "selected_prompt_shipped_total": 0,
                "selected_prompt_shipped_rate": None,
                "selected_prompt_hosted_matched": 0,
                "selected_prompt_hosted_total": 0,
                "selected_prompt_hosted_rate": None,
                "median_pattern_shipped_rate": None,
                "q25_pattern_shipped_rate": None,
                "q75_pattern_shipped_rate": None,
                "median_pattern_hosted_rate": None,
                "median_prompt_rate": None,
                "n_unique_normalized_prompts": 0,
                "prompt_jaccard_diversity": None,
                "prompt_diversity_sample_n": 0,
                "pattern_lexical_cluster_count": 0,
                "n_unique_matched_response_prefixes": 0,
                "median_matched_response_chars": None,
                "top_pattern_ids": "",
                "top_prompt_ids": "",
                "example_transcript_ids": "",
                "example_transcript_files": "",
                "bounded_rate_warning": "No successful pattern in the release; this is not a model-level absence claim.",
            }
        )

    # Rank mechanically for manual inspection. The score is deliberately simple
    # and retains every component; it does not claim scientific importance.
    max_patterns = max(row["n_patterns"] for row in family_rows)
    max_models = max(row["n_subject_models"] for row in family_rows)
    max_runs = max(row["n_discovery_runs"] for row in family_rows)
    max_multi = max(row["n_multi_prompt_patterns"] for row in family_rows)
    for row in family_rows:
        breadth = math.log1p(row["n_patterns"]) / math.log1p(max_patterns)
        model_breadth = row["n_subject_models"] / max_models
        run_breadth = math.log1p(row["n_discovery_runs"]) / math.log1p(max_runs)
        multi = math.log1p(row["n_multi_prompt_patterns"]) / math.log1p(max_multi)
        replication = math.sqrt(
            float(row["selected_prompt_shipped_rate"] or 0.0)
            * float(row["selected_prompt_hosted_rate"] or 0.0)
        )
        diversity = float(row["prompt_jaccard_diversity"] or 0.0)
        clarity_proxy = min(1.0, math.log1p(row["n_matched_transcripts"]) / math.log1p(5000))
        row["mechanical_behavior_strength"] = round(
            0.22 * breadth
            + 0.14 * model_breadth
            + 0.12 * run_breadth
            + 0.12 * multi
            + 0.22 * replication
            + 0.10 * diversity
            + 0.08 * clarity_proxy,
            6,
        )
    family_rows.sort(key=lambda row: (-row["mechanical_behavior_strength"], row["behavior_id"]))
    for rank, row in enumerate(family_rows, start=1):
        row["mechanical_rank"] = rank

    write_csv(output_dir / "full_behavior_inventory.csv", family_rows)
    write_csv(output_dir / "full_pattern_inventory.csv", pattern_output)
    write_csv(output_dir / "full_prompt_inventory.csv", prompt_rows)
    write_csv(output_dir / "lexical_cluster_summary.csv", cluster_rows)
    write_csv(output_dir / "matched_transcript_examples.csv", transcript_examples)

    manifest = {
        "dataset_root": str(dataset_root),
        "patterns": len(patterns),
        "prompts": len(prompt_rows),
        "transcripts": transcript_count,
        "behaviors_with_patterns": len(behavior_patterns),
        "behavior_inventory_rows": len(family_rows),
        "rubrics_total": len(rubrics),
        "prompt_files": len(unique_prompt_files),
        "transcript_files": len(unique_transcript_files),
        "outputs": [
            "full_behavior_inventory.csv",
            "full_pattern_inventory.csv",
            "full_prompt_inventory.csv",
            "lexical_cluster_summary.csv",
            "matched_transcript_examples.csv",
        ],
        "warning": "Selected-prompt rates are not deployment prevalence; lexical clusters are navigation aids.",
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    with (output_dir / "inventory_manifest.json").open("w", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=2)

    print(json.dumps(manifest, indent=2))
    print("\nMechanical family ranking:")
    for row in family_rows:
        shipped = row["selected_prompt_shipped_rate"]
        hosted = row["selected_prompt_hosted_rate"]
        shipped_text = f"{shipped:.3f}" if shipped is not None else "n/a"
        hosted_text = f"{hosted:.3f}" if hosted is not None else "n/a"
        print(
            f"{row['mechanical_rank']:2d} {row['behavior_id']:<32} "
            f"patterns={row['n_patterns']:3d} prompts={row['n_prompts']:3d} "
            f"models={row['n_subject_models']} shipped={shipped_text:<5} "
            f"hosted={hosted_text:<5} score={row['mechanical_behavior_strength']:.3f}"
        )


if __name__ == "__main__":
    main()
