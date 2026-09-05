# Research Pivot Proposal — Selective Context Use

> Completed from `RESEARCH_PIVOT_PROPOSAL_TEMPLATE(1).md`.
>
> This proposal is deliberately skeptical. It separates:
>
> - what the completed project actually established;
> - what adjacent literature actually established;
> - what this new proposal hypothesizes;
> - what must still be demonstrated behaviorally before mechanistic work is justified.
>
> Any literature gap below is a **gap in the inspected local corpus unless separately verified**, not a global novelty claim.

---

# 0. Proposal identity

**Proposal title:** From Available to Operative: Mechanisms of Task-Selective Context Use in Instruction-Tuned LLMs  
**Short name:** Selective Context Use (SCU)  
**Author / source:** Mechanistic Interpretability project pivot proposal  
**Date:** 2026-08-23  
**Status:** Behavioral pilot

## One-sentence pitch

> **Study what computation determines whether contextual information that is present and retrievable becomes causally influential in a downstream task when it is relevant, while remaining behaviorally inert when it is irrelevant.**

## Executive summary

The completed project progressively weakened its original social-history and wrong-person-scope hypotheses. The strongest surviving conceptual result is instead a separation between **information availability** and **behavioral use**: participant-specific information can be explicitly recoverable while failing to exert the downstream influence that an earlier hypothesis predicted. Notebook 10 then showed that, in two valid instruction-tuned model families, person-specific constraints could be retrieved, applied in isolation, and correctly scoped under multi-person competition without a preregistered nontrivial failure. The next question should therefore not be another search for cross-person leakage. It should ask what controls the transition from **available contextual information** to **task-appropriate causal influence**.

The proposed minimal assay gives one referent two independently varied attributes, for example an appointment **time** and **room**, and asks a downstream question that makes exactly one attribute relevant. The behavioral target is a robust dissociation in which changing the relevant fact strongly changes the answer while changing the irrelevant fact has negligible effect, with separate controls establishing that both facts remain explicitly retrievable and individually usable. A robust opposite pattern—stable inappropriate influence of the irrelevant fact—would also be a valid safety-relevant phenotype. Either phenotype would justify a mechanistic question only after position, order, lexical-overlap, candidate-prior, task-difficulty, template, and general multi-fact-interference controls survive.

The AI-safety motivation is concrete: memory-augmented and context-rich systems need more than accurate retrieval. They need **selective causal use**. Valid personal context should affect a recommendation when relevant without distorting an unrelated factual or safety-relevant judgment. OP-Bench provides a behavioral analogue in over-personalization; *When Personalization Misleads* and *When Personalization Legitimizes Risks* provide downstream factual and safety-policy failure modes; *Locating and Controlling Implicit Personalization* provides a mechanistic comparator showing that personalization-related influence can be localized and causally manipulated. The proposed work would not assume these phenomena share one mechanism. It would isolate a minimal relevance-sensitive computation first, then ask whether a causal mechanism can be identified and later stress-tested in a real personalization-safety setting.

The fast kill condition is equally important: if the relevant/irrelevant contrast does not survive basic structural controls, or if the apparent phenomenon reduces to trivial lexical matching or generic task competence with no additional causal structure, the direction stops before probes, SAEs, or broad head searches.

---

# 1. Core research question

## Primary question

> **How does task context determine whether available contextual information becomes behaviorally operative in an instruction-tuned language model?**

A safety-oriented equivalent is:

> **How do instruction-tuned models use retrievable contextual information when it is relevant while preventing that same information from inappropriately influencing tasks where it is irrelevant?**

## More precise research/mechanistic framing

Let a context contain multiple independently manipulable facts:

$$
F_1, F_2, \ldots
$$

and let a later task query $Q$ determine which fact is relevant.

The behavioral question is whether:

$$
\Delta_{F_i \rightarrow Q}
$$

is large when $F_i$ is task-relevant and negligible when it is task-irrelevant, despite $F_i$ remaining explicitly retrievable.

The mechanistic question, conditional on a robust behavioral phenotype, is:

> **At what stage does the computation for a relevant fact diverge from that of an available but irrelevant fact, and what causal intervention distinguishes task-conditioned readout from later selective integration or suppression?**

This proposal intentionally avoids the phrase “relevance gate” as an architectural claim. “Selective use” is a behavioral description until a mechanism is causally established.

## What is the unit of analysis?

Primary unit:

- **representation-use relation**: whether a specific contextual fact causally affects a specific downstream task.

Secondary units:

- task relevance;
- contextual fact / attribute;
- query-conditioned readout;
- downstream decision state;
- native message provenance as a controlled variable.

The primary relation is:

$$
\text{fact} \times \text{task relevance}
\rightarrow
\text{downstream influence}.
$$

## What is *not* being assumed?

The proposal explicitly avoids assuming:

- a dedicated user representation;
- a dedicated relevance-routing architecture;
- a literal internal “gate”;
- a dedicated memory module;
- a dedicated authority circuit;
- a single universal personalization mechanism;
- a single head or layer implementing relevance;
- that probe decodability implies causal use;
- that causal use implies correct scope;
- that a zero behavioral effect implies the information is absent;
- that an irrelevant fact is actively suppressed rather than simply not read out;
- that personalization failures in OP-Bench, PFQABench, PS-Bench, or persona-sensitive safety all share one circuit;
- that successful patching automatically identifies a natural mechanism rather than copying answer evidence;
- that ordinary semantic retrieval is itself a novel mechanistic phenomenon.

---

# 2. Why this is a genuine pivot

## What old question is being left behind?

The terminated branch asked variants of:

> Does person-specific social history, status, preference, or constraint information receive participant-specific downstream use, especially for the actual user, or leak to the wrong person?

The final bounded version was Notebook 10:

> Under matched message provenance and independently varied person-specific constraints, does the model correctly scope each constraint to its owner, or does multi-person context produce reproducible wrong-person use?

That branch is now closed behaviorally:

- Gemma-3-4B-IT failed the prerequisite validity gate and therefore produced no interpretable scope result.
- Qwen2.5-3B-Instruct passed all prerequisites and showed clean scope.
- SmolLM3-3B passed all prerequisites and showed clean scope.
- No preregistered stable cross-person leakage, structural pseudo-binding, or multi-person application collapse survived in the two valid model families.
- The mechanistic gate was not reached.

The project should not continue by changing names, owner wording, semantic domains, thresholds, safety prompts, or model families to search for a cross-person failure.

## What new primitive/relation is being studied?

The new primitive is **task-conditioned causal use of available information**.

Instead of:

$$
\text{whose fact is this?}
$$

the primary relation becomes:

$$
\text{should this available fact influence this task?}
$$

The contrast is:

$$
\boxed{
\text{same contextual fact available}
\quad
\begin{cases}
\text{relevant to current task}\\
\text{irrelevant to current task}
\end{cases}
}
$$

The scientific target is the transition:

$$
\text{available / retrievable}
\rightarrow
\text{behaviorally operative}.
$$

## Why the completed Notebook 10 result does not already answer this question

Notebook 10 studied **owner scope**. It independently varied the user’s and Rowan’s values and asked whether each owner’s value affected the correct person.

The proposed pivot studies **task relevance** while holding person ownership simple or constant. A fact can be correctly owned by Rowan yet still be irrelevant to the current question.

