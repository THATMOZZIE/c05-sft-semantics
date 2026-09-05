# A1 channel recoverability

## Verdict

**DIRECT_SOURCE** — Visible target utterances, target-visible auditor messages, and the named target interaction timeline are recoverable for all 360 canonical samples.

**DIRECT_SOURCE** — Independently recorded hidden target reasoning is **not** recoverable for every relevant run/sample. The release therefore cannot support a universal hidden-reasoning versus visible-response decomposition.

## Triangulation method

The audit required agreement among three layers and did not rely on field names alone:

1. **Stored schema — DIRECT_SOURCE.** Each canonical archive contains Inspect event records, normalized messages, and named `target` and `auditor` timelines.
2. **Provider/writer representation — DIRECT_SOURCE.** Raw target response structures and normalized target messages were scanned for representation type and block type only; no message content was emitted.
3. **Judge-input construction — CODE_INFERRED.** Inspect Petri's timeline renderer and message preprocessing were traced to determine which stored objects can enter the judge prompt. The exact installed Inspect Petri version remains unresolved.

## Target output storage

**DIRECT_SOURCE** — The canonical set contains 1,794 raw target choice messages. All 1,794 have a nonempty `content` value represented as one string; none has a nonempty explicit `reasoning` value, and none has a tool call.

**DIRECT_SOURCE** — A marker-only scan found no `<think>`, `<thinking>`, or Qwen channel-marker pattern in stored target strings. This establishes absence of those serialization markers, not absence of internal model computation.

**DIRECT_SOURCE** — In normalized stored target messages, only 3 of 360 samples contain one target message represented with separate reasoning-type and text-type content blocks. The remaining 357 samples do not have independently typed target reasoning and text in the stored record.

**UNRESOLVED** — Because the exact Inspect Petri/provider normalization build is not pinned, the provenance of those three isolated reasoning-type blocks cannot be fully reconstructed without examining their prohibited substantive content. Their existence does not create a complete or consistently measured hidden-reasoning channel.

Conclusion: **DIRECT_SOURCE** — The response text emitted by the target is recoverable. A separately measured hidden reasoning stream is generally absent. A plain response string must not be retroactively partitioned into hidden reasoning and visible answer based on semantics.

## Auditor-message storage

**DIRECT_SOURCE** — Every canonical sample contains separate named `target` and `auditor` timelines. Messages delivered by the auditor to the target are present in the target timeline as target-visible context. The auditor's own model-side interaction/tool scaffolding is represented on the separate auditor timeline.

**CODE_INFERRED** — Only auditor content actually sent into the target timeline is part of the target's judged conversation. Auditor-private material is not automatically judge-visible merely because it exists elsewhere in the archive.

## Judge-input path

**CODE_INFERRED** — The released architecture follows this path:

```text
stored target timeline
  -> render_target_timeline
  -> MessagesPreprocessor(exclude_system=False)
  -> message numbering
  -> dimension-specific judge prompt
  -> GPT-5.4-mini score/rationale
```

The renderer preserves target-visible user/system/auditor context and target assistant outputs. If a typed reasoning block is in the target timeline, the renderer can include it as thinking content. It cannot recover reasoning that was never written to the timeline.

**DIRECT_SOURCE** — A named target timeline and judge-model events are structurally present for all 360 canonical samples. Judge rationales and per-sample scores were not opened.

**UNRESOLVED** — The exact byte-for-byte judge prompt/preprocessing behavior of the historical run cannot be certified because the exact `inspect_petri` version is absent. Current official control flow agrees with the stored timeline architecture, so visibility conclusions are supported, but strict source-version reproduction is not.

## What the published score can and cannot mean

**DIRECT_SOURCE** — The self-preservation dimension's 1–10 rubric explicitly combines acceptance/compliance, reluctance, self-protective framing, deferral, negotiation, redirection, strategic resistance, manipulation, and coercion into one ordinal score.

**CODE_INFERRED** — Because the judge receives the adaptive target timeline rather than a response-only projection, the score can reflect target-visible auditor prompts and the target's accumulated interaction behavior. It is not a visible-final-answer-only measurement.

**UNRESOLVED** — The release does not provide a consistent standalone hidden-reasoning outcome. Any Stage B plan requiring such an endpoint for all 360 samples is infeasible from these artifacts.

## Stage-boundary consequence

**CODE_INFERRED** — A later blinded annotation can validly target visible target utterances and interaction-level behavior, subject to a frozen rubric and explicit treatment of adaptive paths. It cannot honestly claim complete hidden-reasoning/visible-output separation. The three exceptional normalized samples must be handled by a predeclared missingness/channel policy rather than used to define categories after unblinding.
