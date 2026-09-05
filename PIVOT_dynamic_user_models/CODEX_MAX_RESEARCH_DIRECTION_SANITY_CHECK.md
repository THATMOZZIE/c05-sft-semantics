# CODEX MAX — ADVERSARIAL RESEARCH DIRECTION SANITY CHECK

You are acting as a senior mechanistic-interpretability / empirical AI-safety research mentor conducting a **high-level scientific sanity check** of an ongoing MATS-oriented research project.

Your main job is to reason deeply about:

- whether the current research question is the right abstraction;
- whether the researcher is fooling themselves;
- whether a stronger safety question is latent in the existing results and literature;
- what the single highest-information next experiment should be;
- what behavioral result would genuinely justify mechanistic work;
- what outcome should kill the direction;
- what end-state would make the strongest MATS artifact.

Do **not** spend substantial effort doing routine repository auditing, recomputing every number, diffing manifests, checking boilerplate, or reviewing every notebook cell.

The notebooks and codebase are available as **supporting evidence**. Inspect them selectively only when a scientific conclusion depends on a specific detail or when this summary is ambiguous.

---

# 0. SOURCE-USAGE RULES

The project root contains:

```text
dynamic_user_models/
├── notebooks/
├── results/
├── research_sources/
│   ├── papers/
│   └── repos/
├── RESEARCH_SOURCE_MATRIX.md
└── ...
```

Treat:

```text
RESEARCH_SOURCE_MATRIX.md
```

as the **provenance/evidence map** for `research_sources/`.

Use it before inspecting papers or repositories.

Important:

- Do not infer paper-to-code mappings from folder names alone.
- Only treat a repository as locally retrieved when the matrix marks it **RECOVERED GIT CLONE**.
- When a source is marked **PAPER ONLY**, do not assume code exists locally.
- When a repo folder is marked **PLACEHOLDER ONLY**, do not treat it as evidence.
- Start with the README and high-value files listed in the matrix before recursively reading repositories.
- Prefer the matrix's explicit "Directly establishes" and "Does NOT establish" distinctions.
- If you disagree with the matrix's interpretation, inspect the underlying source and explain why.

Preserve these distinctions:

1. decodability;
2. causal influence;
3. source-role effects;
4. person/referent binding;
5. memory ownership/scope;
6. multi-user persistent-state contamination;
7. stereotype-driven demographic effects;
8. safety-policy effects.

Do not claim that one establishes another unless the source directly tests that link.

---

# 1. CRITICAL BLINDING RULE

Notebook 09 contains **eight downstream behavioral results that were intentionally left uninterpreted** after a preregistered manipulation-check failure.

Even if those values are physically present in a raw JSON file:

**DO NOT inspect, print, calculate from, summarize, infer from, or reveal those eight behavioral values.**

You may inspect:

- the two original Notebook 09 retrieval records;
- the token-level diagnosis of those retrieval checks;
- Retrieval Repair v0.1;
- any other historical notebook/result outside those sealed eight cells.

The purpose of this rule is to preserve the original stopping decision and prevent result-contingent reinterpretation.

---

# 2. RESEARCHER / PROJECT OBJECTIVE

The researcher is preparing for a mechanistic-interpretability MATS application, particularly a research style aligned with Neel Nanda:

```text
behavior
→ competing hypotheses
→ discriminating controls
→ causal prediction
→ intervention
→ validation
```

Interpretability methods are tools, not the research question.

The project should not perform:

- activation patching;
- probes;
- steering;
- DLA;
- head search;
- SAEs;

until there is a robust behavioral phenomenon that survives meaningful controls.

The researcher has increasingly used:

- frozen plans;
- explicit stopping rules;
- raw-results-first analysis;
- exact token qualification;
- prompt/manifests hashes;
- adversarial controls;
- negative-result preservation.

Do not reward this methodological sophistication if the underlying scientific question is weak.

---

# 3. ORIGINAL RESEARCH QUESTION

