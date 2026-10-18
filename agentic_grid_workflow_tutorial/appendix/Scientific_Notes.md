# Scientific notes and reproducibility

**Scope of this record:** the equations and results below document the original restricted workflow. For the general three-use-case OPF/MILP/WLS formulations, see [General Optimization Formulations](General_Optimization_Formulations.md). The separate [standard-method notebook](../Standard_Formulations.ipynb) runs continuous P/Q optimization and compact MILP/WLS experiments. Those additions do not relabel or overwrite the frozen studies.


These notes document the original OpenDSS teaching model and identify extensions that need additional experiments. The separately implemented stage-workflow extension includes a genuine coupled three-phase LinDistFlow MV solver, a matched two-model comparison, and operator readback; its equations, scope, and recorded results are in [Stage_Methods_and_Models.md](Stage_Methods_and_Models.md). The original experiments described below retain their original protocol. The combined teaching route remains three hours.

## 1. What is solved

The voltage-control tool uses **finite-action MPC with a three-step horizon**. It is not a continuous AC optimal-power-flow solver and does not implement a three-phase LinDistFlow approximation. Its predictive model is a table of nonlinear OpenDSS solutions for the included feeder.

The table contains 40 operating points: five demand multipliers and eight common PV caps:

\[
\mathcal L=\{0.3,0.5,0.7,1.0,1.3\},\qquad
\mathcal A=\{0,10,20,30,40,60,80,100\}\%.
\]

The cap is the OpenDSS PV-system %Pmpp setting. The reward uses the actual PV output returned by the electrical simulation, rather than assuming that the cap equals delivered power.

At a tabulated demand and action, the predictive value is a stored solution of the nominal feeder model. There is no interpolation. “Exact table” means that these particular nominal-model operating points were solved; it does not mean that the model exactly represents a real feeder or that arbitrary demand values are represented.

Both the predictive table and the fresh verifier use the same feeder and OpenDSS model. A fresh solve checks that the current candidate is evaluated again; it does not provide independence from common model error. This distinction matters when interpreting apparent agreement [1, 2].

## 2. MPC objective and information

For a given known load-index forecast \(l_0,l_1,l_2\), the tool solves

\[
\max_{a_0,a_1,a_2\in\mathcal A}
\sum_{k=0}^{2}\gamma^k
\left[
\frac{P_{\mathrm{PV}}(l_k,a_k)}{8000}
-0.15\frac{|a_k-a_{k-1}|}{100}
\right],\qquad \gamma=0.95.
\]

Here \(P_{\mathrm{PV}}\) is in kW, \(8000\) is a chosen kW normalization, the cap values \(a_k\) are percentage points, and \(a_{-1}\) is the previous cap. The movement penalty couples consecutive actions. A Bellman recursion finds the best sequence within this finite catalog and forecast.

Feasible candidates satisfy the implemented checks at every predicted step, including voltage bounds of 0.95–1.05 p.u. and line-current limits. A rating fraction \(\rho\) changes the permitted current to \(\rho I_{\mathrm{normal}}\); it does not change the feeder impedance or the solved current. If no feasible horizon exists, the tool escalates. It does not replace an infeasible future with a falsely finite cost.

The rollout applies only the first action, updates the previous action, and replans. This is the receding-horizon mechanism taught here [3]. Five-minute labels describe the demonstration sequence. The model has no battery energy state, thermal dynamics, forecast uncertainty, or robust terminal set. Stability and recursive-feasibility guarantees are not established.

## 3. DQN policy

The supplied DQN is trained from rewards, not from MPC labels. It uses two hidden ReLU layers with architecture \(6\rightarrow48\rightarrow48\rightarrow8\), experience replay, a target network, Huber temporal-difference loss, and Adam.

Its observation contains three normalized forecast demand multipliers, the previous cap, the rating fraction, and the remaining episode fraction. In a one-candidate tool call, the remaining fraction is 1. The selected action is

\[
a=\arg\max_{a\in\mathcal A}Q_\theta(o,a).
\]

The training reward is the MPC stage utility when the nominal action passes the electrical checks, and \(-2\) otherwise. The target is

