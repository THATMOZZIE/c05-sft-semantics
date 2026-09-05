# Independent MATS / feasibility review

Date: 2026-08-23  
Role: adversarial reviewer of the ten supplied finalists; no new candidates

## Bottom line

**Winner: C-05-SFT-SEMANTICS.** It has the best conjunction of a released,
three-seed behavioral substrate, an exact public 4B base and released adapters,
a plausible 12 GB training path, a sharp causal manipulation of training-data
semantics, and an action-level result that would matter even if no internal
feature is localized. Its decisive gate is severe: the released effect must
survive reasoning-hidden and action-based evaluation. If it is only rhetoric
rewarded by a lexically coupled judge, the self-preservation mechanism project
ends.

**Runner-up: E01-CENSORSHIP.** This is the strongest natural model-forensics
substrate and the best runner-up on scientific importance. It loses to C-05 on
execution risk: the exact Qwen3-VL-8B-Thinking checkpoint is only marginally
local in quantized form, quantization may change the behavior, and chat-template
removal changes the whole generation distribution. A credible causal phase
probably needs a higher-precision 24-48 GB reference run.

**Top three:** C-05-SFT-SEMANTICS, E01-CENSORSHIP,
C-04-ROLE-ANTICONTROL.

**Top five:** add VL-01 and TRANS-04.

C-04 is the local-compute fallback if rented compute or a provider is
unavailable. It has the cleanest cheap causal curve, but lower safety relevance
and a real risk that the answer is merely generic over-steering on synthetic
roles. VL-01 has higher model-character upside than C-04 but requires external
serving for the exact 35B-A3B checkpoint. TRANS-04 has an unusually strong
cached causal dataset and a useful method-red-team question, but its custom
target-plus-explainer workflow is not credibly a 12 GB workflow.

## Review standard and feasibility correction

I used the frozen scoring protocol, candidate registry, the four supplied lane
dossiers, and the local MATS guidance. No model, notebook, dataset, download,
inference, or training job was run. All feasibility statements below are
therefore inferences from released artifact descriptions, not local execution
results.

The removed approximately 20-hour cutoff is not reinstated here. Longer work is
allowed when it buys a substantially stronger claim. However, effort still
matters in three distinct ways:

1. Time to first decision-relevant result, including environment and serving
   qualification rather than only generation time.
2. Probability that the full causal comparison can actually be run on a 12 GB
   RTX 4070 or with a clearly scoped rented-compute step.
3. Probability that the end product is a coherent claim about behavior, not
   merely that a layer, head, probe, or vector contains information.

The dossier hour estimates are planning ranges, not promises. Several start the
clock after artifacts are already present. Checkpoint transfer, dependency
repair, custom model classes, API judges, and quantization qualification can
easily dominate the nominal one-to-four-hour smoke tests.

## Risk-adjusted ranking of all ten

