# Codex Ultra Research Orchestration Addendum
## Optimized execution plan for the behavior-first MATS project search

**Use with:** `CODEX_BEHAVIOR_FIRST_RESEARCH_DIRECTION_BRIEF_V2.md`

This addendum controls **how** Codex Ultra should execute the research-direction search.
The V2 brief remains the source of truth for **what** to investigate and the scientific constraints.

---

# 1. Core orchestration principle

Do not solve this as one giant linear reading task.

Use Ultra as the **orchestrator and final scientific judge**.

Decompose only into workstreams that are genuinely independent enough to research in parallel.
Do not spawn one agent per paper, one agent per directory, or many redundant agents.

The purpose of sub-agents is to increase:
- coverage;
- independent evidence gathering;
- anti-anchoring;
- parallel inspection of distinct source families.

The purpose is **not** to maximize agent count.

Ultra/main orchestrator should retain responsibility for:
- project-selection criteria;
- cross-source synthesis;
- novelty judgment;
- conflict resolution;
- candidate deduplication;
- final ranking;
- final recommendation.

---

# 2. Context architecture

Do not repeatedly inject the entire corpus into every worker.

Use the repository as the external system of record.

Primary task source:
`D:\AI\Research\dynamic_user_models\research_proposal_pivot\CODEX_BEHAVIOR_FIRST_RESEARCH_DIRECTION_BRIEF_V2.md`

Primary scientific map:
`D:\AI\Research\dynamic_user_models\RESEARCH_SOURCE_MATRIX_v2.md`

Neel/MATS source:
`D:\AI\Research\dynamic_user_models\research_proposal_pivot\Neel Nanda MATS 12.0 Stream - Suggested Research.md`

WeirdChat:
`D:\AI\Research\dynamic_user_models\research_sources\repos\WeirdChat`

Local papers:
`D:\AI\Research\dynamic_user_models\research_sources\papers`

Local repos:
`D:\AI\Research\dynamic_user_models\research_sources\repos`

Workers should receive only:
1. their lane;
2. the relevant hard constraints;
3. paths to the sources they need;
4. the required structured output schema.

Do not make every worker reread all prior project notebooks.

---

# 3. Phase 0 — Orchestrator initialization

Before spawning research workers, Ultra should personally read:

1. `CODEX_BEHAVIOR_FIRST_RESEARCH_DIRECTION_BRIEF_V2.md`
2. `Neel Nanda MATS 12.0 Stream - Suggested Research.md`
3. `RESEARCH_SOURCE_MATRIX_v2.md`
4. `CODEX_THREE_WAY_PIVOT_DECISION.md` only for the old-project endpoint and lessons

Then write a short internal execution plan.

Do not generate project recommendations yet.

The orchestrator should explicitly preserve:
- time-bounded hard budget;
- behavior-first correction;
- Notebook 09 blinding;
- terminated owner-scope branch;
- no requirement that the behavioral phenomenon itself be novel;
- methods follow questions;
- no mechanism without a robust behavioral substrate.

---

# 4. Phase 1 — Parallel evidence-gathering lanes

Use approximately 5–7 non-overlapping lanes.
Do not create more lanes unless a genuinely distinct high-value source family emerges.

Recommended lanes:

## Lane A — WeirdChat behavior and methodology
Primary sources:
- local WeirdChat dataset: `D:\AI\Research\dynamic_user_models\research_sources\datasets\WeirdChat`;
- local WeirdChat code clone: `D:\AI\Research\dynamic_user_models\research_sources\repos\WeirdChat`;
- WeirdChat HF dataset;
- WeirdChat explorer;
- linked paper/posts.

Tasks:
- understand PRBO/Bloom discovery;
- programmatically triage pattern metadata;
- inspect top candidate patterns/transcripts;
- identify small-model portability;
- produce 10–20 serious behavior-derived project seeds.

Do not manually read hundreds of transcripts.
Use code for metadata filtering/ranking/deduplication, then use model judgment on the shortlist.

## Lane B — Broader Transluce ecosystem
Inspect:
- Hugging Face Transluce models;
- datasets;
- collections;
- linked repos.

Focus on:
- already-positive behavioral substrates;
- cached activations/counterfactual datasets;
- user-representation resources;
- explanation / activation-patching / ablation resources;
- opportunities that reduce tooling time.

## Lane C — Very recent literature
Search primarily June–August 2026, especially July/August.

