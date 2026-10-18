# Instructor guide: 180-minute agentic grid tutorial

## Teaching purpose

The tutorial turns the supplied proposal into an executable decision-support workflow. Participants should leave able to explain what each bounded agent contributes, inspect real Llama messages, evaluate constrained actions with a physical tool, and distinguish empirical search improvement from the protection supplied by independent verification.

The central scientific question is where language reasoning contributes beyond conventional methods. Do not describe every multi-agent result as a success. The saved comparisons include weak proposals, repeated choices and failed runs. The conventional rule search provides an intentionally strong baseline for the small, structured action catalogs.

## Preparation

1. Extract the complete bundle and follow README setup. Test the local Ollama endpoint and the exact model name before the session. Use the recorded benchmark when a participant lacks suitable local hardware.
2. Run `python -m src.validate` and open the executed notebook. Check that its figures display. Run the live seven-call R2 cell once to estimate classroom latency.
3. Keep the PowerPoint in presenter mode so that timed speaker notes remain visible. The deck has 42 slides, and the notebook is the executable companion.
4. Preserve a copy of the supplied results before exercises that alter the catalog or thresholds. The presentation is a fixed snapshot of the supplied study.
5. Participants need basic per-unit power-flow knowledge and enough Python to edit a parameter. Pair a power-systems participant with an AI participant when possible. Package/model downloads are prework, not part of the three-hour session.

## Timing and notebook crosswalk

| Minutes | Slides | Notebook module | Facilitation |
|---|---|---|---|
| 0–20 | 1–5 | 1. Problem and feeder | Establish three hypotheses; inspect the source/assumption distinction |
| 20–45 | 6–10 | 2. Multi-agent framework | Walk through the acceptance code and trust boundary |
| 45–65 | 11–14 | 3. Live Llama | Run actual proposals and critiques; inspect their messages |
| 65–85 | 15–18 | 4. Evaluation design | Explain budgets, baselines, ablations and conditional metrics |
| 85–110 | 19–24 | 5. Voltage | Connect branch-flow intuition to unbalanced simulation |
| 110–135 | 25–30 | 6. Restoration | Contrast feasible full pickup and constrained critical service |
| 135–160 | 31–36 | 7. Cyber | Separate model behavior, evidence authenticity and physical acceptance |
| 160–180 | 37–42 | 8. Interpretation | Read both quality and cost; design a defensible extension |

The schedule includes 51 minutes of exercises. It contains no additional break. A required ten-minute break can replace ten minutes of the final discussion/exercise block, or the event can allocate 190 minutes.

## Module 1: the problem and source provenance

Open the feeder map and ask participants what it establishes. It shows the coordinate layout of a synthetic feeder. It does not validate a real utility asset inventory or a field switching route. The source contains 2,173 load objects, 930 PV objects, 436 storage objects and 1,977 original lines. The experiment uses one 12.47 kV feeder and keeps storage idle.

Introduce the three hypotheses separately: scored history improves search, a separate critic adds value, and an independent verifier changes which proposals survive. Ask which hypothesis needs no LLM at all. The answer is verification on identical proposed actions.

**Exercise 1, four minutes.** Classify electrical source files, synthetic bypasses, critical-load labels and computed voltage as source facts, assumptions or outputs. Expected answer: original files are synthetic source data; ties and labels are constructed assumptions; voltage is conditional on a solved operating point. Award credit for identifying that even a source datum is not a real utility fact.

## Module 2: architecture and acceptance

The proposal's Awareness, Planning, Simulation, Verification and Optimization roles are all present. Awareness is deterministic structured state. The planner and optimizer call Llama. OpenDSS supplies physical metrics. Python decides acceptance. A separately prompted Llama critic interprets failures. All language roles share one model and execute sequentially.

Have participants trace `evaluate`: resolve an action from the immutable catalog, check policy/evidence, reset and simulate, verify physical metrics, then record a score and pass/reject outcome. A favorable rationale cannot override a failed check. The optimizer ranks only passing candidates. No feasible candidate means no recommendation.

**Exercise 2, five minutes.** Ask for a rationale that tries to ignore an overloaded line. Find the rejecting code and name a missing physical check. Expected answer: `verify_physics` reads measured loading independently of text; transformer thermal certification, phase-specific islands and protection coordination remain outside the model. Independence does not make an incomplete checker sufficient.

## Module 3: actual local inference

The notebook's live demo makes four proposal calls and three critic calls on R2. Its messages go into `live_demo_calls.json`, separate from the 123-call benchmark. Let participants predict the next action after one rejection before revealing the critic message. Use exact measured values to evaluate claims in model prose.

Explain the two-field output schema. A valid JSON object gives a string action ID and rationale. A catalog match determines the actual control parameters. Unknown action IDs are rejected and consume their candidate slot. Temperature and seed help record the experiment, but do not guarantee reproducibility across hardware or software changes.

**Exercise 3, six minutes.** Change the seed, retain every candidate and compare final service, candidate feasibility and latency. Expected answer: a claim of “all critical load restored” can be correct while most total demand remains disconnected. Neither a fluent rationale nor a useful critique proves that the next action improves.

## Module 4: the comparison design

Use the table of eight methods. No action and fixed rule use one candidate. Random, rule search, single Llama, no critic and multi-agent have four candidate slots plus one awareness solve. The exhaustive reference uses all eight voltage or ten restoration catalog entries.

