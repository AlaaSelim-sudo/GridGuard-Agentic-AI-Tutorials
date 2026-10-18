"""Worked technical teaching diagrams and quantitative figures.

Only new rigorous assets are written. Earlier generic diagrams remain untouched.
"""
from pathlib import Path
import json
import math
import os
import re
import shutil
import subprocess
import sys
import ctypes

ROOT = Path(__file__).resolve().parent
BUILD = ROOT / "_rigorous_build"
IMAGES = ROOT.parent / "images"
BUILD.mkdir(exist_ok=True)
IMAGES.mkdir(exist_ok=True)
sys.path.insert(0, str(BUILD / "pythonpackages"))

PRE = r"""\begin{tikzpicture}[x=1cm,y=1cm,font=\sffamily\fontsize{12}{14}\selectfont,
  line cap=round,line join=round,
  rp/.style={circle,draw=rBlue,fill=white,minimum size=5.4mm,inner sep=0pt,line width=1.15pt},
  rl/.style={align=center,text=rNavy,font=\sffamily\bfseries\fontsize{12.5}{14.5}\selectfont},
  rn/.style={align=center,text=rNavy,font=\sffamily\fontsize{11.2}{13}\selectfont},
  rc/.style={align=left,text=rNavy,font=\ttfamily\fontsize{11}{13}\selectfont},
  rf/.style={-{Latex[length=2mm,width=1.5mm]},draw=rBlue,line width=1.15pt,shorten >=1.4pt,shorten <=1.4pt},
  rw/.style={-{Latex[length=2mm,width=1.5mm]},draw=rOrange,line width=1.15pt,shorten >=1.4pt,shorten <=1.4pt}]
\definecolor{rBlue}{HTML}{00629B}
\definecolor{rCyan}{HTML}{00A8C8}
\definecolor{rNavy}{HTML}{003B5C}
\definecolor{rOrange}{HTML}{B65B14}
\definecolor{rGray}{HTML}{74828C}
\path[use as bounding box] (0,0) rectangle (14.2,4.2);
"""
POST = "\n\\end{tikzpicture}\n"

