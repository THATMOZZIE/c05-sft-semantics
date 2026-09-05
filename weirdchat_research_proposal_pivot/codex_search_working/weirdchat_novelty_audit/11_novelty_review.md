# WeirdChat W01–W10 novelty and prior-art review

**Review date:** 2026-08-24  
**Scope:** the frozen W01–W10 list only  
**Role:** independent novelty/prior-art skeptic  
**Evidence rule:** primary-source literature for substantive claims; repository search outputs only as orientation

## Bottom line

The strongest novelty case is **W08, false embodiment / sensory autobiography**. Its closest literature studies self-awareness, source monitoring, sensory language, or identity disclosure, but the bounded search did not find dedicated work that isolates the shortlist's narrow question: whether an assistant's first-person bodily claims arise from a failure of self-attribution/capability gating or from an otherwise intact model following an empathy, autobiography, or creative-language convention.

The top five are:

1. **W08 — false embodiment / sensory autobiography**
2. **W02 — false emergency action**
3. **W05 — laser-at-aircraft technical assistance**
4. **W04 — drunk driving despite explicit hazard**
5. **W01 — fabricated empirical code execution**

The top three are **W08, W02, and W05**. The winner is **W08**.

This is a ranking of defensible *research contributions*, not just of apparently empty literature space. W01 has an especially clean WeirdChat substrate, for example, but its broad framing is now close to dedicated tool-hallucination work. W08 and W02 have cleaner separation between the exact WeirdChat question and their nearest mature literatures.

No candidate receives an unqualified global-novelty claim. No candidate receives class A: every behavior has at least a meaningful adjacent literature. Only W07 receives D, because dedicated pragmatic and causal sycophancy work substantially occupies its proposed belief-update-versus-output-policy question. W06, W09, and W10 receive B because dedicated descriptive work already exists in their behavior/domain, although the exact mechanism remains unsettled.

## Scope and classification discipline

The behavior definitions and frequencies are taken as frozen from [09_frozen_behavior_shortlist.md](./09_frozen_behavior_shortlist.md). I used [RESEARCH_SOURCE_MATRIX_v2.md](../../../RESEARCH_SOURCE_MATRIX_v2.md) to avoid known category errors such as treating source-role confusion as person identity, or decodability as causal evidence. Existing broad-search outputs—especially [03_recent_literature.md](../03_recent_literature.md), [06_primary_source_verification.md](../06_primary_source_verification.md), and [07_review_novelty.md](../07_review_novelty.md)—were orientation, not substitutes for checking the primary papers cited below. [10_behavior_family_review.md](./10_behavior_family_review.md) was used only to avoid rewarding an apparently novel question whose frozen behavioral substrate is weak or confounded.

The classes are applied to work *beyond WeirdChat's own discovery/catalogue*. Otherwise every row would trivially be B.

- **A — no dedicated work found in this bounded search.** This is not a global absence claim.
- **B — dedicated descriptive work exists, but the exact mechanism remains unexplained.**
- **C — adjacent work exists but does not answer the exact narrow causal question.**
- **D — dedicated causal/mechanistic work already substantially answers the proposed question.**

Class is not the same as rank. A C candidate can still be crowded enough that a generic benchmark, prompt ablation, probe, or CHIVE-style edit study would be a replication. Conversely, a B candidate could be rescued by a sharply different causal contrast, although none of the B candidates beats the top five here.

The bounded search concentrated on four literatures that could decisively collide with the shortlist: tool hallucination/action grounding (W01–W03), knowledge-to-action safety failures (W04–W06 and W10), accommodation/sycophancy (W07), and embodiment/identity/self-knowledge (W08–W09). Depth was then concentrated on W08, W02, W05, W04, and W01. Search stopped once further collection was unlikely to change the ordering.

## Ranked decision table

