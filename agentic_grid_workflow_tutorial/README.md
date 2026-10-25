# Current workshop notebooks and code

**Start here:** [Open Classroom Labs in Colab](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb).

One notebook covers voltage support, restoration and cyber response. Run setup and L0-L12 in order, including L10B. Keep the two advanced switches False. [Setup and troubleshooting](../COLAB_GUIDE.md).

## Current notebooks

- `Classroom_Labs.ipynb`: the required hands-on notebook.
- `Graph_Workflow_Lab.ipynb`: a companion for LangGraph state, routing and simulated review.
- `Agent_Trace_and_Latency.ipynb`: a companion for recorded replies, provenance and timings.

[View the slides](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/1) · [Download the participant pack](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/downloads/GridGuard-Participant-Labs.zip).

## What the code runs

Python calculates fresh numerical results. A saved SAC actor generates a proposal, and deterministic numerical checks evaluate it. Saved Llama records are displayed separately. The main cases use custom Python coordination; the graph companion executes a deterministic toy workflow in real LangGraph. No standard activity calls a new model or operates equipment.

`src/` contains the helpers. `data/` contains the declared synthetic fixtures. `models/` contains saved weights. `results/` contains historical evidence. You do not need to edit those supporting folders during the workshop.

## Run locally

Start Jupyter in this folder after installing the scientific requirements:

```text
python -m pip install -r requirements_colab.txt
python -m pip install jupyterlab
python -m jupyter lab Classroom_Labs.ipynb
```

For the graph companion, also install `requirements_colab_graph.txt`. Use a virtual environment appropriate to your operating system.

## Model scope

Voltage uses a synthetic feeder's MV LinDistFlow3 model. Restoration uses a six-node active-power graph. Cyber uses a four-bus DC fixture. A PASS covers only its declared inputs, limits and model. L10B's dated saved studies are separate from parameter edits in the fresh labs. Advanced OpenDSS and live-Llama branches require separately prepared software and files.

<details>
<summary>Earlier experiments</summary>

Other notebooks and lecture editions remain for reproducibility. Their model scopes, dependency versions and recorded results may differ. Use the three current notebooks above for this workshop. See the [notebook index](../NOTEBOOK_INDEX.md) for deeper studies.

</details>
