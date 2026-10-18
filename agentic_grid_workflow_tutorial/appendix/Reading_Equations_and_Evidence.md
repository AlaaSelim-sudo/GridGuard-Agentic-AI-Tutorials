# Reading the equations and evaluating the agent workflow

This guide accompanies the three-hour slides and the 23 notebook checkpoints. The revised slides put symbol definitions beside their equations. The supporting [literature comparison](Recent_Agentic_AI_Literature.md) and [actual agent responses](Case_Agent_Responses.md) provide more detail for later study.

## Read a formulation in five steps

1. **State the decision.** Is the method choosing inverter setpoints, connecting loads, estimating angles, or selecting a permitted tool?
2. **Identify the variables and units.** Real-valued setpoints, binary switch decisions and language choices belong to different mathematical spaces.
3. **Read the objective.** It states a preference among feasible choices. Its weights are design choices and must be disclosed.
4. **Read the constraints.** They describe the model and admissible actions. A solver can satisfy them while the model omits a relevant physical effect.
5. **Separate solution, verification and handoff.** A computed candidate, a passing model check and an operator acknowledgment are three different outcomes.

## Symbols are local to a formulation

| Context | Symbols and meaning | Units / interpretation |
|---|---|---|
| Feeder | Bus $i$, phase $\phi$, branch $\ell$, inverter $g$ | Indices, not measured quantities |
| Voltage support | $v_{i\phi}$, current $I_{\ell\phi}$, inverter $p_g,q_g,S_g$ | Voltage magnitude in per unit; current in A; kW, kvar and kVA in the feeder interface |
| Shared control | $u=[a,b]$, $p_g=aS_g$, $q_g=bS_g$ | $a,b$ are dimensionless fleet participation factors; $b<0$ means reactive absorption in this convention |
| Current reserve | $\rho$, $\rho I^{\rm rated}$ | Allowed fraction and allowed current; $\rho=0.8$ preserves a requested 20% reserve |
| MPC | $k$, horizon $H$, previous action $u_{-1}$ | Forecast-step index, number of planned steps, and the last declared setting |
| SAC | Observation $o$, policy $\pi$, normalized action $z$ | A learned mapping; $z\in[-1,1]^2$ is mapped into inverter capability |
| Restoration | $y_i,s_i,z_e\in\{0,1\}$ | Energized bus, served load, selected edge. Here $z_e$ is unrelated to the SAC action |
| Restoration flows | $P_e$, demand $P_i^d$, connectivity commodity $f_e$ | kW, kW, and dimensionless graph-connectivity units |
| Estimation | $z$, state $x$, matrix $H$, covariance $R$ | Measurement vector, non-slack angles in radians, measurement map, and noise covariance. Here $z$ is unrelated to restoration's binary variable |
| Cyber control | Injection $u$, flow map $F$, sensitivity $b$, flow bound $\bar f$ | Scalar injection and branch flows in per unit; $b$ is not voltage control's reactive participation factor |

The appendix and slides define additional subscripts, weights and operators where they occur. General equations may contain more decisions than the deliberately restricted executable examples. Read each slide's **general method** and **implemented reduction** separately.

## What the results actually compare

| Question | Matched comparison | Supported interpretation |
|---|---|---|
| Does verification and repair help a raw SAC point? | The same P3 proposal before and after the common verifier and MPC fallback | In OpenDSS, current falls from 111.97% to 99.60% of the allowed current. This measures the checking-and-repair contribution |
| Does Llama improve the numerical voltage result? | Fixed adaptive rules versus Llama with identical actor, MPC, model and acceptance checks | The recorded final controls are equal. No incremental Llama optimization benefit is demonstrated |
| Can language handling complete more requests? | Rule parser versus selective Llama with the same downstream restoration tools | Five clear restoration requests yield 3/5 versus 5/5 correct completions; this is a descriptive post-hoc subset |
| Does the language gain imply reliability? | All twelve requests in the parent corpus | Wrong READY interpretations are 1/12 versus 2/12. The useful subset must be read alongside this adverse outcome |
| Does the cyber workflow recover a usable control? | Corrupted-data WLS/control versus conventional trusted-data estimation and redispatch | The supplied trusted measurements and numerical method reduce the toy branch flow from 0.24000 to 0.17046 p.u.; the limit is 0.18 |
| Does Llama improve cyber detection? | Fixed versus Llama around the same estimator and redispatch | Same numerical candidate, but Llama requests REVIEW. This does not establish a detector or control advantage |

The output status matters. **MODEL_RECOMMEND** is a modeled recommendation under declared assumptions. **REVIEW** means the workflow has withheld that recommendation. A provisional tool candidate can be inspected without treating it as an approved action. No result in this tutorial is a field command.

## Relate the literature to this implementation

Read the framework comparison as a set of design choices: tool-observation feedback, role specialization, orchestration, durable state and human interruption. The tutorial uses some of these patterns in a small sequential implementation with local Llama 3.1. It does not run AutoGen, MetaGPT, Magentic-One or LangGraph, and it does not claim that eight role labels produce eight independent expert opinions. Their published evaluations do not transfer automatically to grid safety.

For each paper ask: what task did it evaluate, what numerical tools did it expose, what baseline did it use, and which authority did the agent hold? For a grid operator, these details matter more than an overall benchmark score from another domain. The literature appendix identifies publication status, source links, specific advantages and limitations.

## A stronger future experiment

Keep the numerical tools, allowed actions, model, initial proposal and verifier fixed while varying the supervisor. Prespecify diverse requests and disturbance cases; score semantic correctness separately from numerical feasibility and completion. Record Llama abstentions, incorrect interpretations, repeat-run variability, tool calls and latency. Compare against a capable conventional supervisor as well as a simpler baseline.

If the question is human benefit, conduct a separate operator study measuring decision correctness, appropriate challenge of bad advice, workload and task time. Solver timing and a readable explanation alone do not answer that question. These are proposed experiments; the supplied records remain a small teaching study.

## Reproducibility

This editorial revision changes explanatory text and slides. It preserves the executed code, numerical outputs, trained actor and actual recorded Llama replies. `A1–A2` show current continuous voltage records; `R4–R5` and `C4` include explicitly labeled historical records. Code excerpts remain generated directly from the notebook. Changing an input, algorithm or model requires recomputation before revising the numerical claims.
