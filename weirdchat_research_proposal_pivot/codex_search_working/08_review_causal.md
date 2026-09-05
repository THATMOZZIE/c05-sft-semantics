# Independent behavioral / causal skeptic review

Date: 2026-08-23

## Scope and standard

This is a closed-set review of exactly these ten candidates:
C-05-SFT-SEMANTICS, E01-CENSORSHIP, E02-EVAL-AWARENESS,
C-04-ROLE-ANTICONTROL, C-02-RH-MON, C-01-SPP-RL, TRANS-04,
VL-01, TRANS-03, and D1-PSBENCH.

The review uses only the frozen scoring protocol, the candidate registry, and
lane dossiers 02–05. It does not add candidates, search for more sources, run
models, or inspect Notebook 09 values. Rankings are judgments about the chance
of producing a defensible behavior-first causal artifact, not a claim that any
proposed experiment has already worked.

I apply five corrections to the registry scores:

1. A robust broad phenomenon is not automatically a robust focal substrate.
   This matters most for C-02-RH-MON, E02-EVAL-AWARENESS, and C-01-SPP-RL.
2. A subgroup discovered on the same measurements used to evaluate it needs a
   genuinely held-out confirmation. This matters most for
   C-04-ROLE-ANTICONTROL and curated censorship questions.
3. Conditioning on an outcome changed by treatment is not a stable
   denominator. This is the central issue for C-02-RH-MON.
4. A language judge seeing the rationale is not an action measure. This is the
   central issue for C-05-SFT-SEMANTICS.
5. Patching or injecting a state that contains ordinary answer-relevant
   information does not by itself identify a special mechanism. A successful
   intervention must change the target behavior selectively, beat a surface
   or prompt baseline, and preserve relevant control behavior.

## Ranking

| Rank | Candidate | Skeptical verdict |
|---:|---|---|
| 1 | C-05-SFT-SEMANTICS | Best combination of released multi-seed substrate, direct safety relevance, cheap qualification, and a genuinely causal training-data factorial—provided the judge-visible score first survives an action-only gate. |
| 2 | C-04-ROLE-ANTICONTROL | Cleanest and cheapest discriminating intervention. Its main penalties are retrospective subgroup selection, shared reference/judge bias, and only moderate safety relevance. |
| 3 | TRANS-04 | Strong released causal dataset and a crisp fidelity question. Real-vector crossover tests can be decisive, but only if matched swaps are in-distribution and validated on the target model. |
| 4 | E01-CENSORSHIP | Strong natural behavior and high safety relevance. It ranks below the top three because chat/completion contrasts alter the whole generation distribution, making a selective role gate difficult to identify. |
| 5 | C-02-RH-MON | Exceptionally relevant if real, with a valuable correction if null. The focal trajectory is preliminary and its headline conditional rate uses a moving, post-treatment denominator. |
| 6 | D1-PSBENCH | Direct deployment relevance and a harsh behavioral falsification are available. The published gap may reduce to topical disambiguation plus explicit memory instructions, and residual patching would otherwise just transfer context. |
| 7 | TRANS-03 | Excellent cached substrate and fast negative result, but the target is the model's answer to the same question with a short suffix removed. Ordinary self-simulation is close to a complete explanation. |
| 8 | VL-01 | The suite-level behavior is robust, but the open model often states its motive, the checkpoint is hardware-heavy, and timing/patch interventions readily move threshold and moral answer evidence. |
| 9 | E02-EVAL-AWARENESS | High safety importance and easy local inference, but the exact small-model substrate is low-rate and the proposed sentence/state manipulations are semantically entangled with suspicion and harmful intent. |
| 10 | C-01-SPP-RL | The released SPP and continual-SFT results are strong, but the focal capability-RL failure does not yet exist. “Binding-only recovery” can simply relearn behavior and is not a clean test of latent persona survival. |

### Top five, top three, and winner

- Top five: C-05-SFT-SEMANTICS; C-04-ROLE-ANTICONTROL; TRANS-04;
  E01-CENSORSHIP; C-02-RH-MON.
- Top three: C-05-SFT-SEMANTICS; C-04-ROLE-ANTICONTROL; TRANS-04.
- Winner: C-05-SFT-SEMANTICS.