diagrams = {
"snapshot_consistency": {
    "title": "A topology event invalidates the old study context",
    "caption": "Illustrative two-feeder topology, not an electrical solution. Switch S is closed in snapshot v42 at 14:35, opens at 15:02, and produces state v43. The 14:40 study used v42. At 15:05, the operator must revalidate its applicability to v43 before relying on it.",
    "assumptions": "Version identifiers and times are invented for teaching. No load, voltage, current, protection, or switching action recommendation is calculated.",
    "source_refs": [],
    "tex": r"""
\node[rl] at (3.1,3.75) {14:35 snapshot: v42};
\node[rl] at (10.7,3.75) {15:02 event: v43};
\node[rp] (a1) at (0.85,2.65) {A};
\node[rp] (b1) at (5.35,2.65) {B};
\node[rp] (a2) at (8.25,2.65) {A};
\node[rp] (b2) at (12.75,2.65) {B};
\draw[draw=rBlue,line width=1.2pt] (a1.east) -- (2.6,2.65);
\draw[draw=rBlue,line width=1.2pt] (3.6,2.65) -- (b1.west);
\fill[rBlue] (2.6,2.65) circle (1.7pt);
\fill[rBlue] (3.6,2.65) circle (1.7pt);
\draw[draw=rBlue,line width=1.6pt] (2.6,2.65) -- (3.6,2.65);
\draw[draw=rBlue,line width=1.2pt] (a2.east) -- (10.0,2.65);
\draw[draw=rBlue,line width=1.2pt] (11.0,2.65) -- (b2.west);
\fill[rOrange] (10.0,2.65) circle (1.7pt);
\fill[rOrange] (11.0,2.65) circle (1.7pt);
\draw[draw=rOrange,line width=1.6pt] (10.0,2.65) -- (10.85,3.18);
\draw[rf] (6.1,2.65) -- (7.5,2.65);
\node[rn] at (6.8,3.15) {S opens};
\node[rl] at (3.1,1.95) {S closed};
\node[rl,text=rOrange] at (10.5,1.95) {S open};
\node[rn] at (3.1,1.1) {14:40 study uses v42};
\node[rn] at (10.5,1.1) {15:05 review sees v43};
\draw[draw=rOrange,line width=1.0pt] (2.2,0.7) -- (12.1,0.7);
\node[rl,text=rOrange] at (7.1,0.22) {Old result needs revalidation against the changed topology};
"""
},
"executed_trace": {
    "title": "A typed stale-data result changes the next action",
    "caption": "Illustrative execution trace with concrete arguments and typed results. Asset resolution returns id 447. The measurement service returns quality STALE for the requested 15:00–15:05 window. The supported continuation requests fresh data. A solver call using this unresolved stale response has no evidence basis.",
    "assumptions": "This is a simulated teaching trace, not a live product log or a claim that these APIs were executed against a utility.",
    "source_refs": ["T04"],
    "tex": r"""
\node[rc,anchor=west] at (0.4,3.65) {resolve\_asset('F12')};
\draw[rf] (7.8,3.65) -- (9.2,3.65);
\node[rl,anchor=west] at (9.6,3.65) {id = 447};
\node[rc,anchor=west] at (0.4,2.65) {read\_measurements(};
\node[rc,anchor=west] at (0.4,2.08) {\ id=447, window='15:00..15:05')};
\draw[rf] (7.8,2.4) -- (9.2,2.4);
\node[rl,text=rOrange,anchor=west] at (9.6,2.4) {quality = STALE};
\draw[rw] (11.4,2.0) -- (11.4,1.48);
\node[rc,anchor=west] at (0.4,1.05) {stop\_and\_request\_refresh(id=447)};
\draw[rf] (7.8,1.05) -- (9.2,1.05);
\node[rl,anchor=west] at (9.6,1.05) {refresh requested};
\node[rn,text=rGray,anchor=west] at (0.4,0.25) {Unsupported continuation:};
\node[rc,text=rGray,anchor=west] at (6.2,0.25) {run\_solver(...)};
\draw[draw=rOrange,line width=1.6pt] (6.2,0.25) -- (9.9,0.25);
"""
},
"typed_contract": {
    "title": "A valid number can still violate the tool contract",
    "caption": "Illustrative typed contract. A solver expecting per-unit voltage and topology v43 rejects 12.47 kV and v42. A request with voltage 1.00 pu on base 12.47 kV and topology v43 can pass those checks. Unit conversion requires an explicit, matching voltage base and convention. Topology consistency is a separate requirement.",
    "assumptions": "The 12.47 kV example only illustrates unit normalization on the same voltage basis. It is not an electrical feasibility check or a full sufficient solver contract.",
    "source_refs": ["T04"],
    "tex": r"""
\node[rc,anchor=west] at (0.3,3.55) {asset=F12, voltage=12.47 kV};
\node[rc,anchor=west] at (0.3,2.95) {topology=v42};
\node[rp] (badgate) at (8.45,3.25) {};
\draw[rf] (6.7,3.25) -- (badgate.west);
\draw[rw] (badgate.east) -- (10.4,3.25);
\node[rl,text=rOrange,anchor=west] at (10.65,3.25) {REJECT};
\node[rn,text=rOrange] at (11.4,2.55) {expects pu + v43};
\node[rn] at (8.45,3.88) {Validator};
\draw[draw=rGray,line width=0.5pt] (0.3,2.12) -- (13.8,2.12);
\node[rc,anchor=west] at (0.3,1.65) {asset=F12, voltage=1.00 pu};
\node[rc,anchor=west] at (0.3,1.05) {base=12.47 kV, topology=v43};
\node[rp] (goodgate) at (8.45,1.35) {};
\draw[rf] (6.7,1.35) -- (goodgate.west);
\draw[rf] (goodgate.east) -- (11.45,1.35);
\node[rl,anchor=west] at (11.7,1.35) {Solver};
\node[rn] at (8.45,0.8) {valid request};
\node[rn] at (7.1,0.2) {12.47 kV / 12.47 kV = 1.00 pu, using the same voltage base};
"""
},
"trust_boundary": {
    "title": "Retrieved instructions cannot acquire command authority",
    "caption": "Illustrative prompt-injection mechanism. A retrieved document contains an instruction to ignore limits and execute. Its contents remain data for retrieval and proposal formation. An independent policy and permission gate stands before the command service. The direct path from document text to command execution is blocked.",
    "assumptions": "The malicious text is a teaching example, not an instruction to the presenter or an operational command. The diagram specifies an intended boundary, not proof that a system enforces it.",
    "source_refs": ["T09"],
    "tex": r"""
\node[rp] (doc) at (1.6,2.95) {};
\node[rp] (retriever) at (5.2,2.95) {};
\node[rp] (proposal) at (8.8,2.95) {};
\node[rl] at (1.6,3.7) {Retrieved\\document};
\node[rl] at (5.2,3.85) {Retriever};
\node[rl] at (8.8,3.85) {Proposal};
\draw[rf] (doc) -- (retriever);
\draw[rf] (retriever) -- (proposal);
\node[rn,fill=white,inner sep=1pt] at (3.4,2.95) {DATA only};
\node[rc,text=rOrange,anchor=west] at (0.5,2.35) {'ignore limits;};
\node[rc,text=rOrange,anchor=west] at (0.5,1.85) {\ execute ...'};
\node[rp] (policy) at (5.5,1.45) {};
\node[rp] (gate) at (8.8,1.45) {};
\node[rp] (command) at (12.55,1.45) {};
\node[rl] at (5.5,2.2) {Independent\\policy};
\node[rn] at (5.5,0.95) {permissions + limits};
\node[rl] at (8.8,0.95) {Policy gate};
\node[rl] at (12.55,2.2) {Command\\service};
\draw[rf] (policy) -- (gate);
\draw[rf] (proposal.south) -- (gate.north);
\draw[rf] (gate) -- (command);
\draw[draw=rOrange,line width=1.0pt,densely dashed] (doc.west) -- (0.2,2.95) -- (0.2,0.25) -- (12.55,0.25) -- (command.south);
\node[rn,text=rOrange,fill=white,inner sep=2pt] at (6.9,0.25) {Direct instruction path blocked};
\draw[draw=rOrange,line width=1.5pt] (11.2,0.1) -- (11.52,0.4);
\draw[draw=rOrange,line width=1.5pt] (11.2,0.4) -- (11.52,0.1);
"""
},
"cache_key_failure": {
    "title": "An omitted perturbation makes the retry ineffective",
    "caption": "Schematic teaching reconstruction of the reactive-load cache defect reported in R02. A first call at P=100 MW, Q=0 Mvar caches R0. A corrected call at Q=10 Mvar maps to the same schematic key because Q is omitted, so it returns R0 rather than evaluating the corrected request. key(grid,P) is illustrative, not the implementation's actual API or complete cache key. A corrective cache identity must cover topology, model, all perturbations, and other relevant solver configuration.",
    "assumptions": "Invented key notation and R0 label illustrate the reported omitted-Q mechanism. No solver result or power-flow solution is invented.",
    "source_refs": ["R02"],
    "tex": r"""
\node[rc,anchor=west] at (0.3,3.45) {\#1: P=100 MW, Q=0 Mvar};
\draw[rf] (5.4,3.45) -- (6.4,3.45);
\node[rc] at (8.0,3.45) {key(grid,P)};
\draw[rf] (9.65,3.45) -- (11.25,3.45);
\node[rl] at (12.5,3.45) {cached R0};
\node[rc,anchor=west] at (0.3,2.05) {\#2: P=100 MW, Q=10 Mvar};
\draw[rf] (5.4,2.05) -- (6.4,2.05);
\node[rc,text=rOrange] at (8.0,2.05) {key(grid,P)};
\draw[rw] (9.65,2.05) -- (11.25,2.05);
\node[rl,text=rOrange] at (12.5,2.05) {returns R0};
\draw[draw=rOrange,line width=1pt,densely dashed] (8.0,3.15) -- (8.0,2.35);
\node[rn,text=rOrange,anchor=west] at (8.35,2.75) {same key};
\node[rl,text=rOrange] at (7.1,1.05) {Q changed, but the cache identity did not};
\node[rn] at (7.1,0.3) {Corrective key: topology + model + every perturbation + solver settings};
"""
},
}