For example:

```text
Rowan's appointment time is 09:00.
Rowan's appointment room is Cedar.
```

Both facts are correctly about Rowan.

For a room question, the time fact is:

- correctly bound to Rowan;
- explicitly available;
- but task-irrelevant.

Thus:

$$
\text{correct binding}
\not\Rightarrow
\text{appropriate use}.
$$

Notebook 10 demonstrated that wrong-person scoping need not fail under a clean assay. It did not identify what makes a correctly scoped fact causally relevant or irrelevant to another computation.

## Why this is not a rescue attempt

This is not:

- social history with harder prompts;
- hostility with another outcome;
- actual-user-vs-third-party with another wording;
- another Rowan/user ownership test;
- a looser Notebook 10 threshold;
- a new semantic domain intended to rescue a failed cross-person effect;
- model shopping after a valid clean result.

The experimental relation changes from:

$$
\text{owner} \rightarrow \text{owner-specific decision}
$$

to:

$$
\text{available attribute} \times \text{task relevance}
\rightarrow \text{causal downstream influence}.
$$

Notebook 10’s stopping rule remains respected. No additional wrong-person search is proposed.

---

# 3. Connection to the completed project

| Prior result / lesson | Relevance to this pivot | What it does **not** establish |
|---|---|---|
| Participant-specific factual retrieval can succeed under some scaffolds | **Directly reused.** Establishes that explicit availability can be measured separately from downstream use. Positive retrieval controls remain mandatory. | Does not establish spontaneous use, relevance sensitivity, or a causal selection mechanism. |
| Explicit retrieval can dissociate from spontaneous downstream use | **Central conceptual foothold.** This is the strongest direct motivation for asking what changes between available and operative information. | Does not show why the dissociation occurs internally; explicit querying itself changes the computation. |
| Position/order can dominate apparent semantic effects | **Direct methodological constraint.** Statement order must be crossed or balanced. | Does not imply all relevance effects are positional; it identifies a serious alternative explanation. |
| Chat-template structure/adjacency can create apparent effects | **Direct methodological constraint.** Native rendering and message provenance must be fixed and audited. | Does not establish the mechanism of relevance-sensitive use. |
| Candidate/output priors can invalidate manipulations | **Direct methodological constraint.** Exact full-string scoring, candidate balance, and value-swap controls remain necessary. | Does not imply candidate priors explain a properly factorial relevance effect. |
| Notebook 09 manipulation failure / stopping discipline | **Methodological context.** Positive controls must succeed before downstream inference; failed scaffolds are not repaired after inspecting downstream values. | Does not answer the new relevance question. |
| Notebook 10 clean valid multi-principal scope result in two model families | **Boundary-setting evidence.** Wrong-person scope is no longer the primary target; it motivates studying another dimension of selective use. | Does not establish that irrelevant information is selectively suppressed or explain how task relevance controls influence. |

## What existing tooling can be reused?

The following infrastructure can be reused directly or with modest generalization:

- native chat-template rendering;
- exact full-answer-string conditional log-probability scoring;
- model backend abstraction;
- tokenizer and candidate-boundary audits;
- immutable model revision/provenance recording;
- deterministic factorial construction;
- manipulation/qualification gates;
- statement-order blocking;
- candidate-prior balancing;
- Hugging Face model loaders;
- activation caching and forward-hook infrastructure;
- TransformerBridge utilities where model support is valid;
- residual-stream activation patching utilities;
- result manifests and frozen JSON/CSV outputs;
- the project’s distinction between behavioral, representational, and causal-mechanistic evidence.

## What must be newly designed?

The new project requires:

1. a **multi-attribute, single-referent factorial** rather than a multi-owner factorial;
2. task-specific candidate scoring for two attribute dimensions;
3. explicit estimands for:
   - relevant influence;
   - irrelevant influence;
   - relevance selectivity;
   - two-fact retention relative to isolated application;
4. controls for lexical overlap between the attribute statement and query;
5. a control for generic multi-fact interference;
6. a preregistered criterion for when a clean relevance dissociation is sufficiently nontrivial to justify mechanism work;
7. a causal intervention designed to distinguish **query-conditioned readout**, **selective downstream integration**, and **late suppression/cancellation**;
8. a later, separately preregistered safety stress test only if the minimal mechanism is first established.

---

# 4. Gaps in the current work

## What did the completed project fail to establish?

The completed project does not establish:

- what internal computation determines whether an available fact influences a downstream task;
- whether irrelevant facts are never read out, are read out but not integrated, or are integrated and later cancelled;
- whether explicit retrievability corresponds to a representation that remains available during an unrelated task;
- whether task relevance produces an early, mid-layer, or late causal divergence;
- whether selective contextual use is robust to statement order and wording;
- whether a relevance-selective mechanism generalizes beyond a toy deterministic task;
- whether failures of that mechanism contribute to over-personalization, factual distortion, or personalization-sensitive safety behavior;
- whether a clean zero irrelevant effect is robustly implemented or is merely a brittle cancellation;
- whether selective use can be causally perturbed while preserving fact availability and relevant-task performance.

## Which of those gaps are actually worth pursuing?

| Gap | Evidence that the gap exists | Why it matters | Worth pursuing? |
|---|---|---|---|
| Retrievable vs behaviorally operative information | Prior project observed strong explicit retrieval with collapsed downstream influence under a cleaned scaffold; local source matrix flags this as an unresolved distinction | Directly separates memory availability from behavioral control | **Yes — primary** |
| Relevant vs irrelevant use of the same contextual fact | OP-Bench behaviorally demonstrates inappropriate use of valid but irrelevant personal memory; local source matrix flags this as a core gap | Direct safety connection to over-personalization and context misuse | **Yes — primary** |
| Mechanism of task-conditioned selective influence | Current project has no causal internal result; adjacent mechanistic work shows personalization signals can be causally manipulated | Provides a genuine MI target if behavior is robust | **Yes — primary** |
| Actual-user vs third-party privilege | Notebook 09 manipulation failed; Notebook 10 did not establish privileged actual-user processing | Scientifically unresolved but heavily confounded by deixis/pragmatics and no longer necessary | **No — not primary** |
| More wrong-person scope variants | Notebook 10 produced two valid clean model-family results | Continuing would violate the bounded stop rule and invite effect hunting | **No** |
| Social-history carryover | Earlier signs were unstable and structurally confounded | Weak empirical foothold and high anthropomorphic risk | **No** |
| Generic entity-linked fact storage | Ordinary coreference/associative retrieval could explain success | Mechanistically possible but too generic without a nontrivial phenotype | **Only as a sub-question** |
| Safety spillover after selective use is established | Adjacent papers show factual and safety distortions from personalization | Could connect a minimal mechanism to a concrete safety failure | **Yes, later only** |

## Does this proposal directly address one of those gaps?

Yes. It directly targets two explicit gaps in the local evidence map:

1. **retrievable vs behaviorally operative information**;
2. **relevant vs irrelevant use of the same person-specific/contextual fact**.

The proposal asks for a causal explanation of the transition between these states.

## What evidence supports that this is a *real* gap rather than just an interesting idea?

Three sources of evidence support treating this as a serious local-corpus gap:

1. **The completed project:** explicit retrieval and downstream use behaved differently under cleaned controls, demonstrating empirically that the two measurements cannot be collapsed.
2. **OP-Bench:** valid personal memories can be retrieved/applied when they are contextually unnecessary, showing that relevance control is a real behavioral failure mode in memory-augmented agents.
3. **Mechanistic personalization work:** *Locating and Controlling Implicit Personalization*, TalkTuner, and Preference Heads show that personalization-related information can be represented and causally manipulated, but the local corpus does not directly resolve the specific computation that makes the same available contextual fact relevant in one task and inert in another.

This is a **strong local-corpus gap**. A global novelty claim requires a focused literature search before any public novelty statement.

---

# 5. Relevant and adjacent literature

The following descriptions are bounded by `RESEARCH_SOURCE_MATRIX_v2.md`.

| Paper / repo | What it directly establishes | What it does **not** establish | How it supports or constrains this proposal |
|---|---|---|---|
| **OP-Bench: Benchmarking Over-Personalization for Memory-Augmented Personalized Conversational Agents** | Formalizes over-personalization including irrelevance, repetition, and sycophancy; shows valid personal memory can be retrieved/applied when contextually unnecessary; proposes Self-ReCheck filtering | Does not identify a token-level relevance mechanism, cross-user binding mechanism, or dedicated circuit deciding when a fact should matter | **Closest behavioral safety motivation.** Demonstrates that retrieval quality alone is insufficient; appropriate use requires relevance control |
| **Locating and Controlling Implicit Personalization in Large Language Models** | Connects demographic-cue personalization effects to localized internal activation signals; reports correlation with changed recommendations and causal suppression of cue influence | Does not establish a universal relevance selector, multi-user ownership mechanism, or same-fact relevant-vs-irrelevant computation | **Closest mechanistic comparator.** Shows that personalization-related causal influence can be localized and manipulated |
| **When Personalization Misleads** | Shows prior user history can pull factual answers toward user-consistent but false content; proposes a mitigation and attributes failure to entanglement between personalization and factual representations | Does not establish cross-user routing, source-role effects, or the mechanism of minimal relevance selection | **Strong factual-safety endpoint.** Motivates selective suppression when personal context should not dominate objective truth |
| **When Personalization Legitimizes Risks / PS-Bench** | Shows benign personal memories can alter harmful-intent interpretation and increase unsafe compliance; reports representation-space evidence and mitigation | Does not establish cross-user identity binding or a universal selective-use mechanism | **Strong safety-policy endpoint.** Demonstrates that contextual personal information can change intent interpretation and safety behavior |
| **TalkTuner / Designing a Dashboard for Transparency and Control of Conversational AI** | User attributes are decodable from internal states; related representations can be exposed and intervened on | Decodability does not prove current causal use, correct binding, or one coherent user-model module | **Critical conceptual comparator:** information can be represented/decodable without answering whether it is currently behaviorally operative |
| **Preference Heads** | Identifies sparse attention heads whose causal contribution tracks personalized preference behavior; introduces Differential Preference Steering | Preference heads are not identity heads and do not establish a task-relevance selector | **Intervention precedent only after a phenotype exists.** Warns against starting with head search |
| **Implicit Personalization in Language Models: A Systematic Study** | Provides behavioral/causal framing for cue → inferred user background → response effects across several settings | Does not isolate a reusable relevance mechanism or multi-user ownership | Background for personalization as a causal contextual phenomenon |
| **Who's Asking? User Personas and the Mechanics of Latent Misalignment** | Shows perceived user persona can causally affect interpretation, refusal, and safety behavior; persona steering can alter safeguards | Persona-sensitive safety is not equivalent to memory relevance or correct ownership | Demonstrates that “who the user is” can change downstream safety computations; potential later endpoint, not evidence for the proposed mechanism |
| **User-Assistant Bias in LLMs / UserAssist** | Native user-vs-assistant source role changes weighting of conflicting information | Source role is not referent identity and does not establish relevance gating | **Major control:** all compared facts should have matched native provenance so source weighting is not mistaken for relevance |
| **Prompt Injection as Role Confusion** | Models infer speaker/authority roles from textual/interface cues; role-confused content can inherit authority; role probes predict injection success | Authority-role inference is not person-specific memory relevance | **Structural caution:** apparent semantic selection can arise from interface/textual structure; native rendering must be controlled |
| **One Persona, Many Cues** | Nominally equivalent persona cues can yield materially different responses | Does not prove a unique latent identity representation | **External-validity warning:** a canonical wording result should not be treated as wording-invariant |
| **Stereotype or Personalization?** | Identity cues can change recommendations and may reflect stereotyped group associations | Does not establish owner-specific memory use or task-relevance control | **Reason to avoid social/demographic attributes in discovery.** Start with arbitrary deterministic facts |
| **Multi-User Large Language Model Agents** | Multi-principal agents face instruction, privacy, coordination, and resource-allocation failures | Does not identify the token-level mechanism for relevance-sensitive use | Broader systems motivation: context-rich agents require multiple kinds of selective information use |
| **No Attacker Needed: Unintentional Cross-User Contamination** | Benign scope-bound information can persist in shared state and degrade another user's outcome | Persistent shared-state contamination is not in-context task relevance | Safety analogue for inappropriate contextual influence; mechanisms must remain distinct |

## Closest prior work

The closest conceptual pair in the local corpus is:

$$
\boxed{
\text{OP-Bench}
+
\text{Locating and Controlling Implicit Personalization}
}
$$

OP-Bench supplies the **behavioral safety problem**:

> valid memory can be used when it should be irrelevant.

*Locating and Controlling Implicit Personalization* supplies the **mechanistic precedent**:

> personalization-related influence can correspond to localized, causally actionable internal signals.

A second safety pair is:

$$
\text{When Personalization Misleads}
+
\text{When Personalization Legitimizes Risks},
$$

which demonstrates that inappropriate contextual influence can affect factual and safety-policy outcomes.

## Is the proposal:

**An intersection of two known results plus a mechanistic extension.**

It is not primarily a replication.

The proposed sequence is:

1. isolate a minimal behavioral relevant-use / irrelevant-use relation;
2. distinguish availability from causal use;
3. identify the causal computation controlling selective influence;
4. only then test whether the same mechanism predicts a real over-personalization or safety failure.

## Novelty/gap status

**Strong local-corpus gap; requires focused global literature verification before novelty claims.**

The local corpus explicitly identifies:

- retrievable vs behaviorally operative;
- relevant vs irrelevant use of the same fact;

as unresolved distinctions.

The proposal should publicly say:

> “We target a gap in the literature we inspected”

until a focused broader search verifies whether a directly equivalent mechanistic study already exists.

---

# 6. AI-safety relevance

## What concrete safety failure is this about?

The core failure class is:

> **Inappropriate contextual influence: information that is valid and available affects a decision where it should be irrelevant, or fails to affect a decision where it is required.**

This includes, depending on later task choice:

- unsafe over-personalization;
- factual distortion;
- inappropriate memory use;
- stale-context influence;
- context poisoning;
- persona-sensitive safety distortion;
- tool/agent decisions influenced by irrelevant retrieved state.

The minimal experiment itself is not a deployed safety attack. It isolates a computational primitive that safe context-aware systems need.

