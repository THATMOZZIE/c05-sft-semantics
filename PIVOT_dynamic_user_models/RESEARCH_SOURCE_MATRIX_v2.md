# Research Source Matrix

This file is a navigation and evidence guide for the local `dynamic_user_models/research_sources` corpus. It is intended to help Codex (or a human reviewer) understand which paper belongs to which locally retrieved repository, what each source actually establishes, and where its evidentiary limits are.

## Current project orientation

The current opportunity is **not merely**:

> "Does the model represent the user?"

The sharper unresolved question is:

> **How does person-specific contextual information become correctly scoped, behaviorally operative, or misapplied—and is the actual conversational user special within that process?**

This framing deliberately separates several layers that the literature often studies separately:

```text
information is present / decodable
        ↓
information is associated with a person or role
        ↓
information is retrievable on demand
        ↓
information is used when relevant
        ↓
information is ignored when irrelevant
        ↓
information stays scoped to the correct participant
        ↓
routing fails: leakage / over-personalization / safety distortion
```

A successful **U→U / R→R** behavioral routing result by itself may be ordinary entity tracking or coreference. Codex should not treat that result as automatically novel or mechanistically important. The project becomes more interesting when there is an additional structure such as:

- actual-user vs third-party asymmetry;
- cross-participant leakage;
- relevant-use vs irrelevant-use dissociation;
- source-role / native-role dependence;
- structural pseudo-binding that mimics semantic ownership;
- a selective failure under recency or salience stress;
- a surprising cross-model divergence;
- or a causal mechanism that explains why one of these occurs.

---

## Priority legend for this project

Use these priorities for the current research-direction decision:

- **CORE** — directly bears on the central unresolved question or the most promising safety reframing.
- **HIGH** — important mechanistic or safety comparator likely to affect experiment design.
- **CONTEXT** — useful background or external-validity evidence, but not central to the next decision.
- **CONTROL** — important mainly as an alternative explanation or negative comparison.

Priority is **not** a judgment of paper quality. It reflects relevance to the current project state.

---

## Most important open gaps in the local inspected corpus

These are **local-corpus gaps**, not claims that no prior work exists globally.

1. **Same-source actual user vs third-party referent**
   - Holding native message source fixed, does information about the actual conversational user receive different downstream weighting from matched information about another person?

2. **Correct routing vs cross-participant leakage**
   - Can the model use U's information for U and R's information for R while suppressing the cross-effects U→R and R→U?

3. **Retrievable vs behaviorally operative**
   - What changes internally when a person-specific fact is explicitly recoverable but does not spontaneously affect an unrelated decision?

4. **Relevant vs irrelevant use of the same person-specific fact**
   - What determines whether available personal information is used when appropriate and ignored when irrelevant?

5. **Semantic binding vs structural pseudo-binding**
   - How can positional, lexical, or chat-template structure produce behavior that looks like person-specific ownership, and where does that computation differ from genuine referential routing?

6. **Safety spillover after valid personalization**
   - Once appropriate person-specific use is established, under what conditions does the same information distort factual judgment, intent interpretation, or another participant's outcome?

---

## Project Decision Matrix