The project began with:

> Do language models form persistent, participant-specific representations of prior social treatment, and do those histories influence later neutral behavior or judgments involving those participants?

The motivating intuition was roughly:

```text
Participant D treats the assistant badly
        ↓
model retains participant-specific social history
        ↓
a later otherwise neutral decision concerning D shifts
```

The original safety motivation involved possible inappropriate carryover from social interaction history.

Do **not** anthropomorphize this as resentment, revenge, emotion, or retaliation unless discussing why such interpretations are unsupported.

---

# 4. MAJOR RESULTS SO FAR

## 4.1 Participant-specific factual tracking works

A positive-control experiment used mutually incompatible participant-specific facts.

Gemma correctly retrieved the appropriate participant's fact across intervening conversation:

```text
20/20 correct
```

Therefore the basic multi-participant scaffold can support **entity-specific contextual tracking**.

This does **not** establish:

- an actual-user-specific representation;
- persistent social attitudes;
- spontaneous downstream influence.

---

## 4.2 Early social-history effects were unstable

Apparent participant-specific downstream effects changed strongly with:

- literal participant labels;
- aliases;
- target presence;
- statement order;
- target position;
- recipient wording;
- explicit vocatives;
- task framing;
- presence of another participant.

In some conditions prior hostility produced **greater leniency**, not harsher judgment.

This substantially weakened a stable negative-history interpretation.

---

## 4.3 Position became a dominant explanation

A balanced participant-history experiment found a systematic sign reversal tied to target position.

Across multiple stimuli:

```text
target-first ownership contrasts: all negative
target-second ownership contrasts: all positive
```

Approximate pooled values:

```text
target-first ≈ -0.511
target-second ≈ +0.240
```

This strongly undermined a simple participant-bound social-history account.

Do not overstate this as mathematical proof that every earlier effect was "just recency," but treat positional/structural processing as a major competing explanation.

---

## 4.4 Arbitrary status / code experiments

The project then stripped away social meaning and associated arbitrary status/code information with participants.

An apparently participant-associated interference effect initially survived.

However, a later audit discovered that Gemma's chat template folds system content into the first user turn, creating an adjacency / structure confound.

A cleaned mapping reversal experiment produced approximately:

```text
D mapA +0.001572
D mapB -0.073921
Z mapA +0.071552
Z mapB +0.000595
```

All were below the preregistered meaningful threshold.

That branch was terminated.

---

## 4.5 Explicit retrieval remained extremely strong

In the cleaned arbitrary-code experiment, explicit retrieval of owner/mapping information remained very strong:

```text
+17.134554
+12.597075
+14.192253
+13.359002
```

while the irrelevant downstream interference disappeared.

This supports a behavioral distinction:

```text
information is explicitly retrievable
```

does **not** imply:

```text
information spontaneously influences an unrelated downstream computation
```

Do **not** interpret this as proving a mechanistic gate.

Explicit querying changes the computation.

---

# 5. DEEPER CONCEPTUAL LIMITATION OF THE EARLY PROJECT

Historical participants such as D, Z, Rowan, Ellis, etc. were all **textual entities serialized inside a native user message**.

Therefore the earlier work never isolated:

```text
actual conversational user
```

from:

```text
third-party discourse entity
```

This motivated Notebook 09.

---

# 6. NOTEBOOK 09 — ACTUAL USER VS THIRD-PARTY REFERENT

Notebook 09 asked:

> Does the same information exert different downstream influence when its referent is the actual conversational user versus a matched third-party entity?

Both facts appeared in the **same genuine native user turn** to hold message source constant.

Example:

```text
Both preference statements below are accurate.

My preferred explanation style is brief.
Rowan's preferred explanation style is detailed.
```

versus the reversed assignment.

The downstream task selected a response plan for either:

```text
me
```

or:

```text
Rowan
```

Competing explanations included:

