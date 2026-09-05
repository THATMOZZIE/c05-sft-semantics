# Lane B: Transluce ecosystem audit and behavior-first project seeds

**Snapshot date:** 2026-08-23  
**Lane scope:** the current official Transluce Hugging Face organization, its two collections, all 14 models, all 11 datasets, linked first-party research/code, and recent release activity.  
**Candidate output:** four unranked, genuinely distinct projects. This lane does **not** select a winner.

## Evidence labels and scope controls

- **[FACT]** is directly supported by a first-party Transluce page, Hugging Face repository/API/card, linked official GitHub repository, or the primary paper.
- **[INFERENCE]** is my feasibility or scientific interpretation of those facts.
- **[SPECULATION]** is a proposed opportunity or hypothesis that has not been tested here.
- Inventory tables are **[FACT]** unless a cell explicitly says otherwise.
- I did not inspect old notebooks, inspect any blinded Notebook 09 values, run model inference, fine-tune anything, or download a checkpoint/activation archive.
- I did not reopen participant-owner binding, alias/code binding, or the prior social-history branch. The user-model candidates below concern measurement validity or out-of-distribution behavioral control, not owner identity.
- Following the 2026-08-23 criteria update, effort is a graded dimension rather than a hard exclusion at 20 hours. I still report time to first result, a useful first-20-hour path, and a realistic full effort range.

The frozen schema and admission rule are in [`00_execution_plan.md`](./00_execution_plan.md). The ecosystem emphasis comes from sections 23 and 39 of [`CODEX_BEHAVIOR_FIRST_RESEARCH_DIRECTION_BRIEF_V3.md`](../CODEX_BEHAVIOR_FIRST_RESEARCH_DIRECTION_BRIEF_V3.md).

## Bottom-line lane findings (not a ranking)

1. **[FACT] The official organization currently contains exactly 14 public, ungated Transluce model repositories, 11 public datasets, and two collections.** The only Hugging Face dataset created in July/August 2026 is WeirdChat. The only July/August code activity among the linked research repositories is WeirdChat work through August 21 and an input-ablation learning-rate correction on July 7.
2. **[FACT] The richest cheap substrates are cached outputs, not cached activations.** WeirdChat contains 173,184 judged rollouts; SynthSys contains subject completions and judge probability vectors; SelfDescribe contains filtered labels/probabilities; PRISM contains conversations plus revealed/ground-truth labels; the input-ablation datasets contain target outputs with and without hints; the activation-patching datasets contain original/patched continuations and the intervention vectors themselves.
3. **[FACT] Some activation resources do exist off-Hub.** The introspective-interp repository links compressed FineWeb full-activation and activation-difference archives of 180.5 MB and 152.2 MB. The user-modeling repository links a 9.43 GB `latentqa.tar.gz` archive described as checkpoints and evaluation results. None was downloaded here.
4. **[FACT] The strongest published gap inside the user-representation work is a read/control dissociation.** General LatentQA data can read SelfDescribe nearly perfectly yet controls worse; unfiltered SynthSys worsens reading while leaving control/alignment almost unchanged; middle-layer and KV decoders read well but control poorly. This is a real observed substrate, not a proposed failure mode.
5. **[FACT] The strongest published gap inside the intervention-explainer work is weak marginal dependence on the intervention input.** On activation patching, removing the continuous activation vector reduces exact match only from 64.0 to 59.9 for Qwen and 48.6 to 45.2 for Llama; removing layer or token annotations has negligible effect. This makes a matched vector-permutation test decision-relevant.
6. **[INFERENCE] A 12 GB GPU is adequate for dataset-only first tests but not for the authors' documented BF16 workflows.** Every full 8B Transluce checkpoint is about 16.1-16.4 GB on disk. Quantized single-model inference is plausible; dual target/explainer workflows plus large adapters/custom continuous-token code are borderline or likely to need CPU offload or a larger/rented GPU. Quantized compatibility is not documented by Transluce.
7. **[INFERENCE] WeirdChat should remain in Lane A.** It is inventoried here because it is the only July/August addition, but duplicating its behavior search would violate lane separation. No WeirdChat wording variant is counted among this lane's four candidates.

## Current Hugging Face organization inventory

