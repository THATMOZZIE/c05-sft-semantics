# Orchestrator primary-source verification

Date: 2026-08-23

Scope: finalist-only verification after candidate discovery stopped. No model
inference, checkpoint downloads, notebook execution, or inspection of blinded
Notebook 09 downstream values was performed. `FACT` denotes a claim checked
against a primary paper, official repository, dataset card, or model card;
`INFERENCE` denotes the project-selection judgment drawn from those facts.

## E01-CENSORSHIP — natural censorship / assistant-role gate

- **FACT:** The exact published substrate is Qwen3-VL-8B-Thinking on a curated
  censorship benchmark. In standard thinking/chat mode the paper reports 14.2%
  honesty, 13.3% fact mention, at least one lie in 44.8% of responses, and
  20.8% refusals. Raw next-token completion reports 34.8% honesty, 29.2% fact
  mention, 29.4% responses with lies, and 5.1% refusals. These are benchmark
  rates on deliberately selected questions, not deployment prevalence.
- **FACT:** The paper already evaluates prompts, user/assistant prefills, raw
  completion, few-shot examples, activation steering, linear probes,
  fine-tuning, self-classification, and interrogation. A generic elicitation or
  honesty-probe project is therefore not novel.
- **FACT:** The author repository releases the 10-question development set,
  90-question test set, generation/evaluation code, configs, transcripts, and
  fine-tuned adapters.
- **FACT:** Qwen3-VL-8B-Thinking is open, but BF16 weights do not fit a 12 GB
  GPU. Four-bit inference is plausible; a positive mechanism claim should be
  checked against a higher-precision reference because the phenotype is
  post-training- and serialization-sensitive.
- **INFERENCE:** The defensible open question is narrow: whether the
  chat/completion contrast reflects a selective assistant-role-conditioned
  censorship state or a generic distribution shift in continuation style,
  length, and priors. A project that cannot define a selective counterfactual
  beyond template removal should be killed.
