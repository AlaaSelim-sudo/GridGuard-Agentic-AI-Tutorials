# Hands-on: three operator cases

[Open the presentation](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/1) · [Download slides](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/downloads/operator-cases.pdf) · [Participant guide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/downloads/participant-lab-guide.pdf)

**Alaa Selim, MIT/Dartmouth · Mohamed Chehada, UT Austin**

## Start with one notebook

[Open Classroom Labs in Colab](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb).

Save a copy, connect a CPU runtime, run setup and continue from L0 in order. Keep `RUN_OPENDSS` and `RUN_LOCAL_LLAMA` False. [Setup help](../COLAB_GUIDE.md).

## Three problems an operator can recognize

- [Solar settings](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/14): compare options, check voltage and current, and return a proposal for review.
- [Power after a fault](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/35): keep the operator’s priorities while testing restoration options.
- [Suspicious readings](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/48): check the evidence and identify what is needed before proposing a correction.

Each case follows the same story: **problem → agent request → tool result → operator decision**. The agent coordinates requests; numerical tools calculate; the operator reviews the next step.

First run the numerical tools in Colab. Then use L10B to replay actual saved Llama choices and tool results. The replay uses separate saved studies and makes no new model call.

[The multi-agent framework on slide 68](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/68) shows how the five roles work together across the recorded cases. One Llama model handles planning and refinement. Python reads the case, calculates results and checks the limits. The operator reviews the recommendation.

Each exercise has its questions first and a worked answer on the following slide: 22 → 23 for voltage, 40 → 41 for restoration, and 54 → 55 for cyber response. Predict and run before advancing to the answer. The 69-slide workshop remains 90 minutes.

[Full references and figure credits](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/Full_Reading_Guide.html) include the original Stanford CS224V material and the power-system sources.

<details>
<summary>Source and build information</summary>

The slide source is `slidev/slides.md`; authored content is in `content/`. Numerical excerpts come from the canonical Classroom Labs notebook. See [BUILD_GUIDE.md](BUILD_GUIDE.md) for source locations and rebuild commands.

The [presenter script](Presenter_Script.pdf) includes a 90-minute schedule, exact Colab run cues and the three agent-role maps. Its editable source is [LaTeX](latex/presenter_script.tex). The same cues appear in Slidev presenter notes.

</details>

The cases are synthetic or reduced-model studies. Simulated readback operates no equipment.
