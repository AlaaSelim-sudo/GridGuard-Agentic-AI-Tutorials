# Hands-on workshop: three operator cases

**80 slides / 180 minutes / three four-minute exercises.** Keep **Classroom_Labs.ipynb** open beside this second presentation. Start with a five-minute visual explanation of the agentic loop: goal, model-selected tool, returned result and next choice. A recorded voltage example shows a failed current check leading to a fallback. Then run the three cases and connect each one to exact saved Llama choices. Follow **L0–L12, including L10B after L10**, using notebook excerpts, executed outputs, parameter edits and separate debriefs. Finish with a proposed advisory control-room pilot.

[Open the workshop slides](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/1) · [Open Classroom Labs in Colab](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb) · [Download the slides](Three_Operator_Cases.pdf)

**Presenters:** Alaa Selim, MIT/Dartmouth; Mohamed Chehada, UT Austin.

[Participant Lab Guide · PDF](Participant_Lab_Guide.pdf) · [web version](Participant_Lab_Guide.html). This short guide explains Colab, the three exercises and the Llama replay. The opening now includes original Stanford material on function calling and agentic workflows. Four lecture excerpts and the grid teaching adaptations have full source credits and page links.

## Before starting

1. Open Classroom Labs and save a copy in Drive.
2. Connect a CPU runtime. Run the first setup cell and wait for **Ready**.
3. Run **L0**, keeping `RUN_OPENDSS=False` and `RUN_LOCAL_LLAMA=False`, then run **L1**.
4. During the workshop, run each named cell when prompted. Use the L headings and stable cell IDs; displayed cell numbers can change.

The default route needs no GPU, API key, new policy training or language-model download. [Colab instructions](../COLAB_GUIDE.md) and [local Jupyter instructions](../agentic_grid_workflow_tutorial/README.md) are provided.

## Follow the notebook

- **Introduction and setup · L0–L1 · 12 minutes.** See the agentic loop, compare a text reply with model-directed tool use, and separate Llama’s choice from a numerical check and human review. Open the one notebook and test whether evidence still matches.
- **Voltage · L2–L5.** Run L2, check limits before penalty score J, change `RATING_FRACTION` to `0.75`, then reset. L3–L5 inspect and check the separate original `test_01` case. The separate recorded P3 previews show Llama requesting a check, choosing a fallback and returning evidence for review. This is the first four-minute exercise.
- **Restoration · L6–L7.** Run L6, append `180.` to the capacity list while keeping `40.` first, and compare total and critical load served. Reset and rerun L6, then run L7 to reject old evidence after a request changes. This is the second exercise. Recorded feeder-study previews then show a useful tool trial, a failed trial and a wrong ranking caught by the numerical guard.
- **Cyber · L8–L9.** Run L8, add `.10` to the scale list, and compare fit mismatch with error against known teaching truth. Reset L8, then run L9's separate fixed recovery case and compare HOLD with PROPOSE under its trust assumption. This is the third exercise. Separate recorded recovery previews show the permitted tool choice and the pending operator review.
- **Replay the agent choices · L10 and L10B.** Earlier case slides preview the saved episodes; now replay them in the notebook. Inspect L10's separate archive. In L10B, set `SCENARIO` to `"voltage"`, `"restoration"` and `"cyber"` in turn. Follow exact saved Llama reasons, actual tool results and checks, including the numerical guard against a wrong restoration ranking.
- **Readback and proposed pilot · L11–L12 and the closing walkthrough.** Leave L11's new model call disabled, run L12's simulated readback and save your notebook. Discuss a proposed read-only advisory pilot with allowed tools, engineering checks, human review and a decision log.

Each case follows **predict → run → read → edit → rerun → explain**. Run the complete cell; the slide often shows only its relevant lines. Answers follow each exercise and appear in the instructor notes.

## Keep the experiments distinct

L2 edits do not carry into L3–L5's archived `test_01` case. L5 checks that case's original MV-MPC plan, not L4's selected reactive-power relaxation trial. L8 edits change the sweep, while L9 uses a fixed trusted-recovery case. L10 displays a different old five-stage study; it does not reproduce a student's current edits. L12 returns to L4's selected voltage trial.

