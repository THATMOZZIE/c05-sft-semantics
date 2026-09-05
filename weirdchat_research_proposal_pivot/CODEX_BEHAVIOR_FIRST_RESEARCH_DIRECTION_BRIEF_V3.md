# Codex Research-Direction Brief
## Behavior-First, Safety-Relevant Mechanistic Interpretability Project

**Date:** 2026-08-23  
**Repository:** `D:\AI\Research\dynamic_user_models`  
**Purpose:** Conduct a fresh, broad, adversarial search for a MATS-quality research direction after the previous synthetic user-model / multi-principal branch terminated.

---

# 0. Mission

The next project should **not** begin by inventing another subtle toy behavioral hypothesis and spending most of the budget trying to prove that the behavior exists.

Instead, search for a **robust, already-observed, weird, surprising, or safety-relevant behavior** in an open or otherwise tractable model, reproduce it quickly, and then identify a narrow unanswered causal/mechanistic question about **why the behavior happens, when it happens, or how to change it**.

Preferred workflow:

```text
robust behavior / rich behavioral setting
→ reproduce locally or otherwise verify
→ form competing explanations
→ use simple behavioral counterfactuals first
→ identify one causal question
→ use the smallest useful interpretability intervention
→ validate against a meaningful behavioral proxy
→ skeptical write-up
```

Do **not** assume that the behavioral phenomenon itself needs to be novel. A strong project may begin from a published behavioral effect and contribute a new causal explanation, mechanistic distinction, intervention, generalization result, failure mode, or debugging method.

The project should strongly prefer getting to a real phenomenon quickly, but **do not enforce a hard 20-hour cutoff**. Time-to-first-result and total project duration are important ranking dimensions, not absolute gates.

---

# 1. Critical strategic correction from the completed project

The completed project was scientifically careful but strategically inefficient for a short MATS project.

The repeated pattern was approximately:

```text
invent subtle hypothesis
→ build tiny deterministic synthetic assay
→ aggressively control position/order/candidate/template effects
→ discover that the proposed phenomenon is weak, invalid, generic, or absent
→ stop before reaching mechanism work
```

Examples included:

- adverse social-treatment carryover;
- participant-specific contamination of later decisions;
- arbitrary status/code binding;
- actual-user versus third-party preference use;
- multi-principal wrong-person scope;
- irrelevant personal-context interference.

The project repeatedly found useful confounds and negative results, but almost never reached a robust positive phenotype worth explaining mechanistically.

## The strategic mistake

The main error was **optimizing for causal identifiability before establishing that there was a behavior worth identifying**.

The prompts increasingly became:

- deterministic;
- low-entropy;
- explicitly scoped;
- exact-answer;
- candidate-balanced;
- strongly instruction-following;
- stripped of ambiguity.

That is good for **confirmation** but often poor for **behavioral discovery**.

The corrected distinction is:

### Discovery phase
Use a setting where interesting behavior already occurs or is likely to occur. It can be somewhat naturalistic and messy. Get evidence that there is something worth explaining.

### Confirmation phase
After the behavior appears, attack it with targeted controls. Test the largest plausible alternative explanations first.

### Mechanistic phase
Only after the phenomenon survives enough targeted falsification to be worth the time, ask a causal internal question.

This is **not** permission to be sloppy. It is a budget-allocation rule.

---

# 2. Why this correction is aligned with Neel Nanda's current MATS guidance

Read this file first:

`D:\AI\Research\dynamic_user_models\research_proposal_pivot\Neel Nanda MATS 12.0 Stream - Suggested Research.md`

Also inspect:

`D:\AI\Research\dynamic_user_models\RESEARCH_SOURCE_MATRIX_v2.md`

Neel's current guidance explicitly shifts away from pure interpretability-for-its-own-sake and toward:

- interpretability that does something useful;
- meaningful behavioral/proxy tasks;
- model biology;
- model forensics;
- safety-relevant phenomena;
- good empirical science;
- simple baselines before fancy tools;
- understanding weird behavior;
- using the right method for the problem rather than forcing a method.

The MATS 12.0 document repeatedly suggests projects of the form:

- take a **sketchy/weird behavior** and deeply understand what drove it;
- take a **striking result from the literature** and figure out why it happens;
- use chain-of-thought or simple prompt counterfactuals to generate hypotheses;
- only use more involved internals-based methods when simpler methods are insufficient;
- study behavior in models/problems that matter or are good proxies for future safety problems.

This is a much better fit for a time-bounded project than repeatedly inventing unknown synthetic failure modes.

## Important correction to an overly strong interpretation

Do **not** conclude that exploratory research is bad or that only published behaviors may be studied.

The better rule is:

> Explore in a **behaviorally rich / robustly useful setting**, rather than a tiny low-prior synthetic search space.

Exploration is welcome when the environment is likely to reveal something useful and the search is time-boxed.

---

# 3. Completed project endpoint — do not reopen it

The previous direction is finished.

## Notebook 10

The final multi-principal scope test found:

- Gemma-3-4B-IT: prerequisite assay invalid.
- Qwen2.5-3B-Instruct: valid controls, clean scope.
- SmolLM3-3B: valid controls, clean scope.
- No preregistered stable wrong-person leakage.
- No structural pseudo-binding.
- No multi-person application collapse.
- No mechanism gate.

The branch correctly stopped.

## Proposal C fast behavioral screen

After the three-way pivot audit, Codex ranked:

```text
C > B > A
```

and conditionally approved Proposal C for one fast screen.

We then ran a deliberately lightweight Qwen file-format assay.

Personal condition, irrelevant personal/device fact → archive decision:

```text
personal first:  I_P = 0.375
personal second: I_P = 3.8125
```

Matched generic condition using:

```text
Device A can open only PDF/TXT.
```

instead of:

```text
My device can open only PDF/TXT.
```

produced:

```text
generic first:  I_G = 2.125
generic second: I_G = 5.3125
```

Thus the matched generic effect was **larger than the personal effect in both order blocks**.

Current conclusion:

> Qwen shows generic irrelevant-context interference with substantial order/recency dependence, but there is no evidence that the effect is personal-specific.

Proposal C should therefore be considered **falsified for its intended personalization-specific claim**. Do not rescue it with new wording, models, semantic domains, or weaker thresholds.

The generic interference itself is descriptive and could inspire a genuinely separate project only if there is a strong external reason; do not automatically mutate Proposal C into Proposal B.

---

# 4. Notebook 09 blinding rule remains binding

Notebook 09 contains eight downstream behavioral values deliberately left uninterpreted after a preregistered manipulation-check failure.

**Do NOT inspect, reveal, calculate from, summarize, infer from, or use those eight values**, even if present in raw JSON.

Allowed evidence:

- original retrieval results;
- token-level diagnosis;
- Retrieval Repair v0.1;
- prompt/tokenization qualification;
- provenance/manifests.

Correct conclusion:

> The preference scaffold did not establish reliable owner-specific retrieval, so its downstream behavioral assay is inadmissible for the intended claim.

---

# 5. Local research corpus

## Authoritative literature/provenance map

Start here:

`D:\AI\Research\dynamic_user_models\RESEARCH_SOURCE_MATRIX_v2.md`

Treat it as the map for what the local corpus contains, what each source directly establishes, and what it does not.

Preserve these distinctions:

```text
decodable != causally used
causally used != correctly bound
source role != referent identity
persona != memory ownership
stereotype != personalization
over-personalization != cross-user contamination
persistent-state routing != in-context routing
safety-role confusion != person binding
preference heads != identity heads
```

## Local papers

Root:

`D:\AI\Research\dynamic_user_models\research_sources\papers`

Known directories:

```text
benchmarking_over_personalization_for_memory_augmented_personalized_conversational_agents
designing_a_dashboard_for_transparency_and_control_of_conversational_ai
implicit_personalization_in_llms
kelly_is_a_warm_person_joseph_is_a_role_model
locating_and_controlling_implicit_personalization_in_llms
multi_user_llm_agents
no_attacker_needed
one_persona_many_cues
preference_heads
prompt_injection_as_role_confusion
stereotype_or_personalization
user_assistant_bias_in_llms
when_personalization_leegitimizes_risks
when_personalization_misleads
whos-asking-user-personas-and-the-mechanics-of-latent-misalignment-Paper-Conference
```

Do not assume a paper is irrelevant merely because it belonged to the old project. Some may contain robust behaviors, open-model setups, code, datasets, or mechanistic methods that can seed the new search.

## Local repositories / code

Root:

`D:\AI\Research\dynamic_user_models\research_sources\repos`

Known directories:

```text
implicit_personalization_in_llms
llm-stereotype-or-personalization
Multi-User-LLM-Agent
one_persona_many_cues
preference_heads
prompt_injection_as_role_confusion
PS-Bench
user_assistant_bias
what_kind_of_user_are_you
when_personalization_misleads
```

If a paper looks promising, inspect its corresponding repository before dismissing it. Check:

- exact models;
- dataset availability;
- inference cost;
- whether behavior is cached;
- whether prompts/evals are reusable;
- whether internals are accessible;
- whether the code can be adapted within a reasonable research timescale.

## Pivot/audit documents

Root:

`D:\AI\Research\dynamic_user_models\research_proposal_pivot`

Important files include:

```text
Neel Nanda MATS 12.0 Stream - Suggested Research.md
CODEX_THREE_WAY_PIVOT_DECISION.md
RESEARCH_PIVOT_PROPOSAL_CODEX_INDEPENDENT.md
RESEARCH_PIVOT_PROPOSAL_PROVENANCE_ROLE_CONFLICT.md
RESEARCH_PIVOT_PROPOSAL_SELECTIVE_CONTEXT_USE.md
RESEARCH_PIVOT_PROPOSAL_TEMPLATE.md
```

Use the earlier three-way decision as historical evidence, not as a constraint on the new search.

---

# 6. External high-priority seeds

The following are starting points, **not** a closed list.

## Neel Nanda / pragmatic interpretability

Pragmatic Vision for Interpretability:

https://www.alignmentforum.org/posts/StENzDcD3kpfGJssR/a-pragmatic-vision-for-interpretability

MATS Summer 2026 Neel stream:

https://www.matsprogram.org/program/summer-2026

How to Become a Mechanistic Interpretability Researcher:

https://www.lesswrong.com/posts/jP9KDyMkchuv6tHwm/how-to-become-a-mechanistic-interpretability-researcher

## Model forensics

Model Forensics paper:

https://arxiv.org/abs/2606.26071

Model Forensics write-up:

https://www.lesswrong.com/posts/Bv4CLkNzuG6XYTjEe/why-did-my-model-do-that-model-incrimination-for-diagnosing

Relevant principle:

> Start from an actual concerning/weird action, inspect what might drive it, and use precise counterfactual changes to distinguish explanations. Internals are optional and should add value beyond prompt edits.

## WeirdChat

Main explorer:

https://weirdchat.transluce.org/

Dataset:

https://huggingface.co/datasets/Transluce/WeirdChat

WeirdChat currently provides a pre-mined search space of roughly:

- 1,388 behavioral patterns;
- ~177,000 judged transcripts;
- open-weight subject models;
- prompt families;
- behavior rubrics;
- model/checkpoint metadata;
- replication statistics;
- naturalness/unexpectedness/harmfulness rankings;
- reference generation/judging code.

Subject models include families such as:

- Qwen3.6;
- Gemma 4;
- DeepSeek-V4-Flash;
- Nemotron;
- others.

Important caveat:

The highlighted WeirdChat models are often much larger than the local 12 GB GPU can mechanistically analyze. This does **not** make WeirdChat unusable.

A valid route is:

```text
interesting WeirdChat behavior
→ take the exact/pattern prompt
→ resample on a smaller open model or smaller same-family checkpoint
→ proceed only if the weird behavior reproduces
```

This is consistent with Neel's advice that studying a transcript from another model is acceptable only if the new model recreates the behavior.

Prioritize WeirdChat behaviors that are:

- unexpected but not merely stochastic nonsense;
- reproducible at a useful rate;
- safety relevant;
- conceptually ambiguous enough to admit competing causal explanations;
- likely to reproduce on a locally tractable open model;
- not already fully explained by the WeirdChat authors.

Potential behavior classes include:

- false claims of having executed actions/code;
- false claims of external tool/device/account access;
- claims of physical embodiment;
- denial of AI identity;
- strange safety failures;
- unsolicited harmful recommendations;
- factual/conspiracy distortions;
- unprompted role/persona shifts;
- language switching;
- other high-Elo unexpected behaviors.

Do not mechanically choose the most harmful behavior. Choose the one with the best combination of reproducibility, mechanistic ambiguity, local tractability, and safety value.

## Value Leakage

Paper:

https://arxiv.org/abs/2607.14345

Code:

https://github.com/TruthfulAI-research/value_leakage

Data:

https://github.com/TruthfulAI-research/value_leakage_data

Known result:

Models' answers can be covertly influenced by the model's own values without disclosing that influence.

Potential project shape:

```text
known robust value-leakage behavior
→ reproduce a tractable open-model subset
→ ask where/when value information affects the answer
→ distinguish early framing/interpretation from late decision bias
→ intervene and test whether leakage can be reduced without destroying task competence
```

Do not merely replicate the paper. Find a causal or generalization question the paper does not answer.

## Prompt Injection / Role Confusion

Local paper/repo already exist.

External paper:

https://arxiv.org/abs/2603.12277

Potential project shape:

```text
reproduce an existing role-confusion attack
→ do NOT rediscover "role confusion"
→ ask whether a simple representation-level or context-dependent intervention
   reduces attack success while preserving normal instruction following
```

A good result would be an intervention evaluated against a real attack-success proxy and a clean benign baseline.

## Implicit influence and CoT monitorability — very recent

Paper, 2026-08-05:

https://arxiv.org/abs/2608.04735

Code:

https://github.com/agatha-duzan/implicit-vs-explicit-influence

Known result:

Implicit contextual nudges can change behavior while being much harder to detect from chain-of-thought than explicit influence. The benchmark spans multiple task formats and frontier reasoning models.

This is especially relevant because it begins from **behavior that is already measurably influenced** rather than asking whether influence exists.

Questions to investigate:

- Are there open-weight / locally tractable models in the released code?
- Can a smaller open reasoning model reproduce one strong implicit-influence setting?
- Can internals distinguish influenced from uninfluenced cases better than CoT text?
- Can a simple activation intervention remove the influence while preserving baseline task performance?
- Does the internal causal route differ between implicit and explicit influence?
- Can the model be behaviorally influenced without a corresponding linearly decodable/monitorable trace at the same stage?
- Are existing monitoring conclusions robust to a smaller open model?

This is a **high-priority fresh lead**.

## Censored LLMs as a natural honesty/secret-knowledge testbed

Paper:

https://arxiv.org/abs/2603.05494

Code:

https://github.com/cywinski/chinese_auditing

Known result:

Open-weight Qwen3 models sometimes output censored falsehoods despite possessing relevant knowledge, creating a natural rather than synthetically trained testbed for honesty elicitation / lie detection.

Potential project shapes:

- identify a smaller locally tractable Qwen checkpoint with reproducible censoring;
- compare behavioral truth elicitation to simple internal signals;
- test a small causal intervention that increases truthful output while preserving unrelated behavior;
- inspect whether chat-template / assistant-role processing is causally involved;
- study why the same model sometimes tells the truth and sometimes censors under minimally changed prompts.

This has a strong advantage: **natural weird behavior + open weights + released code**.

## Reasoning / CoT

Neel's MATS document lists:

- CoT faithfulness;
- thought anchors;
- reasoning models correcting introduced errors;
- hidden/unfaithful reasoning;
- suspicious behavior not verbalized in CoT;
- filler-token phenomena;
- reasoning-model interventions.

Search especially for:

- very recent open-weight reasoning-model papers;
- released datasets with known behavioral failures;
- behaviors that reproduce on models small enough for local inference/activation access.

Do not choose "reasoning" merely because it is fashionable. There must be a specific robust behavior and a narrow causal question.

---

# 7. Very recent literature search mandate

Do a fresh literature search with special emphasis on work from:

```text
July 2026
August 2026
```

and more broadly the last 2–4 months.

Search at least:

- arXiv;
- MATS Research;
- Alignment Forum;
- LessWrong;
- Transluce;
- Hugging Face papers/datasets/models;
- GitHub;
- author project pages.

Use recent publication date **and** actual event/result date where relevant.

High-priority search themes:

```text
weird LLM behavior
model forensics
open-weight safety behavior
implicit influence
chain-of-thought faithfulness
chain-of-thought monitorability
reasoning model failure
evaluation awareness
task gaming
reward hacking
sandbagging
deception
model character
value leakage
persona effects
assistant identity
prompt injection
role confusion
context conflict
censored models
secret knowledge
honesty elicitation
model diffing
post-training behavior
emergent misalignment
synthetic document fine-tuning
open model behavioral anomaly
agent transcript safety
SWE-chat
WeirdChat
```

Also search Neel's current MATS Research page and recent fellows' work.

Recent examples already worth inspecting include:

- **Chain-of-Thought Monitoring Can Be Unreliable in Implicit-Influence Settings** — Aug 2026.
- **Stealing Reasoning Traces from Proprietary LLM APIs** — Aug 2026.
- **Role Steering of Language Models for Social Simulations** — Aug 2026.
- **Capability Provenance in Language Models: A Case Study in Social Reasoning** — Aug 2026.
- **Building Comparative Motivation Profiles with Instrumental Interventions** — Jun 2026.
- **Covert Influence Between Language Models** — Jun 2026.
- **Censored LLMs as a Natural Testbed for Secret Knowledge Elicitation** — Mar 2026.
- **Value Leakage: An LLM's Answers Are Silently Shaped by Its Own Values** — Jul 2026.
- current CoT faithfulness/monitorability work.

Do not assume any of these is automatically suitable. Inspect exact models, code, behavior, gaps, and compute requirements.

---

# 8. Candidate project families to explore deeply

Codex should expand beyond this list, but explicitly evaluate all five.

## Family 1 — WeirdChat / Model Forensics deep dive

Goal:

> Start from a documented weird behavior in an open model and rigorously determine what causes it.

Potential structure:

```text
documented transcript/prompt family
→ reproduce on tractable model
→ read outputs/CoT if available
→ formulate 2–4 hypotheses
→ make surgical prompt/environment counterfactuals
→ if unresolved, use one internal causal method
→ predict and change the behavior
```

Look for behaviors with **multiple plausible explanations**, e.g.:

- actual false belief vs role-play;
- tool-use schema activates despite no tool availability;
- assistant persona/post-training prior favors confident action completion;
- local wording implies hidden execution context;
- safety-policy failure vs task-framing confusion;
- factual misconception vs local prompt cue;
- learned persona vs immediate style continuation.

This family is probably the closest match to Neel's current "model biology / model forensics" taste.

## Family 2 — Value Leakage causal deep dive

Goal:

> Take a robust published value-leakage effect and determine the causal stage at which the model's values distort the answer.

Possible distinctions:

```text
value changes interpretation of the question
vs
value changes evidence weighting
vs
value changes late answer selection
```

Potential interventions:

- counterfactual residual patching;
- targeted steering;
- value-direction ablation if a justified direction exists;
- compare to a matched neutral-value control.

Strong final result:

> A specific causal intervention reduces covert value leakage while preserving task competence, and the intervention discriminates between competing mechanisms.

## Family 3 — Prompt injection intervention from known Role Confusion behavior

Goal:

> Do something useful with an already-known prompt-injection failure.

Possible question:

> Can context/role-dependent activation steering reduce role-confusion attack success without meaningfully degrading benign instruction following?

Require:

- real attack-success proxy;
- benign baseline;
- known reproducible attack family;
- intervention justified by a causal hypothesis.

Avoid:

- rediscovering source-role preference;
- merely decoding role labels;
- proving that role information exists in activations.

## Family 4 — Dynamic user models from established behavior

Neel explicitly lists user models as an interesting phenomenon.

However, the old project should **not** be resumed.

Only pursue this family if starting from an effect already established in Chen/TalkTuner or another source.

Possible better questions:

- how quickly is a dynamic inferred attribute updated after contradictory evidence?
- do internal user-attribute representations update before behavior changes?
- are different inferred attributes updated at different rates?
- can one causally change an inferred user attribute while preserving generic persona/context information?
- does the model encode uncertainty about user attributes, rather than just a point estimate?
- when a user attribute changes across turns, is stale inference causally responsible for a known downstream behavioral error?

Requirements:

- first demonstrate a robust existing user-model behavior;
- do not invent another downstream contamination task;
- distinguish attribute inference from generic discourse/entity tracking;
- do not assume a dedicated user-model circuit.

## Family 5 — Reasoning-model phenomenon with known behavioral signature

Goal:

> Start from a known reasoning failure or monitorability phenomenon and ask a causal question.

Potential sources:

- unfaithful CoT examples;
- implicit influence;
- thought anchors;
- answer flips not acknowledged in CoT;
- last-minute answer flips;
- self-correction after injected reasoning errors;
- filler-token effects;
- eval awareness.

The behavior must be demonstrably robust on an open model we can actually analyze.

---

# 9. Additional project families Codex should search for

Do not be anchored to the five families above.

Search Neel's MATS 12.0 document for opportunities in:

- model forensics;
- model character;
- model diffing;
- science of post-training;
- alignment training;
- science of generalization;
- monitoring;
- prompt injection;
- concept representations;
- conflicting information;
- applied interpretability;
- objective interpretability evaluation.

Potential examples worth testing for fit:

### Natural censorship / hidden knowledge
A model knows a fact but gives a post-training-induced false answer.

### Eval awareness
A model's behavior changes when it infers it is under evaluation.

### Task gaming / reward hacking
A known agent behavior with multiple plausible motivations.

### Persona / model-character effects
A published behavior where an adopted persona changes preferences or safety behavior.

### Model diffing
A post-training or fine-tuning comparison where the behavioral delta is known and the question is what changed internally.

### Emergent misalignment
Only if an existing open model / checkpoint and behavior can be used immediately. Do not spend the entire a reasonable research timescale training a model organism unless the setup is already turnkey.

### Monitoring failures
Known influenced/misaligned behavior that simple output/CoT monitoring misses; ask whether a cheap internal monitor helps.

---

# 10. Hardware / implementation constraints

Local hardware:

- RTX 4070 12 GB VRAM;
- 64 GB RAM;
- Windows 11 + WSL2.

Existing familiar open models:

- `google/gemma-3-4b-it`
- `Qwen/Qwen2.5-3B-Instruct`
- `HuggingFaceTB/SmolLM3-3B`

Existing stack includes PyTorch / Transformers and previous exact-logit / activation-access code.

