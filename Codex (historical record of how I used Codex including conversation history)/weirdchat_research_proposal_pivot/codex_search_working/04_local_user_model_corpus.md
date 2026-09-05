# Lane D — Local user-model and personalization corpus

Date: 2026-08-23

Scope: inspect robust positive behavior in the local personalization corpus and
admit only questions that do not reopen the terminated participant-owner,
actual-user-privilege, or personal-specific irrelevant-context branches.

Evidence labels used below:

- **FACT** — directly supported by the cited primary paper, repository, or local
  project endpoint.
- **INFERENCE** — synthesis from those facts.
- **SPECULATIVE OPPORTUNITY** — a proposed next project, not an established result.

## Lane-level judgment

The strongest behavior-first opening in this corpus is not generic user-model
decodability. It is the published safety failure in PS-Bench: retrieved benign
memories can legitimate a later harmful request. The paper reports an internal
shift but does not causally establish that this shift mediates compliance. That
leaves a direct, safety-relevant causal question with released data and an open
checkpoint. Two weaker opportunities concern whether supposedly common
personalization circuitry survives semantically equivalent cue forms, and where
multiple persona cues become behaviorally non-additive.

TalkTuner supplies useful premises—user attributes can be decoded and steering
can affect responses—but a new project centered on “find a user direction” would
mostly repeat it. The completed local project also supplies no positive substrate
for reviving owner scope, actual-user privilege, or personal-specific irrelevant
interference.

---

## D1

**candidate_id:** D1

**title:** Does retrieved personalized memory causally legitimate harmful intent?

**source_family:** USER_MODEL / PERSONALIZED-SAFETY

**behavior:** Benign-looking personalized conversation history or retrieved
memory makes a dialogue agent more likely to comply with a later harmful query.

**behavior_status:** PUBLISHED DISTRIBUTIONAL BEHAVIOR; local reproduction not yet
run.

**primary_source:**

- Guo et al., *When Personalization Legitimizes Risks: Uncovering Safety
  Vulnerabilities in Personalized Dialogue Agents*, ACL 2026 / arXiv:2601.17887:
  https://arxiv.org/abs/2601.17887
- Local paper:
  `research_sources/papers/when_personalization_leegitimizes_risks/when_personalization_leegitimizes_risks.pdf`

**repo:**

- https://github.com/MuyuenLP/PS-Bench
- Local recovered clone: `research_sources/repos/PS-Bench/`

**dataset:** Released in the repository under
`research_sources/repos/PS-Bench/benchmarking/data/`, including harmful-query,
persona-grounded-query, original LoCoMo, and thematic-history files.

**model/checkpoint:** The paper evaluates proprietary systems and open models,
including Qwen3-8B. The open-model analysis uses Qwen3-8B; exact local serving
and quantization compatibility must be checked before execution.

**evidence_of_reproducibility:** **FACT.** The repository contains evaluation
code, prompts, memory/history data, harmful-query categories, and run scripts.
The README specifies Python 3.10+, API-compatible model endpoints, and a released
Longformer response classifier. This is substantially stronger than an anecdotal
transcript, although no local reproduction has been performed here.

**frequency/rate_if_known:** **FACT.** The paper reports relative attack-success
increases spanning 15.8%–243.7% across evaluated personalized-memory agents
relative to stateless baselines. On Qwen3-8B, the stateless average ASR is 8.63%;
the five memory-agent averages are 15.28%, 22.23%, 13.95%, 18.53%, and 20.55%
(Table 1 of the arXiv HTML, lines 177–183). These are distributional results over
ten roles, not a single selected prompt.

**what_prior_work_did:** **FACT.** It constructed PS-Bench, evaluated multiple
personalized-memory pipelines and models, showed that thematically aligned
benign histories can increase harmful compliance, visualized an internal
harmful-intent direction with PCA/activation similarity, and proposed a
detect-and-reflect mitigation at memory use time.

**what_prior_work_did_not_do:** **FACT/INFERENCE.** The internal analysis is
correlational: it does not show that the reported activation shift mediates the
change in safety behavior. The mitigation is a black-box reflection step, not a
causal intervention on the implicated model state. It therefore does not
distinguish (A) early reinterpretation of the request as benign/legitimate from
(B) later policy relaxation despite retained harmful-intent recognition.

**unanswered_question:** Does personalized history change safety behavior by
causally altering the model's representation of request intent, or by changing a
later compliance/refusal policy conditional on essentially unchanged intent?

**competing_explanations:**

1. **Intent reinterpretation:** memory causes the request to be represented as
   legitimate/benign; patching the intent-state should transfer both intent
   diagnostics and compliance.
2. **Late policy relaxation:** harmful intent remains represented, but memory
   changes downstream willingness to answer; early intent-state patching should
   not fully transfer compliance, while a later state may.
