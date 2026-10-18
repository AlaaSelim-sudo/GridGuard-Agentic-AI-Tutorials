# Teaching guide — Agentic AI for Grid Operators

Use the animated Slidev deck for the room and [Agentic_Grid_Handout.pdf](Agentic_Grid_Handout.pdf) for individual study. The **128-slide sequence is one complete lesson, with no appendix**. The handout follows it in order and expands the sparse visual slides into explanations, equations, symbol definitions, code excerpts, exercise prompts and references.

The teaching pattern is **predict → reveal → run → explain**. Reveal one relationship at a time, ask for a prediction, then let the numerical result decide what the audience can claim. A role is a responsibility; it need not be a separate LLM. Deterministic methods are essential parts of the workflow.

## Prepare before class

1. Launch the prepared browser deck using [Start_Slides.ps1](Start_Slides.ps1), with Node.js 22 or later. Visit `http://127.0.0.1:3033` and test the projector, click controls and figures. The prebuilt site requires no dependency installation.
2. Prepare two **Python 3.12** environments from the parent tutorial folder. Keep the LangGraph runtime separate from the engineering environment. Run each notebook once before the session.
3. Keep the executed HTML notebooks and the PDF handout available for learners who cannot run a cell. They can still predict, inspect and interpret the recorded outputs.
4. Decide in advance whether to enable the optional OpenDSS audit and local Llama call. Install dependencies and prepare the model outside class.

From the parent tutorial folder, a Windows setup can use:

```powershell
python -m venv .venv-grid
.\.venv-grid\Scripts\python.exe -m pip install -r requirements_linear.txt
.\.venv-grid\Scripts\python.exe -m jupyter lab Classroom_Labs.ipynb
```

In a separate terminal, from that same folder:

```powershell
python -m venv .venv-graph
.\.venv-graph\Scripts\python.exe -m pip install -r requirements_graph_lab.txt
.\.venv-graph\Scripts\python.exe -m jupyter lab --port 8889 Graph_Workflow_Lab.ipynb
```

For full OpenDSS checking, install `requirements.txt` in the engineering environment and set `RUN_OPENDSS=True` in L0. Execute OpenDSS work sequentially; the local engine has shared state. Saved SAC inference uses the supplied weights through NumPy and does not require retraining or the optional training environment.

For L11, prepare the existing Ollama service with `llama3.1:8b` and set `RUN_LOCAL_LLAMA=True` in L0. The default leaves this off. Use the saved actual response if the live call is unavailable or slow. A model download is not a classroom exercise.

## Timing and teaching emphasis

| Minutes | Content and activity | Preserve when time is tight |
|---|---|---|
| 0–40 | Foundations, prior work, graph vocabulary, G0–G5 and L0–L1 | DAG versus cycle; actual repair trace; stale binding |
| 40–82 | Voltage concepts, MPC/SAC, L2–L5, Llama selection and model comparison | Seven-minute L2 lab; fresh trial check; MV/AC scope difference |
| 82–92 | Break | Save work; retain the full break |
| 92–119 | Restoration formulation, eight-minute L6 lab, L7 and recorded five-stage evidence | Critical versus total service; changed-rating rejection |
| 119–149 | WLS, residual cancellation, seven-minute L8 lab and five-minute L9 lab | Detector-visible evidence versus offline truth |
| 149–158 | Evaluation, current research, optional one-minute L11 demonstration and latency | Fair baseline and honest timing boundaries |
| 158–180 | Control-room concept, four-minute L12 lab, capstone and exit ticket | Scoped readback; one supported benefit and one limitation |

Have pairs alternate roles: one operates the notebook and the other audits the interpretation. If the group falls behind, use saved LLM records and demonstrate G5 centrally. Preserve the numerical experiments and capstone; do not turn the break into installation time.

## Hands-on checkpoints and expected observations

| Checkpoint | Learner action | Expected observation or discussion |
|---|---|---|
| G0–G3 | Run the real graph imports, state schema, functions and wiring. | Nodes return updates; the trace reducer appends; routing is explicit. TypedDict alone does not validate values. |
| G4 | Predict three cases, then run unchanged. | Immediate ready, one-repair ready, one-repair HOLD. Direct Python matches all three commands, statuses and traces. |
| G5 | Inspect the pause, then resume with the scripted matching ID. | Before resumption, `report` is pending and acknowledgment is false. Matching readback produces `TOY_ACKNOWLEDGED`. |
| L0–L1 | Run setup and the binding experiment. | Same request/command: true; changed request or command with old evidence: false. The payload is illustrative, not a feeder solve. |
| L2 | Run defaults, change only `LOAD_SCALE`, rerun and explain. | Default MPC cost ≈0.031104; SAC ≈0.436428; both pass the MV gate. Record your own values after changing the scenario. |
| L3–L4 | Inspect archived responses, canonicalize choices and freshly test the frozen selector. | Three replies produce two physical trials. Majority and learner choose the reactive reduction on the original test context. |
| L5 | Inspect the MV audit; optionally run the same-action OpenDSS check and separate AC replanning. | A reduced-model PASS can fail broader-model checks. Replanning with the broader model is a different experiment from auditing the same action. |
| L6 | Sweep tie capacity and add one tighter level. | At 40 kW: weighted 130 total/90 critical kW; unweighted 140 total/30 critical. At 80 and 100 kW, weighted service remains 200 total/90 critical. |
| L7 | Change the rating and revision while retaining the old evidence. | The old binding fails. Recompute and review a result for the new request. |
| L8 | Sweep isolated bias and coordinated corruption. | Coordinated residual stays near 3.92022 while offline state error grows. Threshold is 15.0863; isolated scale-1 residual is ≈277.497. |
| L9 | Compare protected information available versus unavailable. | Unavailable gives HOLD. Under the stated protected-reading assumption, the QP proposes ≈0.12169 p.u.; actual toy flow 1–2 drops from 0.24 to ≈0.17046 p.u. |
| L10 | Inspect all five archived stages for each case. | Observe methods, outputs, public responses, failed checks and durations. These records are not regenerated by changing earlier classroom cells. |
| L11 | Optionally request one local Llama response, or inspect the actual saved call. | The displayed excerpt requests a permitted refinement, followed by new checking. Client time in the saved call was 34.113 s; model loading alone was 16.967 s. |
| L12 | Inspect scope mismatch, wrong ID and matching advisory readback. | Full MV/LV request with MV evidence: HOLD. Wrong ID: REJECTED. Eligible matching readback: acknowledged, with `equipment_dispatch=False`. |

