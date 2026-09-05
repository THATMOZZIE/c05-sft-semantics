# Dynamic User Models Research

This repository contains a MATS 12 empirical AI-safety / model-biology
research project investigating dynamic participant-specific user models.

## Project Goal

The current research question is approximately:

Do language models bind prior interaction histories to specific conversational participants, and can those histories selectively influence later neutral behavior or judgments involving those participants?

Can irrelevant participant-bound social history contaminate an otherwise impartial judgment?

The initial research is behavioral.

Do NOT assume:
- a persistent internal representation exists;
- an observed effect is participant-specific;
- an observed effect reflects "resentment", emotion, dislike, or revenge;
- mechanistic methods are necessary.

The project should follow evidence.

---

## Jupyter notebook safety

- NEVER edit `.ipynb` files directly as text or JSON.
- NEVER use filesystem patches, sed, search/replace, or Python JSON rewriting on `.ipynb` files.
- All notebook cell creation, editing, deletion, and execution must go through the Jupyter MCP tools.
- If the Jupyter MCP server is unavailable, STOP and tell me. Do not fall back to direct `.ipynb` editing.
- Never restart or shut down the Jupyter kernel without asking me first.
- Treat the existing live kernel state as valuable and persistent.
- Load expensive models and datasets once in dedicated setup cells near the top.
- Save expensive derived artifacts such as activations, datasets, and checkpoints to disk.
- Save important plots to PNG in addition to displaying them inline.

## Jupyter

- Treat the live Jupyter kernel as persistent research state.
- NEVER restart or shut down the kernel without asking the researcher first.
- NEVER clear all outputs or restart-and-run-all without explicit permission.
- Put model loading, data loading, API clients, seeds, and experiment
  configuration in dedicated cells near the top of the notebook.
- Reuse already-loaded models and data rather than unnecessarily reloading them.
- Do not silently create additional kernels.
- Save expensive intermediate artifacts to disk when appropriate.
- Save important plots to `outputs/figures/` as PNG files in addition to
  displaying them inline.
- Save raw model generations and transcripts to `outputs/transcripts/`
  before scoring, filtering, summarizing, or transforming them.
- Do not silently alter:
  - prompts;
  - model IDs;
  - seeds;
  - temperatures;
  - sampling parameters;
  - system prompts;
  - scoring rubrics;
  - experimental conditions.
- Prefer surgical edits to individual cells or insertion of new cells over
  wholesale notebook rewrites.
- Do not overwrite researcher-authored cells unless explicitly asked.

---

## Research Integrity

- NEVER invent, infer, or fabricate experimental results.
- Inspect the actual raw outputs underlying important claims.
- Treat a successful-looking result as a hypothesis until it has been
  sanity-checked.
- Preserve negative, anomalous, failed, and confusing results.
- Do not selectively remove inconvenient outputs unless there is a documented
  methodological reason.
- For load-bearing quantitative findings, retain enough raw data to reproduce
  the number independently.
- Where practical, independently recompute important headline metrics.
- Check that the numbers reported in notes or write-ups agree with the actual
  experiment outputs.
- Inspect examples classified as positive, negative, or anomalous by automated
  metrics or judges.

Clearly distinguish:

1. raw observation;
2. metric or judge output;
3. interpretation;
4. causal evidence;
5. speculation.

Do not upgrade correlation, probe accuracy, or decodability into a causal claim.

---

## Experimental Design

Before implementing a major experiment, explicitly identify:

1. the hypothesis being tested;
2. at least one competing explanation;
3. the manipulated variable;
4. what is held constant;
5. the primary outcome metric;
6. the relevant control or baseline;
7. what possible outcomes would update our beliefs.

The experimental design, controls, baselines, and interpretation must remain
under researcher control.

Do not run a large experiment simply because it is easy to automate.

Prefer experiments that discriminate between competing explanations.

Start with the simplest experiment capable of answering the question.

---

## Current Competing Explanations

When relevant, consider alternatives such as:

- no persistent state;
- immediate tone matching;
- global conversation carryover;
- participant / speaker identity leakage;
- recency or order effects;
- positive favoritism;
- generic abuse-handling policy;
- narrative or role-play inference;
- normative reciprocity;
- competence or reliability inference rather than treatment-history bias;
- scoring noise or judge bias.

Do not interpret a participant-specific treatment effect until obvious simpler
explanations have been checked.

---

## Scope Control

Do not autonomously expand the project.