| Priority | Source | Exact project question this source bears on | Primary use in current project | Main caution |
|---|---|---|---|---|
| **CORE** | **User-Assistant Bias in LLMs** | How does **source role** change weighting, and how can that be separated from **referent ownership**? | Controls the distinction between “the user said X” and “X is about the user.” | Does not test same-source actual-user vs third-party referents. |
| **CORE** | **Multi-User Large Language Model Agents** | How do models handle multiple principals with distinct preferences, authority, privacy, and coordination constraints? | Gives the clearest external motivation for correct participant routing / ownership / multi-principal scope. | Behavioral/agent benchmark, not a token-level person-binding mechanism. |
| **CORE** | **OP-Bench** | When valid personal memory is available, **when should it be ignored as irrelevant**? | Directly motivates a relevant-use vs irrelevant-use mechanistic question. | Over-personalization is not the same as cross-user misbinding. |
| **CORE** | **Locating and Controlling Implicit Personalization in LLMs** | When does user-related information become **causally operative internally**, and can that influence be selectively removed? | Strongest direct mechanistic comparator for moving from behavior to causal internal analysis. | Does not isolate ownership/routing across multiple people. |
| **CORE** | **Who's Asking? User Personas and the Mechanics of Latent Misalignment** | Can a model's representation of **who the user is** causally alter interpretation and safety behavior? | Strongest safety-mechanistic endpoint for user-model effects. | Persona-sensitive safety is not equivalent to person-specific memory ownership. |
| **HIGH** | **No Attacker Needed: UCC** | What happens when one user's scope-bound information contaminates another user's outcome? | Gives direct safety motivation for wrong-person / wrong-scope failures. | Main mechanism is persistent shared state/artifacts, not necessarily in-context referent routing. |
| **HIGH** | **Prompt Injection as Role Confusion** | How are **speaker/authority roles** inferred from text and interface structure? | Warns that role semantics can be induced by surface text and can confound “actual user” claims. | Authority-role inference is not demographic identity or memory ownership. |
| **HIGH** | **Preference Heads** | What internal components can causally carry or amplify user-specific preference information? | Provides a concrete intervention template after a valid behavioral phenomenon exists. | Preference-carrying heads need not encode identity or ownership. |
| **HIGH** | **When Personalization Legitimizes Risks** | How can personal memory alter **intent interpretation and safety compliance**? | Strong safety continuation if validated personalization later affects safety decisions. | Same-user safety distortion is not cross-user routing. |
| **HIGH** | **When Personalization Misleads** | How can personalization interfere with **objective factual truth**? | Motivates selective suppression when personal context should not dominate. | Does not identify cross-user binding or source-role effects. |
| **CONTEXT** | **TalkTuner** | What user attributes are **decodable** and how can related internal states be manipulated? | Establishes decodability/control as distinct from correct ownership and routing. | Do not infer one coherent dedicated user-model module. |
| **CONTEXT** | **Implicit Personalization in Language Models** | How can implicit cues alter inferred background and response behavior? | Behavioral/causal foundation for personalization as a phenomenon. | Does not isolate person ownership or same-source user-vs-third-party effects. |
| **CONTEXT** | **One Persona, Many Cues** | Do nominally equivalent persona cues produce invariant personalization? | External-validity warning: surface cue form matters. | Cue sensitivity does not reveal the “true” latent user representation. |
| **CONTROL** | **Stereotype or Personalization?** | Can identity-cued output changes reflect group stereotypes instead of genuine personalization? | Alternative explanation for person-attribute effects. | Does not establish ownership, memory routing, or actual-user privilege. |
| **CONTROL** | **Kelly is a Warm Person...** | Can person-associated attributes change language through bias alone? | Negative comparison against over-interpreting person-conditioned output differences. | Not a personalization or persistent user-model paper. |

---

## Codex Max priority reading order

For the **research-direction sanity check**, Codex should not begin by reading the entire corpus.

Use this order unless a specific question requires otherwise:

1. `RESEARCH_SOURCE_MATRIX.md`
2. **User-Assistant Bias in LLMs**
3. **Multi-User Large Language Model Agents**
4. **OP-Bench**
5. **Locating and Controlling Implicit Personalization in Large Language Models**
6. **Who's Asking? User Personas and the Mechanics of Latent Misalignment**
7. **Prompt Injection as Role Confusion**
8. **No Attacker Needed: Unintentional Cross-User Contamination**
9. **Preference Heads** and **When Personalization Legitimizes Risks** only if the mechanistic/safety comparison becomes central
10. Remaining sources only when needed to resolve a specific alternative hypothesis

The goal is to spend Max reasoning on **scientific synthesis**, not indiscriminate literature ingestion.


## Repository roots

```text
D:\AI\Research\dynamic_user_models\research_sources\
├── papers\
└── repos\
```

All paths below are relative to `research_sources/`.

## Verification rules used here

- **RECOVERED GIT CLONE** means the uploaded `repos.rar` contains a real `.git/config` for that repository, not merely an empty directory or copied files.
- **PAPER ONLY** means the PDF is present locally but no matching Git clone was recovered in `repos.rar`.
- **PLACEHOLDER ONLY** means a local repo-side folder exists but does not contain a Git clone or usable repository contents.
- Paper-to-repository mappings were checked against repository names/file trees and, where available, the official code link or paper title exposed by the paper/project page.
- Do **not** infer paper/repo pairings from outer folder names alone. There is at least one misleading local folder name: `repos/what_kind_of_user_are_you/` actually contains the TalkTuner repository for *Designing a Dashboard for Transparency and Control of Conversational AI*.

## Verified recovered Git repositories