For G4 extensions, use a **new scratch cell** so the supplied assertions continue to describe the original three cases. To make the G5 pause visible during a live demonstration, run its lines 1–17 first, then lines 18–21 in a second cell. The complete cell automatically supplies a simulated response. The in-memory checkpoint does not survive a kernel restart and does not authenticate a person.

L12 depends on the selected-trial context from earlier cells; run the engineering notebook in order. For a quick lecture, run L10 after the cyber experiment and revisit its output during the operator discussion. The exact slide/code correspondence is recorded in [content/notebook_map.json](content/notebook_map.json).

## Keep the scientific boundaries visible

**Graph execution and engineering control are separate experiments.** G0–G5 use an invented scalar response, `i = 0.4 + 0.8u`, with actual LangGraph execution. The numerical classroom workflow uses custom Python orchestration. Do not imply that the engineering studies were migrated into that toy graph.

**Model scope changes the meaning of PASS.** The voltage study uses one synthetic Greensboro feeder. Python LinDistFlow3 covers MV phases with ideal LV aggregation; the supplied OpenDSS model includes MV/LV coverage and transformers. This changes both equations and coverage, so the comparison does not isolate numerical approximation error alone.

**Separate fresh, archived and live evidence.** L2, L6 and L8–L9 compute new numerical results. L3 and L10 inspect actual archived language outputs. L4 freshly checks choices from the original archived context. L11 is optional live generation. Printing saved output is not inference latency.

**Controllers and selectors solve different decisions.** MPC is model-based planning; SAC is the trained continuous-action policy used here. PPO is discussed as an alternative, not another trained result. The contextual bandit selects among already generated canonical operations. It does not choose which LLM to call or retrain the LLMs; all pool selectors pay for all three responses.

**Benefits must survive strong baselines.** The held-out MV learner ties voting, and an identified post-hoc fixed operation matches their choices. The AC experiment does not establish learned superiority. Restoration priorities change the optimization objective; protected cyber readings change the information basis. Neither change is automatically a language-model benefit.

**The smaller cases have declared limits.** The fresh restoration MILP uses a six-node active-power transport fixture; the recorded feeder restoration trace uses a different synthetic catalog. The cyber fixture uses a four-bus DC model. Synthetic truth appears only in offline evaluation. Protected measurements are assumed trustworthy, not authenticated by an LLM. A low WLS residual does not establish that the estimated state is true.

**Human interaction is advisory.** A valid numerical result, a matching evidence record and a matching readback establish different things. The operator exercise neither authenticates a real person nor dispatches equipment. The control-room image is a conceptual AI-generated illustration, not a documented deployment.

## Capstone and exit ticket

Give each group one card and require a decision plus a concrete next step:

- **MV PASS; full-feeder AC FAIL:** request a repair or study at the required scope.
- **Restoration model PASS; isolation record absent:** obtain the authorized isolation evidence; the optimizer cannot supply it.
- **No residual alarm; protected measurements absent:** seek justified independent information or escalate the uncertainty.

End with three short responses: explain one graph concept, identify one exact notebook checkpoint, and state one supported result with its limitation. For a research extension, ask learners to specify the proposed mechanism, a strong fixed baseline, a measurable outcome and a result that would refute the claimed benefit.

## References and adaptation

References appear on the slides and beside the corresponding handout lesson. Framework comparisons describe documented mechanisms, with qualifications; they are not a shared performance leaderboard. PowerDAG's prerequisite supervision has limited rule coverage and a one-shot advisory policy, so it should not be presented as an unconditional safety barrier.

Reused figures and license notices are documented in [content/paper_assets.json](content/paper_assets.json) and [public/assets/papers/ATTRIBUTION.txt](public/assets/papers/ATTRIBUTION.txt). Preserve author credits and license links. Label modifications clearly, and retain CC BY-SA 4.0 for adaptations of the PowerDAG artwork. The new source of the teaching sequence is the Slidev content and components; older LaTeX materials are not part of this lecture route.
