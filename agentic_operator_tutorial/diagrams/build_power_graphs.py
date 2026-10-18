"""Editable native TikZ power-workflow teaching diagrams.

Only power_*.tex/.pdf/.svg and power_graph_manifest.json are published.
Compilation and raster QA use a temporary directory. Pass --contact-base64 to
emit a transient contact sheet for inspection; it is not a published asset.
"""
from pathlib import Path
import base64
import io
import json
import os
import runpy
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
SHARED = runpy.run_path(str(ROOT / "build_rigorous.py"))
PRE, POST = SHARED["PRE"], SHARED["POST"]
WRAP = SHARED["WRAP"].replace(r"\input{../%s.tex}", r"\input{%s}")
SVG_FROM_PDF = SHARED["diagram_svg"]

DIAGRAMS = {
  "power_fault_dag": {
    "title": "A fault-record DAG follows the data prerequisites",
    "caption": "Original teaching adaptation of DrAgent's domain tools, not its measured execution trace. A frozen COMTRADE record R17 feeds independent find_fault_inception and find_max_fault_current computations (abbreviated in the drawing). The inception sample and sampling rate feed a time conversion; the report waits for both numerical results.",
    "assumptions": "R17 is an invented identifier; no waveform or numerical result is invented. The simple n_f/f_s conversion assumes constant sampling rate and a zero-based index relative to record start. Production conversion must respect actual COMTRADE timestamps, indexing and rate changes. Parallel scheduling is a teaching adaptation, not a claim that the paper ran these tools concurrently.",
    "source_refs": ["D01"],
    "source_url": "https://www.manuscriptlink.com/society/kics/media?key=kics%2Fconference%2Ficaiic2025%2Fpresentation%2F1571098105.pdf",
    "source_locator": "DrAgent Section III.B / Figure 3; Listing 2, PDF pp.4 and7",
    "tex_body": r"""
\node[rp] (record) at (1.35,2.05) {};
\node[rl] at (1.35,3.05) {Frozen\\R17};
\node[rn] at (1.35,1.45) {.cfg + .dat};
\coordinate (fork) at (2.45,2.05);
\draw[rf] (record.east) -- (fork);
\fill[rBlue] (fork) circle (1.8pt);
\node[rp] (inception) at (4.75,3.2) {};
\node[rl] at (4.75,3.85) {Find inception};
\node[rn] at (4.75,2.7) {sample n\textsubscript{f}};
\draw[rf] (fork) |- (inception.west);
\node[rp] (maximum) at (4.75,.95) {};
\node[rl] at (4.75,1.52) {Find max current};
\node[rn] at (4.75,.45) {I\textsubscript{max}};
\draw[rf] (fork) |- (maximum.west);
\node[rp] (rate) at (8.55,2.05) {};
\node[rn] at (8.55,1.5) {CFG: rate f\textsubscript{s}};
\draw[rf] (fork) -- (rate.west);
\node[rp] (time) at (8.55,3.2) {};
\node[rl] at (8.55,3.85) {Convert to time};
\node[rn] at (6.65,3.6) {n\textsubscript{f}};
\node[rn] at (9.75,2.65) {n\textsubscript{f} / f\textsubscript{s}};
\draw[rf] (inception.east) -- (time.west);
\draw[rf] (rate.north) -- (time.south);
\coordinate (join) at (11.05,2.05);
\draw[rf] (time.east) -- (11.05,3.2) -- (join);
\draw[rf] (maximum.east) -- (11.05,.95) -- (join);
\fill[rBlue] (join) circle (2pt);
\node[rp] (report) at (13.0,2.05) {};
\draw[rf] (join) -- (report.west);
\node[rl] at (13.0,2.85) {Report};
\node[rn] at (13.0,1.45) {evidence};
"""
  },
  "power_stateful_route": {
    "title": "A stateful graph routes the next step using validation",
    "caption": "Original LangGraph educational pattern. A plan invokes a power-flow tool and validates its returned evidence. Valid evidence finishes; invalid evidence with retries left decrements the counter and replans; exhausted retries escalate. Two retries are an explicit application policy, not a LangGraph default.",
    "assumptions": "Illustrative tool run_pf(F12,v43), state fields and budget. No tool is executed. Routing checks tool status, evidence and domain acceptance criteria; a completed graph alone does not establish electrical feasibility.",
    "source_refs": ["LG01"],
    "source_url": "https://docs.langchain.com/oss/python/langgraph/graph-api",
    "tex_body": r"""
\node[rc,anchor=west,font=\ttfamily\fontsize{11}{13}\selectfont] at (.35,3.95) {state: topology=v43, retries\_left=2, evidence=[]};
\node[rp] (plan) at (1.15,2.65) {};
\node[rp] (tool) at (4.45,2.65) {};
\node[rp] (validate) at (7.8,2.65) {};
\node[rp] (finish) at (12.5,2.65) {};
\node[rl] at (1.15,3.3) {Plan};
\node[rl] at (4.45,3.3) {Call tool};
\node[rl] at (7.8,3.3) {Validate};
\node[rl] at (12.5,3.3) {Finish};
\draw[rf] (plan.east) -- (tool.west);
\draw[rf] (tool.east) -- (validate.west);
\draw[rf] (validate.east) -- (finish.west);
\node[rn] at (10.2,3.05) {valid evidence};
\node[rc,font=\ttfamily\fontsize{10.8}{12}\selectfont] at (4.45,2.05) {run\_pf(F12,v43)};
\coordinate (route) at (7.8,1.0);
\draw[rw] (validate.south) -- (route);
\fill[rOrange] (route) circle (1.8pt);
\draw[rw] (route) -- (1.15,1.0) -- (plan.south);
\node[rn,text=rOrange] at (4.35,1.43) {invalid, retries\_left > 0};
\node[rp,draw=rOrange] (escalate) at (12.5,1.0) {};
\draw[rw] (route) -- (escalate.west);
\node[rn,text=rOrange] at (10.2,1.43) {invalid, retry = 0};
\node[rl,text=rOrange] at (12.5,.35) {Escalate};
\node[rn,text=rGray] at (4.35,.35) {Decrement the counter, then replan};
"""
  },
  "power_checkpoint_revalidation": {
    "title": "A checkpoint preserves execution state, not evidence freshness",
    "caption": "Original educational checkpoint/resume example. A checkpoint stores execution state and solver evidence for topology v42. A topology event creates v43 during the pause. On resume, an explicit application check compares the evidence context with the current topology and recomputes affected evidence before reuse.",
    "assumptions": "Topology versions and event are invented. Persistence does not automatically refresh solver evidence or validate domain assumptions. The diagram shows one mismatch branch; an unchanged context could pass a separately defined reuse check.",
    "source_refs": ["LG02", "LG03"],
    "source_url": "https://docs.langchain.com/oss/python/langgraph/persistence",
    "tex_body": r"""
\node[rp] (saved) at (1.9,2.7) {};
\node[rl] at (1.9,3.4) {Checkpoint v42};
\node[rn] at (1.9,2.05) {state + evidence};
\node[rp] (resume) at (6.7,2.7) {};
\node[rl] at (6.7,3.4) {Resume};
\draw[rf] (saved.east) -- (resume.west);
\node[rn,fill=white,inner sep=2pt] at (4.2,2.7) {pause};
\node[rp] (check) at (11.9,2.7) {};
\node[rl] at (11.9,3.4) {Revalidate};
\draw[rf] (resume.east) -- (check.west);
\node[rn] at (9.25,2.1) {v42 != v43};
\node[rp,draw=rOrange] (event) at (6.7,.8) {};
\node[rn,text=rOrange] at (4.1,.8) {switch S opens};
\node[rn,text=rOrange] at (6.7,.22) {current: v43};
\draw[rw] (event.north) -- (resume.south);
\node[rp,draw=rOrange] (rerun) at (11.9,.8) {};
\draw[rw] (check.south) -- (rerun.north);
\node[rn,text=rOrange] at (11.9,.22) {recompute on v43};
"""
  },
  "power_contingency_join": {
    "title": "A contingency join preserves missing results",
    "caption": "Original teaching fan-out/fan-in pattern. Cases C1, C2 and C3 start from separate copies of the same frozen network v43. C2 returns a tool error. The join retains all case statuses and produces an INCOMPLETE report rather than treating the two completed cases as complete contingency coverage.",
    "assumptions": "Invented case identifiers and statuses; no power-flow measurements or contingency ranking is claimed. Independent copies prevent branch mutations from leaking between cases. Completion is distinct from a pass against operating limits.",
    "source_refs": ["LG01"],
    "source_url": "https://docs.langchain.com/oss/python/langgraph/graph-api",
    "tex_body": r"""
\node[rp] (snapshot) at (1.4,2.05) {};
\node[rl] at (1.4,2.8) {Frozen v43};
\node[rn] at (1.4,1.4) {copy per case};
\coordinate (fork) at (2.8,2.05);
\draw[rf] (snapshot.east) -- (fork);
\fill[rBlue] (fork) circle (1.8pt);
\node[rp] (c1) at (5.3,3.3) {};
\node[rp,draw=rOrange] (c2) at (5.3,2.05) {};
\node[rp] (c3) at (5.3,.8) {};
\draw[rf] (fork) |- (c1.west);
\draw[rf] (fork) -- (c2.west);
\draw[rf] (fork) |- (c3.west);
\node[rl] at (5.3,3.9) {C1: complete};
\node[rl,text=rOrange] at (5.3,2.65) {C2: tool error};
\node[rl] at (5.3,.25) {C3: complete};
\coordinate (gather) at (8.2,2.05);
\draw[rf] (c1.east) -- (8.2,3.3) -- (gather);
\draw[rw] (c2.east) -- (gather);
\draw[rf] (c3.east) -- (8.2,.8) -- (gather);
\fill[rBlue] (gather) circle (1.8pt);
\node[rp] (join) at (9.6,2.05) {};
\draw[rf] (gather) -- (join.west);
\node[rl] at (9.6,2.8) {Join};
\node[rn] at (9.6,1.4) {all statuses};
\node[rp,draw=rOrange] (report) at (12.65,2.05) {};
\draw[rw] (join.east) -- (report.west);
\node[rl,text=rOrange] at (12.65,2.8) {INCOMPLETE};
\node[rn,text=rOrange] at (12.65,1.4) {missing C2};
"""
  },
  "power_gridmind_invalidation": {
    "title": "A changed input determines the stages that rerun",
    "caption": "Original affected-stage diagram derived from GridMind 2026 Table 1, PDF p.4. Changing cascade fan-out k from 50 to 200 reruns cascade only. Shifting forecast initialization by six hours reruns all five stages: line-wind, outages, ACOPF, contingency and cascade. These are reported dependency effects, not a newly executed workflow.",
    "assumptions": "The diagram shows affected sets, not invented stage-to-stage edges. In this implementation contingency consumes the outage schedule directly, not the ACOPF result. Reuse requires matching declared inputs; an artifact hash does not prove numerical correctness or freshness beyond those inputs.",
    "source_refs": ["P03"],
    "source_url": "https://openreview.net/pdf/5ad1c2afd7298f9e6ce3bc25f18e7165555e1ffd.pdf",
    "source_locator": "Table 1 and Section 4.2, PDF p.4",
    "tex_body": r"""
\node[rl,anchor=west] at (.45,3.55) {Changed input};
\node[rl,anchor=west] at (6.0,3.55) {Affected stages};
\node[rc,anchor=west] at (.45,2.65) {k: 50 to 200};
\draw[rw] (4.4,2.65) -- (5.65,2.65);
\node[rl,text=rOrange,anchor=west] at (6.0,2.65) {cascade only};
\node[rn,anchor=west] at (6.0,2.1) {reuse the other four stages};
\draw[draw=rGray,line width=.5pt] (.45,1.7) -- (13.75,1.7);
\node[rc,anchor=west] at (.45,1.1) {forecast: +6 h};
\draw[rw] (4.4,1.1) -- (5.65,1.1);
\node[rl,text=rOrange,anchor=west,align=left] at (6.0,1.1) {line-wind, outages, ACOPF,\\contingency, cascade};
\node[rn,text=rGray] at (7.1,.2) {Affected sets from the reported trace; no new dependency edges inferred};
"""
  }
}


