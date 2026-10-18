"""Draw three separate reported power-system study results; rerun no experiments.

Inputs: power_only_papers.json. Outputs: images/power_study_*.png/pdf/svg
and power_study_statistics.json. Vector files contain native vector marks/text.
"""
from pathlib import Path
import json
import os
import sys
import tempfile

ROOT = Path(__file__).resolve().parent.parent
IMAGES = ROOT / "images"
sys.path.insert(0, str(ROOT / "diagrams" / "_rigorous_build" / "pythonpackages"))
os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "power_study_matplotlib"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
from PIL import Image

BLUE, CYAN, ORANGE = "#00629B", "#00A8C8", "#B65B14"
NAVY, GRAY, GRID = "#003B5C", "#74828C", "#D9E3E9"
DATA = json.loads((ROOT / "research" / "power_only_papers.json").read_text(encoding="utf-8"))
PAPERS = {item["id"]: item for item in DATA["papers"]}


def style_axis(ax):
    ax.set_axisbelow(True)
    ax.grid(axis="x", color=GRID, linewidth=0.8)
    ax.tick_params(axis="y", length=0, pad=12, labelsize=21, colors=NAVY)
    ax.tick_params(axis="x", labelsize=15, colors=GRAY)
    for spine in ax.spines.values():
        spine.set_visible(False)


def save(fig, stem):
    # A fixed canvas makes the same graphic predictable in LaTeX and Slidev.
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    width, height = fig.canvas.get_width_height()
    for artist in fig.findobj(matplotlib.text.Text):
        if artist.get_visible() and artist.get_text().strip():
            bounds = artist.get_window_extent(renderer=renderer)
            assert bounds.x0 >= -1 and bounds.y0 >= -1 and bounds.x1 <= width+1 and bounds.y1 <= height+1, (stem, artist.get_text(), tuple(bounds.bounds))
    for ext in ("png", "pdf", "svg"):
        fig.savefig(IMAGES / f"{stem}.{ext}", dpi=220, facecolor="white",
                    metadata={"Creator": "Power-system tutorial research chart builder"})
    plt.close(fig)


def feedback():
    rows = PAPERS["E02"]["main_chart"]["rows"]
    labels = ["GPT4o-Sole", "GPT4o-SR", "CGPT4o-R", "GPT4o-Full"]
    values = [row[1] for row in rows]
    fig, ax = plt.subplots(figsize=(12, 3.6))
    fig.subplots_adjust(left=0.25, right=0.97, top=0.96, bottom=0.25)
    ax.barh(range(4), values, height=0.48, color=[GRAY, BLUE, ORANGE, CYAN])
    ax.set_yticks(range(4), labels)
    ax.invert_yaxis()
    ax.set_xlim(0, 108)
    ax.set_xticks([0, 20, 40, 60, 80, 100])
    ax.set_xlabel("Attempt-averaged score (%)", fontsize=19, color=NAVY, labelpad=9)
    style_axis(ax)
    for y, value in enumerate(values):
        ax.text(value + 1.4, y, f"{value:.2f}", va="center", fontsize=23,
                weight="bold", color=NAVY)
    save(fig, "power_study_feedback")


