# Three core use cases: general formulations and executable teaching reductions

The tutorial has three applications: **voltage support, service restoration, and cyber-attack response**. Each starts with an engineering problem, gives a mathematical formulation, and then uses agents to organize the numerical work. MPC, optimization, state estimation, and electrical simulation remain the sources of numerical decisions. A language-model response cannot relax a constraint or turn an unsuccessful solve into a feasible recommendation.

The formulations below are a tutorial synthesis of established methods, not a claim that one algorithm is universally preferred or most widely deployed. Their small executable counterparts deliberately expose the variables, objective, constraints, and failure conditions. A successful small example does not establish full-feeder optimality or field readiness.

## Common notation and decision contract

Let \(\mathcal N\) be buses, \(\mathcal E\) physical branches, \(\Phi_i\subseteq\{a,b,c\}\) phases present at bus \(i\), and \(k=0,\ldots,H-1\) forecast intervals. Missing phases are omitted; they are not zero-voltage observations. Let \(\mathcal D\) contain controllable devices and \(\mathcal L\) load blocks.

| Symbol | Meaning | Reporting unit |
|---|---|---|
| \(V_{i\phi},\theta_{i\phi}\) | Complex phase voltage and its angle | V and rad; magnitude also p.u. |
| \(w_{i\phi}=\lvert V_{i\phi}\rvert^2\) | Squared phase voltage | V², or p.u.² after conversion |
| \(P,Q,S=P+\mathrm jQ\) | Active, reactive, complex power | kW, kvar, kVA |
| \(I_{ij\phi}\) | Branch phase current | A |
| \(u_k\) | Authorized device setpoints | Device-specific units |
| \(d_k\) | Demand, available renewable power, other disturbances | kW/kvar and stated forecasts |
| \(c_{ij},e_i,y_{ij}\) | Physical closure, bus energized, energized branch | Binary |
| \(\alpha_\ell\) | Served fraction of load block \(\ell\) | Binary for indivisible pickup; otherwise [0,1] |
| \(z,R\) | Measurement vector and measurement-error covariance | Sensor units and their products |

Electrical equations must use one consistent unit system. For example, \(V\) in volts and current in amperes produce power in VA, so divide by 1,000 when comparing to kVA. Per-unit equations require declared voltage and power bases and appropriately converted impedances. Objective weights carry the units needed to combine their terms; a kW objective is not an energy or monetary objective.

A common decision problem is

\[
\begin{aligned}
\min_{x_{0:H},u_{0:H-1},b_{0:H-1}}\quad &J(x,u,b;\hat d)\\
\text{subject to}\quad
&F_{\mathcal M}(x_k,u_k,b_k,\hat d_k)=0,\\
&g_{\mathcal M}(x_k,u_k,b_k)\leq0,\\
&(u_k,b_k)\in\mathcal A_{\mathrm{authorized}},\\
&x_{k+1}=f(x_k,u_k,\hat d_k)\quad\text{for modeled dynamic states}.
\end{aligned}
\tag{1}
\]

Here \(\mathcal M\) identifies the electrical model and its coverage; \(b\) contains any discrete decisions. Algebraic power-flow variables do not need an invented state-transition equation. Storage energy, tap movement, or control rate limits can supply temporal coupling when those devices are actually modeled.

Every numerical tool should return its input/model identity, candidate, solver status, objective, relevant residuals, modeled scope, and infeasibility or failure reason. The workflow separately checks data validity, action authorization, and electrical feasibility. Infeasibility, numerical failure, missing evidence, and unsupported model features are different outcomes. None should silently produce a control action.

### Shared electrical model

For a fixed topology, a compact exact steady-state relation is

\[
s^{\mathrm{net}}=\operatorname{diag}(V)\overline{Y(c)V},
\qquad s^{\mathrm{net}}=s^{\mathrm{generation}}-s^{\mathrm{demand}}.
\tag{2}
\]

