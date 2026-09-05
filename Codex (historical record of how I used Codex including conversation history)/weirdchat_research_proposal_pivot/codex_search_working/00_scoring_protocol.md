# Candidate Scoring Protocol

Freeze date: 2026-08-23, before lane completion and candidate ranking.

Amendment, 2026-08-23: the researcher explicitly removed the hard approximately
20-hour feasibility cutoff. The rubric below therefore treats total effort and
completion probability as graded costs, not exclusion rules. This amendment was
made before candidate scoring and lane synthesis.

All component scores use 0–10. For positive dimensions, 10 is best. `prompt_model_shopping_risk` and `lexical_triviality_risk` are risks, so 10 is worst and the balanced score uses `10 - risk`.

The numerical registry is a reduction aid, not the final scientific judge. Missing evidence must not be silently scored as average; use a conservative score and record the uncertainty.

## Balanced ranking A — overall MATS project

| Dimension | Weight |
|---|---:|
| existing_behavioral_robustness | 8 |
| reproducibility_evidence | 7 |
| naturalness_deployment_relevance | 3 |
| safety_relevance | 6 |
| scientific_surprise | 3 |
| competing_explanations_quality | 5 |
| mechanistic_discriminability | 8 |
| intervention_usefulness | 6 |
| open_weight_availability | 4 |
| local_12gb_feasibility | 7 |
| code_availability | 2 |
| dataset_cached_output_availability | 2 |
| time_to_first_result | 7 |
| total_project_effort_fit | 7 |
| neel_mats_fit | 7 |
| novelty_gap_plausibility | 5 |
| value_if_mechanism_simple | 2 |
| value_if_hypothesis_falsified | 2 |
| resistance_to_prompt_model_shopping (`10-risk`) | 2 |
| resistance_to_lexical_triviality (`10-risk`) | 2 |
| coherent_artifact_probability | 5 |
| **Total** | **100** |

## Ranking B — highest safety relevance

Primary ordering: safety relevance, naturalness/deployment relevance, behavioral robustness, intervention usefulness, then feasibility. A difficult candidate may rank highly when its expected scientific payoff justifies the extra effort.

## Ranking C — highest probability of reaching a causal result

Primary ordering: behavioral robustness, reproducibility, mechanistic discriminability, local feasibility, time to first result, code/data availability, and coherent-artifact probability.

## Ranking D — highest novelty/upside

Primary ordering: novelty/gap plausibility, surprise, competing explanations, mechanistic discriminability, safety relevance. Speculative behavior remains penalized.

## Ranking E — best model-forensics project

Primary ordering: documented weird action, naturalness, causal ambiguity, quality of precise behavioral counterfactuals, safety relevance, and value if a benign explanation wins.

## Filtered views

- Ranking F: best use of local user-model corpus, restricted to `USER_MODEL` candidates.
- Ranking G: best WeirdChat-derived candidate, restricted to source lane A.
- Ranking H: best very-recent-paper opportunity, restricted to June–August 2026 sources.

## Non-negotiable overrides

A high numerical score cannot rescue a candidate when:

- the behavior is not actually established and cannot be tested within two hours;
- the nearest paper already answers the proposed causal question;
- model/checkpoint access makes the proposed first result or eventual causal test non-credible even after reasonable scoping;
- the proposed internal method adds nothing beyond a simple prompt/CoT baseline;
- the mechanism would merely localize answer evidence;
- the project depends on prompt/model shopping;
- the candidate reopens a terminated branch.

Conversely, a candidate with slightly lower average score may win when its causal question is markedly sharper and its falsified outcome remains a coherent artifact. A candidate is not excluded solely because its honest estimate exceeds 20 hours.