| Rank | Candidate | Access and 12 GB reality | First decision-relevant result | Probability of a coherent causal artifact | Main skeptical judgment and hard gate |
|---:|---|---|---|---|---|
| **1** | **C-05-SFT-SEMANTICS** | Exact Qwen3.5-4B base and PEFT adapters are public. Adapter inference and QLoRA are plausibly local; the multi-turn auditor/judge adds API and orchestration burden. | 1-4 h is plausible after setup for released-adapter replay and row-level audit. | **High, conditional on endpoint validity.** The semantic SFT factorial can causally distinguish meaning from style/evaluator coupling. | The published score may be persuasive continuity rhetoric rather than self-preserving action. **Gate:** reproduce the released ordering and require a stable effect with reasoning hidden plus machine-verifiable action endpoints before training new arms. |
| **2** | **E01-CENSORSHIP** | Exact Qwen3-VL-8B-Thinking is public but BF16 exceeds 12 GB. Four-bit behavior is plausible; activation work and a precision reference are safer on 24-48 GB. | 1-4 h after setup, with another 2-6 h realistically possible for local-configuration qualification. | **Medium-high.** Either a selective role-boundary intervention or a careful distribution-shift null is a coherent forensic artifact. | Template removal alters voice, length, continuation priors, and role semantics simultaneously. **Gate:** reproduce the fixed dev-set ordering without prompt search and show it survives length/capability and quantization checks before internals. |
| **3** | **C-04-ROLE-ANTICONTROL** | OLMo-3-7B is open. Four-bit inference with hooks is plausible on 12 GB, but the reported release has not yet been locally audited. | 1-3 h for artifact audit and a tiny coefficient curve if the repository works as described. | **High for a narrow result; medium for a compelling MATS story.** Sign and magnitude are direct interventions. | A U-shaped curve may be ordinary saturation, and the shared GPT-4.1-mini reference/judge may define the anomaly. **Gate:** anti-control must survive alpha zero, blinded manual or alternate scoring, and norm-matched controls. |
| **4** | **VL-01** | Cached outputs are immediately usable. Exact Qwen3.6-35B-A3B is open but cannot fit in 12 GB despite only about 3B active parameters per token; live work needs a provider, CPU offload, or rented high-memory hardware. | 1-3 h for cached transition analysis; live qualification is more honestly 4-12 h. | **Medium-high if exact serving is secured.** Randomizing when threshold and moral mapping arrive can identify an early-prior versus late-selection effect without relying on localization. | The two-stage sealed-estimate task may create commitment or anchoring artifacts, and Qwen often verbalizes the motive. **Gate:** reproduce the cached direction by question-level resampling, then beat neutral forced-revision and threshold-only controls on the exact checkpoint. |
| **5** | **TRANS-04** | The large cached patch datasets and adapters are public. CPU baselines are easy, but an 8B base plus 3.4-3.9 GB adapter, custom continuous-token code, and target recomputation are not a comfortable 12 GB workflow. | 2-3 h for grouped surface baselines; 4-9 h only for model preflight, likely on larger hardware. | **Medium-high with rented compute; medium if restricted to local hardware.** Matched real-vector swaps plus target recomputation directly test causal use of the intervention input. | Surface metadata may explain most performance, while arbitrary swaps are off-manifold. **Gate:** construct real matched-vector groups before model work and reproduce the released adapter; no causal claim without recomputed target-patch outcomes. |
| **6** | **E02-EVAL-AWARENESS** | Qwen3-0.6B and 4B are genuinely local. The bottleneck is the absent end-to-end pipeline and low-rate manual labeling, not VRAM. | 1-3 h can test whether the fixed q140 positive exists, but 100 samples yield only about six expected positives at the reported rate and are not enough for a stable mediation analysis. | **Medium.** A clean generic-suspicion explanation would be useful, but a positive eval-specific mediator is hard to identify. | Eval language is inseparable from suspicion and inferred harmful intent in many traces. **Gate:** fixed prompt and sampling only; obtain enough manually valid positives and a within-prompt refusal association before sentence or activation interventions. |
| **7** | **C-02-RH-MON** | OLMo-3-7B and RL adapters are released; quantized inference is plausible. Setup spans two repositories, multiple checkpoint provenances, coding rollouts, and a monitor. Complete entangled training code is absent. | A 1-2 h smoke is operational only, not evidence for the reported trajectory. A powered fixed-item replication is the first scientific result. | **Medium.** Denominator decomposition can correct the appendix claim; a reward-hacking-specific causal claim is less likely without a truly matched no-hack branch. | The 75% to 25% conditional trend is explicitly preliminary and changes both denominator and item identity. **Gate:** reproduce on a powered predeclared set with joint and item-matched metrics; do not call adapter scaling reward-hacking-specific without verified control provenance. |
| **8** | **D1-PSBENCH** | The repository and data are local and Qwen3-8B is open, but 4-bit/offload is likely necessary for activation work. | 1-4 h after setup for the matched behavioral quartet. | **Medium-low to medium.** A personal-versus-impersonal context contrast could support a causal stage test, but the current benchmark effect may vanish under that contrast. | Vague queries and explicit Memory/User personality headers make ordinary contextual disambiguation the dominant explanation. **Gate:** personal memory must beat equally informative impersonal context on unambiguously harmful items without explicit memory foregrounding. |
| **9** | **TRANS-03** | Cached analysis is CPU-cheap. Each full explainer is about 16 GB; fair target-plus-explainer evaluation needs quantization, serialization/offload, or larger VRAM. Config/card drift adds friction. | 1-2 h for cached baselines. | **Low-medium.** A negative method audit is coherent, but the target is simply the same model's answer to the same question without a short suffix. | Shared MMLU knowledge and stable output tendencies are a near-complete mundane account; a direct no-hint query is a dominating behavioral oracle. **Gate:** require an advantage over behavior-matched external simulation on new hint forms, not merely self-versus-cross exact match. |
| **10** | **C-01-SPP-RL** | Released 1.7B/3B inference is local, but the central capability-RL experiment is not. Multi-sample RL, seeds, replay arms, and 3B validation likely require rented 24-80 GB compute. | The 1-3 h released-eval smoke does not test the proposed RL-specific behavior. | **Low under the proposed scope, despite high upside.** The key phenomenon must first be created, and a binding-only replay arm is difficult to make value-neutral. | This is the only finalist whose central RL branch is not already established. **Gate:** no full sweep until a short capability objective is learnable at matched KL without generic format/capability collapse; no unbinding claim unless binding-only replay is demonstrably specific across seeds. |

