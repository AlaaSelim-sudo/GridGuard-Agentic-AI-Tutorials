# Hands-on: three operator cases

[Open the presentation](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/1) · [Download slides](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/downloads/operator-cases.pdf) · [Participant guide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/downloads/participant-lab-guide.pdf)

**Alaa Selim, MIT/Dartmouth · Mohamed Chehada, UT Austin**

## Start with one notebook

[Open Classroom Labs in Colab](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb).

Save a copy, connect a CPU runtime, run setup and continue from L0 in order. Keep `RUN_OPENDSS` and `RUN_LOCAL_LLAMA` False. [Setup help](../COLAB_GUIDE.md).

## Explore the three cases

- Voltage: compare numerical proposals and inspect their modeled limits.
- Restoration: compare total and critical load served under changing capacity.
- Cyber: compare measurement consistency, estimation error and trust assumptions.

L10B displays actual saved model choices and returned tool evidence. It makes no new model call or electrical solve. The fresh classroom calculations and saved studies use clearly identified models and inputs.

[Slides 74-77](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/74) map the five roles to each recorded case. One Llama model handles planning and refinement. Python reads the case, calculates results and checks the limits. The operator reviews the recommendation.

[Full references and figure credits](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/Full_Reading_Guide.html) include the original Stanford CS224V material and the power-system sources.

<details>
<summary>Source and build information</summary>

The slide source is `slidev/slides.md`; authored content is in `content/`. Numerical excerpts come from the canonical Classroom Labs notebook. See [BUILD_GUIDE.md](BUILD_GUIDE.md) for source locations and rebuild commands.

The [presenter script](Presenter_Script.pdf) includes a 90-minute schedule, exact Colab run cues and the three agent-role maps. Its editable source is [LaTeX](latex/presenter_script.tex). The same cues appear in Slidev presenter notes.

</details>

The cases are synthetic or reduced-model studies. Simulated readback operates no equipment.