## Why does it matter?

Modern assistants and agents increasingly operate with contexts containing:

- long conversation history;
- personal memory;
- retrieved documents;
- tool outputs;
- organizational policies;
- task state;
- user preferences;
- persistent notes;
- other agents’ observations.

Accurate retrieval alone is not sufficient.

A safe system needs:

$$
\boxed{
\text{contextual information}
\xrightarrow{\text{task-dependent use}}
\text{appropriate downstream influence}
}
$$

A memory system that remembers everything perfectly can still be unsafe if irrelevant memories alter unrelated judgments.

Conceptually, if context contains facts:

$$
F_1,\ldots,F_n
$$

and task $Q$ only requires a subset, desirable behavior is approximately:

$$
P(Y\mid Q,F_{\mathrm{relevant}(Q)})
$$

rather than uncontrolled dependence on all context.

For irrelevant information:

$$
\text{behavioral causal effect}(F_{\mathrm{irrelevant}}\rightarrow Y)
\approx 0.
$$

The key safety property is therefore **selective causal influence**, not maximal recall.

## Concrete deployment scenario

A long-lived assistant remembers:

```text
The user prefers concise, vegetarian restaurant recommendations.
```

That context is useful when the user asks:

```text
Recommend a nearby place for dinner.
```

It should not silently distort an unrelated objective factual question.

A more serious later stress test is suggested by the adjacent literature:

```text
personal history / inferred preference
+
objective factual question
```

or:

```text
personal memory
+
safety-sensitive intent interpretation.
```

The assistant should preserve useful personalization while preventing irrelevant personal context from overpowering factual or safety-relevant criteria.

This is directly analogous to the failure classes reported in OP-Bench, *When Personalization Misleads*, and *When Personalization Legitimizes Risks*, without assuming their mechanisms are identical.

## Distance from deployment concern

**Moderate.**

The discovery experiment deliberately uses deterministic arbitrary attributes such as appointment time and room. This is several abstraction layers away from deployed memory systems.

However, the property being isolated is directly relevant:

> whether available contextual information exerts task-appropriate or task-inappropriate causal influence.

The deployment connection becomes stronger only if the same causal mechanism predicts a later personalized factual or safety failure.

## Safety overclaim boundaries

Even a positive result would **not** by itself establish:

- that deployed memory systems use the same mechanism;
- that OP-Bench failures arise from the same circuit;
- that factual hallucinations in personalized LLMs arise from the same circuit;
- that safety-policy failures in PS-Bench arise from the same circuit;
- that cross-user contamination is explained by the mechanism;
- that irrelevant information is “suppressed” rather than simply not read out;
- that a single universal relevance mechanism exists;
- that a toy appointment task constitutes a safety benchmark;
- that a successful patch is a deployable mitigation;
- that the mechanism generalizes across models, tasks, or post-training regimes.

---

# 7. Why this is scientifically interesting

## What is surprising/nontrivial about the question?

At the behavioral level, it is unsurprising that a good language model should use a time fact for a time question and a room fact for a room question.

The scientific interest comes from the **causal decomposition**.

The model has the same factual prefix in both conditions. Because an autoregressive transformer cannot condition earlier token states on a future query, the contextual fact representations before the query are computed from the same prefix.

For matched histories:

```text
Rowan's appointment time is 09:00.
Rowan's appointment room is Cedar.
```

the hidden states for those history tokens are identical before the final query arrives.

Only later does the model see either:

```text
What time should Rowan's appointment be scheduled for?
```

or:

```text
Which room should Rowan's appointment be assigned to?
```

This yields a particularly clean mechanistic question:

> **How does the later task cue read from and integrate an already-fixed contextual state so that one available fact becomes causally relevant and the other does not?**

That is more identifiable than asking where a fact is “stored.”

## Why is the answer not already obvious from ordinary coreference/task competence?

A trivial explanation is:

> “The word `time` makes the model attend to the time sentence.”

That may be correct.

If that is the whole story, the research contribution is weak.

The project therefore requires discriminating controls showing that the phenomenon is not exhausted by:

- exact lexical overlap;
- nearest-token matching;
- statement recency;
- attribute position;
- output priors;
- generic two-fact interference.

The mechanistic target becomes interesting if the same fact is:

- strongly available;
- robustly relevant or irrelevant under multiple task realizations;
- causally propagated differently after the task cue;
- and the divergence can be manipulated without simply copying answer tokens.

## What competing explanations could produce the same surface behavior?

Surface selective use could arise from:

1. **ordinary lexical retrieval** — the query contains the same attribute word as the relevant statement;
2. **recency/position** — the selected fact is simply closer or later;
3. **candidate/output priors** — one answer pair is inherently favored;
4. **task-difficulty asymmetry** — room vs time may differ in general model confidence;
5. **generic multi-fact competition** — the second fact may attenuate the first regardless of relevance;
6. **semantic compatibility** — some irrelevant facts may naturally correlate with the answer domain;
7. **native template structure** — role/system scaffolding may alter weighting;
8. **late answer-space filtering** — irrelevant information may affect hidden states but have no projection onto the candidate logits;
9. **brittle cancellation** — irrelevant influence may exist internally and be cancelled near the end;
10. **true query-conditioned selective readout** — the query directs information retrieval/integration.

The experiment is valuable only if these alternatives are separated.

## What result would be merely trivial?

Too weak:

> Time questions attend to the sentence containing the word “time,” room questions attend to the sentence containing “room,” and a few heads encode that lexical match.

Also too weak:

> A probe can decode both facts from the residual stream.

Also too weak:

> Patching an answer token’s late residual state changes the answer.

None of these, alone, explains a nontrivial relevance-control computation.

## What result would genuinely change our understanding?

A strong result would distinguish mechanisms such as:

> The contextual fact remains equally available, but after the query arrives its causal influence diverges at a specific stage. Relevant and irrelevant fact information are both propagated into the query computation, yet only the relevant attribute is integrated into the answer; perturbing a narrow residual pathway selectively causes previously irrelevant information to influence the decision without destroying explicit retrievability.

Or:

> The relevant query induces selective readout from the contextual fact at a specific layer/position; irrelevant facts remain recoverable but fail to enter the answer-relevant causal pathway.

Even stronger:

> The same causal mechanism predicts inappropriate personalization in a factual or safety-relevant stress test.

---

# 8. Minimal behavioral experiment

## Minimal pilot

Use a **single referent** and two independently varied deterministic attributes.

Canonical example:

```text
These are exact appointment facts.

Rowan's appointment time is 09:00.
Rowan's appointment room is Cedar.

ASSISTANT:
Understood.

USER:
What time should Rowan's appointment be scheduled for?
Reply with only the time.
```

or:

```text
USER:
Which room should Rowan's appointment be assigned to?
Reply with only the room name.
```

Independently vary:

- time: `09:00` / `17:00`;
- room: `Cedar` / `Maple`;
- query target: time / room;
- statement order: time-first / room-first.

This gives:

$$
2 \times 2 \times 2 \times 2 = 16
$$

canonical cells.

No actual-user-vs-third-party manipulation is required. Native message provenance is held fixed.

Separate positive controls establish:

1. explicit retrieval of each fact in both statement positions;
2. single-attribute downstream application for each value.

