# Continuous SAC: training, inference, and physical verification

This supplement documents the actual implementation in `src/continuous_control.py` and the supplied seed-23 checkpoint. `Continuous_SAC_Training.ipynb` is optional work outside the three-hour workshop. It reads the saved evidence by default. Changing `RETRAIN` to `True` trains a new policy in a separate directory; it does not replace the supplied policy or results.

## What is learned?

The SAC actor proposes two continuous fleet participation factors, not a discrete action index and not 930 independent inverter settings. For inverter rating $S_i$, the commands are $p_i=aS_i$ and $q_i=bS_i$. This fixture assumes available active power equals each inverter's kVA rating; the adapter checks that assumption. Positive $q_i$ denotes reactive injection under the adapter's sign convention.

The actor produces a normalized action $z\in[-1,1]^2$. The environment maps it to

$$a=\frac{z_1+1}{2},\qquad b=z_2\min\{0.44,\sqrt{1-a^2}\}.$$

This guarantees $0\le a\le1$, $|b|\le0.44$, and $a^2+b^2\le1$ for the proposed fleet command. It does **not** guarantee network voltage or current feasibility. SAC's entropy term is defined in the normalized $z$ coordinates; the capability mapping is part of the environment.

The seven observations are the three remaining forecast demand multipliers (padded with the last available value), the previous $a,b$, the permitted fraction $\rho$ of nominal line current, and the remaining horizon divided by three. Demand sequences are known to this small teaching environment. Topology, uncertainty, and other independent inverter controls are not learned state variables.

## Environment and reward

A cubic least-squares response surface predicts four full-feeder OpenDSS summaries: minimum voltage, maximum voltage, maximum nominal line-current fraction, and mean squared voltage deviation from 1.01 pu. Its 20 polynomial features use demand multiplier, $a$, and $b$. The saved data contain 240 fitting samples and 48 separate fit-validation samples, all produced by fresh OpenDSS solves with seed 2301. Active and reactive load scale together; commanded PV kvar, capacitors, shunts, and storage standby power do not scale with the load multiplier. Negative surrogate predictions for current fraction and mean squared voltage deviation are clipped to zero.

For $u=(a,b)$, the base cost is

$$\ell(u,u^-)= (1-a)^2+0.05b^2+10\,\overline{(v-1.01)^2}+0.05\|u-u^-\|_2^2.$$

Let $e_v=[0.95-\widehat v_{\min}]_++[\widehat v_{\max}-1.05]_+$ and $e_I=[\widehat I_{\max}/I_{\rm rated}-1]_+$. The actual training reward is

$$r=-\ell-40(e_v/0.05)^2-10e_I^2-2\,\mathbf1\{e_v>0\text{ or }e_I>0\}.$$

Every training episode has three steps, independent demand multipliers drawn uniformly from $[0.7,1.2]$, a randomized previous command, and nominal current allowance $\rho=1$. The training reward therefore uses the nominal rating, not a randomized reserve. The supplied 80% allowance case is a declared distribution shift. This response surface speeds reward collection; it is not a power-flow solver or the final verifier. No MPC actions, labels, or demonstrations enter the SAC replay buffer.

## Actual SAC protocol

