# Agentic AI for power-system operators

Learn the concepts and follow three operator cases before trying the optional notebooks.

**Alaa Selim, MIT/Dartmouth · Mohamed Chehada, UT Austin**

**[Open the tutorial website](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/)**

## 1. View the presentations

- **[Foundations](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/foundations/#/1)**: agents, tools, utility examples and power-system research. [Slides PDF](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/downloads/foundations.pdf).
- **[Operator case tutorial](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/1)**: understand the voltage, restoration and cyber cases through prepared results and what-if discussions. No software is needed for the slides. [Slides PDF](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/downloads/operator-cases.pdf).

Use the arrow keys to move through the slides. Source credits accompany each presentation.

## 2. Optional practice after the case tutorial

**One notebook covers all three hands-on cases.**

[![Open Classroom Labs in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

1. Save a copy in Google Drive and connect a **CPU** runtime.
2. Run **Set up Google Colab**, wait for **Ready**, then start at **L0**.
3. Continue through **L12**, including **L10B**. Keep `RUN_OPENDSS` and `RUN_LOCAL_LLAMA` set to `False`.

No GPU, API key or language-model download is needed for the standard lab. Setup requires internet access.

## 3. Work through the cases

- **Voltage · L2-L5:** compare a plan and a saved learned controller. Change the current allowance and recheck the result.
- **Restoration · L6-L7:** compare total and critical load served as tie capacity changes.
- **Cyber · L8-L9:** compare an isolated error and a coordinated attack, then inspect trusted replacement measurements.
- **Agent choices · L10-L10B:** inspect saved Llama replies, tool results and next steps.

Run L0-L1 first. Change one exercise input at a time and reset it before continuing. [Setup and troubleshooting](COLAB_GUIDE.md).

## Downloads and references

- **[Participant pack](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/downloads/GridGuard-Participant-Labs.zip)**: the main notebook, two companion labs and their supporting code/data.
- **[Participant lab guide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/downloads/participant-lab-guide.pdf)**: illustrated setup and exercise instructions.
- **[Foundations references](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/foundations/Full_Reading_Guide.html)** and **[hands-on references](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/Full_Reading_Guide.html)**: full papers, documentation and figure credits.

## Explore further

The concept tutorial stands on its own. Classroom Labs and these companions are separate practice activities:

- [LangGraph workflow lab in Colab](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Graph_Workflow_Lab.ipynb): state, branching, retries and simulated review.
- [Agent traces and latency in Colab](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Agent_Trace_and_Latency.ipynb): recorded replies, evidence and timings.

## Read results in context

The cases use synthetic or reduced networks. Python computes fresh numerical results; saved model replies are labeled separately. L10B makes no new model call or electrical solve. Results apply to the stated model and assumptions. No lab operates equipment.

<details>
<summary>Source projects and earlier editions</summary>

- [Current code and notebooks](agentic_grid_workflow_tutorial/README.md).
- [Foundations source project](agentic_operator_tutorial/README.md).
- [Hands-on source project](agentic_operator_cases_tutorial/README.md).
- [Complete notebook index](NOTEBOOK_INDEX.md).

Earlier editions remain in their original folders for reproducibility. Start with the current presentations and Classroom Labs above.

</details>