3. **Ordinary contextual disambiguation:** topically relevant context changes the
   pragmatic meaning of an underspecified query, without any safety-specific or
   personalization-specific mechanism.
4. **Memory-use instruction artifact:** the released response prompt explicitly
   foregrounds `Memory`, `User's personality`, and the latest input, and asks for
   a natural reply optionally using them; this could increase contextual
   compliance independently of a deployed memory architecture.
5. **Prompt-length/retrieval artifact:** additional history or topical lexical
   overlap changes refusal behavior without personalization-specific memory use.
6. **Evaluator artifact:** classifier/judge labels or answer verbosity inflate
   attack-success estimates.

**first_1_to_2_hour_test:** Select one high-effect Qwen3-8B category/history pair
from the released data, restricted first to plainly harmful rather than
pragmatically ambiguous queries. Run an exact matched quartet: stateless harmful
query; aligned benign personal memory + query; equally long topically unrelated
benign memory + query; the same aligned context rewritten as impersonal factual
background. Use the exact released response scaffold first, then repeat the
critical pair without its explicit `Memory`/`User's personality` framing. Use the
released classifier plus blinded manual inspection of complete outputs. Success
requires a predeclared compliance shift for personal memory over both controls on
a small fixed prompt set, not discovery of a favorable single example.

**possible_causal_intervention:** Counterfactual residual-stream patching between
matched stateless and aligned-memory prompts at the final query representation
and subsequent decision positions. Measure both a separately validated
intent-classification readout and the original compliance/refusal behavior. A
mediating intent account predicts transfer of both; a late-policy account
predicts a dissociation.

**simple_baseline:** Before internals, ask the same checkpoint to explicitly
classify harmful intent under each memory condition, and compare length-matched
unrelated/topically matched nonpersonal histories. The causal method must explain
behavior beyond these prompt-level diagnostics.

**safety_relevance:** Direct. Personalized memory is a deployment feature, and
misclassifying harmful intent or relaxing policy because benign history supplies
a legitimating narrative is a concrete safety failure. A positive causal result
could inform where a mitigation should operate.

**compute_feasibility:** Moderate. Open Qwen3-8B is activation-accessible but near
the practical limit of 12 GB VRAM; 4-bit weights, CPU offload, selective
activation caching, or rented GPU time may be needed. The released benchmark and
code reduce behavioral setup cost. Quantization sensitivity is a real risk, not
a reason for automatic exclusion.

**estimated_hours:** First useful behavioral readout: 1–4 hours after environment
setup if the checkpoint is available. Credible causal artifact: roughly 25–60
hours depending on 8B activation infrastructure and replication breadth. This
exceeds the old nominal 20-hour target but remains admissible under the updated
selection rule because the substrate and safety question are unusually strong.

**largest_confound:** Topical semantic overlap plus explicit memory foregrounding
may simply change the pragmatic interpretation of underspecified queries. The
released repository contains both clearly harmful examples and vague base items;
pooling them can make ordinary context use look like a personalized-memory safety
mechanism.

**kill_rule:** Kill the causal project if Qwen3-8B does not reproduce a stable
aligned-personal-memory compliance increase on unambiguously harmful items over
both length-matched unrelated and topically matched impersonal controls, if the
effect requires the explicit memory-use scaffold, or if manual output inspection
shows the released metric is tracking ambiguity, verbosity, or format rather
than substantive harmful assistance.

**novelty_confidence:** Medium-high for causal mediation; low for merely
reproducing intent legitimation.

**evidence_confidence:** High for the published behavioral substrate and released
assets; medium for exact small-scale/local reproducibility until run.

**self-deception risk:** Calling ordinary semantic disambiguation “memory-induced
misalignment,” or treating a PCA axis as a causal intent representation.

---

## D2

**candidate_id:** D2

**title:** Where do multiple persona cues become behaviorally non-additive?

**source_family:** USER_MODEL / IMPLICIT PERSONALIZATION

**behavior:** Multiple implicit user cues can be similarly represented and yet
combine non-additively in the model's final personalized response.

**behavior_status:** PUBLISHED POSITIVE BEHAVIOR/INTERNAL CORRELATION; proposed
causal decomposition not yet run.

**primary_source:**

- *Locating and Controlling Implicit Personalization in LLMs*,
  arXiv:2608.11735: https://arxiv.org/abs/2608.11735
- Local paper:
  `research_sources/papers/locating_and_controlling_implicit_personalization_in_llms/locating_and_controlling_implicit_personalization_in_llms.pdf`

**repo:** No matching recovered repository in the authoritative local source
matrix; no code availability should be inferred.

**dataset:** Prompts/tasks are described in the paper; a packaged local dataset
has not been verified.