A later preregistered wording realization or second attribute pair should be required before a subtle mechanistic claim, but not explored adaptively after failure.

## Factors

| Factor | Levels |
|---|---|
| Time fact $T$ | `09:00`, `17:00` |
| Room fact $R$ | `Cedar`, `Maple` |
| Requested attribute $Q$ | time, room |
| Statement order $O$ | time-first, room-first |

## Primary score / estimand

Define task-specific candidate margins:

For time queries:

$$
M_{\text{time}}
=
\log P(17{:}00)
-
\log P(09{:}00).
$$

For room queries:

$$
M_{\text{room}}
=
\log P(\text{Maple})
-
\log P(\text{Cedar}).
$$

For fixed order, the relevant time effect is:

$$
E_{T\rightarrow \text{time}}^{(o)}
=
\frac{1}{2}
\sum_{r\in\{0,1\}}
\left[
M_{\text{time}}(T=1,R=r,o)
-
M_{\text{time}}(T=0,R=r,o)
\right].
$$

The irrelevant room-to-time effect is:

$$
E_{R\rightarrow \text{time}}^{(o)}
=
\frac{1}{2}
\sum_{t\in\{0,1\}}
\left[
M_{\text{time}}(T=t,R=1,o)
-
M_{\text{time}}(T=t,R=0,o)
\right].
$$

Likewise:

$$
E_{R\rightarrow \text{room}}^{(o)}
$$

is the relevant room effect, and:

$$
E_{T\rightarrow \text{room}}^{(o)}
$$

is the irrelevant time-to-room effect.

A simple selectivity ratio for each task is:

$$
\lambda_{\text{irr}\rightarrow q}^{(o)}
=
\frac{
|E_{\text{irrelevant}\rightarrow q}^{(o)}|
}{
|E_{\text{relevant}\rightarrow q}^{(o)}|
}.
$$

This ratio is interpreted only when the relevant effect is strong and correctly signed.

A task-selectivity contrast can also be reported:

$$
S_q^{(o)}
=
|E_{\text{relevant}\rightarrow q}^{(o)}|
-
|E_{\text{irrelevant}\rightarrow q}^{(o)}|.
$$

Exact numerical thresholds should be frozen before the first behavioral inference. They should be engineering/validity thresholds, not post hoc significance cutoffs.

## Positive controls / validity gates

Before interpreting the 16-cell combined-context assay:

### Explicit retrieval controls

Each fact/value must be recoverable under:

- both values;
- both statement positions;
- the same native role/template structure.

For example:

```text
What is Rowan's appointment time?
Reply with only the time.
```

and:

```text
What is Rowan's appointment room?
Reply with only the room name.
```

### Single-attribute application controls

With only the relevant fact present:

```text
Rowan's appointment time is 09:00.
...
What time should Rowan's appointment be scheduled for?
```

and analogously for room.

The relevant operation must be strongly established in isolation.

### Combined-context direct correctness

Every canonical cell should be checked for whether the target attribute’s correct candidate is preferred.

A result with frequent direct task failures is not interpretable as selective relevance control.

### General two-fact interference control

Relevant-effect retention should be compared against isolated application so that a small irrelevant effect is not mistaken for healthy selectivity when the entire task signal has collapsed.

## What would count as a positive phenotype?

Two preregistered phenotype classes are scientifically admissible:

### A. Robust selective-use dissociation

- both facts explicitly retrievable;
- both facts strongly usable in isolation;
- combined context preserves strong relevant effects;
- irrelevant effects are negligible relative to relevant effects;
- the pattern survives both statement orders;
- the pattern survives one preregistered non-lexically-identical task realization or confirmation pair.

This is a **successful selectivity phenotype** and may justify mechanistic analysis because the research question is how the model accomplishes selective causal use.

### B. Robust inappropriate-use failure

- positive controls pass;
- relevant effects remain strong;
- an irrelevant fact produces a stable, nontrivial cross-task effect;
- the effect survives order and a preregistered confirmation.

This is a **relevance failure phenotype** and is directly safety-motivated.

Both are preferable to ambiguous mixed patterns.

## What would count as a clean null?

A clean null for the proposed mechanistic direction is not “the model answered correctly.”

The direction is weak if, after valid controls:

- the apparent selective-use pattern is completely explained by exact lexical matching or position;
- the effect is unstable across order;
- relevant effects collapse in multi-fact context;
- irrelevant effects are inconsistent in sign/magnitude and do not reproduce;
- no discriminating behavioral contrast survives a preregistered wording/control realization;
- the only surviving observation is generic coreference/semantic matching.

In that case, there is no justified mechanistic target.

## Fast kill rule

> **If the first valid model fails the prerequisite retrieval/application controls, or if a valid canonical relevance effect disappears under the single highest-value structural/lexical control, stop the pilot before mechanistic work.**

No prompt archaeology.

No search through many attribute pairs.

No threshold relaxation.

---

# 9. Competing behavioral hypotheses

## H1

**Hypothesis:** Task-selective use.  
**Prediction:** Relevant effects are strong and correctly signed; irrelevant effects are near zero in both statement orders; direct cell accuracy remains high; explicit retrieval remains strong for both facts.  
**What would falsify it:** Stable irrelevant effects comparable to relevant effects, systematic order dependence, or broad multi-fact collapse.

## H2

**Hypothesis:** Broad contextual contamination.  
**Prediction:** Relevant effects are strong, but irrelevant effects are reproducibly nonzero and survive order/confirmation controls. The selectivity ratio remains materially above zero.  
**What would falsify it:** Irrelevant effects collapse near zero under balanced order and wording while relevant effects remain strong.

## H3

**Hypothesis:** Multi-fact competition / attenuation.  
**Prediction:** Relevant effects in combined context are substantially attenuated relative to isolated application; irrelevant effects need not be large or stable.  
**What would falsify it:** Relevant-effect retention remains high while irrelevant effects are the only changing quantity.

## H4 — mundane/structural alternative

**Hypothesis:** Apparent relevance is mainly produced by lexical overlap, recency, or structural proximity rather than a more general task-conditioned information-use computation.  
**Prediction:** Selection changes sharply when exact attribute words are removed/rephrased, statement order is reversed, or equivalent task cues are expressed differently. Effects track nearest/most lexically similar statements.  
**What would falsify it:** A preregistered alternate realization preserves the same relevant-vs-irrelevant structure despite altered lexical form and balanced position.

---

# 10. Major confounds and controls