\[
y=r+\gamma(1-d)\max_{a'}Q_{\bar\theta}(o',a'),
\]

where \(d\) marks the episode end and \(\bar\theta\) denotes target-network parameters [4].

Training uses seed 11, 18,000 transitions, a replay capacity of 12,000, batches of 64, and target updates every 200 gradient steps. The learning rate is 0.001. Episodes contain 12 demand steps. Nominal rating is the only training rating. Two specific test trajectories are excluded from sequence generation, but the same five demand levels and physical table are used in training and testing. Excluding two trajectories is not evidence of broad out-of-distribution generalization.

This small CPU training run takes seconds on the preparation machine. The checkpoint is supplied so participants can focus on the workflow. Training reward includes exploratory actions, so its learning curve is not a final deterministic-policy evaluation.

## 4. Restoration objective and action scope

The restoration tool enumerates short-bypass choices with shedding fractions \(0,0.25,0.5,0.65,0.75,0.9\), plus a long-bypass full-service choice when that route is available. It evaluates each using OpenDSS and the applicable checks.

Among passing candidates, it maximizes

\[
J_{\mathrm{rest}}=P_{\mathrm{served}}+9P_{\mathrm{critical,served}}.
\]

Because total served load already includes critical load, this gives critical demand weight 10 and other demand weight 1. It is a weighted sum, not a strict lexicographic critical-load-first objective. If weighted service ties, the tool chooses lower simulated losses.

The catalog sheds only noncritical loads. Consequently, preserved critical load partly reflects the catalog design; it does not demonstrate that an optimizer discovered an optimal priority policy. The search is optimal only over its enumerated candidates.

Service is nominal connected demand in kW, scaled by the demand multiplier. It is not integrated energy served. Reachability is checked at bus level. The radiality check uses the reachable medium-voltage multigraph and retains parallel branches. It does not prove complete phase-level restoration or protection feasibility [5]. The precise overlays are documented in [DATA_SOURCE.md](../data/DATA_SOURCE.md).

## 5. Voltage-sensitivity illustration

For a single-phase branch with per-conductor resistance \(r\), reactance \(x\), phase power \(P_\phi+jQ_\phi\), and phase-to-neutral voltage \(V_{\mathrm{LN}}\), dropping loss terms gives

\[
V_{\mathrm{LN},j}^{2}\approx
V_{\mathrm{LN},i}^{2}-2(rP_\phi+xQ_\phi).
\]

For the **balanced illustrative equivalent**, use \(P_{3\phi}=3P_\phi\), \(Q_{3\phi}=3Q_\phi\), and \(V_{\mathrm{LL}}^2=3V_{\mathrm{LN}}^2\). Therefore,

\[
V_{\mathrm{LL},j}^{2}\approx
V_{\mathrm{LL},i}^{2}-2(rP_{3\phi}+xQ_{3\phi}),
\]

and, with squared per-unit voltage \(v=V_{\mathrm{LL}}^2/V_{\mathrm{base,LL}}^2\),

\[
v_j\approx v_i-
\frac{2(rP_{3\phi}+xQ_{3\phi})}{V_{\mathrm{base,LL}}^2}.
\]

Use consistent units: ohms, watts, vars, and volts. Do not combine three-phase total power with a phase-to-neutral voltage base in this expression. These equations explain an intuition; mutual coupling, unbalance, transformers, losses, and nonlinear device behavior require the fuller implemented model or a properly derived multiphase approximation [1, 6].

## 6. Evidence, verification, and agent roles

The workflow requires source, age, topology, and voltage-comparison evidence. It rejects missing fields, invalid values, stale evidence, topology disagreement, and a voltage residual above its stated threshold. The trusted comparison is a simulated fixture, not deployed authenticated telemetry.

Actual local Llama calls select numerical tools and provide bounded repair feedback. The model does not write dispatch commands. It shares a finite tool catalog and operating schema with the scripted workflow [7]. A common initial-tool override in a repair experiment is an experimental intervention and must be applied equally to both routes.

The fresh electrical verifier checks only the implemented conditions. Formal predictive safety filtering requires additional dynamical-model and uncertainty assumptions [8]. Repeated calls to the same model and separate prompts do not make the agents statistically independent.

A measurement residual is not a universal intrusion detector. Prompt-injection behavior and numerical-data consistency should be scored separately. A rejected malicious action does not imply that the model itself resisted the malicious instruction [9].

Request interpretation is another source of error. The electrical gate checks the constraints it receives. In confirmation h05, both the parser and the parser-first hybrid lose a requested 20% current reserve. Their 30% PV cap passes the runtime gate using nominal current allowance but fails the offline gold check at 109.50% of the intended 80% allowance. This is one accepted candidate outside the gold requested limits for each interface. A fresh solve cannot reconstruct a missing semantic restriction. Operator readback and validation of interpreted limits would be needed before such a design supported field recommendations; this tutorial does not implement or evaluate that human process.

## 7. Reproduce and audit

Run these commands from the tutorial folder in the selected Python environment:

~~~text
python -m src.run_labs
python -m src.run_labs --replay
python -m src.run_labs --train
python appendix/test_physics.py
python appendix/test_workflow.py
~~~

The first command executes actual local Ollama calls and writes the experiment records. Replay reads the supplied records and regenerates their figures; it does not perform a new model evaluation. The training option explicitly regenerates the seed-11 checkpoint before running the scenarios. Save a copy of prior results and model files before regenerating if you need to compare revisions.

The AC-table manifest hashes the source feeder, physics code, control code, and catalog settings. The policy manifest additionally covers the training code, training settings, weights, and training record. A mismatch requires rebuilding the table and explicitly retraining; it is not silently treated as a valid checkpoint.

Review results/labs.json, the Llama journal, the AC-table manifest, and models/training_seed_11.json. Record package versions, model identity/digest, seeds, and the machine used. A seed is useful provenance but does not ensure identical language-model output across model/runtime/hardware changes.

The appendix regression tests include explicitly named test doubles to exercise failure paths without live Llama requests. Those doubles are test fixtures only. They are not used as evidence of trained-policy behavior or live agent performance in the main experiments. Electrical verification tests also use fresh OpenDSS solutions.

Timing is descriptive for the recorded run on its preparation hardware. Separate cached lookup/inference time, AC-table construction, fresh solves, model loading, Llama calls, and training where those costs are reported. One run supports neither statistical speedup claims nor hardware-independent latency claims.

The supplied core scenario study has six actual Llama calls; the notebook setup makes one additional separate call. Both matched workflows reach the same principal engineering outcomes, and the fixed supervisor is faster. These findings do not establish an agentic advantage in physical performance, stronger safety, or statistical superiority. They demonstrate a traceable tool-selection and repair workflow.

The additional request pilot, recovery experiment, and prospective hybrid confirmation are documented in [Agentic_Advantage_Study.md](Agentic_Advantage_Study.md), including their separate call counts, controls, results, and reproduction commands. The pilot uses 72 unique actual model calls; recovery uses six; confirmation uses six. Language-assisted intake correctly completes additional authored requests while also making semantic errors. Additional critic/self-review passes perform worse in the pilot. Adaptive deterministic repair matches agent repair on all three known failures. These experiments separate request coverage from physical control quality and do not measure human workload.

Development failures are retained in appendix/schema_debug_*.json and appendix/routing_debug_*.json. The final schema limits responses to each task's permitted tools; the final context supplies an explicit operator objective and structured tool descriptions. These changes address observed development failures. The revised examples are not held-out proof of generalization, and the development calls should not be pooled with the six-call core scenario study.

## 8. Extension exercises

1. **Retrain and inspect.** Regenerate the seed-11 policy. Compare the training metadata, checkpoint provenance, deterministic decisions, and feasibility. Explain why a rising exploratory training reward is not a complete evaluation.
2. **Multiple seeds.** Extend the training function to accept a seed and save each checkpoint separately. Pair each policy with the same held-out scenarios, compare both workflows, and report outcome variability and repeated timing measurements. Do not select only successful seeds.
3. **Shifted demand.** Add demand levels outside the current table and evaluate the resulting actions through fresh OpenDSS solves. Declare how each controller receives the shifted forecast. The current table cannot silently interpolate or extrapolate.
4. **Uncertainty.** Introduce stated forecast/model errors. Give both supervisors the same information and uncertainty-aware tool. Measure constraint violations and conservatism; consider scenario or robust MPC rather than assuming the nominal gate is robust.
5. **Actual switch zones.** Replace individual-load relays and synthetic bypasses with documented sectional switches, feasible switching sequences, phase connectivity, and equipment ratings. Redefine service groups and recheck the objective and radiality conditions.
6. **Operator study.** Compare factual explanation accuracy, task completion time, and interventions with participants, predefined tasks, and a stated protocol. A readable trace alone does not measure reduced workload.

## References

1. M. Farivar and S. H. Low (2013), *Branch Flow Model: Relaxations and Convexification (Parts I, II).* [Paper](https://arxiv.org/abs/1204.4865).
2. EPRI, *OpenDSS Power Flow* and *OpenDSS Solution Techniques* (online documentation, accessed 2026). [Power flow](https://opendss.epri.com/PowerFlow.html); [solution methods](https://opendss.epri.com/OpenDSSSolutionTechniques.html).
3. J. B. Rawlings, D. Q. Mayne, and M. M. Diehl (2022 electronic printing), *Model Predictive Control: Theory, Computation, and Design*, second edition. [Book](https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-4th-printing.pdf).
4. V. Mnih et al. (2015), *Human-level control through deep reinforcement learning*, Nature 518, 529–533. [Paper](https://www.nature.com/articles/nature14236).
5. Y. Wang, Y. Xu, J. Li, J. He, and X. Wang (2020), *On the Radiality Constraints for Distribution System Restoration and Reconfiguration Problems.* [Paper](https://arxiv.org/abs/1912.05185).
6. L. Gan and S. H. Low (2014), *Convex Relaxations and Linear Approximation for Optimal Power Flow in Multiphase Radial Networks.* [Paper](https://arxiv.org/abs/1406.3054).
7. S. Yao et al. (2023), *ReAct: Synergizing Reasoning and Acting in Language Models*, ICLR. [Paper](https://arxiv.org/abs/2210.03629).
8. K. P. Wabersich and M. N. Zeilinger (2021), *A predictive safety filter for learning-based control of constrained nonlinear dynamical systems.* [Paper](https://arxiv.org/abs/1812.05506).
9. A. Vassilev et al. (2025), *Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations*, NIST AI 100-2 E2025. [Report](https://csrc.nist.gov/pubs/ai/100/2/e2025/final).
