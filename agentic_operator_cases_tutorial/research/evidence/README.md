# Agentic AI for grid operators: three-hour teaching tutorial

**Native LaTeX teaching edition, 17 October 2026.** The current lecture has **138 integrated teaching frames with no appendix**. It uses editable TikZ diagrams, worked calculations, typed equations, numerical plots and exact notebook excerpts. It contains no AI-generated imagery.

Start with [the LaTeX project guide](latex_teaching/README.md). The teaching sequence explains a concrete operator decision before introducing software terminology, then follows the same problem through the numerical methods and notebook.

- [Beamer lecture with progressive reveals](latex_teaching/main.pdf): 138 logical frames, with additional PDF pages for the reveal steps.
- [Completed-slide handout](latex_teaching/handout.pdf): one completed page per frame.
- [Written study guide](latex_teaching/study_guide.pdf): explanations, worked examples, code, questions, answers and references.
- [Editable main source](latex_teaching/main.tex) and [chapter sources](latex_teaching/chapters).
- [Exact code map](latex_teaching/Slide_Notebook_Map.json): displayed source ranges and hashes.
- [Graph notebook](Graph_Workflow_Lab.ipynb) and [engineering notebook](Classroom_Labs.ipynb).

The route is 40 minutes of foundations and graph practice, 40 minutes of voltage support, a 10-minute break, 25 minutes of restoration, 27 minutes of cyber response, 8 minutes of evaluation, and 30 minutes of control-room deployment and operator review. The older Slidev and `latex_slides` folders remain prior editions; `latex_teaching` is the revised source.

The graph notebook runs real LangGraph on a declared toy formula. The engineering cases retain their custom Python supervisor. Numerical results, archived actual model responses and optional live calls remain separately labeled.

## Run before class

Use Python 3.12 and start Jupyter in this folder. Prepare the graph lesson in its own environment using `requirements_graph_lab.txt`, as explained in its notebook. The numerical environment below remains separate. Prepare the environment before the three-hour session:

```text
python -m venv .venv
# Activate .venv using the command appropriate to your operating system.
python -m pip install -r requirements_linear.txt
python -m jupyter lab Classroom_Labs.ipynb
```

The default engineering path performs fresh Python LinDistFlow3, optimization and estimation calculations, uses saved SAC weights, and displays genuine archived language-model responses. It does **not** retrain policies, download models or call an LLM. All 13 code cells have executed without errors. Requirements describe the established tutorial environment; earlier recorded studies retain their original version metadata.

In L0, `RUN_OPENDSS=True` enables fresh full-feeder auditing and separate AC MPC replanning in L5. Run OpenDSS studies sequentially because its engine state is shared. `RUN_LOCAL_LLAMA=True` enables one local Ollama call in L11; prepare `llama3.1:8b` in the existing local Ollama service before class. The optional paths were also exercised separately. If unavailable, use the saved outputs and keep execution modes visible.

## What the tutorial demonstrates

- Five explicit responsibilities: Awareness, Planning, Simulation, Verification and LLM Optimizer, followed by human review. A role need not be a separate language model.
- Model-based MPC and model-free SAC produce numerical proposals. Simulation evaluates their consequences; deterministic checks retain or reject them.
- Typed requests and evidence binding expose wrong or stale handoffs. A hash binds content; it is not authentication or proof that measurements are true.
- A learned contextual-bandit selector chooses among already generated canonical operations. It does not train Llama or choose which LLM to call. Its held-out voltage results tie majority voting.
- Restoration and cyber use appropriate standard numerical formulations. Priority weighting and protected measurements explain their respective numerical benefits; those effects must not be attributed to language alone.
- Operator packets expose scope, failed checks and readback identity. No tutorial action operates physical equipment.

Voltage uses one **synthetic SMART-DS Greensboro-area feeder**, not the whole city or a verified utility circuit. The classroom restoration MILP uses a separate six-node transport graph; the optional recorded feeder restoration uses its declared synthetic switching overlay. Cyber uses a separate four-bus DC fixture. LinDistFlow3 and OpenDSS have different constraint coverage in this implementation.

## Scientific evidence and further study

The [research guide](appendix/Agentic_AI_Research_2026.md) reviews primary sources through **17 October 2026**, including PowerAgent/PowerMCP, PowerDAG, Grid-Agent v3, X-GridAgent, PFAgent, CONDUCTOR, PowerAgentBench-SS, skill-based power-system agents, agent scaling and governance-aware control-room workflows. Sources appear at slide bottoms. Preprints, engineering guidance and reproduced tutorial results are labeled separately.

The new exercises are **not** a new aggregate test of agent superiority. The original 168-call voltage pilot is preserved: learned selection ties voting; a posthoc fixed Q rule matches the selected behavior; model coverage changes the acceptance outcome. The fresh optional Llama validation on 17 October is a separate call with its own response and latency record.

| Deeper resource | Purpose |
|---|---|
| [Instructor guide](Workshop_Instructor_Guide.md) | Schedule, questions, expected observations and fallback plan |
| [Exact slide map](latex_slides/Slide_Notebook_Map.md) | Cell IDs, source hashes, excerpt ranges, logical and PDF pages |
| [Speaker notes](latex_slides/Instructor_Notes.md) | A teaching note for every frame |
| [Original methods](Workshop_Step_by_Step.ipynb) / [OpenDSS companion](Workshop_OpenDSS_Executed.ipynb) | Detailed model and controller lessons |
| [Five-stage reference](Proposal_Complete_Workflow.ipynb) | Separately recorded all-stage voltage/restoration/cyber runs |
| [Response selector study](LLM_Response_Selection.ipynb) | Frozen training/test protocol, actual responses, baselines and timings |
| [SAC training](Continuous_SAC_Training.ipynb) | Surrogate fit, learning and fresh engineering evaluation |
| [Existing operator dashboard](Proposal_Operator_Dashboard.html) | Historical P-study interactive readback, separate from new classroom packets |

Keep these experiment families distinct. The full package retains their sources, inputs and recorded evidence for audit.