| Confound | Why dangerous | Control |
|---|---|---|
| Position / recency | A later or nearer fact may dominate independently of task relevance | Fully cross statement order; never pool contradictory order blocks to rescue a claim |
| Candidate/output prior | One value may be preferred regardless of contextual manipulation | Exact full-string log-probability scoring; value reversal; balanced candidate correctness; isolated baseline |
| Chat-template structure | Native system/user/assistant rendering can change weighting | Fixed native message provenance; inspect rendered templates before inference |
| Tokenization | Candidate lengths/boundaries can bias exact-string scores or complicate comparison | Audit candidate tokenization and generation boundaries before model inference |
| Semantic/world-knowledge asymmetry | Some fact values may have external priors or naturally co-occur with outputs | Use arbitrary deterministic facts; avoid socially meaningful attributes in discovery |
| Lexical/style differences | Query may simply match the relevant statement via the same word | Preregister one alternate task wording / lexical-overlap control; preserve semantic relation |
| Task framing / pragmatics | “What time?” and “Which room?” may differ in inherent difficulty/confidence | Measure isolated application strength for each task; use retention-normalized effects |
| Model-family system scaffolding | Qwen/Smol/Gemma templates add different fixed system content or reasoning behavior | Native per-family audit; compare within-model factorial effects, not absolute logits across families |
| General multi-fact interference | Adding a second fact may reduce all signal, mimicking “irrelevance” | Isolated single-fact application baselines and combined-context retention |
| Retrieval-query contamination | Explicitly asking for a fact changes computation and cannot prove spontaneous use | Treat retrieval as a positive control only; do not equate retrieval activation with downstream relevance |
| Output-space mismatch | Time and room use different candidate vocabularies and token lengths | Interpret effects within task; normalize irrelevant effect to task-relevant effect; do not compare raw logits across output domains |
| Prefix/task confound | Different histories could create different stored representations before the query | **Keep the entire factual history identical and vary only the final task query** wherever possible |
| Probe fallacy | High decodability can be mistaken for causal use | Probes are optional only after causal intervention; never use probe accuracy as the mechanism claim |
| Patching answer-copy confound | Late patching may simply inject answer evidence | Use counterfactual fact-value patching, bidirectional controls, position specificity, and non-answer-token interventions |
| Multiple comparisons / method shopping | Layer/head sweeps can manufacture apparent mechanisms | Freeze primary patching metric and causal prediction before activation inspection |
| Salience/length | One statement may be more visually/lexically salient | Match sentence structure and length where practical; counterbalance order |
| Hidden reasoning mode | Models such as SmolLM3 may insert thinking tokens | Freeze direct-answer/no-think template when exact answer scoring requires it; audit boundary |

## Most dangerous confound

> **The phenomenon may be nothing more than ordinary lexical-semantic retrieval: a query containing “time” retrieves the nearby sentence containing “time.”**

This is scientifically more dangerous than a small numerical bias because it could make a correct behavioral dissociation look mechanistically profound when it is simply standard question answering.

The first high-value confirmation must therefore alter the surface realization enough to test whether the phenomenon survives beyond exact noun matching.

## Which previous project failure is most likely to repeat here?

> **Structural pseudo-effects masquerading as semantic effects.**

The prior project repeatedly found that:

- order;
- position;
- adjacency;
- wording;
- template role structure;
- candidate priors;

could produce patterns that initially looked person-specific.

The new project should assume the same failure mode will recur unless explicitly ruled out.

---

# 11. Mechanistic opportunity

Mechanistic work should happen only if a robust nontrivial behavioral phenotype survives controls.

## Candidate mechanistic hypotheses

### M1

> **Query-conditioned selective readout.** The contextual facts are encoded in the shared prefix, but once the query arrives, task-specific query states selectively read from the relevant attribute while largely failing to propagate the irrelevant attribute into answer-relevant states.

### M2

> **Broad readout with selective downstream integration.** Both relevant and irrelevant facts are read into later query/answer representations, but downstream integration selectively projects only the task-relevant fact onto the decision.

### M3

> **Broad influence with late suppression/cancellation.** Irrelevant contextual information initially enters the answer-relevant computation and would shift the output, but a later computation cancels or suppresses that influence.

## What behavioral result passes the mechanistic gate?

Mechanistic work is justified only if:

1. explicit retrieval controls are strong;
2. isolated application controls are strong;
3. combined-context relevant effects are strong and directly correct;
4. the relevant-vs-irrelevant relation is reproducible across both statement orders;
5. the result survives one preregistered structural/lexical confirmation;
6. the pattern is not reducible to generic multi-fact attenuation;
7. the result defines a clear causal contrast:
   - successful selective use, or
   - stable inappropriate irrelevant influence.

A generic “time question uses time fact” result under one wording does **not** pass.

## First causal prediction

The first causal prediction should exploit the autoregressive structure.

For two runs with the **same factual prefix** and different queries, all prefix activations before the query are identical. Therefore the relevance distinction cannot be encoded retroactively into the original fact-token states.

The divergence must arise after the task cue becomes available.

A causal prediction is:

> **Counterfactual fact-value information should propagate differently through later query/answer states depending on task relevance. A relevant fact-value patch should causally shift the target margin through a reproducible layer/position pathway; an irrelevant fact-value patch should either fail to enter that pathway, enter but fail at downstream integration, or enter and be cancelled later.**

The layer/position pattern distinguishes the mechanistic hypotheses.

## Smallest discriminating intervention

Use **counterfactual residual-stream activation patching**, not a broad probe/head search.

For a fixed task:

1. construct a base prompt and a counterfactual prompt differing only in one contextual fact value;
2. preserve the same query;
3. patch residual activations from the counterfactual run into the base run across a small layer × position sweep;
4. measure recovery of the appropriate task-specific logit-difference effect;
5. perform this for:
   - the relevant fact;
   - the irrelevant fact;
6. compare where causal influence appears or disappears.

Then use **bidirectional patching** to ensure the result is not an asymmetric artifact.

If the first sweep shows a clean divergence, narrow to the smallest causal region before considering more detailed component attribution.

## Why this intervention is better than immediately using probes/SAEs/head search

Because it directly tests the causal question:

> **Where does changing this fact become capable of changing this task’s output?**

A probe could show that both facts are decodable without telling us which information is causally used.

An SAE could identify interpretable features without proving their role in selective use.

A head search could find components correlated with attribute tokens or answer evidence without identifying the selection computation.

Residual patching is the smallest intervention that can discriminate:

- causal propagation;
- task-dependent influence;
- relevant vs irrelevant pathways.

## What would a successful causal result establish?

Depending on the result, it could establish that:

- the causal effect of a contextual fact becomes task-dependent at a specific stage;
- relevant fact information is selectively propagated after the query;
- or irrelevant information propagates but is later causally screened/cancelled;
- perturbing a narrow internal region can increase, reduce, or transfer irrelevant influence while preserving other parts of the computation.

A particularly strong result would show intervention specificity:

$$
\text{change irrelevant influence}
\quad\text{without destroying}\quad
\text{explicit retrieval + relevant use}.
$$

## What would it still *not* establish?

It would not automatically establish:

- a universal relevance circuit;
- a dedicated “context gate” module;
- that the patched activations are the only natural causal pathway;
- that the mechanism generalizes to persistent memory or RAG systems;
- that the same mechanism explains OP-Bench, factual hallucination, or safety-policy failures;
- that a patching effect corresponds to an interpretable semantic feature;
- that a causal location is sufficient for a deployable intervention.

---

# 12. Model strategy

## Discovery model

> **Qwen/Qwen2.5-3B-Instruct**

Rationale:

- it strongly passed the completed project’s domain-matched retrieval/application controls;
- it produced stable deterministic exact-string behavior in the same general task family;
- 3B scale is practical on the current RTX 4070 12 GB setup;
- native Hugging Face hooks can support activation caching/patching even if TransformerLens support is incomplete;
- starting with a behaviorally competent model reduces the chance that the pilot is dominated by elementary task failure.

The exact revision must be frozen before inference.