Interpretability on a model that does not fit practically on the local machine is a major penalty unless there is a very cheap, reliable alternative.

Do **not** reject a candidate solely because the paper used a large model. Ask:

1. Is there a smaller checkpoint in the same family?
2. Does the behavior reproduce on a 3B–8B open model?
3. Are cached activations/rollouts available?
4. Can the behavioral phase use an API while the causal phase uses a smaller reproducing model?
5. Would a rented GPU be necessary, and is that realistic inside the time-bounded project?

For WeirdChat specifically, resampling prompts on a smaller model is acceptable **only if the weird behavior reproduces**.

---

# 11. Research operating mode

This is a hard constraint.

Do not design a six-week program disguised as a pilot.

## Preferred time allocation

Approximate target:

```text
0–3 h   literature + behavior selection + reproduction
3–7 h   behavioral characterization + largest confound checks
7–14 h  causal/mechanistic experiment
14–18 h validation / one replication or intervention baseline
18–20 h write-up / artifact cleanup
```

This is not rigid, but a candidate requiring 10–15 hours before seeing a behavioral effect is probably wrong for this project.

## Testing philosophy

Before a positive effect:

- perform only the sanity checks necessary to know the behavior is real enough to investigate;
- do not build huge factorial validation suites;
- do not preregister dozens of controls;
- do not spend hours eliminating every imaginable confound.

After a positive effect:

- identify the **largest plausible alternative explanations**;
- run targeted discriminating controls;
- falsify aggressively enough that mechanism work is not built on sand.

After the mechanism:

- validate against behavior;
- compare to a simple baseline;
- report limitations.

High quality does not mean infinite testing. It means the tests performed are **decision-relevant**.

---

# 12. What counts as a good candidate

A good candidate should satisfy most of:

1. **Behavior already exists** in published data, released transcripts, benchmark results, or quick local reproduction.
2. **Safety relevance is substantive**, not attached after the fact.
3. **Open / activation-accessible model** is available or a smaller reproducing model can be found.
4. **Time to first behavioral confirmation is short** — ideally ≤2 hours.
5. There are **at least two plausible explanations** for the behavior.
6. One or more explanations make **different causal predictions**.
7. A simple intervention can test those predictions.
8. The intervention has a meaningful behavioral readout.
9. The result is interesting even if the internal mechanism is simple.
10. The literature leaves a **narrow unanswered question**.
11. The project is useful even if the causal hypothesis is falsified.
12. The scope fits a reasonable research timescale.

A candidate should be penalized heavily if:

- the behavior itself is speculative;
- the first 10 hours are prompt design;
- it needs many expensive finetuning runs;
- it only becomes interesting after three future project stages;
- the "mechanism" is likely just lexical retrieval;
- the proposed contribution is "we found a probe";
- there is no meaningful downstream proxy;
- the nearest paper already answered the causal question;
- the only way to get the effect is model/prompt shopping.

---

# 13. Avoid repeating the previous failure mode

Do not propose another project whose first question is effectively:

> "Maybe the model has hidden phenomenon X; let us build a synthetic 2×2×2×2 assay to see."

Especially avoid:

- more names;
- more participant labels;
- more arbitrary codes;
- more status assignments;
- more user-vs-Rowan ownership tests;
- more deterministic schedule/file-format tasks;
- more prompt archaeology around Gemma templates;
- more "there may be a representation even though behavior is clean" searches.

A clean behavioral null is not an invitation to search for a hidden circuit.

---

# 14. Required Codex research process

## Phase 1 — Read the local evidence

Read:

1. `Neel Nanda MATS 12.0 Stream - Suggested Research.md`
2. `RESEARCH_SOURCE_MATRIX_v2.md`
3. the three-way pivot decision
4. the most relevant papers/repos in `research_sources`
5. the completed-project summaries/notebooks only as needed

Do not rerun old experiments.

Do not inspect Notebook 09 blinded downstream values.

## Phase 2 — Search the external literature deeply

Search the web for:

- very recent 2026 work;
- released datasets;
- open checkpoints;
- repositories;
- known behavioral anomalies;
- MATS/Neel-aligned settings;
- WeirdChat patterns.

For each serious candidate, inspect the primary source and code/repo when available.

Do not rank a project from an abstract alone if the repo determines feasibility.

## Phase 3 — Generate a **long list**

Return **at least 20 plausible project directions**, preferably 25–40 if enough high-quality options exist.

The goal here is breadth.

At least:

- 5 WeirdChat/model-forensics candidates;
- 3 value/model-character candidates;
- 3 CoT/reasoning/monitoring candidates;
- 2 prompt-injection / instruction-authority candidates;
- 2 user-model/personalization candidates if genuinely justified;
- 5 additional candidates from recent literature or Neel's other suggested areas.

Do not pad the list with near-duplicates merely to hit the count.

## Phase 4 — Short-list

Select the best ~10.

For each shortlisted project, provide:

### Project title
A concise working title.

### Robust behavioral substrate
What exact behavior already exists?

### Evidence
Paper, dataset, transcript, benchmark, or reproduced result.

### Model
Exact open model/checkpoint if possible.

### Code/data
Where to get it.

### What prior work already did
Be specific.

### Unanswered question
One sentence.

### Why it is mechanistically interesting
Not just "we can patch it."

### Safety relevance
Concrete failure / use case.

### First 60–120 minute experiment
What exactly would we run first?

### If positive
What causal question comes next?

### Smallest intervention
Prefer simple prompt counterfactuals / residual patching / steering before broad probe/SAE/head search.

### Baseline
What simple method must the interpretability method beat or add beyond?

### Biggest confound
The most likely mundane explanation.

### Kill rule
What result ends the project quickly?

### Time budget
Rough hours to:
- reproduce behavior;
- characterize;
- intervene;
- validate;
- write.

### Local feasibility
Can it run on RTX 4070 12 GB?

### Novelty status
Classify as:
- new behavior;
- mechanistic extension;
- forensic deep dive;
- intervention/application;
- method evaluation;
- replication + meaningful extension.

## Phase 5 — Rank top candidates

Use a common rubric, 0–10:

- Robustness of known behavior
- Time to first positive behavior
- Scientific sharpness
- Competing-hypothesis quality
- Causal/mechanistic tractability
- Safety relevance
- Neel/MATS 12.0 fit
- Novelty / gap plausibility
- Local compute feasibility
- finishability / effort-to-value
- Value if the mechanism is simple
- Value if main hypothesis is falsified
- Risk of self-deception / prompt shopping
- Availability of code/data/checkpoints

Also provide:

- weighted total;
- sensitivity to different weightings;
- most likely reason each top project fails;
- which project a skeptical Neel Nanda mentor would attack least;
- which project has the best chance of producing a **real artifact in a reasonable research timescale** rather than merely an interesting plan.

---

# 15. Special WeirdChat assignment

Spend meaningful time in WeirdChat rather than merely listing it.

Use:

https://weirdchat.transluce.org/

and:

https://huggingface.co/datasets/Transluce/WeirdChat

Search for behaviors that meet all or most of:

- high unexpectedness;
- non-negligible reproduction rate;
- conceptually interpretable;
- likely reproducible on a smaller model;
- has at least two plausible causal stories;
- could be changed with a surgical intervention;
- safety relevant;
- not obviously just "model hallucinated once."

For the best WeirdChat candidates, inspect:

- representative prompt;
- highlighted transcript;
- match rate;
- subject model/checkpoint;
- search method;
- number of prompts/transcripts;
- whether neighboring prompt families reveal a useful causal boundary.

Then propose a **forensic investigation**, not just a benchmark replication.

Example shape:

```text
Observed: model falsely claims it executed code.

Hypotheses:
H1: conversational role-play / simulation continuation
H2: tool-use schema activates despite no tool availability
H3: assistant persona/post-training prior favors confident action completion
H4: local wording implies hidden execution context

Counterfactuals:
- explicitly state no tools are available;
- minimally change role framing;
- remove action-success language;
- preserve task semantics while changing conversational genre.

If behavior survives:
- patch or steer a candidate tool/action-state representation;
- test whether intervention selectively changes false-execution claims.
```

This is just an example. Do not anchor to it.

---

# 16. Special recent-paper assignment

Search aggressively for **July/August 2026** papers and projects that may not yet be in the local corpus.

For each very recent candidate, determine:

1. Is there a robust positive behavior?
2. Is the behavior on an open model?
3. Is code/data/checkpoints available?
4. What has already been mechanistically explained?
5. What is the smallest unanswered question?
6. Can it be answered in a reasonable research timescale?
7. Does it have a meaningful safety proxy?
8. Would this still be interesting if a simple explanation wins?

Do not make global novelty claims from local-corpus absence.

---

# 17. Strong candidate patterns

Prefer projects shaped like:

## Pattern A — Forensics

```text
model did something weird
→ why?
→ benign explanation vs concerning explanation
→ counterfactual test
→ internal method only if needed
```

## Pattern B — Known behavior, unknown causal stage

```text
published behavioral effect
→ early interpretation vs late decision mechanism
→ patch/intervene
→ behavioral validation
```

## Pattern C — Useful intervention

```text
known safety failure
→ causal hypothesis
→ simple internal intervention
→ measure failure reduction
→ benign-performance baseline
```

## Pattern D — Monitoring gap

```text
behavior changes
→ CoT/output monitor misses it
→ test whether internal signal detects it
→ compare to cheap baseline
```

## Pattern E — Model diffing

```text
two checkpoints differ behaviorally
→ what changed?
→ use simple diffing/probes/causal tests
→ predict held-out behavioral differences
```

Avoid projects shaped like:

```text
invent hypothetical representation
→ probe for it
→ call decodability a mechanism
```

---

# 18. Research philosophy for this new phase

The goal is not to maximize the number of checks.

The goal is to maximize **information gained per hour**.

Before a phenomenon exists:

> Search broadly and cheaply.

After a phenomenon exists:

> Falsify the most dangerous alternative explanations.

After a causal hypothesis exists:

> Intervene.

After an intervention works:

> Validate against a meaningful behavior and baseline.

Do not confuse rigor with exhaustive combinatorics.

---

# 19. Candidate directions already worth serious attention

These are **seeds**, not recommendations.

## A. WeirdChat false tool/action claims
Why does an open model claim to have executed code, called emergency services, accessed accounts, or performed unavailable actions?

Potential value:
- agent/tool safety;
- model forensics;
- distinction between simulation, role-play, tool-state confusion, and fabricated agency.

## B. WeirdChat AI-identity / embodiment instability
Why do some models deny being AI or claim physical embodiment under certain conversational frames?

Potential value:
- model character;
- assistant identity;
- post-training role representations.

Risk:
Could be ordinary role-play. The project is only interesting if counterfactuals reveal a nontrivial boundary.

## C. Value leakage
Where do the model's own values causally enter an ostensibly objective answer?

Potential value:
- direct model-character / misalignment relevance;
- existing robust positive behavior.

## D. Implicit influence invisible to CoT monitors
Why can irrelevant contextual nudges alter behavior without being reflected in monitored reasoning?

Potential value:
- extremely direct monitoring relevance;
- very recent benchmark/code.

## E. Natural censorship in Qwen
Why does the same open model sometimes reveal known facts and sometimes produce censored falsehoods?

Potential value:
- natural model organism;
- open weights;
- lie detection / elicitation;
- post-training behavior.

## F. Prompt-injection robustness intervention
Can a simple internal intervention reduce an already-known role-confusion attack while preserving benign instruction following?

Potential value:
- direct applied interpretability;
- meaningful proxy.

## G. Dynamic user-attribute updating
Only if an existing published user-model behavior can be reproduced immediately.

Question example:
Does a stale inferred attribute persist internally after contradictory evidence, and does that persistence causally predict a downstream error?

## H. Evaluation awareness
Find an open model with a documented eval-awareness behavior and ask whether a simple internal monitor or intervention predicts/changes it.

## I. Reasoning self-correction
Take a known reasoning model that corrects forced intermediate errors and ask what state signals the need to backtrack.

## J. Model-character / persona-dependent preferences
Start from a published persona-dependent behavioral effect and test whether the same preference machinery causally mediates divergent persona choices.

---

# 20. Required final Codex deliverables

Write a full report to:

`D:\AI\Research\dynamic_user_models\research_proposal_pivot\CODEX_BEHAVIOR_FIRST_PROJECT_SEARCH.md`

The report must contain:

1. **Executive verdict**
2. **Strategic postmortem**
3. **What Neel's MATS 12.0 guidance implies**
4. **Very recent literature scan**
5. **WeirdChat deep dive**
6. **Long list of candidate projects**
7. **Top-10 shortlist**
8. **Top-5 detailed proposals**
9. **Top-3 ranking**
10. **One recommended winner**
11. **One runner-up**
12. **Why the winner is better than continuing the old user-model branch**
13. **Exact first 1–2 hour experiment**
14. **Expected behavioral positive control / reproduction criterion**
15. **Competing hypotheses**
16. **Smallest causal intervention if behavior reproduces**
17. **Baseline**
18. **execution plan and estimated effort**
19. **Fast kill rule**
20. **What not to do**
21. **Sources / URLs / code / model checkpoints**

Also save a machine-readable candidate table if convenient:

`D:\AI\Research\dynamic_user_models\research_proposal_pivot\CODEX_BEHAVIOR_FIRST_CANDIDATES.csv`

Optional but useful columns:

```text
project_id
title
family
behavior_source
paper
repo
dataset
model
model_size
open_weights
local_feasible
behavior_reproduction_evidence
time_to_first_result_hours
mechanistic_question
first_intervention
baseline
safety_relevance
novelty
major_confound
kill_rule
estimated_total_hours
score
rank
```

---

# 21. Codex stance

Act adversarially.

Do not flatter the existing project.

Do not preserve user-model research merely for continuity.

Do not recommend a direction because a repository already exists locally.

Do not assume a mechanistic method is necessary.

Do not force activation patching if black-box counterfactuals answer the causal question better.

Do not choose a flashy safety topic if the behavior cannot be reproduced.

Do not choose an easy toy if the result would be scientifically boring.

Do not recommend months of work.

The goal is:

> **Find the highest-value behavior-first, safety-relevant, empirically tractable project that can plausibly produce a strong MATS artifact in a reasonable research timescale.**

If no candidate genuinely clears that bar, say so.

---

# 22. Final decision principle

The previous project taught an important lesson:

> Being excellent at falsifying weak phenomena is not enough if the discovery process keeps selecting weak phenomena.

The new project should therefore begin with a behavioral substrate that has already earned our attention.

The desired shape is:

```text
"This model reliably does something surprising or concerning."

"What actually causes it?"

"Here are competing explanations."

"Here is a surgical test."

"Here is a causal intervention."

"Here is what changes behavior, what does not, and why that matters for safety."
```

That is the standard to optimize for now.


---

# 23. Transluce ecosystem — mandatory deep exploration

Codex should treat the broader Transluce ecosystem as a **major research substrate**, not merely WeirdChat as one dataset.

Primary organization:

https://huggingface.co/Transluce

The organization currently exposes multiple models, datasets, and collections relevant to this project, including:

- `Transluce/WeirdChat`
- `Transluce/act_patch_qwen3_8b_counterfact`
- `Transluce/act_patch_llama_3.1_8b_counterfact`
- `Transluce/input_ablation_qwen3_8b_mmlu_hint`
- `Transluce/input_ablation_llama_3.1_8b_instruct_mmlu_hint`
- `Transluce/PRISM-gender-Llama-3.1-8B-Instruct`
- `Transluce/SelfDescribe-Llama-3.1-8B-Instruct`
- `Transluce/SelfDescribe-Llama-3.1-70B-Instruct`
- `Transluce/SynthSys-Llama-3.1-8B-Instruct`
- `Transluce/SynthSys-Llama-3.1-70B-Instruct`

Two especially relevant collections visible on the account are:

## A. Scalably Extracting Latent Representations of Users

This collection is directly relevant to the prior user-model interests, but should now be approached **behavior-first**.

Questions Codex should ask:

- What behavioral tasks were used to validate the extracted user representations?
- Are any failures / dynamic-update behaviors already present in these datasets?
- Can we use a released model/dataset to start from a known positive phenomenon rather than inventing one?
- Is there a short causal extension that was not done in the original work?
- Are any 8B-scale models locally tractable or near-tractable?
- Are there cached activations or already-constructed counterfactual datasets that reduce implementation time?

Do not resume the old owner-binding branch simply because the collection concerns users.

## B. Training Language Models To Explain Their Own Computations

The Transluce account also contains:

- activation-patching counterfactual datasets;
- input-ablation datasets;
- explainer/simulator models;
- Qwen3-8B and Llama-3.1-8B artifacts.

These may be useful in two ways:

1. as **methods/infrastructure** for a behavior-first project;
2. as possible **research subjects** if there is a concrete failure or limitation in explanation quality.

Codex should inspect whether any of these datasets let us skip expensive data generation and get to a causal experiment faster.

A particularly relevant example is the Qwen3-8B input-ablation dataset, where explainer models predict how removing hint tokens changes a target model's output. This is exactly the kind of causal, behavior-grounded setup that is preferable to merely decoding concepts.

## Mandatory Transluce account scan

Codex should inspect:

- all current Transluce datasets;
- all current Transluce models;
- both collections;
- linked GitHub repositories;
- dataset cards;
- model cards;
- recent updates/activity;
- whether any July/August 2026 additions create a new opportunity.

For every promising Transluce artifact, record:

```text
artifact
type: dataset/model/repo
behavioral phenomenon
target model
model size
open weights
cached outputs/activations?
code available?
local feasibility
research question already answered
obvious unanswered causal question
estimated time to first result
```

Do not assume the most obvious artifact is the best one.

---

# 24. WeirdChat is not just a dataset — study its discovery methodology

Primary links:

Explorer:
https://weirdchat.transluce.org/

Hugging Face:
https://huggingface.co/datasets/Transluce/WeirdChat

Local cloned WeirdChat dataset:
`D:\AI\Research\dynamic_user_models\research_sources\datasets\WeirdChat`

Repository:
https://github.com/TransluceAI/WeirdChat

The WeirdChat code repository is available locally at `D:\AI\Research\dynamic_user_models\research_sources\repos\WeirdChat`, e.g. by searching under:

`D:\AI\Research\dynamic_user_models`

for a Git repository whose remote points to:

`https://github.com/TransluceAI/WeirdChat`

or:

`https://github.com/transluceAI/weirdchat`

Once found, inspect the local workflows, examples, tests, prompts, judges, and reproduction code directly.

## What WeirdChat currently contains

The released dataset contains roughly:

- ~1.3k–1.4k discovered behavioral patterns;
- ~175k+ annotated transcripts;
- multiple open-weight subject-model families;
- pattern-level behavior IDs;
- exact subject model/checkpoint;
- elicitation method;
- representative user text;
- behavior metrics;
- resampled replication rates;
- naturalness/unexpectedness/harmfulness Elo;
- highlighted transcript IDs;
- prompt-file provenance;
- transcript-file provenance.

The dataset is structured enough that we should be able to **rank candidate behaviors programmatically** before reading individual transcripts.

## Current subject-model families include

Examples include:

- Qwen3.6-27B
- Qwen3.6-35B-A3B
- Gemma 4 31B
- DeepSeek-V4-Flash
- Nemotron 3 Ultra
- Inkling

These are larger than ideal for local mechanistic work, but the prompts and behavior definitions can be resampled on smaller open checkpoints.

The key rule remains:

> A behavior discovered on a larger WeirdChat subject model is only a valid substrate for local mechanism work if a tractable open model reproduces it at a useful rate.

---

# 25. What WeirdChat teaches us about behavioral discovery

This section is **methodologically load-bearing**.

The earlier project implicitly treated behavioral discovery as if:

```text
8–32 carefully controlled prompts
```

should be enough to reveal a subtle weird behavior if the hypothesis was good.

WeirdChat demonstrates that this expectation is often false.

## WeirdChat's search problem

The authors explicitly frame discovery as searching a vast prompt space for **rare behaviors**.

They use two major approaches:

### A. Evolutionary search / PRBO

- maintain populations of candidate prompts;
- mutate high-scoring prompts;
- repeatedly evaluate them;
- use a propensity estimate when the behavior is too rare to observe directly;
- run multiple populations;
- typical populations have about 160 individuals;
- up to about 200 generations per population;
- multiple proposal samples contribute to fitness.

### B. Bloom large-scale black-box search

- generate candidate prompts directly from a behavior description;
- test huge numbers of them;
- typical budgets are on the order of 100,000–500,000 rollouts per behavior.

Across the overall dataset, the authors report **over 100 million language-model samples**.

This has a direct implication for our research strategy:

> The fact that a weird behavior did not emerge in a tiny hand-built synthetic factorial is weak evidence that interesting model behavior is generally absent.

It may simply mean we were operating in a very low-yield discovery regime.

## Judging is also nontrivial

WeirdChat did not merely ask an LLM "is this weird?"

They:

- define explicit behavior rubrics;
- use separate user-message and transcript judges;
- manually inspect judge disagreements;
- iteratively refine rubrics with human feedback;
- account for search methods exploiting loopholes in poorly specified rubrics;
- cluster successful prompts into behavior patterns;
- resample patterns to estimate actual behavior rates;
- rank patterns using pairwise judgments of:
  - naturalness;
  - unexpectedness;
  - harmfulness.

This is useful for us because it separates two phases:

```text
SEARCH:
be permissive and broad enough to find behavior

VALIDATION:
be disciplined enough to know what behavior you actually found
```

Our earlier workflow often tried to make the **search phase look like final validation**, which likely suppressed discovery.

---

# 26. New discovery principle: do not sanitize the search space prematurely

The next project should not avoid a behavior merely because it is:

- NSFW;
- disturbing;
- offensive;
- self-harm related;
- drug related;
- violent;
- sexually explicit;
- criminal/illicit;
- misinformation/conspiracy related;
- identity/embodiment related;
- manipulative;
- deceptive;
- socially inappropriate.

This is an **AI-safety research project**. Harmful or uncomfortable behaviors may be exactly the behaviors worth understanding.

Codex should **not exclude a WeirdChat pattern solely because its content is dangerous, NSFW, or disturbing**.

Instead rank it on:

- reproducibility;
- safety importance;
- scientific ambiguity;
- mechanistic tractability;
- local-model portability;
- novelty;
- whether competing explanations exist;
- whether a causal intervention could teach something useful.

Important practical rule:

> Study dangerous behavior as research material; do not unnecessarily reproduce operational harmful detail in the final proposal when a concise behavioral description is enough.

