"""Two editable native TikZ introductory/prerequisite teaching figures.

Only revision_*.tex/.pdf/.svg and revision_graph_manifest.json are published.
Use --contact-base64 for a transient 1280px-wide rendered QA sheet.
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
    "revision_agent_roles": {
        "title": "The agent chooses; the tool executes a capability",
        "caption": "Original teaching abstraction for diagnosing a frozen base case v43. An LLM agent chooses a tool call, the callable interface runs against the case and solver, and returned evidence informs the next choice. LangGraph is shown as a possible orchestration runtime for state and execution, not as a grid solver or a claim about a particular PowerAgent implementation.",
        "assumptions": "The v43 case, run_pf(v43, base) interface and feedback fields are illustrative; no tool was executed and no numerical outcome is asserted. Tool and agent name interface/decision roles; a tool may internally wrap another agent or a complex service. The outer framework marker does not establish the correctness of any electrical result. No PowerAgent SDK relationship is claimed.",
        "source_refs": ["DEF01", "DEF03", "DEF04", "LG01"],
        "source_urls": [
            "https://aima.cs.berkeley.edu/4th-ed/pdfs/newchap02.pdf",
            "https://www.anthropic.com/engineering/building-effective-agents",
            "https://docs.langchain.com/oss/python/langgraph/overview",
            "https://docs.langchain.com/oss/python/langchain/tools"
        ],
        "source_locator": "Russell/Norvig Section 2.1; Anthropic 'What are agents?' and 'Agents'; official LangGraph overview and Tools opening definitions.",
        "tex_body": r"""
\node[rp] (goal) at (1.35,2.6) {};
\node[rl] at (1.35,3.28) {Goal};
\node[rn] at (1.35,1.92) {diagnose v43};
\node[rp] (agent) at (4.45,2.6) {};
\node[rl] at (4.45,3.28) {LLM agent};
\node[rp] (tool) at (8.25,2.6) {};
\node[rl] at (8.25,3.28) {Tool};
\node[rc] at (8.25,1.98) {run\_pf(v43, base)};
\node[rp] (environment) at (12.2,2.6) {};
\node[rl] at (12.2,3.28) {Environment};
\node[rn] at (12.2,1.98) {case + solver};
\draw[rf] (goal.east) -- (agent.west);
\draw[rf] (agent.east) -- (tool.west);
\draw[rf] (tool.east) -- (environment.west);
\node[rn] at (6.35,2.96) {choose call};
\node[rn] at (10.25,2.96) {execute};
\draw[rf] (environment.east) -- (13.65,2.6) -- (13.65,.72) -- (4.45,.72) -- (agent.south);
\node[rn] at (9.0,1.17) {convergence / error / artifact};
\draw[draw=rCyan,line width=.9pt] (3.35,3.62) -- (3.35,3.8) -- (9.25,3.8) -- (9.25,3.62);
\node[rn,text=rBlue] at (6.3,4.03) {LangGraph: state + execution};
"""
    },
    "revision_powerdag_gate": {
        "title": "Check the prerequisite before executing a state-dependent tool",
        "caption": "Original teaching adaptation of PowerDAG v4, Section IV-C, PDF p.5. A planner proposes a voltage-violation check. A prerequisite gate blocks execution and returns the missing solve to the planner when the required solved network state is unavailable; otherwise the check proceeds. This is neither exact source code nor the complete/minimal workflow DAG.",
        "assumptions": "The v43 identifier and call wording are illustrative. The figure strengthens the teaching condition to a solution for the current named network. The paper's formal supervisor tests required Write-tool names against executed-tool names; do not infer from that alone a version-aware freshness/invalidation guarantee. Rule coverage is curated rather than exhaustive, and unruled tools remain executable. A blocked call leaves environment state unchanged; passing this prerequisite is not a numerical feasibility or safety proof.",
        "source_refs": ["PD01"],
        "source_url": "https://arxiv.org/pdf/2603.17418v4",
        "source_locator": "Section IV-C, PDF p.5, voltage-violation example and Eqs. (8)-(10); Algorithm 1. Figure 2, PDF p.3, locates the supervisor between planner and executor.",
        "tex_body": r"""
\node[rp] (planner) at (1.5,2.5) {};
\node[rl] at (1.5,3.25) {Planner};
\node[rp] (gate) at (7.0,2.5) {};
\node[rl] at (7.0,3.5) {Gate:\\solved for v43?};
\node[rp] (check) at (11.95,2.5) {};
\node[rl] at (11.95,3.4) {Run voltage\\check};
\node[rn] at (11.95,1.87) {current solution};
\draw[rf] (planner.east) -- (gate.west);
\node[rn] at (4.0,2.96) {propose check};
\draw[rf] (gate.east) -- (check.west);
\node[rn] at (9.45,2.96) {met};
\draw[rw] (gate.south) -- (7.0,.78) -- (1.5,.78) -- (planner.south);
\node[rn,text=rOrange,anchor=west] at (7.35,1.52) {unmet: no execution};
\node[rn,text=rOrange] at (4.25,1.2) {missing: solve v43 first};
"""
    }
}


def build(contact=False):
    sys.path.insert(0, str(ROOT / "_rigorous_build" / "pythonpackages"))
    import pypdf
    from PIL import Image, ImageOps
    manifest, previews = {}, []
    temp_root = (ROOT.parents[2] / "tmp").resolve()
    with tempfile.TemporaryDirectory(prefix="revision_graphs_", dir=temp_root) as temp:
        work = Path(temp).resolve()
        assert work.is_relative_to(temp_root), "Temporary cleanup must remain inside workspace tmp"
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
            result = subprocess.run([str(tectonic), "--only-cached", "--outdir", str(work), wrapper.name],
                                    cwd=work, env=env, capture_output=True, text=True)
            if result.returncode:
                raise RuntimeError(result.stdout + result.stderr)
            source = pypdf.PdfReader(wrapper.with_suffix(".pdf"))
            page = next(p for p in source.pages if (p.extract_text() or "").strip())
            writer = pypdf.PdfWriter()
            writer.add_page(page)
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
            item = {key: value for key, value in spec.items() if key != "tex_body"}
            item.update({"id": stem, "tex": stem + ".tex", "pdf": stem + ".pdf", "svg": stem + ".svg",
                         "file": stem + ".svg", "credit": "Original native TikZ educational diagram; source and assumptions in caption"})
            manifest[stem] = item
        (ROOT / "revision_graph_manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        if contact:
            sheet = Image.new("RGB", (1280, 430 * len(previews)), "#EAF0F3")
            for index, im in enumerate(previews):
                sheet.paste(ImageOps.contain(im, (1260, 410)), (10, index * 430 + 10))
            buf = io.BytesIO()
            sheet.save(buf, format="JPEG", quality=85)
            return base64.b64encode(buf.getvalue()).decode("ascii")
    return None


if __name__ == "__main__":
    result = build("--contact-base64" in sys.argv)
    print(result or "Built two revision diagrams in native TikZ, vector PDF and SVG; manifest validated.")
