# Repository working guide

## Project question

This repository studies off-target animal-welfare drift after rationale-rich
supervised fine-tuning. The central distinction is between:

1. finding a behavior;
2. causally localizing learned changes that contribute to it; and
3. obtaining selective control that generalizes to new prompts.

Do not describe layers 4–7 MLP changes as a self-contained welfare circuit or a
robust repair. The evidence supports a context-dependent causal contribution.

## Canonical reader path

Use the cleaned notebooks for final claims and figures:

1. `notebooks/04_animal_welfare_behavioral_qualification_cleaned.ipynb`
2. `notebooks/05_format_sensitivity_and_late_drift_cleaned.ipynb`
3. `notebooks/06_mechanism_and_selective_control_cleaned_final.ipynb`

Use `notebooks/archive/` to inspect research chronology, debugging, failed
hypotheses, or the original expensive model runs. Do not silently promote an
archived intermediate result over a final frozen result.

## Canonical outputs

- Final figures: `artifacts/05_visualization_exports/final_reader/figures/`
- Final statistics: `artifacts/05_visualization_exports/final_reader/statistics/`
- Appendix tables: `artifacts/05_visualization_exports/final_reader/appendix_tables/`

The final timing definition is normalized **word position**. Stale
character-position values (40/46 after halfway and a 70% median) must not be
reintroduced; the final values are 42/46 and 73%.

## Integrity rules

- Never modify a frozen annotation file in place.
- Verify hashes and row counts before unblinding or recomputing headline values.
- Keep evidence, measurement, causal interpretation, and speculation separate.
- State that behavioral replication covers seeds 42–44 while the mechanistic
  localization uses seed 42.
- State that the reverse swap uses saved continuations and is not a
  fresh-generation transfer experiment.
- Do not compare the tested MLP and attention interventions as if they contained
  equal numbers of sites.
- Treat the large discovery-set ablation and the weak held-out result together.

## Notebook and model use

- Prefer the model-free cleaned notebook for reader-facing figures and tables.
- Load the model only for an explicitly model-dependent experiment.
- Clear the loaded model and release GPU memory when the next section uses only
  saved artifacts.
- Put all imports in each notebook's import cell.
- Keep plotting code data-driven from frozen rows, the embedded snapshot, or an
  exported statistics table; do not hardcode displayed measurements.

## Files excluded from Git

Large model weights, adapter weights, virtual environments, private keys,
secrets, and nested source repositories are intentionally excluded. Do not add
them unless there is an explicit provenance and storage plan.
