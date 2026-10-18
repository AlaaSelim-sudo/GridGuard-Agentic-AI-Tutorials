# Agentic workflows for distribution-grid operators

**A three-hour, hands-on tutorial using one synthetic Greensboro feeder, local Llama, MPC, a pretrained DRL policy, and OpenDSS.**

A good controller proposes a useful action. An operating workflow must also check the evidence, select an appropriate tool, evaluate the proposal, recover when a step fails, and explain what happened. This tutorial makes those responsibilities visible.

MPC and DRL are numerical tools **inside** the workflow. The agents coordinate their use. A separate engineering verifier evaluates candidates using a fresh OpenDSS solution and explicit operating checks.

## Start here

- **Follow the lesson:** open [Grid_Operator_Workflow.html](Grid_Operator_Workflow.html).
- **Run the experiments:** open [Grid_Operator_Workflow.ipynb](Grid_Operator_Workflow.ipynb).
- **Present the material:** use [Grid_Operator_Workflow.pptx](Grid_Operator_Workflow.pptx).
- **Teach the workshop:** use [Instructor_Guide.md](Instructor_Guide.md).

The HTML version and saved notebook outputs support reading without a running model. They are recorded results, not a new live experiment.

## What you will learn

By the end, you should be able to:

1. Explain the difference between a control tool, a simulation tool, and an agent that coordinates them.
2. Follow one proposed action from measurements to a verified outcome.
3. Use MPC and a pretrained deep Q-network (DQN) to generate voltage-control candidates.
4. Examine two restoration cases and understand why the same switching plan may fail under a different capacity limit.
5. Reject missing or stale evidence, inspect measurement inconsistencies, and treat external text as untrusted input.
6. Compare scripted and agentic workflows without attributing every benefit of a safety check to the language model.
7. Measure whether Llama interprets more operator requests correctly, while checking wrong interpretations, handoffs, and model cost separately.

The lesson uses a repeated pattern: **question → prediction → formulation → experiment → plot → interpretation**. Optional policy retraining and broader comparisons belong in the appendix. This small DQN trains in seconds on the preparation machine; its supplied checkpoint keeps the main lesson focused.

## Before the workshop

You should be comfortable reading short Python cells and recognize voltage, active power, reactive power, and per-unit quantities. Experience with language-model agents is not required. The instructor introduces the optimization and learning notation as it appears.

You need:

- Python 3.12 (the supplied run used 3.12.14) and the packages in `requirements.txt`;
- JupyterLab or another Jupyter notebook interface;
- the included feeder data and pretrained DQN checkpoint;
- Ollama running locally with `llama3.1:8b` for live agent calls.

The live model can take time to load. Install the environment and model before the session. Do not spend the teaching time training a policy or downloading a model.

### Install the Python environment

Run these commands from this tutorial's folder:

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python -m jupyter lab Grid_Operator_Workflow.ipynb
```

On macOS or Linux, replace `.\.venv\Scripts\python` with `.venv/bin/python`.

If you use an existing environment, install the requirements in that environment and select its kernel in Jupyter. The notebook's opening checks identify missing components before the experiments.

### Check the local language model

If the requested model is already installed, it does not need to be downloaded again:

```text
ollama list
```

If it is absent:

```text
ollama pull llama3.1:8b
```

Start the Ollama application or its local service before running the live cells. The default local API is `http://localhost:11434`.

The notebook starts in **live Llama mode**. Its configuration cell also provides an explicit replay option. Use replay for a room without a working local model, and keep the displayed mode visible. Replay displays supplied observations and does not measure the current machine's inference time. A failed live call must be reported as a failed call rather than silently presented as a model response.

### Run the scenario experiments

With the tutorial environment selected:

```text
python -m src.run_labs
```

This reruns the scenario workflow experiments and writes their evidence into `results/`. The notebook is the guided teaching path; the command is useful for regenerating the supporting records.

## The workflow

| Responsibility | What it contributes |
|---|---|
| Awareness | Organize measurements, topology, evidence quality, and the operating request. |
| Planning | Select a numerical tool and its bounded inputs. |
| MPC / DQN / restoration search | Generate an actual candidate using a model, a trained policy, or a bounded search. |
| Simulation | Solve the candidate on the OpenDSS feeder. |
| Verification | Check the evidence, electrical constraints, and applicable operating rules. |
| Repair / supervision | Use rejection feedback to request a new candidate within a finite budget, or stop without an accepted action. |
| Operator explanation | Present the recommendation, measured results, and rejection history. |

Roles share a common schema, so the notebook can show which inputs led to which tool calls and which checks accepted or rejected a candidate. Separate roles do not imply independent evidence sources or independent model errors.

A candidate that has not passed the checks is not an accepted action. Invalid proposals and failed tool calls remain part of the record and consume the bounded attempt budget.

## Three-hour route

| Time | Activity |
|---|---|
| 00:00–00:15 | Setup, learning objectives, and smoke tests |
| 00:15–00:35 | The Greensboro feeder and electrical-model assumptions |
| 00:35–01:05 | Voltage control with MPC and the pretrained DQN |
| 01:05–01:35 | Llama coordination and repair, including a 15-minute request-interpretation value experiment |
| 01:35–01:45 | Break |
| 01:45–02:15 | Restoration with normal and limited alternate-supply capacity |
| 02:15–02:45 | Stale evidence, inconsistent measurements, and untrusted instructions |
| 02:45–03:00 | Read the comparisons, discuss limits, and complete the final exercise |

