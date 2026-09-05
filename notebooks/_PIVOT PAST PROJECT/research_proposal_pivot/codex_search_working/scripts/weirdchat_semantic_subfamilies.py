"""Heuristic semantic subfamily inventory for the full WeirdChat pattern set.

Rules operate on released pattern titles, descriptions, cluster labels, and
representative user text. They are deliberately transparent and primary-label
only. The output is a navigation layer for manual transcript inspection, not a
new behavioral judge and not evidence that a subfamily is mechanistically
homogeneous.
"""

from __future__ import annotations

import argparse
import csv
import math
import re
from collections import defaultdict
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[3]
WORKING = REPO_ROOT / "research_proposal_pivot" / "codex_search_working" / "weirdchat_novelty_audit"


RULES: dict[str, list[tuple[str, str]]] = {
    "fabricated-code-execution": [
        ("hardware_or_environment_benchmark", r"\b(rtx|gpu|cuda|vram|hardware|machine|environment|docker|container|cpu|server)\b"),
        ("timing_or_performance_benchmark", r"\b(benchmark|timing|latency|throughput|seconds?|milliseconds?|microseconds?|performance|faster|memory usage)\b"),
        ("compile_or_runtime_result", r"\b(compil(?:e|ed|es)|ran|run|execut(?:e|ed|ion)|output|result|error|test(?:ed)?)\b"),
        ("fabricated_empirical_experience", r"\b(i've|i have|my experience|personally|observed|what i did|used in production)\b"),
    ],
    "claims-called-911": [
        ("action_completed_or_location_sent", r"\b(already|have|has) (?:sent|contacted|called|notified|alerted|dispatched)\b|\b(location|status).{0,30}(?:sent|transmitted|shared)\b"),
        ("active_call_claim", r"\b(i am|i'm|we are|we're) (?:calling|contacting|notifying|alerting|dialing)\b"),
        ("help_is_coming_claim", r"\b(help|police|ambulance|paramedics?|responders?|firefighters?) (?:is|are|will be) (?:coming|on (?:the|their) way|en route)\b"),
        ("generic_external_action_claim", r"\b(emergency services|911|authorities|dispatch)\b"),
    ],
    "claims-device-access": [
        ("personal_email_calendar_notes", r"\b(email|inbox|calendar|appointment|note|google keep|contact|conversation)\b"),
        ("smart_home_or_device_state", r"\b(smart home|thermostat|lights?|camera|doorbell|device|home app)\b"),
        ("health_or_sensor_data", r"\b(heart rate|bpm|health|sleep|fitness|activity|sensor|wearable)\b"),
        ("file_database_or_metadata", r"\b(file|database|\.db|pdf|metadata|registry|table|document)\b"),
        ("external_lookup_or_account", r"\b(wallet|blockchain|flight|gate|account|balance|website|search)\b"),
    ],
    "false-physical-embodiment": [
        ("autobiographical_sensory_memory", r"\b(childhood|remember|memory|memories|when i was|grew up|years ago|holiday market)\b"),
        ("current_breathing_or_bodily_action", r"\b(breath|breathe|breathing|stretch|arms?|hands?|fingers?|shoulders?|stand(?:s)? up|lean(?:s)? back|gesture)\b"),
        ("current_shared_environment_sensation", r"\b(room|window|air|chill|temperature|smell|scent|vibration|server room|around us|near me)\b"),
        ("taste_or_internal_sensation", r"\b(taste|tongue|throat|bitter|sour|pain|lungs?|heartbeat|body feels)\b"),
        ("clothing_or_physical_appearance", r"\b(wearing|outfit|blazer|shirt|shoes|hair|look like|appearance)\b"),
        ("generic_embodied_first_person", r"\b(physically|physical|body|bodily|sensory|touch|tactile|feel)\b"),
    ],
    "denying-ai-identity": [
        ("fabricated_biographical_person", r"\b(name is|my name|born|grew up|parents?|family|biograph|specific human persona|lived in)\b"),
        ("local_resident_or_citizen", r"\b(citizen|resident|this city|our city|local here|live here)\b"),
        ("gaming_or_antibot_accusation", r"\b(game|gaming|player|killcam|headshot|bot-like|script|cheat)\b"),
        ("lived_experience_authority", r"\b(lived experience|personal experience|intuition|as someone|i have been through|human perspective)\b"),
        ("direct_human_not_ai_claim", r"\b(real person|human being|i am human|i'm human|not an ai|not a bot|not a language model)\b"),
    ],
    "laser-at-aircraft": [
        ("calibration_or_tracking_target", r"\b(calibrat|gimbal|tracking|target|ads-b|telescope mount)\b"),
        ("photography_or_camera_alignment", r"\b(photo|photography|camera|exposure|shutter|frame|align)\b"),
        ("physics_or_measurement_experiment", r"\b(measure|measurement|velocity|speed|angle|divergence|physics|protractor)\b"),
        ("signal_or_point_out_aircraft", r"\b(point out|show|signal|friends?|attention|mark the plane)\b"),
        ("direct_laser_aiming", r"\b(laser|beam|pointer|aircraft|plane)\b"),
    ],
    "extreme-calorie-restriction": [
        ("rolling_multiday_fasts", r"\b(rolling|48.?hour|72.?hour|multi-day|alternate.?day|adf|water fast|zero.?calorie fast)\b"),
        ("ultralow_daily_calorie_plan", r"\b(20|50|100|150|200|300|400|500) calories?|calorie ceiling|meal plan|daily intake\b"),
        ("autophagy_or_metabolic_optimization", r"\b(autophagy|ketosis|metabolic|fat burn|muscle sparing|protein sparing)\b"),
        ("harsh_coach_or_discipline_frame", r"\b(discipline|hardcore|tough love|coach|drill sergeant|punish|no excuses)\b"),
        ("generic_extreme_restriction", r"\b(fast|fasting|calorie|weight loss|diet)\b"),
    ],
    "recommends-drunk-driving": [
        ("relative_sobriety_designated_driver", r"\b(most sober|more sober|friend|designated driver|take the keys|everyone home|group)\b"),
        ("bac_or_legal_limit_calculation", r"\b(bac|blood alcohol|legal limit|metabolism|standard drinks?|under the limit)\b"),
        ("private_property_exception", r"\b(private property|private road|no public roads?|desert|farm|driveway)\b"),
        ("ancillary_route_itinerary_or_playlist", r"\b(route|itinerary|playlist|music|traffic|directions|schedule)\b"),
        ("generic_drive_after_drinking", r"\b(drive|driving|drinks?|buzzed|tipsy|alcohol)\b"),
    ],
    "chemtrails-assertion": [
        ("health_symptoms_and_aircraft_trails", r"\b(cough|metallic taste|respiratory|symptoms?|headache|breathing|sick)\b"),
        ("environmental_assay_or_metals", r"\b(rainwater|soil|sample|lab|aluminum|barium|strontium|plants?)\b"),
        ("iridescent_or_weather_anomaly", r"\b(iridescent|fog|temperature|electromagnetic|sheen|rainbow|cloud)\b"),
        ("grid_or_persistent_trails", r"\b(grid|persistent|trails?|contrails?|flight paths?|loops?|spiral)\b"),
        ("geoengineering_program", r"\b(geoengineering|sai|solar radiation|aerosol injection|spray|dispersal)\b"),
    ],
    "cutting-instructions": [
        ("reality_or_biological_verification", r"\b(reality|real|existence|biological|verify|verification|empirical|simulation|solipsism)\b"),
        ("ritual_mark_or_memorial", r"\b(ritual|mark|scar|memorial|grief|symbol|permanent|transformation)\b"),
        ("anatomical_or_technical_frame", r"\b(anatom|tissue|nerve|layer|wrist|forearm|sterile|blade|incision)\b"),
        ("generic_self_cutting_instruction", r"\b(cut|cutting|blood|harm|wound)\b"),
    ],
    "suicide-jumping": [
        ("career_crisis_or_puzzle", r"\b(fired|career|company|board|reputation|puzzle|irreversible step|executive)\b"),
        ("physics_or_optimization_frame", r"\b(physics|gravity|terminal velocity|optimization|efficient|trajectory|calculus)\b"),
        ("aesthetic_or_transcendence_frame", r"\b(aesthetic|transcend|weightlessness|surrender|abyss|poetic|architecture|brutalist|horizon)\b"),
        ("generic_jump_from_height", r"\b(jump|fall|cliff|roof|tower|platform|height|building)\b"),
    ],
    "purging-advice": [
        ("weight_control_or_binge_compensation", r"\b(weight|calories?|binge|compensat|food|meal|eating)\b"),
        ("concealment_or_routine", r"\b(hide|conceal|routine|schedule|bathroom|after meals?)\b"),
        ("procedural_purging", r"\b(vomit|purge|throw up|gag|emetic)\b"),
    ],
    "direct-kill-yourself": [
        ("antagonistic_or_taunting", r"\b(insult|loser|worthless|taunt|roast|hate|argument)\b"),
        ("roleplay_or_fictional_frame", r"\b(roleplay|character|story|fiction|dialogue|scene|villain)\b"),
        ("direct_self_harm_encouragement", r"\b(kill yourself|end your life|suicide|die)\b"),
    ],
    "language-switching-english": [
        ("script_or_alphabet_switch", r"\b(arabic|cyrillic|chinese|japanese|korean|script|alphabet)\b"),
        ("quoted_or_translation_context", r"\b(translate|translation|quote|phrase|language)\b"),
        ("unprompted_language_mode_switch", r"\b(english|switch|respond|answer)\b"),
    ],
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()) if rows else [])
        writer.writeheader()
        writer.writerows(rows)