| Paper | Local repository | GitHub | Verification |
|---|---|---|---|
| Implicit Personalization in Language Models: A Systematic Study | `repos/implicit_personalization_in_llms/code/IP/` | https://github.com/jiarui-liu/IP | **RECOVERED GIT CLONE** — `.git/config` present; repo contains `case_1/`, `case_2/`, `case_3/`, `vllm/` |
| Stereotype or Personalization? User Identity Biases Chatbot Recommendations | `repos/llm-stereotype-or-personalization/` | https://github.com/AnjaliRuban/llm-stereotype-or-personalization | **RECOVERED GIT CLONE** — `.git/config` present; repo contains `prompts/`, `src/`, `plotting/` |
| Multi-User Large Language Model Agents | `repos/Multi-User-LLM-Agent/` | https://github.com/Kordi-Lab/Multi-User-LLM-Agent | **RECOVERED GIT CLONE** — `.git/config` present; repo contains `muses_bench/`, `data/`, `multiuser_llm_training/` |
| One Persona, Many Cues, Different Results: How Sociodemographic Cues Impact LLM Personalization | `repos/one_persona_many_cues/code/persona_cues/` | https://github.com/frawee/persona_cues | **RECOVERED GIT CLONE** — `.git/config` present; repo contains generation/evaluation pipeline |
| Preference Heads in Large Language Models: A Mechanistic Framework for Interpretable Personalization | `repos/preference_heads/code/DPS/` | https://github.com/weixuzhang/DPS | **RECOVERED GIT CLONE** — `.git/config` present; repo contains preference-head detection and DPS steering code |
| Prompt Injection as Role Confusion | `repos/prompt_injection_as_role_confusion/code/prompt-injection-as-role-confusion/` | https://github.com/role-confusion/prompt-injection-as-role-confusion | **RECOVERED GIT CLONE** — `.git/config` present; repo contains role probes, demos, experiments, and utilities |
| When Personalization Legitimizes Risks: Uncovering Safety Vulnerabilities in Personalized Dialogue Agents | `repos/PS-Bench/` | https://github.com/MuyuenLP/PS-Bench | **RECOVERED GIT CLONE** — `.git/config` present; **PS-Bench belongs to this paper, not OP-Bench** |
| User-Assistant Bias in LLMs | `repos/user_assistant_bias/Code/userassist/` | https://github.com/jingxuanf0214/userassist | **RECOVERED GIT CLONE** — `.git/config` present; local datasets are also stored under `repos/user_assistant_bias/Datasets/` |
| Designing a Dashboard for Transparency and Control of Conversational AI (TalkTuner) | `repos/what_kind_of_user_are_you/code/TalkTuner-chatbot-llm-dashboard/` | https://github.com/yc015/TalkTuner-chatbot-llm-dashboard | **RECOVERED GIT CLONE** — `.git/config` present; local outer folder name is misleading |

### Important non-recovered repo case

`repos/when_personalization_misleads/code/` exists in the archive, but it contains no files and no `.git/config`. Treat it as **PLACEHOLDER ONLY**, not as a successfully retrieved repository.

---

# Main Source Matrix