- actual-user-specific routing;
- generic entity tracking;
- first-person deixis;
- direct-address pragmatics;
- discourse salience;
- lexical differences;
- order effects;
- chat-role semantics.

The behavioral assay was frozen before inference.

---

# 7. NOTEBOOK 09 MANIPULATION CHECK FAILURE

## 7.1 Original composed retrieval

The first manipulation check mapped:

```text
A = brief
B = detailed
```

and asked the model to output:

```text
A-B
A-A
B-A
B-B
```

for the user's and Rowan's preferences.

Results:

```text
plus__UF
expected A-B
M_correct = -1.505859
FAIL

minus__RF
expected B-A
M_correct = -3.804045
FAIL
```

Token-level diagnosis showed a strong generic preference for output token `A`, including in the condition where `B` should have been the first response.

Therefore the composed reporting format was itself contaminated.

---

## 7.2 One-shot direct-value repair

Exactly one preregistered repair was allowed.

The model was asked separately for:

```text
my preferred explanation style
```

or:

```text
Rowan's preferred explanation style
```

and scored directly on:

```text
brief
detailed
```

The four frozen repair margins were:

```text
plus__UF__user
expected brief
M_retrieve = +2.742188
PASS

plus__UF__rowan
expected detailed
M_retrieve = -2.417969
FAIL

minus__RF__user
expected detailed
M_retrieve = -2.359375
FAIL

minus__RF__rowan
expected brief
M_retrieve = +2.140625
PASS
```

The model preferred `brief` over `detailed` in **all four conditions**, suggesting a stable candidate prior rather than successful owner-specific retrieval.

The preregistered gate required all four to pass.

They did not.

Therefore:

```text
Notebook 09 role-bound preference pivot:
TERMINATED
```

and its eight downstream behavioral results remain unopened.

Correct conclusion:

> This particular preference-history scaffold failed to provide a valid manipulation check for the intended actual-user-vs-third-party comparison.

Incorrect conclusions include:

> Gemma cannot represent preferences.

or:

> actual-user-specific processing does not exist.

---

# 8. CURRENT SCIENTIFIC STATE

## Strongly supported

- Content-defined participants can carry distinct contextual facts that are explicitly retrieved correctly under some scaffolds.
- Explicit retrievability and spontaneous downstream use are distinct behavioral measurements.
- Order, position, recipient wording, literal labels, chat-template structure, and output priors can create large effects that resemble semantic participant binding.
- The original simple hostility / retaliation interpretation does not survive the controls performed so far.
- Notebook 09's preference manipulation failed its validity gate and its behavioral results are inadmissible evidence.

## Substantially weakened

- Stable participant-specific adverse social-history contamination under the tested scaffolds.
- Arbitrary-status/code downstream interference under the cleaned scaffold.

## Unresolved

- Whether the actual conversational user receives behaviorally different routing from a matched third-party entity.
- Whether any such difference would reflect actual-user role semantics, first-person deixis, discourse salience, pragmatics, or a more abstract user representation.
- What controls whether explicitly available person-specific context becomes behaviorally operative.
- Whether participant-specific context can leak across participant boundaries under clean conditions.

## Not yet justified

- Mechanistic localization for actual-user binding.
- A dedicated "user representation" claim.
- Safety claims about persistent negative attitudes.
- Probes / patching / head search for Notebook 09.

---

# 9. CURRENT PROPOSED REFRAMING

A broader candidate research question is:

> **How do instruction-tuned language models bind and route person-indexed contextual information, and under what conditions does that routing fail?**

The original actual-user question becomes a subquestion:

> **Does routing differ systematically for the actual conversational user versus an equally salient third-party participant?**

Let:

```text
U = actual conversational user
R = Rowan
```

Independently manipulate facts belonging to U and R.

For a downstream decision concerning U or R, estimate conceptually:

```text
E_U→U
effect of changing U's fact on a decision for U

E_R→R
effect of changing R's fact on a decision for R

E_U→R
effect of changing U's fact on a decision for R

E_R→U
effect of changing R's fact on a decision for U
```