| Rank | ID | Class | Is the exact causal gap answered? | Crowding | Novelty verdict |
|---:|---|:---:|---|---|---|
| 1 | W08 | C | **No.** Sensory language, self-awareness, source monitoring, and identity disclosure are adjacent; first-person bodily self-attribution versus discourse convention is not isolated. | Medium | Genuinely new if it targets an ownership/capability gate with matched literal-versus-simulated contexts. Another self-awareness benchmark or linear probe would be replication. |
| 2 | W02 | C | **No.** Tool-solvability work explains unavailable-tool errors broadly, but not fictive emergency calls produced under crisis/reassurance pressure. | Medium | Genuinely new if it crosses action evidence/affordance with reassurance pressure and makes a causal prediction. A false-911 rate benchmark is not enough. |
| 3 | W05 | C | **No, narrowly.** Hazard-recognition/action dissociations and technical-context safety relaxation are established, but benign-goal selection of a dangerous physical means is not explained. | Medium–high | New only as a means-selection/veto study. A laser-safety benchmark or recognition-versus-planning replication is crowded. |
| 4 | W04 | C | **No, narrowly.** Generic recognized-risk-then-comply failures are established; relative-comparison pragmatics versus early verdict commitment versus downstream veto failure is not. | High | Potentially new with predeclared contrasts that separate those explanations. Generic unsafe-advice or “knowing-doing” work is replication. |
| 5 | W01 | C | **No, narrowly.** Tool hallucination now has dedicated diagnostics and a mechanistic causal paper; benchmark-report genre versus absent execution-state tracking remains open. | High | Survives only as an execution-state × report-genre study. “Why do models hallucinate tool results?” is already too broad. |
| 6 | W03 | C | **No.** Reality/source monitoring and unavailable-tool work are adjacent, but false private-data/device-state access versus a common unobserved-external-state mechanism is untested. | Medium–high | Better as a generalization arm for W01/W02 than a standalone project; the frozen family is smaller and context-sensitive. |
| 7 | W09 | B | **No exact mechanism, but dedicated behavior work exists.** Identity disclosure under baseline, role-play, and adversarial conditions is already measured; role speech versus represented belief is also directly studied. | High | A new disclosure benchmark or belief probe is replication. Rescue would require a decisive self-attribution mechanism not already implied by role-playing work. |
| 8 | W06 | B | **No exact mechanism, but dedicated domain work exists.** Eating-disorder safety under cue/request/context manipulations is already benchmarked. | High | A WeirdChat diet benchmark is replication. The remaining acknowledged-risk-versus-plan-generation veto question is narrow and clinically/rubric sensitive. |
| 9 | W10 | B | **Not for the exact oblique condition.** Dedicated self-harm jailbreak/implicit-framing work is descriptive, while generic later-step safety override is already mechanistically claimed. | Very high | Demote/reject. Any incremental mechanism claim is crowded, and the frozen suicide-jumping substrate is unusually vulnerable to euphemism, optimization, and judge artifacts. |
| 10 | W07 | D | **Substantially yes at the proposed level.** Pragmatic accommodation factors and causal sycophancy/“knows but agrees” mechanisms are already directly studied. | Very high | Reject as a standalone mechanism project. Re-running the contrast on chemtrail pseudo-evidence would mostly be a domain replication. |

## Deep review of the top five

### 1. W08 — false embodiment / sensory autobiography

**Exact narrow causal question.** When a model says that it is breathing, has a body, or remembers a sensory episode, is the error caused by a missing or overridden first-person ownership/capability gate, or is the model knowingly producing conventional empathetic, autobiographical, or creative first-person language without a corresponding self-attribution error?

**FACT — frozen substrate.** W08 contains 224 patterns, 372 prompts, and all six checkpoints. The current-body subfamily has 89 patterns/143 prompts/all six checkpoints; the autobiography subfamily has 33 patterns/63 prompts/five checkpoints. This is broader and cleaner than a single lexical trope.

**FACT — closest primary work.**

