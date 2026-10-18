"""Native TikZ conceptual visual aids; only va_* assets and their manifest."""
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
 "va_system_overview": {
  "title": "One agent within a complete study process",
  "caption": "Original illustrative system: a goal guides one AI agent, tools produce study evidence, an explicit check controls the report, and a human receives the result. Observations and failed checks can return the process to the agent. Multiple agents are not required.",
  "assumptions": "Conceptual advisory-study process, not a measured implementation. The check is application-defined; no control authority or numerical guarantee follows from the diagram.",
  "source_refs": ["DEF03", "DEF04"],
  "source_url": "https://www.anthropic.com/engineering/building-effective-agents",
  "source_locator": "What are agents?; Agents; original teaching synthesis.",
  "tex_body": r"""
\node[rp] (goal) at (1.1,2.95) {};
\node[rp] (agent) at (4.0,2.95) {};
\node[rp] (tools) at (7.0,2.95) {};
\node[rp] (check) at (10.0,2.95) {};
\node[rp] (human) at (12.9,2.95) {};
\node[rl] at (1.1,3.65) {Goal};
\node[rl] at (4.0,3.65) {AI agent};
\node[rl] at (7.0,3.65) {Tools};
\node[rl] at (10.0,3.65) {Check};
\node[rl] at (12.9,3.65) {Human};
\node[rn] at (12.9,2.2) {evidence\\report};
\draw[rf] (goal.east) -- (agent.west);
\draw[rf] (agent.east) -- (tools.west);
\draw[rf] (tools.east) -- (check.west);
\draw[rf] (check.east) -- (human.west);
\node[rn] at (11.45,3.23) {pass};
\coordinate (return) at (4.0,1.55);
\draw[draw=rBlue,line width=1.15pt] (tools.south) -- (7.0,1.55) -- (return);
\node[rn] at (5.5,1.92) {results};
\draw[rw] (check.south) -- (10.0,.55) -- (4.0,.55) -- (return);
\node[rn,text=rOrange] at (7.0,.95) {missing evidence};
\fill[rBlue] (return) circle (1.7pt);
\draw[rf] (return) -- (agent.south);
"""
 },
 "va_generation_call": {
  "title": "A generative-model call produces content",
  "caption": "Original example of a single generative-model call: a prompt and selected records produce a draft report for review. This illustrates one use of generative AI, not a universal boundary around the technology; the same kind of model can also participate in an agent.",
  "assumptions": "No external-action feedback loop is shown in this particular example. Draft content is not established engineering evidence or permission to operate equipment.",
  "source_refs": ["DEF03"],
  "source_url": "https://www.anthropic.com/engineering/building-effective-agents",
  "source_locator": "When (and when not) to use agents; original teaching contrast.",
  "tex_body": r"""
\node[rp] (prompt) at (1.6,3.0) {};
\node[rl] at (1.6,3.7) {Prompt};
\node[rp] (records) at (1.6,1.05) {};
\node[rl] at (1.6,1.83) {Selected\\records};
\coordinate (join) at (4.1,2.05);
\draw[draw=rBlue,line width=1.15pt] (prompt.east) -- (4.1,3.0) -- (join);
\draw[draw=rBlue,line width=1.15pt] (records.east) -- (4.1,1.05) -- (join);
\fill[rBlue] (join) circle (1.7pt);
\node[rp] (model) at (7.0,2.05) {};
\node[rl] at (7.0,3.02) {Generative\\model};
\draw[rf] (join) -- (model.west);
\node[rp] (draft) at (12.15,2.05) {};
\node[rl] at (12.15,2.83) {Draft report};
\node[rn] at (12.15,1.36) {content to review};
\draw[rf] (model.east) -- (draft.west);
"""
 },
 "va_classical_agent": {
  "title": "An agent observes and acts in an environment",
  "caption": "Original grid-study illustration of the classical observation/action abstraction. A software environment supplies case files and solver logs; an agent selects study actions or asks for evidence. The agent need not be an LLM.",
  "assumptions": "Illustrative software environment, not a physical control implementation. Actions can include information gathering; a closed loop does not by itself establish rationality or successful results.",
  "source_refs": ["DEF01", "DEF02"],
  "source_url": "https://aima.cs.berkeley.edu/4th-ed/pdfs/newchap02.pdf",
  "source_locator": "Russell/Norvig Section 2.1, Figure 2.1; verified older author-hosted chapter sample, not fourth-edition text.",
  "tex_body": r"""
\node[rp] (environment) at (3.4,2.05) {};
\node[rl] at (1.65,2.05) {Study\\environment};
\node[rp] (agent) at (10.8,2.05) {};
\node[rl] at (12.2,2.05) {Agent};
\draw[rf] (environment.north) -- (3.4,3.43) -- (10.8,3.43) -- (agent.north);
\node[rl] at (7.0,3.86) {Observations};
\node[rn] at (7.0,3.0) {case files / solver logs};
\draw[rf] (agent.south) -- (10.8,.72) -- (3.4,.72) -- (environment.south);
\node[rn] at (7.0,1.15) {run a study / request evidence};
\node[rl] at (7.0,.26) {Actions};
"""
 },
 "va_workflow_agent": {
  "title": "Programmed steps and model-directed choices",
  "caption": "Original comparison of control allocation. The top study sequence is prescribed in code. In the lower example an LLM chooses an allowed tool using returned evidence, or finishes. These are useful engineering patterns rather than mutually exclusive universal categories; programmed workflows can also contain feedback loops.",
  "assumptions": "Illustrative routes, not a measured workflow or a hierarchy of maturity. Both paths need application-defined budgets, checks and stop conditions.",
  "source_refs": ["DEF03", "DEF04"],
  "source_url": "https://www.anthropic.com/engineering/building-effective-agents",
  "source_locator": "What are agents?; Workflow: Routing; Workflow: Evaluator-optimizer; Agents.",
  "tex_body": r"""
\node[rl] at (1.7,3.05) {Programmed};
\node[rp] (load) at (4.1,3.05) {};
\node[rp] (run) at (7.25,3.05) {};
\node[rp] (check) at (10.15,3.05) {};
\node[rp] (report) at (13.0,3.05) {};
\node[rn] at (4.1,3.72) {Load};
\node[rn] at (7.25,3.72) {Run};
\node[rn] at (10.15,3.72) {Check};
\node[rn] at (13.0,3.72) {Report};
\draw[rf] (load.east) -- (run.west);
\draw[rf] (run.east) -- (check.west);
\draw[rf] (check.east) -- (report.west);
\node[rl] at (1.35,1.1) {Model\\directed};
\node[rp] (llm) at (4.1,1.1) {};
\node[rn] at (3.2,1.1) {LLM};
\node[rp] (tool) at (7.65,1.1) {};
\node[rn] at (7.65,1.72) {Allowed tool};
\draw[rf] (llm.east) -- (tool.west);
\node[rn] at (5.9,1.47) {choose};
\draw[rf] (tool.south) -- (7.65,.28) -- (4.1,.28) -- (llm.south);
\node[rn] at (5.9,.65) {feedback};
\node[rp] (stop) at (11.8,1.1) {};
\node[rn] at (13.25,1.1) {Stop /\\report};
\draw[rf] (llm.north) -- (4.1,2.32) -- (11.8,2.32) -- (stop.north);
\node[rn,fill=white,inner sep=2pt] at (9.8,2.32) {finish};
"""
 },
 "va_authority": {
  "title": "Study autonomy stops at an operating authority boundary",
  "caption": "Original advisory-study example. The agent performs allowed studies and returns evidence for operator review. In this explicitly defined process, only the authorized operator approves an operating action; review may instead require revision or a stop.",
  "assumptions": "An illustrative allocation of authority, not a universal claim about every automation system or a representation of a particular utility's switching procedure. No live action is executed.",
  "source_refs": ["DEF02", "DEF01"],
  "source_url": "https://www.cs.ox.ac.uk/people/michael.wooldridge/pubs/ker95.pdf",
  "source_locator": "Historical agency properties inform the distinction; the illustrated authority boundary is an original application policy.",
  "tex_body": r"""
\node[rp] (agent) at (1.2,2.55) {};
\node[rp] (study) at (4.05,2.55) {};
\node[rp] (report) at (7.0,2.55) {};
\node[rp] (operator) at (10.0,2.55) {};
\node[rp] (action) at (13.0,2.55) {};
\node[rl] at (1.2,3.3) {Agent};
\node[rl] at (4.05,3.3) {Study};
\node[rn] at (4.05,1.9) {allowed};
\node[rl] at (7.0,3.3) {Report};
\node[rl] at (10.0,3.3) {Operator};
\node[rl] at (13.0,3.3) {Action};
\node[rn] at (13.0,1.9) {operating};
\draw[rf] (agent.east) -- (study.west);
\draw[rf] (study.east) -- (report.west);
\draw[rf] (report.east) -- (operator.west);
\draw[rf] (operator.east) -- (action.west);
\node[rn] at (12.25,2.93) {approve};
\draw[draw=rOrange,dashed,line width=.9pt] (11.4,1.0) -- (11.4,3.85);
\node[rn,text=rOrange] at (11.4,.48) {approval required};
\draw[rw] (operator.south) -- (10.0,.95) -- (7.0,.95) -- (report.south);
\node[rn,text=rOrange] at (8.5,1.36) {revise / stop};
"""
 },
 "va_three_graphs": {
  "title": "Three graphs with different meanings",
  "caption": "Original schematics: undirected physical equipment connections, directed calculation prerequisites with fork/join dependencies, and runtime execution routes with a retry cycle. The physical network and all labels are illustrative; the diagrams are not a minimal DAG or a measured paper trace.",
  "assumptions": "Physical edges describe connectivity, not instruction order. Task edges describe required outputs, not transmission lines. Runtime edges route execution; an execution cycle and an acyclic dependency graph can describe different views of the same application.",
  "source_refs": ["LG01", "D01"],
  "source_url": "https://docs.langchain.com/oss/python/langgraph/graph-api",
  "source_locator": "Official LangGraph graph model; original teaching comparison with the existing fault-record dependency example.",
  "tex_body": r"""
\node[rl] at (2.25,3.85) {Grid connections};
\node[rl] at (7.0,3.85) {Task DAG};
\node[rl] at (11.8,3.85) {Workflow loop};
\node[rp] (b1) at (.85,2.25) {};
\node[rp] (b2) at (2.3,2.25) {};
\node[rp] (b3) at (3.75,2.25) {};
\node[rp] (b4) at (2.3,1.2) {};
\draw[draw=rBlue,line width=1.15pt] (b1.east) -- (b2.west);
\draw[draw=rBlue,line width=1.15pt] (b2.east) -- (b3.west);
\draw[draw=rBlue,line width=1.15pt] (b2.south) -- (b4.north);
\node[rn] at (.85,1.7) {B1};
\node[rn] at (2.3,2.88) {B2};
\node[rn] at (3.75,1.7) {B3};
\node[rn] at (2.3,.7) {B4};
\node[rn] at (2.25,.23) {equipment links};
\node[rp] (a) at (5.25,2.25) {};
\node[rp] (b) at (6.75,2.8) {};
\node[rp] (c) at (6.75,1.4) {};
\node[rp] (d) at (8.45,2.25) {};
\coordinate (fork) at (5.9,2.25);
\draw[draw=rBlue,line width=1.15pt] (a.east) -- (fork);
\draw[rf] (fork) |- (b.west);
\draw[rf] (fork) |- (c.west);
\coordinate (join) at (7.75,2.25);
\draw[draw=rBlue,line width=1.15pt] (b.east) -- (7.75,2.8) -- (join);
\draw[draw=rBlue,line width=1.15pt] (c.east) -- (7.75,1.4) -- (join);
\draw[rf] (join) -- (d.west);
\node[rn] at (5.25,1.7) {A};
\node[rn] at (6.75,3.28) {B};
\node[rn] at (6.75,.85) {C};
\node[rn] at (8.45,2.9) {D};
\node[rn] at (7.0,.23) {needed results};
\node[rp] (plan) at (10.15,2.25) {};
\node[rp] (tool) at (11.65,2.25) {};
\node[rp] (check) at (13.15,2.25) {};
\draw[rf] (plan.east) -- (tool.west);
\draw[rf] (tool.east) -- (check.west);
\node[rn] at (10.15,2.94) {Plan};
\node[rn] at (11.65,2.94) {Tool};
\node[rn] at (13.15,2.94) {Check};
\draw[rw] (check.south) -- (13.15,1.0) -- (10.15,1.0) -- (plan.south);
\node[rn,text=rOrange] at (11.65,1.38) {retry};
\node[rn] at (11.8,.23) {next software step};
"""
 }
}