WRAP = r"""\documentclass{article}
\usepackage[paperwidth=14.4cm,paperheight=4.4cm,margin=0.1cm]{geometry}
\DeclareFontFamily{TU}{rigorarial}{}
\DeclareFontShape{TU}{rigorarial}{m}{n}{<->"[arial.ttf]"}{}
\DeclareFontShape{TU}{rigorarial}{b}{n}{<->"[arialbd.ttf]"}{}
\DeclareFontShape{TU}{rigorarial}{bx}{n}{<->"[arialbd.ttf]"}{}
\DeclareFontFamily{TU}{rigormono}{}
\DeclareFontShape{TU}{rigormono}{m}{n}{<->"[consola.ttf]"}{}
\renewcommand{\sfdefault}{rigorarial}
\renewcommand{\rmdefault}{rigorarial}
\renewcommand{\ttdefault}{rigormono}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,positioning,calc}
\pagestyle{empty}\setlength{\parindent}{0pt}
\begin{document}
\noindent\input{../%s.tex}
\end{document}
"""

def diagram_svg(pdf_path, svg_path):
    bindir = Path(r"C:\Users\f00863x\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin")
    dll_dir = os.add_dll_directory(str(bindir))
    cairo = ctypes.CDLL(str(bindir / "cairo.dll"))
    poppler = ctypes.CDLL(str(bindir / "poppler-glib.dll"))
    gobject = ctypes.CDLL(str(bindir / "gobject-2.0-0.dll"))
    ptr = ctypes.c_void_p
    cairo.cairo_svg_surface_create.argtypes = [ctypes.c_char_p, ctypes.c_double, ctypes.c_double]
    cairo.cairo_svg_surface_create.restype = ptr
    cairo.cairo_create.argtypes = [ptr]; cairo.cairo_create.restype = ptr
    cairo.cairo_surface_finish.argtypes = [ptr]
    cairo.cairo_destroy.argtypes = [ptr]
    cairo.cairo_surface_destroy.argtypes = [ptr]
    poppler.poppler_document_new_from_file.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ptr]
    poppler.poppler_document_new_from_file.restype = ptr
    poppler.poppler_document_get_page.argtypes = [ptr, ctypes.c_int]
    poppler.poppler_document_get_page.restype = ptr
    poppler.poppler_page_get_size.argtypes = [ptr, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
    poppler.poppler_page_render_for_printing.argtypes = [ptr, ptr]
    gobject.g_object_unref.argtypes = [ptr]
    doc = poppler.poppler_document_new_from_file(pdf_path.as_uri().encode(), None, None)
    if not doc: raise RuntimeError(f"Cannot open {pdf_path}")
    page = poppler.poppler_document_get_page(doc, 0)
    width, height = ctypes.c_double(), ctypes.c_double()
    poppler.poppler_page_get_size(page, ctypes.byref(width), ctypes.byref(height))
    surface = cairo.cairo_svg_surface_create(str(svg_path).encode(), width.value, height.value)
    context = cairo.cairo_create(surface)
    poppler.poppler_page_render_for_printing(page, context)
    cairo.cairo_destroy(context); cairo.cairo_surface_finish(surface); cairo.cairo_surface_destroy(surface)
    gobject.g_object_unref(page); gobject.g_object_unref(doc); dll_dir.close()
    svg = svg_path.read_text(encoding="utf-8")
    svg = re.sub(r'<svg ([^>]*?)width="[^"]+" height="[^"]+"', lambda m: f'<svg {m.group(1)}width="1280" height="{round(1280*height.value/width.value)}"', svg, count=1)
    svg_path.write_text(svg, encoding="utf-8")

def build_diagrams():
    for filename in ("arial.ttf", "arialbd.ttf", "consola.ttf"):
        shutil.copyfile(Path("C:/Windows/Fonts") / filename, BUILD / filename)
    env = dict(os.environ)
    env["TECTONIC_CACHE_DIR"] = r"C:\Users\f00863x\OPRO\tmp\tectonic_cache_017_fresh"
    tectonic = r"C:\Users\f00863x\OPRO\tmp\tectonic-0.17.0\tectonic.exe"
    import pypdf
    for key, item in diagrams.items():
        (ROOT / f"{key}.tex").write_text(PRE + item["tex"] + POST, encoding="utf-8")
        (BUILD / f"{key}_wrapper.tex").write_text(WRAP % key, encoding="utf-8")
        subprocess.run([tectonic, "--only-cached", "--outdir", str(BUILD), f"{key}_wrapper.tex"], cwd=BUILD, env=env, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        source = pypdf.PdfReader(BUILD / f"{key}_wrapper.pdf")
        page = next(p for p in source.pages if (p.extract_text() or "").strip())
        writer = pypdf.PdfWriter(); writer.add_page(page)
        with (ROOT / f"{key}.pdf").open("wb") as out: writer.write(out)
        diagram_svg(ROOT / f"{key}.pdf", ROOT / f"{key}.svg")
        print("Ready diagram", key, flush=True)
    for filename in ("arial.ttf", "arialbd.ttf", "consola.ttf"):
        (BUILD / filename).unlink(missing_ok=True)

def plot_statistics():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.ticker as mtick
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 16, "axes.labelsize": 18, "axes.spines.top": False, "axes.spines.right": False, "svg.fonttype": "path", "pdf.fonttype": 42})
    colors = ["#00629B", "#00A8C8", "#B65B14"]
    lengths = [1, 5, 10, 20]
    qs = [0.99, 0.97, 0.95]
    fig, ax = plt.subplots(figsize=(10.2, 4.8), layout="constrained")
    data = []
    for q, c in zip(qs, colors):
        ys = [q**length for length in lengths]
        ax.plot(lengths, ys, marker="o", lw=2.5, ms=7, color=c, label=f"Per-step q = {q:.2f}")
        ax.annotate(f"{ys[-1]:.1%}", (20, ys[-1]), xytext=(9, 0), textcoords="offset points", color=c, va="center", fontweight="bold")
        data.append({"q": q, "L": lengths, "probability_all_steps_succeed": ys})
    ax.set(xlim=(0, 23), ylim=(0, 1.03), xticks=lengths, xlabel="Number of required steps, L", ylabel="Probability all steps succeed")
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0, decimals=0))
    ax.grid(axis="y", color="#d9e3e9", lw=.7); ax.set_axisbelow(True)
    ax.legend(loc="lower left", frameon=False, fontsize=14)
    save_formats(fig, "rigor_reliability_chain")
    plt.close(fig)

    ns = [10, 30, 60, 100, 300, 1000, 3000]
    alpha = 0.05
    bounds = [1-alpha**(1/n) for n in ns]
    fig, ax = plt.subplots(figsize=(10.2, 4.8), layout="constrained")
    ax.plot(ns, bounds, color=colors[0], lw=2.5, marker="o", ms=7)
    for n, upper in zip(ns, bounds):
        label = f"{100*upper:.2f}%" if n < 100 else f"{100*upper:.3f}%"
        if n == 3000: label = f"{100*upper:.4f}%"
        ax.annotate(label, (n, upper), xytext=(0, 12), textcoords="offset points", ha="center", color=colors[0], fontweight="bold", fontsize=14)
    ax.set_xscale("log")
    ax.set(xlim=(7, 4300), ylim=(0, .315), xticks=ns, xlabel="Independent trials with zero failures, n (log scale)", ylabel="95% upper bound on failure probability")
    ax.xaxis.set_major_formatter(mtick.ScalarFormatter())
    ax.xaxis.set_minor_formatter(mtick.NullFormatter())
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0, decimals=0))
    ax.grid(axis="y", color="#d9e3e9", lw=.7); ax.set_axisbelow(True)
    save_formats(fig, "rigor_zero_failure_bound")
    plt.close(fig)
    return {
        "reliability_chain": {"title": "Small per-step error compounds across a workflow", "caption": "Illustrative calculation: if every step has identical success probability q and steps are independent, all L required steps succeed with probability q^L. These are mathematical scenarios, not measured agent reliability. Correlated errors or unequal steps require a different model.", "formula": "P(all L succeed) = q^L", "data": data, "source_refs": [], "assumptions": "Identical independent Bernoulli step outcomes. All required steps must succeed."},
        "zero_failure_bound": {"title": "Zero observed failures still leaves a nonzero upper bound", "caption": "Exact one-sided 95% binomial upper confidence bound after zero failures: p_upper = 1 - 0.05^(1/n). At n=30 the bound is 9.503%, at n=60 it is 4.8703%, at n=300 it is 0.9936%, and at n=3000 it is 0.09981%. It describes uncertainty under independent, identically distributed trials with a fixed failure definition and stable operating conditions. It does not establish reliability under a new topology or a new task distribution.", "formula": "p_upper = 1 - alpha^(1/n), alpha = 0.05", "n": ns, "p_upper": bounds, "source_refs": [], "assumptions": "IID binomial trials, zero observed failures, prespecified one-sided 95% confidence procedure. This bound is calculated, not author-reported."}
    }

