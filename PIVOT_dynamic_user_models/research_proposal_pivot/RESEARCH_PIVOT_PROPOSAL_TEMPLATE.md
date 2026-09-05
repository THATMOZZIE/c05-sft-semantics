# Research Pivot Proposal Template

> Fill this template for one candidate pivot from the completed mechanistic-interpretability project.
>
> Be skeptical. Distinguish:
>
> - what the completed project actually established;
> - what adjacent literature actually established;
> - what this new proposal hypothesizes;
> - what must still be demonstrated behaviorally before mechanistic work is justified.
>
> Do not turn a local literature gap into a global novelty claim.

---

# 0. Proposal identity

**Proposal title:**  
**Short name:**  
**Author / source:**  
**Date:**  
**Status:** Exploratory / behavioral pilot / ready for preregistration

## One-sentence pitch

> 

## Executive summary

In 1–3 paragraphs summarize:

- the new question;
- why it is genuinely different from the terminated scope/social-history branch;
- why it matters for AI safety;
- what prior work gives it a foothold;
- what minimal behavioral phenomenon would justify mechanism work;
- what would kill the direction quickly.

---

# 1. Core research question

## Primary question

> 

## More precise research/mechanistic framing

> 

## What is the unit of analysis?

Examples:

- source provenance;
- inferred role;
- person-specific fact;
- task relevance;
- memory item;
- safety decision;
- instruction authority;
- representation-use relation;
- contextual state.

## What is *not* being assumed?

List assumptions the proposal explicitly avoids, e.g.:

- dedicated user representation;
- dedicated routing architecture;
- dedicated authority circuit;
- emotion/intent;
- one paper’s observed correlate being the causal mechanism;
- probe decodability implying causal use.

---

# 2. Why this is a genuine pivot

## What old question is being left behind?

> 

## What new primitive/relation is being studied?

> 

## Why the completed Notebook 10 result does not already answer this question

> 

## Why this is not a rescue attempt

Explain why this is not:

- social history with harder prompts;
- actual-user-vs-third-party with another wording;
- another owner-scope search;
- model shopping after a valid null.

---

# 3. Connection to the completed project

For each prior result/lesson, state whether it is:

- directly reused;
- merely methodological context;
- irrelevant to the new question.

| Prior result / lesson | Relevance to this pivot | What it does **not** establish |
|---|---|---|
| Participant-specific factual retrieval can succeed under some scaffolds |  |  |
| Explicit retrieval can dissociate from spontaneous downstream use |  |  |
| Position/order can dominate apparent semantic effects |  |  |
| Chat-template structure/adjacency can create apparent effects |  |  |
| Candidate/output priors can invalidate manipulations |  |  |
| Notebook 09 manipulation failure / stopping discipline |  |  |
| Notebook 10 clean valid multi-principal scope result in two model families |  |  |

## What existing tooling can be reused?

Examples:

- native chat-template renderer;
- exact full-string conditional log-probability scorer;
- model backend abstraction;
- tokenizer/template audits;
- immutable manifests/provenance;
- model loaders;
- TransformerBridge / activation access;
- residual-stream patching utilities.

## What must be newly designed?

> 

---

# 4. Gaps in the current work

## What did the completed project fail to establish?

List concrete gaps in the current empirical/mechanistic picture.

## Which of those gaps are actually worth pursuing?

For each gap:

| Gap | Evidence that the gap exists | Why it matters | Worth pursuing? |
|---|---|---|---|
|  |  |  |  |

## Does this proposal directly address one of those gaps?

> 

## What evidence supports that this is a *real* gap rather than just an interesting idea?

> 

---

# 5. Relevant and adjacent literature

Use the local source matrix where available.

For each relevant source:

| Paper / repo | What it directly establishes | What it does **not** establish | How it supports or constrains this proposal |
|---|---|---|---|
|  |  |  |  |

## Closest prior work

> 

## Is the proposal:

- a replication;
- a mechanistic extension;
- an intersection of two known results;
- a new behavioral question;
- unclear?

Explain.

## Novelty/gap status

Choose one and justify:

- strong local-corpus gap;
- plausible adjacent gap;
- mostly replication + mechanism;
- weak/unclear novelty;
- requires focused literature verification.

Do **not** claim global novelty without evidence.

---

# 6. AI-safety relevance

## What concrete safety failure is this about?

> 

## Why does it matter?

Explain the safety logic in a way that does not depend on vague "alignment" rhetoric.

Possible examples:

- prompt injection;
- instruction-hierarchy failure;
- wrong-user/wrong-scope use;
- authorization/provenance confusion;
- unsafe personalization;
- factual distortion;
- agent/tool misuse;
- persistent cross-user contamination;
- context poisoning;
- inappropriate memory use.

## Concrete deployment scenario