SAC learns from stored transitions using entropy-regularized actor and critic updates. The implementation uses Stable-Baselines3 SAC, with a stochastic squashed-Gaussian actor during training and deterministic actor inference for the study. The actor and critic use two 64-unit hidden layers; the actor export applies ReLU hidden layers and a tanh output. The general SAC method is described by [Haarnoja et al. (2018)](https://proceedings.mlr.press/v80/haarnoja18b.html); implementation conventions are documented in [Stable-Baselines3 SAC](https://stable-baselines3.readthedocs.io/en/master/modules/sac.html).

| Item | Supplied setting |
|---|---:|
| Seed; environment steps | 23; 12,000 |
| Episode length; completed episodes | 3; 4,000 |
| Discount $\gamma$ | 0.98 |
| Learning rate; batch size | 0.0003; 128 |
| Replay capacity; learning starts | 30,000; 600 |
| Target update factor $\tau$ | 0.005 |
| Fixed entropy coefficient | 0.005 |
| Device; PyTorch threads | CPU; 1 |
| Observed gradient updates | 11,400 |
| Recorded versions | PyTorch 2.14.0+cpu; SB3 2.9.0; Gymnasium 1.3.0 |

The supplied run records 12,000 replay transitions, 4,000 terminal transitions, and 12,000 distinct normalized replay actions. Its final checkpoint was retained without selecting a checkpoint on heldout performance. The exported NumPy actor differed from the trained implementation by at most $5.96\times10^{-8}$ on the three declared probe observations. That is a finite parity check, not an exhaustive equivalence proof. The recorded training duration is 31.7 seconds on one host; surface preparation took 48.5 seconds. These are descriptive single-run timings, not a hardware-independent benchmark.

The fixed entropy coefficient means this run does not use automatic temperature tuning. [Soft Actor-Critic Algorithms and Applications (Haarnoja et al., 2018)](https://arxiv.org/abs/1812.05905) discusses that broader algorithm family; not every feature in that paper is enabled here. [PPO (Schulman et al., 2017)](https://arxiv.org/abs/1707.06347) is an extension option; no PPO policy has been trained or compared in the supplied study.

## Keep three kinds of evidence separate

| Evidence | What it measures | What it does not establish |
|---|---|---|
| Training episode reward | Learning behavior in the approximate environment | Fresh AC feasibility or generalization |
| 48 surface-validation points | Approximation error on separately sampled points from the same sampling range | Worst-case error bound or heldout control performance |
| Three authored control trajectories on two backends | Actual proposals and fresh checks on this feeder | Population success rate, unseen-feeder transfer, or field safety |

The surface-validation mean absolute errors are 0.000872 pu for minimum voltage, 0.002100 pu for maximum voltage, and 0.040989 of nominal current (4.099 percentage points). Maximum observed errors are 0.004697 pu, 0.007109 pu, and 0.167215 of nominal current. They explain why the surrogate cannot serve as the acceptance gate.

P1 is nominal demand; P2 changes demand over three steps; P3 also reduces permitted current to $0.8I_{\rm rated}$. The same actor is used on OpenDSS and the MV-only three-phase LinDistFlow model. OpenDSS covers the supplied MV/LV feeder; LinDistFlow uses ideal transformer aggregation and checks MV phases only. Agreement or a pass in the latter scope cannot certify LV limits.

The saved `continuous_control.json` study gives raw SAC a fresh selected-model check. If that first move fails, the fixed shield proposes the first move of the continuous local horizon optimizer and checks it again. The raw SAC action fails the OpenDSS P3 thermal limit; the optimizer fallback passes the selected-model check. All six selected checked first moves pass their respective model checks in this authored demonstration. This result belongs to the **combined check-and-fallback procedure**, not to SAC alone. Full three-step raw rollouts and their feasibility are also stored. The main agentic workflow adds its own routing, optimization comparisons, review decisions, and operator report; its separate records must be consulted for those results.

The optimizer solves a local $H=3$ sequential sensitivity-QP planning problem, retains only horizons accepted by fresh physical solves, and proposes the first move. This experiment inspects one horizon decision; it does not execute a closed-loop receding-horizon study. The supplied plans do not prove global AC optimality, recursive feasibility, robustness, or stability. The final engineering check reconstructs feasibility from finite, identified, fresh evidence, including model scope, voltage, allowed current, and per-device P/Q tracking. It cannot correct an incorrectly interpreted operator limit.

## Reproduce and extend

1. Open `Continuous_SAC_Training.ipynb` with the ordinary workshop dependencies. Leave `RETRAIN=False` to inspect the checkpoint hashes, protocol, learning curves, action mapping, and saved physical evaluations. This path needs no Llama, PyTorch, or fresh OpenDSS solve.
2. For optional new training, install `requirements_training.txt`. The notebook copies the supplied surface into a new `models/continuous_sac_runs/<timestamp-and-ID>` directory, temporarily points `train_sac(seed, steps)` there, and restores the module's original model directory in a `finally` block. Run this cell serially in its notebook kernel. It starts training from initialization; it does not resume the saved replay buffer.
3. Compare new training traces separately. Retraining on the supplied surface is not a new physical-data experiment. To prepare a different surface, use `build_surrogate(...)` in an isolated model directory with the full OpenDSS dependencies; predeclare fit and validation splits before control evaluation.
4. For a scientific extension, predeclare several training seeds and unseen demand sequences, vary reserve during training, and evaluate voltage/current violations, objective, fallback frequency, and end-to-end time with identical model checks. Add PPO only through an actual trained implementation under the same observations, action mapping, budget, and checks. Report uncertainty across runs rather than selecting the best seed.

Provenance is stored in `models/continuous_sac/training_protocol.json`, `training.json`, and `response_surface.json`. The notebook checks the actor, training checkpoint, and response-surface SHA-256 values against those records. Source hashes identify the producing revision; they are not a claim that later orchestration edits regenerated these frozen numerical records. A subsequent wording-only source change is documented in [source_revision_note.json](../models/continuous_sac/source_revision_note.json); it did not retrain the policy or alter its numerical evidence.