def veragrid():
    # First three table rows are an explicit representative selection, not a rank.
    rows = PAPERS["E04"]["raw_chart_rows"][:3]
    fig, ax = plt.subplots(figsize=(12, 3.6))
    fig.subplots_adjust(left=0.28, right=0.95, top=0.87, bottom=0.25)
    ys = [0, 1.2, 2.4]
    for i, (model, no_tool, agent, n) in enumerate(rows):
        ax.barh(ys[i] - 0.20, no_tool, height=0.33, color=BLUE,
                label="No tool" if i == 0 else None)
        ax.barh(ys[i] + 0.20, agent, height=0.33, color=CYAN,
                label="Solver agent" if i == 0 else None)
        ax.text(no_tool + 2, ys[i] - 0.20, f"{no_tool}/{n}", va="center",
                fontsize=19, weight="bold", color=NAVY)
        ax.text(agent - 2, ys[i] + 0.20, f"{agent}/{n}", ha="right", va="center",
                fontsize=19, weight="bold", color=NAVY)
    ax.set_yticks(ys, [row[0] for row in rows])
    ax.invert_yaxis()
    ax.set_xlim(0, 155)
    ax.set_xticks([0, 30, 60, 90, 120, 150])
    ax.set_xlabel("Correct answers (out of 150 questions)", fontsize=18, color=NAVY, labelpad=9)
    style_axis(ax)
    ax.legend(loc="lower left", bbox_to_anchor=(0, 1.01), ncols=2,
              frameon=False, fontsize=17, labelcolor=NAVY, borderaxespad=0)
    save(fig, "power_study_veragrid")


def xgrid():
    rows = PAPERS["E01"]["chart_ready_case_results"][1]["rows"]
    fig = plt.figure(figsize=(12, 3.6))
    grid = fig.add_gridspec(1, 2, width_ratios=[3.2, 1.6], left=0.18,
                          right=0.99, top=0.96, bottom=0.25, wspace=0.27)
    ax = fig.add_subplot(grid[0, 0])
    for y, row in enumerate(rows[:2]):
        value = row[1]
        ax.scatter([value], [y], s=180, color=[BLUE, CYAN][y], zorder=3)
        ax.text(value, y - 0.24, f"{value:,.2f}", ha="center", va="center",
                fontsize=22, weight="bold", color=NAVY)
    ax.set_yticks([0, 1], ["Base case", "Line 11 out"])
    ax.set_ylim(1.42, -0.55)
    ax.set_xlim(41700, 42300)
    ax.set_xticks([41800, 42000, 42200])
    ax.xaxis.set_major_formatter(StrMethodFormatter("{x:,.0f}"))
    ax.set_xlabel("Reported OPF objective", fontsize=18, color=NAVY, labelpad=9)
    style_axis(ax)
    unavailable = fig.add_subplot(grid[0, 1])
    unavailable.set_axis_off()
    unavailable.text(0.5, 0.90, "All loads doubled", ha="center", va="center",
                     fontsize=20, color=NAVY, transform=unavailable.transAxes)
    unavailable.text(0.5, 0.60, "×", ha="center", va="center", fontsize=48,
                     color=ORANGE, transform=unavailable.transAxes)
    unavailable.text(0.5, 0.33, "NOT CONVERGED", ha="center", va="center",
                     fontsize=18, weight="bold", color=ORANGE,
                     transform=unavailable.transAxes)
    unavailable.text(0.5, 0.12, "No objective value", ha="center", va="center",
                     fontsize=17, color=GRAY, transform=unavailable.transAxes)
    save(fig, "power_study_xgrid")


