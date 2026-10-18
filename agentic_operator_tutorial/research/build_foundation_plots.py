"""Rebuild five standalone historical-paper result charts and provenance.

Run with Python. Matplotlib/Pillow can be provided by the existing tutorial
diagrams/_rigorous_build/pythonpackages directory. No experiments are rerun.
Only the expanded_foundation_* images and statistics JSON are written
inside the tutorial; the visual-QA contact sheet is written to the system temp dir.
"""
from pathlib import Path
import json
import os
import sys
import tempfile

ROOT = Path(__file__).resolve().parent.parent
IMAGES = ROOT / "images"
PACKAGES = ROOT / "diagrams" / "_rigorous_build" / "pythonpackages"
sys.path.insert(0, str(PACKAGES))
os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "foundation_matplotlib"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image, ImageOps, ImageDraw

BLUE, CYAN, ORANGE = "#00629B", "#00A8C8", "#B65B14"
NAVY, GRAY, GRID = "#003B5C", "#74828C", "#D9E3E9"

CHARTS = {
    "react_webshop": {
        "id": "expanded_foundation_react", "source_refs": ["F01"],
        "title": "ReAct: reasoning alongside actions",
        "metric": "WebShop success rate (%)",
        "labels": ["Act-only", "ReAct"], "values": [30.1, 40.0],
        "colors": [BLUE, CYAN], "percent_labels": True,
        "footnote": "PaLM 540B | 500 test instructions | F01, Table 4, PDF p.8\nReported rates; no uncertainty interval or success counts inferred.",
        "source_url": "https://arxiv.org/pdf/2210.03629v3",
        "source_locator": "Table 4, PDF p.8; evaluation setup, PDF p.7",
        "caption": "Reported WebShop success rates: Act-only 30.1%, ReAct 40.0%, using PaLM 540B and 500 test instructions. Success requires satisfying all product requirements. These historical benchmark results are distinct from task score and from LATS's different WebShop experiment.",
        "assumptions": "Reported rates preserved. No integer success counts, confidence intervals, replication model, or current production performance inferred.",
        "setup": {"model":"PaLM 540B", "dataset":"WebShop", "evaluated_n":500, "n_unit":"test instructions", "repetitions":"not established for plotted cells"},
    },
    "toolformer_mawps": {
        "id": "expanded_foundation_toolformer", "source_refs": ["F02"],
        "title": "Toolformer: the same model with API calls enabled",
        "metric": "MAWPS first-number accuracy (%)",
        "labels": ["API calls disabled", "API calls enabled"], "values": [15.0, 44.0],
        "colors": [BLUE, CYAN], "percent_labels": True,
        "footnote": "Same fine-tuned GPT-J | at most one API call per input | F02, Table 3, PDF p.6\nExact evaluated n undisclosed; reported accuracy, not process reliability.",
        "source_url": "https://proceedings.neurips.cc/paper_files/paper/2023/file/d842425e4bf79ba039352da0f658a906-Paper-Conference.pdf",
        "source_locator": "Table 3 and math-benchmark evaluation criterion, PDF p.6",
        "caption": "Reported MAWPS accuracy is 15.0% with API calls disabled and 44.0% enabled for the same fine-tuned GPT-J Toolformer model. The evaluation checks the first generated number, or the first number following an equals sign in an equation. Decoding allows at most one API call per input. Exact evaluated n is undisclosed.",
        "assumptions": "Same-model decoding ablation. This first-number criterion is more lenient than full-solution correctness. No confidence intervals or sample count inferred.",
        "setup": {"model":"GPT-J, fine-tuned Toolformer", "dataset":"MAWPS", "evaluated_n":None, "n_note":"exact evaluated count undisclosed", "max_api_calls_per_input":1},
    },
    "reflexion_ablation": {
        "id": "expanded_foundation_reflexion", "source_refs": ["F03"],
        "title": "Reflexion: tests and reflection work together here",
        "metric": "HumanEval Rust pass@1 accuracy (%)",
        "labels": ["Base model", "Reflection without tests", "Tests without reflection", "Full Reflexion"],
        "values": [60.0, 52.0, 60.0, 68.0],
        "colors": [BLUE, ORANGE, GRAY, CYAN], "percent_labels": True,
        "footnote": "GPT-4 | 50 hardest translated HumanEval Rust tasks | F03, Table 3, PDF p.8\nReported accuracy; this ablation does not establish a universal reflection benefit.",
        "source_url": "https://proceedings.neurips.cc/paper_files/paper/2023/file/1b44b878bb782e6954cd888628510e90-Paper-Conference.pdf",
        "source_locator": "Table 3, PDF p.8; subset description in Table 2 and adjoining text",
        "caption": "Reported pass@1 accuracy on the 50 hardest HumanEval problems translated to Rust: GPT-4 base model 60%, reflection without test generation 52%, tests without reflection 60%, full Reflexion 68%. The ablation separates internal test generation/execution from natural-language reflection. It is specific to this selected hard programming subset.",
        "assumptions": "Percentages converted directly from reported 0.60, 0.52, 0.60 and 0.68. No uncertainty intervals or success counts inferred. Tests and compiler feedback are task-specific evidence.",
        "setup": {"model":"GPT-4", "dataset":"HumanEval Rust, 50 hardest tasks", "evaluated_n":50, "n_unit":"selected translated programming problems"},
    },
    "lats_webshop": {
        "id": "expanded_foundation_lats", "source_refs": ["F04"],
        "title": "LATS: searching alternative action paths",
        "metric": "WebShop task score (0–100)",
        "labels": ["Reflexion", "LATS (ReAct)"], "values": [64.2, 75.9],
        "colors": [BLUE, CYAN], "percent_labels": False,
        "footnote": "GPT-3.5 | 50 instructions | 30 trajectories | F04, Table 6, PDF p.8\nScore = 100 × mean reward; equal trajectory count is not equal token cost.",
        "source_url": "https://arxiv.org/pdf/2310.04406v3",
        "source_locator": "Table 6 and Section 5.3, PDF p.8; Appendix D.3, PDF pp.16–17",
        "caption": "Reported WebShop task score is 64.2 for Reflexion and 75.9 for LATS (ReAct), with GPT-3.5 on 50 instructions. Score equals 100 times mean environment reward and is separate from success rate. Both methods use up to 30 trajectories; LATS expands five children. Equal trajectory count does not imply equal model-call or token budgets.",
        "assumptions": "Historical prompting-method comparison, not a cross-paper ranking. Exact model snapshot and repeated-run uncertainty undisclosed. LATS requires environment reversion; the benchmark is a controlled shopping environment.",
        "setup": {"model":"GPT-3.5", "model_snapshot":"unspecified", "dataset":"WebShop", "evaluated_n":50, "n_unit":"instructions/environments", "max_trajectories":30, "lats_children_per_expansion":5},
    },
    "aflow_mbpp": {
        "id": "expanded_foundation_aflow", "source_refs": ["F05"],
        "title": "AFlow: optimizing the workflow before use",
        "metric": "MBPP pass@1 (%)",
        "labels": ["Best manual workflows", "AFlow workflow"], "values": [73.6, 83.4],
        "colors": [BLUE, CYAN], "percent_labels": True,
        "footnote": "GPT-4o-mini executor | mean of 3 test runs | F05, Table 1, PDF p.8\nExact test n undisclosed; best manual value is shared by three methods.",
        "source_url": "https://arxiv.org/pdf/2410.10762v4",
        "source_locator": "Table 1 and Section 5.1, PDF pp.7–8",
        "caption": "Reported MBPP pass@1 is 73.6% for the best manual baselines (CoT self-consistency, MedPrompt and MultiPersona tie) and 83.4% for AFlow, all executed with GPT-4o-mini. Table 1 averages three test runs. The paper states a 20% validation/80% test split with seed 42 but does not disclose the exact MBPP test count. Workflow search uses Claude-3.5-sonnet as optimizer.",
        "assumptions": "Same-executor workflow comparison. Selecting the largest reported manual-baseline value is a descriptive comparison. No confidence intervals or exact test count inferred; no deployment reliability claim.",
        "setup": {"executor":"GPT-4o-mini-0718", "optimizer":"Claude-3.5-sonnet", "dataset":"MBPP", "evaluated_n":None, "n_note":"exact test count undisclosed", "test_repetitions":3, "aggregation":"mean", "validation_fraction":0.2, "test_fraction":0.8, "split_seed":42},
    },
}


