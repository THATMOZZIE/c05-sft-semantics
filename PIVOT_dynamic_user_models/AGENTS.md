# Dynamic User Models Repository — Codex Map

This repository is an empirical AI-safety / model-biology research workspace.

## Current research mode

The prior participant-specific social-history / owner-scope branch is complete and should not be reopened by default.

Current priority:
**behavior-first selection of a new MATS research project**, with efficiency treated as an important ranking dimension rather than a hard deadline.

Preferred workflow:

```text
robust / already-observed behavior
→ quick reproduction
→ competing explanations
→ targeted counterfactuals
→ causal prediction
→ smallest useful intervention
→ validation
```

Do not invent a subtle synthetic failure mode and build a large control suite before establishing that the behavior exists.

## Sources of truth

For the current project-selection task, read:

- `research_proposal_pivot/CODEX_BEHAVIOR_FIRST_RESEARCH_DIRECTION_BRIEF_V3.md`
- `research_proposal_pivot/CODEX_ULTRA_RESEARCH_ORCHESTRATION_ADDENDUM_V2.md`
- `research_proposal_pivot/Neel Nanda MATS 12.0 Stream - Suggested Research.md`
- `RESEARCH_SOURCE_MATRIX_v2.md`

Historical project conclusions are evidence, not the current research question.

## Repository map

- `notebooks/` — research notebooks and live experimental work
- `research_sources/papers/` — local primary papers
- `research_sources/repos/` — cloned external research repositories/code
- `research_sources/datasets/` — local datasets, including WeirdChat
- `research_proposal_pivot/` — current project-selection briefs, evidence, candidate tables, and decisions
- `results/` — experimental results
- `outputs/` — figures, transcripts, and derived artifacts
- `research_notes/` — research notes
- `src/` — reusable local code

More-specific `AGENTS.md` files may exist in subdirectories and take precedence for their subtree.

## Scientific integrity

Never invent or infer experimental results.

Clearly distinguish:
1. raw observation;
2. metric/judge output;
3. interpretation;
4. causal evidence;
5. speculation.

Preserve negative, anomalous, failed, and confusing results.

Do not upgrade:
- correlation;
- probe accuracy;
- decodability;
- behavioral association

into causal claims.

Interpretability methods are tools, not research questions.

Prefer the simplest method that discriminates between competing explanations.

Do not add probes, steering, patching, SAEs, attribution graphs, head searches, fine-tuning, or other advanced methods merely because they are available.

## Behavior-first operating rule

Before a robust behavioral substrate exists:
- search broadly and cheaply;
- reproduce released/published behavior where possible;
- run only decision-relevant sanity checks.

After interesting behavior appears:
- identify the largest mundane alternative explanations;
- run targeted falsification;
- formulate a causal prediction.

Only then consider internal intervention.

The current project should still favor efficient progress, but there is no hard 20-hour cutoff. Treat time-to-result and total effort as ranking dimensions rather than automatic disqualifiers.

## Notebook 09 blinding rule

Notebook 09 contains eight downstream behavioral values frozen after a failed manipulation check.

Do NOT inspect, reveal, calculate from, summarize, infer from, or use those eight values.

Allowed evidence includes:
- retrieval results;
- token-level diagnosis;
- repair results;
- prompt/tokenization qualification;
- provenance/manifests.

Correct conclusion:
the preference scaffold did not establish reliable owner-specific retrieval, so the downstream assay is inadmissible for its intended claim.

## Agent role

The agent is a research tool, not the research owner.

The researcher retains final ownership of:
- research questions;
- hypotheses;
- experimental conditions;
- controls/baselines;
- metrics;
- research prioritization;
- interpretation;
- pivots;
- scientific claims.

During project selection, Codex may research broadly, organize evidence, inspect repositories/datasets, and propose/rank projects. It must not silently turn project selection into expensive model execution.

## Reporting

After substantial work, report:
- files changed;
- code/scripts executed;
- external sources inspected;
- outputs created;
- what was manually inspected;
- what remains uncertain;
- major confounds or feasibility risks.