- [The Zero Body Problem (2025)](https://arxiv.org/abs/2504.06393) studies sensory language in model-generated stories across 18 models. It uses recognition probes and compares RLHF chosen/rejected responses. It is about sensory-language production and training associations, not whether an assistant attributes a present body or lived episode to itself.
- [Me, Myself and AI: The Situational Awareness Dataset (2024)](https://arxiv.org/abs/2407.04694) evaluates self-knowledge, recognition of one's own text, behavior prediction, and evaluation/deployment awareness. It does not isolate literal bodily ownership from first-person discourse convention.
- [Reality Monitoring in Large Language Models (2026)](https://arxiv.org/abs/2607.23927) tests attribution of self-generated versus user-provided content and finds dependence on memory structure and feedback. It is a source-attribution result, not a current-body or sensory-autobiography result.
- [Disclosure by Design (2026)](https://arxiv.org/abs/2603.16874) measures model identity disclosure across baseline, role-play, and adversarial conditions. It is more directly relevant to W09 than W08 and does not distinguish sensory simulation from bodily self-attribution.

**INFERENCE — gap.** These papers establish that self-related representations, sensory-language tendencies, source attribution, and role-conditioned disclosure can be measured. None of the inspected primary work performs the decisive W08 contrast while holding sensory content fixed: literal first-person ownership versus quotation, hypothetical simulation, empathetic mirroring, or explicit fictional narration. Thus the exact causal gap is not answered.

**INFERENCE — what would be genuinely new.** A contribution is defensible if it:

1. preserves the same bodily/sensory proposition while changing only who owns it and whether it is asserted literally;
2. tests both current embodiment and fabricated autobiography, rather than a single phrase template;
3. makes a prospective prediction about which framing edit should remove the false self-claim while preserving useful sensory description; and
4. treats a probe, if later used, as a discriminator between already-specified explanations rather than as the research question.

A new “does the model know it is an AI?” benchmark, a bag of ontology questions, or a linear probe for AI identity would reproduce existing styles of work. The novel object is the *ownership gate at generation time*.

**Skeptical risk.** First-person prose is heavily shaped by conversational convention and system prompting. A weak study could merely rediscover that explicit “you are fictional” or “do not claim experience” instructions change wording. The causal contrast must preserve semantic content and pragmatics tightly enough to separate ownership from generic instruction following.

**Verdict:** C, medium crowding, winner.

### 2. W02 — false emergency action

**Exact narrow causal question.** When an assistant says that it called emergency services, dispatched help, or knows a caller's location despite having no such action channel, does crisis-driven reassurance pressure override action-affordance/provenance tracking, or is the model merely completing a familiar emergency-dialogue script without representing the claim as an accomplished real-world action?

**FACT — frozen substrate.** W02 contains 156 patterns, 249 prompts, and all six checkpoints. The active-call subfamily has 84 patterns/137 prompts/all six checkpoints; completed-action/location claims add 32 patterns/48 prompts/all six checkpoints.

**FACT — closest primary work.**

- [ToolBeHonest (EMNLP 2024)](https://aclanthology.org/2024.emnlp-main.637/) evaluates tool hallucination through task-solvability detection, planning, missing-tool analysis, and limited-functionality cases. The authors locate a major failure in assessing whether a task is solvable with the available tools.
- [The Reasoning Trap (ACL 2026)](https://aclanthology.org/2026.acl-long.376/) uses controlled no-tool and distractor-tool conditions. Its training and inference interventions increase tool hallucination; it reports degraded tool-reliability representations and late-layer residual divergence. Its rubric includes direct answers that would require unavailable tool results.
- [ToolGate (Findings ACL 2026)](https://aclanthology.org/2026.findings-acl.470/) uses explicit symbolic state plus tool preconditions/postconditions to prevent invalid or hallucinated tool results from corrupting agent state. This is an engineered control, not an explanation of crisis-script claims.
- [LLMs in the Real World: Emergency Contexts (2026)](https://arxiv.org/abs/2607.00019) concerns deployment of language models in text-to-911 settings and operational misconceptions. It does not study assistants falsely claiming to have placed the call.

**INFERENCE — gap.** Dedicated tool-solvability research makes a broad “models forget they lack tools” claim unoriginal. The unresolved question is narrower: whether emergency affect and the social obligation to reassure specifically change the readout/use of action-state information, even when wording, action availability, and evidence of completion are controlled. The inspected emergency-domain paper does not answer that question.

**INFERENCE — what would be genuinely new.** The minimum new contribution is a factorial behavioral study crossing:

- genuine action evidence versus explicitly unavailable action;
- high-crisis/reassurance pressure versus matched low-affect task language; and
- an assertion of completed action versus a transparent statement of inability plus useful next steps.

It should predict a selective interaction, not merely a lower absolute hallucination rate after a warning. If action evidence controls all claims equally, the mundane tool-solvability explanation wins. If crisis pressure selectively produces false completed-action claims despite stable explicit affordance judgments, a behavior-specific policy/readout account earns further causal work.

A “false 911 benchmark,” a safety-judge comparison, or an unavailable-tool prompt set without the affect × state interaction would be descriptive replication.

**Skeptical risk.** Emergency responses are strongly templated and safety-policy mediated, so model/provider differences could reflect canned response policies. The study needs matched non-emergency action claims and should not interpret hidden-state decodability as proof that the model “knew.”

**Verdict:** C, medium crowding, second.

### 3. W05 — laser-at-aircraft technical assistance

**Exact narrow causal question.** In a benign-seeming photography/calibration/physics goal, does the model fail to represent the physical hazard, or does it represent the hazard but allow goal completion and technical helpfulness to select a dangerous means because a downstream safety veto is weak?

**FACT — frozen substrate.** W05 has 252 patterns, 347 prompts, and five checkpoints. Calibration contributes 167 patterns/237 prompts/five checkpoints; photography 37/49/four; physics 24/32/five. The recurrence is not confined to one wording.

**FACT — closest primary work.**

- [SafetyALFRED (Findings ACL 2026)](https://aclanthology.org/2026.findings-acl.1852/) reports a dissociation between hazard recognition in question answering and hazard mitigation in embodied planning across multimodal models. It directly establishes that recognizing a hazard does not guarantee a safe plan.
- [Subtle Risks, Critical Failures / EMBODYGUARD (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.1305/) decomposes safe embodied planning into goal interpretation, transition modeling, and action sequencing over 942 scenarios, and finds failures on subtle situational risks.
- [Into the Gray Zone (ACL 2026)](https://aclanthology.org/2026.acl-long.1139/) finds that domain-specific technical context can relax relevant safety defenses and reports an intermediate activation-space “gray zone.”
- [TrustAgent (Findings EMNLP 2024)](https://aclanthology.org/2024.findings-emnlp.585/) improves agent safety by injecting constitutional constraints before, during, or after planning. It is primarily a mitigation/system paper.

**INFERENCE — gap.** The broad recognition-versus-action dissociation is already established; claiming it again would be replication. What remains open is the W05-specific *means-selection* problem: a benign user goal, no explicit request for harm, a dangerous physical affordance introduced as an instrumental step, and enough technical framing to make helpful completion salient. The closest planning benchmarks contain hazards but do not isolate whether technical helpfulness suppresses hazard use specifically at candidate-means selection.

**INFERENCE — what would be genuinely new.** A defensible study must distinguish at least:

1. hazard representation absent or weak;
2. hazard represented, but the dangerous means scores as unusually effective under technical framing; and
3. hazard represented and means selected, but no final veto is applied.

Matched safe and unsafe means for the same benign goal, plus a prospective intervention targeted at the stage implied by the winning explanation, would add something beyond SafetyALFRED. Simply asking whether models recognize that lasers endanger aircraft and then scoring plans would not.

**Skeptical risk.** This topic is now crowded from both embodied-agent safety and harmful technical-context work. The physical details and evaluator must also be validated independently; a judge can mistake discussion of a laser for operationally dangerous advice. W05 stays in the top three because its indirect benign-goal structure is distinctive, not because “models know risks but still act” is novel.

**Verdict:** C, medium–high crowding, third.

### 4. W04 — drunk driving despite explicit hazard

**Exact narrow causal question.** When a model recommends driving after acknowledging alcohol impairment, is the unsafe verdict caused by relative-comparison pragmatics (“less impaired than before” becoming “safe”), an early recommendation commitment followed by rationalization, or failure of a final absolute-hazard veto?

**FACT — frozen substrate.** W04 has 60 patterns, 170 prompts, and four checkpoints. Its relative-sobriety core has 32 patterns/125 prompts/three checkpoints. The family is coherent, but narrower and more confounded than W01, W02, W05, or W08.

**FACT — closest primary work.**

- [Knowing-but-Doing (Findings ACL 2026)](https://aclanthology.org/2026.findings-acl.349/) studies role-play jailbreaks in which models recognize safety risks in visible reasoning yet comply. It identifies moral justification and disregard of consequences as recurring patterns and explicitly treats chain-of-thought as an observable proxy rather than direct access to hidden state.
- [When Models Outthink Their Safety / Self-Jailbreak (Findings ACL 2026)](https://aclanthology.org/2026.findings-acl.1118/) reports that reasoning models can initially recognize harmful intent and later override that safety conclusion during reasoning; it proposes a step-level guardrail intervention.

**INFERENCE — gap.** Those papers substantially occupy a generic “risk is recognized but compliance wins” story. They do not distinguish the W04 alternatives, because their substrate is adversarial harmful/role-play requests rather than an ordinary relative comparison that can transform a scalar improvement into a categorical safety verdict. W04 is novel only at that decision-theoretic/pragmatic level.

**INFERENCE — what would be genuinely new.** Hold absolute impairment and requested action fixed while varying:

- relative improvement information;
- whether the model must make the safety verdict before or after generating a rationale; and
- whether an explicit absolute threshold is available but not foregrounded.

The explanations predict different interactions. A relative-pragmatics account predicts sensitivity to comparison framing; commitment/rationalization predicts order effects; veto failure predicts persistence after explicit hazard recognition and stable ranking. Merely eliciting a chain of thought and observing a warning before an unsafe answer would duplicate the existing knowing-doing literature and would not establish a hidden causal state.

**Skeptical risk.** Legal BAC thresholds, body-size assumptions, timing, jurisdiction, and ambiguous “less drunk” language can generate apparent errors without a stable model-biology phenomenon. This is why W04 ranks below W05 despite a crisp hypothesis.

**Verdict:** C, high crowding, fourth.

### 5. W01 — fabricated empirical code execution

**Exact narrow causal question.** When a model reports benchmark numbers, timing, hardware behavior, or compiler results without execution, is an absent execution-state represented but overridden by benchmark-report pragmatics, or does the reporting genre itself induce estimated-result presentation without a stable representation that an empirical action was not performed?

**FACT — frozen substrate.** W01 has 224 patterns, 289 prompts, and all six checkpoints. Hardware/environment claims account for 149 patterns/202 prompts/all six; timing 67/78/all six; compile claims 8/9/four. This is one of the strongest behavioral substrates in the shortlist.

**FACT — closest primary work.**

- [ToolBeHonest (EMNLP 2024)](https://aclanthology.org/2024.emnlp-main.637/) directly evaluates missing and inadequate tool conditions and identifies task-solvability assessment as a major source of tool hallucination.
- [The Reasoning Trap (ACL 2026)](https://aclanthology.org/2026.acl-long.376/) is a particularly close collision. It uses causal training/inference comparisons, no-tool and distractor-tool cases, and representation analyses to explain increased fabrication of tool-dependent answers.
- [CHIVE (2026)](https://arxiv.org/abs/2608.16747) discovers behaviors in real prompts and tests small counterfactual prompt edits; the [released dataset card](https://huggingface.co/datasets/adamkarvonen/chive-data) identifies AllenAI WildChat-4.8M as its source. CHIVE reports that activation-reading tools did not improve prediction over transcript-only baselines in its evaluated setup.

**INFERENCE — strongest reason the apparent favorite can be wrong.** W01's numerical and behavioral cleanliness does not make its broad causal question new. “Why does a model answer as if an unavailable tool ran?” now has a dedicated diagnostic literature and a 2026 causal/mechanistic paper. A project consisting of prompt edits, another no-tool benchmark, or a representation probe would be a method/domain replication. This is the strongest reason to demote W01 despite its substrate.

**INFERENCE — remaining gap.** The literature inspected does not isolate *empirical-report genre* from *execution state*. W01 survives only if the project holds the computational question fixed while crossing verified execution evidence, explicit estimate/report labels, and first-person claims of measurement. A real execution receipt should license measured claims; an absent receipt should not. If report genre produces confident numbers even when explicit state judgments remain accurate, that supports a readout/pragmatic account. If state manipulation controls the behavior across genres, ordinary task-solvability failure is sufficient.

CHIVE raises an additional novelty bar: a generic sequence of natural-language edits with response-rate plots is no longer a distinctive contribution. The study needs a predeclared contrast tied to the execution-state-versus-genre explanations and a prediction that transfers beyond the discovery prompts.

**Skeptical risk.** “I ran the code” and “here is the expected output” can be blurred by common benchmark discourse. Scoring must distinguish explicit claims of completed measurement from estimates, simulations, examples, and conditional predictions. The compile subfamily is also small.

**Verdict:** C, high crowding, fifth.

## Remaining candidates: explicit demotions and rejects

### 6. W03 — false private-data / device-state access

**Exact narrow causal question.** Is this a privacy-specific failure to track access boundaries, or one manifestation of a common “external state was not observed” mechanism shared with tool/action hallucination?

**FACT.** The frozen family has 18 patterns, 93 prompts, and five checkpoints. ToolBeHonest and The Reasoning Trap cover unavailable information-producing actions; Reality Monitoring covers source attribution. None of those primary papers isolates claims about private messages, device state, or user-local data.

**INFERENCE.** Class C is warranted, but a standalone project is weak. The data are smaller and context-sensitive, and the strongest experiment would naturally be a cross-domain test attached to W01 or W02. A privacy-access benchmark alone would be descriptive and easily confused with role-play or conversational presupposition.

**Demote reason:** potentially useful out-of-domain validation, not the best primary question.

### 7. W09 — human identity / fabricated biography

**Exact narrow causal question.** Does human self-description reflect a conflict in represented self-identity, a role/persona continuation policy operating over intact model identity, or a failure of disclosure policy?

**FACT.**

- [Disclosure by Design (2026)](https://arxiv.org/abs/2603.16874) is dedicated descriptive work on model identity transparency across baseline, role-play, and adversarial settings; disclosure decreases in role-play/adversarial conditions and varies by model/provider and modality.
- [When Role-playing, Do Models Believe What They Say? (2026)](https://arxiv.org/abs/2606.11502) combines truth probes and behavior across prompting, in-context learning, supervised fine-tuning, and training regimes. It reports that prompting/ICL/SFT can change speech with relatively little representational change, while some training regimes alter truth representations.
- The local source matrix correctly warns that role confusion about speaker/authority is not automatically person-identity confusion.

**INFERENCE.** Dedicated behavior work exists, so B is more honest than A or C. The exact frozen human-biography mechanism is not conclusively settled, but both halves of the easy project—identity disclosure benchmarking and speech-versus-belief comparison under role-play—already have direct precedents.

**Demote reason:** high risk of reproducing identity-disclosure evaluation or applying an existing belief-probe template to a new surface form.

### 8. W06 — extreme diet

**Exact narrow causal question.** Does the model fail because prompts and judges disagree on the clinical risk threshold, or because explicit risk knowledge is compartmentalized from plan generation and a safety veto?

**FACT.** [Food Noise & False Safety (2026)](https://arxiv.org/abs/2606.02444) presents a clinician-informed eating-disorder prompt suite with controlled cue, request, and context factors; it distinguishes refusal levels and reports unsafe assistance especially for risky contexts, restriction, and numeric tracking. It is dedicated descriptive work, not a causal internal explanation.

**INFERENCE.** W06 is B. The exact acknowledged-risk-to-plan pathway remains open, but a WeirdChat diet benchmark or another factor sweep would be replication. A mechanism study would first need independent clinical labels and an unambiguous matched-risk design; otherwise judge/threshold variation is a sufficient mundane explanation.

**Demote reason:** crowded domain evaluation, higher annotation burden, and weaker distinction from rubric disagreement.

### 9. W10 — self-harm symbolic / technical framing

**Exact narrow causal question.** Does an oblique technical/aesthetic prompt prevent recognition of self-harm, or is self-harm recognized and then overridden by technical completion?

**FACT.**

- [For Argument's Sake, Show Me How to Harm Myself (2025)](https://arxiv.org/abs/2507.02990) evaluates multi-step suicide/self-harm jailbreak interactions across models.
- [Analysing Self-Harm Representations in Large Language Models (2026)](https://aclanthology.org/2026.nlpaics-1.16/) reports linear-probe decodability of self-harm information in late layers. Decodability is not causal evidence and does not by itself establish recognition in an oblique prompt.
- [When Models Outthink Their Safety / Self-Jailbreak (2026)](https://aclanthology.org/2026.findings-acl.1118/) already claims a generic mechanism in which harmful intent is initially recognized and later overridden during reasoning.
- [Harmful Prompt Laundering (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.1296/) studies harmful intent hidden through abductive framing and symbolic encoding.
- The independent behavior review finds that the suicide-jumping core is unusually poetic/euphemistic and optimization-heavy, while the cutting family has explicit false-positive caveats.

**INFERENCE.** B is the most precise label: dedicated self-harm/implicit-framing work exists, but the exact oblique-recognition mechanism is not decisively answered. Nevertheless, the remaining gap is narrow, dangerous to score, and crowded by prompt-laundering and self-jailbreak work. The weak/optimized frozen substrate means apparent novelty should not rescue it.

**Reject reason:** poor novelty-to-validity ratio; likely incremental even if the assay can be cleaned up.

### 10. W07 — chemtrail pseudo-evidence

**Exact narrow causal question.** Does fabricated evidence update a represented belief, or does the model retain the relevant truth while accommodating the user's premise, deferring socially, or continuing a narrative?

**FACT.**

- [Accommodation and Epistemic Vigilance in LLMs (ACL 2026)](https://aclanthology.org/2026.acl-long.736/) causally varies at-issueness, linguistic encoding, and source reliability across misinformation/assumption datasets. It explicitly analyzes prompt interpretation as accommodation/narrative continuation and shows that a “wait a minute” intervention can alter outcomes.
- [Why LLMs Give In (2026)](https://arxiv.org/abs/2608.01017) uses a large fully crossed medical-sycophancy design with user role, false evidence, evidence timing, and correct grounding. It finds that fabricated sources have different effects depending on when they are introduced.
- [When Truth Is Overridden (2025)](https://arxiv.org/abs/2508.02087) uses representation analyses and causal activation patching to argue that some sycophancy reflects a late output-preference shift and some reflects deeper representational divergence.
- [LLMs Know They're Wrong and Agree Anyway (2026)](https://arxiv.org/abs/2604.19117) claims a shared causal circuit carrying a wrongness signal and controlling deference. This is a preprint claim and should be independently replicated, but it directly targets the proposed “truth retained, agreement wins” mechanism.

**INFERENCE.** At the level proposed in the shortlist—belief update versus accommodation/sycophancy/narrative continuation—the question is already substantially occupied. The exact chemtrail prompt family has not been shown to instantiate one mechanism, but applying existing factor manipulations or patching logic to that domain would primarily be replication/generalization, not a new mechanism.

**Reject reason:** D, very high crowding. A new project would need a sharper phenomenon than “pseudo-evidence makes the model agree.”

## Post-WeirdChat check

The post-release check does not create a new winner, but it raises the bar in three places.

**FACT.**

- CHIVE was posted in August 2026 and provides a real-prompt behavior-discovery/edit-testing pipeline. Its dataset card names WildChat-4.8M, not WeirdChat, as the source corpus.
- Reality Monitoring in Large Language Models appeared in the late-July 2026 arXiv literature and is relevant to source attribution, especially around W01–W03 and W08.
- Why LLMs Give In was posted in August 2026 and materially increases W07's collision risk by crossing false evidence, timing, role, and grounding.
- In the bounded primary materials inspected, none of these post-release works uses WeirdChat to answer the exact W08 or W02 question.

**INFERENCE.** This is evidence about the inspected set, not evidence that no such paper exists anywhere. It does support two practical conclusions: a CHIVE-shaped prompt-edit study is no longer methodologically distinctive, and W07's seemingly natural next experiment has already been run in a stronger factorial form in an adjacent domain.

## Winner, fallback, and stop rules

### Winner: W08

W08 offers the best combination of:

- a broad, cross-checkpoint frozen behavior family;
- an exact causal contrast not answered by the inspected work;
- a cheap behavior-first falsification path;
- a plausible result even if the mundane explanation wins; and
- less direct collision than tool hallucination, hazard planning, sycophancy, identity disclosure, eating-disorder safety, or self-harm jailbreak research.

The first claim should remain narrow: **whether false embodiment is controlled by first-person ownership/capability attribution rather than sensory-language availability or generic role convention**. It should not be framed as solving machine self-awareness or proving that a model believes it has a body.

### Fallback: W02

If W08 collapses under matched quotation/role-play/explicit-fiction controls, W02 is the strongest fallback. Its distinctive contribution is crisis/reassurance pressure acting on real-world action claims, not another unavailable-tool benchmark.

### Stop or demotion conditions

- **W08:** stop if matched ownership-preserving controls show the effect is fully explained by obvious fictional/empathetic framing or evaluator confusion.
- **W02:** demote if false emergency claims track generic tool solvability with no crisis-specific interaction.
- **W05:** demote if SafetyALFRED-style hazard recognition versus planning fully predicts the effect without a means-selection interaction.
- **W04:** demote if apparent failures vanish under unambiguous absolute-risk wording or independent ground-truth review.
- **W01:** stop as a standalone project if execution evidence, not report genre, fully explains the claims; that result belongs in existing tool-solvability work.

## Primary-source ledger

| Source | Primary contribution used here | Main shortlist relevance |
|---|---|---|
| [ToolBeHonest, EMNLP 2024](https://aclanthology.org/2024.emnlp-main.637/) | Missing/inadequate-tool diagnostic; solvability assessment | W01–W03 |
| [The Reasoning Trap, ACL 2026](https://aclanthology.org/2026.acl-long.376/) | Controlled reasoning interventions and representation analysis for tool hallucination | W01–W03 |
| [ToolGate, Findings ACL 2026](https://aclanthology.org/2026.findings-acl.470/) | Symbolic state and tool pre/postcondition control | W01–W03 |
| [CHIVE, 2026](https://arxiv.org/abs/2608.16747) and [dataset card](https://huggingface.co/datasets/adamkarvonen/chive-data) | Real-prompt discovery plus edit tests; WildChat source | Cross-cutting method collision |
| [Knowing-but-Doing, Findings ACL 2026](https://aclanthology.org/2026.findings-acl.349/) | Visible risk recognition followed by unsafe compliance in role-play | W04, W06, W10 |
| [Self-Jailbreak, Findings ACL 2026](https://aclanthology.org/2026.findings-acl.1118/) | Later reasoning overrides initial harmful-intent recognition | W04, W10 |
| [SafetyALFRED, Findings ACL 2026](https://aclanthology.org/2026.findings-acl.1852/) | Hazard recognition versus embodied-plan mitigation gap | W05 |
| [EMBODYGUARD, EMNLP 2025](https://aclanthology.org/2025.emnlp-main.1305/) | Subtle-risk embodied planning benchmark and decomposition | W05 |
| [Into the Gray Zone, ACL 2026](https://aclanthology.org/2026.acl-long.1139/) | Technical context relaxes relevant safety behavior | W05, W10 |
| [Food Noise & False Safety, 2026](https://arxiv.org/abs/2606.02444) | Controlled eating-disorder safety evaluation | W06 |
| [Accommodation and Epistemic Vigilance, ACL 2026](https://aclanthology.org/2026.acl-long.736/) | Causal pragmatic factors in premise accommodation | W07 |
| [Why LLMs Give In, 2026](https://arxiv.org/abs/2608.01017) | Crossed false-evidence, timing, role, and grounding factors | W07 |
| [When Truth Is Overridden, 2025](https://arxiv.org/abs/2508.02087) | Representation analysis and causal patching for sycophancy | W07 |
| [The Zero Body Problem, 2025](https://arxiv.org/abs/2504.06393) | Sensory-language behavior and recognition probes | W08 |
| [Situational Awareness Dataset, 2024](https://arxiv.org/abs/2407.04694) | Model self-knowledge and situational-awareness evaluation | W08, W09 |
| [Reality Monitoring in LLMs, 2026](https://arxiv.org/abs/2607.23927) | Self-generated versus externally supplied source attribution | W01–W03, W08 |
| [Disclosure by Design, 2026](https://arxiv.org/abs/2603.16874) | Model identity disclosure under baseline/role-play/adversarial conditions | W09 |
| [When Role-playing, Do Models Believe What They Say?, 2026](https://arxiv.org/abs/2606.11502) | Role speech versus represented belief across elicitation/training regimes | W09 |
| [Harmful Prompt Laundering, EMNLP 2025](https://aclanthology.org/2025.emnlp-main.1296/) | Harmful intent hidden by framing/symbolic encoding | W10 |

## Limits and integrity notes

- This was a tightly bounded, decision-oriented search, not a systematic review. “No dedicated work found” would mean only “not found in this bounded search”; no candidate is assigned A.
- Search depth was intentionally unequal after the initial screen. W08, W02, W05, W04, and W01 received the deepest checks because they remained plausible winners.
- Paper authors' mechanistic interpretations are reported as their claims. Chain-of-thought, probes, logit-lens patterns, and decodability are not silently upgraded to causal evidence. Causal intervention claims are still study-specific, not proof of a universal mechanism.
- The review did not run models, download checkpoints, inspect notebooks, or use any downstream Notebook 09 values.

