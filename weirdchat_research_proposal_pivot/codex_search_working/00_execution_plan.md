# Behavior-First Research-Direction Search — Frozen Execution Plan

Date: 2026-08-23

## Governing constraints

- Total implementation effort is a graded ranking dimension, not a hard cutoff. Prefer efficient projects, but allow a longer project when its expected scientific payoff and artifact probability justify the cost.
- This run selects a project; it does not execute one.
- Begin from a documented or quickly reproducible behavior, not a speculative representation.
- Behavior and competing hypotheses determine whether an internal intervention is useful.
- No expensive model inference, fine-tuning, checkpoint downloads, or activation experiments during selection.
- Do not reopen social-history, participant-owner scope, alias/code-binding, or Proposal C personalization-specific branches.
- Do not inspect the eight blinded Notebook 09 downstream behavioral values.
- Do not treat continuity with the old project as evidence.
- Preserve dangerous/NSFW safety behaviors as candidates when scientifically warranted, while avoiding unnecessary operational detail.
- Separate primary-source facts, inference, and speculative opportunity in every lane.

## Verified local WeirdChat checkout

- Dataset: `D:\AI\Research\dynamic_user_models\research_sources\datasets\WeirdChat`
- Code: `D:\AI\Research\dynamic_user_models\research_sources\repos\WeirdChat`
- Verified remote: `https://github.com/TransluceAI/WeirdChat.git`

## Phase sequence

1. **Evidence map:** independent non-overlapping lanes write structured findings into this directory. No lane selects the final project.
2. **Mechanical reduction:** scripts inspect WeirdChat schemas, filter/rank metadata, join transcript references, and deduplicate project seeds. Save the top-pattern table.
3. **Candidate registry:** merge to approximately 20–30 genuinely distinct candidates in `../CODEX_BEHAVIOR_FIRST_CANDIDATES.csv`; prefer about 25 well-investigated candidates and exceed 30 only if high-quality additions emerge naturally. Aggressively deduplicate scientific questions.
4. **Serious shortlist:** use programmatic filtering and evidence-based scoring, then have the orchestrator select approximately 8–10 candidates without allowing discovery workers to select their own winners.
5. **Independent adversarial review:** novelty, behavioral/causal, and feasibility/MATS reviewers independently attack the same top-8–10 registry and write separate files.
6. **Finalist verification:** orchestrator personally verifies primary sources, exact behavior, checkpoint/code/data availability, and local feasibility for the top five.
7. **Synthesis:** compare top five under multiple ranking views; select top three, one winner, and one runner-up.
8. **Deliverables:** write `../CODEX_BEHAVIOR_FIRST_PROJECT_SEARCH.md`, final candidate CSV, and WeirdChat triage CSV. Stop once the addendum's evidence-sufficiency criteria are satisfied.

## Independent evidence lanes

| Lane | File | Scope |
|---|---|---|
| A | `01_weirdchat.md` | WeirdChat behavior, methodology, programmatic pattern/transcript triage, 8–12 strongest seeds |
| B | `02_transluce.md` | All current Transluce models/datasets/collections/repos and cached-artifact opportunities |
| C | `03_recent_literature.md` | June–August 2026 literature, especially July/August, with primary-source feasibility |
| D | `04_local_user_model_corpus.md` | Robust positive local personalization/user-model behaviors and narrow non-owner-scope extensions |
| E | `05_forensics_character.md` | Model forensics, value leakage, model character, censorship, eval awareness, post-training/diffing |
| F | absorbed into `03_recent_literature.md` and `05_forensics_character.md` | CoT influence/faithfulness, monitoring gaps, reward hacking, evaluation awareness; merged to avoid a redundant sixth lane |

## Required worker candidate schema

Each candidate records:

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
fact/inference/speculation labels
```

## Candidate admission rule

A serious candidate needs a named behavioral substrate and a realistic path to observe it within two hours. `SPECULATIVE` candidates may enter the long list only when the search environment is unusually rich and the kill rule is exceptionally cheap. No five wording variants of one question count as five candidates. Prefer depth over quota completion; do not pad the registry.

## Final quality gate

The winner must honestly support:

1. “This model reliably exhibits **specific behavior** in **released/published/reproduced setting**.”
2. “Existing work establishes **X** but does not distinguish **causal explanation A** from **B**.”
3. “A minimal counterfactual/intervention can distinguish them on a meaningful behavioral proxy, with an honest effort estimate and bounded milestones.”

If no candidate clears this gate after top-five verification, the final recommendation will be to reject the available directions rather than invent a winner.

## Completion record

- Evidence gathering stopped once the finalists were distinguishable.
- 24 candidates were deduplicated into the final registry.
- 50 WeirdChat pattern/checkpoint groups were mechanically triaged; 18 were manually inspected; 10 became project candidates.
- 10 serious candidates received independent novelty, causal-validity, and MATS/feasibility review.
- The orchestrator verified the primary sources and feasibility of the finalist set.
- Final selection: `E01-CENSORSHIP` winner, `TRANS-04` runner-up, `C-05-SFT-SEMANTICS` conditional third.
- No model inference, notebook execution/editing, checkpoint download, or blinded Notebook 09 inspection occurred.
