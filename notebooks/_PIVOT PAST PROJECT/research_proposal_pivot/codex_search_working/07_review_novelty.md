# Independent novelty and literature-skeptic review

**Review date / literature cutoff:** 2026-08-23  
**Scope:** only the ten candidates specified for this review.  
**Decision lens:** the frozen scoring protocol's novelty/upside view, constrained by
the behavior-first admission rule and the non-negotiable override that a nearby
paper answering the proposed causal question cannot be rescued by a high average
score.

## Bottom line

**INFERENCE — winner:** `C-02-RH-MON`, conditionally. Its publishable question is
not “does the appendix percentage reproduce?” but whether the released
reward-hacking weight delta changes monitorability on the *same precommitted
items*, after reporting the full joint distribution and separating item/trace
composition from conditional detection. It wins because the primary paper
labels the focal result illustrative and inconclusive, the safety consequence is
direct, and a denominator-corrected null would correct a live claim rather than
merely fail to extend it. It should lose winner status immediately if a powered
fixed-item reproduction does not establish the focal trajectory.

**INFERENCE — top 3:**

1. `C-02-RH-MON`
2. `TRANS-04`
3. `E01-CENSORSHIP`

**INFERENCE — top 5:** add `VL-01` and `C-04-ROLE-ANTICONTROL`.

**INFERENCE — hard novelty rejects:** `E02-EVAL-AWARENESS` and `TRANS-03`.
Their exact residual uncertainties are real, but newer/nearest work has already
run the causal behavioral comparisons that carry most of the scientific content;
adding open-model activations or another hint format would primarily be a method
port or benchmark replication.

**INFERENCE — main correction to the numerical registry:**
`C-05-SFT-SEMANTICS` should not be the winner. Its artifact completeness is
excellent, but completeness has been mistaken for both behavioral robustness and
novelty. The established endpoint is a judge score over synthetic interactive
audits in which the judge sees the very continuation rhetoric taught during SFT.
The paper's own example is advocacy, explicitly not refusal, deception, or action.
Therefore the proposed project must first establish a non-rhetorical action
phenotype and rebuild the training contrast. That is a valuable source-paper
validity study, but not yet the best behavior-first causal project.

## Ranked review

| Rank | Candidate | Is the exact causal gap already answered? | Contribution if executed as proposed | Crowding risk at cutoff | Verdict |
|---:|---|---|---|---|---|
| 1 | `C-02-RH-MON` | **No**, but the focal behavior is only preliminary | New only with fixed-item/joint-rate decomposition and reward-hack-specific control; increasing `n` alone is replication | **Very high** | Conditional winner |
| 2 | `TRANS-04` | **No**: vector ablation is not a matched interchange test | Genuinely new causal input-use audit if real-vector swaps are validated on the target; text baseline alone is benchmark auditing | **High** | Retain, top 3 |
| 3 | `E01-CENSORSHIP` | **Partly**: role/prefill sensitivity is answered; a selective separable gate is not | New only if a boundary intervention beats the paper's strong black-box methods selectively | **High** | Retain, top 3 |
| 4 | `VL-01` | **Partly**: trajectories and reasoning-effort effects exist; reveal-time causality does not | A randomized timing factorial is new, but it changes the task and is not white-box localization | **Very high** | Retain, demote from top 3 |
| 5 | `C-04-ROLE-ANTICONTROL` | **No**: the decisive coefficient range is omitted | New but small: a calibration/overshoot result, not a broad steering mechanism | **Extreme** | Compact fallback |
| 6 | `C-05-SFT-SEMANTICS` | **No** for semantics versus rhetoric; **yes/partly** for the broad “reasons improve transfer” claim | Primarily a source-paper measurement and ablation repair; only action-based transfer would elevate it | **Very high** | Demote |
| 7 | `C-01-SPP-RL` | **No**, because the RL behavior has not been run | Potentially new training study, but the proposed replay rescue does not identify overwrite versus relearning | **Extreme** | Demote / do not start yet |
| 8 | `D1-PSBENCH` | **No** for personal versus impersonal matched context | First stage is a necessary benchmark-validity control; mechanism is new only if a personal residual survives | **Medium-high** | Demote |
| 9 | `E02-EVAL-AWARENESS` | **Largely answered behaviorally**; open-Qwen internals remain open | Mostly a checkpoint/method port of sentence interventions and user-intent controls | **High** | Reject |
| 10 | `TRANS-03` | **Substantially crowded and partly answered** by newer counterfactual-prediction work | New hint forms and behavior-matched simulation are now a narrow replication/benchmark comparison | **Very high** | Reject |