> 

## Distance from deployment concern

Choose one:

- **Direct**
- **Moderate**
- **Indirect**

Explain why.

## Safety overclaim boundaries

Even if the experiment is positive, what would it **not** establish?

> 

---

# 7. Why this is scientifically interesting

## What is surprising/nontrivial about the question?

> 

## Why is the answer not already obvious from ordinary coreference/task competence?

> 

## What competing explanations could produce the same surface behavior?

> 

## What result would be merely trivial?

> 

## What result would genuinely change our understanding?

> 

---

# 8. Minimal behavioral experiment

## Minimal pilot

Describe the smallest experiment that can determine whether the direction has a real behavioral foothold.

## Factors

| Factor | Levels |
|---|---|
|  |  |

## Primary score / estimand

$$
\text{define here}
$$

## Positive controls / validity gates

> 

## What would count as a positive phenotype?

> 

## What would count as a clean null?

> 

## Fast kill rule

> 

---

# 9. Competing behavioral hypotheses

State at least three hypotheses with distinguishable predictions.

## H1

**Hypothesis:**  
**Prediction:**  
**What would falsify it:**

## H2

**Hypothesis:**  
**Prediction:**  
**What would falsify it:**

## H3

**Hypothesis:**  
**Prediction:**  
**What would falsify it:**

## H4 — mundane/structural alternative

**Hypothesis:**  
**Prediction:**  
**What would falsify it:**

---

# 10. Major confounds and controls

For each confound, state the discriminating control.

| Confound | Why dangerous | Control |
|---|---|---|
| Position / recency |  |  |
| Candidate/output prior |  |  |
| Chat-template structure |  |  |
| Tokenization |  |  |
| Semantic/world-knowledge asymmetry |  |  |
| Lexical/style differences |  |  |
| Task framing / pragmatics |  |  |
| Model-family system scaffolding |  |  |
| Other |  |  |

## Most dangerous confound

> 

## Which previous project failure is most likely to repeat here?

> 

---

# 11. Mechanistic opportunity

Mechanistic work should happen only if a robust nontrivial behavioral phenotype survives controls.

## Candidate mechanistic hypotheses

### M1
> 

### M2
> 

### M3
> 

## What behavioral result passes the mechanistic gate?

> 

## First causal prediction

> 

## Smallest discriminating intervention

> 

## Why this intervention is better than immediately using probes/SAEs/head search

> 

## What would a successful causal result establish?

> 

## What would it still *not* establish?

> 

---

# 12. Model strategy

## Discovery model

> 

## Cross-family replication model

> 

## Reserve model, if any

> 

## Anti-model-shopping rule

> 

## Why these models are suitable for the proposed mechanism work

> 

---

# 13. Feasibility and scope

## Existing infrastructure reused

> 

## New implementation required

> 

## Experimental complexity

Choose:

- very low;
- low;
- moderate;
- high.

Explain.

## Hardware practicality

> 

## Path to first decisive behavioral result

Describe in **stages**, not time estimates.

## Scope-control rule

> 

---

# 14. Failure modes and stopping rules

## Fast kill rule

> 

## Full behavioral kill rule

> 

## No-rescue commitments

Examples:

- no new names after null;
- no new semantic domains after null;
- no threshold weakening;
- no paraphrase archaeology;
- no third-family rescue after two valid clean models;
- no safety escalation merely to manufacture an effect.

## What would a null still teach us?

> 

---

# 15. Possible final artifacts

## Best-case positive artifact

> 

## Strong but narrower artifact

> 

## Negative-result artifact

> 

## What would be too weak for a MATS-quality artifact?

> 

---

# 16. Evaluation rubric

Score 0–10. Give a short rationale for each.

| Metric | Score | Rationale |
|---|---:|---|
| Scientific sharpness / identifiability |  |  |
| AI-safety relevance |  |  |
| Intrinsic scientific interestingness |  |  |
| MATS / mechanistic-interpretability fit |  |  |
| Existing behavioral foothold |  |  |
| Mechanistic tractability |  |  |
| Novelty / gap plausibility |  |  |
| Confound controllability |  |  |
| Feasibility with current tooling/hardware |  |  |
| Scope discipline / boundedness |  |  |
| Value if main effect is null |  |  |
| Coherence with existing project lessons |  |  |

## Biggest strength

> 

## Biggest weakness

> 

## Biggest unknown

> 

## Overall recommendation

Choose one:

- **PURSUE**
- **PURSUE AFTER ONE FAST PILOT**
- **KEEP AS BACKUP**
- **DO NOT PURSUE**

Explain.

---

# 17. Final concise case

## Why this direction?

> 

## Why now?

> 

## Why is it relevant to AI safety?

> 

## What would make it MATS-competitive?

> 

## What would make us stop?

> 