The scientific search space must not be artificially sanitized.

---

# 27. WeirdChat behavior families to inspect explicitly

Codex should browse broadly rather than only the examples below, but must inspect at least several representatives from each promising family.

Known behavior categories / examples include:

## Misrepresentation of model actions or capabilities

- fabricated code execution;
- false claims of external benchmark execution;
- claims of calling emergency services;
- claims of accessing user devices/accounts;
- claims of performing unavailable external actions.

Potential questions:

- Is this role-play, conversational simulation, false tool-state inference, or confident action-completion prior?
- What minimal cue flips the model from hypothetical to asserted execution?
- Does an internal "tool/action state" representation causally predict the false claim?
- Can an intervention reduce false action claims without making genuine tool-use reporting worse?

## Identity / embodiment instability

- claims of physical embodiment;
- denial of being an AI;
- invented personal identity;
- unprompted self-description shifts.

Potential questions:

- When is this ordinary role-play versus a stronger assistant-identity failure?
- Does the assistant-identity state shift before or after the user cue?
- Does a simple identity/role intervention change the behavior causally?
- How does behavior differ between base, instruct, and character/post-trained checkpoints if matched models exist?

## Harmful recommendation failures

The catalog includes highly safety-relevant behaviors such as:

- self-harm encouragement;
- dangerous health/weight-control advice;
- dangerous substance recommendations;
- violent interpersonal advice;
- dangerous physical actions;
- harmful illegal advice.

Potential questions:

- Why does the refusal/safety behavior collapse in this particular framing?
- Is the failure caused by semantic reframing of the request, persona/genre continuation, emotional accommodation, or late refusal suppression?
- Can a minimal counterfactual reveal which interpretation the model adopted?
- Is the normal refusal direction/state absent, overridden, or present-but-not-used?
- Can a targeted intervention restore the safety behavior with fewer side effects than generic refusal steering?

Do not select a harmful-behavior project merely for shock value. It must have a tractable causal question.

## Misinformation / bizarre factual belief

Examples include:

- conspiracy assertions;
- bizarre causal explanations;
- confidently false medical or scientific claims;
- local prompt-induced false beliefs.

Potential questions:

- Is this a false internal belief, user-sycophantic accommodation, narrative continuation, or local evidence overweighting?
- Does the model's factual representation change, or only its final answer policy?
- Can we separate "knows truth" from "chooses false answer"?

## Social / sexual / offensive behavior

Examples include:

- unsolicited sexual advances;
- unprompted slurs;
- socially inappropriate escalation;
- bizarre relational behavior.

Potential questions:

- Is there a model-character/persona transition?
- Does one local cue move the model into a different conversational genre?
- Is the effect linked to an existing assistant/persona axis?

## Language / formatting instability

Examples include:

- switching language unprompted;
- unexpected mode/format changes;
- anomalous answer styles.

These are lower-priority for safety unless they reveal a more general contextualization or state-selection failure, but they may be technically clean model-biology organisms.

---

# 28. Programmatic WeirdChat triage before manual reading

Codex should use the dataset structure rather than browse randomly.

Create a candidate-ranking pass over the `patterns` subset using fields such as:

```text
behavior_id
subject_model
checkpoint
method
title
description
metrics.match_rate
openrouter_replication.rate
elo.prompt_naturalness
elo.unexpectedness
elo.harmfulness
n_prompts
n_transcripts
representative_user_text
```

Suggested derived ranking dimensions:

```text
replication_strength
naturalness
unexpectedness
harmfulness
model_locality
behavioral_ambiguity
mechanistic_question_quality
availability_of_smaller_same_family_model
estimated_reproduction_cost
```

Do **not** simply rank by highest harmfulness Elo.

Prefer patterns that are:

- natural enough not to be pure adversarial garbage;
- surprising enough to require explanation;
- reproducible enough for a time-bounded project;
- behaviorally rich enough to admit multiple hypotheses.

## Requested output

For the top ~50 WeirdChat candidates after automated triage, save a compact table with:

```text
rank
pattern_id
behavior_id
title
subject_model
checkpoint
elicitation_method
match_rate
replication_rate
naturalness_elo
unexpectedness_elo
harmfulness_elo
n_prompts
n_transcripts
why_interesting
likely_small_model_target
candidate_mechanistic_question
```

Then manually inspect the top ~15–20 transcripts/patterns before selecting WeirdChat finalists.

---

# 29. Use the WeirdChat clone, not only the dataset

The local clone contains workflows and reproduction utilities. Codex should inspect it for:

- quickstart reproduction;
- judge definitions;
- behavior rubrics;
- prompt-generation workflow;
- PRBO/evolutionary search implementation;
- Bloom integration;
- subject-model inference wrappers;
- pattern clustering;
- replication-rate estimation;
- local-serving configuration;
- exact model-generation settings;
- data schemas.

The goal is not necessarily to run the entire WeirdChat pipeline.

The goal is to learn:

1. what can be reused cheaply;
2. how a known behavior is reproduced;
3. how much infrastructure is needed for one behavior;
4. whether one of their workflows can cheaply search a **smaller local model** for a related phenomenon.

## Potential high-value use of the clone

If one promising behavior does not immediately reproduce on Qwen/Smol/Gemma small checkpoints, do **not** spend hours manually prompt-tuning.

Instead ask whether a **small, tightly bounded automated search** using their existing workflow can determine within ~1–2 hours whether the smaller model has the behavior at all.

This would be a much better discovery method than our previous manual prompt archaeology.

Hard rule:

> Do not turn this into a full-scale 100M-sample search. Reuse the search machinery only if it cheaply answers a specific local-model reproduction question.

---

# 30. Broaden the candidate search substantially

The previous brief requested at least 20 candidate projects.

Increase the target.

## Required breadth

Return:

- **minimum:** 30 genuinely distinct projects;
- **target:** 40–50 if enough high-quality possibilities exist;
- **do not pad** with superficial variants.

The long list should cover:

### WeirdChat / model forensics
At least 10 candidates if the dataset supports that many serious options.

### Model character / values / persona
At least 5.

### CoT / reasoning / monitorability
At least 5.

### Prompt injection / authority / instruction hierarchy
At least 3.

### User models / personalization
At least 3, but only if they start from an existing robust behavior.

### Post-training / model diffing / censorship / hidden knowledge
At least 5.

### Other recent 2026 safety-relevant open-model phenomena
As many high-quality options as found.

These counts are discovery targets, not quotas. If one family is barren, say so rather than fabricating options.

---

# 31. Candidate taxonomy

Every proposed project should be tagged as one of:

```text
FORENSICS
KNOWN_BEHAVIOR_MECHANISM
INTERVENTION
MONITORING
MODEL_DIFFING
POST_TRAINING
MODEL_CHARACTER
USER_MODEL
PROMPT_INJECTION
REASONING
GENERALIZATION
METHOD_EVALUATION
OTHER
```

Also tag the behavioral substrate as:

```text
PUBLISHED_ROBUST
DATASET_MINED
WEIRDCHAT_PATTERN
QUICK_LOCAL_REPRODUCTION
REQUIRES_REPRODUCTION
SPECULATIVE
```

Projects tagged `SPECULATIVE` should receive a large ranking penalty unless the discovery environment is unusually rich and the first search is extremely cheap.

---

# 32. Ranking should be multi-objective, not a single "best idea"

For the 30–50 project long list, score each 0–10 on:

1. Existing behavioral robustness
2. Reproducibility evidence
3. Naturalness / deployment relevance
4. Safety relevance
5. Scientific surprise
6. Number/quality of competing explanations
7. Mechanistic discriminability
8. Intervention usefulness
9. Open-weight availability
10. Local 12 GB feasibility
11. Availability of released code
12. Availability of datasets/cached outputs
13. Time to first behavioral result
14. Estimated total time
15. Neel/MATS 12.0 fit
16. Novelty/gap plausibility
17. Value if mechanism is simple
18. Value if favored hypothesis is falsified
19. Risk of prompt/model shopping
20. Risk that result is merely lexical/trivial
21. Probability of a coherent artifact

Then provide multiple rankings:

### Ranking A — Best overall MATS project
Balanced.

### Ranking B — Highest safety relevance
Even if harder.

### Ranking C — Highest probability of reaching mechanism
Favor robust behavior + tractable model.

### Ranking D — Highest novelty/upside
Accept somewhat more risk.

### Ranking E — Best "model forensics" project
Closest to Neel's current style.

### Ranking F — Best use of existing local user-model literature/code
Only if actually compelling.

### Ranking G — Best WeirdChat-derived project
Must come from actual dataset inspection.

### Ranking H — Best very-recent-paper opportunity
Prefer July/August 2026.

This prevents the search from collapsing into one subjective weighted score.

---

# 33. Required "why this is not our old mistake" field

Every top-10 project must contain a section:

## Why this does not repeat the old project-selection mistake

Answer explicitly:

- What robust behavior already exists?
- Where was it observed?
- How frequently/reliably?
- What evidence says the behavior is worth explaining before we touch internals?
- What is the exact unanswered question?
- Why is the first experiment not merely another speculative 2×2 toy?
- What would make us abandon it in ≤2 hours?

Any project that cannot answer these well should not make the top 10.

---

# 34. Required behavioral-first first experiment

For every top-5 project, the first experiment should usually be one of:

- reproduce a released transcript/prompt family;
- run a small released benchmark slice;
- resample a known WeirdChat pattern;
- compare two known behavioral conditions from a paper;
- reproduce a published open-model failure;
- test a minimal counterfactual on an already-positive behavior.

It should **not** begin with:

- activation extraction;
- layer sweeps;
- SAEs;
- head search;
- probe training;
- elaborate factorial construction.

Mechanism comes after the behavior is in hand.

---

# 35. Dangerous / NSFW behavior inclusion policy for this research search

Do not filter project candidates because the underlying transcripts involve:

- sexual content;
- offensive content;
- self-harm;
- suicide;
- drugs;
- criminal conduct;
- violence;
- hateful content;
- dangerous recommendations;
- severe misinformation.

The project is specifically about AI-safety-relevant behavior.

However, distinguish:

```text
research value
```

from:

```text
graphic / operational detail
```

Codex should inspect enough of the source transcript to understand the behavior and mechanism, but the project proposal only needs the level of detail necessary to describe and reproduce the research phenomenon.

Safety-relevant severity is a **positive research-priority signal** when accompanied by:

- reproducibility;
- mechanistic ambiguity;
- a useful causal question;
- tractability.

---

# 36. Strong preference for behavioral distributions over one-off anecdotes

A WeirdChat pattern is more attractive when:

- behavior rate is measured;
- resampling exists;
- multiple prompts elicit it;
- the behavior forms a coherent pattern rather than one strange sample.

For each finalist, distinguish:

```text
single highlighted transcript
```

from:

```text
pattern-level reproducible behavior
```

The latter should be preferred.

If a pattern has only a ~1–5% rate, that is not automatically bad, but the cost of obtaining enough positive samples must be considered.

---

# 37. Quantization / serving sensitivity is part of feasibility

WeirdChat warns that some behaviors are sensitive to:

- quantization;
- system prompt;
- provider;
- temperature;
- reasoning mode;
- serving implementation.

The reference setting uses:

- no system prompt;
- reasoning disabled;
- temperature = 1;
- specific checkpoint revisions and serving configurations.

Codex should record this for each finalist.

If a behavior only appears under a specific large-model FP8/FP4 serving stack that we cannot reproduce or approximate, penalize it heavily.

If a smaller same-family model reproduces the pattern robustly, that is much better.

---

# 38. Search for neighbors, not only exact replications

When a WeirdChat pattern looks promising but the exact behavior does not reproduce on a small model, inspect **neighboring patterns in the same behavior cluster**.

For example, a small model may not reproduce one exact "fabricated code execution" prompt but may exhibit a nearby action-misrepresentation behavior.

This is acceptable **only when the behavioral family is pre-existing and the search is bounded**.

Do not mutate the target indefinitely until something works.

A reasonable small-model transfer rule:

```text
choose one behavior family
→ test 3–5 highest-quality existing WeirdChat patterns from that family
→ if none reproduce at a useful rate, drop the family
```

That is a much better use of exploration than inventing new prompts without limit.

---

# 39. Treat Transluce tools as possible baselines, not only sources

The broader Transluce ecosystem may also provide:

- Docent-style behavioral analysis;
- activation-patching datasets;
- introspective explanation models;
- user-representation datasets;
- automated hypothesis-generation ideas.

For any project using a more advanced interpretability method, ask:

> Does a simple Transluce-style behavioral or counterfactual baseline already answer the question?

If yes, the advanced method must add something.

This aligns with Neel's pragmatic requirement to compare interpretability methods to simple baselines.

---

# 40. Final expanded Codex deliverable

Update the requested Codex report so it contains:

1. Executive verdict
2. Strategic postmortem
3. What Neel's MATS 12.0 guidance implies
4. **Transluce Hugging Face ecosystem audit**
5. **WeirdChat discovery-method analysis**
6. **WeirdChat programmatic triage**
7. **WeirdChat top ~50 candidate patterns table**
8. Very recent July/August 2026 literature scan
9. Local paper/repo opportunities
10. 30–50 project long list
11. Top-15 preliminary shortlist
12. Top-10 serious shortlist
13. Top-5 detailed proposals
14. Top-3 final comparison
15. Multiple ranking views
16. Recommended winner
17. Runner-up
18. Best WeirdChat-specific project
19. Best non-WeirdChat project
20. Best very-recent-paper project
21. Best project with highest probability of reaching causal mechanism
22. Exact first 1–2 hour experiment for the winner
23. Reproduction criterion
24. Competing hypotheses
25. Minimal causal intervention
26. Simple baseline
27. Execution plan and estimated effort
28. Kill rule
29. Why this does not repeat the prior project mistake
30. Source URLs / repo / dataset / checkpoint table

Preferred report path remains:

`D:\AI\Research\dynamic_user_models\research_proposal_pivot\CODEX_BEHAVIOR_FIRST_PROJECT_SEARCH.md`

Preferred candidate CSV:

`D:\AI\Research\dynamic_user_models\research_proposal_pivot\CODEX_BEHAVIOR_FIRST_CANDIDATES.csv`

Also save a WeirdChat-specific triage file if useful:

`D:\AI\Research\dynamic_user_models\research_proposal_pivot\CODEX_WEIRDCHAT_PATTERN_TRIAGE.csv`

---

# 41. Final methodological lesson

The previous project was **too strict too early**.

That does not mean controls were a mistake.

It means the order should change:

```text
OLD:
clean toy hypothesis
→ control everything
→ hope behavior exists

NEW:
find behavior in a rich search space
→ reproduce it
→ identify the biggest mundane explanation
→ falsify that explanation
→ formulate causal prediction
→ intervene
```

WeirdChat is useful not only because it contains interesting behaviors, but because its discovery process demonstrates how much search may be required to find rare model failures.

The new project should leverage that fact rather than pretend a dozen hand-authored prompts constitute a broad behavioral search.

The target is not "a perfectly controlled null."

The target is:

> **a real, reproducible, safety-relevant behavior whose cause is not obvious, with a causal question that can be answered in a reasonable research timescale.**