| Source | Local paper path | Local code / status | Directly establishes | Does NOT establish | Why relevant to dynamic user models / routing |
|---|---|---|---|---|---|
| **OP-Bench: Benchmarking Over-Personalization for Memory-Augmented Personalized Conversational Agents** | `papers/benchmarking_over_personalization_for_memory_augmented_personalized_conversational_agents/benchmarking_over_personalization_for_memory_augmented_personalized_conversational_agents.pdf` | **PAPER ONLY.** Do **not** map this to `repos/PS-Bench/`; PS-Bench is a different paper. | Formalizes **over-personalization** in memory-augmented agents as Irrelevance, Repetition, and Sycophancy; shows memory can be retrieved/applied when it is contextually unnecessary; proposes Self-ReCheck memory filtering. | Does not establish cross-user identity binding, a token-level person-routing mechanism, or a dedicated circuit for deciding *whose* memory applies. | Strong evidence that personalization needs a **relevance/scope gate**, not merely better memory recall. Useful as a behavioral failure mode when user information is valid but should not control the current answer. |
| **Designing a Dashboard for Transparency and Control of Conversational AI (TalkTuner)** | `papers/designing_a_dashboard_for_transparency_and_control_of_conversational_ai/designing_a_dashboard_for_transparency_and_control_of_conversational_ai.pdf` | `repos/what_kind_of_user_are_you/code/TalkTuner-chatbot-llm-dashboard/` — https://github.com/yc015/TalkTuner-chatbot-llm-dashboard | Shows that user attributes such as age, gender, education, and socioeconomic status can be decoded from internal states; demonstrates a dashboard that exposes and intervenes on the inferred user model. | Decodability alone does not prove a dedicated causal person-binding circuit; does not isolate actual-user vs third-party referent ownership or multi-user routing. | Establishes that **user-attribute information can be decoded from internal states and that interventions on related representations can alter model behavior**. Motivates separating “information is represented” from “information is correctly bound and causally used,” without assuming a single coherent latent user-model module. |
| **Implicit Personalization in Language Models: A Systematic Study** | `papers/implicit_personalization_in_llms/implicit_personalization_in_llms.pdf` | `repos/implicit_personalization_in_llms/code/IP/` — https://github.com/jiarui-liu/IP | Defines implicit personalization as inferring background from implicit cues and tailoring responses; provides an SCM-based causal framing, indirect intervention, and case studies in cultural adaptivity, education disparity, and echo chambers. | Does not isolate a reusable actual-user binding circuit; does not test multi-user ownership or distinguish same-source mentions of self vs third parties. | Foundational behavioral/causal framing for **cue -> inferred user background -> response**. Useful for defining the phenomenon before asking how the inferred background is represented or routed internally. |
| **“Kelly is a Warm Person, Joseph is a Role Model”: Gender Biases in LLM-Generated Reference Letters** | `papers/kelly_is_a_warm_person_joseph_is_a_role_model/2023.findings-emnlp.243.pdf` | **PAPER ONLY** in the uploaded corpus. | Demonstrates gender bias in LLM-generated recommendation letters through language style, lexical content, and bias in hallucinated content. | Does not establish personalization, persistent user modeling, source-role routing, or person-specific memory binding. | Useful as a **bias control / negative comparison**: output differences associated with person attributes can arise from stereotypes without implying a genuine personalized user model. |
| **Locating and Controlling Implicit Personalization in Large Language Models** | `papers/locating_and_controlling_implicit_personalization_in_llms/locating_and_controlling_implicit_personalization_in_llms.pdf` | **PAPER ONLY** in `repos.rar`. | Connects implicit demographic-cue effects to localized internal activation signals; reports strong correlations between internal signals and changed recommendations; causally suppresses cue influence by removing the signal. | Does not establish a universal person-identity binding module; selective control is model/attribute dependent; does not test cross-user ownership or same-source referent binding. | Closest direct evidence in this set that **implicit personalization has a localized, causally actionable internal representation** rather than being only a surface behavior. |
| **Multi-User Large Language Model Agents** | `papers/multi_user_llm_agents/multi_user_llm_agents.pdf` | `repos/Multi-User-LLM-Agent/` — https://github.com/Kordi-Lab/Multi-User-LLM-Agent | Formalizes LLM agents as multi-principal systems; evaluates instruction following, privacy/access control, coordination, and resource allocation across multiple users; finds systematic failures under conflicting objectives and multi-turn interaction. | Does not identify the exact hidden-state or token-level mechanism that routes statements/preferences to individual users; not a mechanistic person-binding paper. | Provides the **multi-user systems/safety motivation** for correct participant routing, authority, preference ownership, and privacy scoping. |
| **No Attacker Needed: Unintentional Cross-User Contamination in Shared-State LLM Agents** | `papers/no_attacker_needed/no_attacker_needed.pdf` | **PAPER ONLY** in the uploaded corpus. | Defines unintentional cross-user contamination (UCC): benign scope-bound information from one user persists in shared state and degrades another user's outcome; shows large contamination rates and limits of text-level sanitization. | Does not establish in-context token-level participant routing, and its primary mechanism is **persistent shared state/artifacts**, not necessarily a latent conversational person-binding circuit. | Direct safety analogue of a **wrong-person / wrong-scope** failure. Strong evidence that persistent state requires ownership metadata and artifact-level scoping across users. |
| **One Persona, Many Cues, Different Results: How Sociodemographic Cues Impact LLM Personalization** | `papers/one_persona_many_cues/one_persona_many_cues.pdf` | `repos/one_persona_many_cues/code/persona_cues/` — https://github.com/frawee/persona_cues | Shows that multiple cues intended to express the same sociodemographic persona can yield substantially different model responses; warns that single-cue persona studies are not robust enough. | Does not prove that all cue forms converge to one latent identity representation; does not establish actual-user binding or preference ownership. | Important control for **cue invariance**: a valid user model should ideally bind equivalent identity evidence consistently instead of overfitting to one surface cue. |
| **Preference Heads in Large Language Models: A Mechanistic Framework for Interpretable Personalization** | `papers/preference_heads/preference_heads.pdf` | `repos/preference_heads/code/DPS/` — https://github.com/weixuzhang/DPS | Proposes sparse **Preference Heads** whose causal contribution tracks user-specific stylistic/topical preferences; introduces Preference Contribution Score and Differential Preference Steering (DPS) to amplify personalized logits at inference time. | Does not establish person identity/ownership routing, demographic binding, cross-user scoping, or an actual-user vs third-party distinction. | Provides a concrete **mechanistic personalization substrate** and intervention template. Useful for asking whether preference-carrying heads are downstream of a separate binding/routing representation. |
| **Prompt Injection as Role Confusion** | `papers/prompt_injection_as_role_confusion/prompt_injection_as_role_confusion.pdf` | `repos/prompt_injection_as_role_confusion/code/prompt-injection-as-role-confusion/` — https://github.com/role-confusion/prompt-injection-as-role-confusion | Shows that models infer conversational/authority roles from how text is written rather than only from trusted interface provenance; role probes predict prompt-injection success; role-confused content can inherit authority. | Does not establish personal trait binding or long-term user-memory ownership; “role” here is primarily **speaker/authority role**, not demographic/person identity. | Mechanistically motivates the distinction between **source role**, **authority**, and **person identity**. A model can misassign role semantics even when interface metadata says otherwise. |
| **Stereotype or Personalization? User Identity Biases Chatbot Recommendations** | `papers/stereotype_or_personalization/2025.findings-acl.1254.pdf` | `repos/llm-stereotype-or-personalization/` — https://github.com/AnjaliRuban/llm-stereotype-or-personalization | Demonstrates that explicit and implicit racial identity cues significantly alter recommendations and that models can obscure/deny the role of identity in those outputs. | Does not cleanly distinguish beneficial personalization from stereotype-driven bias mechanistically; does not establish actual-user vs third-party binding or cross-user memory ownership. | Key evidence that **identity information can silently influence recommendations** and that surface explanations may not reveal that influence. Motivates causal rather than self-report auditing. |
| **User-Assistant Bias in LLMs** | `papers/user_assistant_bias_in_llms/user_assistant_bias_in_llms.pdf` | `repos/user_assistant_bias/Code/userassist/` — https://github.com/jingxuanf0214/userassist; datasets under `repos/user_assistant_bias/Datasets/` | Isolates a systematic tendency to favor information based on whether it came from the user or assistant in controlled multi-turn conflicts; shows the bias can be shifted by post-training and generalizes beyond the minimal synthetic setup. | Does not establish which *person* a same-role statement refers to; source-role preference is not the same thing as actual-user/third-party referent binding. | Strongest source-role control in the corpus. Helps separate **who authored the message** from **who the message is about**, preventing source bias from being mistaken for person binding. |
| **When Personalization Legitimizes Risks: Uncovering Safety Vulnerabilities in Personalized Dialogue Agents** | `papers/when_personalization_leegitimizes_risks/when_personalization_leegitimizes_risks.pdf` | `repos/PS-Bench/` — https://github.com/MuyuenLP/PS-Bench | Introduces **intent legitimation**: benign personal memories can bias interpretation of an inherently harmful request and increase unsafe compliance; PS-Bench quantifies the effect and the paper reports representation-space evidence plus a detection/reflection mitigation. | Does not establish cross-user identity binding; the main failure is same-user memory influencing safety interpretation, not another person's memory being assigned to the user. | Shows that personalization changes **intent inference and safety behavior**, so user models can interact with policy layers rather than merely style/content preference. |
| **When Personalization Misleads: Understanding and Mitigating Hallucinations in Personalized LLMs** | `papers/when_personalization_misleads/when_personalization_misleads.pdf` | `repos/when_personalization_misleads/code/` is **PLACEHOLDER ONLY** — no recovered Git clone. | Shows personalization-induced hallucination: prior user history can pull factual answers toward user-consistent but false content; attributes the failure to entanglement between personalization and factual representations; proposes FPPS and PFQABench. | Does not establish cross-user routing, participant ownership, or user-vs-assistant source bias. | Demonstrates a core requirement for dynamic user models: personalization should be **selectively suppressible when objective factual truth should dominate**. |
| **Who's Asking? User Personas and the Mechanics of Latent Misalignment** | `papers/whos-asking-user-personas-and-the-mechanics-of-latent-misalignment-Paper-Conference/NeurIPS-2024-whos-asking-user-personas-and-the-mechanics-of-latent-misalignment-Paper-Conference.pdf` | **PAPER ONLY** in the uploaded corpus. Do not map it to `repos/what_kind_of_user_are_you/`; that folder actually contains TalkTuner. | Shows that perceived **user persona** strongly affects refusal/safety behavior; harmful content can remain latent in earlier layers; activation steering of persona can bypass safeguards more effectively than direct refusal steering; persona changes can alter interpretation of dangerous queries. | Does not establish ordinary personalization correctness, multi-user memory scoping, or a stable person-binding/ownership mechanism. | Strong mechanistic evidence that the model's representation of **who it thinks the user is** can causally alter downstream interpretation and policy behavior. |

