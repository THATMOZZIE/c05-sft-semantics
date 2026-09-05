# Notebook-specific Codex Instructions

These instructions apply to `notebooks/`.

## Notebook safety

- NEVER edit `.ipynb` files directly as text or JSON.
- NEVER use filesystem patches, sed, search/replace, or Python JSON rewriting on `.ipynb`.
- All notebook cell creation/editing/deletion/execution must go through the configured Jupyter tooling.
- If the required Jupyter tool/server is unavailable, STOP rather than falling back to direct file editing.
- Never restart or shut down a live kernel without explicit permission.
- Never silently create or switch kernels.
- Treat live kernel state as valuable persistent research state.
- Confirm the intended notebook and existing kernel before substantial work.
- Prefer surgical cell edits/insertion over wholesale rewrites.
- Do not overwrite researcher-authored cells unless explicitly asked.

## Experiment state

- Reuse already-loaded models/data when appropriate.
- Put expensive model/data setup in dedicated cells.
- Save expensive derived artifacts to disk.
- Save important figures to `outputs/figures/`.
- Save raw generations/transcripts before scoring or summarizing.
- Do not silently change prompts, model IDs, seeds, temperatures, system prompts, sampling parameters, rubrics, or conditions.

## Experimental integrity

Before a major confirmatory experiment, identify:
- hypothesis;
- competing explanation;
- manipulated variable;
- held-constant variables;
- primary outcome;
- baseline/control;
- predicted updating outcomes.

Exploratory work may be lighter-weight. Label exploratory versus confirmatory evidence honestly.

Inspect representative raw prompts/responses before trusting aggregates.

Preserve mapping between seed, condition, prompt, and raw output.