def records():
    specs = {
        "feedback": {
            "source_refs": ["E02"],
            "source_url": "https://arxiv.org/pdf/2411.16707v3",
            "source_locator": "Section V.A–B, PDF p.9; Figure 8, p.11; scheme definitions Table I, p.7",
            "caption": "DALINE graded attempt-averaged scores: GPT4o-Sole 0.00, GPT4o-SR 31.37, CGPT4o-R 33.82 and GPT4o-Full 93.13. The evaluation uses 34 tasks with a maximum of three attempts each, awarding 100/50/0 points and carrying the last executed score into unused slots. This is not a final-completion fraction.",
            "assumptions": "Reported values preserved. API schemes use gpt-4o-2024-05-13; CGPT4o-R is the ChatGPT4o built-in-RAG product scheme. Complete-system comparison, not isolated causal effects. No binomial interval or implied completed-task count.",
            "metric": "Paper-defined attempt-averaged score (%)",
            "data": PAPERS["E02"]["main_chart"]["rows"],
            "setup": {"tasks":34, "attempt_budget":3, "tool":"DALINE", "human_grading":True},
        },
        "veragrid": {
            "source_refs": ["E04", "E04C"],
            "source_url": "https://arxiv.org/pdf/2607.25155v1",
            "source_locator": "Table I, PDF p.4; benchmark definition Section III, p.3",
            "caption": "Three explicitly selected same-model comparisons from VeraGrid-MCQ-150: GPT-5.2 64/150 without tools versus 149/150 with the solver-agent; Claude Sonnet 4.5 71/150 versus 149/150; Gemini 3 Flash 74/150 versus 150/150. Questions use one balanced 8-bus feeder and a VeraGrid reference solve.",
            "assumptions": "First three Table I rows selected for legibility, not ranked. Template-derived MCQs share one solved feeder. Repeated-run uncertainty is unspecified; results do not estimate field-control reliability or arbitrary-feeder generalization.",
            "metric":"Correct MCQ answers / 150",
            "columns":PAPERS["E04"]["raw_chart_columns"],
            "data":PAPERS["E04"]["raw_chart_rows"][:3],
            "setup":{"questions":150,"tiers":{"easy":50,"medium":50,"hard":50},"buses":8,"generators":4,"load_MW":185,"repetitions":"unspecified"},
        },
        "xgrid": {
            "source_refs":["E01"],
            "source_url":"https://arxiv.org/pdf/2512.20789v1",
            "source_locator":"Table I, Q10, PDF p.9",
            "caption":"X-GridAgent's reported IEEE39 scenario outputs: base-case objective 41,872.30, line11-out objective 42,115.34, and nonconverged AC OPF when all loads are doubled. The third scenario has no objective value; it is displayed outside the numerical axis. This is a scenario output, not an accuracy comparison.",
            "assumptions":"Objective units are not specified in the paper table; no currency/hour unit invented. The dot-plot axis is deliberately zoomed and has no zero baseline; dots encode reported values, not bars. Nonconvergence is not represented as zero.",
            "metric":"Reported total-generation-cost OPF objective (units unspecified)",
            "columns":PAPERS["E01"]["chart_ready_case_results"][1]["columns"],
            "data":PAPERS["E01"]["chart_ready_case_results"][1]["rows"],
            "setup":{"case":"IEEE 39-bus","scenarios":3,"converged":2,"nonconverged":1},
        },
    }
    for key, rec in specs.items():
        stem = f"power_study_{key}"
        rec.update({"id":stem,"plot_id":stem,"file":stem+".png","pdf":stem+".pdf","svg":stem+".svg",
                    "credit":"Original plot redrawn from cited primary-paper numerical results; no experiments rerun",
                    "value_status":"author-reported","uncertainty_intervals":None})
    return specs


def validate():
    for stem in ("power_study_feedback", "power_study_veragrid", "power_study_xgrid"):
        for ext in ("png", "pdf", "svg"):
            path = IMAGES / f"{stem}.{ext}"
            assert path.exists() and path.stat().st_size > 1000, path
        with Image.open(IMAGES / (stem+".png")) as im:
            assert im.size == (2640, 792), im.size
            im.verify()
        pdf = (IMAGES / (stem+".pdf")).read_bytes()
        svg = (IMAGES / (stem+".svg")).read_text(encoding="utf-8")
        assert pdf.startswith(b"%PDF") and b"/Subtype /Image" not in pdf
        assert "<svg" in svg and "<image" not in svg


def main():
    IMAGES.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({"font.family":"DejaVu Sans", "font.size":15,
                         "svg.fonttype":"path", "pdf.fonttype":42})
    feedback()
    veragrid()
    xgrid()
    (IMAGES / "power_study_statistics.json").write_text(json.dumps(records(), ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    validate()
    print(json.dumps({"charts":3,"formats":["png","pdf","svg"],"data":"power_only_papers.json","manifest":"images/power_study_statistics.json"}))


if __name__ == "__main__":
    main()
