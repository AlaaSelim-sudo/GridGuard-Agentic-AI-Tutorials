"""Build editable teaching diagrams and render the same TikZ source to SVG."""
from pathlib import Path
import json
import os
import subprocess
import shutil
import ctypes
import re

ROOT = Path(__file__).resolve().parent
BUILD = ROOT / "_build"
BUILD.mkdir(exist_ok=True)

PRE = r"""\begin{tikzpicture}[x=1cm,y=1cm,font=\sffamily\fontsize{12}{14}\selectfont,
  line cap=round,line join=round,
  teachPoint/.style={circle,draw=teachBlue,fill=white,line width=1.2pt,minimum size=5.7mm,inner sep=0pt},
  teachDot/.style={circle,fill=teachBlue,minimum size=3.5mm,inner sep=0pt},
  teachLabel/.style={align=center,text=teachNavy,font=\sffamily\bfseries\fontsize{13}{15}\selectfont},
  teachNote/.style={align=center,text=teachNavy,font=\sffamily\fontsize{11}{13}\selectfont},
  teachFlow/.style={-{Latex[length=2.2mm,width=1.6mm]},draw=teachBlue,line width=1.15pt,shorten >=1.5pt,shorten <=1.5pt},
  teachWarn/.style={-{Latex[length=2.2mm,width=1.6mm]},draw=teachOrange,line width=1.15pt,shorten >=1.5pt,shorten <=1.5pt}]
\definecolor{teachBlue}{HTML}{00629B}
\definecolor{teachCyan}{HTML}{00A8C8}
\definecolor{teachNavy}{HTML}{003B5C}
\definecolor{teachOrange}{HTML}{B65B14}
\definecolor{teachGray}{HTML}{74828C}
\path[use as bounding box] (0,0) rectangle (14.3,3.6);
"""
POST = "\n\\end{tikzpicture}\n"

