# Agentic AI for Grid Operators — Slidev teaching edition

A complete **three-hour teaching sequence with 128 logical slides**, integrated hands-on work and **no appendix**. The local **Grid Classroom** theme uses diagrams, equations, paper figures, code highlights and click-by-click reveals within the same slide. This project uses **Slidev 53.0.0**.

## Present the prepared deck

With **Node.js 22 or later** available, open PowerShell in this folder and run:

```powershell
.\Start_Slides.ps1
```

Open [http://127.0.0.1:3033](http://127.0.0.1:3033). Keep that terminal open; press `Ctrl+C` there when finished. The launcher serves the included `dist` folder locally. **No package installation is needed to present the prebuilt deck.** Do not open `dist/index.html` directly as a file.

Use the right arrow or space to advance reveals, then slides; use the left arrow to go back. The Slidev toolbar provides navigation and presentation controls. Animations live in the browser presentation. PDF files contain static final states.

## What to use

| Resource | Purpose |
|---|---|
| [Agentic_Grid_Slides.pdf](Agentic_Grid_Slides.pdf) | Static slide reference, one final state per logical slide. |
| [Agentic_Grid_Handout.pdf](Agentic_Grid_Handout.pdf) | Reading guide with explanations, symbols, code, experiments, expected observations and references. |
| [Teaching_Guide.md](Teaching_Guide.md) | Instructor preparation, timing and lab guidance. |
| [Graph_Workflow_Lab.ipynb](../Graph_Workflow_Lab.ipynb) | G0–G5: actual LangGraph execution, bounded repair and simulated human readback. |
| [Classroom_Labs.ipynb](../Classroom_Labs.ipynb) | L0–L12: numerical experiments, real archived model responses and advisory operator review. |
| [Graph reading page](../Graph_Workflow_Lab.html) / [Classroom reading page](../Classroom_Labs.html) | Executed outputs for reading without a Python kernel. |
| [Notebook map](content/notebook_map.json) | Slide IDs, exact cell ranges and source/excerpt hashes. |

The prebuilt browser package also includes notebook reading pages under `notebooks/` and the printable [handout page](http://127.0.0.1:3033/Handout.html).

The current teaching route is this Slidev edition. Earlier LaTeX files retained elsewhere in the tutorial folder are legacy material; they are not the source of this deck. The Slidev source package contains the editable Slidev project.

## Three-hour route

| Minutes | Topic | Notebook |
|---|---|---|
| 0–40 | Agent concepts, research, DAGs, state and graph execution | G0–G5; L0–L1 |
| 40–82 | Voltage support: MPC, SAC, Llama and model scope | L2–L5 |
| 82–92 | Break | Save work |
| 92–119 | Restoration: priorities, MILP and stale evidence | L6–L7; recorded L10 trace |
| 119–149 | Cyber response: WLS, detector limits and constrained recovery | L8–L9; recorded L10 trace |
| 149–158 | Evaluation, research frontier, optional Llama and latency | L11 |
| 158–180 | Control-room handoff, readback, capstone and synthesis | L12 |

## Edit and rebuild

Source content lives in `content/foundations.json`, `content/cases.json` and `content/closing.json`. Each lesson carries its teaching text, notes, references and any exact notebook excerpt. `scripts/prepare.mjs` combines these into the generated lesson data, notebook map and `slides.md`.

The layouts, animated teaching components and visual theme are in `components/`, `layouts/`, `styles/`, `theme/` and `style.css`. Edit those for presentation behavior. Edit the content JSON for durable text changes: **running `prepare-content` regenerates `slides.md`**.

For authoring, install project dependencies using the included lockfile:

```powershell
pnpm install --frozen-lockfile
pnpm run prepare-content
node scripts/handout.mjs
pnpm run dev
```

The development presentation uses port **3030**. To refresh the prepared browser package:

```powershell
pnpm run build
```

`node scripts/handout.mjs` generates `public/Handout.html` from the same lesson content. Run it before `build` so the prepared site includes the refreshed handout. The handout page has a print button for saving a PDF. The `export` package script provides Slidev PDF export. For CLI export, install `playwright-chromium` and its Chromium browser, or pass `--executable-path` with your installed Chrome/Edge executable. Keep export settings at final click states for the static slide reference.

The handout includes static exports of the teaching diagrams in `public/assets/diagrams/`. If you change a diagram, refresh that SVG from the browser before rebuilding the handout. The animated presentation renders the editable Vue component directly.

Notebook excerpts are extracted from the notebooks one folder above this project. Preserve that directory relationship when rebuilding. The graph and engineering Python environments are separate from Node/Slidev; see the teaching guide before running the labs.

## Evidence and figure provenance

- Fresh numerical calculations, saved-policy inference, archived actual LLM responses and optional live calls are labeled separately.
- The voltage example uses one synthetic SMART-DS Greensboro feeder. Restoration and cyber classroom experiments also use explicitly separate small fixtures.
- The five proposed stages are awareness, planning, simulation, verification and the LLM optimizer, followed by advisory human review. The notebook does not dispatch equipment.
- Results include ties and limitations; the materials do not claim general superiority of additional agents over conventional numerical workflows.
- Paper figures retain individual attribution and licenses. See [paper_assets.json](content/paper_assets.json) and [ATTRIBUTION.txt](public/assets/papers/ATTRIBUTION.txt). PowerDAG artwork is CC BY-SA 4.0; Grid-Agent and ReAct artwork is CC BY 4.0. Preserve credits, license links and change notices when adapting them.