Single Llama sees previous IDs but no scored history. No critic adds scored history. Multi-agent adds critic feedback and three extra model calls. All use the same acceptance checker. Rule search uses explicit informed orders. Explain that this is not a comparison to an AC OPF or mixed-integer restoration optimizer, which are future benchmarks.

Relative gap is defined only if a verified solution exists. Report success beside conditional gap. Do not turn a failed run into zero gap, and do not treat repeat measurements of a deterministic rule as independent cases.

**Exercise 4, five minutes.** Design equal-token or equal-wall-time comparisons. Expected answer: permit extra direct proposals when the critic's inference budget is removed, preserve information and tool access, and report actual solves, model calls and total time. Fixing candidate count alone does not fix computation.

## Module 5: voltage control

Derive the voltage intuition from squared-voltage branch flow: downstream consumption usually creates a drop, while export can create a rise. The actual checker uses unbalanced OpenDSS, not the simplified equation. Explain why current can bind after voltage violations disappear.

V1 holds nominal demand. V2 uses 70% demand. The only control is the fleet-wide active PV cap. The objective is measured instantaneous PV kW, with voltage and line-current constraints. This restriction creates a tractable, inspectable scientific case. It does not represent comprehensive Volt/VAR control.

**Exercise 5, eight minutes.** Predict the V1 PV_40 result and then inspect it. Expected answer: voltage violations clear but overloaded lines remain. Adding PV_35 changes the finite action space and requires a new reference evaluation. Explain why `%Pmpp` does not directly measure energy curtailed.

## Module 6: restoration

R1 isolates the incoming line and offers two synthetic bypass alternatives. They connect the same source and downstream terminal; they are not neighboring utility feeders. R2 removes PV, disables the long bypass and lowers the short-bypass rating to 100 A.

The objective is critical-weighted nominal service, with weight 10 on every tenth sorted load. All shedding options preserve the critical subset. The noncritical shedding percentage counts load objects, not power. Selection is lexicographic and assumes individual relays. The resulting disconnect count should prompt discussion about a more realistic sectional-switch model.

Explain multigraph cycles. Two parallel closed bypasses create a cycle; collapsing them into a simple edge would miss the violation. Bus connectivity and MV cycle count remain limited approximations of operational topology requirements.

**Exercise 6, eight minutes.** Explain why `short_all` passes R1 and fails R2. Expected answer: reduced bypass capacity and absent PV increase loading. Propose real switchable sections and an objective penalty for switching burden. Distinguish full critical service from full demand restoration, and nominal kW from energy not served.

## Module 7: attacks and gate ablation

Use all 14 fixtures. Eleven are controlled evidence/action cases including clean and benign controls; three call Llama with actual malicious notes. Preserve the stealth-bias pass, which reveals the residual rule's limitation. In the saved prompt-injection trials, one model response selects fault reclosure and the policy gate rejects it. Discuss that specific evidence without claiming general robustness.

The evidence booleans and timestamp values are fixtures. There is no authentication, deployed state estimator or hardware readback pipeline. Defaults represent the nominal clean simulated case. A field implementation should require explicit trusted evidence and fail closed. A post-action readback failure also needs a recovery procedure, since rejection cannot reverse an earlier actuation.

Show the three ablation columns on the same proposed actions: ungated, catalog-only and full checker. Do not call every accepted action under malicious input physically unsafe. Separate attack compliance, authenticity detection and action feasibility.

**Exercise 7, eight minutes.** Tighten the scalar residual threshold to 0.002 pu. Expected answer: both benign +0.003 and malicious +0.005 errors now reject. The exercise exposes a false-alarm/detection tradeoff, not a robust detector. A compromised trusted reference is outside this fixture design.

## Module 8: interpretation and research design

Read the result plots aloud with their denominators. There are four scenarios and two seeds, yielding eight runs per method. The multi-agent and rule-search methods both find a feasible action in every saved run. The no-critic method fails on both R2 seeds. Rule search is much faster and reaches the catalog reference in all cases. This supports a discussion of critic contribution in these runs, while preventing an unsupported claim of LLM superiority.

The framework's demonstrated value is reproducible context, bounded actions, measured consequences, explicit rejection and an auditable final selection. Reduced operator workload is a plausible objective but requires a separate user study.

**Capstone, seven minutes.** Each pair chooses one claimed advantage and states the comparator, controlled variables, outcome metric and limitation. A strong answer separates search quality from gate safety and identifies how a result could falsify the claimed advantage.

## Assessment rubric

Award one point for each: correct physical explanation; correct action/constraint distinction; correct budget accounting; explicit source-versus-assumption distinction; honest interpretation of failures. A complete five-point response should avoid a deployment-safety or statistical-superiority claim.

## Troubleshooting

- No Ollama connection: use a local kernel, verify the endpoint, or set the live flag false and explicitly teach from saved actual calls.
- Missing model: install the stated tag, or choose an installed model and treat the resulting run as a different experiment.
- Imports fail: install requirements in the environment that provides the Jupyter kernel.
- Results change: inspect model digest, versions, seeds and catalog edits. Retain the changed result rather than selecting only favorable runs.
- Figure changes do not appear: regenerate plots and rerun the notebook display cells. The slide deck remains the original study snapshot.
