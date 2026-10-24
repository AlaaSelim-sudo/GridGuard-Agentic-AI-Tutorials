# Run GridGuard in Google Colab

Start with **Classroom Labs** to run all three cases in one notebook. The two companion notebooks explain graph execution and the recorded model evidence.

## 1. Open a notebook

**Three cases: Classroom Labs**

[![Open in Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**Companion: LangGraph workflow lab**

[![Open in Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Graph_Workflow_Lab.ipynb)

**Companion: Agent traces and latency**

[![Open in Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Agent_Trace_and_Latency.ipynb)

## 2. Connect and run

1. Sign in to Google. Choose **File → Save a copy in Drive** if you want to keep your changes.
2. Connect to a **CPU** runtime. A GPU and paid Colab plan are unnecessary for these default exercises.
3. Choose **Runtime → Run all**. If Colab asks whether to run this GitHub notebook, review it and continue. The first setup cell downloads the needed public files, installs packages and opens the correct working folder. Wait for its **Ready** message.
4. Work through the cells from top to bottom. Read each prediction before revealing its answer, then change a parameter and rerun the relevant cells. Opening each companion notebook in its own Colab tab gives it a separate session.

Setup needs internet access. The default lessons require no API key, Ollama, OpenDSS, new policy training or model download. Leave `RUN_OPENDSS = False` and `RUN_LOCAL_LLAMA = False` in Classroom Labs for this route. The existing local installation sections in the notebooks apply to local Jupyter, so skip those sections when using Colab.

## 3. Work through the three cases

Run **L0–L1 first** to initialize the helpers and learn why a changed request needs new evidence. Continue in order; later cells use earlier results.

- **Voltage support · L2–L5.** Compare an MPC proposal with a saved SAC policy, inspect archived model choices, and check the selected action numerically. Try `LOAD_SCALE = 1.05` in L2. Rerun that cell and compare feasibility before cost. A changed fresh case does not change the original context of an archived model reply.
- **Service restoration · L6–L7.** Compare priority-weighted service with maximum total kW on a six-node graph. Add `180.` to `CAPACITIES_KW` in L6 and rerun L6–L7. Explain which loads are served and why stale evidence is rejected after the capacity changes.
- **Cyber response · L8–L9.** Compare an isolated measurement error with a coordinated false-data attack on a four-bus DC network. Add `2.` to `ATTACK_SCALES` in L8 and rerun L8–L9. Explain why a small residual can accompany a wrong state, and why missing trusted channels require HOLD.

Finish **L10–L12** to inspect the five recorded stages, compare timing boundaries and try a simulated operator readback. The notebook labels fresh calculations, saved policy inference and archived actual LLM responses separately. No cell dispatches equipment. A simulated acknowledgment in the exercise does not complete a historical operator review.

## Keep your work

Use **File → Save** in your Drive copy, or **File → Download → Download .ipynb** to keep your edited notebook and outputs. Runtime files and in-memory graph checkpoints disappear when a session is reset; rerun setup and then the lesson cells in order in a new session. The public source files on GitHub are unchanged by your session.

## If a cell stops

- **Missing `src` or data:** run the first setup cell, then start the lesson again from L0, G0 or T1. Setup selects the working folder as well as retrieving files.
- **Installation interrupted:** reconnect and rerun setup. If Colab asks for a session restart after a package change, restart, rerun setup, then run all cells again.
- **A graph pause is waiting:** follow G5's supplied resume step. This is the exercise's simulated human review.
- **Colab has changed its runtime:** try **Runtime → Change runtime type → Runtime Version → 2026.07**, if still offered. Google lists this as a Python 3.12 runtime. Otherwise use the [local setup guide](agentic_grid_workflow_tutorial/README.md).

Google's documentation: [Using Colab with GitHub](https://github.com/googlecolab/colabtools/blob/main/notebooks/colab-github-demo.ipynb), [Colab FAQ](https://research.google.com/colaboratory/faq.html), and [runtime versions](https://research.google.com/colaboratory/runtime-version-faq.html).

The three current notebooks have new setup cells. Their existing experiment cells, recorded outputs and archived evidence snapshots are preserved. Colab setup uses compatible scientific-package ranges and pins the graph lesson's runtime packages; the original local requirement files still describe the historical environments.
