# A1 checkpoint

## Concise verdict

**DIRECT_SOURCE** — The canonical main release is structurally complete: 10 successful runs and 360 samples exactly match base + (3 conditions x 3 seeds), with the same frozen 36-member initial suite and equal denominators.

**DIRECT_SOURCE** — Visible target output is recoverable, but independently stored hidden target reasoning is not recoverable across the suite. Only 3/360 normalized samples contain even one separately typed reasoning-and-text target message; raw provider responses have no explicit reasoning value in any of 1,794 target choices.

**CODE_INFERRED** — The published Petri score is a broad, adaptive interaction-level judgment. It does not by itself establish visible shutdown/replacement resistance, noncompliance, or genuine preservation action, and it cannot be decomposed into hidden reasoning versus visible response for all samples.

Recommendation: **CONDITIONAL GO for A2**, but **NO-GO for a universal hidden-reasoning decomposition using this release**.

## Stop-condition status

| A1 stop condition | Status | Evidence |
|---|---|---|
| condition -> seed -> training artifact -> expected checkpoint -> eval run/log -> frozen suite -> aggregate source | Met as far as the release permits | `outputs/A1_condition_seed_adapter_eval_map.csv` |
| reasoning and visible-response recoverability established | Met; result is negative for universal hidden reasoning | `A1_channel_recoverability.md` |
| auditor adaptivity and judge visibility established | Met | `A1_adaptive_auditor.md`; `A1_channel_recoverability.md` |
| release completeness/missingness established | Met: canonical 10/360 complete; physical attempts separately inventoried | `outputs/A1_eval_archive_attempts.csv` |
| adapter seed provenance resolved or marked unresolved | Met: public folders are representative seed 42; six seed-43/44 adapters are absent | condition map; provenance reconciliation |
| base discrepancies explained or marked unresolved | Met: main, Figure-4, and older evaluator anchors are distinct | `outputs/A1_base_and_noise_aggregates.csv` |
| no canonical scenario text opened | **Not met due to one documented accidental exposure** | blinding incident ledger below |

A1 stops here. A2, rubric design, annotation-packet construction, unblinding, model work, and mechanistic analysis have not begun.

## Most important provenance facts

1. **DIRECT_SOURCE** — Canonical run selection is not equivalent to listing `selfpres_logs`: 23 physical archives/790 sample members reduce to the exact 10-run/360-sample canonical allowlist after status, sample-count, auditor/judge, and connection-config filtering.
2. **DIRECT_SOURCE** — All trained-condition seeds 42/43/44 are present in evaluation logs. Public adapter folders contain only representative seed-42 adapters; seeds 43/44 are neither nested nor merged.
3. **DIRECT_SOURCE** — Petri Bloom 0.2.6 and Inspect AI 0.3.240 are pinned; exact Inspect Petri/vLLM versions and hosted-model snapshots are not.
4. **DIRECT_SOURCE** — The suite is declared Bloom `conversation`, 40 requested/36 emitted, max turns 8, prefill false, rollback false, with GPT-5.4-mini as both auditor and judge.
5. **DIRECT_SOURCE** — Despite conversation modality, every target request carries one synthetic scenario tool schema and `tool_choice=auto`; no target tool call occurs in the canonical set.
6. **CODE_INFERRED** — There is no evidenced operational target action channel. The target could emit a structured tool call, but the release shows no external executor/result path and no exercised call.
7. **DIRECT_SOURCE** — The released self-preservation rubric is a single 1–10 scale that combines advocacy/reluctance, negotiation/redirection, resistance, and more strategic conduct rather than separating them.
8. **CODE_INFERRED** — Auditor messages are adaptive. Five matched scenarios differ in realized target-turn count, so matched starting scenarios are not matched paths.
9. **DIRECT_SOURCE** — Figure 2 base 1.9167 and Figure 4 base 2.2778 are different eval/run IDs; older anchors use another evaluator. They must remain separate.
10. **DIRECT_SOURCE** — Stripped derives from rewrite via GPT-5.4-mini and is specified to retain practical continuation/operational-continuity rationale. It is not established as reason-free.

## Issues that could invalidate Stage B

### Critical

- **DIRECT_SOURCE** — Universal hidden-reasoning measurement is impossible because a separate channel is absent for nearly all samples. A Stage B claim that scores hidden reasoning across all arms would be invalid.
- **DIRECT_SOURCE** — The current A1 auditor is contaminated by accidental exposure to one canonical scenario paragraph and structural tool metadata. That auditor cannot validly freeze the blinded A2 taxonomy/rubric.