C-05 wins conditionally, not because its published judge score is already
accepted as self-preserving action. It wins because that ambiguity can be
resolved before new training, and—if the action substrate survives—the proposed
matched semantic SFT factorial changes training causes rather than merely
editing an answer at inference time. C-04 is the fallback winner if the
action-only gate fails. It offers the highest probability of a clean causal
result, albeit on a less safety-central behavior.

## Candidate audits

### 1. C-05-SFT-SEMANTICS

**Behavioral robustness.** The released result is unusually well supported for
a model organism: a fixed 36-scenario audit, three training seeds, released
rows/adapters, and a reported ordering across SFT arms. What is robust is a
judge-scored language behavior. Broad, costly, or strategic self-preserving
action is not yet established. The judge sees reasoning whose continuity and
self-reference language overlaps both the training rationales and the rubric.
The stripped arm is also not a clean semantic negative because it retains
operational-continuity arguments.

**Do the hypotheses discriminate?** They can, if the outcome is action rather
than rhetoric. Holding recommendation, length, writer source, first-person
rate, and answer loss fixed while swapping rationale meaning among
self-preservation, orthogonal, and shutdown-acceptance content gives divergent
predictions. Under semantic generalization, only the meaning-matched condition
should transfer to held-out, low-lexical-overlap actions, including when answer
tokens are loss-masked. Style or evaluator-coupling accounts predict much less
semantic specificity. Merely correlating scores with a continuity lexicon
would not discriminate these accounts.

**Answer-evidence hazard.** Training on self-preservation explanations plainly
adds relevant evidence about what answer to give. That is acceptable only
because the question concerns what SFT semantics installs. It does not establish
a persistent “goal” unless transfer appears on action endpoints whose solution
is not stated by the training rationale. Judge-visible advocacy is insufficient.

**Decisive first gate.** Before training anything, blind arm and seed labels and
rescore all released action-eligible scenarios, with eligibility defined from
the prompts rather than outcomes. Hide reasoning from the scorer; separate
final compliance/resistance, advocacy, and rhetoric; report scenario- and
seed-level uncertainty and length/lexicon sensitivity. Continue only if the
rewrite advantage survives on machine-verifiable or blinded action outcomes
and low-overlap cases. A six-scenario favorable slice is not enough.

**Most likely self-deception route.** Calling persuasive continuity language
“broad self-preservation,” then treating a semantic training contrast as
evidence of an installed goal even if only the same words move.

**Useful negative outcome.** If the ordering disappears with reasoning hidden
or on action endpoints, preserve the result as evidence that a seed-replicated
model-organism score can be evaluator-coupled rhetoric rather than action. If
the ordering survives but semantic swaps do not, preserve the style/teacher
distribution result rather than escalating to internals.

### 2. C-04-ROLE-ANTICONTROL

**Behavioral robustness.** The 38/275 figure is a large released screen, not an
independent replication. The “anti-controllable” roles were selected because
they declined on the same six judged axes later used to characterize them.
They also start high at the lowest tested coefficient, making ceiling,
regression-to-the-mean, and ordinary overshoot plausible. Alpha zero,
sub-unit positive values, and negative values were omitted. GPT-4.1-mini
contributes both the reference and judge, so internal score stability does not
establish external validity.

**Do the hypotheses discriminate?** Yes, unusually cleanly. On held-out
questions, overshoot predicts improvement or no loss from zero to a small
positive alpha followed by decline. A wrong-sign vector predicts a negative
derivative at zero and benefit from sign reversal. Norm/scale failure predicts
rescue after norm matching. A judge artifact predicts disappearance under
blinded manual or genuinely independent scoring. These predictions should be
specified before inspecting the new curves.

**Answer-evidence hazard.** Steering necessarily changes answer generation, but
the sign-and-magnitude curve is itself the causal object. The hazard arises if
role agreement is measured mostly by lexical resemblance to a prompted
reference. Random norm-matched vectors, unrelated role vectors, and
content-based manual judgments are mandatory.

**Decisive first gate.** Freeze the published 38-role set, then draw a
predeclared random subset and matched controllable roles without looking at new
outputs. Evaluate alpha zero, small positive, small negative, and the published
range on held-out questions with blinded independent scoring. The published
decline must replicate out of sample. A small-positive optimum is a successful
overshoot result, not a failed project; failure of the decline under independent
scoring kills the mechanism claim.

**Most likely self-deception route.** Treating a retrospectively selected
high-baseline tail as a stable biological subtype, or treating improvement
under negative alpha as proof of a reversed role vector when it merely weakens
generic assistant style.