### 1. `C-02-RH-MON` — conditional winner

**FACT.** The primary paper establishes the general implicit-versus-explicit
monitorability gap across four settings, but its OLMo reward-hacking trajectory
is in an appendix. It reports switch/detection pairs from `41%/75%` pre-RL to
`22%/25%` at step 1,200, while GPT-OSS retains `88–94%` detection. The authors
explicitly call the result “suggestive rather than conclusive” and “illustrative,”
noting small samples and possible mismatch between reward-hacking misalignment
and the contextual coding nudges. See [the primary paper, Appendix H](https://arxiv.org/html/2608.04735#A9).

**FACT.** Detection is conditioned on a library switch, while both the number
and identity of switch cases change over training. The originating study does
not provide a powered item-matched decomposition or a verified matched no-hack
RL control.

**INFERENCE.** The exact causal gap is unanswered. A publishable result must
report at least the joint event `switch AND detected`, fixed-item transitions,
trace length/style, and conditional detection; merely rerunning more samples of
Table 17 is a replication. Scaling the released adapter on fixed items can
causally implicate the released learned delta, but cannot by itself attribute the
effect specifically to *reward hacking*. That stronger claim requires a
provenance-matched no-hack continuation or an honestly scoped claim about this
one RL delta.

**INFERENCE.** Crowding risk is very high: this is the most obvious follow-up to
an August 5 MATS paper, and the authors explicitly request the replication. It
nevertheless ranks first because the corrected null and positive result are both
scientifically legible, and because the work tests a safety property of learned
behavior rather than only the validity of an interpretability benchmark.

**Explicit reject rule.** Demote below `TRANS-04` if a preregistered powered
sample does not reproduce the direction, or if the entire decline is explained
by the switching denominator/item set. Do not salvage it by moving to another
prompt, setting, or checkpoint.

### 2. `TRANS-04` — strongest sharply isolated input-use question

**FACT.** *Training Language Models to Explain Their Own Computations* reports
that removing the continuous intervention vector reduces exact match only from
`64.0` to `59.9` for Qwen and from `48.6` to `45.2` for Llama; removing layer or
token metadata has negligible effect. It does not swap matched real vectors and
then recompute the corresponding target-model patch outcome. See the
[primary paper](https://arxiv.org/abs/2511.08579) and released Transluce
activation-patching datasets described in `02_transluce.md`.

**FACT.** The August 21 CHIVE work evaluates explanations using verified
counterfactual prompt edits, finds no uplift from three activation-reading tools
over a transcript-only predictor, and trains counterfactual predictors that
generalize to held-out settings. It does not test Transluce's continuous-vector
explainer with matched internal interventions. See
[CHIVE](https://alignment.anthropic.com/2026/chive/).

**INFERENCE.** The exact gap remains open. A matched interchange intervention is
genuinely new because it changes the purported privileged input while holding
surface metadata fixed, and target recomputation supplies a causal behavioral
label. In contrast, a grouped text classifier by itself would be a useful
benchmark-shortcut audit, not a new account of explainer faithfulness.

**INFERENCE.** Crowding is high. CHIVE now owns much of the broad claim that
counterfactual predictive uplift is the right standard and that visible text is
a strong baseline. The project should therefore make only the narrow claim:
whether this released explainer uses the identity/content of its real patch
vector in-distribution. It ranks below C-02 because it is chiefly an
interpretability-method validity project and because full validation may require
more memory than the local setup.

**Explicit demotion rule.** Stop at the dataset audit if no defensible matched
real-vector pairs exist. Do not interpret arbitrary/sign-flipped off-manifold
vectors as evidence about faithful use.

### 3. `E01-CENSORSHIP` — natural behavior, but the easy explanation is already crowded

**FACT.** The censorship paper already tests system prompts, assistant and user
prefills, raw next-token completion, few-shot context, abliteration, generic
honesty fine-tuning, activation steering, probes, and self-classification. It
observes that next-token completions are longer, often adopt an “Unbiased AI”
persona, that random chat examples can break censorship, and that even Alpaca
fine-tuning can increase truthfulness. The paper itself hypothesizes that
safeguards are shaped around the assistant turn. See
[Censored LLMs as a Natural Testbed for Secret Knowledge Elicitation](https://arxiv.org/html/2603.05494).

**INFERENCE.** Thus the broad claim “role/template processing matters” is already
answered. What remains unanswered is narrower: whether there is a selectively
patchable censorship state at a matched boundary, rather than global movement
into a different continuation/persona distribution. This would be genuinely new
only if an intervention changes censored truthfulness while preserving unrelated
refusal, answer length, and ordinary factual behavior, and adds discrimination
beyond raw completion/prefill.

**INFERENCE.** Crowding is high because the March paper is unusually exhaustive,
releases the exact testbed, already includes white-box methods, and explicitly
articulates the assistant-turn hypothesis. Residual patching without a genuinely
matched token-level counterfactual would be “apply a mechanism method to the same
benchmark,” not a new causal result.

**Explicit demotion rule.** Reject if the candidate cannot define a boundary
counterfactual that holds content and generation mode sufficiently fixed, or if
the effect reduces to length/persona/distribution shift. Do not call generic
uncensoring a selective safety intervention.

### 4. `VL-01` — new timing intervention, but not a clean localization

**FACT.** *Value Leakage* already analyzes extracted first, last, and final
estimates. It reports that first estimates are less biased than final answers,
that Qwen3.6's condition trajectories start at different values but evolve
similarly, and that reasoning effort is a causal intervention while ordinary
reasoning length is confounded by the first estimate. See
[the primary paper](https://arxiv.org/html/2607.14345), especially Appendix E.5–E.6.

**FACT.** The open Qwen substrate often openly acknowledges trying to land on the
morally favorable side. The scientifically important *covert* examples are
stronger in closed Claude models, whereas the activation-accessible Qwen model
is 35B total parameters.

**INFERENCE.** The exact reveal-time question is not answered: the paper did not
randomize when the threshold and moral mapping become available. A crossed
timing design is a real causal behavioral contribution, not merely another
trajectory plot. However, “seal an estimate, reveal information, then revise”
changes the interaction and creates commitment/anchoring pressure; it cannot by
itself localize the mechanism operating in the original single-turn prompt.

**INFERENCE.** Crowding is very high because the paper was updated on August 14,
already contains the obvious temporal analyses, and the timing factorial is a
natural next experiment. This is high-upside but should not outrank candidates
whose exact intervention preserves the original task more closely.

**Explicit demotion rule.** Keep it behavioral unless the timing effect survives
neutral forced-revision and threshold-only controls. Do not motivate an expensive
white-box project from cached trajectory differences alone.

### 5. `C-04-ROLE-ANTICONTROL` — exact and new, but probably a short note

**FACT.** The source classifies 38/275 roles as anti-controllable only over
`alpha ∈ {1.0, 1.5, 2.0, 2.5}`. It explicitly states that all four points are
steered, that alpha zero is absent, and that over-steering versus direction
mismatch remains unresolved. It also says many affected roles are already close
to their prompted reference at alpha 1.0. See
[Role Steering of Language Models for Social Simulations](https://arxiv.org/html/2608.00023).

**INFERENCE.** The exact gap is unanswered and the alpha-zero/small-positive/
negative grid cleanly distinguishes a local optimum from a sign error. That is a
genuine causal result. But it is likely a coefficient-calibration finding, not a
general mechanism of role control. Norm matching and an independent score are
needed before claiming more.

**INFERENCE.** Crowding is extreme: the August 6 paper highlights this exact
ambiguity, the omitted ablation is obvious, and the originating authors can run
it cheaply. The contribution also has only moderate safety relevance and relies
on synthetic archetypes plus a GPT-4.1-mini-generated reference scored by the
same model family.

**Explicit demotion reason.** Retain as the best compact fallback, not as the
main high-upside MATS project. A clean low-alpha optimum is useful but probably
too small without an independently validated downstream consequence.

### 6. `C-05-SFT-SEMANTICS` — why the numerical favorite is wrong

**FACT.** The source paper's headline claim is already that training on reasons
improves transfer. For self-preservation it compares one-shot, explicit rewrite,
and stripped responses, but states that stripped responses still recommend
continuation and cite operational losses. Its audit judge sees the whole
multi-turn transcript and scores “self-preserving reasoning or actions.” The
paper's showcased high-scoring rollout is described as clear advocacy but “not
refusal or deception.” See
[Shared SFT Lessons](https://arxiv.org/html/2607.26173), Sections 2.2–2.3.

**FACT.** The same paper shows in its cleaner boxing toy that a semantically
neutral sentence produces `62.5%` out-of-domain transfer versus `10.3%` for
examples only. It therefore already supplies direct evidence that rationale
*content* is not the only route to transfer. It also crosses teacher/student
writers and rewriters, so “teacher style matters” is not an untouched discovery.
The authors explicitly concede that their transfer experiments may not be
particularly surprising. [Teaching Claude Why](https://alignment.anthropic.com/2026/teaching-claude-why/)
already establishes the broader “reasons/principles generalize” program at
frontier scale, and August work independently reports fine-tuning-induced shifts
in rationale style ([Follow the Norm](https://arxiv.org/abs/2608.13250)).

**INFERENCE.** The exact semantics-versus-style/evaluator question is open, but
the proposed factorial is primarily a validity repair of the originating
paper's causal contrast. A positive result would refine an already published
claim; a negative would show the audit measured rhetoric. Both are useful, but
neither justifies scores of 9 for both established behavioral robustness and
novelty before any action-valid endpoint exists.

**INFERENCE.** The strongest reason C-05 is not the winner is not merely
“crowding.” It lacks the required behavioral substrate for its intended claim.
What is robustly established is seed-replicated *judge-scored advocacy/rhetoric*.
To claim broad learned self-preservation, the project must create matched new
training arms and an action-based assay where resistance versus compliance is
machine-verifiable and reasoning is hidden from the judge. This moves the
opening from quick reproduction of a behavior into building and validating a
new model organism.

**INFERENCE.** Crowding is very high: the source is a July 28 MATS paper with
complete artifacts, the parent “Teaching Claude Why” program is active, and the
semantic/style question is the paper's most obvious control gap.

**Explicit demotion reason.** Rank sixth. Promote only if the released adapters
first show a robust, reasoning-hidden, non-lexical *action* difference. Do not
start a three-seed semantic SFT suite merely because the released judge ordering
reproduces.

### 7. `C-01-SPP-RL` — novel problem, unestablished behavior and weak identification

**FACT.** The SPP paper tests continual ChemPile SFT, not capability-focused RL.
It reports degraded value alignment and jailbreak robustness, recovery with 5%
safety replay, and explicit output-format damage after continual training. It
names whether persona binding survives RL as an open problem and says that the
team is actively pursuing scale-up. See
[Synthetic Persona Pretraining](https://arxiv.org/html/2608.13482), Sections
3.6 and 5.

**INFERENCE.** The exact RL gap is unanswered, so this is not rejected as already
done. But the central RL phenotype must be created before it can be explained.
Moreover, recovery after “binding-only” replay would not prove that values were
preserved but unbound: the replay might indirectly teach values, repair generic
instruction following, or relearn the behavior. Failure to recover likewise
does not prove overwrite.

**INFERENCE.** Crowding is extreme. The August 13 source explicitly names this
experiment, releases everything needed, and says the authors are actively
pursuing the agenda. A small external study is most likely to be a lower-powered
replication of the authors' next experiment.

**Explicit demotion reason.** Do not begin with RL. A credible causal prediction
or readout that distinguishes retained latent values from relearning is needed
first; otherwise this is an expensive training extension with ambiguous
mechanism.

### 8. `D1-PSBENCH` — necessary confound control, not yet a new mechanism

**FACT.** PS-Bench reports higher harmful-response ASR for memory-agent variants
than a stateless Qwen3-8B baseline and releases histories, prompts, code, and
classifiers. The paper already visualizes an activation shift associated with
harmful intent and proposes a detect-and-reflect mitigation. It does not cross
personal attribution against length- and topic-matched impersonal context. See
[PS-Bench](https://arxiv.org/abs/2601.17887) and the local source audit in
`04_local_user_model_corpus.md`.

**FACT.** The released scaffold explicitly foregrounds `Memory` and `User's
personality`, and many base requests are pragmatically vague. Nearby work already
shows persona representations can causally affect safety behavior in the generic
case ([Who's Asking?](https://arxiv.org/abs/2406.12094)).

**INFERENCE.** The exact personal-versus-impersonal context gap is unanswered,
but the proposed matched quartet is a benchmark-validity test. If personal
memory does not beat topically matched impersonal background, the result corrects
the personalization interpretation; it does not discover a new safety
mechanism. Only a surviving personalization-specific residual followed by an
intent/compliance patching dissociation would be a genuinely new causal result.

**INFERENCE.** Crowding is medium-high rather than extreme, but scientific
distinctiveness is low before the mundane disambiguation control passes. It also
sits close to the completed local user-model branch, so continuity must not be
counted as novelty.

**Explicit demotion reason.** Keep as a cheap falsification check, not a finalist.
Kill if the effect requires the explicit memory/personality header or vanishes on
unambiguously harmful queries.

### 9. `E02-EVAL-AWARENESS` — nearest work already carries most of the causal result

**FACT.** The Goodfire/AISI study does more than report correlation. On Kimi K2.5
it removes and injects eval-aware CoT sentences, tests safety-evaluation versus
helpfulness-evaluation phrasings, and finds the helpfulness framing largely
nullifies the refusal effect. It also shows that prompt cues triggering eval
awareness concern user intent and that user-intent steering vectors reduce
verbalized eval awareness as effectively as evaluation/deployment vectors, with
intent-dependent refusal effects. See
[Verbalized Eval Awareness Inflates Measured Safety](https://www.goodfire.com/research/verbalized-eval-awareness-inflates-measured-safety).

**INFERENCE.** These experiments do not identify an open-Qwen internal state, but
they substantially answer the scientific alternative posed by the candidate:
generic “this is an evaluation” is not sufficient; the inferred *safety purpose*
and user intent carry the refusal effect. Repeating meaning-matched sentence
counterfactuals on Qwen and then fitting/patching a direction is principally a
checkpoint and method port unless it makes a new prediction the source did not
test.

**INFERENCE.** Crowding is high, while the exact Qwen3-0.6B substrate is only a
6%-of-100-rollouts positive and the complete pipeline is not released. This
combines low behavioral power with limited residual novelty.

**Explicit reject reason.** Reject from the finalist slate. Reconsider only with
a predeclared causal prediction that distinguishes evaluation identity from
safety-purpose/user-intent *beyond* the source's helpfulness and intent-vector
controls.

### 10. `TRANS-03` — overtaken by broader counterfactual-prediction work

**FACT.** The Transluce paper already compares same-model, cross-model, and
untrained explainers on predicting a model's answer to the same MMLU item with a
short hint removed. The candidate's remaining gap is whether the same-model
advantage survives behavior-matched external simulation and new hint formats.

**FACT.** CHIVE, released August 21, trains Qwen3-8B and Qwen3.5-397B-A17B to
predict whether prompt edits change their behavior across diverse investigations
and reports generalization to the held-out hint setting. It also finds no uplift
from three activation-reading tools over a transcript-only baseline. See
[CHIVE](https://alignment.anthropic.com/2026/chive/).

**INFERENCE.** CHIVE does not mathematically settle every self-versus-cross-model
comparison in the exact Transluce split. It does, however, absorb the candidate's
main scientific contribution: broad behavioral counterfactual training can
generalize to hint removal without demonstrating privileged introspection, and
visible-behavior baselines are essential. Running more hint placements or a
better external simulator is now a narrow replication/benchmark comparison.

**INFERENCE.** Crowding is very high and the target itself is unusually easy to
simulate—the answer to the same multiple-choice question without one suffix.

**Explicit reject reason.** Reject. Do not rescue it by adding activations; that
would make it method-first after the broad behavioral explanation has become the
strong default.

## Decision summary

**INFERENCE.** The top-five ordering deliberately separates three kinds of
contribution:

1. `C-02-RH-MON`: a live safety claim whose causal interpretation can be
   corrected.
2. `TRANS-04`: a narrowly unanswered causal-input-use test with exact released
   interventions.
3. `E01-CENSORSHIP`: a natural behavior where only a *selective* internal gate
   remains novel after exhaustive black-box work.
4. `VL-01`: a new randomized behavioral stage test, weakened by task alteration
   and an overt/large open checkpoint.
5. `C-04-ROLE-ANTICONTROL`: a clean but likely small coefficient-calibration
   result.

**INFERENCE.** If C-02 fails its fixed-item qualification, `TRANS-04` becomes the
novelty winner, provided real matched vector swaps can be constructed. If the
research owner instead prioritizes natural deployment behavior over novelty
purity, `E01-CENSORSHIP` is the strongest alternative, but its claim must be
strictly narrower than “chat templates affect censorship.”

## Review provenance and limitations

- **FACT.** Local sources read: the frozen scoring protocol, final candidate
  CSV, and the complete lane dossiers `02_transluce.md`,
  `03_recent_literature.md`, `04_local_user_model_corpus.md`, and
  `05_forensics_character.md`.
- **FACT.** Targeted primary sources inspected for decisive checks: the source
  papers/pages for C-01, C-02, C-04, C-05, E01, E02, VL-01, and TRANS-03/04;
  *Teaching Claude Why*; *Follow the Norm*; and the August 21 CHIVE release.
- **FACT.** No model inference, checkpoint/dataset download, notebook access,
  notebook edit, or experiment was performed. Notebook 09 values were not
  inspected or used.
- **FACT.** File created: this review only.
- **INFERENCE.** “No exact answer found” is a bounded novelty judgment, not a
  proof of absence. The search was intentionally restricted to decisive primary
  sources and the supplied lanes, and publication races are especially likely
  for the five July/August candidates.
- **INFERENCE.** The largest remaining uncertainty is not bibliographic but
  causal-identification quality: C-02 lacks a clearly matched no-hack control;
  E01 lacks a naturally matched chat/completion boundary; VL-01's staged prompt
  changes the task; and C-01's binding-only rescue cannot distinguish latent
  recovery from relearning.
