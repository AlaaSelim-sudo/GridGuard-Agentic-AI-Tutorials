# Hands-on workshop: three operator cases

**59 slides / 120 minutes / three four-minute exercises.** Keep **Classroom_Labs.ipynb** open beside this second presentation. Follow the notebook's actual L0-L12 sequence using exact excerpts, real executed outputs, parameter edits and separate debriefs.

[Open the workshop slides](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/1) · [Open Classroom Labs in Colab](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb) · [Download the slides](Three_Operator_Cases.pdf)

## Before starting

1. Open Classroom Labs and save a copy in Drive.
2. Connect a CPU runtime. Run the first setup cell and wait for **Ready**.
3. Run **L0**, keeping `RUN_OPENDSS=False` and `RUN_LOCAL_LLAMA=False`, then run **L1**.
4. During the workshop, run each named cell when prompted. Use the L headings and stable cell IDs; displayed cell numbers can change.

The default route needs no GPU, API key, new policy training or model download. [Colab instructions](../COLAB_GUIDE.md) and [local Jupyter instructions](../agentic_grid_workflow_tutorial/README.md) are provided.

## Follow the notebook

- **Prepare · slides 1-9.** Set up, read the evidence labels and test binding in L1.
- **Voltage · slides 10-26.** Run L2, read feasibility and cost, change `RATING_FRACTION` to `0.75`, then reset. L3-L5 inspect and check the separate original `test_01` context. Preview the L12 operator packet; run it at the end. Exercise: slide 15.
- **Restoration · slides 27-40.** Run L6, append `180.` to the capacity list, inspect total/critical service, then reset. Run L7 to reject stale evidence after a rating change. Exercise: slide 33.
- **Cyber · slides 41-56.** Run L8, add `.10` to the scale list, compare residuals with offline state error, then reset. Run L9's fixed recovery fixture and compare HOLD with PROPOSE under its trust premise. Exercise: slide 46.
- **Finish · slides 57-59.** Inspect L10's separate archive, leave L11's model call disabled, run L12's simulated readback and save your notebook.

Each case follows **predict → run → read → edit → rerun → explain**. Run the complete cell; the slide often shows only its relevant lines. Answers follow each exercise and appear in the instructor notes.

## Keep the experiments distinct

L2 edits do not propagate into L3-L5's archived `test_01` context. L5 checks that context's MV-MPC incumbent. L8 edits change the sweep, while L9 uses a fixed trusted-recovery fixture. L10 displays a different archived five-stage study; it does not reproduce the student's current edits. L12 returns to L4's selected voltage trial.

Fresh numerical checks, saved-policy inference, archived actual model replies and simulated acknowledgments are separately labeled. The engineering supervisor is custom Python; the separate graph notebook demonstrates LangGraph. No exercise operates equipment.

Voltage uses one synthetic SMART-DS feeder and the default MV model. Restoration uses a six-node active-power graph. Cyber uses a four-bus DC fixture with assumed trusted channels. A failed binding means the old evidence is stale; it does not prove the changed case infeasible.

## Teaching and sources

- [Slide-to-notebook guide](Code_and_Record_Guide.html): L labels, stable IDs, exact excerpts, source hashes and launch links.
- [Instructor guide](Instructor_Guide.md): timings, prompts, expected outputs and debriefs.
- [Teaching and source guide](Teaching_and_Source_Guide.pdf): complete notes, references, URLs and figure credits.
- [Exercise sheet](Exercises.html): the three parameter-edit tasks.
- [Executed notebook review](research/hands_on/index.html): actual cells and outputs used for the new visuals.
- [Visual provenance](research/hands_on/hands_on_manifest.json): hashes and exact output selections.

These visuals show a clean Python 3.12 execution, not a Google-hosted Colab UI. Slide footers identify the relevant notebook, L label, stable cell or numerical source. Complete references remain in the notes and guide. Historical snapshots in `research/evidence` remain separate.

## Edit and rebuild

Edit the five module JSON files in `content/`, then run `python build_cases.py`. Notebook excerpts are read from the canonical sibling notebook by stable cell ID and checked by source hash.

Compile `latex/main.tex` and `latex/teaching_guide.tex` with LaTeX or Tectonic. Run `python package_cases.py --pdf-only` to refresh downloadable PDFs and the exercise page. Without that flag, packaging also creates portable ZIPs.

For Slidev, use Node.js 24 and the pinned dependencies. The repository's `scripts/build-pages.mjs` builds the public site. Native TikZ diagrams remain editable and have supplied SVG/PDF versions.

The IEEE ComSoc blue/cyan theme matches the foundations tutorial. Independent educational adaptation; IEEE sponsorship or endorsement is not claimed. Original artwork and literature retain their credits.