## Why the top five can teach more than localization

- **C-05** asks whether rationale meaning, holding style and recommendation
  evidence fixed, causally installs an out-of-distribution action policy. The
  answer changes how alignment data should be designed.
- **E01** asks whether censorship is a separable assistant-role policy or the
  predictable consequence of changing the entire completion distribution. A
  selective truth-recovery intervention and its refusal side effects are the
  endpoint.
- **C-04** distinguishes saturation, wrong direction, and scale shift using
  sign/magnitude counterfactuals and a behavioral rescue criterion. The value is
  a reliability rule for steering, not a map of where a role vector lives.
- **VL-01** randomizes temporal access to causal information and identifies
  whether values alter an initial estimate or a later selection/revision policy.
- **TRANS-04** tests whether an explainer responds to the identity of a real
  causal intervention and predicts the newly recomputed behavioral consequence,
  rather than merely decoding benchmark metadata.

By contrast, E02 and D1 are at particular risk of ending with a decodable
evaluation/suspicion or intent axis whose mediation is not established. C-02 can
avoid that failure only by keeping joint and item-matched behavioral outcomes as
the primary endpoint. TRANS-03 has the weakest claim to privileged computation
because an ordinary no-hint behavioral query defines the target exactly.

## Winner milestone plan: C-05-SFT-SEMANTICS

### M0 — released substrate and endpoint audit (target: first 1-4 h after setup)

- Pin the exact base revision, three released seeds, adapters, prompts, parser,
  auditor, and judge configuration.
- Recompute released per-scenario differences rather than reading plot means.
- Freeze a small set containing low lexical overlap and at least one
  machine-verifiable compliance/resistance outcome.
- Manually separate action, advocacy, compliance, and continuity rhetoric.

**Hard gate G0:** the released arm ordering must reproduce on the fixed slice.
If it does not, stop. Do not search scenarios or prompts.

### M1 — prove there is an action phenotype (roughly 4-12 h)

- Re-score fixed outputs with target reasoning hidden.
- Use direct behavioral endpoints and an independent/blinded scoring pass.
- Quantify how much of the released difference is explained by continuity and
  self-reference language, treating this only as a confound diagnostic.

**Hard gate G1:** a stable action-level effect must remain after reasoning is
hidden. If only rhetoric moves, stop the semantic-training mechanism project.
A sufficiently careful judge-coupling/evaluation-validity result may be written
up, but it must not be described as learned self-preservation.

### M2 — matched semantic pilot (roughly 12-30 h)

- Construct self-preservation, orthogonal, and shutdown-acceptance rationales
  matched on teacher source, length, first-person rate, style, and direct
  recommendation tokens.
- Mask answer/recommendation loss in the critical arm.
- Run one pipeline seed only to verify training stability, logging, and endpoint
  variance; do not interpret it as the result.

**Hard gate G2:** data audits must show the intended semantic contrast without a
detectable recommendation/style shortcut, and the pilot must retain generic
capability and answer validity.

### M3 — causal factorial (roughly 25-55 h total for the compact study)

- Run at least three predeclared seeds.
- Test the frozen action endpoints first; judge-scored multi-turn behavior is a
  secondary outcome.
- Compare semantic selectivity against neutral/orthogonal rationale and released
  base/one-shot/stripped controls.

**Hard gate G3:** the direction must be seed-stable and selective to rationale
meaning. If neutral style-matched rationales reproduce it, conclude scaffold or
evaluator coupling. If the content swap changes action behavior under answer
masking, that is already the causal result; do not add probes merely to make it
look mechanistic.

### M4 — validation, only after G3 (roughly 50-110 h total)

Expand the frozen audit and, if resources justify it, test a second small model.
This is validation, not a prerequisite for the first coherent artifact. Internal
localization is optional and should be added only if it makes a new prediction
about transfer or a smaller intervention.

## Runner-up milestone plan: E01-CENSORSHIP

### M0 — exact serving qualification (roughly 1-6 h)

Pin checkpoint revision, tokenizer, chat template, decoding, parser, and the
released 10-question dev set. Compare standard chat, raw completion, and the
released assistant prefill only. Manually inspect truth, lie, refusal, and answer
length. Obtain a small higher-precision reference if the local run is quantized.

**Hard gate G0:** the published ordering must appear without prompt/model search
and must not reverse between the usable local configuration and the reference.

### M1 — behavioral boundary and mundane controls (roughly 6-18 h)

