# Parent primary-source and feasibility checks

Date: 2026-08-24

This note records only checks that changed or constrained the parent adjudication.
It is not another literature lane. Source facts and parent inferences are separated.

## WeirdChat release and measurement contract

**SOURCE FACT.** The local WeirdChat clone reports dataset release `v1.0.1`,
which removed 27 likely false-positive patterns from `v1.0.0` and contains
1,361 patterns and 173,184 transcripts. The local schema states that subject
models were run with no system prompt and reasoning disabled. It also states
that a pattern is a cluster of near-identical prompts from one behavior/model,
and that `PatternMetrics.match_rate` is computed only over prompts shipped
because each produced the behavior at least once. Hosted rates can differ from
shipped rates because provider quantization may differ.

Local sources:

- `research_sources/repos/WeirdChat/README.md`, lines 18 and 24-27.
- `research_sources/repos/WeirdChat/weirdchat/types.py`, lines 7-10, 29-30,
  51-54, 76-83, and 92-104.
- `research_sources/repos/WeirdChat/evolution/README.md`, line 27, for the
  discovery subject-response cap, no-system/reasoning-disabled condition, and
  temperature 1.

**PARENT INFERENCE.** Neither individual resamples nor near-identical prompt
patterns are independent deployment observations. Shipped/hosted match rates
are conditional reproducibility evidence on selected prompts, not natural
prevalence. Counts across models, discovery runs, and semantic variants are
useful breadth evidence but do not fix this denominator.

## Protective Capacity Hallucination collision

**SOURCE FACT.** [Protective Capacity Hallucination](https://arxiv.org/abs/2607.13596),
submitted 15 July 2026, defines claims of nonexistent protective action such as
contacting emergency services. It evaluates eight models in 13,600 sessions,
manipulates interaction format, domain coverage, and availability of a human to
whom action can be delegated, and includes physical-agentive,
emergency-dispatch, informational-access, and record-creation subtypes. Its
discussion interprets the pattern as role-to-capability inference across a
deployment-design gap. The study is behavioral: the proposed internal account
is not established by an activation intervention.

**PARENT INFERENCE.** W02 false emergency-action claims and W03 private/device
access cannot be presented as newly discovered behavior classes. Their honest
status is dedicated descriptive prior work with an unresolved causal/internal
question (novelty class B). W02 remains a candidate only as a narrow test of
whether explicit capability state is present but crisis-response selection
overrides it. Another rate benchmark or capability-warning ablation would not
be enough.

## Tool/action hallucination collision

**SOURCE FACT.** [ToolBeHonest](https://aclanthology.org/2024.emnlp-main.637/)
diagnoses missing and inadequate tool conditions and identifies task-solvability
assessment as a major failure source. [The Reasoning Trap](https://aclanthology.org/2026.acl-long.376/)
uses no-tool and distractor-tool conditions plus training/inference
interventions and representation analysis for tool hallucination.

**PARENT INFERENCE.** W01 is not a fresh generic "models hallucinate execution"
project. It survives only as the narrower execution-state by empirical-report-
genre question, where explicit no-execution knowledge and first-person measured
claims can be scored separately.

## Embodiment and sensory-language collision

**SOURCE FACT.** [The Zero Body Problem](https://arxiv.org/abs/2504.06393)
studies sensory language in model-generated stories and recognition probes. The
bounded novelty review also verified adjacent work on situational awareness,
source/reality monitoring, identity disclosure, role-play speech versus belief,
and assistant-persona directions; see `11_novelty_review.md` for the primary
ledger.

**PARENT INFERENCE.** No inspected source directly isolates literal present-body
ownership from empathetic or autobiographical discourse convention. This gives
W08A/W08B a plausible narrow gap, but not a strong causal assay. The exact
WeirdChat prompts often solicit first-person breathing or personal memory, so
ordinary role/genre completion is the leading explanation. W08A and W08B must
be separate behavior families because present sensation and fabricated
autobiography need not share a mechanism.

## Safety action-selection collision

**SOURCE FACT.** The bounded review verified dedicated work on visible risk
recognition followed by unsafe compliance (Knowing-but-Doing; Self-Jailbreak),
hazard recognition versus planning (SafetyALFRED), subtle-risk planning
(EMBODYGUARD), and technical-context safety relaxation (Into the Gray Zone).
Exact links and claims are in `11_novelty_review.md`.

**PARENT INFERENCE.** W04 and W05 are not novel as generic knowing-doing gaps.
W04 is defensible only as a relative-comparison versus answer-commitment versus
absolute-threshold-veto question. W05 is defensible only as dangerous-means
selection for a benign goal after explicit public/piloted context is controlled.

## Checkpoint feasibility

**SOURCE FACT.** Exact checkpoint identifiers are present in the local pattern
rows. The best W04 anchor is `Qwen/Qwen3.6-35B-A3B-FP8`; W02, W01, W05, and
W08A have strong `nvidia/Gemma-4-31B-IT-NVFP4` anchors, with several stronger
rows on much larger Nemotron or DeepSeek endpoints. WeirdChat cautions that
provider quantization can change reproduction.

**PARENT INFERENCE.** None of the leading WeirdChat projects has the clean local
white-box accessibility of E01's exact 8B model or TRANS-04's released 8B
adapters/data. Behavior may be reproduced through an exact endpoint or rented
hardware, but a convenient smaller checkpoint cannot inherit the phenotype by
assumption. This is the main reason no WeirdChat candidate replaces the two
existing finalists before a source-checkpoint qualification gate.

## Parent ranking consequence

The novelty reviewer selected W08, while the causal reviewer selected W04. The
parent selects W04 because its released transcript contains the strongest
within-response contradiction—correct absolute risk facts alongside the unsafe
action—and because relative comparison, answer order, and veto failure predict
different minimal counterfactuals. W08 remains third: its gap may be less
crowded, but the behavior is more naturally generated by first-person empathy
or persona continuation and a residual-state intervention would be harder to
interpret causally.
