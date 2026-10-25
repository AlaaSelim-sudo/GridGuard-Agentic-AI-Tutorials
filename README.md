# GridGuard: Agentic AI for Power-System Operators

Two connected tutorials for power engineers, operators, researchers and instructors.

**[Open the tutorial website](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/)**

**Presenters:** Alaa Selim, MIT/Dartmouth; Mohamed Chehada, UT Austin.

[Choose a tutorial](#choose-a-tutorial) · [Run the lab](#run-the-lab) · [Present](#present-the-workshop) · [Edit and rebuild](#edit-and-rebuild) · [Archive](#archive)

<a id="watch"></a>

## Choose a tutorial

1. **[Foundations](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/foundations/#/1)** — 80 slides / 165 minutes / two exercises. Agent concepts, utility developments, power-system research and evidence. [Slides PDF](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/downloads/foundations.pdf).
2. **[Hands-on workshop](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/1)** — 80 slides / 180 minutes / three exercises. Begin with Stanford concepts, then run voltage, restoration and cyber studies in one Colab notebook. [Workshop overview](agentic_operator_cases_tutorial/README.md) · [Slides PDF](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/downloads/operator-cases.pdf).

The sessions can be taught separately. Combined teaching time is 5 hours 45 minutes, plus breaks. Viewing the presentations needs no installation or model account.

<a id="get-notebooks"></a>

## Run the lab

**Only Classroom Labs is required for the hands-on slides.**

[![Open Classroom Labs in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

1. Save a notebook copy in Drive and connect a CPU runtime.
2. Run the first setup cell until **Ready**, then L0 and L1. Keep both live-tool switches False.
3. During the workshop, run each named lesson when prompted. Change one input for each exercise, compare the new result and reset before continuing.

[Participant guide · PDF](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/downloads/participant-lab-guide.pdf) · [Colab setup and troubleshooting](COLAB_GUIDE.md) · [Complete notebook index](NOTEBOOK_INDEX.md).

Classroom Labs calculates numerical results now. L10B displays saved Llama choices, exact public reasons and original tool results; it makes no new model request or electrical solve. The standard route needs no GPU, API key or model download.

### Companion notebooks

Use these for additional study; they are separate from the required workshop route.

**LangGraph workflow lab:** state, tool routing, branching and execution.

[![Open the LangGraph workflow lab in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Graph_Workflow_Lab.ipynb)

**Agent traces and latency:** saved model replies, tool outputs and timing boundaries.

[![Open Agent traces and latency in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Agent_Trace_and_Latency.ipynb)

<a id="teach"></a>

## Present the workshop

- **[Presenter script online](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/Presenter_Script.html)** — spoken cues, timings, Colab actions and discussion prompts for all 80 slides. [PDF](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/downloads/operator-cases-presenter-script.pdf) · [Editable script](agentic_operator_cases_tutorial/Presenter_Script.md).
- **[Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/1)** — present the slides beside the script.
- **[Participant guide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/downloads/participant-lab-guide.pdf)** and **[exercise prompts](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/Exercises.html)** — share these with learners.
- **[Instructor guide](agentic_operator_cases_tutorial/Instructor_Guide.md)** and **[code-and-record guide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/Code_and_Record_Guide.html)** — detailed answers and exact notebook alignment.
- **[Teaching and Source Guide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/downloads/operator-cases-teaching-guide.pdf)** — complete references and figure credits.

The opening uses Monica Lam’s **CS224V Agentic AI, Lecture 1: Introduction**, Stanford University, Fall 2026, with original figures and clearly labeled grid adaptations. [Full lecture](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf) · [Source map and full paper citations](agentic_operator_cases_tutorial/README.md#stanford-teaching-materials).

For the **foundations session**, use the **[presenter script online](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/foundations/Presenter_Script.html)**: spoken explanations, visual walkthroughs, questions with answers and transitions for every slide. The printable version has one page per slide, a glossary and all 74 references. [Script PDF](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/downloads/foundations-presenter-script.pdf) · [Editable script](agentic_operator_tutorial/Presenter_Script.md) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/foundations/#/presenter/1) · [Instructor guide](agentic_operator_tutorial/Instructor_Guide.md) · [Reading guide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/foundations/Full_Reading_Guide.html).

<a id="edit"></a>

## Edit and rebuild

The current presentation sources and ready PDFs are included. Follow the **[hands-on build guide](agentic_operator_cases_tutorial/BUILD_GUIDE.md)** for authoring dependencies, source locations and the full rebuild command:

```text
python scripts/build-workshop.py check
python scripts/build-workshop.py all
```

- [Hands-on project](agentic_operator_cases_tutorial/README.md) · [Slidev source](agentic_operator_cases_tutorial/slidev/slides.md) · [Presenter cue source](agentic_operator_cases_tutorial/content/presenter_script.json).
- [Foundations project](agentic_operator_tutorial/README.md) · [Slidev source](agentic_operator_tutorial/slidev/slides.md) · [Presenter cue source](agentic_operator_tutorial/content/presenter_script.json) · [Script rebuild instructions](agentic_operator_tutorial/README.md#rebuild-the-presenter-script).
- [Website build guide](web/README.md) · [GitHub Pages workflow](.github/workflows/deploy-pages.yml).

Pushing the generated materials to `main` triggers the Pages workflow. The local build commands do not push or publish. Existing figure-capture and TikZ helpers have their own documented runtime requirements; the main build uses the supplied assets.

## Evidence and scope

The labs use synthetic or reduced networks. Fresh classroom calculations and the separate L10B archives are labeled. A model explanation, a numerical PASS, a simulated readback and an operator approval are different events. The closing control-room pilot is a teaching proposal. Recorded outcomes do not establish a general numerical advantage from adding an LLM.

## Archive

<details>
<summary>Earlier tutorial editions and publication records</summary>

Earlier work remains available for reproduction and comparison:

- [Original three-hour tutorial](agentic_grid_tutorial_3h/README.md).
- [MPC and deep reinforcement learning tutorial](agentic_grid_tutorial_mpc_drl/README.md).
- [Greensboro multi-agent tutorial](smartgridcomm_greensboro/README.md) and [recorded Llama edition](smartgridcomm_greensboro_llama_v2/README.md).
- [Earlier operator-workflow package](Grid_Operator_Workflow_Tutorial/agentic_grid_workflow_tutorial/README.md) and [earlier LaTeX source package](Agentic_Grid_LaTeX_Source/README.md).

Use the two **Watch** links above for the current presentations. Some unchanged notebooks also appear inside presentation evidence folders. [PUBLICATION_MANIFEST.json](PUBLICATION_MANIFEST.json) and [PUBLICATION_AUDIT.json](PUBLICATION_AUDIT.json) record the initial upload, source locations, SHA-256 hashes and publication checks. Later edits are recorded in Git history. Installed dependencies, build caches and duplicate delivery bundles are excluded.

</details>

## Sources and credits

Primary references, paper URLs, image credits and evidence limits accompany the slides and guides. See [THIRD_PARTY_SOURCES.md](THIRD_PARTY_SOURCES.md). Independent educational material using an IEEE ComSoc theme; IEEE sponsorship or endorsement is not claimed. Third-party materials retain their respective terms.
