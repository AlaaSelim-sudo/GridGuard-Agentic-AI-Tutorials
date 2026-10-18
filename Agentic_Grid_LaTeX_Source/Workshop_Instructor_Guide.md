# Instructor guide: a coherent 180-minute teaching session

Begin with `Graph_Workflow_Lab.ipynb`, then use `Classroom_Labs.ipynb` for the engineering cases. Present `latex_slides/Agentic_Grid_Lecture.pdf`. The complete 140-frame resource adds a 68-frame appendix after the 72-frame lecture. Installation, model downloads and training happen before class. Keep the ten-minute break.

Advance the presentation one PDF page at a time. Repeated pages progressively disclose diagram edges, state updates, algebra and results. The same question stays in view while its answer appears. All pages include a short fade transition, which works only in viewers that support PDF transitions. The reveal sequence itself needs only page advance. Use the handout for a single completed diagram per logical frame. The visible Next question supplies the bridge to the following frame.

## Teaching sequence

| Time | Logical frames | Learning task and transition |
|---|---:|---|
| 0–40 | 1–23 | Teach tool/agent/runtime, DAG dependencies, state, routing, bounded feedback, checkpoints and the five stages. Run G0–G4, demonstrate G5, then L0–L1. Explain model-based and model-free methods before voltage. |
| 40–53 | 24–30 | Physical voltage problem, MPC objective and constraints, two model scopes, SAC. |
| 53–63 | 31–32 | L2: predict and perturb demand, rerun MPC and saved-actor inference, compare constraints before cost. |
| 63–76 | 33–36 | L3–L4: critique actual reasons, canonicalize actions, explain voting and contextual-bandit updates, then recheck the selected operation. |
| 76–82 | 37–39 | Null result, broader-model audit and animated all-stage attribution. |
| 82–92 | 40 | Full break. |
| 92–102 | 41–43 | Six-node restoration network, service/energization distinction, MILP and matched feasible-set baseline. |
| 102–119 | 44–48 | L6–L7: capacity sweep, priority tradeoff, stale topology and stage-by-stage evidence. |
| 119–128 | 49–51 | Estimation pipeline, WLS/residual test, derive why an Hc perturbation cancels out of the residual. |
| 128–145 | 52–55 | L8–L9: compare bias and stealth; protected-data QP and consequences using offline truth. |
| 145–149 | 56–57 | Animated cyber stages; distinguish model scope, topology state and information trust. |
| 149–157 | 58–61 | Coordination value, reusable skills, executable authority and matched evaluations. |
| 157–162 | 62–64 | Actual latency, L11 optional local call, separate task/physical/report/human metrics. |
| 162–174 | 65–69 | L12 readback; L10 actual stage traces; decision cards; choose an adequate architecture. |
| 174–180 | 70–72 | Explain all stages, test scientific claims and design one controlled extension. |

Run G0 through G5 in the graph notebook, then L0 through L12 in the engineering notebook. G5 can be an instructor demonstration; its code also runs after class. Use the prepared graph environment and switch to the prepared numerical kernel before L0. L10 prints the archived all-stage records and can run after cyber; revisit its output during operator review. The optional L11 cell can remain disabled. The final L12 packet is the local classroom acknowledgment exercise, not a new deployment of the historical dashboard.

## Questions and expected observations

**G0–G5: What makes the graph executable?** Nodes return partial state updates. The trace reducer appends new entries. A conditional edge chooses review, repair or HOLD. The retry counter bounds the loop. A checkpoint records state under a thread ID; an interrupt returns control to the caller until a matching resume command arrives. The toy example uses rule-driven decisions and a declared current formula. It has no LLM and establishes no feeder feasibility. Ask students to predict the passing, repaired and exhausted paths before running G4. The language/solver nodes in the engineering workflow fill these responsibilities with their actual tools.

**Before the graph code:** distinguish the DAG concept drawing from the implemented feedback graph. A return edge creates a cycle. Parallel branches need a well-defined merge and can conflict if they update the same field. A typed state declaration alone does not validate physical ranges. When showing G5, explain that code before an interrupt can execute again on resume, so external side effects need idempotence. The exercise saves state in memory and does not persist it across process restarts.

**L1: What does a passing hash check prove?** Only identity and consistency of the bound contents. The illustrative payload is not physical evidence. Same request/command passes; changed load or command fails. Try a string-valued load multiplier or unknown backend: typed validation rejects it.