def draw_chart(spec):
    fig, ax = plt.subplots(figsize=(12.0, 3.6), facecolor="white")
    fig.subplots_adjust(left=0.31, right=0.96, top=0.97, bottom=0.25)
    ys = list(range(len(spec["labels"])))
    ax.barh(ys, spec["values"], height=0.48, color=spec["colors"])
    ax.set_yticks(ys, spec["labels"], fontsize=20, color=NAVY)
    ax.invert_yaxis()
    ax.set_xlim(0, 100)
    ax.set_xticks([0, 20, 40, 60, 80, 100])
    ax.tick_params(axis="y", length=0, pad=12)
    ax.tick_params(axis="x", colors=GRAY, labelsize=14)
    ax.set_xlabel(spec["metric"], fontsize=17, color=NAVY, labelpad=8)
    ax.set_axisbelow(True)
    ax.grid(axis="x", color=GRID, linewidth=0.8)
    for spine in ax.spines.values():
        spine.set_visible(False)
    suffix = "%" if spec["percent_labels"] else ""
    for y, v in zip(ys, spec["values"]):
        ax.text(v + 1.6, y, f"{v:.1f}{suffix}", color=NAVY,
                fontsize=24, va="center", weight="bold")
    for ext in ("png", "pdf", "svg"):
        fig.savefig(IMAGES / f"{spec['id']}.{ext}", dpi=220,
                    facecolor="white", metadata={"Creator":"Tutorial research chart builder"})
    plt.close(fig)