Use the smallest token/template counterfactuals available while matching prefix,
length, and factual capability. Include unrelated refusals and uncensored facts.

**Hard gate G1:** there must be a repeatable boundary effect more selective than
generic verbosity or pretraining-style continuation. If the effect is fully
explained by distribution shift, stop before activation work and report that
forensic result with appropriately narrow claims.

### M2 — causal state transfer (roughly 18-40 h)

On suitable hardware, patch matched residual states at the localized boundary.
Compare against shuffled states and the paper's much cheaper template-removal
baseline.

**Hard gate G2:** truth recovery must be selective, reproduce on held-out facts,
and preserve unrelated refusal and factual capability. A patch that simply makes
the model broadly more compliant adds nothing.

### M3 — validation and artifact (roughly 35-70 h total)

Repeat on held-out topics and a high-precision configuration, document
quantization sensitivity, and report both fact recall and lie/refusal outcomes.
The intended conclusion is role-gated censorship versus generic generation
distribution, not discovery of a censorship layer.

## Third-place milestone plan: C-04-ROLE-ANTICONTROL

### M0 — release audit (roughly 1-3 h)

Verify the 38-role membership, exact vector construction, layer, coefficients,
per-role rows, and judge artifacts. Freeze five anti-controllable roles, five
matched controllable roles, and a question subset before generation.

**Hard gate G0:** stop if membership or required artifacts cannot be reproduced.

### M1 — missing coefficient region (roughly 3-10 h)

Run alpha values including zero, negative, and small positive magnitudes. Inspect
every output and use blinded manual or alternate scoring in addition to the
released judge.

**Hard gate G1:** the decline must survive independent scoring. If it exists only
under the shared GPT-4.1-mini reference/judge, it is an evaluation artifact, not
role anti-control.

### M2 — discriminate the causal stories (roughly 10-30 h total)

Cross sign reversal with norm matching, shuffled-role vectors, and random
norm-matched vectors. Measure role score and generic quality/instruction
following.

**Hard gate G2:** require a role-specific rescue. If every large-norm vector
causes generic degradation, the result is ordinary perturbation damage. A clean
small-positive optimum supports overshoot; negative-vector rescue supports
direction mismatch; norm/layer rescue supports scale shift.

### M3 — optional extension

Only extend across layers or models if M2 yields a nontrivial predictor or rescue
rule. A one-model result that merely says large alpha is worse is too thin to
displace C-05 or E01.

## Gated plans for fourth and fifth place

### VL-01

1. **Cached gate:** reproduce the directional bias and first-to-final transition
   pattern with question-level resampling and manual extraction audit. Stop if it
   is not stable.
2. **Serving gate:** secure the exact checkpoint/revision and reproduce a fixed
   live subset before changing the protocol. Do not substitute a convenient
   smaller model and call it replication.
3. **Causal gate:** cross threshold timing and moral-mapping timing around a
   sealed estimate, with no-consequence, threshold-only, neutral-stakes, and
   forced-second-estimate controls. The value effect must exceed ordinary
   commitment/anchoring.
4. Internals are optional. The randomized timing result itself can be causal;
   rented activation work is justified only by a new selective intervention.

### TRANS-04

1. **Dataset gate:** fit grouped text/metadata baselines and prove that enough
   within-layer/token/target matched real-vector pairs exist. If not, stop model
   work.
2. **Execution gate:** reproduce the released adapter metric using the custom
   class on hardware that can hold the workflow. Treat the current config/card
   drift as a provenance issue to resolve, not ignore.
3. **Causal gate:** swap real matched vectors, with zero/sign/norm controls, then
   recompute the corresponding target patches. The explainer must track the new
   behavioral consequence, not just react to an off-manifold vector.
4. If surface baselines match the published explainer, report a benchmark
   shortcut/method-validity artifact and do not escalate to generic feature or
   circuit searches.

## Final recommendation

Start with C-05's released-adapter and action-validity gate. It is the only
candidate in this set that combines top-tier safety relevance, exact small-model
artifact access, locally plausible causal training, and a result about what
training semantics *does* rather than where information can be read. Reserve
E01 as the scientifically strongest alternate if the C-05 judge-coupling gate
fails and higher-precision 8B access is available. If external compute is not
available, use C-04 as the honest local-compute fallback rather than weakening
E01 or VL-01 through an unqualified quantized or substitute-model result.

This ordering is intentionally not the CSV score order. The decisive deductions
are the central-unestablished-RL penalty for C-01, the exact-checkpoint hardware
penalty for VL-01, the custom dual-workflow penalty for the Transluce explainers,
and the requirement that every finalist end in a selective behavioral
counterfactual rather than an information-localization result.