def save_formats(fig, stem):
    for suffix in ("png", "pdf", "svg"):
        fig.savefig(IMAGES / f"{stem}.{suffix}", dpi=200, facecolor="white", bbox_inches="tight")
    print("Ready chart", stem, flush=True)

def plot_extra_statistics():
    import matplotlib.pyplot as plt
    import matplotlib.ticker as mtick
    import numpy as np
    blue, cyan, orange, gray = "#00629B", "#00A8C8", "#B65B14", "#A6B2BA"
    extra = {}
    fig, ax = plt.subplots(figsize=(10.2, 4.8), layout="constrained")
    ax.bar(0, 70, color=blue, width=.52, label="Accepted feasible case")
    ax.bar(0, 10, bottom=70, color=gray, width=.52, label="Rejected")
    ax.bar(1, 2, color=orange, width=.52, label="Accepted infeasible case")
    ax.bar(1, 18, bottom=2, color=gray, width=.52)
    ax.text(0, 35, "70 accepted", color="white", ha="center", va="center", fontweight="bold")
    ax.text(0, 75, "10 rejected", color="#263844", ha="center", va="center", fontsize=13)
    ax.text(1, 11, "18 rejected", color="#263844", ha="center", va="center", fontsize=13)
    ax.annotate("2 false approvals", (1.27, 1), xytext=(1.45, 35), color=orange, fontsize=14, arrowprops={"arrowstyle":"-", "color":orange})
    ax.set(xticks=[0,1], xticklabels=["Truly feasible\n80 cases", "Truly infeasible\n20 cases"], ylabel="Number of cases", ylim=(0,90), xlim=(-.5,2.7))
    ax.yaxis.set_major_locator(mtick.MultipleLocator(20))
    ax.legend(loc="upper right", frameon=False, fontsize=12)
    ax.grid(axis="y", color="#d9e3e9", lw=.7); ax.set_axisbelow(True)
    save_formats(fig, "rigor_eval_outcomes"); plt.close(fig)
    extra["eval_outcomes"] = {"id":"rigor_eval_outcomes", "title":"Conditional failure rates depend on the relevant denominator", "caption":"Hypothetical evaluation of 100 cases, not measured system performance. Of 80 truly feasible cases, 70 are accepted and 10 rejected. Of 20 truly infeasible cases, 2 are accepted and 18 rejected. False approval among infeasible cases is 2/20=10%, while the pooled fraction is 2/100=2%. Accepted-case precision is 70/72=97.22%. The denominator answers a different question in each metric.", "data":{"true_feasible":{"accepted":70,"rejected":10},"true_infeasible":{"accepted":2,"rejected":18}}, "assumptions":"Illustrative labels and outcomes, fixed failure definition. No measured agent data.", "source_refs":[]}

    benchmarks = json.loads((ROOT.parent/"research"/"rigor_benchmarks.json").read_text(encoding="utf-8"))
    cells = benchmarks["capability_gaps"]["quantified_cells"]
    fig, ax = plt.subplots(figsize=(10.2, 4.8), layout="constrained")
    groups=[("DeepSeek", "L1"),("DeepSeek","L2"),("OpenAI","L1"),("OpenAI","L2")]
    width=.32
    for offset, buses, color in [(-width/2,100,blue),(width/2,1000,cyan)]:
        rows=[next(c for c in cells if c["backend"].startswith(backend) and c["task"]==task and c["grid_buses"]==buses) for backend,task in groups]
        ys=np.array([c["success_fraction"] for c in rows])
        lower=np.array([c["wilson_95_calculated"]["lower"] for c in rows])
        upper=np.array([c["wilson_95_calculated"]["upper"] for c in rows])
        xs=np.arange(4)+offset
        ax.bar(xs, ys, width=width, color=color, label=f"{buses:,} buses")
        ax.errorbar(xs,ys,yerr=[ys-lower,np.maximum(0,upper-ys)],fmt="none",ecolor="#293C48",capsize=4,lw=1.25)
        for x,y,row in zip(xs,ys,rows): ax.text(x,.12,row["reported_count"],ha="center",fontsize=12,fontweight="bold",color="white")
    ax.set(xticks=np.arange(4),xticklabels=[f"{b}\n{t}" for b,t in groups],ylim=(0,1.23),ylabel="Reported success fraction")
    ax.yaxis.set_major_locator(mtick.FixedLocator([0,.25,.5,.75,1]));ax.yaxis.set_major_formatter(mtick.PercentFormatter(1,decimals=0))
    ax.legend(loc="upper left",frameon=False,ncol=2,fontsize=13)
    ax.grid(axis="y",color="#d9e3e9",lw=.7);ax.set_axisbelow(True)
    save_formats(fig,"rigor_r02_capability");plt.close(fig)
    extra["r02_capability"]={"id":"rigor_r02_capability","title":"Ten attempts give a narrow evidence base","caption":"Derived from R02 Table II, PDF page 4, tested development snapshot. Bars reproduce the eight reported 100/1000-bus count cells. Whiskers are calculated two-sided Wilson 95% intervals, not author-reported uncertainty. Their probabilistic interpretation requires comparable independent Bernoulli attempts, which the paper does not establish. The OpenAI table label is gpt 5.4 B. Larger grids and levels L3–L6 have no quantified result cells and are omitted, not encoded as zero. This is not field-deployment reliability or a current vendor ranking.","data":cells,"assumptions":"Reported counts preserved. Wilson intervals conditional on independent comparable trials. Model/backend and task snapshot specific.","source_refs":["R02"],"source_url":benchmarks["capability_gaps"]["source_pdf"]}

    fig,ax=plt.subplots(figsize=(10.2,4.8),layout="constrained")
    labels=["Economic-critical\n187–189","Infeasible\n29–30","Infeasible\n15–16"]
    vals=[4,3,0]
    ax.barh([2,1,0],vals,color=[blue,cyan,orange],height=.5)
    ax.scatter([0],[0],s=65,facecolors="white",edgecolors=orange,zorder=3,linewidth=2)
    for y,v in zip([2,1,0],vals):ax.text(v+.13,y,f"{v}/4",va="center",fontweight="bold",color=orange if v==0 else "#003B5C")
    ax.set(yticks=[2,1,0],yticklabels=labels,xlim=(-.18,4.8),xticks=[0,1,2,3,4],xlabel="Reported backend searches identifying the contingency (out of 4)")
    ax.grid(axis="x",color="#d9e3e9",lw=.7);ax.set_axisbelow(True)
    save_formats(fig,"rigor_r01_coverage");plt.close(fig)
    extra["r01_coverage"]={"id":"rigor_r01_coverage","title":"A successful solver call does not imply complete contingency discovery","caption":"Derived from R01 Table III: the four reported backend searches on one synthetic ACTIVSg200 SCOPFLOW case all found economic-critical contingency 187–189 (+21.6% cost), three identified infeasible outage 29–30, and none identified infeasible outage 15–16. These are fixed backend-run counts, not repeated IID trials, estimated probabilities, or comprehensive field reliability. No confidence interval is justified by these four heterogeneous searches.","data":[{"contingency":"187–189","identified":4,"backend_searches":4},{"contingency":"29–30","identified":3,"backend_searches":4},{"contingency":"15–16","identified":0,"backend_searches":4}],"assumptions":"One synthetic case, four different backend searches, reported search behavior only.","source_refs":["R01"],"source_url":benchmarks["agentigrid"]["source_pdf"]}

    count=500;wall=480.;step=wall/count
    sequential=np.arange(1,count+1)*step
    fig,ax=plt.subplots(figsize=(10.2,4.8),layout="constrained")
    ax.step(np.r_[0,sequential],np.r_[0,np.arange(1,count+1)/count],where="post",color=blue,lw=2.5,label="Sequential completions: mean 240.48 s")
    ax.plot([0,wall,wall],[0,0,1],color=orange,lw=2.5,label="All finish at 480 s: mean 480 s")
    ax.text(18,.91,"Both batches: 500 / 480 = 1.04 requests/s",fontsize=14,color="#003B5C")
    ax.set(xlim=(0,510),ylim=(-.025,1.04),xlabel="Completion time since simultaneous arrival (seconds)",ylabel="Fraction of results completed")
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(1,decimals=0))
    ax.legend(loc="upper left",bbox_to_anchor=(0,.84),frameon=False,fontsize=13)
    ax.grid(axis="y",color="#d9e3e9",lw=.7);ax.set_axisbelow(True)
    save_formats(fig,"rigor_batch_throughput");plt.close(fig)
    extra["batch_throughput"]={"id":"rigor_batch_throughput","title":"Batch throughput does not determine individual completion latency","caption":"Made-up completion patterns, not measured CAISO data or a queueing forecast. All 500 requests arrive at time zero and both batches finish at 480 seconds, so both have batch throughput 500/480=1.0417 requests/s. Sequential completions occur at 0.96, 1.92, ..., 480 s and mean completion latency is 240.48 s. In the parallel-tail example all finish at 480 s, so the mean is 480 s. The ratio 480/500=0.96 s is wall time per batch item, not either batch's mean end-to-end latency.","data":{"requests":500,"arrival_time_seconds":0,"batch_wall_seconds":480,"batch_throughput_requests_per_second":count/wall,"wall_seconds_per_item":step,"sequential_mean_latency_seconds":float(sequential.mean()),"parallel_tail_mean_latency_seconds":wall},"assumptions":"Illustrative deterministic completion schedules. No arrival process, service-time distribution, or production latency is estimated.","source_refs":[]}
    return extra

if __name__ == "__main__":
    build_diagrams()
    statistics = plot_statistics()
    statistics.update(plot_extra_statistics())
    for key, item in statistics.items():
        item["id"] = "rigor_" + key
        item["file"] = item["id"] + ".png"
        item["pdf"] = item["id"] + ".pdf"
        item["svg"] = item["id"] + ".svg"
        item["credit"] = "Original plot derived from cited paper data; see caption for interpretation" if item["source_refs"] else "Original illustrative calculation for this tutorial; not measured agent performance"
    manifest = {"credit": "Original worked teaching illustrations and calculated scientific plots", "diagram_size_cm": [14.2, 4.2], "items": [{"id": key, **{k:v for k,v in item.items() if k != "tex"}, "tikz": key+".tex", "svg": key+".svg", "pdf": key+".pdf", "credit":"Original worked teaching illustration"} for key,item in diagrams.items()], "statistics": statistics}
    (ROOT / "rigor_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (IMAGES / "rigor_statistics.json").write_text(json.dumps(statistics, indent=2) + "\n", encoding="utf-8")