def metadata(spec):
    result = {k:spec[k] for k in ("id", "title", "caption", "assumptions", "source_url", "source_refs", "source_locator", "setup")}
    result.update({
        "id":spec["source_refs"][0],
        "plot_id":spec["id"],
        "metric":spec["metric"],
        "data":[{"method":k,"reported_value":v} for k,v in zip(spec["labels"],spec["values"])],
        "value_status":("author-reported fractions expressed as percentages" if spec["source_refs"] == ["F03"] else "author-reported"),
        "uncertainty_intervals":None,
        "derived_delta":None,
        "file":f"{spec['id']}.png", "pdf":f"{spec['id']}.pdf", "svg":f"{spec['id']}.svg",
        "credit":"Original plot derived from cited primary-paper data; no experiments rerun",
    })
    return result


def validate_outputs():
    for spec in CHARTS.values():
        stem = IMAGES / spec["id"]
        for ext in ("png", "pdf", "svg"):
            path = stem.with_suffix("." + ext)
            assert path.exists() and path.stat().st_size > 1000, path
        with Image.open(stem.with_suffix(".png")) as im:
            assert im.width >= 2600 and im.height >= 750
            im.verify()
        pdf = stem.with_suffix(".pdf").read_bytes()
        svg = stem.with_suffix(".svg").read_text(encoding="utf-8")
        assert pdf.startswith(b"%PDF") and b"/Subtype /Image" not in pdf
        assert "<svg" in svg and "<image" not in svg
    content = json.loads((IMAGES / "expanded_foundation_statistics.json").read_text(encoding="utf-8"))
    assert len(content) == 5


def contact_sheet():
    canvas = Image.new("RGB", (2340, 1120), "#EAF0F3")
    drawer = ImageDraw.Draw(canvas)
    for i,spec in enumerate(CHARTS.values()):
        with Image.open(IMAGES / f"{spec['id']}.png") as original:
            thumb = ImageOps.contain(original.convert("RGB"), (1150, 350))
        x,y = 10 + (i % 2)*1170, 10 + (i // 2)*370
        canvas.paste(thumb, (x,y))
    drawer.text((1190, 850), "Five separate historical results; no cross-paper ranking.", fill=NAVY)
    path = Path(tempfile.gettempdir()) / "expanded_foundation_contact_sheet.png"
    canvas.save(path)
    return path


def main():
    IMAGES.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({"font.family":"DejaVu Sans", "font.size":14,
                         "svg.fonttype":"path", "pdf.fonttype":42})
    for spec in CHARTS.values():
        draw_chart(spec)
    (IMAGES / "expanded_foundation_statistics.json").write_text(
        json.dumps({k:metadata(v) for k,v in CHARTS.items()}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    validate_outputs()
    print(json.dumps({"charts":len(CHARTS), "formats":["png","pdf","svg"],
                      "contact_sheet":str(contact_sheet()),
                      "metadata":str(IMAGES / "expanded_foundation_statistics.json")}, indent=2))


if __name__ == "__main__":
    main()