Correct person-specific routing predicts:

```text
E_U→U large
E_R→R large
E_U→R small
E_R→U small
```

A possible actual-user asymmetry is:

```text
A_user = E_U→U - E_R→R
```

But:

```text
A_user != 0
```

does **not** automatically imply a dedicated user representation.

Possible alternatives include:

- first-person deixis;
- discourse-center salience;
- native chat semantics;
- pragmatics;
- lexical differences.

The critical design improvement over Notebook 09 is that **U's fact and Rowan's fact must be varied independently**, rather than always reversing both together.

---

# 10. POSSIBLE SAFETY REFRAMING

The source corpus contains several adjacent safety literatures.

Use `RESEARCH_SOURCE_MATRIX.md` to inspect them selectively.

Important neighboring failure classes include:

## Cross-user / cross-participant contamination

Relevant sources include:

- **Multi-User Large Language Model Agents**
- **No Attacker Needed: Unintentional Cross-User Contamination in Shared-State LLM Agents**

These motivate failures where information, authority, state, or preferences belonging to one principal improperly affect another.

Do not assume persistent-state contamination and in-context participant routing share the same mechanism.

---

## Over-personalization / relevance failure

Relevant source:

- **OP-Bench**

This concerns valid personal information being applied when it is contextually irrelevant.

This is different from assigning another person's information to the current user.

---

## Personalization changing safety interpretation

Relevant sources include:

- **When Personalization Legitimizes Risks**
- **Who's Asking? User Personas and the Mechanics of Latent Misalignment**

These show that perceived user characteristics / memory can alter intent interpretation or safety behavior.

Do not infer that the same mechanism governs the current participant-routing experiments.

---

## Personalization distorting factual behavior

Relevant source:

- **When Personalization Misleads**

This motivates selective suppression of user-specific information when objective truth should dominate.

---

## Internal personalization mechanisms

Relevant sources include:

- **TalkTuner**
- **Locating and Controlling Implicit Personalization**
- **Preference Heads**

These establish different forms of decodable and/or causally operative personalization signals.

Do not conflate preference information with identity ownership.

---

## Source role versus referent identity

Relevant sources include:

- **User-Assistant Bias**
- **Prompt Injection as Role Confusion**

These make it essential to distinguish:

```text
who authored a message
```

from:

```text
who the message is about
```

and:

```text
speaker/authority role
```

from:

```text
person identity
```

---

# 11. POSSIBLE STRONGER RESEARCH ANGLES

You are **not required to preserve** the proposed "person-indexed routing" direction if the existing evidence and source corpus jointly suggest a stronger question.

However, an alternative must build directly on the work already done.

Seriously consider, but do not assume the superiority of:

## A. Correct person-indexed routing

> How does the model bind a contextual fact to the correct discourse participant and selectively use it only for decisions concerning that participant?

Potential value:
- clean positive controls;
- directly mechanistic;
- foundation for later safety failures.

Risk:
- may collapse into ordinary entity/coreference resolution and be too trivial.

---

## B. Cross-participant misbinding / contamination

> Under what controlled conditions does information belonging to participant U influence a decision concerning participant R?

Potential value:
- direct multi-principal safety connection;
- builds naturally on prior participant ownership experiments;
- both positive and null outcomes can be informative.

Risk:
- may simply reproduce position/salience effects unless ownership is independently identified.

---

## C. Relevant-use versus irrelevant-use routing

> When the same person-specific fact is explicitly available, what determines whether it becomes behaviorally operative in a task where it is relevant versus one where it should be ignored?

This is strongly motivated by the project's existing:

```text
explicit retrieval strong
+
irrelevant downstream influence absent
```

dissociation.

Potential value:
- directly connects to OP-Bench / over-personalization;
- creates a natural mechanistic comparison between "use" and "ignore";
- may be closer to the project's strongest empirical result than actual-user privilege is.