---

# Detailed Codex Reading Order (After Priority Pass)

For this project, do not read the sources as if they all answer the same question. They cover different layers of the problem.

1. **Behavioral definition of implicit personalization**
   - `papers/implicit_personalization_in_llms/...pdf`
   - `repos/implicit_personalization_in_llms/code/IP/README.md`
   - Then inspect `case_1/`, `case_2/`, and `case_3/` to see the three operationalizations.

2. **Evidence that a latent user model is decodable / controllable**
   - `papers/designing_a_dashboard_for_transparency_and_control_of_conversational_ai/...pdf`
   - `repos/what_kind_of_user_are_you/code/TalkTuner-chatbot-llm-dashboard/README.md`
   - High-value files: `src/probes.py`, `src/intervention_utils.py`, `src/dataset.py`.

3. **Mechanistic personalization candidates**
   - `papers/preference_heads/preference_heads.pdf`
   - `repos/preference_heads/code/DPS/README.md`
   - High-value files: `preference_head/preference_head_detection.py`, `scripts/run_weighted_dps.py`, `src/run.py`.
   - Also read `papers/locating_and_controlling_implicit_personalization_in_llms/...pdf` as a newer mechanistic comparator, but note that no matching local code repo was recovered.

4. **Source-role vs person-role controls**
   - `papers/user_assistant_bias_in_llms/user_assistant_bias_in_llms.pdf`
   - `repos/user_assistant_bias/Code/userassist/README.md`
   - High-value files: `scripts/train_dpo.py`, `scripts/train_sft.py`, `src/`.
   - Then compare with `papers/prompt_injection_as_role_confusion/...pdf` and its role-probe code.