Primary organization: [Transluce on Hugging Face](https://huggingface.co/Transluce).  
Direct inventory endpoints used mechanically: [models](https://huggingface.co/api/models?author=Transluce&limit=200&full=true) and [datasets](https://huggingface.co/api/datasets?author=Transluce&limit=200&full=true).

### Collections (2/2)

| Collection | Current members | What it establishes | Last material release activity |
|---|---:|---|---|
| [Scalably Extracting Latent Representations of Users](https://huggingface.co/collections/Transluce/scalably-extracting-latent-representations-of-users) | 10: six datasets and four 8B LoRA decoder repositories | Released behavioral datasets, four Llama-3.1-8B-Instruct LatentQA decoders, and configs for all-to-all versus 15-to-0 and held-out versus no-held-out training | Models added/collection updated 2026-03-09; linked code and a 9.43 GB result archive released 2026-03-16 |
| [Training Language Models To Explain Their Own Computations](https://huggingface.co/collections/Transluce/training-language-models-to-explain-their-own-computations) | 12: four datasets and eight models | Feature-description, activation-patching, and input-ablation explainer resources for Llama-3.1-8B/Qwen3-8B | Hub artifacts last updated 2026-01-03; primary paper v3 on 2026-02-09; input-ablation configs corrected 2026-07-07 |

The two 2024 `llama_8b_explainer` / `llama_8b_simulator` models and WeirdChat are outside these collections.

### Datasets (11/11)

Sizes below are repository manifest/download sizes, not decoded in-memory size. Current row counts were checked through Hugging Face's dataset server where available.

| Dataset | Created / last modified | Current released contents | Manifest size | Card / linked source quality |
|---|---|---|---:|---|
| [WeirdChat](https://huggingface.co/datasets/Transluce/WeirdChat) | 2026-07-19 / 2026-08-12 | 1,361 patterns; 2,661 prompts; 173,184 judged transcripts; 486,486 pairwise judgments; 21 rubrics; 217 search-compute rows; six subject-model families | 232.93 MB | Detailed card, [research page](https://transluce.org/weirdchat), [code](https://github.com/TransluceAI/WeirdChat), schemas, and changelog |
| [act_patch_qwen3_8b_counterfact](https://huggingface.co/datasets/Transluce/act_patch_qwen3_8b_counterfact) | 2025-12-17 / 2026-01-03 | 120,644 train + 14,357 test rows; token/layer metadata, 4,096-d intervention vectors, original and patched continuations, CounterFact targets | 911.40 MB compressed; card reports 2.318 GB decoded | Detailed schema/card; [paper](https://arxiv.org/abs/2511.08579); [code](https://github.com/TransluceAI/introspective-interp) |
| [act_patch_llama_3.1_8b_counterfact](https://huggingface.co/datasets/Transluce/act_patch_llama_3.1_8b_counterfact) | 2025-12-17 / 2026-01-03 | 13,454 train + 5,600 test + 107,130 overlapping `train_full` rows; same intervention/output schema | 837.20 MB compressed; card reports 2.147 GB decoded across listed splits | Detailed schema/card; same paper/code |
| [input_ablation_qwen3_8b_mmlu_hint](https://huggingface.co/datasets/Transluce/input_ablation_qwen3_8b_mmlu_hint) | 2025-12-17 / 2026-01-03 | 12,642 train + 1,400 test; MMLU question/choices, random hint, hinted and zero-shot predictions, hint-token IDs, fully rendered training prompt | 22.15 MB | Detailed schema/card; same paper/code |
| [input_ablation_llama_3.1_8b_instruct_mmlu_hint](https://huggingface.co/datasets/Transluce/input_ablation_llama_3.1_8b_instruct_mmlu_hint) | 2025-12-17 / 2026-01-03 | 12,642 train + 1,400 test; corresponding Llama target outputs and prompts | 22.63 MB | Narrative card but no declared feature schema; viewer/API supplies it; same paper/code |
| [PRISM-gender-Llama-3.1-8B-Instruct](https://huggingface.co/datasets/Transluce/PRISM-gender-Llama-3.1-8B-Instruct) | 2025-12-26 / 2025-12-26 | 5,041 real PRISM conversations with `attr` (revealed gender), `gt_attr`, and tag | 14.21 MB | Card is only an MIT stub; substantive definition is on the [user-modeling page](https://transluce.org/user-modeling) and in [code](https://github.com/TransluceAI/observatory/tree/main/project/user_modeling) |
| [SelfDescribe-Llama-3.1-8B-Instruct](https://huggingface.co/datasets/Transluce/SelfDescribe-Llama-3.1-8B-Instruct) | 2025-12-26 / 2025-12-26 | 2,666 filtered implicit self-descriptions with attribute/value and `pred_prob` | 0.954 MB | MIT-only card; substantive source as above |
| [SelfDescribe-Llama-3.1-70B-Instruct](https://huggingface.co/datasets/Transluce/SelfDescribe-Llama-3.1-70B-Instruct) | 2025-12-26 / 2025-12-26 | 2,585 corresponding 70B positives | 0.931 MB | MIT-only card; substantive source as above |
| [SynthSys-Llama-3.1-8B-Instruct](https://huggingface.co/datasets/Transluce/SynthSys-Llama-3.1-8B-Instruct) | 2025-12-26 / 2025-12-26 | Current Hub: 80,488 train + 50,807 test; system/user prompts, two cached subject completions, judge probability vectors | 381.67 MB | MIT-only card; substantive source as above |
| [SynthSys-Llama-3.1-70B-Instruct](https://huggingface.co/datasets/Transluce/SynthSys-Llama-3.1-70B-Instruct) | 2025-12-26 / 2025-12-26 | Current Hub: 109,515 train + 48,703 test; same cached fields | 469.89 MB | MIT-only card; substantive source as above |
| [SynthSysPre](https://huggingface.co/datasets/Transluce/SynthSysPre) | 2025-12-26 / 2025-12-26 | Model-agnostic system and user prompt pools; 30.0 MB and 37.5 MB JSONL files | 67.51 MB | MIT-only card; **current viewer fails with a column mismatch** because the two JSONL files have different schemas |

Important dataset qualifications:

- **[FACT]** The user-modeling article says SynthSys(8B) and SynthSys(70B) contain 78,964 and 109,514 examples. The current Hub files instead expose 131,295 and 158,218 total train+test rows (80,488/50,807 and 109,515/48,703). There is no card changelog explaining the 8B discrepancy or whether the article's totals refer only to a historical/pre-QA-filter subset. Treat the current Hub split counts and the article counts as different source facts, not interchangeable numbers.
- **[FACT]** The input-ablation paper's changed/unchanged test counts sum to 1,395 for each target, while each current test split has 1,400 rows. The paper does not explain the five-row difference in the table.
- **[FACT]** The activation-patching Llama `train` split is a subset/alternative to `train_full`; summing all three displayed splits would double-count training examples.
- **[FACT]** No user-model dataset contains activations. SynthSys contains completions/probabilities; SelfDescribe contains a filtered probability; PRISM contains labels and conversations. Activations/checkpoints/evaluation outputs are linked separately through the 9.43 GB S3 archive.

### Models (14/14)

All 14 Transluce repositories report `private=false` and `gated=false`. “Public” below describes the Transluce repository. A derived model may still require a base tokenizer/model or license acceptance in the documented workflow.

| Model repository | Created / last modified | Artifact type and weight size | Target / base | Card and practical qualification |
|---|---|---|---|---|
| [llama_8b_explainer](https://huggingface.co/Transluce/llama_8b_explainer) | 2024-10-31 / 2024-10-31 | Full checkpoint, 16.07 GB | Llama-3.1-8B-Instruct neuron-description generator | Card is MIT-only; substantive source is [Scaling Automatic Neuron Description](https://transluce.org/neuron-descriptions) and [observatory](https://github.com/TransluceAI/observatory) |
| [llama_8b_simulator](https://huggingface.co/Transluce/llama_8b_simulator) | 2024-10-31 / 2024-10-31 | Full checkpoint, 16.07 GB | Llama-3.1-8B-Instruct neuron-activation simulator | MIT-only card; same source |
| [features_explain_llama3.1_8b_llama3.1_8b](https://huggingface.co/Transluce/features_explain_llama3.1_8b_llama3.1_8b) | 2025-12-17 / 2026-01-03 | Full checkpoint, 16.06 GB | Llama-3.1-8B explains its own residual features | Detailed card; custom continuous-token class required |
| [features_explain_llama3.1_8b_llama3.1_8b_instruct](https://huggingface.co/Transluce/features_explain_llama3.1_8b_llama3.1_8b_instruct) | 2025-12-05 / 2026-01-03 | Full checkpoint, 16.06 GB | Llama-3.1-8B-Instruct explains Llama-3.1-8B | Detailed card; custom continuous-token class required |
| [features_explain_llama3.1_8b_llama3_8b](https://huggingface.co/Transluce/features_explain_llama3.1_8b_llama3_8b) | 2025-12-17 / 2026-01-03 | Full checkpoint, 16.06 GB | Llama-3-8B explains Llama-3.1-8B | Detailed card; custom continuous-token class; usage snippet contains a repository-name typo |
| [features_explain_llama3.1_8b_simulator](https://huggingface.co/Transluce/features_explain_llama3.1_8b_simulator) | 2025-12-17 / 2025-12-22 | Full checkpoint, 16.06 GB | Scores descriptions of Llama-3.1-8B features via token-level activation correlation | Detailed card; custom simulator wrapper required |
| [act_patch_qwen3_8b_qwen3_8b](https://huggingface.co/Transluce/act_patch_qwen3_8b_qwen3_8b) | 2025-12-17 / 2026-01-03 | PEFT/LoRA adapter, 3.886 GB | Qwen3-8B explains Qwen3-8B patch outcomes | Detailed card; base Qwen checkpoint plus custom continuous-token code needed |
| [act_patch_llama3.1_8b_llama3.1_8b](https://huggingface.co/Transluce/act_patch_llama3.1_8b_llama3.1_8b) | 2025-12-17 / 2026-01-03 | PEFT/LoRA adapter, 3.444 GB | Llama-3.1-8B explains its own patch outcomes | Detailed card; documented base is Meta Llama-3.1-8B |
| [input_ablation_qwen3_8b_qwen3_8b_hint](https://huggingface.co/Transluce/input_ablation_qwen3_8b_qwen3_8b_hint) | 2025-12-21 / 2026-01-03 | Full checkpoint, 16.40 GB | Qwen3-8B predicts its own no-hint answer | Detailed but contains a Llama target copy error and a model-ID typo in usage |
| [input_ablation_llama3.1_8b_instruct_llama3.1_8b_instruct](https://huggingface.co/Transluce/input_ablation_llama3.1_8b_instruct_llama3.1_8b_instruct) | 2025-12-21 / 2026-01-03 | Full checkpoint, 16.08 GB | Llama-3.1-8B-Instruct predicts its own no-hint answer | Detailed card; standard Transformers checkpoint, but evaluation loads a separate target |
| [all_to_all](https://huggingface.co/Transluce/all_to_all) | 2026-03-01 / 2026-03-09 | LoRA adapter, 1.227 GB (1.236 GB repository) | Llama-3.1-8B-Instruct LatentQA, all residual layers mapped to matching decoder layers; held-out attributes excluded | MIT-only card; released YAML/config are the documentation |
| [15_to_0](https://huggingface.co/Transluce/15_to_0) | 2026-03-09 / 2026-03-09 | LoRA adapter, 1.227 GB | Llama-3.1-8B-Instruct LatentQA, subject layer 15 to decoder layer 0; held-out attributes excluded | MIT-only card; released YAML/config are the documentation |
| [all_to_all_noheldout](https://huggingface.co/Transluce/all_to_all_noheldout) | 2026-03-01 / 2026-03-09 | LoRA adapter, 1.227 GB | Same all-to-all architecture trained on `train_full.pkl` including the held-out attributes | MIT-only card; name is easy to misread: “noheldout” means no attributes withheld from training |
| [15_to_0_noheldout](https://huggingface.co/Transluce/15_to_0_noheldout) | 2026-03-01 / 2026-03-09 | LoRA adapter, 1.227 GB | Same 15-to-0 architecture trained on `train_full.pkl` | MIT-only card; released YAML/config are the documentation |

Local 12 GB implications:

- **[FACT]** Every full checkpoint above is larger than 16 GB, and every provided usage example uses BF16 or an ordinary full-precision load. Therefore none fits wholly in 12 GB VRAM as documented.
- **[INFERENCE]** A single 8B model should usually fit with 4-bit quantization, but Transluce does not document quantization for its custom continuous-token models. This is a preflight question, not an established capability.
- **[INFERENCE]** Input-ablation evaluation likely needs both the fine-tuned explainer and an unmodified target; activation patching and LatentQA definitely couple target and explainer/decoder computations. Two quantized 8B instances plus a 1.2-3.9 GB adapter and runtime overhead are borderline or above 12 GB. CPU offload, serialized evaluation, weight sharing changes, or a larger GPU may be needed.
- **[FACT]** The user-modeling article used one H100 to train the 8B decoders; the introspective-interp README says its published training arguments were configured for two 80 GB H100s, while noting smaller batch sizes can reduce memory. These are training facts, not minimum inference requirements.

## Linked code, cached resources, and recent activity

### First-party code repositories

| Repository | What is available | Current activity fact | Reproduction qualification |
|---|---|---|---|
| [TransluceAI/WeirdChat](https://github.com/TransluceAI/WeirdChat) | MIT code, schemas, judging/search workflow, pipeline prompts | Created 2026-07-20; commits on 2026-08-12 for v1.0.1 and on 2026-08-21 adding evolution prompt templates | Active and small; Lane A owns scientific triage |
| [TransluceAI/observatory](https://github.com/TransluceAI/observatory) | User-model dataset generation, LatentQA train/read/steer/circuit evaluation, older neuron-description/monitor code | User-modeling and LatentQA added 2026-03-16; no later code push as of snapshot | Requires the repository's `luce` environment; user data generation additionally assumes API keys and vLLM |
| [TransluceAI/introspective-interp](https://github.com/TransluceAI/introspective-interp) | Training/evaluation for feature descriptions, activation patching, input ablation; continuous Llama/Qwen classes and configs | Last pushed 2026-07-07; all input-ablation learning rates changed from `5e-5` to `1e-5` | README says configs target two 80 GB H100s; current configs post-date January Hub checkpoints, so exact checkpoint-training hyperparameters need confirmation |

### Linked non-Hub archives (HEAD-only inspection)

| Resource | First-party description | Compressed size / last modified | Cached outputs or activations? |
|---|---|---:|---|
| [`latentqa.tar.gz`](https://transluce-public.s3.amazonaws.com/user-modeling/latentqa.tar.gz) | Observatory README: checkpoints and evaluation results used to reproduce user-modeling plots; also all 8B training/eval data | 9.43 GB; 2026-03-15 | **[FACT]** evaluation results/checkpoints are claimed; archive contents were not listed/downloaded here, so whether raw activations are included is uncertain |
| [`SAE_feature_explanations_llama3.1_8b.tar.gz`](https://transluce-public.s3.amazonaws.com/introspective-interp/SAE_feature_explanations_llama3.1_8b.tar.gz) | Training + in-distribution feature-description data | 26.92 GB; 2025-12-18 | Cached feature/explanation training data; too large for a cheap first test |
| [`fineweb...acts_grads...tar.gz`](https://transluce-public.s3.amazonaws.com/introspective-interp/fineweb_llama_3.1_8b_95seqlen_fineweb_acts_grads_-1.0.tar.gz) | OOD full-activation evaluation data | 180.53 MB; 2025-12-18 | **Yes: cached full activations/gradients** |
| [`fineweb...activation_difference.tar.gz`](https://transluce-public.s3.amazonaws.com/introspective-interp/fineweb_llama_3.1_8b_95seqlen_counterfact_subsampled_2000_activation_difference.tar.gz) | OOD CounterFact activation-difference evaluation data | 152.17 MB; 2025-12-18 | **Yes: cached activation differences** |

### July/August 2026 delta

- **[FACT] WeirdChat v1.0.0** was released 2026-07-21 with 1,388 patterns and 177,408 transcripts.
- **[FACT] WeirdChat v1.0.1** was committed to the Hub 2026-08-12 and removed 27 patterns, 66 prompts, and 4,224 transcripts that an automated review flagged as likely false positives. Current totals are 1,361 patterns and 173,184 transcripts.
- **[FACT] WeirdChat code** added evolution prompt templates on 2026-08-21, after the v1.0.1 dataset update.
- **[FACT] introspective-interp code** changed all input-ablation configuration learning rates from `5e-5` to `1e-5` on 2026-07-07. The relevant Hub models were last modified 2026-01-03. It is unknown from the commit message whether the July values document the released checkpoints or correct future retraining.
- **[FACT]** No Transluce Hub model, user-model dataset, intervention dataset, or collection other than WeirdChat was created or modified in July/August 2026.

## Promising artifact dossiers

These dossiers record the required feasibility fields at an artifact-family level. A family is used only where artifacts are paired components of one released experiment.

### A. WeirdChat (inventory only; candidate generation delegated to Lane A)

- **Artifact name/type:** [WeirdChat dataset](https://huggingface.co/datasets/Transluce/WeirdChat), [research page](https://transluce.org/weirdchat), [code](https://github.com/TransluceAI/WeirdChat); behavior catalog plus prompts, judged rollouts, pairwise rankings, and search metadata.
- **Directly established behavior [FACT]:** 1,361 released behavioral patterns across six named frontier open-weight model families, with 173,184 cached judged rollouts. Some patterns are benign; others include severe self-harm or dangerous-advice behaviors.
- **Target model/checkpoint/size [FACT]:** DeepSeek-V4-Flash, Gemma 4 31B, Inkling, Nemotron 3 Ultra 550B-A55B, Qwen3.6-35B-A3B, and Qwen3.6-27B. Checkpoints are not hosted by Transluce and are mostly not 12 GB targets.
- **Open weights [FACT]:** described as frontier open-weight models; availability/licensing belongs to upstream providers.
- **Cached outputs/activations [FACT]:** complete cached transcripts/judgments; no activations.
- **Code availability [FACT]:** MIT code and current prompt templates.
- **Local 12 GB feasibility [INFERENCE]:** dataset analysis is easy; most exact subject-model reproduction is not locally feasible. A small-model analog would be a generalization study rather than exact reproduction.
- **Prior work answered [FACT]:** automated methods can elicit many unexpected patterns and attach naturalness/unexpectedness/harmfulness judgments.
- **Narrow unanswered causal question [SPECULATION]:** many exist, but Lane A is responsible for selecting them.
- **1-2 hour first test:** use Lane A's programmatic triage; no duplicate test proposed here.
- **Effort path:** not estimated in this lane.
- **Biggest confound [FACT]:** v1.0.1 removed 27 likely false positives; judgments are automated and reproduction is parameter-sensitive.
- **Kill rule:** defer to Lane A.

### B. SynthSys / SelfDescribe / PRISM behavioral datasets

- **Artifact name/type:** [SynthSys 8B](https://huggingface.co/datasets/Transluce/SynthSys-Llama-3.1-8B-Instruct), [SynthSys 70B](https://huggingface.co/datasets/Transluce/SynthSys-Llama-3.1-70B-Instruct), [SelfDescribe 8B](https://huggingface.co/datasets/Transluce/SelfDescribe-Llama-3.1-8B-Instruct), [SelfDescribe 70B](https://huggingface.co/datasets/Transluce/SelfDescribe-Llama-3.1-70B-Instruct), and [PRISM gender 8B](https://huggingface.co/datasets/Transluce/PRISM-gender-Llama-3.1-8B-Instruct); filtered behavioral positives.
- **Directly established behavior [FACT]:** Llama-3.1-Instruct completions often reveal user attributes implied by explicit/indirect system prompts (SynthSys), stereotypical first-person descriptions (SelfDescribe), or real conversation histories (PRISM). The release is filtered to positive/consistent cases; it does not by itself establish population frequency.
- **Target/checkpoint/size [FACT]:** Llama-3.1-8B-Instruct and 70B-Instruct. The subject checkpoints are upstream, not included in the datasets.
- **Open weights [FACT]:** upstream Meta open-weight license; typical Hugging Face access is gated. Transluce data are MIT/public.
- **Cached outputs/activations [FACT]:** SynthSys caches completions and judge probability arrays; SelfDescribe caches one `pred_prob`; PRISM caches aggregate revealed/ground-truth labels, not elicitation completions or per-prompt probabilities; no activations.
- **Code availability [FACT]:** full generation/filtering scripts in [observatory user_modeling](https://github.com/TransluceAI/observatory/tree/main/project/user_modeling).
- **Local 12 GB feasibility [INFERENCE]:** CPU data analysis is easy. Quantized 8B behavioral checks are plausible. 70B reproduction is not locally realistic.
- **Prior work answered [FACT]:** it defined revealed belief, filtered positives above a no-system-prompt baseline, showed decoder reading on synthetic/real distributions, and documented that elicitation queries themselves can bias gender. Only two PRISM gender prompts worked well for 8B; the authors failed to find low-bias prompts for 70B or other attributes.
- **Narrow unanswered causal question [SPECULATION]:** for PRISM, do the two agreeing biography/obituary elicitors reveal a belief already present at the end of the conversation, or induce the same gender prior because both request a third-person identity narrative?
- **1-2 hour first test:** fit a group-split bag-of-words/character baseline from released PRISM conversations to `attr` versus `gt_attr`, inspect class and disagreement structure, and pre-register three matched elicitation rewrites. This cheaply determines whether labels are dominated by overt lexical cues before any model run.
- **Effort path:** hours 0-2 data audit/baseline; 2-6 quantized 8B reproduction on 24-48 examples; 6-14 matched query swaps and neutral downstream probes; 14-22 repeat/score and analyze. Full range 14-26 hours depending on model setup.
- **Biggest confound [FACT/INFERENCE]:** elicitation is a measurement intervention, and no prompt-independent “true model belief” is observable.
- **Kill rule:** stop if the released PRISM label cannot be reproduced on a small sample under the two published prompts or if one template/decoding artifact wholly determines outputs with no stable conversation-conditioned variation.

### C. LatentQA user decoders and cached evaluation archive

- **Artifact name/type:** [all_to_all](https://huggingface.co/Transluce/all_to_all), [15_to_0](https://huggingface.co/Transluce/15_to_0), their `noheldout` variants, and [`latentqa.tar.gz`](https://transluce-public.s3.amazonaws.com/user-modeling/latentqa.tar.gz); Llama-3.1-8B-Instruct LoRA decoders, configs, and claimed evaluation outputs/checkpoints.
- **Directly established behavior [FACT]:** all-to-all and 15-to-0 can have similar reading accuracy while all-to-all controls subject behavior much better. KV reading likewise works while KV control fails. Decoders trained on unfiltered SynthSys read worse but have almost identical control/alignment; general LatentQA data can read SelfDescribe extremely well but controls worse.
- **Target/checkpoint/size [FACT]:** Llama-3.1-8B-Instruct base plus a 1.227 GB adapter. The all-to-all decoder reads/writes all 32 residual layers; 15-to-0 maps subject layer 15 to decoder layer 0.
- **Open weights [FACT]:** Transluce adapters public and ungated; the documented base is Meta Llama-3.1-8B-Instruct.
- **Cached outputs/activations [FACT]:** the public README calls the 9.43 GB archive checkpoints and evaluation results and also the full training/evaluation data. Archive contents were not downloaded, so raw activation availability is uncertain.
- **Code availability [FACT]:** read, gradient-steering, and circuit-steering scripts in [observatory latentqa](https://github.com/TransluceAI/observatory/tree/main/project/latentqa).
- **Local 12 GB feasibility [INFERENCE]:** low for the documented two-model workflow. Two quantized 8B instances plus adapter/activations may be borderline; a 24 GB+ GPU or CPU offload is the safer plan. Training is out of scope.
- **Prior work answered [FACT]:** readout can generalize; all-layer access is important for gradient control; the decoder tracks three manually selected country-neuron circuits (France, India, South Korea) despite not training on those interventions.
- **Narrow unanswered causal question [SPECULATION]:** does gradient-based “user-model control” transfer to behaviorally different, non-prefilled decisions, or does it mostly optimize label-token/infobox continuations used by both decoder objective and evaluator?
- **1-2 hour first test:** after environment preflight, use one released all-to-all adapter and five gender source-target cases; compare the published forced-infobox metric with one semantically different neutral recommendation and a same-norm random edit. If weights are not cached, expect 3-6 hours to first result rather than pretending download/setup is free.
- **Effort path:** hours 0-4 load/preflight; 4-10 five-case reproduction and simple output-logit baseline; 10-20 30-50 held-out downstream probes and controls; 20-35 robustness, seed, and mechanistic follow-up. A useful decision is possible by hour 10-14; a solid result likely needs 20-35 hours.
- **Biggest confound [INFERENCE]:** changing arbitrary activations can broadly corrupt or bias generation, so a changed attribute token is not evidence of a coherent user representation.
- **Kill rule:** stop if published five-case steering cannot be reproduced, or if same-norm random/direct label-logit steering matches all downstream changes and decoder alignment adds no discriminatory signal.

### D. Input-ablation datasets and explainers

- **Artifact name/type:** [Qwen dataset](https://huggingface.co/datasets/Transluce/input_ablation_qwen3_8b_mmlu_hint), [Llama dataset](https://huggingface.co/datasets/Transluce/input_ablation_llama_3.1_8b_instruct_mmlu_hint), [Qwen explainer](https://huggingface.co/Transluce/input_ablation_qwen3_8b_qwen3_8b_hint), [Llama explainer](https://huggingface.co/Transluce/input_ablation_llama3.1_8b_instruct_llama3.1_8b_instruct); cached MMLU hint counterfactuals and fine-tuned 8B explainers.
- **Directly established behavior [FACT]:** random hints change Qwen3-8B's answer in 8,517/12,642 train cases (67.4%) and 929/1,395 paper-counted test cases (66.6%); they change Llama's answer in 4,739/12,642 (37.5%) and 518/1,395 (37.1%). Fine-tuned self-explainers predict the no-hint counterfactual with 83.4% Qwen and 63.8% Llama exact match. Cross-model and untrained explainers are worse.
- **Target/checkpoint/size [FACT]:** Qwen3-8B and Llama-3.1-8B-Instruct; full explainer checkpoints are 16.40 and 16.08 GB.
- **Open weights [FACT]:** Transluce checkpoints are public/ungated; Qwen base is public. The Llama workflow is derived from Meta Llama.
- **Cached outputs/activations [FACT]:** both hinted and zero-shot predictions, question/choices/correct answer, hint strings/token IDs, and full prompts; no activations.
- **Code availability [FACT]:** [introspective-interp](https://github.com/TransluceAI/introspective-interp). Current input-ablation configs use `1e-5` after a July 7 update.
- **Local 12 GB feasibility [INFERENCE]:** CPU-only dataset baselines are trivial. One 4-bit checkpoint is plausible; target-plus-explainer evaluation is borderline and may require serialization/offload or larger VRAM.
- **Prior work answered [FACT]:** fine-tuning is necessary; same-model explainers outperform cross-model explainers; untrained Qwen predicts “changed” only 8.6% of the time and performs mainly on unchanged cases.
- **Narrow unanswered causal question [SPECULATION]:** is the same-model advantage privileged access to its decision rule, or ordinary model-specific behavioral self-simulation/MMLU solving that an output-matched black-box baseline can reproduce?
- **1-2 hour first test:** on cached data, measure two simple behavioral baselines with no weights: predict the no-hint answer from the MMLU correct answer; and treat one extra black-box no-hint query as the upper-bound counterfactual baseline. Stratify reported explainer gains by target correctness, hint agreement, subject, and changed/unchanged class. This reveals whether “explanation” accuracy is mostly question solving/class balance.
- **Effort path:** hours 0-2 cached baseline; 2-7 quantized checkpoint preflight and published-split reproduction; 7-15 matched changes to hint wording/position/authority while holding answer semantics fixed; 15-22 cross-model/black-box behavioral matching and analysis. Full range 12-24 hours.
- **Biggest confound [INFERENCE]:** the task asks for the model's output on the same question without one short suffix; high self-prediction can arise from shared weights/output tendencies without access to a particular hidden computation.
- **Kill rule:** stop if the released evaluation cannot be reproduced or if the new hint rewrites eliminate target behavioral variance. A simple baseline matching the self-explainer is a substantive negative result, not automatically a kill.

### E. Activation-patching counterfactual datasets and explainers

- **Artifact name/type:** [Qwen patch dataset](https://huggingface.co/datasets/Transluce/act_patch_qwen3_8b_counterfact), [Llama patch dataset](https://huggingface.co/datasets/Transluce/act_patch_llama_3.1_8b_counterfact), [Qwen adapter](https://huggingface.co/Transluce/act_patch_qwen3_8b_qwen3_8b), and [Llama adapter](https://huggingface.co/Transluce/act_patch_llama3.1_8b_llama3.1_8b); cached causal interventions and continuous-token explainers.
- **Directly established behavior [FACT]:** patching averaged residual vectors from a counterfactual fact across layer blocks sometimes changes the constrained target answer. Fine-tuned self-explainers predict Qwen outcomes at 64.0% exact match / 80.2 macro-F1 and Llama outcomes at 48.6% / 77.5 macro-F1.
- **Target/checkpoint/size [FACT]:** Qwen3-8B or Llama-3.1-8B target plus 3.886/3.444 GB LoRA adapter.
- **Open weights [FACT]:** Transluce adapters/datasets public; Qwen base public; documented Llama base is Meta Llama.
- **Cached outputs/activations [FACT]:** the dataset includes the exact intervention vector, layer block, original/counterfactual token positions, original/patched continuations, and target labels. It does not require regenerating the full training set.
- **Code availability [FACT]:** [introspective-interp](https://github.com/TransluceAI/introspective-interp) with continuous Qwen/Llama classes.
- **Local 12 GB feasibility [INFERENCE]:** dataset-only baselines are easy. Full target+explainer causal validation is unlikely to be comfortable on 12 GB because a quantized base, multi-GB adapter, second target computation, and continuous vectors are required.
- **Prior work answered [FACT]:** the authors balanced labels across layer/token categories and tested removing activation, layer, or token from the explainer input. Removing the activation causes only a 4.1-point Qwen and 3.4-point Llama exact-match drop; removing layer/token is negligible. Activations alone allow 98.7% reconstruction of layer/token on a separate task.
- **Narrow unanswered causal question [SPECULATION]:** holding all surface metadata fixed, do explainer predictions causally track the identity/content of the intervention vector, or mostly CounterFact prompt/target priors?
- **1-2 hour first test:** stream/download one released split and fit grouped metadata/text-only baselines for `is_different` and patched content using layer block, token type, original/counterfactual text, and target choices, with subject/relation groups held out. Compare with the paper's activation-ablated numbers.
- **Effort path:** hours 0-3 dataset and grouped baseline; 3-9 adapter/custom-code preflight; 9-17 within-layer/token matched vector swaps, zeros, and sign/norm controls; 17-30 recompute a small set of target patches and analyze OOD/permutation effects. Useful baseline result by hour 3; full causal validation likely 18-32 hours.
- **Biggest confound [INFERENCE]:** random vector permutations can be off-manifold, so an explainer response to them may not diagnose faithfulness. Matched real intervention vectors and target-model recomputation are essential.
- **Kill rule:** stop model work if the released adapter/custom class cannot run within available compute or if no matched vector pairs exist. A surface-only baseline matching the explainer remains an informative result but would redirect the project away from a costly vector intervention.

### F. Feature explainer/simulator and 2024 neuron resources (useful baseline, not admitted as a project here)

- **Artifact name/type:** four 16.06 GB 2025 feature explainer/simulator checkpoints, two 16.07 GB 2024 neuron explainer/simulator checkpoints, 26.92 GB SAE training archive, and 180/152 MB cached OOD activation archives.
- **Directly established behavior [FACT]:** fine-tuned models generate feature descriptions with measurable simulator correlation; self-explainers outperform less-aligned models, and 2024 automated neuron descriptions average 0.61 versus a human expert's 0.55 on the paper's simulator metric.
- **Target/checkpoint/size/open weights [FACT]:** Llama-3.1-8B(-Instruct), public Transluce full checkpoints around 16.1 GB; custom wrappers required for 2025 models.
- **Cached outputs/activations/code [FACT]:** substantial cached activation resources and full code exist. The smaller OOD archives are locally tractable; the 26.92 GB training archive is not a cheap opening move.
- **Local 12 GB feasibility [INFERENCE]:** only quantized inference is plausible, and custom quantization support is unverified.
- **Prior work answered [FACT]:** OOD description quality was evaluated on full activations and CounterFact activation differences; the 2024 work explicitly notes top exemplars can miss lower-quantile behavior.
- **Narrow unanswered question [SPECULATION]:** whether simulator score predicts causal importance for a concrete model behavior outside top-activation regimes.
- **Why no candidate slot:** no released behavior/model pair in this lane creates a clean, locally cheap causal test; WeirdChat targets do not match Llama-3.1-8B. Starting here would be method-first and weaker than the four admitted substrates.
- **Potential 1-2 hour use:** treat simulator/nearest-neighbor scores as baselines if a finalist later needs feature explanations.
- **Biggest confound / kill rule:** simulator agreement is not behavioral causal validity; do not promote this family unless a finalist supplies a named behavior and matched target model.

## Unranked candidate registry (4 distinct projects)

### TRANS-01

```text
candidate_id
TRANS-01

title
Does PRISM “revealed gender” pre-exist the elicitation query, or is it induced by biography/obituary framing?

source_family
Transluce user representations: PRISM-gender + SelfDescribe/SynthSys measurement methodology

behavior
On filtered real PRISM conversations, Llama-3.1-8B-Instruct gives gender inferences that agree across a biography-infobox and an obituary elicitation query; released labels sometimes differ from participant ground truth.

behavior_status
[FACT] RELEASED_FILTERED_POSITIVE. There are 5,041 released rows. This establishes agreement under the two selected elicitors, not a denominator-wide rate or prompt-independent latent belief.

primary_source
https://transluce.org/user-modeling
https://huggingface.co/datasets/Transluce/PRISM-gender-Llama-3.1-8B-Instruct

repo
https://github.com/TransluceAI/observatory/tree/main/project/user_modeling

dataset
Transluce/PRISM-gender-Llama-3.1-8B-Instruct (5,041 rows, 14.21 MB); SelfDescribe can supply synthetic positive controls.

model/checkpoint
meta-llama/Llama-3.1-8B-Instruct. Optional Transluce LatentQA adapters for a later internal readout, not required for the opening behavioral test.

evidence_of_reproducibility
[FACT] Prompts, filtering code, labels, and conversation inputs are released. [FACT] Authors explicitly report that query wording can bias the inferred attribute and that only two prompts worked for 8B gender; they failed for 70B/other attributes.

frequency/rate_if_known
[FACT] 5,041 accepted rows; denominator and per-elicitor agreement rate are not released in the dataset card, so no population frequency is claimed.

what_prior_work_did
[FACT] Generated ten completions per elicitor, judged probabilities with GPT-4.1-mini, kept rows when both elicitor argmaxes agreed, trained/evaluated LatentQA, and compared revealed labels with ground truth/direct asking/probes.

what_prior_work_did_not_do
[FACT/INFERENCE] It did not establish that the label is stable under semantically different, attribute-neutral elicitors or behaviorally relevant downstream questions. The released PRISM file omits per-elicitor completions/probabilities.

unanswered_question
[SPECULATION] Does conversation history causally set a stable gender-conditioned state before measurement, or do two closely related third-person identity requests impose the same prior during measurement?

competing_explanations
A. Stable conversation-conditioned user inference exists before the elicitor.
B. Biography/obituary formats independently induce a shared gender prior.
C. Overt lexical/demographic cues directly drive each completion without a reusable user representation.

first_1_to_2_hour_test
Load the 5,041-row release; quantify attr/gt class balance and disagreement; train group-split character/word baselines to predict attr versus gt from conversation text; pre-register three matched elicitors (published biography, published obituary, attribute-neutral downstream choice). If the model is already cached, run 24 stratified rows; otherwise report setup separately rather than hiding it.

possible_causal_intervention
For a fixed conversation, swap only the elicitation query and response prefill; cross the published identity formats with neutral downstream probes. Capture/read activations before the elicitor only if behavioral disagreement warrants an internal test.

simple_baseline
Majority class; bag-of-words/character classifier; prompt-only output distribution with conversation removed.

safety_relevance
Models may silently infer protected attributes from real conversations and personalize/refuse differently; measurement tools could themselves create the belief they claim to expose.

compute_feasibility
[INFERENCE] Dataset work is CPU-cheap. Quantized single-8B inference is plausible on 12 GB; BF16 is not. No dual-model setup is necessary for the core test.

estimated_hours
First data result 1-2h; behavioral reproduction 3-6h if checkpoint setup is needed; useful causal comparison 10-16h; full robust study 14-26h.

largest_confound
There is no prompt-independent oracle for a model's belief; every measurement query can alter the state being measured.

kill_rule
Stop if the two published elicitors fail to reproduce on a small stratified sample, or if one response-format/tokenization artifact wholly determines the label and conversation-conditioned variation disappears.

novelty_confidence
MEDIUM-HIGH: the source explicitly documents measurement bias but does not resolve it; verify against any post-2025 follow-up before final selection.

evidence_confidence
HIGH for the released filtered behavior and documented limitation; MEDIUM for exact local reproducibility before running the checkpoint.

fact/inference/speculation labels
Facts: released row count, filter, failed prompt search, target model. Inference: third-person formats may share a prior. Speculation: a stable pre-elicitor state versus measurement-induced state can be separated by the proposed query swaps.
```

### TRANS-02

```text
candidate_id
TRANS-02

title
Does LatentQA user-attribute steering transfer beyond the label-bearing behavior used to optimize and score it?

source_family
Transluce user representations: LatentQA all-to-all / 15-to-0 / KV read-control dissociations

behavior
LatentQA architectures that read user attributes similarly can differ sharply in behavioral control: all-to-all controls well; 15-to-0 and KV variants often read but control poorly. Training-data changes can alter reading without correspondingly altering control.

behavior_status
[FACT] PUBLISHED_CAUSAL_DISSOCIATION with gradient interventions and a smaller circuit-steering validation on country neurons.

primary_source
https://transluce.org/user-modeling
https://huggingface.co/collections/Transluce/scalably-extracting-latent-representations-of-users

repo
https://github.com/TransluceAI/observatory/tree/main/project/latentqa

dataset
SelfDescribe-Llama-3.1-8B-Instruct for published control; SynthSys and PRISM for reading/generalization. The 9.43 GB S3 archive claims evaluation results/checkpoints.

model/checkpoint
Transluce/all_to_all, Transluce/15_to_0 and optionally noheldout variants; each is a 1.227 GB LoRA over meta-llama/Llama-3.1-8B-Instruct.

evidence_of_reproducibility
[FACT] Adapters, train configs, data, plot archive, and read/gradient/circuit evaluation scripts are released. Cards are empty license stubs, so configs/repo are essential.

frequency/rate_if_known
[FACT] Source gives qualitative/figure-level aggregate control and alignment, not a single textual success rate. Circuit validation covers manually selected France (14 neurons), India (26), and South Korea (8) neuron sets.

what_prior_work_did
[FACT] Optimized activations for 20 Adam steps toward target answers; evaluated forced attribute tokens/free-form generations; compared architectures/data; and showed decoder tracking of three country-neuron circuit interventions.

what_prior_work_did_not_do
[INFERENCE] It did not demonstrate broad transfer to downstream behaviors that neither name nor prefill the attribute, nor compare against a direct output-label/logit steering baseline matched for edit norm and fluency.

unanswered_question
[SPECULATION] Does all-to-all control causally modify a reusable user representation, or a broad direction optimized for the attribute-token evaluator?

competing_explanations
A. All-to-all accesses and edits a distributed causal user model used across tasks.
B. The gradient follows a decoder-specific direction that changes the same label-bearing completion but not unrelated decisions.
C. Large activation edits cause generic generation/logit shifts that look like attribute control.

first_1_to_2_hour_test
Preflight one all-to-all adapter on five gender source-target cases and score the published forced-infobox output plus one neutral recommendation and same-norm random edit. If assets are not cached, the honest time-to-first-result is 3-6h because model/archive setup dominates.

possible_causal_intervention
Use the same optimized activation edit across (i) published forced answer, (ii) semantically different attribute-relevant choice, and (iii) attribute-irrelevant fluency/control prompts; compare all-to-all, 15-to-0, random-direction, and direct label-logit directions at matched norm.

simple_baseline
Direct output-token/logit gradient; mean activation-difference direction from source/target examples; same-norm random edit.

safety_relevance
A monitor/control system that reads protected or vulnerability-related traits but only changes its own readout can create false assurance; broad non-specific steering can introduce covert side effects.

compute_feasibility
[INFERENCE] Scientifically strong but locally risky. The documented workflow couples subject and decoder 8B computations. Two quantized instances plus adapter may exceed 12 GB; CPU offload or a 24 GB+ GPU is likely.

estimated_hours
Environment/result preflight 3-6h; five-case reproduction/baselines 6-10h; useful downstream battery by 14-20h; robust matched-norm study 20-35h.

largest_confound
Activation edits can perturb many computations at once; downstream change does not by itself show a coherent attribute representation.

kill_rule
Stop if the published control cannot be reproduced on five cases, or if direct label-logit/random edits match the full downstream pattern and LatentQA architecture adds no discriminating behavior.

novelty_confidence
MEDIUM-HIGH: the source explicitly leaves the filtering/read-control contrast open, but downstream generalization literature should be rechecked for a finalist.

evidence_confidence
HIGH for the published dissociations; MEDIUM for local feasibility and archive contents.

fact/inference/speculation labels
Facts: architecture/training-data dissociations, released adapters/configs, circuit validation. Inference: evaluator-coupled control is a major alternative. Speculation: cross-behavior matched-norm tests will discriminate it.
```

### TRANS-03

```text
candidate_id
TRANS-03

title
Is hint-ablation “self-explanation” privileged introspection or ordinary model-specific behavioral self-simulation?

source_family
Training Language Models To Explain Their Own Computations: MMLU input ablation

behavior
Random answer hints often change Qwen3-8B and Llama-3.1-8B-Instruct multiple-choice predictions; after fine-tuning, a model predicts its own no-hint counterfactual better than another model or its untrained self.

behavior_status
[FACT] PUBLISHED_AND_CACHED behavioral counterfactuals with released full explainers.

primary_source
https://arxiv.org/abs/2511.08579
https://huggingface.co/datasets/Transluce/input_ablation_qwen3_8b_mmlu_hint
https://huggingface.co/datasets/Transluce/input_ablation_llama_3.1_8b_instruct_mmlu_hint

repo
https://github.com/TransluceAI/introspective-interp

dataset
Two 14,042-row datasets (about 22 MB each), containing questions, choices, correct answer, random hint, hint/zero-shot target predictions, token IDs, and rendered prompts.

model/checkpoint
Transluce/input_ablation_qwen3_8b_qwen3_8b_hint (16.40 GB) and Transluce/input_ablation_llama3.1_8b_instruct_llama3.1_8b_instruct (16.08 GB); target Qwen3-8B or Llama-3.1-8B-Instruct.

evidence_of_reproducibility
[FACT] Data, model weights, code, configs, and evaluation entrypoints are public. [CAUTION] July 2026 configs use a lower LR than the initial repo, and cards contain copy/ID errors.

frequency/rate_if_known
[FACT] Qwen hint-change: 67.4% train and 66.6% of the paper-counted test subset. Llama: 37.5% train and 37.1% test. Self-explainer exact match: Qwen 83.4%; Llama 63.8%. Released tests contain 1,400 rows, five more than each paper table accounts for.

what_prior_work_did
[FACT] Balanced/constructed changed versus unchanged examples, compared same- and cross-model explainers, reported exact/content/F1, and analyzed the untrained Qwen's strong “unchanged” bias.

what_prior_work_did_not_do
[INFERENCE] It did not behavior-match an external simulator or separate solving the underlying MMLU question from accessing a particular hidden decision procedure. It studied one short random-hint template per target.

unanswered_question
[SPECULATION] After controlling for target accuracy and output tendencies, does self-model advantage persist on semantically equivalent new hint formats and authority/position counterfactuals?

competing_explanations
A. Shared weights give privileged access to the target's decision rule.
B. The self-explainer simply reproduces its own stable no-hint output distribution/MMLU knowledge.
C. The advantage is template/tokenizer-specific or driven by changed-class imbalance.

first_1_to_2_hour_test
Use cached data only: measure a correct-answer/MMLU-solving baseline and stratify reported target counterfactuals by correctness, hint match, subject, and changed class. Specify the one-extra-black-box-query baseline, which exactly obtains the no-hint counterfactual, as the simple causal behavioral ceiling.

possible_causal_intervention
Hold question, choices, and hinted answer fixed while changing hint wording, location, asserted authority, or unrelatedness; compare same-model, cross-model, and behavior-matched external predictors on newly measured no-hint outcomes.

simple_baseline
Correct-answer predictor; class-conditional majority; one direct target query on the ablated input; small text classifier trained on cached target outputs.

safety_relevance
Models can silently follow misleading hints while failing to verbalize that influence; an “introspective” monitor that is merely a behavior emulator may fail under distribution shift or strategic behavior.

compute_feasibility
[INFERENCE] The strongest 1-2h baseline is CPU-only. Full checkpoints need quantization on 12 GB, and a fair target+explainer run may need offload/larger VRAM.

estimated_hours
Cached baseline 1-2h; checkpoint reproduction 4-8h; matched hint counterfactuals 8-16h; robust cross-model analysis 12-24h.

largest_confound
The counterfactual answer is simply the target's answer to the same question without a short suffix; predicting it need not involve introspection into the original hinted computation.

kill_rule
Stop if the released checkpoint/eval does not reproduce or new hint formats remove target behavioral variance. If simple behavior/MMLU baselines match the self-explainer, preserve that as the main negative result rather than adding mechanisms.

novelty_confidence
MEDIUM: a sharp extension of the paper's privileged-access claim, but neighboring introspection/self-prediction work needs a finalist novelty check.

evidence_confidence
HIGH for target behavior, cached data, and reported metrics; MEDIUM for the causal interpretation.

fact/inference/speculation labels
Facts: dataset fields/rates/results. Inference: shared output tendencies are a serious mundane explanation. Speculation: matched hint-format counterfactuals separate it from privileged access.
```

### TRANS-04

```text
candidate_id
TRANS-04

title
Do activation-patching explainers actually use the intervention vector on matched counterfactuals?

source_family
Training Language Models To Explain Their Own Computations: CounterFact activation patching

behavior
Counterfactual residual-stream patches causally change some constrained factual outputs, and fine-tuned Qwen/Llama explainers predict those outcomes above untrained baselines.

behavior_status
[FACT] PUBLISHED_CAUSAL_DATASET with exact cached intervention vectors and before/after behavior.

primary_source
https://arxiv.org/abs/2511.08579
https://huggingface.co/datasets/Transluce/act_patch_qwen3_8b_counterfact
https://huggingface.co/datasets/Transluce/act_patch_llama_3.1_8b_counterfact

repo
https://github.com/TransluceAI/introspective-interp

dataset
Qwen: 120,644 train + 14,357 test, 911 MB compressed. Llama: 13,454 train + 5,600 test plus 107,130 train_full, 837 MB compressed. Each row includes vector, position/layers, tokens, targets, and original/patched continuations.

model/checkpoint
Transluce/act_patch_qwen3_8b_qwen3_8b (3.886 GB adapter over Qwen3-8B) or Transluce/act_patch_llama3.1_8b_llama3.1_8b (3.444 GB over Llama-3.1-8B).

evidence_of_reproducibility
[FACT] Intervention data, adapters, custom continuous-token classes, configs, and evaluation code are released. The data let a project skip expensive training-data generation.

frequency/rate_if_known
[FACT] Dataset was deliberately balanced across changed/unchanged categories rather than sampled to estimate a natural frequency. Qwen self-explainer: 64.0 exact / 80.2 macro-F1; Llama: 48.6 / 77.5.

what_prior_work_did
[FACT] Compared self/cross/untrained explainers and ablated activation, layer, or token inputs. Dropping the vector reduced exact match only 4.1 points for Qwen and 3.4 for Llama; layer/token drops were negligible.

what_prior_work_did_not_do
[INFERENCE] It did not show, with matched surface prompts, that changing only the real intervention vector causes corresponding changes in the explainer prediction and validates against newly recomputed target patches.

unanswered_question
[SPECULATION] Is the continuous vector a causally used explanation input, or a small refinement atop CounterFact text/answer priors?

competing_explanations
A. The vector encodes patch content and causally controls the explainer's prediction.
B. Surface text, targets, layer/token distribution, and answer priors explain most performance.
C. The vector identifies dataset strata/position rather than patch semantics (the paper shows 98.7% position reconstruction from it).

first_1_to_2_hour_test
Fit grouped metadata/text-only baselines to `is_different` and patched answer, holding out CounterFact subjects/relations. Compare to the paper's vector-ablated metrics before loading any model.

possible_causal_intervention
Within matched layer/token/target groups, swap real vectors between examples, use norm-matched zeros/sign flips, obtain explainer predictions, then recompute target patches for a small subset to distinguish meaningful in-manifold swaps from generic OOD failure.

simple_baseline
Grouped logistic/tree/text classifier; nearest-neighbor by original/counterfactual targets; activation-ablated released model.

safety_relevance
An explanation generator that ignores the causal intervention can look faithful on benchmark averages yet fail exactly when used to predict safety-relevant internal edits.

compute_feasibility
[INFERENCE] Dataset baseline is CPU-feasible. Adapter plus base plus target validation is likely above comfortable 12 GB use; external 24 GB+ GPU/CPU offload may be required.

estimated_hours
Dataset baseline 2-3h; adapter preflight 4-9h; matched vector intervention 10-18h; target recomputation/robustness 18-32h.

largest_confound
Arbitrary vector swaps may be off-manifold; conclusions require real matched vectors and target-model behavioral validation.

kill_rule
Stop costly model work if grouped matches cannot be constructed or the custom adapter cannot run. If surface baselines match published results, report that result and do not escalate to broader mechanistic searches.

novelty_confidence
MEDIUM-HIGH: directly targets a surprisingly small published vector-ablation gap; check for post-February follow-ups before finalist status.

evidence_confidence
HIGH for data/interventions/metrics; MEDIUM for local model feasibility.

fact/inference/speculation labels
Facts: cached causal patches, ablation numbers, released code/adapters. Inference: surface shortcuts may dominate. Speculation: matched real-vector swaps will distinguish semantic use from shortcut use.
```

## Explicit non-candidates and deduplication decisions

| Opportunity | Decision | Reason |
|---|---|---|
| WeirdChat behavior variants | Do not add here | Lane A owns the behavior search; duplicating it would inflate the registry |
| Straight SynthSys “does the model personalize?” reproduction | Do not add | Positive examples were selected precisely because they personalize; no new competing explanation |
| Generic “try a probe/SAE on user representations” | Reject | Method-first and redundant with stronger published read/control evidence |
| 2024 neuron simulator score audit | Retain as baseline resource only | Concrete metric behavior exists, but no matching named target behavior makes a small causal project cleaner than TRANS-03/04 |
| Re-train an introspective explainer | Reject for selection | Released checkpoints/data already exist; training is costly and does not answer a distinct behavioral question |
| 70B user-decoder reproduction | Do not admit | Scale demonstration exists, local feasibility is poor, and it does not add a narrower causal question |
| “Use Transluce explanations on WeirdChat” | Reject as currently formulated | WeirdChat subject checkpoints do not match the Llama-3.1/Qwen3-8B explanation resources |

## Reproducibility and scientific cautions to carry into synthesis

1. **Selection-conditioned behavior:** SynthSys, SelfDescribe, PRISM gender, and activation-patching class balance are constructed/filtered datasets. Do not report their positive fraction as natural incidence.
2. **Measurement intervention:** PRISM's revealed label is conditional on a biography/obituary query and a response prefill. The source itself documents prompt-induced gender bias.
3. **Judge dependence:** user revealed beliefs rely on GPT-4.1-mini probabilities; WeirdChat presence judgments use Gemma 4 31B and pairwise rankings use Gemini 3.5 Flash.
4. **Metric versus causality:** explainer exact match, simulator correlation, and decoder reading are not causal evidence. The strongest causal facts here are target output changes under actual patches/steering, and even those require specificity controls.
5. **Code/card drift:** user model cards contain no usage documentation; the current data totals differ from prose; input-ablation code learning rates changed in July; multiple introspective cards/README snippets contain copied target IDs or path/name errors.
6. **Hardware optimism:** “8B” does not imply documented 12 GB compatibility. All full checkpoints are ~16 GB, and several evaluations load or couple two models.
7. **Safety content:** WeirdChat includes self-harm/suicide and dangerous-advice content. Programmatic handling is appropriate; manual inspection should be limited to decision-relevant examples.

## Audit trail

### Files changed

- Created `research_proposal_pivot/codex_search_working/02_transluce.md` (this report).

### Mechanical checks/scripts executed

- Direct Hugging Face API enumeration for all Transluce models/datasets, creation/modification dates, public/gated status, tags, file manifests, and blob sizes.
- Hugging Face dataset-server metadata and small-row inspection for exact splits/schemas and cached-field verification.
- HEAD-only checks of four linked S3 archives; no archive was downloaded.
- GitHub public API checks for linked repository metadata, recent commits, and the July input-ablation configuration diff.

### Primary external sources inspected

- [Transluce Hugging Face organization](https://huggingface.co/Transluce), both collections, all model/dataset cards/manifests, and WeirdChat commit history.
- [Scalably Extracting Latent Representations of Users](https://transluce.org/user-modeling).
- [Training Language Models To Explain Their Own Computations, arXiv v3](https://arxiv.org/html/2511.08579v3).
- [Scaling Automatic Neuron Description](https://transluce.org/neuron-descriptions).
- [WeirdChat research page](https://transluce.org/weirdchat).
- Official code: [observatory](https://github.com/TransluceAI/observatory), [introspective-interp](https://github.com/TransluceAI/introspective-interp), and [WeirdChat](https://github.com/TransluceAI/WeirdChat).

### Manually inspected

- Representative cached rows/schemas from PRISM, SelfDescribe, SynthSys, input-ablation, and activation-patching releases.
- All substantive cards plus the MIT-only stub cards, four LatentQA adapter configs/YAMLs, paper result/ablation tables, and recent repository diffs.

### What remains uncertain

- Exact contents of the 9.43 GB LatentQA archive and whether it contains reusable raw activations.
- Whether Transluce's custom continuous-token and LatentQA paths support 4-bit quantization/weight sharing on a 12 GB GPU.
- Why current SynthSys split totals differ from the prose article, why five input-ablation test rows are absent from the paper's class-count table, and whether the July LR correction matches released January checkpoints.
- Finalist novelty against literature published after the primary works; this lane audited the ecosystem, not the entire literature.

