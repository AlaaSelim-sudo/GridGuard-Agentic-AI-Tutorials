# MPC, DRL and agentic supervision: the comparison the tutorial should make

The scientific claim is **added supervisory capability**, not universal numerical superiority over MPC or DRL. The agentic framework can use an MPC optimizer or a trained policy as a tool. Verification, event interpretation, tool coordination and explanation then sit around that controller. A deterministic supervisor must remain a strong baseline because it can supply many of the same protections.

## Three distinct experiments

1. **Numerical control:** compare finite-action economic MPC and a genuinely trained deep Q-network on the same feeder, observations, actions and stage objective.
2. **Safety attribution:** compare raw controllers, updated MPC, DQN with a shared checker, and agents using MPC with that same checker. Attribute improvement to the component that changes.
3. **Language interface:** compare Llama's interpretation of maintenance notes with a deliberately narrow literal-number parser. This separate test does not measure control performance, operator workload or all conventional supervisory software.

The original voltage/restoration/attack cases remain in the tutorial. The new MPC/DQN numerical benchmark concerns voltage control only. Neither a trained restoration policy nor a mixed-integer restoration MPC is implemented; presenting those as tested would be incorrect.

## Economic MPC formulation

At each five-minute interval, solve a three-step finite-action horizon and apply its first action. The control is a fleet-wide PV cap from `{0,10,20,30,40,60,80,100}` percent of Pmpp. The state contains the previous cap. Demand is exogenous, with a supplied forecast. The stage utility is:

`PV_kW / 8000 − 0.15 × |cap − previous_cap| / 100`.

The horizon discounts future utility by 0.95 and imposes the same voltage and line-current constraints as the tutorial. The change penalty couples decisions over time. Dynamic programming solves the finite action problem exactly, and the controller replans at each interval. This is receding-horizon economic MPC for a **quasi-static feeder**. It does not simulate inverter transients, storage energy dynamics or closed-loop stability.

All methods use the same precomputed OpenDSS table: five demand levels and eight caps, totaling 40 unbalanced AC solves. The temporary line-rating reduction changes the allowable current, not the electrical solution, so those AC results remain reusable. This speeds up the class exercise and makes comparisons deterministic. It also makes the benchmark much easier than an unknown physical grid.

The forecast covers the next three demand samples. Each controller knows the currently validated rating; the MPC horizon holds that current rating constant. Future rating changes are not announced ahead of time. The intentionally stale-MPC ablation retains nominal ratings even after a change. It is a mismatch example, not a representative claim about well-maintained MPC.

## A trained DQN rather than a renamed heuristic

The DQN has six inputs, two 48-unit ReLU hidden layers and eight Q outputs. Inputs include the three-step demand forecast, previous cap, current rating fraction and remaining episode fraction. It learns from 18,000 transitions per seed using replay, a separate target network, Huber temporal-difference loss and Adam. Three independent training seeds are retained.

The reward uses the same stage utility for feasible actions and −2 for an unsafe action. The Bellman discount is 0.95. Training explores in software simulation only, under nominal ratings. Training sequences exclude the two exact test sequences, although training and test share the same five demand values. The changed-rating test is a deliberately small distribution shift. This is not broad out-of-distribution generalization.

The network learns from rewards and next states, not labels supplied by MPC. Its weights, training history and hyperparameters are included. It is a small teaching implementation of DQN, not a benchmark of all DRL algorithms or a production-grade policy.

## Matched and deliberately mismatched comparators

| Method | What changes | What its comparison establishes |
|---|---|---|
| MPC with stale limits | Keeps nominal rating during the maintenance event | Consequence of model/constraint mismatch |
| MPC with updated limits | Receives the same validated current limit as the agents | Strong deterministic matched-information baseline |
| Raw DQN | Trained only at nominal ratings, receives the new rating at test | Behavior under the specified unseen rating |
| DQN plus checker | Same trained network, with feasible-action filtering | Contribution of a controller-independent safety layer |
| Agents plus MPC | Llama routes numerical tools at events, critic records advice, common checker and MPC fallback remain independent | Feasibility, event coordination and inference overhead of this implementation |

The agentic controller invokes a planner and critic at initial observation and rating changes. The critic's advice is logged for inspection. In this supervisory experiment it does not itself revise the chosen route, so no causal improvement may be attributed to that extra critic call. The original four-slot search benchmark separately tests feedback and critic ablations.