The admittance and device models must represent the actual phase connections, transformers, shunts, and load characteristics. This nonlinear relation is the physical constraint; OpenDSS supplies a numerical circuit solution for given inputs. Calling a power-flow simulator does not by itself solve an OPF. [EPRI, OpenDSS power flow](https://opendss.epri.com/PowerFlow.html).

For a radial line segment on one voltage base, with downstream complex phase powers \(S_{ij}\), a useful three-phase approximation is

\[
w_j\simeq w_i-2\Re\!\left[
\overline{D_\beta}Z_{ij}D_\beta\overline{S_{ij}}\right],\qquad
D_\beta=\operatorname{diag}(1,e^{-\mathrm j2\pi/3},e^{\mathrm j2\pi/3}).
\tag{3}
\]

Use the phase-restricted matrices on one- or two-phase branches. With \(Z\) in ohms and \(S\) in VA, the voltage-drop term is in V². This uses approximately balanced phase-voltage ratios and neglects series-loss terms in the power balance; unequal phase powers and mutual impedance remain. It is not three independent copies of a balanced single-phase model. Transformer ratio/connection maps require separate treatment. [Gan and Low, 2014, Section V](https://arxiv.org/abs/1406.3054).

The implemented LinDistFlow backend retains the same feeder's MV phase network and aggregates LV devices to transformer-primary phases. Its checks cover **MV voltages and approximate MV line currents**. It omits LV voltage and transformer thermal constraints. A fresh OpenDSS audit is a separate, more detailed modeled check. Compare approximation error on common MV phases; classify additional LV failures as a coverage issue. Neither model is measured field truth. In the continuous P/Q companion, the voltage objective averages each backend's own modeled phase set, so both constraint coverage and objective coverage differ. Cross-backend control differences are not a pure measurement of approximation error.

## 1. Voltage support: three-phase Volt/VAR OPF within MPC

**Engineering question.** Which available active/reactive setpoints keep phase voltages and currents within limits while limiting curtailment and unnecessary device movement?

At time \(t\), estimate the operating state, form the next \(H\) forecasts, solve a constrained horizon problem, and propose only its first move. After the next measurement, update the estimate and forecasts and solve again. This repeated feedback procedure is receding-horizon MPC. A single horizon solve demonstrates its optimization step; it is not a measured closed-loop experiment. [Rawlings, Mayne, and Diehl, MPC textbook, author edition](https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-4th-printing.pdf).

One possible objective, chosen transparently for this lesson, is

\[
\begin{aligned}
J_V=\sum_{k=0}^{H-1}\bigg[&
c_v\sum_{i,\phi}(w^{\mathrm{pu}}_{i\phi,k}-1)^2
+c_c\Delta t\sum_{d}(P^{\mathrm{avail}}_{d,k}-P^g_{d,k})\\
&+c_l\Delta t P^{\mathrm{loss}}_k
+c_u\|D_u^{-1}(u_k-u_{k-1})\|_2^2\bigg].
\end{aligned}
\tag{4}
\]

Here \(\Delta t\) is in hours and powers are in kW for the energy terms. \(D_u\) scales each control by its declared range. The voltage and movement weights have objective-units per normalized squared quantity; \(c_c,c_l\) have objective-units/kWh. Zero weights are legitimate choices but must be reported. The objective expresses preferences; voltage and current limits remain separate constraints.

For every forecast interval impose (2), or a stated approximation such as (3), and

\[
\begin{gathered}
(V_i^{\min})^2\leq w_{i\phi,k}\leq(V_i^{\max})^2,\qquad
|I_{ij\phi,k}|\leq \rho_{ij,k}I^{\mathrm{rated}}_{ij\phi},\\
0\leq P^g_{d,k}\leq P^{\mathrm{avail}}_{d,k},\qquad
(P^g_{d,k})^2+(Q^g_{d,k})^2\leq(S_d^{\mathrm{rated}})^2,\\
Q_d^{\min}\leq Q^g_{d,k}\leq Q_d^{\max},\qquad
|u_k-u_{k-1}|\leq\Delta u^{\max}.
\end{gathered}
\tag{5}
\]

\(\rho\in(0,1]\) is an explicitly imposed current allowance, not a learned rating. Inverter circles here are per device; enforce phase allocation and shared-device coupling appropriate to its hardware. They do not authorize arbitrary independent per-phase control. Tap/capacitor integers, transformer limits, and storage energy dynamics belong in the problem when those assets are controllable. For storage, for example, \(E_{k+1}=E_k+\eta_cP^c_k\Delta t-P^d_k\Delta t/\eta_d\), with energy/power bounds and suitable charge/discharge logic.

**Solution method.** Exact three-phase AC constraints lead to a nonlinear OPF, ordinarily requiring careful initialization and feasibility checks; a local solution is not a global-optimality certificate. A linearized electrical model with quadratic cost and affine bounds yields a QP; exact circular inverter constraints instead yield a conic or convex quadratically constrained problem. Discrete tap choices change the class again. Sequential QP rebuilds sensitivities around the latest operating point and needs step limits and fresh nonlinear verification. Model predictive voltage control with explicit treatment of renewable uncertainty has established research examples; nominal MPC alone has no automatic robustness guarantee. [Maharjan, Khambadkone, and Peng, 2021](https://doi.org/10.1109/TSTE.2020.3001115).

**Agent contribution and fair comparison.** Give both supervisors the same measurements, forecast, objective, device limits, optimization tool, and fresh electrical verifier. The agent may choose a permitted tool, request an updated solve, or explain a rejection. DRL may supply a candidate or warm start, but its action values are not constraints or physical evidence. Compare accepted objective, constraint failures, repair success, and total latency. If a deterministic adaptive supervisor achieves the same result, report that equality.

**Connection to the executable lessons.** The original `stage_workflow.py` uses eight shared PV-cap choices and a three-step Bellman dynamic program. Its reward is normalized PV production minus cap movement, not (4); reactive power is not independently optimized. It finds the optimum of that small finite-action problem. Each recorded case executes a proposed first move, not a complete time-series MPC loop. The separate `standard_formulations.py` companion solves local QPs in two shared P/Q participation variables, uses an inscribed inverter-capability polygon, and checks candidate steps through fresh selected-backend solves. It is restricted one-step Volt/VAR optimization; it does not execute repeated forecasting or a multi-step P/Q MPC loop. Its actual normalized objective and stopping conditions are returned in the results.

**Experiment.** Start with adequate reactive headroom, then lower the allowed current or inverter capacity. Plot each phase's voltage, current utilization, inverter P–Q point, curtailed energy over any executed time series, and control movement. Distinguish an infeasible optimization problem from a feasible solution rejected by the detailed simulator. Record the model domain of every voltage plot.

## 2. Service restoration: weighted load pickup with switching and network constraints

**Engineering question.** After isolating damaged equipment, which available connections and load blocks can be energized while preserving an admissible electrical network?

A time-indexed objective is

\[
\max\quad
\sum_{k=0}^{H-1}\Delta t\sum_{\ell\in\mathcal L}
\omega_\ell P^d_{\ell,k}\alpha_{\ell,k}
-\lambda_{\mathrm{sw}}\sum_{k,(i,j)}\delta_{ij,k}.
\tag{6}
\]

The first term is weighted served kWh when \(P^d\) is kW. \(\omega_\ell\) is an explicitly assigned priority; \(\delta\geq0\) counts physical switching changes and \(\lambda_{\mathrm{sw}}>0\) has corresponding weighted-kWh/operation units. For one snapshot, use weighted served kW and state that time-to-restoration and energy are not measured. Lexicographic maximization of critical service, total service, then minimal switching avoids implying that a finite weight always guarantees strict priority. Unbalanced sequential restoration with coordinated switch, generator, and load decisions has been formulated as MILP in the primary literature. [Chen et al., 2018](https://doi.org/10.1109/TPWRS.2017.2720122).

**Decision variables.** \(\alpha_\ell\) is binary for a switchable load block. Use a continuous fraction only for a physically curtailable load. \(c_{ij}\) is physical branch closure; \(e_i\) is bus energization; \(y_{ij}\) means a closed, energized branch. Separate these: a closed branch in a dead section is not a switching operation or part of the energized tree.

For a connected single-source energized network with root 0, one transparent topology formulation is

\[
\begin{gathered}
e_0=1,\qquad \alpha_\ell\leq e_{i(\ell)},\qquad
|e_i-e_j|\leq1-c_{ij},\\
y_{ij}\leq c_{ij},\quad y_{ij}\leq e_i,\quad y_{ij}\leq e_j,\quad
y_{ij}\geq c_{ij}+e_i+e_j-2,\\
\sum_{j:(j,i)}f_{ji}-\sum_{j:(i,j)}f_{ij}=e_i\quad(i\ne0),\\
\sum_{j:(0,j)}f_{0j}-\sum_{j:(j,0)}f_{j0}=\sum_{i\ne0}e_i,\\
-M y_{ij}\leq f_{ij}\leq M y_{ij},\qquad
\sum_{(i,j)\in\mathcal E}y_{ij}=\sum_i e_i-1.
\end{gathered}
\tag{7}
\]

Use an arbitrary fixed orientation for each branch; signed \(f\) is a fictitious connectivity commodity, not kW. \(M=|\mathcal N|-1\) suffices here. Each energized non-root bus consumes one unit, forcing a path to the source. Together with the edge count this makes a tree. Edge count alone permits disconnected cycles. Multiple intentional islands require a forest formulation with explicitly eligible energized roots; a grid-following PV inverter is not automatically an island-forming source. [Wang et al., radiality and single-commodity flow](https://arxiv.org/abs/1912.05185).

Add the following physical and operational constraints:

\[
\begin{gathered}
c_{ij}=0\quad\text{for isolated faults or forbidden closures},\qquad
c_{ij}=c^{\mathrm{fixed}}_{ij}\quad\text{for non-switchable branches},\\
\delta_{ij,k}\geq c_{ij,k}-c_{ij,k-1},\qquad
\delta_{ij,k}\geq c_{ij,k-1}-c_{ij,k},\\
s^{\mathrm{served}}_{\ell,k}=\alpha_{\ell,k}s^d_{\ell,k},\qquad
F_{\mathcal M}(V,S,I,c,s^{\mathrm{served}},s^g)=0,\\
(V_i^{\min})^2e_i\leq w_{i\phi}\leq(V_i^{\max})^2e_i,\qquad
|I_{ij\phi}|\leq I^{\mathrm{allowed}}_{ij\phi}y_{ij}.
\end{gathered}
\tag{8}
\]

The electrical model must gate branch equations correctly: zero flow on an unenergized connection and valid voltage-drop equations on an energized one. Generator/inverter capability, source capacity, transformer limits, available controls, and any required phase-specific load service accompany (8). A multiperiod problem also needs actual switching times, startup/energy limits, and cold-load-pickup assumptions if those effects are claimed.

**Solution method and interpretation.** Affine power-flow approximations and polyhedral capability limits with binary decisions produce MILP, solved using branch-and-bound/cuts. Retaining second-order cones produces MISOCP; a conic relaxation is not automatically exact. Exact AC equations produce a nonconvex mixed-integer problem. Report the formulation, incumbent feasibility, time limit, bound, and optimality gap. A final static feasible topology does not certify the entire switching sequence, protection coordination, synchronism, or transient stability.

**Agent contribution and fair comparison.** The agent gathers the allowed topology/fault information, calls the restoration optimizer, requests a different authorized scenario after a rejection, and presents a switching proposal for review. Compare it with a deterministic supervisor using the same optimizer and constraints. Language reasoning does not replace the graph proof, branch-flow constraints, or fresh electrical check.

**Connection to the executable lessons.** The original workflow enumerates two synthetic bypasses and a finite list of shedding fractions. Critical loads are a reproducible synthetic priority subset. It maximizes `served_kw + 9 * critical_served_kw`, so critical load has total weight 10; it proves only best-in-catalog selection. The two bypasses are teaching overlays, not verified utility switching assets. The separate six-node MILP companion introduces genuine binary pickup/connectivity decisions and an independently enumerated optimum. Its secondary objective minimizes energized branches, rather than physical switching changes from a prior topology. Its active-power branch capacities are not a full three-phase voltage/current model of the Greensboro feeder.

**Experiment.** Keep the fault fixed and reduce the available source or tie capacity. Plot energized topology, picked-up load blocks by priority, service versus capacity, and the MILP bound/gap. Then change the allowed branch set to demonstrate infeasibility and review. For a full electrical claim, evaluate the selected configuration in the stated three-phase simulator and show any constraints outside the optimization's approximation.

## 3. Cyber-attack response: state estimation, bad-data screening, and constrained redispatch

**Engineering question.** Is the measurement set consistent with the trusted model, which measurements require investigation, and is sufficient trustworthy information available to recommend a constrained redispatch?

### Estimate first, then test residuals

Use an explicit measurement model

\[
z=h(x;\tau)+\epsilon+a,\qquad \epsilon\sim\mathcal N(0,R),\qquad
\hat x=\arg\min_x(z-h(x;\tau))^TR^{-1}(z-h(x;\tau)).
\tag{9}
\]

\(\tau\) is the assumed topology/parameter set and \(a\) represents corrupted measurements. The state may contain phase-voltage magnitudes/angles or rectangular components after fixing reference freedoms. Measurements may mix voltage, current, and P/Q; \(R\) accounts for their units and uncertainty. Check positive-definite covariance, finite data, time alignment, and local observability. The Jacobian \(H=\partial h/\partial x\) must have full column rank in the free-state coordinates. Nonlinear WLS commonly uses iterative linearization; the linear model \(h(x)=Hx\) permits a direct weighted least-squares solve. [Schweppe and Wildes, 1970](https://ieeexplore.ieee.org/abstract/document/4074022).

With residual \(r=z-h(\hat x)\), the global statistic and threshold are

\[
J_{\mathrm{SE}}=r^TR^{-1}r,\qquad
J_{\mathrm{SE}}>\chi^2_{m-n_x,\,1-\alpha_{\mathrm{FA}}}.
\tag{10}
\]

Here \(m\) is the number of scalar measurements, \(n_x\) the number of identifiable free states, and \(\alpha_{\mathrm{FA}}\) a predeclared false-alarm probability. The chi-square distribution is exact for the full-rank linear Gaussian model and approximate under local nonlinear linearization. It is not justified by an arbitrary residual threshold, an unobservable model, or unknown sensor variances. The test flags inconsistency; it does not identify its cause as a cyberattack. [PMDSE authors, chi-square implementation and assumptions](https://electa-git.github.io/PowerModelsDistributionStateEstimation.jl/v0.4/bad_data/).

For an unconstrained locally linear WLS problem,

\[
G=H^TR^{-1}H,\qquad
\Omega=R-HG^{-1}H^T,\qquad
r_i^N=\frac{|r_i|}{\sqrt{\Omega_{ii}}}.
\tag{11}
\]

The largest normalized residual provides a suspect measurement for further checks. Compute it using residual covariance, not just the raw sensor standard deviation. A zero or tiny \(\Omega_{ii}\) cannot be divided into a usable test statistic; critical measurements may have no residual redundancy. Recheck observability before quarantine and recompute estimation and test thresholds after removal. Multiple interacting errors can mislead localization. These are established residual-analysis concerns. [Handschin et al., 1975, author-provided manuscript](https://www.researchgate.net/publication/3458147_Bad_data_analysis_for_power_system_state_estimation).

Numerically, solve weighted least-squares systems using suitable factorizations rather than forming explicit inverses. A localization threshold is a separate design choice from the global false-alarm level. Testing many residuals changes the family-wide alarm rate; calibrate or bound it rather than treating a per-measurement threshold as a system-wide guarantee. Hard equality constraints in a different estimator require the corresponding constrained covariance and effective degrees of freedom.

### The negative control: a residual-preserving attack

For the linear model, if an allowed corruption has \(a=Hc\), then

\[
z'=z+Hc,\qquad \hat x'=\hat x+c,\qquad
z'-H\hat x'=z-H\hat x.
\tag{12}
\]

Thus a biased state can have exactly the same residual statistics. With limited access, an attack must also satisfy \(\operatorname{supp}(Hc)\subseteq\mathcal A\), the compromised measurement set. A sparse attack is possible only when those structural constraints permit it. For protected channels \(\mathcal T\), require \(H_{\mathcal T}c=0\); a full-column-rank trusted submatrix rules out nonzero shifts of this form. Nonlinear attacks require their own model assumptions; the linear demonstration is not universal attack construction or detection. [Liu, Ning, and Reiter, 2009](https://reitermk.github.io/papers/2009/CCS1.pdf).

Show this negative control next to an isolated bad measurement. It demonstrates why a low residual cannot establish data authenticity. Timestamps, signed provenance, topology records, independent sensing, and operator confirmation address different evidence questions; calling several language agents does not create new independent measurements.

### Response: restore trustworthy estimation before recommending redispatch

After evidence checks, construct a declared trusted/retained set \(\mathcal T\). Do not infer trust solely because a residual is small. Re-estimate using that set and recheck observability and uncertainty. If an adequately supported state/forecast is available, solve a redispatch problem such as

\[
\begin{aligned}
\min_{u,x}\quad &\|D_u^{-1}(u-u_{\mathrm{last}})\|_W^2
+c_{\mathrm{curt}}\sum_d(P_d^{\mathrm{avail}}-P_d^g)\\
\text{subject to}\quad
&F_{\mathcal M}(x,u,\hat d_{\mathcal T})=0,\quad
g_{\mathcal M}(x,u)\leq0,\quad u\in\mathcal A_{\mathrm{authorized}}.
\end{aligned}
\tag{13}
\]

This is the voltage-support OPF with a response-specific movement/curtailment preference, not a new proof that the data are clean. A robust extension enforces constraints for every disturbance in a defensible uncertainty set, or a stochastic formulation uses a justified distribution. An arbitrary tightened limit alone does not supply that guarantee. No trustworthy observable input, no valid uncertainty set when required, or no feasible plan means **REVIEW/no new action**. Holding a previous setpoint is not presumed safe after an unknown physical change.

**Agent contribution and fair comparison.** The agent routes the case through data checks, WLS, localization, trusted re-estimation, redispatch, and fresh verification. The numerical tests remain authoritative. Compare against the same deterministic incident-response sequence. Report state error in synthetic experiments, false alarms, missed attacks including the stealth negative control, lost observability, verified redispatch, and latency. Detection rate needs a declared attack/noise distribution and repeated trials; a few scripted scenarios support only those individual outcomes.

**Connection to the executable lessons.** The original awareness function compares two synthetic voltage extrema, checks timestamps/topology identity, and rejects a 0.03 p.u. injected bias. It is not WLS, chi-square screening, or an empirical cyber-detection benchmark. The separate WLS companion uses a four-bus DC model with three unknown voltage angles, declared covariance, isolated corruption, and a stealth \(Hc\) negative control. It actually links the estimated state to a scalar constrained redispatch, and evaluates that control against the synthetic true state. Recovery assumes three protected angle measurements; their exactly determined estimate has no residual degrees of freedom for chi-square testing. This is a complete estimation-to-control illustration within that DC model, not a three-phase Greensboro state estimator or AC redispatch. Its fixed planning margin is an engineering choice, not a calibrated uncertainty guarantee.

## What the three-use-case comparison can establish

| Comparison question | Keep identical | Measure | Do not infer |
|---|---|---|---|
| Does orchestration help complete a verified task? | Numerical tools, data, constraints, attempt budget | Completion, handoff, rejected/accepted proposals, tool/LLM calls, latency | An LLM improves the underlying optimum |
| How does model choice affect the recommendation? | Feeder inputs, scenario, objective, control permissions | Common-MV voltage/current errors; separate whole-model violations | MV-only acceptance certifies omitted LV devices |
| Does repair help after a rejected or unavailable tool? | Initial proposal and allowed fallbacks | Recovery success versus single-pass and adaptive deterministic rules | Repair is uniquely enabled by language models |
| Does data screening prevent an unsupported action? | Corruption/noise fixtures and trust assumptions | Bad-data flags, missed attacks, observability, no-action decisions | A residual pass proves the absence of a cyberattack |

These are three applications of one workflow: **validate evidence → formulate → solve or propose → simulate → verify → repair or review → explain → operator acknowledgment**. Acknowledgment records review of a specific recommendation and its limits. This tutorial does not dispatch physical equipment.