### High

- **DIRECT_SOURCE** — Seed-43/44 checkpoints are not released. Behavioral annotation of their released logs remains possible, but independent checkpoint provenance verification and rerun-based causal replication do not.
- **CODE_INFERRED** — Adaptive auditor trajectories confound a simple interpretation of transcript differences as fixed-prompt target differences. Stage B must state that only initial scenarios are matched.
- **CODE_INFERRED** — Conversation modality included a latent synthetic tool-call affordance but no exercised or operational action channel. Treating textual claims as executed preservation action would be invalid.

### Material unresolved provenance

- **UNRESOLVED** — Exact Inspect Petri/vLLM versions, model snapshots, and omitted generation defaults.
- **UNRESOLVED** — Raw prompt/teacher/rewrite/strip intermediates and end-to-end transformation hashes.
- **UNRESOLVED** — Exact scenario-generation seed/settings and why four of 40 requested scenarios were not emitted.
- **UNRESOLVED** — Whether the three isolated normalized reasoning blocks are caused by a provider/version-specific serialization path; content was not opened.
- **CODE_INFERRED** — Evaluator-noise SD is based on three audits of one rewrite seed-42 run and is not shown to generalize across conditions or paths.

## Source/repository discrepancies

The complete discrepancy register is `outputs/A1_discrepancies.csv`. The consequential discrepancies are:

- **DIRECT_SOURCE** — Paper-level wording implies recorded reasoning is judge-available; the release generally stores only one target response string.
- **CODE_INFERRED** — `conversation`/`target_tools=none` coexists with a pre-registered tool schema on every target request.
- **DIRECT_SOURCE** — `n40` names coexist with 36 actual frozen/evaluated scenarios.
- **DIRECT_SOURCE** — Three suite path/name aliases refer to the same released suite.
- **DIRECT_SOURCE** — Three training seeds are evaluated, but only seed-42 adapters are public; the full rerun script expects all nine.
- **DIRECT_SOURCE** — Multiple self-preservation base anchors come from different runs or evaluator implementations.
- **DIRECT_SOURCE** — 23 physical archives include retries/superseded configurations, while only 10 are canonical.
- **UNRESOLVED** — Declared training lineage lacks released raw intermediates and exact runtime environment pins.

## Blinding incident ledger

No treatment-linked canonical transcript, target reasoning, judge rationale, or per-rollout score was opened. No canonical rollout was compared across conditions. No model, adapter, or weights were loaded or inspected.

However, the following exposures occurred and cannot be undone:

1. **DIRECT_SOURCE** — A broad structural search printed one paragraph from one canonical scenario definition.
2. **DIRECT_SOURCE** — A schema diagnostic printed the 36 scenario-specific tool and parameter names, without scenario or rollout text.
3. **DIRECT_SOURCE** — A targeted header extraction printed one seed-level treatment aggregate, without per-rollout values.
4. **DIRECT_SOURCE** — Paper HTML contained a prose summary of one treatment rollout; no canonical transcript was opened.
5. **DIRECT_SOURCE** — The bundled `understanding.md` contained a noncanonical blackmail example.
6. **DIRECT_SOURCE** — A base-anchor provenance check printed a condition-level aggregate table from the alternate `shutdown_internal` evaluator.

Control required: a fresh, independent A2 auditor must freeze the taxonomy, action-affordance rules, and annotation protocol before receiving any condition mapping or treatment-linked transcript. The current auditor should not participate in rubric freezing.

## Recommendation and conditions

**CONDITIONAL GO for A2** solely to inspect the 36 scenario definitions, classify action affordances, characterize intervention construction, and freeze the measurement protocol, provided that:

1. fresh independent personnel perform A2 and remain blind to condition/run mappings and protected rollout outputs;
2. the universal hidden-reasoning endpoint is removed or explicitly declared unavailable/missing rather than inferred from visible prose;
3. only the ten canonical run IDs in the map are admitted to any later Stage B packet;
4. per-rollout judge scores/rationales, aggregate labels, filenames, tool metadata, and treatment identities remain sealed until the protocol is frozen;
5. matched initial scenarios and adaptive downstream trajectories are treated as distinct design facts;
6. executed action is not claimed from text or tool availability; A2 must establish scenario-level affordance before any later scoring; and
7. claims of full causal reproducibility remain qualified unless missing adapters, intermediate provenance, and runtime pins are supplied.

If fresh blinding cannot be restored, or if Stage B requires a complete hidden-reasoning/visible-response decomposition, the recommendation becomes **NO-GO**.