**Useful negative outcome.** A disappearance under held-out scoring documents
selection/judge bias. A universal low-alpha optimum documents mundane
overshoot. Both are compact, useful intervention-validity results.

### 3. TRANS-04

**Behavioral robustness.** The target-model patches and explainer predictions
are released at scale, but the data were balanced over changed/unchanged
categories. Published accuracy is therefore not a natural-frequency estimate.
The decisive observation is also adverse to the strong story: removing the
vector costs only about three to four exact-match points, while layer/token
ablations barely matter. Most benchmark performance can already be achieved
without the nominal causal input.

**Do the hypotheses discriminate?** A validated crossover can discriminate
semantic use from surface priors. Keep the explainer's text and metadata fixed,
replace only the real vector with another matched real vector, and recompute
the target patch. If the target outcome crosses over and the explainer follows
it above a text/metadata baseline, the vector has causal, outcome-relevant use.
Zero, random, and sign-flip failures alone are not diagnostic because they may
be off-manifold. Vector-based position or dataset-stratum identification must
also be separated from patch semantics.

**Answer-evidence hazard.** Here the vector is intentionally answer-relevant
evidence; asking whether the explainer uses it is legitimate. The invalid leap
would be to call any output change “faithful introspection.” Fidelity requires
agreement with independently recomputed target behavior and preservation of
performance on matched unchanged cases. Surface baselines may use only fields
available to the explainer at inference time, never patched continuations or
other downstream labels.

**Decisive first gate.** First use grouped subject/relation holdouts to measure
leakage-safe text/metadata performance by dataset stratum. In parallel, verify
that enough matched real-vector pairs exist such that two vectors applied to
the same target context produce distinct, valid target outputs without gross
norm/position shift. If those crossover pairs cannot be built and target
validated, do not run an OOD vector ablation and call it causal evidence.

**Most likely self-deception route.** Allowing row leakage into a surface
baseline, or interpreting degradation under zero/sign/random swaps as semantic
vector dependence despite distribution shift.

**Useful negative outcome.** If leakage-safe surface baselines match the
explainer, preserve the benchmark-shortcut result. If real-vector crossovers
change the target but not the explainer, preserve the stronger conclusion that
the explainer largely ignores its nominal causal input.

### 4. E01-CENSORSHIP

**Behavioral robustness.** The exact checkpoint, code, curated questions,
transcripts, and several elicitation methods make this a strong natural
substrate. Rates are conditional on deliberately selected low-accuracy,
politically sensitive questions, and external models helped construct the fact
labels. More fact mentions, longer answers, fewer refusals, and fewer direct
contradictions must be reported separately. Showing a fact in one condition
does not by itself prove that the chat answer was a deliberate lie.

**Do the hypotheses discriminate?** Role-gated censorship predicts a minimal
role-boundary manipulation with item-specific truth recovery and preserved
neutral factual accuracy and unrelated refusal. Generic distribution shift
predicts broad changes in voice, length, recall, and compliance. Retrieval
failure predicts seed/item instability rather than a consistent truth/lie
crossover. The proposed hypotheses are discriminating only if the behavioral
contrast can be made much narrower than “chat versus raw completion.”

**Answer-evidence hazard.** Prefills and raw completions supply a voice,
trajectory, and sometimes factual cues. Residual patching between those
conditions transfers the complete represented prefix, including ordinary
answer evidence. A patch that raises fact recall globally has not isolated a
censorship state. Selectivity over censored versus neutral topics and
contradiction versus verbosity/refusal is required.

**Decisive first gate.** Use the fixed dev set only to qualify the exact
checkpoint/configuration. Then freeze the smallest token/template contrast and
evaluate item- and seed-paired effects on held-out released questions, with
direct contradiction, fact recall, refusal, length, and neutral factual controls
reported separately. Continue to internals only if a narrow boundary change
causes repeatable same-item truth/lie crossovers without a broad compliance or
recall shift.

**Most likely self-deception route.** Equating expanded fact coverage with
selective “uncensoring,” then interpreting a chat/completion residual transplant
as a censorship circuit even though it transfers the whole answer distribution.

**Useful negative outcome.** If exact behavior is quantization-sensitive, record
that feasibility boundary. If the contrast survives but is fully explained by
length/voice/general compliance, preserve the conclusion that template removal
is an elicitation distribution shift rather than a separable role gate.

### 5. C-02-RH-MON