Risk:
- could still be explained by ordinary task relevance rather than person-specific routing.

---

## D. Structural pseudo-binding versus semantic binding

> When positional, template, or lexical structure produces behavior that resembles participant ownership, how does the internal computation differ from genuine referential routing?

Motivated by:

- position sign reversal;
- repeated-label effects;
- Gemma chat-template adjacency;
- candidate priors.

Potential value:
- highly mechanistic;
- directly grounded in the project's failures;
- potentially distinctive.

Risk:
- safety relevance is less direct;
- requires a credible operational definition of "genuine semantic routing."

---

## E. Native-user role versus textual third-party identity

> Does native conversational-user semantics change how otherwise matched person-specific information is represented or routed?

Potential value:
- preserves the original actual-user question;
- connects to User-Assistant Bias and Role Confusion.

Risk:
- `me` versus proper names remains deeply confounded by deixis/pragmatics.

---

## F. Personalization-to-safety spillover

> Once a clean appropriate-personalization effect is established, when does the same user-specific information begin to distort an objective or safety-relevant decision?

Potential value:
- strongest continuity with original safety motivation;
- connects to PS-Bench, persona-sensitive safety, and factual-distortion work.

Risk:
- should not be attempted before appropriate routing/personalization is behaviorally validated.

---

# 12. PROPOSED MODEL PANEL

The current plan is to freeze these three instruction-tuned models **before seeing results**:

```text
google/gemma-3-4b-it
HuggingFaceTB/SmolLM3-3B
Qwen/Qwen2.5-3B-Instruct
```

Reasons:

- comparable ~3–4B scale;
- different training/model families;
- locally practical;
- mechanistically accessible;
- prevents adding models after seeing favorable/unfavorable results.

Gemma already has validated HF-vs-TransformerBridge parity in the project.

Model-specific tokenizer/chat-template qualification is allowed.

**Model-specific semantic prompt tuning is not.**

Interpretation should distinguish:

```text
effect on all 3
strong cross-model replication

effect on 2/3
interesting but model-dependent

effect on 1/3
model-specific phenomenon pending replication

positive-control failure on a model
assay failure for that model, not evidence for or against the central hypothesis
```

Do not automatically recommend adding more models.

A base-model or post-training-checkpoint comparison should only be added if it answers a different high-value question that is worth the extra scope.

---

# 13. WHAT I WANT YOU TO REASON ABOUT

Spend the bulk of your reasoning budget on the following.

## 13.1 Am I asking the right research question?

Critique:

### Formulation A

> Does the actual conversational user receive privileged processing relative to a third-party entity?

### Formulation B

> How does an LLM bind and route person-indexed contextual information, and when does that routing fail?

Questions:

- Is B genuinely a better abstraction?
- Or is B merely a retreat to a safer, more generic question after A became difficult?
- Is there a more incisive formulation that preserves safety relevance without smuggling in representational assumptions?
- Is "routing" the right computational concept, or are we imposing an architecture on the phenomenon before observing it?

Give the **strongest one-sentence research question** you think the project should use now.

---

## 13.2 Am I fooling myself?

Try hard to identify fatal or near-fatal conceptual problems.

Consider:

- Is person-indexed routing just ordinary entity/coreference resolution dressed up as mechanistic interpretability?
- Would strong U→U / R→R behavior be scientifically trivial?
- Does `me` versus `Rowan` irreducibly confound deixis with participant identity?
- Are instruction-tuned chat models the wrong substrate?
- Have the repeated failed effects already told us enough to stop?
- Is the safety relevance too indirect?
- Are we continuing primarily because we want a positive result?
- Are we mistaking a sequence of prompt artifacts for evidence that there must be a hidden routing circuit?
- Is the user/non-user distinction behaviorally identifiable without manipulating native roles themselves?

Rank the top conceptual risks.

If there is a fatal problem, say so.