diagrams = {
"agent_loop": ("The agent loop", "A goal prompts a model to choose a tool. Observations update the plan and can branch to operator review. The separate authority diagram explains permission before consequential execution.", r"""
\node[teachPoint] (goal) at (0.9,2.1) {};
\node[teachPoint] (model) at (4.5,2.1) {};
\node[teachPoint] (tool) at (8.2,2.1) {};
\node[teachPoint] (obs) at (12.4,2.1) {};
\node[teachLabel] at (0.9,2.7) {Goal};
\node[teachLabel] at (4.5,2.7) {Model};
\node[teachLabel] at (8.2,2.7) {Tool};
\node[teachLabel] at (12.4,2.7) {Observation};
\draw[teachFlow] (goal) -- (model);
\draw[teachFlow] (model) -- (tool);
\draw[teachFlow] (tool) -- (obs);
\draw[teachFlow] (obs.south) -- (12.4,1.2) -- (4.5,1.2) -- (model.south);
\node[teachNote,fill=white,inner sep=2pt] at (8.4,1.2) {update the plan};
\node[teachPoint,draw=teachCyan] (human) at (8.2,0.35) {};
\draw[teachFlow,draw=teachCyan] (obs.east) -- (13.6,2.1) -- (13.6,0.35) -- (human.east);
\node[teachNote] at (10.8,0.75) {when review is required};
\node[teachLabel,anchor=east] at (7.7,0.35) {Operator review};
"""),
"evidence_path": ("The evidence path", "Event logs, historian data, and procedures feed a brief that preserves timestamps and source links for operator review.", r"""
\node[teachDot] (logs) at (0.55,2.9) {};
\node[teachDot] (hist) at (0.55,1.8) {};
\node[teachDot] (proc) at (0.55,0.7) {};
\node[teachLabel,anchor=west] at (0.9,2.9) {Event logs};
\node[teachLabel,anchor=west] at (0.9,1.8) {Historian};
\node[teachLabel,anchor=west] at (0.9,0.7) {Procedures};
\coordinate (merge) at (4.25,1.8);
\draw[teachFlow] (3.7,2.9) -- (merge);
\draw[teachFlow] (3.7,1.8) -- (merge);
\draw[teachFlow] (3.7,0.7) -- (merge);
\node[teachPoint] (brief) at (7.25,1.8) {};
\node[teachPoint] (operator) at (12.35,1.8) {};
\draw[teachFlow] (merge) -- (brief);
\draw[teachFlow] (brief) -- (operator);
\node[teachLabel] at (7.25,2.55) {Source-linked brief};
\node[teachLabel] at (12.35,2.55) {Operator};
\node[teachNote] at (7.25,0.85) {claims + timestamps + links};
\node[teachNote] at (12.35,0.85) {checks the evidence};
"""),
"authority": ("Levels of authority", "Reading, recommending, and preparing a draft are distinct permissions. Execution crosses an explicit human authorization boundary.", r"""
\node[teachPoint] (read) at (1.25,1.8) {};
\node[teachPoint] (recommend) at (5.0,1.8) {};
\node[teachPoint] (prepare) at (8.6,1.8) {};
\node[teachPoint] (execute) at (12.6,1.8) {};
\draw[teachFlow] (read) -- (recommend);
\draw[teachFlow] (recommend) -- (prepare);
\draw[teachFlow] (prepare) -- (execute);
\node[teachLabel] at (1.25,2.4) {Read};
\node[teachLabel] at (5.0,2.4) {Recommend};
\node[teachLabel] at (8.6,2.4) {Prepare};
\node[teachLabel] at (12.6,2.4) {Execute};
\node[teachNote] at (1.25,0.85) {observe};
\node[teachNote] at (5.0,0.85) {advise};
\node[teachNote] at (8.6,0.85) {draft only};
\node[teachNote] at (12.6,0.85) {approved action};
\draw[draw=teachOrange,line width=1.1pt,densely dashed] (10.65,0.25) -- (10.65,3.0);
\node[teachNote,text=teachOrange,fill=white,inner sep=2pt] at (10.65,3.18) {Explicit permission};
"""),
"rag_tools": ("Retrieval and calculation", "A grounded proposal combines documentary evidence with engineering tool results. Neither source replaces the other.", r"""
\node[teachPoint] (question) at (1.15,1.8) {};
\node[teachLabel] at (1.15,2.4) {Question};
\node[teachPoint] (docs) at (4.3,2.8) {};
\node[teachPoint] (calc) at (4.3,0.8) {};
\node[teachLabel,anchor=west] at (4.8,2.8) {Document retrieval};
\node[teachLabel,anchor=west] at (4.8,0.8) {Engineering calculation};
\draw[teachFlow] (question) -- (2.6,1.8) -- (2.6,2.8) -- (docs);
\draw[teachFlow] (question) -- (2.6,1.8) -- (2.6,0.8) -- (calc);
\coordinate (merge) at (10.65,1.8);
\draw[teachFlow] (9.5,2.8) -- (merge);
\draw[teachFlow] (10.05,0.8) -- (merge);
\node[teachPoint] (proposal) at (12.75,1.8) {};
\draw[teachFlow] (merge) -- (proposal);
\node[teachLabel] at (12.75,2.55) {Proposal};
\node[teachNote] at (12.75,0.95) {evidence + results};
\node[teachNote] at (6.8,2.15) {rules, limits, procedures};
\node[teachNote] at (6.8,0.15) {power flow, constraints, units};
"""),
"state_resume": ("State, review, and resume", "A checkpoint preserves workflow state. Before resuming, the system checks whether inputs and authority remain current.", r"""
\node[teachPoint] (snapshot) at (1.15,1.8) {};
\node[teachPoint] (tool) at (3.25,1.8) {};
\node[teachPoint] (checkpoint) at (5.65,1.8) {};
\node[teachPoint] (human) at (8.05,1.8) {};
\node[teachPoint] (fresh) at (10.45,1.8) {};
\node[teachPoint] (resume) at (12.85,1.8) {};
\draw[teachFlow] (snapshot) -- (tool);
\draw[teachFlow] (tool) -- (checkpoint);
\draw[teachFlow] (checkpoint) -- (human);
\draw[teachFlow] (human) -- (fresh);
\draw[teachFlow] (fresh) -- (resume);
\node[teachLabel] at (1.15,2.5) {Snapshot};
\node[teachLabel] at (3.25,2.5) {Tool call};
\node[teachLabel] at (5.65,2.5) {Checkpoint};
\node[teachLabel] at (8.05,2.6) {Human\\review};
\node[teachLabel] at (10.45,2.6) {Freshness\\check};
\node[teachLabel] at (12.85,2.5) {Resume};
\draw[teachWarn] (fresh.south) -- (10.45,0.5) -- (3.25,0.5) -- (tool.south);
\node[teachNote,text=teachOrange,fill=white,inner sep=2pt] at (6.9,0.5) {stale inputs: refresh or stop};
"""),
"evaluation": ("Evaluation before review", "A candidate passes domain checks and evidence checks before operator review. Failed or stale inputs trigger a request for new data.", r"""
\node[teachPoint] (candidate) at (1.05,2.0) {};
\node[teachPoint] (domain) at (4.9,2.0) {};
\node[teachPoint] (evidence) at (8.65,2.0) {};
\node[teachPoint] (review) at (12.55,2.0) {};
\draw[teachFlow] (candidate) -- (domain);
\draw[teachFlow] (domain) -- (evidence);
\draw[teachFlow] (evidence) -- (review);
\node[teachLabel] at (1.05,2.7) {Candidate};
\node[teachLabel] at (4.9,2.7) {Domain check};
\node[teachLabel] at (8.65,2.7) {Evidence check};
\node[teachLabel] at (12.55,2.7) {Review};
\node[teachPoint,draw=teachOrange] (request) at (6.8,0.65) {};
\draw[teachWarn] (domain.south) -- (4.9,0.65) -- (request.west);
\draw[teachWarn] (evidence.south) -- (8.65,0.65) -- (request.east);
\node[teachNote,text=teachOrange] at (3.55,1.0) {failed};
\node[teachNote,text=teachOrange] at (9.7,1.0) {stale or unsupported};
\node[teachLabel,anchor=west] at (7.25,0.25) {Request new data};
"""),
"framework_layers": ("The application stack", "The operator application delegates workflow control to an orchestrator. Typed tools mediate access to utility data and engineering simulators.", r"""
\node[teachLabel] (app) at (7.15,3.15) {Operator application};
\node[teachLabel] (orchestrator) at (7.15,2.25) {Orchestrator};
\node[teachLabel] (tools) at (7.15,1.35) {Typed tools};
\node[teachLabel] (data) at (3.8,0.3) {Utility data};
\node[teachLabel] (sim) at (10.5,0.3) {Engineering simulator};
\draw[teachFlow] (app.south) -- (orchestrator.north);
\draw[teachFlow] (orchestrator.south) -- (tools.north);
\draw[teachFlow] (tools.south) -- (7.15,0.85) -- (3.8,0.85) -- (data.north);
\draw[teachFlow] (tools.south) -- (7.15,0.85) -- (10.5,0.85) -- (sim.north);
\node[teachNote,anchor=west] at (10.1,3.15) {operator interaction};
\node[teachNote,anchor=west] at (10.1,2.25) {state and routing};
\node[teachNote,anchor=west] at (10.1,1.35) {schemas and access};
"""),
"exercise_packet": ("Input freshness exercise", "At the 15:05 review, telemetry is 30 minutes old, the study is 25 minutes old, and the alarm is 3 minutes old. Check whether the inputs describe the post-event state. Request fresh data or justification for using earlier data. No fixed age threshold is implied.", r"""
\node[teachPoint,draw=teachOrange] (telemetry) at (1.45,1.85) {};
\node[teachPoint,draw=teachOrange] (study) at (5.2,1.85) {};
\node[teachPoint] (alarm) at (9.0,1.85) {};
\node[teachPoint,draw=teachCyan] (review) at (12.8,1.85) {};
\draw[teachFlow] (telemetry) -- (study);
\draw[teachFlow] (study) -- (alarm);
\draw[teachFlow] (alarm) -- (review);
\node[teachLabel] at (1.45,2.65) {Telemetry\\14:35};
\node[teachLabel] at (5.2,2.65) {Study\\14:40};
\node[teachLabel] at (9.0,2.65) {Alarm\\15:02};
\node[teachLabel] at (12.8,2.65) {Review now\\15:05};
\node[teachNote,text=teachOrange] at (1.45,1.15) {30 min old};
\node[teachNote,text=teachOrange] at (5.2,1.15) {25 min old};
\node[teachNote] at (9.0,1.15) {3 min old};
\node[teachNote] at (12.8,1.15) {decision time};
\node[teachLabel] at (7.15,0.3) {Post-event state: what needs checking?};
"""),
"aes_audit": ("AES audit review workflow", "Simplified teaching reconstruction of the published AES case: documents feed coordinated review agents, which prepare a score and report for human review.", r"""
\node[teachPoint] (docs) at (1.75,1.8) {};
\node[teachPoint] (agents) at (5.25,1.8) {};
\node[teachPoint] (report) at (9.0,1.8) {};
\node[teachPoint,draw=teachCyan] (human) at (12.8,1.8) {};
\draw[teachFlow] (docs) -- (agents);
\draw[teachFlow] (agents) -- (report);
\draw[teachFlow] (report) -- (human);
\node[teachLabel] at (1.75,2.6) {Protocols +\\program docs};
\node[teachLabel] at (5.25,2.6) {Coordinated\\review agents};
\node[teachLabel] at (9.0,2.6) {Score +\\report};
\node[teachLabel] at (12.8,2.6) {Human\\review};
\node[teachNote] at (7.15,0.6) {Simplified teaching reconstruction of the published AES case};
"""),
"tc_piper": ("TC Energy Piper workflow", "Simplified teaching reconstruction: Textract extracts records, Claude and Strands agents support cross-checks, and engineers review outputs. Bedrock AgentCore hosts agents and tools. AWS Step Functions coordinates processing.", r"""
\node[teachPoint] (textract) at (1.45,1.8) {};
\node[teachPoint] (agents) at (5.25,1.8) {};
\node[teachPoint] (checks) at (9.0,1.8) {};
\node[teachPoint,draw=teachCyan] (human) at (12.8,1.8) {};
\draw[teachFlow] (textract) -- (agents);
\draw[teachFlow] (agents) -- (checks);
\draw[teachFlow] (checks) -- (human);
\node[teachLabel] at (1.45,2.6) {Textract};
\node[teachLabel] at (5.25,2.6) {Claude +\\Strands agents};
\node[teachLabel] at (9.0,2.6) {Record\\cross-checks};
\node[teachLabel] at (12.8,2.6) {Engineer\\review};
\node[teachNote] at (7.15,0.75) {Bedrock AgentCore hosts agents and tools};
\node[teachNote] at (7.15,0.2) {AWS Step Functions coordinates processing};
"""),
"duke_study": ("Duke Energy study workflow", "Simplified teaching reconstruction: workflow agents prepare a case and coordinate existing engineering tools. An engineer confirms the case before the simulator study and reviews the report.", r"""
\node[teachPoint] (prepare) at (1.45,1.8) {};
\node[teachPoint,draw=teachCyan] (confirm) at (5.25,1.8) {};
\node[teachPoint] (simulator) at (9.0,1.8) {};
\node[teachPoint,draw=teachCyan] (report) at (12.8,1.8) {};
\draw[teachFlow] (prepare) -- (confirm);
\draw[teachFlow] (confirm) -- (simulator);
\draw[teachFlow] (simulator) -- (report);
\node[teachLabel] at (1.45,2.6) {Prepare case};
\node[teachLabel] at (5.25,2.6) {Engineer\\confirms};
\node[teachLabel] at (9.0,2.6) {Simulator\\study};
\node[teachLabel] at (12.8,2.6) {Reviewed\\report};
\node[teachNote] at (7.15,0.6) {Workflow agents coordinate existing engineering tools};
"""),
}