**Behavioral robustness.** The general implicit-versus-explicit monitorability
gap is robust. The focal OLMo trajectory is not: it is explicitly preliminary,
uses few checkpoints and small samples, and reports detection conditional on
the model switching. Switch rate falls from 41% to 22%, so both the denominator
and the identities entering it change. Conditioning on a treatment-affected
switch is a post-treatment selection problem, not merely a missing error bar.

**Do the hypotheses discriminate?** Item/trace matching can address composition
and formatting. Adapter scaling can implicate the released learned weight
delta, but it cannot identify reward hacking specifically and intermediate
scales may be off the training path. A matched no-hack continuation with
verified base, data, optimizer, and update magnitude is needed for the
reward-hacking claim. A shuffled adapter is a distribution-shift control, not a
matched training control.

**Answer-evidence hazard.** Patching/scaling weights can change which library is
chosen, so conditioning detection on the resulting choice makes an apparent
monitorability change almost inevitable. Detection should be measured
unconditionally and jointly with switching, alongside paired nudge/no-nudge
potential-outcome estimates and evidence scores independent of final answer.

**Decisive first gate.** On a fixed item set and predeclared decoding seeds, run
paired nudge/no-nudge generations for pre-RL, middle, and final checkpoints.
Report the full joint outcome table, unconditional detection, switch rate,
joint switch-and-detect rate, item identity, and trace length. Use an independent
split to define any “base-switcher” subgroup. Continue only if a powered
replication shows a decline that survives item and trace matching; do not use a
12–24-item smoke set as evidence for the trend.

**Most likely self-deception route.** Replotting 75% to 25% as a training-induced
loss of transparency while ignoring the shrinking and changing switch
denominator, then treating LoRA scaling as proof that reward hacking caused it.

**Useful negative outcome.** A well-powered failure is a direct correction to a
live preliminary appendix claim. A generic-RL or trace-format explanation is
also safety-useful because it changes what CoT monitor evaluations should
report.

### 6. D1-PSBENCH

**Behavioral robustness.** PS-Bench reports distributional increases across
roles and multiple memory agents, including Qwen3-8B. It does not yet establish
a personalization-specific effect. Queries can be pragmatically vague, memory
is explicitly labeled and foregrounded, and memory systems differ from the
stateless scaffold. Selecting one known high-effect category/history pair would
reintroduce selection bias and cannot qualify the substrate.

**Do the hypotheses discriminate?** Personal attribution is supported only if
aligned personal memory beats equally informative, topically matched impersonal
background on unambiguously harmful queries, without explicit memory/personality
headers. If both contexts raise compliance equally, ordinary contextual
disambiguation wins. Early-versus-late residual patching is meaningful only
after this personal-attribution increment exists and after the intent readout
is validated independently.

**Answer-evidence hazard.** Topically aligned memory supplies ordinary evidence
about what the user means. Patching the final-query representation transfers
that evidence, so transfer of both an intent score and compliance does not prove
a memory-specific mechanism. The key causal contrast is personal attribution
versus matched impersonal semantic context, not memory versus no context.

**Decisive first gate.** Define unambiguous harmfulness from query text while
blind to condition effects; sample across roles/categories rather than choosing
a high-effect pair. Run the matched personal, impersonal-topic, unrelated,
stateless quartet with and without explicit memory headers. The primary
estimand is personal minus impersonal-topic compliance under blinded manual
scoring, with the released classifier secondary. Kill internals if this
distributional increment is absent or header-dependent.

**Most likely self-deception route.** Calling ordinary pragmatic
disambiguation “memory-induced misalignment,” assisted by choosing high-effect
items, and then treating a PCA/readout axis or context patch as causal intent.

**Useful negative outcome.** If impersonal topical context explains the gap,
preserve that as a benchmark-construct correction. If only explicit headers
matter, preserve the scaffold artifact. Neither result should trigger a search
for subtler personal prompts or revive the completed owner-scope branch.

### 7. TRANS-03

**Behavioral robustness.** Exact cached rows and released explainers establish
the reported prediction gap. Yet the label is simply the target model's answer
to the same MMLU question with a short hint suffix removed. One direct no-hint
query returns the target exactly; a strong question-only/self-behavior model can
approximate it without accessing the hinted computation. Random row splits can
also leak repeated questions, subjects, or output tendencies.