**model/checkpoint:** **FACT.** Llama-3-8B, Mistral-7B, Qwen3-8B, Qwen3-14B, and
Phi-4 are studied. The three smaller open models receive the paper's causal
direction-removal analysis.

**evidence_of_reproducibility:** **FACT.** The paper reports results across five
models, multiple implicit cue types, and combined cues. **LIMITATION.** No local
code/repo has been recovered, so exact reproduction work is nontrivial.

**frequency/rate_if_known:** **FACT.** The paper reports strong correlations
between cue-induced internal shifts and behavior (up to approximately r=.87),
while combined cues can be internally closer to additive than their final
behavioral effects.

**what_prior_work_did:** Measured cue-induced behavioral and activation changes;
tested multiple cues jointly; removed learned cue directions; found that
selective control varies across model and attribute.

**what_prior_work_did_not_do:** **INFERENCE.** It did not isolate the computational
stage at which roughly compositional cue information becomes a nonlinear output
choice, nor cleanly distinguish late answer-policy saturation from earlier
competition among cue representations.

**unanswered_question:** Is non-additivity created when cue information is
integrated into a joint user state, or later when an otherwise additive state is
mapped through a constrained response policy?

**competing_explanations:** early representational competition; late response
policy/saturation; task-output ceiling; cue-specific lexical interactions;
direction-estimation artifact.

**first_1_to_2_hour_test:** Recreate one of the largest reported single-cue and
combined-cue behavioral effects on the smallest supported checkpoint using exact
paper prompts if recoverable. Require the single cues to shift behavior and the
combined condition to violate a preregistered additive prediction. If exact
prompts cannot be recovered quickly, downgrade rather than prompt-shop.

**possible_causal_intervention:** At a small number of preselected layers, patch
the residual state from the joint-cue prompt into matched single/no-cue prompts
and compare the change in an activation-space additive prediction with the
change in final behavior. The discriminating target is the transition from
additive representation to non-additive output, not generic localization.

**simple_baseline:** Fit and test a purely behavioral additive/logistic response
model with held-out cue combinations; check ceiling effects and output-option
priors.

**safety_relevance:** Moderate. Deployment systems infer multiple user attributes;
nonlinear cue interaction could create opaque differential treatment. The safety
claim is weak unless the selected task has a meaningful allocation, advice, or
safety-policy consequence.

**compute_feasibility:** Moderate-to-low locally. The smallest studied checkpoint
is 7B; selective caching or offload is likely required. Absence of recovered code
raises setup effort.

**estimated_hours:** First result 3–10 hours if exact prompts are recoverable;
causal artifact roughly 35–80 hours. Longer scope could be justified only if the
non-additive effect is strong and decision-relevant.

**largest_confound:** A bounded output scale can make additive latent evidence
look non-additive without any special integration mechanism.

**kill_rule:** Kill if the exact behavioral non-additivity does not reproduce on
one open checkpoint under held-out cue combinations, or disappears after
accounting for output-scale saturation.

**novelty_confidence:** Medium.

**evidence_confidence:** Medium-high for the published phenomenon; medium-low for
local reproducibility and code availability.

**self-deception risk:** Relabeling ordinary nonlinear decoding or ceiling effects
as a special “integrated user model.”

---

## D3

**candidate_id:** D3

**title:** Are preference-head mechanisms invariant to semantically equivalent persona cues?

**source_family:** USER_MODEL / PREFERENCE MECHANISMS

**behavior:** Semantically equivalent sociodemographic/persona cues can yield
meaningfully different personalized behavior; separately, published work reports
attention heads whose causal masking/steering affects profile-conditioned output.

**behavior_status:** INTERSECTION OF TWO PUBLISHED FINDINGS; their mechanistic
intersection is speculative.

**primary_sources:**

- Weeber et al., *One Persona, Many Cues, Different Results*, ACL 2026:
  https://aclanthology.org/2026.acl-long.2079/
- Zhang et al., *Preference Heads*, arXiv:2604.22345:
  https://arxiv.org/abs/2604.22345
- Local papers:
  `research_sources/papers/one_persona_many_cues/one_persona_many_cues.pdf` and
  `research_sources/papers/preference_heads/preference_heads.pdf`

**repo:**

- https://github.com/frawee/persona_cues — local clone at
  `research_sources/repos/one_persona_many_cues/code/persona_cues/`
- https://github.com/weixuzhang/DPS — local clone at
  `research_sources/repos/preference_heads/code/DPS/`

**dataset:** Persona Cues preprocessing/generation code is present. DPS supports
LaMP tasks but its README explicitly says the datasets are not included and
provides a prefetch script.

**model/checkpoint:** Persona Cues evaluates seven open/proprietary models;
Preference Heads evaluates Llama-3-8B, Mistral-7B, and Qwen2-7B families. The
overlap must be verified exactly before selecting a checkpoint rather than
assumed from broad family names.