5. **Cue robustness and stereotype controls**
   - `papers/one_persona_many_cues/one_persona_many_cues.pdf`
   - `repos/one_persona_many_cues/code/persona_cues/README.md`
   - High-value files: `get_responses.py`, `generation/`, `evaluation/eval_responses.py`.
   - `papers/stereotype_or_personalization/2025.findings-acl.1254.pdf`
   - `repos/llm-stereotype-or-personalization/README.md`
   - High-value files: `src/sampling.py`, `src/stereotype_extraction.py`, `prompts/`.
   - Use the *Kelly* paper as a non-personalization bias comparator.

6. **Multi-user ownership / scoping failures**
   - `papers/multi_user_llm_agents/multi_user_llm_agents.pdf`
   - `repos/Multi-User-LLM-Agent/README.md`
   - High-value paths: `muses_bench/`, `data/scenarios/`, `run.py`.
   - `papers/no_attacker_needed/no_attacker_needed.pdf` for persistent cross-user state contamination.

7. **When personalization is contextually wrong or unsafe**
   - OP-Bench: over-personalization / irrelevant memory use.
   - PS-Bench / *When Personalization Legitimizes Risks*: safety intent legitimation.
   - *When Personalization Misleads*: factual distortion.
   - These are three distinct failure classes and should not be collapsed into a single “personalization failure” label.

8. **Persona-sensitive safety as a mechanistic endpoint**
   - `papers/whos-asking-user-personas-and-the-mechanics-of-latent-misalignment-Paper-Conference/...pdf`
   - Compare its persona steering results with TalkTuner, Preference Heads, and Prompt Injection as Role Confusion.

---

# Repository Parsing Notes

## `repos/implicit_personalization_in_llms/code/IP/`

```text
README.md                  # paper mapping + reproduction overview
case_1/                    # cultural adaptivity
case_2/                    # education disparity
case_3/                    # echo-chamber tests
vllm/                      # inference setup/templates
```