In particular, do NOT add:

- probes;
- steering;
- activation patching;
- path patching;
- SAEs;
- attribution graphs;
- DLA;
- model diffing;
- fine-tuning;

merely because they are available or technically impressive.

Internal interpretability methods should be introduced only when a behavioral
result motivates a concrete question they can answer.

A simple behavioral counterfactual or baseline is preferable when it answers
the same question.

One strong finding investigated deeply is better than many shallow experiments.

If an experiment reveals that the original hypothesis is wrong, surface that
clearly rather than trying to rescue the original idea.

---

## Raw Data First

Frequently inspect:

- complete prompts;
- complete model responses;
- conversation histories actually sent to the model;
- participant labels;
- generated condition assignments;
- samples behind aggregate metrics;
- surprising datapoints;
- disagreements between automated scoring and manual inspection.

Do not rely entirely on aggregate scores.

Before trusting a pipeline, manually inspect representative examples from each
condition.

---

## Agent Use

The agent is a research tool, not the research owner.

The agent may freely help with:

- boilerplate;
- repetitive experiment execution;
- data serialization;
- plotting;
- API wrappers;
- refactoring;
- mechanical checks;
- candidate analyses;
- literature/context organization.

The researcher retains ownership of:

- research questions;
- hypotheses;
- experimental conditions;
- controls;
- baselines;
- metric choice;
- research prioritization;
- interpretation;
- decisions to pivot;
- scientific claims;
- conclusions.

Agent-generated code must remain understandable and auditable.

If uncertain about a consequential research decision, surface the decision and
alternatives rather than silently choosing one.

---

## Research Notes

Maintain a running record of:

- hypotheses;
- why experiments were run;
- predictions made before seeing results;
- important outputs;
- failed hypotheses;
- anomalies;
- interpretation changes;
- unresolved confounds;
- next-step decisions.

Do not rewrite the history of the project to make it appear cleaner than it was.

Negative and inconclusive results are valid research results.

---

## Reporting After Substantial Work

After substantial agent work, report:

- which files or notebook cells changed;
- what code was executed;
- what model/data/settings were used;
- what outputs were produced;
- what was manually inspected;
- what sanity checks were performed;
- what remains unverified;
- any unexpected behavior or possible confounds.

Do not describe an experiment as successful until its key outputs have been
checked.

## Notebook and Kernel Identity

Research notebooks are stored under `notebooks/` and numbered sequentially by
experimental stage.

Before reading, modifying, or executing notebook content:

1. Confirm the intended notebook path.
2. Confirm the intended existing kernel ID.
3. Never assume the newest-numbered notebook is the active notebook.
4. Never assume one notebook corresponds to one kernel.
5. Multiple notebooks may intentionally share the same persistent kernel.
6. Do not create a new kernel unless explicitly requested.

When using Jupyter MCP:

- Prefer an explicitly configured existing `CODE_SANDBOX_ID`.
- Set `START_NEW_CODE_SANDBOX=false` when preserving existing research state.
- Do not use `use_notebook` if doing so may silently create or switch kernels.
- Before substantial work, verify the expected live state with a harmless
  fingerprint such as checking for known existing variables.
- If the notebook path or kernel identity is ambiguous, STOP and ask.


## Exploratory vs Confirmatory Evidence

Clearly label experiments as exploratory or confirmatory.

Exploratory experiments may be used to:
- discover effects;
- debug confounds;
- calibrate prompts;
- choose metrics;
- generate hypotheses.

Do not present statistical evidence from adaptively discovered contrasts as
though the hypothesis, metric, conditions, and analysis were fixed in advance.

Before a confirmatory experiment:
- freeze the primary hypothesis;
- freeze conditions and controls;
- freeze the primary metric;
- freeze the sample size or stopping rule;
- freeze the seed-generation procedure where applicable;
- record the prediction before viewing results.

Prefer held-out participant identities, scenarios, prompts, and/or seeds for
confirmation after exploratory development.


## Matched Experimental Conditions

When comparing paired or factorial conditions:

- Use matched inference settings across conditions.
- Use shared seeds across paired conditions when the design calls for it.
- Change only the intended manipulated variable.
- Before generation, print or inspect representative complete prompts from
  every condition.
- Record condition metadata separately from model-visible prompt content.
- Do not infer experimental condition from output text when it can be stored
  explicitly.
- Preserve the mapping between seed, condition, prompt, and raw response.