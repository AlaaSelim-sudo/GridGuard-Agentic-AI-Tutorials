# GridGuard: Agentic AI for Power-System Operators

Tutorial notebooks, recorded experiments, and presentation material on voltage support, service restoration and cyber response.

## Start here

- [Foundations presentation: 80 slides](agentic_operator_tutorial/latex/main.pdf) — agent definitions, power-system research, frameworks and utility case studies; IEEE ComSoc theme.
- [Three operator cases: 59 slides](agentic_operator_cases_tutorial/Three_Operator_Cases.pdf) — a 120-minute follow-on with real GridGuard screenshots, five-step recorded walkthroughs and three exercises.
- [Three-case teaching and source guide](agentic_operator_cases_tutorial/Teaching_and_Source_Guide.pdf) — explanations, timings, exercise debriefs, full citations and evidence boundaries.
- [Code and recorded-result guide](agentic_operator_cases_tutorial/Code_and_Record_Guide.html) — source statements, original files, model-call journals and result records.
- [Classroom Labs notebook](agentic_grid_workflow_tutorial/Classroom_Labs.ipynb) and [LangGraph workflow lab](agentic_grid_workflow_tutorial/Graph_Workflow_Lab.ipynb).
- [Complete notebook index](NOTEBOOK_INDEX.md).

The foundations presentation is the restored edition before the later image-notice revision. The current three-case presentation makes the responsibilities explicit: inputs → bounded model choice → Python numerical tool → recorded result → operator review. Its code panels reference original source lines and preserve the same Python statements.

## What is included

The current workshop folder preserves all 12 teaching notebooks, their executed HTML views, source code, feeder inputs, saved model weights, numerical results, original local model-call journals, figures, dashboards and requirements. The two current presentation folders contain PDFs, editable LaTeX/TikZ and Slidev sources, figures, complete source credits and teaching guides.

Earlier tutorial editions are retained in `agentic_grid_tutorial_3h`, `agentic_grid_tutorial_mpc_drl`, `smartgridcomm_greensboro`, `smartgridcomm_greensboro_llama_v2`, `Grid_Operator_Workflow_Tutorial` and `Agentic_Grid_LaTeX_Source`. They provide historical notebooks and presentations; start with the current links above. Some notebooks also appear as unchanged evidence copies inside presentation projects.

[PUBLICATION_MANIFEST.json](PUBLICATION_MANIFEST.json) lists every copied tutorial file, its original project-relative location, size and SHA-256 hash. Active three-case project paths are rebased using its existing portable-package conversion; the manifest records that change. Archived raw journals remain unchanged. Installed dependencies, build caches, temporary files and duplicate delivery ZIPs are excluded; the unpacked material is included. Small saved-model ZIP checkpoints are retained where the source uses them.

## Read, present and edit

GitHub can display notebooks and PDFs directly. Download or clone the repository to open the saved interactive HTML dashboards and source guides locally.

For either current Slidev project, enter its `slidev` directory, install the dependencies pinned in `package.json` using npm or pnpm, and run `npm run dev`. The built `dist` output and `node_modules` are intentionally not committed. The two presentations use separate local preview ports in their own scripts; see each project README.

For LaTeX, compile `latex/main.tex` in either current presentation folder. The three-case written guide uses `latex/teaching_guide.tex`. The projects retain native editable TikZ and the vector assets used by the PDFs. A normal TeX installation or Tectonic can compile them. Some graphics-generation utilities contain environment-specific runtime paths; the already generated assets are provided.

## Run the notebooks

Enter `agentic_grid_workflow_tutorial` and follow its [README](agentic_grid_workflow_tutorial/README.md) and instructor guide. Create a dedicated Python environment using the supplied requirements, then open `Classroom_Labs.ipynb`. The separate graph lab has its own requirements. Recorded studies retain their original version metadata; a fresh environment installation was not performed for this publication.

The default classroom path uses numerical tools, saved policy weights and archived model replies. Optional OpenDSS runs and local Ollama calls require the corresponding dependencies and models. Reading saved outputs makes no new language-model call and operates no equipment.

## Interpreting the evidence

Voltage uses a synthetic SMART-DS feeder. Restoration uses a separate six-node transport graph; cyber uses a separate four-bus DC fixture. Archived experiment families are labeled separately. A solver result, a language-model explanation and a human approval are different events. The recorded walkthroughs retain their original REVIEW or PENDING outcomes. They establish neither live utility deployment nor a general numerical advantage from adding a language model.

The archived workshop uses custom Python supervisors. The separate current GridGuard application uses LangGraph; these dated records do not validate that newer application runtime.

## Sources and rights

Full references, publisher/author URLs, image credits, provenance manifests and recorded evidence limits are kept with the material. This is an independent educational adaptation of IEEE ComSoc artwork and colors. Sponsorship or endorsement is not claimed. See [THIRD_PARTY_SOURCES.md](THIRD_PARTY_SOURCES.md) and the preserved dependency notices. No blanket license is applied to third-party figures, photographs, paper crops, logos or source material.

The screenshot and diagram regeneration helpers were authored for the original Windows runtime. Their bundled-browser/TeX/DLL paths may require adjustment elsewhere; the ready screenshots, vector figures, PDFs and presentation sources are included.