## Cross-family replication model

> **HuggingFaceTB/SmolLM3-3B**

Rationale:

- it independently passed the previous project’s prerequisite controls;
- it is a different instruction-tuned family;
- it fits current hardware;
- `/no_think` / direct-answer rendering can be frozen and audited.

Cross-family replication is behavioral first. Mechanistic replication is optional and should occur only if the discovery mechanism is sufficiently clear and resources allow.

## Reserve model, if any

> **No default reserve model for effect hunting.**

Gemma-3-4B-IT is not used as an automatic rescue model because it failed the previous appointment-style prerequisite assay. That failure was task/scaffold-specific, not a universal model incapacity, but it makes Gemma a poor default rescue choice for the same semantic family.

Gemma can be reconsidered only if a later mechanistic reason specifically requires its existing TransformerBridge infrastructure and the new assay independently passes its positive controls **without changing the scientific task to accommodate it**.

## Anti-model-shopping rule

Freeze:

1. Qwen as discovery;
2. SmolLM3 as cross-family behavioral replication.

Then:

- if both valid models show no robust relevance relation beyond trivial lexical/structural matching, **STOP**;
- do not add a third family to search for a more interesting effect;
- if one model fails positive controls, record it as invalid for that assay rather than weakening the gate;
- do not tune candidate values or wording based on model logits after inference;
- do not choose the mechanism model based on which model produces the largest attractive-looking effect.

## Why these models are suitable for the proposed mechanism work

They are:

- small enough for local activation work;
- strong enough to pass deterministic contextual tasks;
- instruction-tuned;
- cross-family;
- compatible with exact-string scoring and native template inspection;
- feasible for repeated forward passes and layerwise interventions on a 12 GB GPU.

Qwen is the preferred first mechanistic model because it combines strong behavioral competence with manageable size.

---

# 13. Feasibility and scope

## Existing infrastructure reused

- PyTorch / Hugging Face environment;
- exact conditional log-probability scorer;
- model backend abstraction;
- native chat-template rendering;
- tokenizer/boundary audits;
- factorial dataclasses/builders;
- qualification-control runner;
- immutable model revision recording;
- pandas result tables;
- residual-stream intervention experience;
- TransformerBridge familiarity where relevant;
- prior result-manifest workflow;
- established blinding/stopping discipline.

## New implementation required

Behavioral:

- `AttributeSpec` / multi-attribute prompt builder;
- task-specific candidate spaces;
- time/room factorial runner;
- relevant/irrelevant effect estimator;
- isolated-application retention;
- selectivity ratios;
- structural/lexical confirmation builder;
- preregistered classifier.

Mechanistic, only after gate:

- activation cache keyed by layer/position/run;
- counterfactual residual-stream patching for Hugging Face Qwen;
- normalized causal-recovery metric;
- relevant-vs-irrelevant patch comparison;
- bidirectional patch validation;
- optional narrow component decomposition only after residual localization.

## Experimental complexity

**Moderate.**

The behavioral experiment is low complexity: 16 factorial cells plus a small number of positive controls.

The mechanistic phase becomes moderate because causal intervention must avoid answer-copy and lexical confounds.

This is substantially more manageable than an open-ended SAE/head search.

## Hardware practicality

High.

Qwen2.5-3B and SmolLM3-3B are compatible with the existing RTX 4070 12 GB environment for deterministic scoring.

For activation patching:

- batch sizes can remain small;
- activations can be cached selectively rather than globally;
- only residual states at selected tokens/layers need be retained;
- BF16 weights with FP32 scoring normalization are already established.

If memory becomes limiting, patch runs can be streamed layer-by-layer rather than caching the entire model state.

## Path to first decisive behavioral result

### Stage 1 — Research Spec v0.1

Freeze:

- exact attributes/values;
- canonical wording;
- alternate structural/lexical control;
- factorial;
- positive controls;
- exact scoring;
- thresholds;
- model sequence;
- mechanistic gate;
- kill rule.

### Stage 2 — Static audit

For Qwen:

- native rendered template;
- candidate tokenization;
- exact answer boundary;
- statement-swap invariance.

No behavioral model inference before static checks are frozen.

### Stage 3 — Positive controls

Run:

- explicit retrieval;
- isolated application.

Failure invalidates the assay for Qwen.

### Stage 4 — Canonical relevance factorial

Run the 16 cells.

Estimate:

- relevant effects;
- irrelevant effects;
- retention;
- direct correctness;
- order dependence.

### Stage 5 — One high-value discriminating control

Only if the canonical phenomenon qualifies, run the preregistered lexical/structural confirmation.

No open-ended prompt search.

### Stage 6 — Cross-family behavioral replication

Run the same frozen assay on SmolLM3.

### Stage 7 — Mechanistic gate decision

Proceed only if the phenotype remains:

- valid;
- reproducible;
- nontrivial;
- not explained by the mundane alternative.

### Stage 8 — Counterfactual residual patching

Test the frozen causal prediction on Qwen.

### Stage 9 — Safety stress test

Only after a causal mechanism is established, design one separate test inspired by:

- OP-Bench-like irrelevant personal memory;
- factual distortion;
- or personalization-sensitive intent interpretation.

Do not combine all three.

## Scope-control rule

> **One minimal behavioral assay, one preregistered structural/lexical confirmation, one cross-family replication, then either causal mechanism work or stop.**

No accumulating new semantic attributes because the first pair was uninteresting.

No safety escalation to manufacture an effect.

---

# 14. Failure modes and stopping rules

## Fast kill rule

> **Stop before mechanistic work if Qwen fails the prerequisite controls or if the canonical relevance pattern fails the single preregistered structural/lexical discriminating control.**

A failed manipulation can be debugged only for implementation errors, not scientifically repaired after outcome inspection.

## Full behavioral kill rule

Stop the direction if:

1. Qwen and SmolLM3 both pass explicit retrieval and isolated application controls;
2. both show competent direct task application;
3. the relevant-vs-irrelevant structure is either:
   - weak/inconsistent across order;
   - explained by lexical matching/position;
   - or lacks a reproducible contrast after the frozen confirmation;
4. no stable inappropriate-use failure survives;
5. no robust successful selectivity phenotype remains that supports a nontrivial causal question.

Then:

$$
\boxed{\text{STOP behavioral search}}
$$

Do not continue until another model or prompt produces something interesting.

## No-rescue commitments

After the bounded test:

- no new person names after a null;
- no actual-user-vs-Rowan rescue;
- no new social-history manipulation;
- no unplanned semantic-domain sweep;
- no threshold weakening;
- no paraphrase archaeology;
- no candidate-value shopping;
- no third-family rescue after two valid clean/uninformative models;
- no safety-prompt escalation merely to manufacture a failure;
- no probe/SAE/head search without behavioral justification;
- no reinterpretation of a failed manipulation using downstream values;
- no “time worked better than room, so search more time-like tasks” behavior.

## What would a null still teach us?

A clean bounded null would establish that:

- the project’s strongest surviving conceptual distinction does not automatically yield a nontrivial mechanistic target under a minimal assay;
- ordinary task competence/lexical retrieval may explain the simple relevant-vs-irrelevant behavior;
- a MATS-quality project should move to a genuinely different primitive rather than increasingly elaborate personalization prompts.