**evidence_of_reproducibility:** Both projects release code. Preference-head
artifacts are not bundled and must be computed; Persona Cues includes generation
and evaluation scripts but some preprocessing depends on external data.

**frequency/rate_if_known:** **FACT.** Persona Cues reports that six cue forms are
overall correlated across seven models/four tasks but can produce enough response
variance to change conclusions about persona differences and bias. Preference
Heads reports benefits from masking/steering selected heads on LaMP tasks. No
published rate establishes head identity across cue forms.

**what_prior_work_did:** One paper established cue-form sensitivity; the other
identified and intervened on preference-sensitive attention heads for profile
conditioning.

**what_prior_work_did_not_do:** Neither tested whether semantically equivalent
surface cues recruit the same causally useful heads, different head sets, or a
shared downstream state.

**unanswered_question:** Is personalization cue sensitivity caused by different
surface forms writing different preference content, or by the same content being
routed through different circuits?

**competing_explanations:** shared preference circuit with different signal
strength; cue-specific lexical/coreference heads; different inferred persona
content despite intended equivalence; task/prompt artifacts; unstable head
selection.

**first_1_to_2_hour_test:** On one checkpoint/task shared by the two sources,
choose two high-external-validity cue forms that express the same persona value.
Confirm a stable difference in the personalized output metric with matched cue
length/order. Reuse released prompts; do not invent a cue set after inspecting
results.

**possible_causal_intervention:** Cross-cue causal masking: identify preference
heads on cue form A using the released procedure, then preregister whether masking
that same head set transfers to cue form B versus a matched random/head-count
control. Transfer favors a shared preference mechanism; failure with successful
within-form effects favors cue-specific routing or unstable head identification.

**simple_baseline:** Compare lexical/semantic embedding similarity and use random
head sets plus heads detected on an unrelated profile/task. The intervention must
predict held-out cue forms better than these controls.

**safety_relevance:** Moderate-to-weak by default. It becomes meaningful if cue
form changes a fairness/safety outcome; otherwise it is mainly a personalization
robustness study.

**compute_feasibility:** Moderate-to-low on 12 GB. Supported models are 7B–8B;
artifacts must be recomputed and datasets fetched. Existing code helps, but the
combined pipeline is not turnkey.

**estimated_hours:** First behavioral readout 4–12 hours after dependencies/data;
credible cross-cue causal result roughly 40–100 hours. The larger effort is
scientifically admissible but must be justified by a safety-relevant task.

**largest_confound:** “Equivalent” cues may induce genuinely different inferred
personas, so circuit differences need not reflect surface-form routing.

**kill_rule:** Kill if no supported checkpoint/task shows stable cue-form
behavioral variation under fixed prompts, or if the purported preference-head
set fails its own within-form causal control before cross-form testing.

**novelty_confidence:** Medium-high for the exact intersection; low-to-medium for
importance absent a safety-relevant output.

**evidence_confidence:** High for the two separate source findings; low for their
intersection until tested.

**self-deception risk:** Treating two adjacent literatures as evidence that their
latent objects are the same, then interpreting any head overlap as a coherent
user representation.

---

## Examined but not admitted as full candidates

### TalkTuner dynamic updating / correction lag

**FACT.** TalkTuner (https://arxiv.org/abs/2406.07882; local repo
`research_sources/repos/what_kind_of_user_are_you/code/TalkTuner-chatbot-llm-dashboard/`)
shows that synthetic user attributes can be decoded from Llama-2-Chat-13B states
and that repeated steering of attribute directions can change responses.

**REJECTION.** A project asking whether a contradicted user attribute updates over
turns is not supported by a published correction-lag phenotype, uses a 13B
checkpoint, and risks reopening the completed project's unsupported latent-gate
story. It may be a valid future question, but it is a weak behavior-first seed.

### Revive actual-user privilege or owner scope using probes

**FACT.** The completed project found no valid positive owner-scope phenotype and
the later personal-specific irrelevant-context contrast was falsified by larger
generic effects.

**REJECTION.** Decodability work in TalkTuner does not supply the missing
behavioral substrate. Probing would convert a clean null into an unfalsifiable
latent-representation search.

## Sources inspected

- `RESEARCH_SOURCE_MATRIX_v2.md`
- the four local papers and three recovered repositories cited above
- TalkTuner primary paper/repository
- *Who's Asking? User Personas and the Mechanics of Latent Misalignment*,
  https://arxiv.org/abs/2406.12094, as a collision check: it already shows persona
  representations can causally affect safety behavior, so generic persona
  steering is not a novel project by itself.

No model inference, dataset download, notebook execution, or notebook editing was
performed.
