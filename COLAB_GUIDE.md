# Run GridGuard in Google Colab

Start with **Classroom Labs** to run all three cases in one notebook. The accompanying operator workshop has **86 slides, 180 minutes and three short exercises**. It introduces the terms in plain language, then connects each request to its calculation, checks and next decision. The two companion notebooks explain graph execution and recorded model evidence.

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
3. For a complete run, choose **Runtime → Run all**. For the paced workshop, run setup first and then each named lesson cell when prompted. If Colab asks whether to run this GitHub notebook, review it and continue. Setup downloads the needed public files, installs packages and opens the correct working folder. Wait for **Ready**.
4. Work from top to bottom using the **L labels**, including **L10B between L10 and L11**. Read each prediction before revealing its answer, then change one parameter and rerun the matching cells. Each companion notebook has a separate session when opened in its own Colab tab.

Setup needs internet access. The default lessons require no API key, Ollama, OpenDSS, new policy training or language-model download. Leave `RUN_OPENDSS = False` and `RUN_LOCAL_LLAMA = False` in Classroom Labs for this route. The existing local installation sections in the notebooks apply to local Jupyter, so skip those sections when using Colab.

## 3. Work through the three cases

Run **L0–L1 first** to initialize the helpers and learn why a changed request needs new evidence. Continue in order; later cells use earlier results.

- **Voltage support · L2–L5.** Compare a forecast-based plan (MPC) with a saved learned controller (SAC). In the exercise, change only `RATING_FRACTION` from `0.80` to `0.75` in L2. Check the limits before comparing penalty score J. Reset L2 afterward. L3–L5 use the separate original `test_01` case: old model choices and new numerical checks, not replies to your edit.
- **Service restoration · L6–L7.** Compare a priority service goal with serving the most total kW on a six-node graph. Add `180.` to `CAPACITIES_KW` in L6, keeping `40.` first, then rerun L6. Compare total and critical load served. Reset the list and rerun L6 before L7, which rejects old evidence after a request changes.
- **Cyber response · L8–L9.** Compare one biased reading with a coordinated false-data shift on a four-bus DC model. Add `.10` to `ATTACK_SCALES` in L8 and rerun. Compare the alarm with error against the known teaching truth. Reset L8 before L9. L9 uses a fixed recovery case, not your changed scale; without the assumed trusted replacement readings it returns HOLD.

## 4. Replay saved Llama choices in L10B

After L10's separate recorded five-stage study, run **L10B** with `SCENARIO = "voltage"`. Follow the supplied inputs, allowed tool choice, exact public Llama reason, returned numerical result and next step. Change the same line to `"restoration"` and then `"cyber"`, rerunning L10B each time.

These are actual saved `llama3.1:8b` replies and saved tool results. **L10B makes no new model call or electrical solve.** Its voltage case is an archived OpenDSS recovery study, not L3's `test_01`. Its restoration case uses a feeder bypass catalog, not L6's six-node optimizer. The restoration numerical guard catches a wrong ranking in the model's final language order. Its cyber case assumes trusted channels; the model does not authenticate them. A public reason is an explanation, not hidden reasoning or proof that an action passes its limits. Fixed comparison methods return the same numerical outcomes, so this replay does not show a numerical advantage from adding Llama.

Continue to **L11** with `RUN_LOCAL_LLAMA=False`; the optional new model call is skipped. Finish **L12** for a simulated operator readback of L4's selected voltage trial. The closing slides then walk through a **proposed advisory control-room pilot**, from a read-only request to checks, human review and a decision log. This is a teaching proposal, not a claim of utility deployment.

The notebook labels new calculations, saved-policy proposals, old model replies and simulated acknowledgments separately. No cell dispatches equipment. A simulated acknowledgment does not complete a historical operator review.

## Keep your work

Use **File → Save** in your Drive copy, or **File → Download → Download .ipynb** to keep your edited notebook and outputs. Runtime files and in-memory graph checkpoints disappear when a session is reset; rerun setup and then the lesson cells in order in a new session. The public source files on GitHub are unchanged by your session.

## If a cell stops

- **Missing `src` or data:** run the first setup cell, then start the lesson again from L0, G0 or T1. Setup selects the working folder as well as retrieving files.
- **Installation interrupted:** reconnect and rerun setup. If Colab asks for a session restart after a package change, restart, rerun setup, then run all cells again.
- **A graph pause is waiting:** follow G5's supplied resume step. This is the exercise's simulated human review.
- **Colab has changed its runtime:** try **Runtime → Change runtime type → Runtime Version → 2026.07**, if still offered. Google lists this as a Python 3.12 runtime. Otherwise use the [local setup guide](agentic_grid_workflow_tutorial/README.md).

Google's documentation: [Using Colab with GitHub](https://github.com/googlecolab/colabtools/blob/main/notebooks/colab-github-demo.ipynb), [Colab FAQ](https://research.google.com/colaboratory/faq.html), and [runtime versions](https://research.google.com/colaboratory/runtime-version-faq.html).

The three current notebooks include Colab setup cells. Classroom Labs also includes L10B's replay of preserved source records. Earlier experiment records remain separate. Colab setup uses compatible scientific-package ranges and pins the graph lesson's runtime packages; the original local requirement files still describe the historical environments.

## Participant handout

Use the [six-page Participant Lab Guide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/downloads/participant-lab-guide.pdf) for an illustrated explanation of Colab, exact exercise edits and the L10B replay tasks. The workshop uses one required notebook, Classroom Labs. The current notebook introduction follows the 180-minute route.