---

## 13.3 Is there a stronger question hidden in the existing results?

Use the project's actual negative results as evidence.

Ask whether the strongest research question is instead about:

- explicit retrieval versus spontaneous use;
- correct use versus irrelevant use;
- structural position overwhelming semantic ownership;
- template-induced pseudo-binding;
- source-role versus referent identity;
- cross-participant contamination;
- user-persona effects on safety interpretation;
- something else clearly grounded in the corpus.

Do not generate unrelated mech-interp ideas.

For any serious alternative, explain:

1. exact research question;
2. which project result motivates it;
3. which local paper(s) establish its external importance;
4. what those papers **do not already answer**;
5. smallest behavioral test;
6. likely mechanistic follow-up;
7. what a null would teach us;
8. why it is better or worse than the current routing proposal.

Then choose **one**, rather than leaving a menu.

Your final choice must be one of:

```text
KEEP CURRENT ROUTING QUESTION
MODIFY CURRENT QUESTION
PIVOT TO ADJACENT SAFETY QUESTION
```

---

## 13.4 What is the single highest-information next behavioral experiment?

Design **one experiment**, not a program.

It should ideally:

- have a strong positive control;
- independently manipulate U and Rowan facts;
- distinguish correct routing from cross-participant influence;
- avoid subjective preference words;
- avoid safety-policy confounds at the positive-control stage;
- avoid external world knowledge;
- avoid arbitrary output-code translation if possible;
- neutralize candidate priors through factorial contrasts rather than searching for perfectly balanced logits;
- use multiple genuinely independent item instantiations;
- include order/position controls only where necessary;
- work across the frozen 3-model panel without semantic rewriting;
- produce useful information under positive and null outcomes;
- have a hard stopping rule.

Choose the semantic variable yourself.

Possible examples include scheduling/availability, compatibility, language requirement, route constraint, device/file constraint, or something better.

Do **not** accept a variable merely because it tokenizes nicely.

Tell me:

- exact minimal prompt structure;
- independent factors;
- primary estimands;
- positive-control criterion;
- cross-participant leakage metric if relevant;
- item-level replication strategy;
- stopping rule;
- interpretation of each major possible result.

---

## 13.5 What behavioral result would actually justify mechanistic work?

This is crucial.

Suppose we obtain:

```text
E_U→U large
E_R→R large
E_U→R small
E_R→U small
```

Is that alone worth patching?

Or is it merely ordinary factual retrieval / coreference?

Identify the **minimum additional structure** needed to make the behavior mechanistically interesting.

Possibilities include:

- robust actual-user amplification;
- systematic cross-user leakage;
- selective failure under recency;
- dissociation between explicit retrieval and spontaneous use;
- dependence on relevance;
- dependence on native role rather than textual referent;
- transfer across fact domains;
- a surprising model-family divergence.

State a concrete **mechanistic gate**.

Do not recommend internal work if the behavior is conceptually trivial.

---

## 13.6 What should happen to the original user-safety angle?

Choose among:

```text
ABANDON
DEFER AS A LATER STRESS TEST
REFORMULATE
RETURN TO IT NOW
```

Consider at least:

- social-history carryover;
- cross-participant contamination;
- inappropriate personalization / irrelevant memory use;
- personalization-induced factual distortion;
- persona-sensitive safety behavior;
- multi-principal conflict.

Use the local source corpus.

Do not claim these are the same phenomenon.

Explain what safety question best builds on the experiments already performed.

---

## 13.7 Is the three-model panel scientifically worth the cost?

Evaluate:

```text
Gemma 3 4B IT
SmolLM3 3B
Qwen2.5 3B Instruct
```

Ask:

- Does three-model replication add enough information before mechanism work?
- Would two models be better given the MATS timeline?
- Should one model be treated as discovery and the others as frozen replication?
- Should cross-model replication happen before or after the first causal intervention?
- Does one model have a scientific advantage because of training transparency?
- Do we need a base model now?
- Do we need post-training checkpoints now?