wrapper = r"""\documentclass{article}
\usepackage[paperwidth=14.5cm,paperheight=3.8cm,margin=0.1cm]{geometry}
\DeclareFontFamily{TU}{teacharial}{}
\DeclareFontShape{TU}{teacharial}{m}{n}{<->"[arial.ttf]"}{}
\DeclareFontShape{TU}{teacharial}{b}{n}{<->"[arialbd.ttf]"}{}
\DeclareFontShape{TU}{teacharial}{bx}{n}{<->"[arialbd.ttf]"}{}
\renewcommand{\sfdefault}{teacharial}
\renewcommand{\rmdefault}{teacharial}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,positioning,calc}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\begin{document}
\noindent\input{../%s.tex}
\end{document}
"""

for key, (title, desc, body) in diagrams.items():
    (ROOT / f"{key}.tex").write_text(PRE + body + POST, encoding="utf-8")
    (BUILD / f"{key}_wrapper.tex").write_text(wrapper % key, encoding="utf-8")

manifest = {
    "kind": "Original educational concept diagrams requested for the tutorial",
    "credit": "Original tutorial illustrations. Editable TikZ source accompanies each SVG.",
    "source": "Author-created for this tutorial, not a vendor product diagram or deployment claim",
    "required_tikz_libraries": ["arrows.meta", "positioning", "calc"],
    "inclusion": "Each .tex is an unconditional tikzpicture fragment. Colors and styles are scoped inside its picture. Include with input and optional resizebox.",
    "coordinate_size_cm": [14.3, 3.6],
    "svg_size_px": [1280, 335],
    "items": [{"id": k, "title": v[0], "description": v[1], "tikz": f"{k}.tex", "svg": f"{k}.svg"} for k, v in diagrams.items()],
}
case_references = {
    "aes_audit": ["https://cloud.google.com/customers/aes"],
    "tc_piper": ["https://aws.amazon.com/solutions/case-studies/tcenergy-bedrock/"],
    "duke_study": ["https://press.aboutamazon.com/aws/2026/9/aws-launches-agentic-grid-planning-program-to-accelerate-interconnection-studies", "https://aws.amazon.com/energy-utilities/agentic-grid-planning/"],
}
source_refs = {
    "agent_loop": ["T01", "T04"],
    "evidence_path": ["O01"],
    "authority": ["T09"],
    "rag_tools": ["L01"],
    "state_resume": ["T01", "T03"],
    "framework_layers": ["T01", "T02", "T04", "T06"],
    "evaluation": ["R02", "T14"],
    "aes_audit": ["U01", "V02"],
    "tc_piper": ["U04"],
    "duke_study": ["U02", "U03"],
    "exercise_packet": [],
}
for item in manifest["items"]:
    item["source_refs"] = source_refs[item["id"]]
    if item["id"] in case_references:
        item["teaching_reconstruction"] = True
        item["external_references"] = case_references[item["id"]]
        item["disclosure"] = "Original simplified teaching illustration based on the cited case. Not a vendor-provided architecture or measured execution trace."
