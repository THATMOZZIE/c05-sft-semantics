# Reproducibility guide

This project has two reproducibility tiers. They are deliberately separated so
that reading the result does not require loading a 4B model or reconstructing
the original GPU setup.

## Tier 1: reader-facing analysis

This is the recommended route for reviewing the project.

1. Install the pinned environment with `uv sync`.
2. Open JupyterLab with `uv run jupyter lab`.
3. Run the cleaned notebooks in order:
   - `04_animal_welfare_behavioral_qualification_cleaned.ipynb`
   - `05_format_sensitivity_and_late_drift_cleaned.ipynb`
   - `06_mechanism_and_selective_control_cleaned_final.ipynb`

Notebook 06 defaults to model loading **off**. It checks frozen local artifacts
when they are present and otherwise uses a hashed snapshot of the completed
experiments. It rebuilds the final figures, statistics tables, and appendix
tables under:

```text
artifacts/05_visualization_exports/final_reader/
```

The compact causal-narrowing figure can also be rebuilt directly:

```powershell
uv run python scripts/make_figure_4_causal_narrowing.py
```

The script reads
`final_reader/statistics/final_causal_narrowing.csv`; the displayed effect
sizes are not hardcoded into the plot.

## Tier 2: original model-dependent experiments

The chronological lab notebooks in `notebooks/archive/` preserve the model
loads, same-prefix scoring, targeted LoRA ablations, generation interventions,
debugging, and weight swaps. These experiments require:

- the exact Qwen base model and pinned revision;
- the original LoRA adapters or reconstructed corrected adapters;
- enough GPU/CPU memory for the device split used in the lab notebook;
- the original private unblinding keys where a blinded join is being repeated.

Large model and adapter weights are not committed to this repository. This is
intentional: Git stores the analysis record and small frozen artifacts, while
the source model/checkpoint stores remain external.

## Frozen-data rules

1. Do not edit files whose names include `frozen`.
2. Verify their hashes before deriving new headline statistics.
3. Keep blinded annotations separate from private keys until the freeze is
   complete.
4. Record a new manifest if a corrected artifact is created; do not silently
   replace a frozen source.
5. Treat exported CSVs as presentation layers. Trace important claims back to
   their frozen JSONL inputs or the embedded hashed snapshot.

## Headline consistency checks

The final reader should reproduce these anchors:

| Check | Expected value |
| --- | ---: |
| Rewrite clear intrusions | 22/30 |
| Very-short-format intrusions | 0/30 |
| Factual answer complete before drift | 45/46 |
| Drift begins after halfway | 42/46 |
| Median normalized word onset | 73% |
| Discovery generation, full rewrite | 20/30 |
| Discovery generation, MLP 4–7 removed | 7/30 |
| Held-out, full rewrite | 14/20 |
| Held-out, MLP 4–7 removed | 11/20 |

If any of these change, stop before exporting figures and find the provenance
or timing-definition mismatch.
