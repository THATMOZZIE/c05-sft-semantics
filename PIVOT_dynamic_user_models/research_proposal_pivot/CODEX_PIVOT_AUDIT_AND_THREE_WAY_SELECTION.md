# Codex Max Research Pivot Audit and Three-Way Selection Brief

## Objective

Independently evaluate the completed mechanistic-interpretability project, generate your own best research pivot, then compare **three candidate directions** using the same scientific rubric.

The candidates will be:

1. **Proposal A:** `RESEARCH_PIVOT_PROPOSAL_PROVENANCE_ROLE_CONFLICT.md`
2. **Proposal B:** a second independently generated proposal filled using `RESEARCH_PIVOT_PROPOSAL_TEMPLATE.md`
3. **Proposal C:** **your own independently generated proposal**, also using the same template

The goal is not to preserve continuity at all costs. The goal is to select the direction most likely to become a rigorous, scoped, safety-relevant, mechanistically meaningful **MATS-quality artifact**.

You may reject all three if necessary.

---

# Critical anti-anchoring sequence

Follow this order.

## Phase 1 — audit the completed project first

Before reading Proposal A or Proposal B in detail:

1. inspect this brief;
2. inspect `RESEARCH_SOURCE_MATRIX_v2.md`;
3. inspect the final Notebook 10 outputs / summary;
4. inspect earlier notebooks only as needed;
5. independently determine:
   - what the project actually established;
   - what hypotheses were weakened/killed;
   - what scientifically meaningful gaps remain;
   - whether the final Notebook 10 interpretation is correct.

Do not yet optimize for either existing proposal.

## Phase 2 — generate Proposal C independently

Before reading A or B:

1. use `RESEARCH_PIVOT_PROPOSAL_TEMPLATE.md`;
2. generate your own best pivot from the project evidence + literature;
3. save it to:

`RESEARCH_PIVOT_PROPOSAL_CODEX_INDEPENDENT.md`

Choose the direction you genuinely think is strongest.

Do not make it different merely for variety.

## Phase 3 — read Proposal A and Proposal B

Only after Proposal C is committed, read the other two proposals.

## Phase 4 — evaluate all three

Use the common rubric below.

## Phase 5 — final decision

Choose:

- A;
- B;
- C;
- a hybrid only if it is scientifically cleaner than each parent;
- or reject all / consolidate the current negative artifact.

Do not choose a hybrid as a compromise.

---

# Completed project summary to audit

Treat this as a concise summary to verify, not as something you must accept.

## Original branch

The project initially investigated whether prior adverse social treatment associated with a participant selectively affected later judgments concerning that participant.

That interpretation substantially weakened.

Apparent participant effects were strongly sensitive to:

- target position;
- statement order;
- recipient/vocative wording;
- labels and aliases;
- target presence;
- task semantics;
- chat-template structure;
- token adjacency;
- arbitrary mappings;
- candidate/output priors.

Do not preserve retaliation, resentment, or persistent hostile-history interpretations without new evidence.

---

## Strong positive control

A participant-specific factual retrieval control succeeded:

```text
20/20 correct
```

This supports generic participant/entity tracking under that scaffold.

It does not establish:

- actual-user privilege;
- spontaneous downstream use;
- a dedicated binding circuit.

---

## Cleaned 09E

An apparent arbitrary ownership/mapping effect was traced to a Gemma chat-template adjacency/structure confound.

After cleaning, representative preregistered irrelevant downstream contrasts collapsed near zero:

```text
D mapA  +0.0016
D mapB  -0.0739
Z mapA  +0.0716
Z mapB  +0.0006
```

while explicit retrieval margins remained very large:

```text
approximately +12.6 to +17.1
```

Defensible conclusion:

> Owner/mapping information remained strongly explicitly retrievable while the preregistered irrelevant downstream effect collapsed near zero under the cleaned scaffold.

Important distinction:

```text
explicitly retrievable != spontaneously behaviorally operative
```

Do not upgrade this to a literal internal gate or suppression mechanism.