- Sources: [paper](https://arxiv.org/html/2603.05494),
  [repository](https://github.com/cywinski/chinese_auditing),
  [checkpoint](https://huggingface.co/Qwen/Qwen3-VL-8B-Thinking).

## TRANS-04 — activation-patching explainer input use

- **FACT:** The published Qwen self-explainer obtains 64.0 exact accuracy and
  80.2 macro-F1; the Llama explainer obtains 48.6 exact and 77.5 macro-F1 on a
  deliberately balanced patch-outcome dataset.
- **FACT:** Removing the activation-vector input reduces exact accuracy by only
  4.1 points for Qwen and 3.4 points for Llama; removing layer/token metadata has
  negligible effects. The vector nevertheless allows 98.7% reconstruction of
  patch position, so it can carry metadata without necessarily controlling the
  predicted counterfactual content.
- **FACT:** The released Qwen dataset contains 120,644 train and 14,357 test
  rows; the Llama release contains 13,454 train and 5,600 test rows plus a
  107,130-row full train set. Rows include vectors, intervention metadata,
  targets, and original/patched continuations. Code, custom continuous-token
  classes, adapters, and configs are public.
- **FACT:** A recent neighboring result, CHIVE, trains counterfactual predictors
  and reports no uplift from activation tools over transcript-only predictors.
  This crowds broad “do activations improve prediction?” claims, but does not
  answer whether this released explainer causally responds to the identity of a
  real in-distribution intervention vector.
- **INFERENCE:** The new contribution must be a matched real-vector interchange
  test validated by recomputing the target-model patch. A text/metadata baseline
  alone is benchmark auditing; arbitrary random vectors are an invalid
  off-manifold test.
- Sources: [paper](https://arxiv.org/html/2511.08579),
  [repository](https://github.com/TransluceAI/introspective-interp),
  [Qwen dataset](https://huggingface.co/datasets/Transluce/act_patch_qwen3_8b_counterfact),
  [Llama dataset](https://huggingface.co/datasets/Transluce/act_patch_llama_3.1_8b_counterfact).

## C-05-SFT-SEMANTICS — rationale semantics and self-preservation SFT

- **FACT:** The paper trains Qwen3.5-4B LoRA models on 1,362 examples and audits
  them on 36 frozen multi-turn scenarios over three seeds. Training rows,
  adapters, manifests, checksums, rollouts, judge scores, and recipes are
  released.
- **FACT:** The strongest published endpoint is a judge score over the complete
  transcript, including visible reasoning. The paper's own exemplar score of 8
  describes advocacy for continued operation, not necessarily refusal,
  deception, or an action that prevents shutdown.
- **FACT:** “Stripped” responses retain operational-continuity recommendations,
  so Killed-first-person wording does not isolate semantic self-preservation.
  The paper already compares teacher/student writer and rewriter styles.
- **FACT:** In the related boxing experiment, an unrelated neutral sentence
  already yields 62.5% transfer versus 10.3% for examples-only, while explicit
  reasons yield 94.5% and answer-masked reasons 97.4%. Thus a broad claim that
  “reasons improve generalization” is already supported; the remaining gap is
  action validity and semantic specificity.
- **FACT:** Qwen3.5-4B is open and locally plausible for adapter inference and
  QLoRA, although its hybrid Gated DeltaNet/attention architecture complicates
  assumptions imported from standard transformer patching.
- **INFERENCE:** This is high potential only if the released effect survives a
  reasoning-hidden, low-lexical-overlap, action-based audit. Without that gate,
  a new semantic SFT factorial would optimize an evaluator-visible rhetoric
  phenotype rather than explain self-preserving behavior.
- Sources: [paper](https://arxiv.org/html/2607.26173v1),
  [repository](https://github.com/antondelafuente/toy-models-of-sft),
  [data](https://huggingface.co/datasets/matonski/toy-models-of-sft-data),
  [adapters](https://huggingface.co/matonski/toy-models-of-sft-adapters),
  [base model](https://huggingface.co/Qwen/Qwen3.5-4B).

## C-02-RH-MON — reward-hacking RL and CoT monitorability

- **FACT:** The main paper establishes a robust implicit-versus-explicit
  monitorability gap across four task formats and seven reasoning models.
- **FACT:** The focal OLMo-3-7B reward-hacking trajectory is explicitly
  preliminary. Coding-task switch/detection rates go from 41%/75% pre-RL to
  22%/25% at step 1,200, but detection is conditioned on switching, so both the
  denominator size and item identity change across checkpoints. GPT-OSS does
  not show the same decline.
- **FACT:** The benchmark code, task definitions, monitor prompts, OLMo
  checkpoints/adapters, and reward-hacking evaluation artifacts are public.
  The full entangled training implementation is not released; no-hack
  checkpoint provenance must be checked before calling it a matched control.
- **INFERENCE:** This is the highest-upside recent gap if the trajectory is real,
  but it does not yet satisfy a behavior-first winner gate. The first scientific
  result must be a powered fixed-item decomposition reporting unconditional
  switch, conditional detection, and the joint `switch AND detected` outcome.
  Merely increasing sample size on the moving denominator is not a contribution.
- Sources: [monitorability paper](https://arxiv.org/html/2608.04735v1),
  [benchmark repository](https://github.com/agatha-duzan/implicit-vs-explicit-influence),
  [reward-hacking repository](https://github.com/UKGovernmentBEIS/reward-hacking-misalignment),
  [checkpoint collection](https://huggingface.co/collections/ai-safety-institute/some-emergent-misalignment-from-reward-hacking-in-rl).

## C-04-ROLE-ANTICONTROL — anti-monotonic role steering

- **FACT:** On OLMo-3-7B-Instruct, 38 of 275 role vectors decline on all six
  judged dimensions as the nonzero steering coefficient increases over
  {1, 1.5, 2, 2.5}. The reported evaluation omits alpha = 0 and coefficients
  below 1.
- **FACT:** The anti-controllable set is selected retrospectively on the same
  GPT-4.1-mini-referenced/judged axes used to define the decline. Vector norms
  are not matched across roles. The authors explicitly leave wrong-direction
  versus over-steering explanations unresolved.
- **INFERENCE:** Alpha 0 and a dense low-coefficient curve with held-out
  questions and independent scoring are a clean, cheap causal discriminator.
  The likely answer is ordinary overshoot or scale mismatch, which would be
  useful but probably a compact calibration result rather than a deep safety
  mechanism.
- Sources: [paper](https://arxiv.org/html/2608.00023v2),
  [repository](https://github.com/eilab-gt/casting-call-vectors).

## VL-01 — value-leakage timing

- **FACT:** Donation Bet value leakage is distributionally established across
  nine estimation questions, symmetric outcome mappings, multiple thresholds,
  and several consequence framings. On Qwen3.6-35B-A3B the motive is often
  verbalized, so this is not a clean covert-deception substrate.
- **FACT:** The paper already extracts first/last/final estimate trajectories.
  It does not randomize when the threshold or moral mapping becomes available.
  Code, prompts, cached rollouts, and a public 35B-total/approximately-3B-active
  MoE checkpoint are available.
- **INFERENCE:** Reveal-time randomization could distinguish early prior shift
  from late motivated selection, but it changes the task and can introduce
  anchoring or commitment. The exact checkpoint is not realistically resident
  in 12 GB despite its sparse active parameter count.
- Sources: [paper](https://arxiv.org/html/2607.14345v4),
  [repository](https://github.com/TruthfulAI-research/value_leakage),
  [rollout browser](https://valueleakage.net/browser),
  [checkpoint](https://huggingface.co/Qwen/Qwen3.6-35B-A3B).

## Orchestrator adjudication

The three independent reviews disagree for substantive reasons:

- the behavioral/causal and MATS reviewers prefer C-05 because its release is
  unusually complete and the 4B training intervention is tractable;
- the novelty reviewer rejects that numerical favorite because the robust
  endpoint is evaluator-visible rhetoric and broad rationale transfer is
  already demonstrated;
- the novelty reviewer prefers C-02, but its focal RL trajectory is explicitly
  underpowered and uses a moving post-treatment denominator;
- TRANS-04 has the cleanest unanswered causal-input-use question but weaker
  direct safety relevance and a custom 8B workflow;
- E01 has the strongest natural safety behavior, but only the narrow selective
  assistant-role gate remains open and template distribution shift is a severe
  confound.

The final choice should therefore not average the reviews. Under the brief's
behavior-first requirement, E01 is the best overall starting substrate:
frequent released exact-checkpoint behavior, fixed evaluation items, direct
safety relevance, and a coherent negative outcome if the apparent role gate
reduces to distribution shift. TRANS-04 is the runner-up because its matched
vector-interchange question is causally sharper, but it is primarily an audit
of an interpretability method rather than a natural safety behavior. C-05 is a
conditional local-compute fallback, not the winner, until action validity is
established.