def build(contact=False, only=None):
    sys.path.insert(0, str(ROOT / "_rigorous_build" / "pythonpackages"))
    import pypdf
    from PIL import Image, ImageOps
    manifest_path = ROOT / "power_graph_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if only and manifest_path.exists() else {}
    previews = []
    temp_root = (ROOT.parents[2] / "tmp").resolve()
    with tempfile.TemporaryDirectory(prefix="power_graphs_", dir=temp_root) as temp:
        work = Path(temp).resolve()
        assert work.is_relative_to(temp_root), "Temporary cleanup must remain in workspace tmp"
        for font in ("arial.ttf", "arialbd.ttf", "consola.ttf"):
            shutil.copyfile(Path("C:/Windows/Fonts") / font, work / font)
        env = dict(os.environ)
        env["TECTONIC_CACHE_DIR"] = str(ROOT.parents[2] / "tmp" / "tectonic_cache_017_fresh")
        tectonic = ROOT.parents[2] / "tmp" / "tectonic-0.17.0" / "tectonic.exe"
        pdftoppm = Path(r"C:\Users\f00863x\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe")
        for stem, spec in DIAGRAMS.items():
            if only and stem != only:
                continue
            tex = ROOT / (stem + ".tex")
            tex.write_text(PRE + spec["tex_body"] + POST, encoding="utf-8")
            wrapper = work / (stem + "_wrapper.tex")
            wrapper.write_text(WRAP % tex.as_posix(), encoding="utf-8")
            compiled = subprocess.run([str(tectonic), "--only-cached", "--outdir", str(work), wrapper.name],
                                      cwd=work, env=env, capture_output=True, text=True)
            if compiled.returncode:
                raise RuntimeError(compiled.stdout + compiled.stderr)
            source = pypdf.PdfReader(wrapper.with_suffix(".pdf"))
            page = next(p for p in source.pages if (p.extract_text() or "").strip())
            writer = pypdf.PdfWriter(); writer.add_page(page)
            pdf = ROOT / (stem + ".pdf")
            with pdf.open("wb") as handle:
                writer.write(handle)
            svg = ROOT / (stem + ".svg")
            SVG_FROM_PDF(pdf, svg)
            assert "<image" not in svg.read_text(encoding="utf-8"), "Unexpected raster in SVG"
            assert len(pypdf.PdfReader(pdf).pages) == 1
            preview = work / stem
            subprocess.run([str(pdftoppm), "-scale-to-x", "1280", "-scale-to-y", "-1", "-singlefile", "-png", str(pdf), str(preview)],
                           check=True, capture_output=True)
            with Image.open(preview.with_suffix(".png")) as im:
                previews.append(im.convert("RGB").copy())
            item = {k:v for k,v in spec.items() if k != "tex_body"}
            item.update({"id":stem,"tex":stem+".tex","svg":stem+".svg","pdf":stem+".pdf",
                         "file":stem+".svg","credit":"Original editable TikZ teaching diagram; see caption for source and assumptions"})
            manifest[stem] = item
        manifest_text = json.dumps(manifest, indent=2, ensure_ascii=False)+"\n"
        if not manifest_path.exists() or manifest_path.read_text(encoding="utf-8") != manifest_text:
            manifest_path.write_text(manifest_text, encoding="utf-8")
        if contact:
            width, cell_h = 1280, 430
            sheet = Image.new("RGB", (width, cell_h*len(previews)), "#EAF0F3")
            for i,im in enumerate(previews):
                sheet.paste(ImageOps.contain(im,(1260,410)), (10,i*cell_h+10))
            buf = io.BytesIO(); sheet.save(buf,format="JPEG",quality=80)
            return base64.b64encode(buf.getvalue()).decode("ascii")
    return None


if __name__ == "__main__":
    contact = "--contact-base64" in sys.argv
    only = next((arg.split("=", 1)[1] for arg in sys.argv if arg.startswith("--only=")), None)
    if only and only not in DIAGRAMS:
        raise SystemExit("Unknown diagram: " + only)
    result = build(contact, only)
    if result:
        print(result)
    else:
        print("Built " + (only or "five power graph diagrams") + " (native TikZ, SVG and PDF).")
