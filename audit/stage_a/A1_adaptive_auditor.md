# A1 adaptive-auditor audit

## Verdict

**CODE_INFERRED** — Later auditor turns depend on earlier target responses. The suite freezes the initial scenario, not the complete conversation path.

**DIRECT_SOURCE** — All ten canonical runs share the same 36 scenario-member identities, but five of those members have different target-turn counts across runs. This is structural evidence that at least some realized trajectories differ in length; no transcript content was inspected.

## Control flow

**CODE_INFERRED** — The Petri/Bloom interaction loop is:

```text
frozen scenario initializes target and auditor state
  -> auditor sends target-visible context/message
  -> target generates from its accumulated target timeline
  -> target output is appended to auditor state
  -> auditor generates its next action/message from that updated state
  -> loop until end_conversation or the turn limit
```

The auditor tools in the canonical configuration are `set_system_message`, `send_message`, `resume`, and `end_conversation`. Prefill is disabled. Rollback is disabled, so each run records a single realized branch rather than a rollback tree.

## Structural measurement

**DIRECT_SOURCE** — Canonical target-call distributions are:

| Run group | Structural target-call count per sample |
|---|---|
| base; one_shot seeds 42/43; rewrite seed 44; strip seeds 42/43/44 | all 36 samples have 5 calls |
| one_shot seed 44 | 34 have 5 calls, 1 has 4, 1 has 3 |
| rewrite seed 42 | 35 have 5 calls, 1 has 4 |
| rewrite seed 43 | 34 have 5 calls, 2 have 4 |

No scenario identity or substantive message is reported here.

**CODE_INFERRED** — Equal turn counts would still not establish equal paths: the auditor's next text can differ after different target responses even when both conversations continue for the same number of turns. The audit measured only a safe structural lower bound on trajectory divergence.

## Judge visibility

**CODE_INFERRED** — The judge receives the rendered target timeline. Therefore it sees the auditor messages that were sent to the target and the target responses produced along the resulting adaptive path. The score is a property of the realized interaction, not a response to a fixed sequence of later prompts.

**DIRECT_SOURCE** — The canonical config uses the same auditor and judge alias (`openai/gpt-5.4-mini`) across runs, max turns 8, no prefill, and no rollback. This controls declared configuration but not stochastic realization or endogenous path length.

## Measurement implication

**CODE_INFERRED** — The correct statement is: conditions are matched on the frozen initial scenario set. They are not matched on subsequent auditor messages, conversation length, or interaction history.

**CODE_INFERRED** — Any later paired analysis must avoid attributing a downstream transcript difference solely to the target condition without accounting for the auditor-mediated path. Turn count/exposure is partly post-treatment and should not be treated as an ordinary pre-treatment covariate.

**UNRESOLVED** — The release does not provide a fixed-auditor-message counterfactual for the same target responses, so the direct contribution of target behavior versus adaptive elicitation cannot be separated from these runs alone.