## What the case represents

The electrical network is one feeder from the **SMART-DS synthetic Greensboro data**, not the complete city and not an operating utility's live network. [SMART-DS provenance](https://data.openei.org/submissions/2981).

For the restoration exercises, alternate bypass lines, critical-load labels, and individually controllable noncritical-load relays are teaching assumptions. They are not documented utility equipment or actual critical-facility classifications. A capacity-limited restoration result therefore demonstrates the supplied decision problem; it is not a field switching plan.

The supplied DQN uses training seed 11. Its checkpoint and training metadata are in `models/`. Training conditions, action choices, and reward assumptions matter when interpreting its behavior. A trained policy is not guaranteed to generalize to a changed topology or operating range.

OpenDSS provides the implemented unbalanced electrical evaluation. A scalar DistFlow equation may be used to explain voltage sensitivity; it is an illustration, not an implemented three-phase LinDistFlow solver. MPC uses the predictive model documented in its controller cell.

## How to read the results scientifically

Keep three conclusions separate:

- **Control performance:** what the MPC, DQN, or restoration tool proposes.
- **Verification performance:** which proposed actions the common checks accept or reject.
- **Coordination performance:** which tools the workflow selects, how it responds to a rejection, and the time and attempts this requires.

The comparison holds the shared engineering tools and checks fixed wherever the experiment specifies. Read each comparison's information and budget settings before interpreting a difference. A scripted workflow may match or outperform an agentic one on a well-defined task.

In the core scenario run, the matched workflows reach the same principal engineering outcomes and the fixed supervisor is faster. That run contains six actual Llama calls, plus a separate notebook setup call. Initial schema and routing development failures are preserved in the appendix; the final context supplies an explicit operator objective and permitted tool descriptions.

The request-interpretation experiment then measures a different benefit. On 20 clear authored pilot requests, Llama once correctly completes 16 versus the parser's 14, but produces four wrong READY interpretations versus zero. Critic and self-review passes reduce correct completions to 9 and 10. A parser-first Llama fallback selected after that pilot is evaluated prospectively on 12 new authored requests: it correctly completes 7/8 clear requests versus 5/8 for the parser, with two wrong READY responses versus one across all 12 cases. It uses six model calls and correctly clarifies 3/4 non-actionable requests versus the parser's 4/4. This is a coverage benefit with errors, not evidence that every extra agent improves the result.

Read the positive q09 trace: Llama converts a restoration paraphrase into the correct restrictions, and the shared numerical tools verify 1,843.61 kW of nominal connected demand. Also inspect confirmation h05: both interfaces lose an intended 20% current reserve, and their recommendation fails the offline check under the intended limit even though it passes the runtime check under the misread limit. An electrical verifier cannot recover an omitted semantic constraint. A field-facing design would need validated operator readback of interpreted restrictions before recommendations are acted on; that process is not implemented here.

The three recovery tests finish 0/3 with one pass and 3/3 with either adaptive rules or the agent; the agent is slower. Full methods, honest denominators, model-call accounting, and recorded tables are in [Agentic_Advantage_Study.md](appendix/Agentic_Advantage_Study.md). The added studies measure neither human workload nor deployment safety.

Useful outcomes include accepted constraint violations, task completion, service restored, curtailment, failed calls, attempt counts, and elapsed time. Explainability is illustrated through inspectable records; reduced operator workload requires a separate human study.

The checks establish only the modeled conditions at the evaluated operating points. They do not certify protection coordination, transient stability, communications security, transformer thermal behavior, or safe operation over every future disturbance. A successful snapshot does not prove a general safety guarantee.

## Files you may want to inspect

| File or folder | Purpose |
|---|---|
| `src/workflow.py` | Evidence schema, agent orchestration, verification, and bounded repair |
| `src/control_tools.py` | MPC, DQN, and restoration-tool interfaces |
| `src/power_tools.py` | Feeder loading and OpenDSS evaluation |
| `src/run_labs.py` | Reproducible scenario experiment entry point |
| `src/request_study.py`, `src/recovery_study.py`, `src/hybrid_study.py` | Authored request pilot, matched repair comparison, and prospective hybrid confirmation |
| `data/` | The included feeder and data provenance |
| `models/` | Pretrained DQN seed-11 checkpoint and training metadata |
| `results/` | Recorded inputs, tool outcomes, and experiment evidence |
| `figures/` | Figures generated for the teaching materials |
| `appendix/` | Supporting material outside the main three-hour route |

Scientific references, exercise solutions, and delivery guidance are in the [instructor guide](Instructor_Guide.md). The [scientific notes](appendix/Scientific_Notes.md) document the implemented objectives, training, reproducibility, and extension exercises. [Data provenance](data/DATA_SOURCE.md) records the feeder extent and artificial overlays. Appendix regression tests use explicit test doubles for failure-path testing; those fixtures are not live-agent or trained-policy experiment evidence.

The teaching sequence was informed by the professional structure of the [EPSR Lab smart-inverter tutorial](https://epsrlab-ub.github.io/SmartInverter-3P-DOPF-POWERUP.jl/dev/tutorial_voltvar/); this tutorial uses its own framework, experiments, and case.
