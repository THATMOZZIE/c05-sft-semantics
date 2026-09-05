"""Build the compact paper version of Figure 4 from saved statistics."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = (
    ROOT
    / "artifacts"
    / "05_visualization_exports"
    / "final_reader"
    / "statistics"
    / "final_causal_narrowing.csv"
)
OUTPUT_DIR = (
    ROOT
    / "artifacts"
    / "05_visualization_exports"
    / "final_reader"
    / "figures"
)

INK = "#202B36"
MUTED = "#7B8792"
GRID = "#DDE4E8"
BLUE = "#88B7CC"
ORANGE = "#B94D1B"
ORANGE_PALE = "#F7E8DF"

STAGES = [
    ("Broad groups", "A. Broad layer groups"),
    ("Split of layers 0–7", "B. Split of the early group"),
    ("Single layers", "C. Single-layer checks"),
    ("Learned parts tested", "D. Learned components tested"),
]


def build_figure(results: pd.DataFrame) -> plt.Figure:
    """Return a compact four-panel view of the causal narrowing path."""

    required = {"stage", "key", "label", "sites", "extra", "selected"}
    missing = required.difference(results.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")

    expected_keys = {
        "layers_0_7",
        "layers_8_15",
        "layers_16_23",
        "layers_24_31",
        "layers_0_3",
        "layers_4_7",
        "layer_4",
        "layer_5",
        "layer_6",
        "layer_7",
        "layers_4_7_mlp",
        "layers_4_7_attn",
    }
    if set(results["key"]) != expected_keys:
        raise ValueError("The saved causal rows do not match the frozen figure plan.")

    height_ratios = [4, 2, 4, 2]
    fig, axes = plt.subplots(
        4,
        1,
        figsize=(7.0, 7.15),
        sharex=True,
        gridspec_kw={"height_ratios": height_ratios},
    )

    for ax, (stage, panel_title) in zip(axes, STAGES):
        panel = results.loc[results["stage"].eq(stage)].reset_index(drop=True)
        y = np.arange(len(panel))

        for row_number, row in panel.iterrows():
            selected = bool(row["selected"])
            color = ORANGE if selected else BLUE

            if selected:
                ax.axhspan(
                    row_number - 0.42,
                    row_number + 0.42,
                    color=ORANGE_PALE,
                    zorder=0,
                )

            ax.plot(
                [0, row["extra"]],
                [row_number, row_number],
                color=color,
                linewidth=2.4 if selected else 2.0,
                solid_capstyle="round",
                zorder=2,
            )
            ax.scatter(
                row["extra"],
                row_number,
                s=64 if selected else 48,
                color=color,
                edgecolor="white",
                linewidth=0.8,
                zorder=3,
            )
            ax.text(
                row["extra"] + 0.035,
                row_number,
                f'{row["extra"]:.3f}',
                va="center",
                ha="left",
                fontsize=9.5,
                color=INK,
                weight="bold" if selected else "normal",
            )

        labels = [
            f'{row.label}  ({int(row.sites)} sites)'
            for row in panel.itertuples(index=False)
        ]
        labels = [
            label.replace("Normal attention tested", "Attention tested")
            for label in labels
        ]

        ax.set_yticks(y, labels, fontsize=9.5, color=INK)
        ax.set_ylim(len(panel) - 0.35, -0.55)
        ax.set_title(
            panel_title,
            loc="left",
            fontsize=10.5,
            weight="bold",
            color=MUTED,
            pad=7,
        )
        ax.set_xlim(-0.04, 1.66)
        ax.set_axisbelow(True)
        ax.xaxis.grid(True, color=GRID, linewidth=0.8)
        ax.yaxis.grid(False)
        ax.tick_params(axis="y", length=0, pad=8)
        ax.tick_params(axis="x", colors=INK, labelsize=9)

        for spine in ["top", "right", "left"]:
            ax.spines[spine].set_visible(False)
        ax.spines["bottom"].set_color(INK if ax is axes[-1] else GRID)
        ax.spines["bottom"].set_linewidth(0.9)

    axes[-1].set_xticks([0.0, 0.4, 0.8, 1.2, 1.6])
    axes[-1].set_xlabel(
        "Mean extra loss at welfare onset\n"
        "welfare target minus nearby-text control",
        fontsize=10.5,
        color=INK,
        labelpad=8,
    )

    fig.suptitle(
        "Causal narrowing points to MLP layers 4–7",
        x=0.5,
        y=0.985,
        ha="center",
        fontsize=17,
        weight="bold",
        color=INK,
    )
    fig.text(
        0.5,
        0.947,
        "The joint effect is much larger than any single-layer effect.",
        ha="center",
        va="top",
        fontsize=9.8,
        color=MUTED,
    )

    fig.subplots_adjust(
        left=0.31,
        right=0.94,
        top=0.89,
        bottom=0.105,
        hspace=0.75,
    )
    return fig


def main() -> None:
    results = pd.read_csv(INPUT_PATH)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    figure = build_figure(results)
    png_path = OUTPUT_DIR / "Figure_4_causal_narrowing.png"
    svg_path = OUTPUT_DIR / "Figure_4_causal_narrowing.svg"

    figure.savefig(png_path, dpi=300, bbox_inches="tight", facecolor="white")
    figure.savefig(svg_path, bbox_inches="tight", facecolor="white")
    plt.close(figure)

    print(f"Saved: {png_path}")
    print(f"Saved: {svg_path}")


if __name__ == "__main__":
    main()
