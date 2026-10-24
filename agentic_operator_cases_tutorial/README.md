# Hands-on workshop: three operator cases

**80 slides / 180 teaching minutes / one required notebook / three four-minute exercises.**

**Presenters:** Alaa Selim, MIT/Dartmouth; Mohamed Chehada, UT Austin.

[Attend](#attend-the-workshop) · [Present](#present-the-workshop) · [Session route](#session-route) · [Edit and rebuild](#edit-and-rebuild) · [Stanford sources](#stanford-teaching-materials)

<a id="before-starting"></a>

## Attend the workshop

1. [Open the slides](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/1) and [Classroom Labs in Colab](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb). Save a notebook copy in Drive.
2. Follow the twelve-minute Stanford introduction. Prepare Colab when the slides reach setup: connect a CPU, run the first cell to **Ready**, then run **L0** and **L1**.
3. Run each named lesson when prompted. Keep `RUN_OPENDSS=False` and `RUN_LOCAL_LLAMA=False` for the standard route. Each case asks you to change one input, rerun, compare and explain.

Only **Classroom_Labs.ipynb** is required. The graph and trace notebooks are companion resources. No GPU, API key, new policy training or model download is needed for the standard route.

Keep the [Participant Lab Guide](Participant_Lab_Guide.pdf) beside the notebook, or use its [web version](Participant_Lab_Guide.html). [Detailed Colab setup and troubleshooting](../COLAB_GUIDE.md).

<a id="teaching-and-sources"></a>

## Present the workshop

1. Open [presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/1).
2. Use the **[presenter script online](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/Presenter_Script.html)**, its **[PDF](Presenter_Script.pdf)** or the **[editable Markdown](Presenter_Script.md)**. Every slide has a short spoken explanation, timing and delivery action. Notebook excerpts include stable cell IDs.
3. Share the [participant guide](Participant_Lab_Guide.pdf) and [three exercise prompts](Exercises.html). Give each exercise four minutes, then reset its changed input.
4. Keep the [Instructor Guide](Instructor_Guide.md) for detailed prompts and answers, the [code-and-record guide](Code_and_Record_Guide.html) for exact excerpts, and the [Teaching and Source Guide](Teaching_and_Source_Guide.pdf) for complete references.

Teaching time includes demonstrations and discussion. Add breaks outside the 180-minute schedule. The script uses the same slide titles and order as the published presentation.

<a id="follow-the-notebook"></a>

## Session route

- **Slides 1–15 / 19 minutes:** Stanford concepts connected to the three cases in twelve minutes, then seven minutes of Colab setup and L0–L1.
- **Slides 16–37 / 49 minutes / voltage L2–L5:** calculate proposals, check limits and scope, then inspect separate saved model choices. Exercise on **slide 25:** change `RATING_FRACTION` to `0.75`; reset afterward.
- **Slides 38–53 / 35.5 minutes / restoration L6–L7:** compare service goals and check changed-request evidence. Exercise on **slide 44:** append `180.` to the capacity list, keeping `40.` first; reset afterward.
- **Slides 54–69 / 35 minutes / cyber L8–L9:** compare model fit with teaching truth, then inspect a separate fixed recovery case. Exercise on **slide 59:** add `.10` to the scale list; reset afterward.
- **Slides 70–80 / 41.5 minutes:** run L10 and L10B, leave L11 at False, then run L12’s simulated readback. Finish with a proposed advisory control-room pilot and an exit ticket.

In L10B, use `SCENARIO="voltage"`, then `"restoration"`, then `"cyber"`, rerunning each time. It displays saved replies and results. Earlier preview slides do not change the required notebook order.

## Edit and rebuild

The [build guide](BUILD_GUIDE.md) covers setup, source locations and each command. From the repository root:

```text
python scripts/build-workshop.py check
python scripts/build-workshop.py all
```

`check` validates the eighty presenter cues, timing, three exercises, visuals and thirteen exact notebook excerpts. `all` rebuilds the handouts, LaTeX PDFs and complete tutorial site. Install the documented authoring dependencies first.

Edit these source files:

- `content/opening.json`, `voltage.json`, `restoration.json`, `cyber.json`, `closing.json`: slide content and timing.
- `content/presenter_script.json`: spoken cues and delivery actions, matched by slide title.
- `slidev/slides.md`: generated Slidev presentation; use the content files for lasting edits.
- `latex/`: generated LaTeX plus compiled slides and guide.
- `diagrams/` and `images/`: supplied figures and editable TikZ sources.
- `research/`: source records, figure provenance and executed evidence.

The IEEE ComSoc theme matches the foundations tutorial. The rebuild helper targets this hands-on project; the site command also assembles the existing foundations deck.

## Stanford teaching materials

The figures come from **Monica Lam. _CS224V Agentic AI, Lecture 1: Introduction._ Stanford University, Fall 2026.** [Read the complete lecture](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf).

- **Slide 3 / lecture p.2:** function calling and agentic workflows introduce the model’s permitted tool choices.
- **Slides 4–5 / lecture p.19:** WikiChat’s evidence-checking idea connects to the L2 voltage/current check.
- **Slides 6–7 / lecture p.40:** Genie Worksheets’ explicit task rules connect to the L6 restoration goal.
- **Slides 8–9 / lecture p.53:** language and decision checks connect to the L8–L9 fit, trust and recovery examples.
- **Slide 10 / lecture pp.52–53:** four review questions tie together all three cases.

Read the underlying papers:

- Sina Semnani, Violet Yao, Heidi Zhang and Monica Lam. **WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia.** _Findings of EMNLP 2023_, pp.2387–2413, December 2023. [Paper and full citation](https://aclanthology.org/2023.findings-emnlp.157/) · [PDF](https://aclanthology.org/2023.findings-emnlp.157.pdf).
- Harshit Joshi, Shicheng Liu, James Chen, Larsen Weigle and Monica Lam. **Controllable and Reliable Knowledge-Intensive Task-Oriented Conversational Agents with Declarative Genie Worksheets.** _Proceedings of ACL 2025, Volume 1: Long Papers_, pp.27264–27308, July 2025. [Paper and full citation](https://aclanthology.org/2025.acl-long.1323/) · [PDF](https://aclanthology.org/2025.acl-long.1323.pdf).

The notebook runs our Python tools. It does not run WikiChat, Genie Worksheets or a theorem prover. Their source examples explain design ideas; they are not grid performance or deployment results.

<a id="keep-the-experiments-distinct"></a>

## Evidence and scope

<details>
<summary>Fresh calculations, recorded model choices and model coverage</summary>

L2 edits do not carry into L3–L5's archived `test_01` case. L5 checks that case's original MV-MPC plan, not L4's selected reactive-power relaxation trial. L8 edits change the sweep, while L9 uses a fixed trusted-recovery case. L10 displays a different old five-stage study; it does not reproduce a student's current edits. L12 returns to L4's selected voltage trial.

L10B displays saved `llama3.1:8b` replies, exact public reasons and saved numerical traces. It makes no new model call or electrical solve. Its voltage replay is an archived OpenDSS recovery study, separate from `test_01`. Its restoration replay uses a feeder bypass catalog, separate from L6. Its cyber replay assumes trusted channels. The wrong language ranking is caught by a numerical guard; a fluent reason does not prove that limits pass. Fixed comparison methods return the same numerical outcomes, so these traces do not establish a numerical benefit from adding Llama.

Fresh numerical checks, saved-controller proposals, archived actual model replies and simulated acknowledgments are separately labeled. The engineering supervisor is custom Python; the separate graph notebook demonstrates LangGraph. The default CPU route needs no GPU, API key or language-model download. No exercise operates equipment. The closing advisory pilot is proposed teaching practice, not an existing utility deployment.

Voltage uses one synthetic SMART-DS feeder and the default MV model. Restoration uses a six-node active-power graph. Cyber uses a four-bus DC fixture with assumed trusted channels. A failed binding means the old evidence is stale; it does not prove the changed case infeasible.


</details>

Independent educational adaptation. IEEE sponsorship or endorsement is not claimed. Original artwork and literature retain their credits.
