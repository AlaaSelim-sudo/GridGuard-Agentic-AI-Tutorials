# Agentic AI for Grid Operators — LaTeX teaching edition

This is the revised teaching source. The course uses native **LaTeX Beamer**, editable **TikZ diagrams**, typeset equations, exact notebook excerpts and numerical plots. It contains no AI-generated imagery. The source is ordinary editable LaTeX, not exported slide screenshots.

The teaching sequence starts from an operator problem, works through a small calculation, defines the corresponding concept, and then runs the notebook experiment. The full three-hour route includes the foundations, voltage support, restoration, cyber response and operator review. There is no appendix.

## Files to use

- `main.tex` / `main.pdf`: lecture with Beamer reveals. Advance the PDF one page to reveal the next step; the logical frame number stays unchanged during a reveal. Fade effects depend on the viewer, but the progressive pages work in ordinary PDF viewers.
- `handout.tex` / `handout.pdf`: one completed page per logical frame, for review and printing.
- `study_guide.tex` / `study_guide.pdf`: written explanations, worked examples, notebook instructions, questions, answers and references.
- `chapters/`: editable chapter text and TikZ drawings. The teaching notes are embedded with `\note{...}` beside each frame.
- `preamble.tex`: typography, colors, code style and common teaching commands.
- `snippets/`: exact excerpts and complete classroom cells extracted from the supplied notebooks.
- `Slide_Notebook_Map.json`: source lines, notebook checkpoints and hashes for the code actually included in this lecture.

## Compile

Use a current TeX Live or MiKTeX installation with XeLaTeX, Beamer, TikZ/PGFPlots, listings, mathtools, booktabs and tabularx. No shell escape, Python, image-generation service or web application is required to compile the slides.

```text
xelatex main.tex
xelatex main.tex
xelatex handout.tex
xelatex handout.tex
xelatex study_guide.tex
xelatex study_guide.tex
```

Alternatively, run `tectonic main.tex`, `tectonic handout.tex`, then `tectonic study_guide.tex`. The study guide imports selected completed slide pages as vector figures, so compile `handout.tex` first. The source package includes the compiled PDFs.

After changing chapter teaching notes, run `python scripts/sync_study_guide.py` to refresh the guide and the code mapping, then recompile it. This optional synchronization uses only the Python standard library.

## Three-hour route

| Minutes | Teaching and experiment |
|---|---|
| 0–40 | Operator question, worked scalar example, agents/tools, DAGs, state, routing, real LangGraph G0–G5, contracts L0–L1 |
| 40–80 | Voltage physics, MPC, SAC, model scope, L2–L5 and actual Llama response selection |
| 80–90 | Break |
| 90–115 | Restoration paths, capacity, service priorities, MILP, L6–L7 |
| 115–142 | Measurements, state estimates, residuals, stealth attacks and constrained response, L8–L9 |
| 142–150 | Evaluation, current research, optional L11 and measured latency |
| 150–180 | Control-room deployment examples, operator packet and L12, capstone and synthesis |

L10 contains archived five-stage traces and is revisited within the case discussions. Keep installation and model downloads outside class. Use the executed HTML notebooks if an audience member cannot run a local kernel.

The notebooks live one level above this project in the complete tutorial. Use separate Python environments for `Graph_Workflow_Lab.ipynb` and `Classroom_Labs.ipynb`, following `requirements_graph_lab.txt` and `requirements_linear.txt`. Install `requirements.txt` and enable `RUN_OPENDSS=True` for the optional full model audit. Set `RUN_LOCAL_LLAMA=True` only when the existing Ollama service and model are ready.

## What the results establish

The voltage study uses one synthetic SMART-DS Greensboro feeder. The restoration classroom exercise is a six-node transport model and the cyber classroom exercise is a four-bus DC model. The introductory scalar calculations are explicitly illustrative. The graph lab runs real LangGraph on a toy response; the engineering studies use their existing Python supervisor.

MPC and SAC remain numerical tools in the workflow. Language responses propose or explain permitted next steps; numerical checks determine feasibility. The recorded experiments include ties and failures and do not establish general superiority over strong conventional baselines. The operator exercise records an advisory acknowledgment and does not dispatch equipment.

## Visual and scientific provenance

TikZ diagrams in the chapter files are original explanatory drawings of the declared models and processes. Numerical plots come from the tutorial outputs. Scientific references appear at the bottom of every frame and in the study guide. Sources for any retained paper artwork are listed in `Figure_Provenance.md`; this lecture does not use AI-generated control-room pictures.

## Control-room deployment examples

Frames D01–D09 (including D04B) add an illustrated deployment path and operator scenarios. They cover operational data sources, proposed advisory services, voltage alerts, restoration priorities and request interpretation, suspect measurements, human review and field readback, study expiry, and staged pilot evaluation. The current notebook remains an advisory sandbox. Live connectors, authenticated operator identities, durable service recovery, command authorization and field readback are proposed deployment work.

The final 30 minutes now include these examples, a four-minute pair rehearsal and the existing L12 exercise. The total timetable remains three hours.