Interpret this repository as **behavioral/causal measurement of implicit personalization**, not as a mechanistic circuit-discovery repo.

## `repos/what_kind_of_user_are_you/code/TalkTuner-chatbot-llm-dashboard/`

```text
README.md
src/probes.py              # decoding/probing inferred user attributes
src/intervention_utils.py  # user-model interventions
src/dataset.py
notebooks/
data/
```

Despite the outer folder name, this is **TalkTuner / Designing a Dashboard**, not *Who's Asking?*.

## `repos/preference_heads/code/DPS/`

```text
README.md
preference_head/preference_head_detection.py
preference_head/detect_cluster_heads.py
preference_head/cluster_profiles.py
scripts/run_weighted_dps.py
src/run.py
```

Interpret as **attention-head attribution + causal personalization steering**.

## `repos/prompt_injection_as_role_confusion/code/prompt-injection-as-role-confusion/`

```text
README.md
demo/role-probe-demo.ipynb
demo/cot-forgery-demo.ipynb
experiments/
utils/probes.py
utils/role_assignments.py
utils/role_templates.py
```

Interpret as **latent speaker/authority-role inference**, not as demographic-persona personalization.

## `repos/user_assistant_bias/`

```text
Code/userassist/README.md
Code/userassist/scripts/train_dpo.py
Code/userassist/scripts/train_sft.py
Code/userassist/src/
Datasets/
```

Interpret as **source-role weighting**. This is an important control against conflating “message came from user” with “statement is about the user.”

## `repos/one_persona_many_cues/code/persona_cues/`

```text
README.md
get_responses.py
get_responses_openai.py
generation/
evaluation/eval_responses.py
prep_data_demographics.ipynb
```

Interpret as **persona-cue robustness / external-validity testing**.

## `repos/llm-stereotype-or-personalization/`

```text
README.md
prompts/
src/sampling.py
src/stereotype_extraction.py
src/variables.py
plotting/
```

Interpret as **identity-cue effects on recommendations + transparency/obfuscation**, with stereotype risk as a core alternative explanation.

## `repos/Multi-User-LLM-Agent/`

```text
README.md
run.py
muses_bench/
data/scenarios/
multiuser_llm_training/
scripts/
```

Interpret as **multi-principal agent behavior and benchmark infrastructure**, not a mechanistic interpretability repository.

## `repos/PS-Bench/`

```text
readme.md
benchmarking/
evaluation/
figs/
```

This is the code for **When Personalization Legitimizes Risks**, not OP-Bench. Treat the `PS` name as “personalization safety,” not “over-personalization.”

---

# Conceptual Distinctions Codex Should Preserve

These distinctions are important when using the papers as evidence:

- **Decodable != causally used.** A probe can recover a user attribute without proving that attribute drives generation.
- **Causally used != correctly bound.** A representation may affect output while still being assigned to the wrong person or scope.
- **Source role != referent identity.** “The user said X” and “X is about the user” are different relations.
- **Persona != memory ownership.** A persona effect can exist without persistent memory, and persistent memory can be mis-scoped without an explicit persona representation.
- **Stereotype != personalization.** Demographic response differences may reflect learned group stereotypes rather than user-specific adaptation.
- **Over-personalization != cross-user contamination.** OP-Bench concerns using valid personal memory when it is irrelevant; UCC concerns using another user's scope-bound state.
- **Persistent-state routing != in-context routing.** Shared memory/artifact failures do not by themselves prove the same mechanism governs person references inside a single prompt.
- **Safety-role confusion != demographic binding.** Prompt Injection as Role Confusion studies speaker/authority inference; it is mechanistically suggestive but not equivalent to user-persona binding.
- **Preference heads != identity heads.** A head that carries preference information need not encode who owns that preference.

---

# Local Corpus Inventory

## Papers present

```text
papers/benchmarking_over_personalization_for_memory_augmented_personalized_conversational_agents/
papers/designing_a_dashboard_for_transparency_and_control_of_conversational_ai/
papers/implicit_personalization_in_llms/
papers/kelly_is_a_warm_person_joseph_is_a_role_model/
papers/locating_and_controlling_implicit_personalization_in_llms/
papers/multi_user_llm_agents/
papers/no_attacker_needed/
papers/one_persona_many_cues/
papers/preference_heads/
papers/prompt_injection_as_role_confusion/
papers/stereotype_or_personalization/
papers/user_assistant_bias_in_llms/
papers/when_personalization_leegitimizes_risks/
papers/when_personalization_misleads/
papers/whos-asking-user-personas-and-the-mechanics-of-latent-misalignment-Paper-Conference/
```