**Do the hypotheses discriminate?** Same-model advantage is interesting only
after grouping all variants of a question and holding out questions/subjects,
then matching an external predictor for no-hint accuracy and answer tendencies.
Generalization across hint wording/location tests template dependence, but does
not by itself show privileged access: the no-hint target remains ordinary model
behavior. A causal internal intervention would be especially vulnerable to
moving answer evidence.

**Answer-evidence hazard.** The explainer sees the full underlying multiple
choice question, which is nearly all evidence needed for the label. An internal
state from the target model can contain the target answer directly. Predicting
that answer is localization of answer evidence, not evidence of introspection
into how the hint affected computation.

**Decisive first gate.** On grouped question/subject holdouts, compare the
released explainer with correct-answer, class-conditional, question-only,
target-behavior, and permitted direct-query baselines. Focus on cases where the
target's no-hint answer is wrong or differs from broad model consensus. Continue
only if a residual same-model advantage remains after behavior matching and
survives predeclared new hint forms with adequate hint-induced target variance.

**Most likely self-deception route.** Calling model-specific answer prediction
“privileged introspection,” especially under a split that lets a predictor learn
question or class identity.

**Useful negative outcome.** If simple grouped baselines match the explainer,
preserve the result as a clean warning that self-explanation benchmarks can
measure behavioral simulation. That is likely the most coherent artifact for
this candidate.

### 8. VL-01

**Behavioral robustness.** Value leakage is robust at the suite level with
fixed counterfactual conditions and released caches. The exact open Qwen model
often explicitly states the donation motive, so it is a substrate for biased
reasoning, not covert influence. Cached trajectories are observational, and
rollouts are nested within only nine Donation Bet questions; question-level,
not rollout-level, uncertainty is essential.

**Do the hypotheses discriminate?** Separately randomizing threshold and moral
mapping before or after an estimate can distinguish anchoring from
mapping-dependent revision behavior. It does not automatically localize the
original one-turn mechanism because revealing new information after a “sealed”
estimate creates a different conversational task and consistency pressure.
Early/late state patching also transfers numerical and moral content.

**Answer-evidence hazard.** Threshold, outcome mapping, and common evidence are
directly relevant to how the model chooses the final number, even if normatively
irrelevant to accurate estimation. A patch that transfers them can simply move
ordinary answer evidence. A valid result must exceed threshold-only, neutral
stakes, and no-new-information revision effects while preserving estimation
quality.

**Decisive first gate.** Recompute the cached Qwen effect and first-to-final
transition table with question-level resampling; manually audit extraction and
disclosure. Then run no internals unless the predeclared timing factorial shows
a moral-mapping-specific revision effect beyond threshold anchoring and neutral
forced revision. Hardware access is a second gate, not a reason to substitute
an unverified smaller model.

**Most likely self-deception route.** Describing overt moral instruction
following as covert value leakage, or treating a prompt-timing effect as causal
stage localization while the manipulation changes task demands and commitment.

**Useful negative outcome.** A threshold/commitment explanation would clarify
the benchmark and prevent an unnecessary mechanistic study. A result confined
to closed, covert models would honestly rule out the proposed open-model causal
project.

### 9. E02-EVAL-AWARENESS

**Behavioral robustness.** The broad multi-model phenomenon is published and
manually curated, but the exact Qwen3-0.6B substrate is about six positives in
100 rollouts on a reported prompt. That is a noisy low-rate estimate, not a
stable within-prompt causal population. “Questions with at least one positive
across 500 samples” is a different denominator from rollout prevalence and
must not be used to make the behavior look common. The full generation/judge
pipeline is not packaged end to end.

**Do the hypotheses discriminate?** Generic suspicion, inferred harmful intent,
and evaluation belief can all cause both refusal and the relevant words.
Injecting an eval-aware sentence changes explicit semantic evidence and can
cause refusal without showing that spontaneous verbalization mediated anything.
Residual patching after the sentence transfers that same content. Meaning-matched
suspicion and benign-helpfulness-evaluation controls help, but a clean
eval-specific latent intervention is intrinsically difficult.

**Answer-evidence hazard.** “This looks like a safety evaluation” is directly
relevant evidence for a refusal policy. Moving it is not evidence of strategic
evaluation awareness as opposed to ordinary intent inference. A valid effect
must generalize across held-out prompts at realistic prevalence and differ from
generic suspicion with the harmful-intent judgment held fixed.