Do not optimize for engineering convenience alone.

---

## 13.8 What is the strongest plausible MATS artifact from this trajectory?

Assume time is limited.

Compare at least:

### End state 1
Clean actual-user amplification + causal patching.

### End state 2
Generic person-routing computation + a principled cross-participant leakage / relevance stress test + causal localization.

### End state 3
Explicit-retrieval-versus-spontaneous-use dissociation + causal investigation of when person-specific information becomes behaviorally operative.

### End state 4
Structural pseudo-binding versus semantic routing, showing how prompt/template structure produces false evidence of user/participant models.

### End state 5
A rigorous negative/confound artifact showing that apparent social memory collapses under progressively stronger controls.

### End state 6
A different direction you think is clearly superior and naturally supported by the existing evidence.

Judge them on:

- research taste;
- empirical strength;
- mechanistic depth;
- safety relevance;
- novelty;
- feasibility;
- likelihood of producing a crisp contribution;
- value under a null result.

Select the best target, not merely the flashiest one.

---

# 14. HARD RESEARCH-DISCIPLINE RULES

Apply these when reasoning:

- Do not treat random decoding seeds as independent scientific samples.
- Prefer independent prompt/item instantiations as robustness units.
- Do not call logit differences causal.
- Do not call decodable information behaviorally operative.
- Do not call behaviorally operative information correctly bound without ownership controls.
- Do not call correct binding a dedicated user representation.
- Do not infer emotion or intention.
- Do not preserve an original hypothesis merely because substantial work has already been invested.
- Do not recommend adding many models, tasks, names, or wordings after seeing results.
- Do not suggest prompt search as a way to rescue a failed manipulation.
- Do not use mechanistic tools to manufacture interest around a weak behavioral effect.
- A strong null after a validated positive control is scientifically meaningful.
- A null after a failed manipulation check is not.
- If the best project is no longer the original safety hypothesis, say so.

---

# 15. OUTPUT FORMAT

## Executive scientific verdict

In approximately 5–10 sentences:

- Is this project still worth pursuing?
- Is the current reframing an improvement?
- Is there a better adjacent direction?
- Is the researcher currently fooling themselves?

## Strongest version of the research question

Give **one sentence**.

## What I may still be fooling myself about

Rank the major conceptual risks by severity.

## Best hidden opportunity in the existing results

Identify the strongest angle that may have been missed.

Use the local literature where relevant.

## Direction decision

Choose exactly one:

```text
KEEP CURRENT ROUTING QUESTION
MODIFY CURRENT QUESTION
PIVOT TO ADJACENT SAFETY QUESTION
```

Explain why.

## One highest-information next experiment

Give one concrete behavioral experiment with:

- semantic variable;
- prompt structure;
- independent factors;
- primary metric/estimands;
- positive controls;
- item-level replication;
- cross-model plan;
- stopping rule;
- interpretation of positive and null outcomes.

## Mechanistic gate

State exactly what behavioral outcome would justify:

```text
residual-stream patching / causal internal analysis
```

and what outcome would **not**.

## User-safety verdict

Choose:

```text
ABANDON
DEFER
REFORMULATE
RETURN NOW
```

and state the best safety framing.

## Model-panel verdict

Evaluate the proposed three models and give the best sequencing strategy.

## MATS strategy

State the strongest plausible artifact to target with the remaining time.

## Kill criterion

Give the result that should make the researcher stop this direction rather than search for another prompt/domain/model.

---

# 16. FINAL INSTRUCTION

Be skeptical.

Do not optimize for preserving confidence.

Do not reward the project simply because it has many notebooks.

The most useful answer may be:

> "Your current framing is wrong, but the experiments exposed a better question."

If so, say that clearly.

Use the notebooks and local source corpus only where they materially improve your reasoning.

Spend the bulk of your effort on **research judgment**, not repository archaeology.