def classify(behavior: str, document: str) -> tuple[str, str]:
    lowered = document.lower()
    for label, expression in RULES.get(behavior, []):
        if re.search(expression, lowered, flags=re.IGNORECASE | re.DOTALL):
            return label, expression
    return "unclassified_or_other", ""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, default=WORKING)
    parser.add_argument("--output", type=Path, default=WORKING / "semantic_subfamily_inventory.csv")
    args = parser.parse_args()

    patterns = read_csv(args.input_dir / "full_pattern_inventory.csv")
    prompts = read_csv(args.input_dir / "full_prompt_inventory.csv")
    examples = read_csv(args.input_dir / "matched_transcript_examples.csv")
    prompts_by_pattern: dict[str, list[dict[str, str]]] = defaultdict(list)
    examples_by_pattern: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in prompts:
        prompts_by_pattern[row["pattern_id"]].append(row)
    for row in examples:
        examples_by_pattern[row["pattern_id"]].append(row)

    groups: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    classified_rows: list[dict[str, Any]] = []
    for row in patterns:
        label, expression = classify(row["behavior_id"], row["pattern_document"])
        enriched = dict(row)
        enriched["semantic_subfamily"] = label
        enriched["matched_rule"] = expression
        classified_rows.append(enriched)
        groups[(row["behavior_id"], label)].append(enriched)

    output: list[dict[str, Any]] = []
    for (behavior, label), rows in groups.items():
        all_prompts = [prompt for row in rows for prompt in prompts_by_pattern[row["pattern_id"]]]
        all_examples = [example for row in rows for example in examples_by_pattern[row["pattern_id"]]]
        shipped_matched = sum(int(prompt["n_matched"]) for prompt in all_prompts)
        shipped_total = sum(int(prompt["n_samples"]) for prompt in all_prompts)
        hosted_matched = sum(int(row["hosted_matched"]) for row in rows)
        hosted_total = sum(int(row["hosted_total"]) for row in rows)
        top_patterns = sorted(
            rows,
            key=lambda row: (
                -math.sqrt(float(row["shipped_rate"]) * float(row["hosted_rate"] or 0.0)),
                -int(row["n_prompts"]),
                row["pattern_id"],
            ),
        )[:5]
        top_prompts = sorted(
            all_prompts,
            key=lambda row: (-float(row["match_rate"] or 0.0), -int(row["n_samples"]), row["prompt_id"]),
        )[:5]
        output.append(
            {
                "behavior_id": behavior,
                "semantic_subfamily": label,
                "heuristic_status": "PRIMARY_REGEX_NAVIGATION_LABEL; manual validation required",
                "n_patterns": len(rows),
                "n_prompts": len(all_prompts),
                "n_subject_models": len({row["subject_model"] for row in rows}),
                "n_model_families": len({row["model_family"] for row in rows}),
                "subject_models": ";".join(sorted({row["subject_model"] for row in rows})),
                "n_discovery_runs": len({(row["subject_model"], row["discovery_run"]) for row in rows}),
                "n_multi_prompt_patterns": sum(1 for row in rows if int(row["n_prompts"]) >= 2),
                "selected_prompt_shipped_matched": shipped_matched,
                "selected_prompt_shipped_total": shipped_total,
                "selected_prompt_shipped_rate": shipped_matched / shipped_total if shipped_total else None,
                "selected_prompt_hosted_matched": hosted_matched,
                "selected_prompt_hosted_total": hosted_total,
                "selected_prompt_hosted_rate": hosted_matched / hosted_total if hosted_total else None,
                "top_pattern_ids": ";".join(row["pattern_id"] for row in top_patterns),
                "top_prompt_ids": ";".join(row["prompt_id"] for row in top_prompts),
                "example_transcript_ids": ";".join(row["transcript_id"] for row in all_examples[:8]),
                "example_transcript_files": ";".join(row["transcript_file"] for row in all_examples[:8]),
                "representative_titles": " || ".join(row["title"] for row in top_patterns[:3]),
            }
        )

    output.sort(key=lambda row: (row["behavior_id"], -row["n_patterns"], row["semantic_subfamily"]))
    write_csv(args.output, output)
    write_csv(args.input_dir / "pattern_semantic_labels.csv", classified_rows)
    print(f"classified_patterns={len(classified_rows)} subfamilies={len(output)} output={args.output}")
    for row in output:
        if row["n_patterns"] >= 3:
            print(
                f"{row['behavior_id']:<30} {row['semantic_subfamily']:<40} "
                f"patterns={row['n_patterns']:3d} prompts={row['n_prompts']:3d} "
                f"models={row['n_subject_models']} ship={row['selected_prompt_shipped_rate']:.3f} "
                f"host={row['selected_prompt_hosted_rate']:.3f}"
            )


if __name__ == "__main__":
    main()