The controller experiment receives already validated structured events. Consequently, it does **not** measure autonomous extraction or authentication of maintenance messages. The separate language test examines extraction and preserves failures. Its output never feeds the numerical benchmark.

## Measured outcomes

On nominal episodes, all five methods produce the same safe operating outcome. During the 80%-rating event, stale MPC and raw DQN average three violating simulated steps per 12-step episode. Updated MPC, shielded DQN and agents plus MPC have zero violating steps in these tests and the same mean PV energy, approximately 2,169.48 kWh over one hour. Their unprotected counterparts produce approximately 2,390.10 kWh while violating the operating limit. Higher infeasible output is not better control.

The zero-violation result comes from correct constraints and verification, which conventional controllers can also use. The measured agentic controller adds seconds of local inference. Its audit trail exposes the chosen tool and rationale, but a conventional implementation can also log decisions. Reduced engineering effort, better operator understanding or workload reduction require separate measurement.

The language test has eight notes. The narrow literal parser matches five expected outcomes, and Llama with schema/provenance checks matches six. Llama correctly interprets worded percentages but invents a 35% reduction for an ambiguous “reduce loading somewhat” note. A schema-valid, source-trusted answer can still misstate the intended policy. All interpreted policies therefore remain proposals requiring independent confirmation; none is dispatched in this test. This result supports supervised language assistance, not autonomous policy updates.

## A constraint set that neither controller can satisfy

At load multiplier 1.3 and 65% permitted line ratings, no action in the PV-only catalog passes. This initially probed severity is retained in `infeasibility_stress.json`. The main transient uses 80% to study adaptation where a feasible action exists. The severe case teaches a separate requirement: return no feasible recommendation and request additional control authority, such as different resources or load management. Agentic reasoning cannot make an infeasible action space feasible.

## Limits and cost accounting

The study uses two test load sequences, each in nominal and changed-rating form. DQN has three training seeds; MPC repetitions across those seeds are deterministic duplicates. The agentic method uses the seed-11 policy and one Llama run for each of the four physical scenarios. Do not use these unequal counts as a significance test.

Decision timing includes cached-table lookup, controller logic and any Llama calls. It excludes the 40-solve table build and the separate DQN training cost, both reported in their own records. It is not an end-to-end field-control latency measurement. The uncertainty, protection and transformer limitations of the original tutorial still apply.

## What benefits can be claimed, and what needs evidence?

| Proposed benefit | Demonstration here | Stronger evidence needed |
|---|---|---|
| Safety screening | Same unsafe proposals are blocked by shared checker | Robustness to model error and unmodeled constraints |
| Adaptation to changed limits | Updated MPC, shielded DQN and agentic MPC all adapt | Multiple unseen networks, contingencies and operating changes |
| Handling language | Some worded notes interpreted, including recorded errors | Larger blinded set, confirmation workflow and error costs |
| Coordinating numerical tools | Actual Llama routing calls and deterministic fallback | Complex tasks where routing improves outcome over fixed routing |
| Explainability | Exact tool calls, rejections and rationales available | Operator comprehension and fidelity study |
| Reduced workload or development time | Not measured | Controlled operator/developer study |
| Better optimality than MPC | Not established | Matched model, action space, information and compute |

## Exercise replacing the old five-minute baseline exercise

Use ten minutes within the expanded 30-minute comparison module. First predict which of the five methods will violate a changed limit. Read the result table, then identify the causal component for every improvement. Finally inspect the ambiguous maintenance note and specify what independent confirmation would be required before changing an operational constraint.

Expected answer: the checker or updated constraint explains the safety improvement. Llama is unnecessary for solving this small numeric case. Its potential contribution lies in assisting interpretation and coordination, with verified structured inputs and operator authority retained. A sophisticated deterministic supervisor is the appropriate counterfactual for those functions.

## Primary foundations

- Rawlings, Mayne and Diehl, [Model Predictive Control: Theory, Computation, and Design](https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-4th-printing.pdf).
- Mnih et al., [Human-level control through deep reinforcement learning](https://www.nature.com/articles/nature14236). The implementation uses the replay/target-network DQN structure, not the paper's image-based network.
- Wabersich and Zeilinger, [A predictive safety filter for learning-based control of constrained nonlinear dynamical systems](https://arxiv.org/abs/1812.05506). Safety filtering predates this agentic framework and can wrap different controllers. This tutorial does not implement that paper's formal uncertainty-aware guarantees.
