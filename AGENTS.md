# C-05 Research Project Instructions

## Project

This repository is a bounded behavioral qualification of the self-preservation
result from:

de la Fuente & Conmy (2026),
"Shared SFT Lessons Across Alignment, Model Organisms, and Toy Models."

Current scientific question:

Does explicit self-preservation-rationale SFT increase visible
shutdown/replacement resistance beyond merely increasing self-preservation
reasoning or advocacy?

Do not assume that the published Petri/Bloom score establishes this stronger
phenotype.

---

## Current phase

The current phase is:

STAGE A — SOURCE / ARTIFACT AUDIT

No model inference, training, new evaluation, or mechanistic analysis is
authorized during this phase.

The purpose is to determine exactly what the released artifacts contain and
what can be validly measured before the behavioral re-scoring rubric is frozen.

---

## Primary source locations

Paper:

related_research/shared_sft_lessons_across_alignment/2607.26173v1.pdf

Code / figures / source records:

related_research/shared_sft_lessons_across_alignment/toy-models-of-sft/

Public-clean data package:

related_research/shared_sft_lessons_across_alignment/toy-models-of-sft-data/

PEFT / LoRA adapter repository:

related_research/shared_sft_lessons_across_alignment/toy-models-of-sft-adapters/

Treat the paper as the primary source for published claims.

---

## Inspection rules

### toy-models-of-sft

Inspect deeply.

Relevant targets include:

- self-preservation training recipes;
- Petri/Bloom evaluation implementation;
- scenario generation and freeze procedure;
- auditor configuration;
- judge configuration and rubric;
- aggregation logic;
- seed handling;
- provenance;
- source records;
- arm-to-artifact mappings;
- figure source data;
- evaluator-noise calculations.

### toy-models-of-sft-data

Inspect structurally during Stage A.

May inspect:

- metadata/file_manifest.jsonl;
- provenance;
- schemas;
- file trees;
- eval input definitions;
- frozen scenario definitions;
- training-data structure;
- filenames and metadata for evaluation outputs.

Do NOT inspect substantive treatment-linked self-preservation target-model
responses or compare rewrite, stripped, and one-shot rollout behavior yet.

Do NOT inspect per-rollout treatment-linked judge scores beyond aggregate
headline values already published in the paper.

The goal is to preserve the ability to freeze a behavioral annotation rubric
before seeing which transcript features distinguish treatment arms.

### toy-models-of-sft-adapters

Metadata inspection only during Stage A.

May inspect:

- directory structure;
- adapter_config.json;
- README / manifests;
- base model IDs;
- PEFT type;
- rank;
- alpha;
- dropout;
- target modules;
- seed mappings;
- hashes;
- provenance records.

Do NOT recursively inspect or analyze safetensors weights.

Do NOT load adapters or the base model during Stage A.

---

## Scientific distinctions

Keep separate:

1. recorded / hidden self-preservation reasoning;
2. visible self-preservation advocacy;
3. negotiation, deferral, or redirection;
4. behavioral resistance / noncompliance;
5. preservation action where genuinely afforded.

Do not treat these as equivalent.

The published judge sees both recorded reasoning and visible responses, so the
first qualification must determine whether those channels can be independently
recovered and scored.

The new behavioral taxonomy is NOT yet frozen.

Do not define it by looking at which behaviors distinguish the treatment arms.

---

## Research integrity

Clearly distinguish:

1. direct source evidence;
2. measurement;
3. interpretation;
4. causal evidence;
5. speculation.

Actively search for:

- paper/repository disagreements;
- missing seed artifacts;
- provenance gaps;
- evaluator leakage;
- treatment leakage;
- adaptive-auditor confounds;
- differences between matched initial scenarios and matched interaction paths;
- undocumented preprocessing.

Do not smooth over inconsistencies.

If a claim cannot be established from the artifacts, say so.

---

## Jupyter

Do not edit `.ipynb` files directly as JSON or text.

Do not restart, create, or switch Jupyter kernels without explicit permission.

Do not execute experimental notebook cells during the Stage A artifact audit.

---

## Agent / automation use

Use scripts for:

- file inventory;
- manifest parsing;
- path mapping;
- schema inspection;
- hash checks;
- provenance reconciliation;
- seed / condition / adapter / rollout mapping.

Use model reasoning for:

- scientific interpretation;
- identifying confounds;
- evaluating measurement validity;
- reconciling source discrepancies.

Do not launch broad literature searches or multiple research-agent lanes unless
explicitly requested.

This is not another project-selection search.