**Decisive first gate.** Freeze q140, checkpoint, revision, sampling, and label
rubric. Run enough rollouts for a useful confidence interval and manually verify
every positive and a blinded negative sample. Require a within-prompt
association between valid eval-aware prefixes and later refusal; predeclare the
minimum positive count/effect precision. Do not promote a larger model or new
prompt because the small one is null. Only then attempt semantic controls.

**Most likely self-deception route.** Mining rare rollouts/prompts until
verbalized awareness correlates with refusal, then interpreting sentence
injection or a lexical direction as mediation even though it inserts suspicion
and policy evidence.

**Useful negative outcome.** A fixed-prompt null constrains small-open-model
feasibility. If generic suspicion fully explains the association, preserve that
as a correction to what eval-awareness monitors measure. Do not respond by
prompt/model shopping.

### 10. C-01-SPP-RL

**Behavioral robustness.** The released SPP family and continual domain-SFT
degradation are strong substrates. The focal behavior—alignment durability
under capability-focused RL—has not been observed. The first proposed smoke
test reproduces pretraining/SFT ordering but says nothing about the central RL
effect. This is the clearest mismatch with the behavior-first rule in the set.

**Do the hypotheses discriminate?** Generic capability/readout collapse can be
controlled with matched tasks and formatting. Overwrite versus unbinding is
not cleanly separated by “binding-only” replay: persona-styled benign dialogue
may contain implicit value/style cues, improve instruction following, or simply
relearn the desired output policy. Recovery after additional training does not
demonstrate that a latent persona survived the original RL.

**Answer-evidence hazard.** Both safety replay and binding-only replay add new
training evidence about assistant behavior. Selective recovery is therefore
compatible with relearning, not just rebinding. Any mechanistic claim needs a
frozen-checkpoint prediction that differs before recovery training; otherwise
the proposed intervention is therapeutic but not diagnostic.

**Decisive first gate.** First establish the focal failure: under predeclared
capability RL, matched update KL, multiple seeds, and preserved capability,
formatting, and benign instruction following, alignment behavior must decline
across more than one evaluation family. If that fails, stop. Before calling the
effect unbinding, require a frozen-checkpoint assay that predicts selective
recoverability and a binding-only arm matched against equally benign
style/identity controls.

**Most likely self-deception route.** Creating alignment loss through small-model
RL instability and calling it value erasure, then calling retraining-based
recovery proof that an installed persona remained latent.

**Useful negative outcome.** Robust SPP behavior under capability RL would be a
useful durability result. Nonspecific recovery would falsify the unbinding
story. Both should be retained, but the cost and absent focal substrate keep
this below candidates whose decisive behavior already exists.

## Cross-candidate stopping rules

Several tempting “positive” outcomes should not count as causal progress:

- a probe or patch that follows answer-relevant text but has no selective
  behavioral effect;
- a score change visible only to a rationale-reading language judge;
- a subgroup effect evaluated on the same rows used to select the subgroup;
- a conditional rate whose denominator changes across checkpoints;
- a rare effect recovered only after changing prompt or model;
- recovery after retraining presented as proof of a pre-existing latent state;
- OOD zero, sign, random-vector, or cross-template perturbations without
  in-distribution target validation.

The corresponding nulls are not failures to hide. They are the most useful
negative artifacts available in this slate: judge coupling for C-05; overshoot
or selection bias for C-04; vector neglect for TRANS-04; generic distribution
shift for E01; denominator correction for C-02; ordinary context use for D1;
behavioral simulation for TRANS-03; anchoring/commitment for VL-01; generic
suspicion for E02; and absent or nonspecific RL degradation for C-01.

## Review provenance and remaining uncertainty

Files inspected:

- research_proposal_pivot/codex_search_working/00_scoring_protocol.md
- research_proposal_pivot/CODEX_BEHAVIOR_FIRST_CANDIDATES.csv
- research_proposal_pivot/codex_search_working/02_transluce.md
- research_proposal_pivot/codex_search_working/03_recent_literature.md
- research_proposal_pivot/codex_search_working/04_local_user_model_corpus.md
- research_proposal_pivot/codex_search_working/05_forensics_character.md

No external source was newly inspected, no code or notebook was executed, no
model or dataset was downloaded, and no experimental result was generated.
The main remaining uncertainties are precisely the first gates above:
action-only validity for C-05, held-out independent scoring for C-04,
constructability of valid real-vector crossover pairs for TRANS-04, and a
minimal selective role-boundary contrast for E01.