def build(contact=False):
    sys.path.insert(0, str(ROOT / "_rigorous_build" / "pythonpackages"))
    import pypdf
    from PIL import Image, ImageOps
    manifest, previews = {}, []
    temp_root = (ROOT.parents[2] / "tmp").resolve()
    with tempfile.TemporaryDirectory(prefix="visual_aids_", dir=temp_root) as temp:
        work = Path(temp).resolve()
        assert work.is_relative_to(temp_root)
        for font in ("arial.ttf", "arialbd.ttf", "consola.ttf"):
            shutil.copyfile(Path("C:/Windows/Fonts") / font, work / font)
        env = dict(os.environ)
        env["TECTONIC_CACHE_DIR"] = str(temp_root / "tectonic_cache_017_fresh")
        tectonic = temp_root / "tectonic-0.17.0" / "tectonic.exe"
        pdftoppm = Path(r"C:\Users\f00863x\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe")
        for stem, spec in DIAGRAMS.items():
            tex = ROOT / (stem + ".tex")
            tex.write_text(PRE + spec["tex_body"] + POST, encoding="utf-8")
            wrapper = work / (stem + "_wrapper.tex")
            wrapper.write_text(WRAP % tex.as_posix(), encoding="utf-8")
            result = subprocess.run([str(tectonic), "--only-cached", "--outdir", str(work), wrapper.name], cwd=work, env=env, capture_output=True, text=True)
            if result.returncode:
                raise RuntimeError(result.stdout + result.stderr)
            source = pypdf.PdfReader(wrapper.with_suffix(".pdf"))
            page = next(p for p in source.pages if (p.extract_text() or "").strip())
            writer = pypdf.PdfWriter(); writer.add_page(page)
            pdf = ROOT / (stem + ".pdf")
            with pdf.open("wb") as handle:
                writer.write(handle)
            svg = ROOT / (stem + ".svg")
            SVG_FROM_PDF(pdf, svg)
            assert "<image" not in svg.read_text(encoding="utf-8")
            assert len(pypdf.PdfReader(pdf).pages) == 1
            preview = work / stem
            subprocess.run([str(pdftoppm), "-scale-to-x", "1280", "-scale-to-y", "-1", "-singlefile", "-png", str(pdf), str(preview)], check=True, capture_output=True)
            with Image.open(preview.with_suffix(".png")) as im:
                previews.append(im.convert("RGB").copy())
            item = {key: value for key, value in spec.items() if key != "tex_body"}
            item.update({"id":stem,"tex":stem+".tex","pdf":stem+".pdf","svg":stem+".svg","file":stem+".svg", "credit":"Original editable TikZ teaching diagram; source and assumptions in caption"})
            manifest[stem] = item
        (ROOT / "visual_aid_manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
        if contact:
            sheet = Image.new("RGB", (1280, 430*len(previews)), "#EAF0F3")
            for index,im in enumerate(previews):
                sheet.paste(ImageOps.contain(im,(1260,410)),(10,index*430+10))
            buf=io.BytesIO(); sheet.save(buf,format="JPEG",quality=83)
            return base64.b64encode(buf.getvalue()).decode("ascii")
    return None


if __name__ == "__main__":
    print(build("--contact-base64" in sys.argv) or "Built six native TikZ visual aids, vector PDF/SVG, and manifest.")