**L2: Is a cheap policy automatically the better control?** Inspect feasibility before objective. The default fresh numerical run gives MPC current-step J about 0.03110 and saved-actor SAC about 0.43643; both pass the MV contract. These values are not a broad benchmark. The actor is freshly evaluated from saved weights, without retraining. Change load or current allowance and explain the response; independently sorted voltage curves compare distributions, not the same bus at each horizontal index.

**L3–L4: What did language contribute?** The archived test_01 pool offers two distinct actions from three model responses. Llama 3.2 and Qwen propose reactive-effort reduction; Llama 3.1 proposes a small active increase. Critique unsupported curtailment/stability statements. Vote and the frozen learner select the same canonical operation; fresh rechecking gives J about 0.031082 on the ORIGINAL archived case. Do not subtract it from a changed L2 case. The training checkpoint has 24 selected-feedback updates; evaluation does not learn.

**L5: Does MV PASS mean full-feeder PASS?** No. Optional fresh checking of the same original MV action gives an AC violation; separately solved AC MPC passes. Both network coverage and model equations differ. The historical 12-case table in the deck is separate from this single-case live audit. A changed action always needs new checking.

**L6: Why not simply maximize all kW?** At the sampled 40-kW tie, priority optimization serves 130 total/90 critical kW; unweighted maximum-kW optimization serves 140 total/30 critical kW. At 80 and 100 kW the priority solution serves 200 total/90 critical. This is the effect of objective weights, not LLM superiority. Both objectives use the identical feasible set; weighted service uses HiGHS plus independent enumeration, unweighted service uses exact enumeration. Selected optimal weighted service is preserved by a secondary edge-count/index tie-break. Edge count is not the number of switching operations from an initial topology.

**L7: What changes when a topology or rating changes?** The request hash changes, so old evidence fails binding. A newly computed result must carry the new identity. The transport fixture does not establish AC feasibility, protection or physical isolation.

**L8: Why can the residual stay small?** The same Hc change shifts the WLS estimate by c, cancelling in the residual. The default stealth residual statistic remains about 3.92022 as state error changes; isolated bias grows above threshold 15.0863. The plot uses a symmetric-log residual scale to keep the threshold visible. Synthetic truth is only an evaluation target.

**L9: What creates the improved recovery action?** The protected, full-rank measurement set changes the estimate used by the QP. The reference action is u≈0.121694 p.u., reducing true toy branch flow from 0.24 to 0.170461 p.u. under a 0.18 limit. Trust is assumed, not authenticated by an LLM. Three protected angles provide no residual redundancy. Do not attribute the effect to an explanation generator.

**L10–L12: What does the operator acknowledge?** A specific case/candidate/model/evidence packet. A wrong ID, missing operator name or insufficient model scope is rejected. Actual saved Llama traces remain distinct from fresh numerical labs. The optional live call returns a choice and public rationale, never approval. The local acknowledgment does not dispatch equipment.

## Timing and reliability

Run all cells once before class, using the folder as the working directory. Check the executed HTML on a machine without dependencies. Preload the desired local model if using L11. The separate 17 October validation took 34.113 seconds including 16.967 seconds of model loading; it is a useful example of why cached display and warm inference are different clocks. Have the saved response ready if a live call is slow.

During labs ask for a prediction before execution, then a specific supporting metric. Work in pairs: one operates the notebook, the other audits the claim. If the group is behind, preserve the core numerical experiments and use saved LLM output; do not consume the break with installation. Do not add appendix frames unless replacing an equally long activity.

## Scientific reading and limitations

Use `appendix/Agentic_AI_Research_2026.md` for verified primary-source descriptions through 17 October 2026. The foundation table summarizes mechanisms; it is not a cross-paper leaderboard. New literature examples are not installed/reproduced benchmarks. Cite the original source for each claim and keep preprint status visible.

The five-stage structure and numerical verification have close prior art. No novelty claim is made for merely using several agents. Recorded selector results show no general superiority over voting or simpler rules. A future study should measure language interpretation, evidence-supported completion, electrical outcomes, latency, workload and human error separately.

Each frame has additional notes in `latex_slides/Instructor_Notes.md`. Exact source alignment, including historical appendix cells, is in `latex_slides/Slide_Notebook_Map.md`.