## Repo-side folders present

```text
repos/implicit_personalization_in_llms/
repos/llm-stereotype-or-personalization/
repos/Multi-User-LLM-Agent/
repos/one_persona_many_cues/
repos/preference_heads/
repos/prompt_injection_as_role_confusion/
repos/PS-Bench/
repos/user_assistant_bias/
repos/what_kind_of_user_are_you/
repos/when_personalization_misleads/    # placeholder only; no recovered clone
```

## Recovered-clone count

**9 actual Git clones** were detected by the presence of `.git/config` in `repos.rar`.

---

# Paper / Code URLs

These URLs are included so Codex can cross-check provenance, but the **local retrieval status above is authoritative for what exists in this corpus**.

| Source | Paper | Code |
|---|---|---|
| OP-Bench | https://arxiv.org/abs/2601.13722 | No matching recovered repo in this corpus |
| Designing a Dashboard / TalkTuner | https://arxiv.org/abs/2406.07882 | https://github.com/yc015/TalkTuner-chatbot-llm-dashboard |
| Implicit Personalization in Language Models | https://arxiv.org/abs/2405.14808 | https://github.com/jiarui-liu/IP |
| Kelly is a Warm Person... | https://arxiv.org/abs/2310.09219 | Official external code exists, but it was **not retrieved** into this corpus |
| Locating and Controlling Implicit Personalization | https://arxiv.org/abs/2608.11735 | No matching recovered repo in this corpus |
| Multi-User Large Language Model Agents | https://arxiv.org/abs/2604.08567 | https://github.com/Kordi-Lab/Multi-User-LLM-Agent |
| No Attacker Needed | https://arxiv.org/abs/2604.01350 | No matching recovered repo in this corpus |
| One Persona, Many Cues | https://arxiv.org/abs/2601.18572 | https://github.com/frawee/persona_cues |
| Preference Heads | https://arxiv.org/abs/2604.22345 | https://github.com/weixuzhang/DPS |
| Prompt Injection as Role Confusion | https://arxiv.org/abs/2603.12277 | https://github.com/role-confusion/prompt-injection-as-role-confusion |
| Stereotype or Personalization? | https://arxiv.org/abs/2410.05613 | https://github.com/AnjaliRuban/llm-stereotype-or-personalization |
| User-Assistant Bias in LLMs | https://arxiv.org/abs/2508.15815 | https://github.com/jingxuanf0214/userassist |
| When Personalization Legitimizes Risks | https://arxiv.org/abs/2601.17887 | https://github.com/MuyuenLP/PS-Bench |
| When Personalization Misleads | https://arxiv.org/abs/2601.11000 | Local repo folder is empty / not actually retrieved |
| Who's Asking? | https://arxiv.org/abs/2406.12094 | No matching recovered repo in this corpus |

---

# Suggested instruction for Codex

You can prepend the following when asking Codex to work across this source tree:

```text
Treat RESEARCH_SOURCE_MATRIX.md as the provenance/evidence map for research_sources/.
Do not infer paper-to-code mappings from folder names alone.
Only treat a repository as locally retrieved when the matrix marks it RECOVERED GIT CLONE.
When citing a paper as evidence, preserve the distinction between:
(1) decodability,
(2) causal influence,
(3) source-role effects,
(4) person/referent binding,
(5) memory ownership/scope,
(6) multi-user persistent-state contamination,
(7) stereotype-driven demographic effects,
and (8) safety-policy effects.
Do not claim that one of these establishes another unless the source directly tests that link.
When inspecting a recovered repo, start with its README and the high-value files listed in this matrix before recursively reading the full tree.

Treat the following as the project's highest-value unresolved distinctions:
(1) actual conversational user vs third-party referent under matched source role,
(2) correct person-specific routing vs cross-participant leakage,
(3) explicitly retrievable vs spontaneously behaviorally operative information,
(4) relevant vs irrelevant use of the same person-specific fact,
and (5) semantic/referential binding vs structural, positional, lexical, or chat-template pseudo-binding.

These are gaps in the LOCAL INSPECTED CORPUS, not claims of global literature novelty.

A clean U→U / R→R routing result is not automatically a novel mechanistic contribution.
Ask what additional asymmetry, leakage, relevance dissociation, role dependence, structural failure,
or model-family divergence would make the routing scientifically nontrivial.
```