(ROOT / "diagram_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
print(f"Wrote {len(diagrams)} native TikZ snippets and wrappers")

def pdf_to_svg(pdf_path, svg_path):
    """Render the PDF's first page through the bundled Poppler/Cairo libraries."""
    bindir = Path(r"C:\Users\f00863x\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin")
    dll_dir = os.add_dll_directory(str(bindir))
    cairo = ctypes.CDLL(str(bindir / "cairo.dll"))
    poppler = ctypes.CDLL(str(bindir / "poppler-glib.dll"))
    gobject = ctypes.CDLL(str(bindir / "gobject-2.0-0.dll"))
    ptr = ctypes.c_void_p
    cairo.cairo_svg_surface_create.argtypes = [ctypes.c_char_p, ctypes.c_double, ctypes.c_double]
    cairo.cairo_svg_surface_create.restype = ptr
    cairo.cairo_create.argtypes = [ptr]
    cairo.cairo_create.restype = ptr
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
    if not doc:
        raise RuntimeError(f"Poppler could not open {pdf_path}")
    # Very short article pages may include an empty page before the picture.
    # Select the actual diagram page rather than exporting an empty first page.
    import pypdf
    pages = pypdf.PdfReader(pdf_path).pages
    page_index = next(i for i, p in enumerate(pages) if (p.extract_text() or "").strip())
    page = poppler.poppler_document_get_page(doc, page_index)
    width = ctypes.c_double()
    height = ctypes.c_double()
    poppler.poppler_page_get_size(page, ctypes.byref(width), ctypes.byref(height))
    surface = cairo.cairo_svg_surface_create(str(svg_path).encode(), width.value, height.value)
    context = cairo.cairo_create(surface)
    poppler.poppler_page_render_for_printing(page, context)
    cairo.cairo_destroy(context)
    cairo.cairo_surface_finish(surface)
    cairo.cairo_surface_destroy(surface)
    gobject.g_object_unref(page)
    gobject.g_object_unref(doc)
    dll_dir.close()
    svg = svg_path.read_text(encoding="utf-8")
    svg = re.sub(r'<svg ([^>]*?)width="[^"]+" height="[^"]+"', lambda m: f'<svg {m.group(1)}width="1280" height="{round(1280*height.value/width.value)}"', svg, count=1)
    svg_path.write_text(svg, encoding="utf-8")

if __name__ == "__main__":
    for filename in ("arial.ttf", "arialbd.ttf"):
        shutil.copyfile(Path("C:/Windows/Fonts") / filename, BUILD / filename)
    tectonic = Path(r"C:\Users\f00863x\OPRO\tmp\tectonic-0.17.0\tectonic.exe")
    env = dict(os.environ)
    env["TECTONIC_CACHE_DIR"] = r"C:\Users\f00863x\OPRO\tmp\tectonic_cache_017_fresh"
    for key in diagrams:
        subprocess.run([str(tectonic), "--only-cached", "--keep-logs", "--outdir", str(BUILD), f"{key}_wrapper.tex"], cwd=BUILD, env=env, check=True)
        pdf_to_svg(BUILD / f"{key}_wrapper.pdf", ROOT / f"{key}.svg")
        print("Ready", key, flush=True)