L10B displays saved `llama3.1:8b` replies, exact public reasons and saved numerical traces. It makes no new model call or electrical solve. Its voltage replay is an archived OpenDSS recovery study, separate from `test_01`. Its restoration replay uses a feeder bypass catalog, separate from L6. Its cyber replay assumes trusted channels. The wrong language ranking is caught by a numerical guard; a fluent reason does not prove that limits pass. Fixed comparison methods return the same numerical outcomes, so these traces do not establish a numerical benefit from adding Llama.

Fresh numerical checks, saved-controller proposals, archived actual model replies and simulated acknowledgments are separately labeled. The engineering supervisor is custom Python; the separate graph notebook demonstrates LangGraph. The default CPU route needs no GPU, API key or language-model download. No exercise operates equipment. The closing advisory pilot is proposed teaching practice, not an existing utility deployment.

Voltage uses one synthetic SMART-DS feeder and the default MV model. Restoration uses a six-node active-power graph. Cyber uses a four-bus DC fixture with assumed trusted channels. A failed binding means the old evidence is stale; it does not prove the changed case infeasible.

## Stanford teaching materials

The figures come from **Monica Lam. _CS224V Agentic AI, Lecture 1: Introduction._ Stanford University, Fall 2026.** [Read the complete lecture](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf).

- **Slide 3 / lecture p.2:** the original function-calling and agentic-workflow panels introduce the model’s tool choice.
- **Slide 64 / lecture p.53:** the original clinical-trial diagram separates language from decision checks. Our grid application is a teaching analogy using numerical checks.
- **Slide 70 / lecture p.19:** WikiChat separates retrieval, claim checking and writing.
- **Slide 71 / lecture p.40:** Genie Worksheets motivates explicit task rules. Slide 72 adapts the accountability questions on pp.52–53.

Read the underlying papers:

- Sina Semnani, Violet Yao, Heidi Zhang and Monica Lam. **WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia.** _Findings of EMNLP 2023_, pp.2387–2413, December 2023. [Paper and full citation](https://aclanthology.org/2023.findings-emnlp.157/) · [PDF](https://aclanthology.org/2023.findings-emnlp.157.pdf).
- Harshit Joshi, Shicheng Liu, James Chen, Larsen Weigle and Monica Lam. **Controllable and Reliable Knowledge-Intensive Task-Oriented Conversational Agents with Declarative Genie Worksheets.** _Proceedings of ACL 2025, Volume 1: Long Papers_, pp.27264–27308, July 2025. [Paper and full citation](https://aclanthology.org/2025.acl-long.1323/) · [PDF](https://aclanthology.org/2025.acl-long.1323.pdf).

The notebook runs our Python tools. It does not run WikiChat, Genie Worksheets or a theorem prover. Their source examples explain design ideas; they are not grid performance or deployment results.

## Teaching and sources

- [Slide-to-notebook guide](Code_and_Record_Guide.html): L labels, stable IDs, exact excerpts, source hashes and launch links.
- [Instructor guide](Instructor_Guide.md): timings, prompts, expected outputs and debriefs.
- [Teaching and source guide](Teaching_and_Source_Guide.pdf): complete notes, references, URLs and figure credits.
- [Exercise sheet](Exercises.html): the three parameter-edit tasks.
- [Executed notebook review](research/hands_on/index.html): actual cells and outputs used for the new visuals.
- [Visual provenance](research/hands_on/hands_on_manifest.json): hashes and exact output selections.

These visuals show a clean Python 3.12 execution, not a Google-hosted Colab UI. Slide footers identify the relevant notebook, L label, stable cell or numerical source. Complete references remain in the notes and guide. Historical snapshots in `research/evidence` remain separate.

## Edit and rebuild

Edit the module JSON files in `content/`, then run `python build_cases.py`. Notebook excerpts are read from the canonical sibling notebook by stable cell ID and checked by source hash.

Build the participant guide with `python research/lab_teaching/build_participant_guide.py`.

Compile `latex/main.tex` and `latex/teaching_guide.tex` with LaTeX or Tectonic. Run `python package_cases.py --pdf-only` to refresh downloadable PDFs and the exercise page. Without that flag, packaging also creates portable ZIPs.

For Slidev, use Node.js 24 and the pinned dependencies. The repository's `scripts/build-pages.mjs` builds the public site. Native TikZ diagrams remain editable and have supplied SVG/PDF versions.

The IEEE ComSoc blue/cyan theme matches the foundations tutorial. Independent educational adaptation; IEEE sponsorship or endorsement is not claimed. Original artwork and literature retain their credits.