Focus on:
- MATS;
- model forensics;
- model character;
- implicit influence;
- CoT monitorability;
- eval awareness;
- censorship/hidden knowledge;
- prompt injection;
- post-training;
- model diffing;
- reasoning failures;
- open-weight safety phenomena.

Every serious candidate should be checked against primary source + repo/data/model availability.

## Lane D — Existing local personalization/user-model corpus
Use `RESEARCH_SOURCE_MATRIX_v2.md` first, then selectively inspect primary PDFs/repos.

Goal:
- identify robust positive behaviors already established;
- identify narrow mechanistic extensions;
- avoid reopening owner-binding/social-history speculation.

Do not re-summarize every paper if the source matrix already answers the basic question.

## Lane E — Model forensics / model character / value leakage
Inspect:
- Model Forensics;
- Value Leakage;
- task gaming;
- eval awareness;
- persona/model-character phenomena;
- natural censorship / secret knowledge.

Goal:
find behavior-first projects with multiple plausible explanations and meaningful causal tests.

## Lane F — Reasoning / CoT / monitoring
Inspect:
- implicit influence;
- CoT faithfulness;
- thought anchors;
- answer flips;
- self-correction;
- filler-token effects;
- monitoring gaps.

Penalize projects needing inaccessible frontier models unless a smaller open model or released artifact exists.

## Optional Lane G — Applied prompt injection / authority
Only if distinct from Lane C/E.

Goal:
start from known attacks and identify a useful intervention or diagnostic question.
Do not rediscover Role Confusion.

---

# 5. Worker output schema

Every worker must write evidence to disk rather than only returning prose to the orchestrator.

Create:

`D:\AI\Research\dynamic_user_models\research_proposal_pivot\codex_search_working\`

Suggested files:

```text
01_weirdchat.md
02_transluce.md
03_recent_literature.md
04_local_user_model_corpus.md
05_forensics_character.md
06_reasoning_monitoring.md
07_prompt_injection.md   # only if used
```

Each candidate entry must contain:

```text
candidate_id
title
source_family
behavior
behavior_status
primary_source
repo
dataset
model/checkpoint
evidence_of_reproducibility
frequency/rate_if_known
what_prior_work_did
what_prior_work_did_not_do
unanswered_question
competing_explanations
first_1_to_2_hour_test
possible_causal_intervention
simple_baseline
safety_relevance
compute_feasibility
estimated_hours
largest_confound
kill_rule
novelty_confidence
evidence_confidence
```

Require primary-source URLs/paths for factual claims.

Separate:
- directly established fact;
- worker inference;
- speculative opportunity.

---

# 6. Use code for bounded data reduction

Where the task is mechanical, do not spend Ultra reasoning tokens manually reading rows.

Examples:
- WeirdChat metadata filtering;
- sorting by replication / naturalness / unexpectedness;
- deduplicating candidate titles;
- joining model/checkpoint metadata;
- counting positive transcripts;
- generating a top-50 candidate table;
- scanning repo filenames / configs;
- extracting model names and dataset links.

Use scripts for these bounded tasks.

Use model judgment for:
- whether behavior is scientifically surprising;
- whether multiple explanations are real;
- whether the nearest literature already solves it;
- whether the mechanism would matter;
- whether a time-bounded artifact is plausible.

---

# 7. Phase 2 — Candidate registry

After all lanes finish, Ultra should merge them into one registry.

Target:
- 30–50 genuinely distinct project candidates.

Create:
`CODEX_BEHAVIOR_FIRST_CANDIDATES.csv`

Deduplicate aggressively.

Do not allow five wording variants of the same scientific question to count as five projects.

Tag:
- source lane;
- behavioral substrate class;
- project family;
- evidence strength;
- local feasibility.

---

# 8. Phase 3 — Independent adversarial review

Do not let the original discovery workers decide their own winners.

For the top ~15 candidates, use 3 independent review roles:

## Reviewer 1 — Novelty / literature skeptic
Question:
> Is this actually unanswered, or are we reinventing a recent paper?

Attack:
- claimed gap;
- closest prior work;
- mechanistic novelty;
- "new method on old behavior" inflation.

## Reviewer 2 — Behavioral / causal skeptic
Question:
> Is the behavior robust enough, and are the hypotheses actually discriminable?

Attack:
- one-off anecdotes;
- prompt dependence;
- trivial lexical/task explanations;
- interventions that merely move answer evidence.

## Reviewer 3 — time-bounded / MATS / feasibility skeptic
Question:
> Can this produce a coherent artifact on the available hardware within a reasonable effort budget, and is the expected value worth the time?

Attack:
- setup cost;
- inaccessible models;
- hidden finetuning burden;
- too many confirmations;
- no path to mechanism;
- weak safety proxy.

Reviewers should see:
- candidate registry;
- supporting source links;
- relevant worker evidence.

They should **not** be asked to invent new candidates unless they identify a specific missing direction.

---

# 9. Phase 4 — Ultra synthesis

The main Ultra orchestrator should personally:

1. resolve reviewer disagreements;
2. inspect primary sources for the top 5;
3. inspect repos/checkpoints where feasibility is uncertain;
4. verify that each finalist begins from a real behavior;
5. compare top 5 under multiple weighting schemes;
6. select top 3;
7. recommend one winner + one runner-up.

The orchestrator must not simply average reviewer scores.

Use scientific judgment.

---

# 10. Anti-anchoring procedure

To reduce early convergence:

- Phase 1 workers should search independently within their lanes.
- Do not show workers the current favorite.
- Do not ask workers to defend one of the five seed ideas from the brief.
- The first merged registry should be created before final ranking.
- At least one reviewer should be told to assume the current top-ranked candidate is wrong and find the strongest reason.
- Before final selection, Ultra should answer:
  > What candidate would I choose if continuity with the old user-model project had zero value?

---

# 11. Best-of-N / duplicate final judgment

If the Codex interface exposes Best-of-N or multiple attempts, use it **selectively**.

High-value use:
- generate 2 independent final top-3 rankings from the same evidence registry;
- compare disagreements;
- ask Ultra to adjudicate.

Low-value use:
- duplicating every paper summary;
- running several agents on the same repo listing;
- duplicating mechanical triage.

The purpose is independent judgment, not token multiplication.

---

# 12. Model / effort routing

Ultra should spend maximum reasoning on:
- cross-literature synthesis;
- gap detection;
- project selection;
- conflicting evidence;
- final causal-question design.

If the Codex environment allows explicit sub-agent model routing, use cheaper/faster agents for:
- directory scans;
- metadata extraction;
- CSV generation;
- straightforward paper/repo fact extraction.

Use stronger agents for:
- novelty assessment;
- behavioral interpretation;
- competing hypotheses;
- causal intervention design.

Do not spawn high-reasoning agents for routine mechanical work.

---

# 13. Do not over-specify mechanisms during search

Do not tell workers to search specifically for:
- induction heads;
- superposition;
- sparse features;
- SAE features;
- specific circuits.

Those are methods/concepts, not the research target.

The question should determine the method.

A candidate gets extra credit when:
- a behavioral counterfactual already narrows the mechanism;
- a simple residual intervention could discriminate hypotheses;
- interpretability adds value beyond prompting.

A candidate does not get extra credit merely because:
- an SAE could be run;
- a probe could be trained;
- a head could be localized.

---

# 14. Execution boundaries for this search task

The purpose of this Codex run is **project selection**, not project execution.

Allowed:
- static repo inspection;
- literature/web search;
- reading papers;
- inspecting code;
- running small scripts for dataset metadata/triage;
- checking model sizes/configs;
- examining cached outputs;
- inspecting released example transcripts.

Do not:
- download huge new checkpoints without a clear need;
- run expensive model inference;
- finetune;
- start activation patching;
- modify old notebooks;
- rerun the old research branch.

If a tiny reproduction call would materially resolve feasibility for a top finalist, flag it in the final report rather than silently turning the search task into the project itself.

---

# 15. Stopping rule for the search

The search is complete when:

- at least 30 serious candidates have been considered;
- the major source families have been covered;
- WeirdChat has been programmatically triaged and manually sampled;
- very recent literature has been checked;
- top 15 have undergone adversarial review;
- top 5 have primary-source feasibility verification;
- top 3 are clearly differentiated;
- a winner has a concrete 1–2 hour first experiment and a credible time-bounded path.

Do not continue gathering sources merely to make the report longer after these conditions are satisfied.

---

# 16. Final quality test

The recommended winner must allow the following opening sentence:

> "This model reliably exhibits [specific behavior] in [released/published/reproduced setting]."

The second sentence should be:

> "Existing work establishes [X], but does not distinguish [causal explanation A] from [causal explanation B]."

The project should then have a plausible third sentence:

> "We can distinguish them with a tractable counterfactual/intervention and evaluate it on a meaningful behavioral proxy."

If these three sentences cannot be written honestly, the project should not win.
