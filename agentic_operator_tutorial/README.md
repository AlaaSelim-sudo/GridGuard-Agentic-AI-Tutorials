# Agentic AI for Utility Operators

**80 slides in one integrated 165-minute teaching route, including two worked exercises.** Every slide belongs to the session. Application studies address power-system tasks; the opening definitions use classical agent literature and current engineering terminology. Evidence reviewed 18 October 2026. This tutorial prepares the audience for the separate three-case GridGuard workshop.

The deck uses an IEEE ComSoc theme and genuine source images on **46 of 80 slides**. These include utility article screenshots, original paper architectures, actual software interfaces, operator photographs and source-authored framework illustrations. Thirteen quantitative plots remain. Eight native TikZ diagrams appear in the talk; fifteen other editable TikZ alternatives are retained in the source package. Plain-language text accompanies the images throughout. Slides contain no tables, transitions or click reveals. The source line on each slide gives the primary reference's full author/issuer, title and publication details. All supporting sources and complete URLs appear in the presenter notes, instructor guide and separate reading guide.

## Present the tutorial

- **[Presenter script online](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/foundations/Presenter_Script.html)**: complete spoken explanations for all 80 slides, visual walkthroughs, quick questions with expected answers and transitions. Search by term, paper or slide number. Expand a slide's visual or source credits when preparing.
- **[Printable presenter script](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/downloads/foundations-presenter-script.pdf)**: one page per slide, relative start/end times, both worked exercises, a plain-language glossary and all 74 full references. Use its PDF bookmarks to reach a slide or source. [Editable Markdown](Presenter_Script.md).
- **[Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/foundations/#/presenter/1)**: open beside the script. The narration follows the accepted slide order and the deck's 18 October 2026 evidence snapshot.
- `latex/main.pdf`: complete presentation.
- `slidev/slides.md`: editable Slidev source with presenter notes.
- `Instructor_Guide.md`: cumulative timing, explanations and exercise answers.
- `Full_Reading_Guide.pdf` and `.html`: 74 complete source entries, original papers, documentation, full URLs and visual credits. The reading guide is untimed.
- `LaTeX_Source.zip`: portable native TikZ/LaTeX source, required images, reading-guide source and visual data.
- `Agentic_Operator_Tutorial_Complete.zip`: both formats, built web presentation, sources, notes and credits.

`latex/presentation.pdf` is a compatibility copy of the same presentation.

### Use the script to teach

1. Read **Say** as a starting explanation and adapt it to your voice.
2. Use **Show / explain** to walk through the actual image, graph, equation or concept. The online script can display the existing source visual beside its teaching cues.
3. Use **Ask** for a quick check, then reveal the **Expected answer** during discussion. Use the exercise timers on slides 26 and 53.
4. Use **Transition** to connect the point to the next slide. The 165-minute schedule includes discussion and the two exercises; add breaks separately.

No notebook or model account is required for this foundations session. The separate hands-on session uses one required Classroom Labs notebook. Research explanations retain each metric's task, denominator, scoring rule and evidence limits.

With Node.js installed, run from the package folder:

```text
node slidev/preview-server.mjs
```

Open **http://127.0.0.1:3043/**. The built presentation requires no model account, API key or dependency installation. Internet access is needed for external readings. The server stays local to this computer; stop it with Ctrl+C.

## Teaching route

The opening asks “What is agentic AI?” and defines agents, callable tools, workflows and orchestration. Russell and Norvig establish the classical perception/action view; Wooldridge and Jennings supply the historical properties of agency. Anthropic's workflow/agent distinction is attributed as an engineering convention. The agent/tool/runtime diagram uses an illustrative grid-study task, with autonomy bounded by its assigned permissions and success criteria.

The news section examines Tapestry/PJM HyperQ, CAISO/OATI outage review, Duke/AWS planning support, Siemens' announced agentic planning capabilities, National Grid's project assurance and GE Vernova's integration platform. New Eversource and NYPA material describes engineering capability-building and data-quality work, without claiming a production agent deployment from a vacancy or a separate product demonstration. Named deployments, supplier-reported measurements, utility disclosures and product announcements are identified separately.

The operator section defines data, engineering and decision validity through typed calls, unit contracts, topology versions and solver status. Exercise 1 (slide 26, six minutes) asks participants to audit three returned evidence packets against a stated advisory task.

The power-system research sequence covers Harvard's PowerAgent roadmap and a concrete PowerWF/LangGraph example; PowerDAG's exemplar retrieval, prerequisite gate and controlled benchmark; DrAgent; feedback-driven DALINE/MATPOWER simulation agents; X-GridAgent; both GridMind studies; PowerAgentBench-Dyn; Grid-Agent; VeraGrid-Agent; AgentiGrid; a grid-task capability study; and PowerBench. Each study retains its task, tools, workflow, measured results and limits. PowerAgent is distinguished from its later benchmark. PowerDAG uses the inspected v4 rather than older search headlines. Percentages from different studies are not a comparative ranking.

LangGraph and directed acyclic graphs are taught in the middle of the course through DrAgent's disturbance-analysis dependencies and GridMind's weather-risk workflow. The diagrams distinguish the electrical network, artifact dependencies and stateful execution. They explain conditional loops, state merging, checkpoints, changed inputs, parallel studies and incomplete joins. Framework documentation is cited separately from paper implementations; an SDK is not inferred when a paper does not name it.

Exercise 2 (slide 53, eight minutes) asks groups to decide what must rerun after a cascade-parameter change or forecast shift and what an operator should receive when a required stage fails. Answers are in presenter notes and the instructor guide.

The final section teaches uncertainty, compounded workflow reliability, conditional false approvals, zero-failure bounds, tool interfaces, trust boundaries and pilot evaluation. It ends with the acceptance contract used in the follow-on voltage support, restoration and cyber-response workshop. There are no appended extension slides.

## Edit and rebuild

Edit `power_content.py` and run:

```text
python build_tutorial.py
```

Retained power-domain material is in `power_retained_content.json`; `revision_content.py` supplies the integrated definition, utility-update and PowerAgent/PowerDAG additions. The final wording is applied from `plain_language_1.json` and `plain_language_2.json`, followed by `visual_revision.py`. The final source-image placements, captions and local wording refinements are applied by `real_image_revision.py` from `research/real_image_slide_plan.json`. These overrides use the corresponding original title keys or verified slide numbers; update their entries when changing slide wording. The route does not import previous editions. The renderer is `build_teaching.py`. `build_intro.py` supplies shared reading-guide helpers. Source metadata is in `research/source_map.json`.

Compile `latex/main.tex` and `latex/reading_guide.tex` with pdfLaTeX, XeLaTeX or Tectonic. Compile twice for final links and page counts. No shell escape is required. The LaTeX project opens with `main.tex` as its main document.

Used figures, diagram alternatives and the exact source-image slide count are listed in `build_manifest.json`. LaTeX includes native TikZ and vector chart/source PDFs; Slidev uses SVG display wrappers and source images. Provenance is consolidated in `visual_provenance.json`. Article screenshots retain original page pixels. Figure excerpts select the relevant original panel without redrawing its content. Display wrappers embed unchanged original image bytes; the originals behind those wrappers are included. Paper crops retain native PDF text where available. Acquisition and framing scripts are in `research/acquire_real_*`, `research/capture_real_framework_diagrams.mjs` and `research/frame_*`. The editable teaching figures are generated by `diagrams/build_visual_aids.py` and `diagrams/build_domain_visuals.py`. Recreating a paper crop additionally requires the original paper from its recorded source URL. Plot generators require Matplotlib; native diagram generators require a TeX runtime.

For Slidev editing:

```text
cd slidev
npm install
npm run dev
npm run build
```

Pinned dependencies and the lockfile are included. The built `dist` folder can also be served by another static web server.

### Rebuild the presenter script

Edit `content/presenter_script.json`. Each entry is matched to its exact slide title and number, so an altered slide order prompts a review rather than silently attaching the wrong explanation. From the repository root:

```text
python -m pip install -r agentic_operator_cases_tutorial/requirements-authoring.txt
python agentic_operator_tutorial/build_presenter_script.py --pdf
python agentic_operator_tutorial/build_presenter_script.py --check
node scripts/build-pages.mjs --base /GridGuard-Agentic-AI-Tutorials/
```

The first command installs the shared authoring dependencies. Script generation updates `Presenter_Script.md`, `.html` and `.pdf`, their copies under `slidev/public/`, and a source-hash manifest in `research/presenter/`. Validation checks all 80 explanations, 165-minute timing, exercise positions, figure paths, the PDF's one-page-per-slide structure and matching public copies. The site build also needs the pinned Node dependencies described in [the website guide](../web/README.md).

Run the existing slide build first after changing the teaching content, then review and regenerate the script. Script generation itself does not change the slides or notebooks. `research/author_foundations_script.py` preserves the original narration-authoring record against the accepted Git baseline; routine edits use the JSON source above.

## Theme and visual sources

This is an independent educational adaptation of IEEE ComSoc's official network artwork and blue/cyan palette. The artwork and lockup are preserved. Arial and Latin Modern replace proprietary Formata. IEEE endorsement or sponsorship is not claimed.

Empirical results, calculated intervals and invented examples are labeled separately. The DrAgent count chart reconstructs the authors' score cells and preserves the Q6 grading exception; it is not an independent experiment. HyperQ computational timings exclude document-transfer latency and human validation. Small-sample intervals assume comparable independent trials. The GridGuard feeder is synthetic. Research harnesses may require licensed simulators. Source terms and recorded licenses govern redistribution.
