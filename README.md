# GridGuard: Agentic AI for Power-System Operators

Two connected tutorials for power engineers, operators, researchers and instructors. Begin with agentic AI concepts and power-system evidence, then follow recorded engineering cases from inputs and tool calls to results and human review.

**[Open the tutorial site](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/)**

[Watch](#watch) · [Get notebooks](#get-notebooks) · [Teach](#teach) · [Edit](#edit) · [Archive](#archive)

## Watch

1. **[Foundations — open the slides](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/foundations/)** · **80 slides / 165 minutes**. Agents, tools and workflows; utility developments; power-system research; LangGraph concepts; and how to assess evidence. Includes two exercises. [Download the PDF](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/downloads/foundations.pdf).
2. **[Three operator cases — open the slides](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/)** · **59 slides / 120 minutes**. Voltage support, service restoration and cyber response, with three four-minute exercises. Genuine saved notebook screenshots and original code show **inputs → bounded model choice → Python tool → recorded result → operator review**. [Download the PDF](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/downloads/operator-cases.pdf).

The browser presentations need no Python installation, model account or live language-model service. Both use an IEEE ComSoc visual theme and include source credits and presenter notes. The sessions can be taught separately; their combined scheduled time is 4 hours 45 minutes.

## Get notebooks

Start with the [Classroom Labs](agentic_grid_workflow_tutorial/Classroom_Labs.ipynb) for the numerical cases and the separate [LangGraph workflow lab](agentic_grid_workflow_tutorial/Graph_Workflow_Lab.ipynb) for graph execution, state and branching.

For a closer look at the evidence:

- [Agent traces and latency](agentic_grid_workflow_tutorial/Agent_Trace_and_Latency.ipynb): actual saved model replies, tool outputs, stopping decisions and measured timing boundaries.
- [Standard formulations](agentic_grid_workflow_tutorial/Standard_Formulations.ipynb): optimization, restoration MILP and state-estimation/control examples.
- [LLM response selection](agentic_grid_workflow_tutorial/LLM_Response_Selection.ipynb): the recorded voltage response-selection study and its comparisons.
- [Complete notebook index](NOTEBOOK_INDEX.md): all 12 current workflow notebooks and preserved earlier editions.

GitHub previews the notebooks. To run them, clone or download the repository so each notebook keeps its sibling `src`, `data`, `models` and `results` folders. Follow the [workflow setup guide](agentic_grid_workflow_tutorial/README.md); the graph lab uses its own requirements.

**Saved and live execution are different.** Opening saved outputs makes no new model call. The default Classroom Labs path performs numerical calculations with saved policy weights and archived model replies. Optional full-feeder OpenDSS checks, local Ollama calls and policy training require their respective dependencies and models. Earlier studies retain their original environment metadata.

## Teach

- **Foundations:** [instructor guide](agentic_operator_tutorial/Instructor_Guide.md) and [full reading and source guide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/foundations/Full_Reading_Guide.html).
- **Operator cases:** [instructor guide](agentic_operator_cases_tutorial/Instructor_Guide.md), [teaching and source guide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/downloads/operator-cases-teaching-guide.pdf), and [code and recorded-result guide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/Code_and_Record_Guide.html).
- **Hands-on workshop:** [Classroom Labs instructor guide](agentic_grid_workflow_tutorial/Workshop_Instructor_Guide.md).

The guides include timings, explanations, exercise answers, complete references and figure credits. The current source and code guides are also available on the tutorial site. Download the repository to keep the local notebooks, dashboards and supporting records together.

Keep the studies distinct when teaching. Voltage uses a synthetic SMART-DS feeder; restoration uses a separate six-node transport graph; cyber response uses a separate four-bus DC fixture. Numerical checks, model explanations and human approval are different events. The walkthroughs preserve their actual `REVIEW` or `PENDING` outcomes. These teaching records do not establish live utility deployment, switching authority or a general numerical advantage from adding an LLM. Their engineering supervisors are custom Python; the separate graph lab teaches LangGraph.

## Edit

The two current projects include editable Slidev, LaTeX/TikZ, figures, source registries and notes:

- [Foundations project and rebuild instructions](agentic_operator_tutorial/README.md) · [Slidev source](agentic_operator_tutorial/slidev/slides.md).
- [Operator-cases project and rebuild instructions](agentic_operator_cases_tutorial/README.md) · [Slidev source](agentic_operator_cases_tutorial/slidev/slides.md).

For local Slidev authoring, use Node.js 24 and pnpm 11.25.0. Enter either project's `slidev` folder, run `pnpm install --frozen-lockfile`, then `pnpm dev`. The LaTeX entry point is `latex/main.tex` in each project. Follow each project guide when regenerating content or figures; some original screenshot and graphics helpers need local runtime paths adjusted. Ready figures and PDFs are included.

The [online-site build guide](web/README.md) explains the shared Pages build. The [deployment workflow](.github/workflows/deploy-pages.yml) republishes the site when its presentation or website sources change on `main`.

## Archive

<details>
<summary>Earlier tutorial editions and publication records</summary>

Earlier work remains available for reproduction and comparison:

- [Original three-hour tutorial](agentic_grid_tutorial_3h/README.md).
- [MPC and deep reinforcement learning tutorial](agentic_grid_tutorial_mpc_drl/README.md).
- [Greensboro multi-agent tutorial](smartgridcomm_greensboro/README.md) and [recorded Llama edition](smartgridcomm_greensboro_llama_v2/README.md).
- [Earlier operator-workflow package](Grid_Operator_Workflow_Tutorial/agentic_grid_workflow_tutorial/README.md) and [earlier LaTeX source package](Agentic_Grid_LaTeX_Source/README.md).

Use the two **Watch** links above for the current presentations. Some unchanged notebooks also appear inside presentation evidence folders. [PUBLICATION_MANIFEST.json](PUBLICATION_MANIFEST.json) records copied files, source locations and SHA-256 hashes; [PUBLICATION_AUDIT.json](PUBLICATION_AUDIT.json) records the publication checks. Installed dependencies, build caches and duplicate delivery bundles are excluded.

</details>

## Sources and credits

Primary references, paper URLs, original image credits and evidence limits accompany the slides and guides. See [THIRD_PARTY_SOURCES.md](THIRD_PARTY_SOURCES.md) for source and rights information. IEEE sponsorship or endorsement is not claimed. Third-party photographs, figures, logos and source material retain their respective terms; no blanket license is applied to them.