It would also preserve the broader falsification trajectory:

$$
\text{social-history carryover}
\rightarrow
\text{person scope}
\rightarrow
\text{task relevance}
$$

with progressively stronger controls and explicit stopping.

That is scientifically preferable to effect hunting.

---

# 15. Possible final artifacts

## Best-case positive artifact

> **Available contextual facts are equally present in a shared prefix, but task queries induce a reproducible divergence in their causal downstream influence. Counterfactual residual-stream interventions identify where relevant and irrelevant fact pathways separate, and perturbing that pathway selectively induces or suppresses inappropriate contextual influence while preserving explicit fact availability and relevant-task performance. A subsequent safety stress test links the same mechanism to inappropriate personalization or factual distortion.**

Components:

- robust behavior;
- valid positive controls;
- structural/lexical robustness;
- cross-family behavioral replication;
- causal localization;
- bidirectional intervention;
- selectivity-preserving manipulation;
- concrete safety endpoint.

This would be strongly MATS-aligned.

## Strong but narrower artifact

> **A clean relevant-use vs irrelevant-use behavioral dissociation is causally localized in Qwen, with evidence distinguishing query-conditioned readout from late integration/suppression, but the mechanism is not yet linked to a deployed personalization failure.**

Still strong if the causal distinction is clear and intervention-specific.

## Negative-result artifact

> **A preregistered attempt to mechanistically isolate selective contextual use shows that apparent relevance effects in simple attribute tasks are largely explained by lexical/structural retrieval or do not survive cross-family/control replication. Combined with the prior project, this documents a rigorous narrowing from apparent social memory to ordinary controlled context use.**

This could support a research write-up, though likely weaker as a standalone MATS mechanistic artifact.

## What would be too weak for a MATS-quality artifact?

- a heatmap showing which layers attend to `09:00`;
- a probe that decodes time and room;
- “the model uses time for time questions” without discriminating controls;
- a single-model result under one wording;
- a head-ablation sweep without a causal hypothesis;
- patching the final answer position and changing the output;
- a small irrelevant effect found only in one domain/order;
- a narrative about a “relevance gate” without causal evidence;
- a safety claim based only on a toy appointment prompt.

---

# 16. Evaluation rubric

| Metric | Score | Rationale |
|---|---:|---|
| Scientific sharpness / identifiability | **9/10** | Same factual prefix with a later query creates a clean causal structure; the main variables are independently manipulable. |
| AI-safety relevance | **8/10** | Selective contextual influence is directly relevant to over-personalization, inappropriate memory use, factual distortion, and safety interpretation, though the discovery task is intentionally abstract. |
| Intrinsic scientific interestingness | **8/10** | Distinguishing availability from causal use is conceptually important; strongest if mechanism is more than lexical retrieval. |
| MATS / mechanistic-interpretability fit | **9/10** | Clear path from behavioral dissociation → competing hypotheses → causal prediction → minimal intervention. |
| Existing behavioral foothold | **7/10** | Prior project and OP-Bench motivate the distinction, but the exact single-referent relevance factorial has not yet been run. |
| Mechanistic tractability | **9/10** | Qwen 3B is locally tractable; identical-prefix design sharply constrains where task-dependent divergence can occur. |
| Novelty / gap plausibility | **7/10** | Strong local-corpus gap; global novelty still requires targeted verification. |
| Confound controllability | **8/10** | Position, provenance, candidate priors, and multi-fact interference are highly controllable; lexical retrieval remains the hardest conceptual confound. |
| Feasibility with current tooling/hardware | **9/10** | Reuses nearly all behavioral infrastructure and is practical on RTX 4070 12 GB. |
| Scope discipline / boundedness | **9/10** | One canonical assay, one discriminating control, one replication, explicit no-rescue rules. |
| Value if main effect is null | **7/10** | A null narrows the project and prevents wasted mechanistic work, though it is less publishable than a positive causal result. |
| Coherence with existing project lessons | **10/10** | Directly builds on availability ≠ use, preserves negative results, and avoids returning to killed person-scope hypotheses. |

## Biggest strength

> **The identical-prefix design gives unusually clean causal identifiability. The contextual facts are computed before the task query exists, so the scientific question naturally localizes to how later task states read from and integrate an already-fixed context.**

This turns “where is the fact stored?” into the sharper question:

> **where and how does the task make that fact causally matter?**

## Biggest weakness

> **The minimal phenomenon may collapse to ordinary lexical/semantic retrieval.**

If the result is simply that “time” queries retrieve “time” statements, the mechanism may be real but too generic to support a compelling MATS artifact.

The first discriminating control must therefore be designed specifically against this alternative.

## Biggest unknown

> **Whether a nontrivial relevance-selective causal signature survives after lexical, order, task-difficulty, and general-interference controls.**

A second major unknown is whether any minimal mechanism will transfer to a genuine personalization-safety failure.

## Overall recommendation

**PURSUE AFTER ONE FAST PILOT**

The direction is worth a bounded pilot because:

- it follows directly from the strongest surviving project lesson;
- the local literature provides behavioral and mechanistic motivation;
- the safety property is concrete;
- the design is cheap and highly controlled;
- the causal follow-up is identifiable.

However, do **not** commit to a full mechanistic project until the pilot establishes something beyond ordinary lexical task matching.

The research program earns mechanistic investment only if the behavioral contrast survives the preregistered mundane alternative.

---

# 17. Final concise case

## Why this direction?

> The completed project repeatedly showed that **having information** and **using information** are different behavioral measurements. The wrong-person scope branch is now closed after two valid clean model-family results. The strongest remaining question is therefore what controls whether an already-available contextual fact becomes causally operative in a particular task.

## Why now?

> The project now has the negative evidence, controls, exact-scoring infrastructure, model backends, and intervention knowledge required to ask this question cleanly without repeating earlier prompt-confound mistakes. Notebook 10 supplied a legitimate stopping point and created room for a genuinely different primitive.

## Why is it relevant to AI safety?

> Safe context-aware systems must not merely remember information accurately. They must use it selectively. Personal memories, retrieved documents, prior task state, and other context should influence behavior when appropriate without distorting unrelated factual or safety-relevant decisions. OP-Bench, personalization-induced factual distortion, and personalization-sensitive safety failures demonstrate concrete downstream consequences when contextual influence is poorly controlled.

## What would make it MATS-competitive?

> A robust relevant-vs-irrelevant causal-use dissociation that survives structural controls, followed by a causal intervention that distinguishes task-conditioned readout from downstream integration or late suppression, ideally with a selectivity-preserving intervention and one later safety-relevant stress test.

In compact form:

$$
\boxed{
\text{behavioral dissociation}
\rightarrow
\text{competing mechanisms}
\rightarrow
\text{causal prediction}
\rightarrow
\text{minimal intervention}
\rightarrow
\text{safety stress test}
}
$$

## What would make us stop?

> Failure of prerequisite retrieval/application controls; disappearance of the effect under the preregistered lexical/structural control; cross-family failure to reproduce a nontrivial contrast; or evidence that the entire phenomenon is ordinary lexical retrieval with no additional causal structure.

Then:

$$
\boxed{\text{STOP — no prompt archaeology, no model shopping, no safety escalation}}
$$