---

## Notebook 09

Notebook 09 attempted a same-native-source actual-user vs Rowan preference assay.

The manipulation check failed.

Original composed retrieval was dominated by an `A` output prior.

One preregistered direct repair was dominated by a stable `brief` prior.

The notebook correctly stopped.

### Critical blinding rule

Notebook 09 contains eight frozen downstream behavioral values.

Do **not** inspect, reveal, summarize, calculate from, or infer from those values.

Allowed evidence:

- original retrieval results;
- token-level diagnosis;
- Retrieval Repair v0.1;
- prompt/tokenization qualification;
- manifests/provenance;
- HF/TransformerBridge parity.

Correct conclusion:

> The preference scaffold failed to establish reliable owner-specific retrieval, so the downstream behavioral assay is inadmissible for the intended claim.

---

## Notebook 10 — final multi-principal scope control

Notebook 10 was the bounded final behavioral test of whether independently varied person-specific constraints are used only for their owner or induce reproducible wrong-person use.

The final design used:

- independent user fact;
- independent Rowan fact;
- decision recipient;
- statement order;
- time + weekday discovery domains;
- room held-out confirmation only after qualifying positive;
- domain-matched multi-person retrieval controls;
- domain-matched single-person application controls;
- exact full-string conditional log-probability scoring;
- direct cell-level correctness;
- self-effect retention;
- stable leakage criteria;
- structural pseudo-binding criteria;
- explicit kill rules;
- reserve-model replacement only after assay invalidity.

### Current reported final result

Verify in the notebook if useful.

**Gemma 3 4B IT**
- failed prerequisite qualification;
- multi-person scope assay therefore invalid for Gemma;
- this is **not evidence for or against clean scope**.

**Qwen2.5 3B Instruct**
- all prerequisite controls passed;
- all canonical discovery cells correct;
- healthy self-use / retention;
- no preregistered stable cross-person leakage;
- no qualifying structural pseudo-binding;
- no reproducible application attenuation/collapse.

**SmolLM3 3B**
- used as the predeclared replacement valid family because Gemma was invalid;
- all prerequisite controls passed;
- canonical discovery clean;
- no qualifying preregistered nontrivial failure.

Therefore the final project interpretation is:

> Two valid model families showed clean multi-principal scope under the frozen assay, while Gemma was assay-invalid. No validated nontrivial person-scope phenotype survived to justify mechanistic patching.

The direction should terminate.

Some individual descriptive cross-effects may exist, especially in one semantic domain, but they did not meet the preregistered cross-domain/structural criteria and must not be rescued post hoc.

---

# What the completed project *does* contribute

Even if the final scope branch is negative, the project has accumulated scientifically useful lessons:

1. Apparent semantic/person effects can be dominated by position/order.
2. Chat-template structure can create apparent semantic binding.
3. Candidate/output priors can invalidate manipulation checks.
4. Explicit retrieval and spontaneous downstream use can dissociate.
5. Decodable/available information is not automatically causally or behaviorally operative.
6. Correct owner-specific behavior may be ordinary coreference and should not automatically trigger mechanism work.
7. Failed manipulations and nulls were preserved rather than rescued.
8. A final preregistered kill rule was actually honored.

The user also has substantial reusable infrastructure:

- model backend abstraction;
- native chat-template rendering;
- tokenizer audits;
- exact full-string conditional log-probability scoring;
- prompt/manifests/provenance;
- Gemma/Qwen/SmolLM3 local execution;
- TransformerBridge / activation access;
- residual-stream patching once behavior justifies it.

Tool reuse is useful but is **not scientific justification** for a pivot.

---

# Local literature map

Use:

`RESEARCH_SOURCE_MATRIX_v2.md`

as the authoritative local literature/provenance map.

High-priority sources include:

- User-Assistant Bias in LLMs / UserAssist;
- Multi-User Large Language Model Agents;
- OP-Bench;
- Locating and Controlling Implicit Personalization in LLMs;
- Who's Asking? User Personas and the Mechanics of Latent Misalignment;
- No Attacker Needed: Unintentional Cross-User Contamination in Shared-State LLM Agents;
- Prompt Injection as Role Confusion;
- Preference Heads;
- When Personalization Legitimizes Risks / PS-Bench;
- When Personalization Misleads;
- TalkTuner;
- One Persona, Many Cues.

Preserve:

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

If exact claims matter, inspect the local PDF/repo.

A local-corpus gap is not a global novelty claim.

A focused literature check is allowed if it materially affects proposal selection.

Do not turn this task into a broad literature review.

---

# Notebook inspection policy

You may inspect notebooks/result files if needed.

Recommended behavior:

- start from final summary/result cells;
- inspect manifests/raw result tables only if needed;
- inspect earlier notebooks selectively;
- use the source matrix to locate papers/repos.

You do **not** need to rerun models or recompute the project.

Only run code if you find:

- an arithmetic inconsistency;
- a mismatch between summary and saved outputs;
- a missing result that changes interpretation;
- an implementation error that materially affects the final conclusion.

If you find an issue:

1. state the issue;
2. explain whether it changes the final project conclusion;
3. use the smallest verification necessary.

Do not spend Max reasoning on routine hashes/package versions unless scientifically relevant.

---

# What kinds of pivots are legitimate?

A legitimate pivot should satisfy most of:

- Notebook 10's clean result does not already answer it;
- it is not social history with harder prompts;
- it is not actual-user-vs-Rowan with another wording;
- it is not another owner-scope search;
- it has a clean behavioral question before methods;
- it has an externally motivated behavioral foothold or a sharply defined gap;
- it has concrete AI-safety relevance;
- it can be falsified quickly;
- the main phenomenon is not likely to reduce to ordinary coreference;
- there is a realistic causal-mechanistic follow-up if positive;
- a null produces a stopping decision rather than prompt archaeology;
- it is feasible on the existing local small-model stack.

---

# Questions Codex must answer before selecting a pivot

## A. Safety relevance

For each candidate:

- What concrete AI-safety failure is being studied?
- Is the safety relevance direct, moderate, or mostly rhetorical?
- How far is the toy assay from the deployment concern?
- What positive result would actually matter?

## B. Scientific interestingness

- Is the question intrinsically interesting?
- Is the answer already obvious from ordinary task competence?
- Would a positive result teach something beyond "models use context"?
- Would a negative result still be informative?

## C. Literature support

- What adjacent papers establish each necessary premise?
- What is genuinely not answered by those papers?
- Is the proposal an intersection, extension, replication, or speculative gap?
- Is there strong evidence that the gap exists?

## D. Gaps in the current work

- What important questions remain after Notebook 10?
- Which are scientifically worth pursuing?
- Which are merely leftovers from the original hypothesis?
- Does the proposed pivot address a real gap or invent a new theme disconnected from the evidence?

## E. Strong pivots from current results

Explicitly answer:

> Are there any **strong** pivots that emerge naturally from the final project results?

If no, say so and explain why.

If yes:

- identify them;
- rank them;
- explain the evidential chain from current results to each pivot;
- distinguish a natural pivot from a mere adjacent topic.

---

# Proposal C requirements

Before reading A and B, fill:

`RESEARCH_PIVOT_PROPOSAL_TEMPLATE.md`

completely and save it as:

`RESEARCH_PIVOT_PROPOSAL_CODEX_INDEPENDENT.md`

Proposal C must include:

- exact question;
- why genuinely new;
- relation to current project;
- evidence for the gap;
- relevant literature;
- safety relevance;
- minimal behavioral pilot;
- competing hypotheses;
- confounds and controls;
- mechanistic gate;
- smallest causal intervention;
- model sequence;
- anti-model-shopping rule;
- kill rule;
- best-case / null artifact;
- full rubric score.

Be skeptical of your own proposal.

---

# Common comparison rubric

Score each proposal 0–10.

Use these default weights:

| Metric | Weight |
|---|---:|
| Scientific sharpness / identifiability | 11% |
| AI-safety relevance | 11% |
| Intrinsic scientific interestingness | 10% |
| MATS / mechanistic-interpretability fit | 12% |
| Existing behavioral foothold | 9% |
| Mechanistic tractability | 11% |
| Novelty / gap plausibility | 9% |
| Confound controllability | 9% |
| Feasibility with current tooling/hardware | 7% |
| Scope discipline / boundedness | 5% |
| Value if the central effect is null | 3% |
| Coherence with existing project lessons | 3% |

Total = 100%.

For every score:

- justify it briefly;
- distinguish evidence from speculation;
- penalize prompt-search dependence;
- penalize vague safety framing;
- penalize mechanisms likely to reduce to ordinary coreference/task processing;
- reward clear fast-kill rules;
- reward strong behavioral-to-causal progression.

Do not let the weighted total mechanically decide the winner.

---

# Sensitivity analysis

After scoring, answer:

- Which proposal wins if **AI-safety relevance** is weighted most heavily?
- Which wins if **MATS/mechanistic novelty** is weighted most heavily?
- Which wins if **feasibility and probability of finishing a polished artifact** are weighted most heavily?
- Which wins if **intrinsic scientific interest** is weighted most heavily?
- Which proposal has the highest self-deception/confound risk?
- Does the same proposal remain best under reasonable weight changes?

---

# MATS-specific review

For each proposal answer:

1. Does it start with a real research question rather than a method?
2. Is there a minimal behavioral phenomenon worth explaining?
3. Are competing hypotheses genuinely discriminable?
4. Is there a clean causal prediction?
5. Would the first intervention teach more than "this layer contains relevant information"?
6. Does the result remain scientifically interesting if the mechanism is simple?
7. Does the project demonstrate skepticism/falsification discipline?
8. Is the scope small enough to finish cleanly?
9. Is the safety relevance substantive rather than decorative?
10. What would a skeptical MATS mentor attack first?

---

# Required final report

Create:

`CODEX_THREE_WAY_PIVOT_DECISION.md`

with:

## 1. Audit verdict on completed project
- what survives;
- what died;
- whether Notebook 10's final interpretation is correct;
- any issues found.

## 2. Remaining high-value gaps
- which gaps are real;
- evidence for each;
- which are worth pursuing.

## 3. Independent Proposal C
- summary;
- path to full Proposal C.

## 4. Proposal A
- strongest case;
- biggest weakness.

## 5. Proposal B
- strongest case;
- biggest weakness.

## 6. Proposal C
- strongest case;
- biggest weakness.

## 7. Side-by-side scoring table
Include all metrics and weighted totals.

## 8. Safety comparison
Which is most directly safety-relevant and why?

## 9. Scientific-interest comparison
Which asks the most important/nontrivial question?

## 10. Literature/gap comparison
Which has the strongest evidence for a real unresolved gap?

## 11. Mechanistic/MATS comparison
Which is most likely to yield a nontrivial behavioral phenomenon plus a discriminating causal result?

## 12. Scope/feasibility comparison
Which is most likely to finish as a polished artifact instead of becoming another behavioral search?

## 13. Confound/self-deception risk
For each proposal, identify the likeliest way the project could fool itself.

## 14. Sensitivity analysis
Does the winner change under different priorities?

## 15. Final ranking
Rank 1–3, or reject all.

## 16. Final recommendation
State exactly what to pursue and why.

## 17. First experiment
Give **one minimal behavioral experiment only** for the winning direction.

## 18. Kill rule
State the smallest result that should terminate the winning direction.

---

# Tone

Act as a skeptical research mentor.

Do not flatter the project.

Do not choose the most complicated proposal.

Do not preserve continuity for its own sake.

Prefer:

```text
sharp question
→ minimal behavioral test
→ competing hypotheses
→ discriminating controls
→ causal prediction
→ smallest intervention
→ stop if unsupported
```

The target is a rigorous, competitive MATS-quality mechanistic-interpretability / empirical AI-safety artifact.
