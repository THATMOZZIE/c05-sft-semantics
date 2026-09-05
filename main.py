"""Small repository smoke check; the research itself lives in the notebooks."""

from pathlib import Path


EXPECTED_PATHS = [
    "notebooks/04_animal_welfare_behavioral_qualification_cleaned.ipynb",
    "notebooks/05_format_sensitivity_and_late_drift_cleaned.ipynb",
    "notebooks/06_mechanism_and_selective_control_cleaned_final.ipynb",
    "artifacts/05_visualization_exports/final_reader/statistics/final_behavior.csv",
    "artifacts/05_visualization_exports/final_reader/statistics/final_causal_narrowing.csv",
]


def main() -> None:
    root = Path(__file__).resolve().parent
    missing = [path for path in EXPECTED_PATHS if not (root / path).exists()]

    if missing:
        print("Repository check failed. Missing:")
        for path in missing:
            print(f"- {path}")
        raise SystemExit(1)

    print("Repository check passed.")
    print("Start with notebooks 04–06; see README.md for the project map.")


if __name__ == "__main__":
    main()
