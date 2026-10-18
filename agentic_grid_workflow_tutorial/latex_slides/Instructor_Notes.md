# Instructor notes: core workshop and optional code routes

Begin with Graph_Workflow_Lab.ipynb (G0–G5), then use Classroom_Labs.ipynb (L0–L12) for the engineering cases. G is a real LangGraph toy example. L uses the existing custom Python engineering workflow. All other notebook checkpoints in the technical appendix are explicitly separate recorded experiments or detailed method companions. Implementation excerpts are exact source copies, not standalone cells.

Each logical frame can have several presentation pages for progressive reveals. The handout shows one completed page per frame. Stop the taught route after frame 72; the technical appendix follows as one separate block. Every frame has a visible Next bridge and a short PDF fade transition. Reveal pages work with normal page advance; fade support depends on the viewer.

72 core frames form the 180-minute route, including a ten-minute break; 0 optional detail frames and 68 reference frames are outside that timed route.

## Frame 1: One operator, three decisions, one evidence trail

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 1–2. Handout page: 1.

Visible transition: What will we build in three hours?

0--2 min. Invite two answers: what evidence makes a recommendation reviewable? Reveal the goal after their answers. Cases use a synthetic feeder and small teaching fixtures. Spoken bridge: We will build that evidence trail in small pieces, then test it on three different decisions.

## Frame 2: A three-hour route from diagrams to operator review

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 3. Handout page: 2.

Visible transition: Which part of the software makes a decision?

2--3 min. Installation is a prerequisite. Graph_Workflow_Lab teaches orchestration; Classroom_Labs contains engineering exercises. Saved responses are actual previous calls, with previous-call latency. Spoken bridge: Before using any package, distinguish a tool from the component that chooses to call it.

## Frame 3: Tool, agent and orchestrator have different jobs

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 4–5. Handout page: 3.

Visible transition: How do we draw these responsibilities clearly?

3--5 min. Trace request and result. Dashed line means execution rules here. Distinguish language-selected next actions from a fixed script; both can share tools and safeguards. A graph alone implies neither AI nor independent models. Spoken bridge: We need a small visual vocabulary before those boxes become a workflow.

## Frame 4: Read the diagram: operation, state, dependency and decision

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 6–7. Handout page: 4.

Visible transition: Which operations could run independently?

5--6 min. Name each symbol: operation A, record s and routing rule r. Later physical figures use edges as feeder connections; these are computational arrows. Spoken bridge: Once dependencies are visible, we can see where work may branch and where it must wait.

## Frame 5: A dependency DAG can split work and join the evidence

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 8–10. Handout page: 5.

Visible transition: Which execution orders preserve every dependency?

6--8 min. Reveal input, two checks, then join. Ask whether one branch supplies a complete verdict. Independent work may overlap; this guarantees neither speedup nor independent errors. Our engineering adapters are not claimed to run concurrently. Spoken bridge: Splitting work still leaves an ordering rule, and more than one order can satisfy it.

## Frame 6: Topological order puts every prerequisite before its consumer

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 11–12. Handout page: 6.

Visible transition: What changes when a failed check requests a retry?

8--10 min. Pause before revealing. Ask why D cannot precede C. Topological order is a dependency-respecting list, not measured runtime. Braces group independent work. Spoken bridge: A repair step introduces a backward arrow, so we must change our description of the graph.

## Frame 7: A retry loop is a graph with a cycle, not a DAG

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 13–14. Handout page: 7.

Visible transition: What information must survive every node?

10--12 min. Trace success, then reveal repair and exhaustion. Identify the cyclic arrow. A finite unrolled trace can be acyclic although the program has a loop. Tool timeouts are separate from a retry count. Spoken bridge: To decide whether another retry is allowed, the next node must read a reliable shared record.

## Frame 8: Typed state is the record carried through the graph

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 15. Handout page: 8.

Visible transition: Should a new result replace or append to a field?

12--14 min. Treat state as a laboratory record, not a chat transcript. TypedDict describes keys/types but performs no runtime validation itself. Applications still check values and units. Spoken bridge: Updating a scalar result and preserving a history require different merge rules.

## Frame 9: A reducer states how a field absorbs new information

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 16–17. Handout page: 9.

Visible transition: How does the record choose the next edge?

14--16 min. Reveal after prediction. List addition appends; it is not averaging or voting. Empty appended lists do not erase history. The G trace is sequential; parallel order needs interpretation. Concurrent writes to a non-reduced field can raise an error. Spoken bridge: Once the record is updated, a routing function can select the next permitted operation.

## Frame 10: Conditional routing makes the next action explicit

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 18–20. Handout page: 10.

Visible transition: Where can a human pause this process?

16--18 min. Read success, remaining budget, then exhaustion as mutually exclusive branches. The G code returns report on success; the default report function records TOY_READY. G5 replaces that function with human review. Routing is deterministic here; language-selected refinements still face the same gate. Spoken bridge: A ready proposal can still require a person, so the program needs a resumable pause.

## Frame 11: A checkpoint and an interrupt make review resumable

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 21–22. Handout page: 11.

Visible transition: How do these graph ideas map to our five stages?

18--20 min. Stop at pause before revealing resume. A thread ID groups execution state, not operator credentials. The toy's in-memory saver does not survive process loss. A repeated node must not duplicate side effects. Spoken bridge: These are software mechanisms; the proposal assigns them to five engineering responsibilities.

## Frame 12: Five proposed stages share one candidate and its evidence

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 23–24. Handout page: 12.

Visible transition: Which returned facts should a verifier trust?

20--22 min. Trace a candidate, then reveal repair. Planners vary by case: MPC, MILP or estimation/control. Llama supports bounded interpretation and trial choice; it does not replace equations. Main implementation is custom Python, separate from the toy. Spoken bridge: A well-connected graph still needs a precise rule for accepting the facts passed between stages.

## Frame 13: Typed, current and feasible are three separate claims

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 25–26. Handout page: 13.

Visible transition: Which prior frameworks teach these mechanisms?

22--23 min. Ask which check rejects the example. A schema, matching hash and converged solve answer different questions. Spoken bridge: Existing power-system frameworks contribute useful mechanisms, so our comparison should describe those contributions precisely.

## Frame 14: Recent frameworks provide mechanisms we can test

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 27. Handout page: 14.

Visible transition: What does a comparison checkmark actually mean?

23--24 min. Name one mechanism per row. PowerAgent is a published roadmap and ecosystem; other cited sources are preprints. The benchmark is not a controller. Skills, governance and scaling return near the end. Spoken bridge: A capability matrix is useful only when its symbols preserve these qualifications.

## Frame 15: A capability tick describes scope, not superiority

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 28. Handout page: 15.

Visible transition: Can we run the graph mechanics without an LLM?

24--25 min. Tools means execution, feedback means results; checks and review retain final-column qualifications. Readback is not authenticated field approval. No common cross-paper leaderboard is claimed. Spoken bridge: We can learn the control-flow machinery with transparent arithmetic before asking Llama or an electrical solver to participate.

## Frame 16: The G lab makes every state transition visible

Route: **core**. Notebook: Graph_Workflow_Lab.ipynb.

Presentation pages: 29. Handout page: 16.

Visible transition: How is this diagram expressed in Python state?

25--26 min. G0 confirms installed version. The response law is illustrative arithmetic; execution is real LangGraph and needs neither Ollama nor OpenDSS. Main engineering notebooks are custom Python. Spoken bridge: First the code states what data exists, then it states which node may change it.

## Frame 17: G1: give the graph a record and an event history

Route: **core**. Notebook: Graph_Workflow_Lab.ipynb.

Presentation pages: 30–31. Handout page: 17.

Visible transition: Where does the graph decide to stop or retry?

26--27 min. Run G1 and point to command, limit and trace. Trace supports debugging; it is not a private reasoning transcript or cryptographic audit log. Spoken bridge: Node functions now have a place to record facts, and a router can act on those facts.

## Frame 18: G2--G3: bind node functions to permitted routes

Route: **core**. Notebook: Graph_Workflow_Lab.ipynb.

Presentation pages: 32–33. Handout page: 18.

Visible transition: Will every initial command reach the ready node?

27--29 min. Run full G2 then G3. Match an edge to the loop drawing. Compilation checks structural requirements; it does not prove physics or every condition. Ask what fixes the retry budget. Spoken bridge: Three initial states will show success, successful repair and a legitimate stop without success.

## Frame 19: G4: predict three paths before running the graph

Route: **core**. Notebook: Graph_Workflow_Lab.ipynb.

Presentation pages: 34–35. Handout page: 19.

Visible transition: How does a ready result wait for a person?

29--31 min. Allow two minutes, reveal after predictions. Repaired commands become 0.50 and 0.65. G4 assertions describe its original three cases; use a separate scratch cell for modified inputs. Comparisons use explicit tolerance. The baseline holds controller functions fixed: graph orchestration changes inspectability, not the physical solution here. Spoken bridge: Ready means eligible for the next review step, so let us make that pause observable.

## Frame 20: G5: pause, inspect the checkpoint, then resume review

Route: **core**. Notebook: Graph_Workflow_Lab.ipynb.

Presentation pages: 36–37. Handout page: 20.

Visible transition: Can saved evidence survive a changed request?

31--34 min. G5 contains a real interrupt and then automatically supplies a scripted simulated response in the same cell. Inspect its printed pre-resume snapshot before discussing the final output. For a live teaching pause, execute lines1--17, then18--21 separately. In-memory state lasts within the kernel. No dispatch endpoint exists. The interrupted node restarts; earlier code must tolerate replay. Paused status is TOY_NEW, not TOY_READY. Spoken bridge: Even a carefully saved result loses relevance when the request or command changes.

## Frame 21: L1: a changed request needs fresh evidence

Route: **core**. Notebook: Classroom_Labs.ipynb.

Presentation pages: 38–39. Handout page: 21.

Visible transition: Which method should propose the real command?

34--37 min. Three minutes include setup, prediction, run and explanation. Load changes 1.00 to 1.10 and revision1 to2; command changes0.25 to0.50. Reveal after prediction. Fixed and LLM supervisors can both use this guard. Spoken bridge: Binding identifies the right calculation; we still need a numerical method that produces a useful action.

## Frame 22: Model-based planning and model-free learning supply proposals

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 40–41. Handout page: 22.

Visible transition: What must the voltage experiment compare fairly?

37--39 min. Define model predictive control, soft actor-critic and proximal policy optimization. Model-free learning may use simulator experience. Actor training cost is separate; class runs inference. Other cases need their own formulations. Spoken bridge: Both proposals can now enter one experiment with the same state and acceptance rules.

## Frame 23: From graph mechanics to a physical voltage decision

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 42–43. Handout page: 23.

Visible transition: Which inverter action supports this feeder?

39--40 min. Ask what the G toy taught and what it could not establish. It taught state, routing, repair and pause; it did not solve a feeder. Return to custom Python and numerical models. Spoken bridge: We now leave the arithmetic demonstrator and ask the selected Greensboro feeder model to evaluate an inverter command.

## Frame 24: Voltage support: choose the next action, then test its consequences

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 44–45. Handout page: 24.

Visible transition: Which methods can propose the same physical action?

40--42 min. Transition: We now have a valid tool request. What numerical tool should produce the control? Ask participants to name one constraint that the map does not show. Mention synthetic geography and artificial critical-load labels. This map supplies context, not evidence of utility deployment. Spoken bridge: Which methods can propose the same physical action?

## Frame 25: Model-based and model-free methods answer the same action question

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 46–48. Handout page: 25.

Visible transition: How does a planner use a forecast before acting?

42--44 min. Model-free describes how the policy is learned, not an absence of engineering models in the full system. The SAC actor was trained using a simulator. PPO can represent continuous actions but is not the trained actor used in this experiment. Keep inference latency distinct from training cost. Spoken bridge: How does a planner use a forecast before acting?

## Frame 26: MPC plans several moves and applies only the first

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 49–51. Handout page: 26.

Visible transition: What exactly should one control move minimize?

44--46 min. Derive receding horizon verbally before showing code. Ask which future action is actually used now. The generalized dynamic equation explains MPC, while the actual tutorial uses algebraic power-flow solves at each forecast step. No terminal-set or closed-loop stability guarantee is claimed. Spoken bridge: What exactly should one control move minimize?

## Frame 27: Make the objective interpretable before optimizing it

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 52–54. Handout page: 27.

Visible transition: Which constraints can overrule a low cost?

46--48 min. Define every symbol; no one should infer the sign convention. The supplied available active power equals the inverter kVA assumption verified in the adapter. The policy does not choose 930 independent inverter settings. Ask: if we reduce reactive effort, can voltage constraints become worse even though one cost term improves? Yes. Spoken bridge: Which constraints can overrule a low cost?

## Frame 28: A low objective is useful only inside the admissible set

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 55–57. Handout page: 28.

Visible transition: Which constraints can our chosen model see?

48--50 min. Show the question before revealing. Explain why solver convergence, good objective and feasibility are three different statements. Constants such as voltage bounds and current derating must come from the selected experiment contract, never from generated prose. The local optimizer can be suboptimal; fresh checking is essential. Spoken bridge: Which constraints can our chosen model see?

## Frame 29: LinDistFlow3 and OpenDSS expose different parts of this feeder

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 58–60. Handout page: 29.

Visible transition: How does a learned actor produce an alternative?

50--52 min. Do not treat agreement of two differently scoped models as a pure accuracy benchmark. The equation matches the fixed-phase phasor closure in src/lindistflow3.py. Mutual impedance coupling is retained. Currents use the fixed 1.03-pu reference; losses are diagnostic and are omitted from the branch balance. Model fidelity and constraint coverage are separate experimental factors. Spoken bridge: How does a learned actor produce an alternative?

## Frame 30: SAC learns a continuous proposal; verification remains a separate step

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 61–63. Handout page: 30.

Visible transition: What changes when we perturb the demand?

52--53 min. Keep this to one minute; detailed actor and critic training go to the appendix. SAC and the LLM-response selector solve different learning problems. The classroom performs fresh inference with the saved actor weights and freshly checks the action. It does not retrain SAC. The archived training environment uses a fitted cubic surrogate rather than 12,000 full power-flow solves. Spoken bridge: What changes when we perturb the demand?

## Frame 31: Lab 2: change demand and compare the same two numerical actions

Route: **core**. Notebook: Classroom_Labs.ipynb.

Presentation pages: 64–65. Handout page: 31.

Visible transition: Which margins explain the numerical result?

53--60 min. Allow seven minutes including questions. Run L2 as a full cell. Students work in pairs: one predicts, one executes. Ask them to point to a metric supporting their answer. If local setup fails, use the executed output and edit the prediction worksheet rather than waiting for installs. Spoken bridge: Which margins explain the numerical result?

## Frame 32: Read the margins before deciding which controller was better

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 66–68. Handout page: 32.

Visible transition: What can a language model add to this evidence?

60--63 min. This figure is generated by the default L2 execution, not invented to favor agentic AI. A proposal can be feasible but much worse on cost. Ask whether the result comes from MPC, SAC, a better model or orchestration. Keep causal attribution separate. Spoken bridge: What can a language model add to this evidence?

## Frame 33: Actual Llama responses can be useful and still contain unsupported claims

Route: **core**. Notebook: Classroom_Labs.ipynb.

Presentation pages: 69–70. Handout page: 33.

Visible transition: How do different replies become comparable actions?

63--68 min. Run L3 and allow students to identify one supported and one unsupported clause before revealing. These are short exact excerpts; full public responses are in the notebook. They are not private chain-of-thought. Actual times were recorded in September, not measured by the new cached display cell. Llama is the model family; Ollama is the local runtime. Spoken bridge: How do different replies become comparable actions?

## Frame 34: Voting selects one physical operation, not the most persuasive paragraph

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 71–73. Handout page: 34.

Visible transition: Can feedback teach us which operation to test?

68--70 min. Explain that a predetermined SHA tie-break is repeatability, not engineering preference. Correlated models can share a mistaken assumption. The all-responses comparator receives more numerical trials and must be labeled as extra budget. Voting cannot lower limits or invent permissions. Spoken bridge: Can feedback teach us which operation to test?

## Frame 35: The LLM optimizer can learn which proposed operation to test

Route: **core**. Notebook: Classroom_Labs.ipynb.

Presentation pages: 74–76. Handout page: 35.

Visible transition: What reward should the selector receive?

70--73 min. First describe select, observe, update in words. Then reveal the equations. Training has an uncertainty bonus; frozen classroom evaluation uses predicted reward only. The selected-feedback simulator replay is not observational deployment data. No future score, gate outcome or held-out feedback may enter selection features. Spoken bridge: What reward should the selector receive?

## Frame 36: Reward learning and safety checking have different jobs

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 77–79. Handout page: 36.

Visible transition: Does the learned selector outperform a simpler rule?

73--76 min. Reserve the three minutes. Training and test files are separate. All permitted trial outcomes exist for audit, but training consumes only selected feedback. Ask how changing the reward scaling changes learning without changing the physical limits. The posthoc simple-rule diagnostic is not a predeclared baseline. Spoken bridge: Does the learned selector outperform a simpler rule?

## Frame 37: A rigorous result can show that the extra agent adds no benefit

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 80–82. Handout page: 37.

Visible transition: Will the same action pass a broader model?

76--78 min. Do not hide the negative result. The denominator is 12 scenarios, not number of model calls. The measured time is reconstructed serial accounting from actual components. A claim that agentic AI improves optimization must survive the identical-tool fixed-rule baseline. Explain why this negative result is a valuable research lesson. Spoken bridge: Will the same action pass a broader model?

## Frame 38: Lab 5: ask a broader model to audit the recommendation

Route: **core**. Notebook: Classroom_Labs.ipynb.

Presentation pages: 83–85. Handout page: 38.

Visible transition: Which stage produced each part of the evidence?

78--80 min. Default performs a fresh MV audit of the archived original action. If OpenDSS is installed, enable the fresh AC check and separate AC replanning. The 12-case table on this slide is the separately labeled historical pilot, not output from this one-case cell. Both audiences use the same tool contract. Explain that different bus sets also change the voltage term in the objective, so cross-model objective values are not a pure solver ranking. Spoken bridge: Which stage produced each part of the evidence?

## Frame 39: Voltage support: what each stage contributed

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 86–89. Handout page: 39.

Visible transition: What changes when the decision is a topology, not a setpoint?

80--82 min. Ask one participant to summarize the actual benefit and one limitation. The language layer provides bounded interpretation and trial selection; engineering methods produce the physical evidence. Transition to topology and discrete optimization. This completes voltage without switching to another historical protocol mid-lesson. Spoken bridge: What changes when the decision is a topology, not a setpoint?

## Frame 40: Ten-minute break: 82--92 minutes

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 90. Handout page: 40.

Visible transition: After the break, which loads should the remaining paths support?

82--92 minutes. Take the full break. Resume at restoration. This frame is inside the taught route; appendix material must not consume the break.

## Frame 41: After a fault, reconnecting service is a discrete decision

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 91–93. Handout page: 41.

Visible transition: How do we express pickup, energization and connectivity?

92--95 min. Resume from the break with a physical question. Draw attention to node 4 as a transit node. Ask for predictions before revealing. The faulted edge is unavailable, not merely expensive. Dashed green ties are choices, not a preselected solution. Spoken bridge: How do we express pickup, energization and connectivity?

## Frame 42: Restoration MILP: choose service while preserving a source path

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 94–97. Handout page: 42.

Visible transition: What makes the comparison with a baseline fair?

95--99 min. Spend four minutes connecting each equation to the picture. Edge count alone is insufficient. Fictitious flow is a graph certificate, not electricity. The source supplies commodity and electrical balances; non-source equations shown for clarity. The exact model is solved by SciPy/HiGHS and independently enumerated. A secondary solve preserves the optimal weighted service, then minimizes energized branch count plus a 0.001 edge-index tie-break. This is not a count of switching operations relative to an initial topology. Spoken bridge: What makes the comparison with a baseline fair?

## Frame 43: A fair baseline must optimize the same feasible network

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 98–100. Handout page: 43.

Visible transition: Where should the service curve change as capacity shrinks?

99--102 min. The new lab baseline solves the same constraints with unit weights. It is stronger and clearer than an arbitrary greedy ordering. Finite weight ten is not a universal lexicographic priority guarantee. Ask how to implement strict critical-first priority: solve two stages or impose a verified primary objective bound. Spoken bridge: Where should the service curve change as capacity shrinks?

## Frame 44: Lab 6: predict the effect of reducing tie capacity

Route: **core**. Notebook: Classroom_Labs.ipynb.

Presentation pages: 101–102. Handout page: 44.

Visible transition: Why can several ratings produce the same service?

102--110 min. Includes the beginning of the restoration lab block. Pair exercise: one follows the source path, one checks branch capacities. Do not infer proportional service reduction from proportional capacity reduction. If ties occur, compare objective and feasibility rather than insisting on identical edge IDs. Spoken bridge: Why can several ratings produce the same service?

## Frame 45: Discrete service can stay constant while a rating changes

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 103–105. Handout page: 45.

Visible transition: Can this result still be used after the topology changes?

110--113 min. Plot is generated from fresh solves. Ask students to locate a capacity at which the two objectives favor different critical service, if such a point appears in the executed sweep. A tie is also an informative result; do not invent a benefit. Review one selected branch-flow constraint numerically. Spoken bridge: Can this result still be used after the topology changes?

## Frame 46: Lab 7: a changed topology needs a new evidence record

Route: **core**. Notebook: Classroom_Labs.ipynb.

Presentation pages: 106–108. Handout page: 46.

Visible transition: Which stage must repair a stale handoff?

113--116 min. The intended outcome is rejection of stale evidence, not merely producing a warning in prose. Ask which fields should change when the topology changes. This experiment demonstrates a deterministic architectural property available to both fixed and LLM-based supervisors. Spoken bridge: Which stage must repair a stale handoff?

## Frame 47: Use every workflow stage, but attribute the benefit correctly

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 109–112. Handout page: 47.

Visible transition: Can correctly bound evidence still describe the wrong state?

116--118 min. Keep the six-node live exercise separate from the archived feeder catalog. The archived actual agent traces can be inspected in L10 later. The language model is not required to solve the MILP. The standard method establishes numerical decisions; the architecture makes handoffs and unsupported assertions inspectable. Spoken bridge: Can correctly bound evidence still describe the wrong state?

## Frame 48: From restoration to cyber response: what if the evidence is wrong?

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 113–115. Handout page: 48.

Visible transition: How does an operator estimate a state from imperfect sensors?

118--119 min. Explicit conceptual bridge. Identity, consistency and truth are different properties. The next case is a four-bus DC model designed to expose this distinction, not an attack on the full Greensboro feeder. Spoken bridge: How does an operator estimate a state from imperfect sensors?

## Frame 49: Cyber response begins with an estimation problem

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 116–118. Handout page: 49.

Visible transition: What does a residual actually measure?

119--121 min. Begin from data flow. The teacher knows the simulated state; the controller does not. The attack is confined to this numerical teaching fixture. We are studying limitations of a detector and safe handling of uncertainty, not exploiting infrastructure. Spoken bridge: What does a residual actually measure?

## Frame 50: WLS measures consistency with a model and noise assumption

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 119–122. Handout page: 50.

Visible transition: Can the estimate change while the residual stays the same?

121--124 min. Solve with weighted least squares rather than explicitly inverting a normal matrix in numerical code. Walk through the meaning of covariance. Full column rank matters before thresholding. An alarm says the readings are inconsistent with the assumptions, not which actor caused the problem. Spoken bridge: Can the estimate change while the residual stays the same?

## Frame 51: A coordinated perturbation can change the estimate without the residual

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 123–125. Handout page: 51.

Visible transition: What do the residual and state-error curves look like?

124--128 min. Match the reference teaching style: keep the same equation visible and reveal cancellation step by step. Ask learners to cancel Hc themselves before showing the answer. This is a mathematical negative control, not a claim that all attacks are stealthy or all networks are equally vulnerable. Spoken bridge: What do the residual and state-error curves look like?

## Frame 52: Lab 8: sweep the attack size and watch two different signals

Route: **core**. Notebook: Classroom_Labs.ipynb.

Presentation pages: 126–127. Handout page: 52.

Visible transition: Which plotted signal is available to the operator?

128--135 min. Seven minutes working time. Learners should not report the offline truth metric as available operational evidence. Ask them to mark the detector threshold and distinguish nominal confidence from empirical false-alarm estimation. Spoken bridge: Which plotted signal is available to the operator?

## Frame 53: A missed alarm can coexist with a large estimation error

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 128–130. Handout page: 53.

Visible transition: What additional evidence can justify recovery?

135--137 min. Review the plot from the executed default sweep. Ask which part is observable in a real control room. A language model can explain the discrepancy in this fixture; it cannot conjure trustworthy sensors from the same corrupted data. Spoken bridge: What additional evidence can justify recovery?

## Frame 54: Protected measurements enable a constrained recovery action

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 131–133. Handout page: 54.

Visible transition: Does the recovery action remove the physical overload?

137--140 min. Define the scalar QP and the operational meaning of u. The sensitivity is F times the inverse reduced susceptance matrix times the node-2 injection direction. Full rank permits estimation; exactly three sensors for three states leaves no residual degrees of freedom. Do not call this authentication or a universal attack defense. Spoken bridge: Does the recovery action remove the physical overload?

## Frame 55: Lab 9: verify the control consequence under the same synthetic truth

Route: **core**. Notebook: Classroom_Labs.ipynb.

Presentation pages: 134–135. Handout page: 55.

Visible transition: How should every stage preserve the uncertainty?

140--145 min. Keep the original numeric reference distinct from any new student perturbation. Ask for a physical causal statement: state estimate changes, so constrained control changes. Remove protected information conceptually: the correct response is escalation, not inventing a trusted state or assuming a previous action stays safe. Spoken bridge: How should every stage preserve the uncertainty?

## Frame 56: The cyber workflow must preserve uncertainty at each handoff

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 136–139. Handout page: 56.

Visible transition: Which failure boundary is common across the three cases?

145--147 min. Point out that awareness and verification are substantial computational modules even when not every stage makes an LLM call. The stage table should be read as inputs and returned outputs. L10 later exposes all recorded responses and timings; it is not a fresh language-model run. Spoken bridge: Which failure boundary is common across the three cases?

## Frame 57: The three cases teach three different failure boundaries

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 140–142. Handout page: 57.

Visible transition: How should we evaluate the next generation of this framework?

147--149 min. Give participants a minute to write one sentence for each case. Transition from case mechanics to current research and experimental evaluation. This is the common framework; it is not a claim that one numerical algorithm fits all tasks. Spoken bridge: How should we evaluate the next generation of this framework?

## Frame 58: Recent research asks when coordination is worth its cost

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 143–144. Handout page: 58.

Visible transition: How can an effective procedure carry over to a new task?

Allow two minutes. Bridge from the case results: now that the audience has seen actual candidates, they can assess architectural value. The six benchmarks in Kim et al. are general agent tasks, not grid operations. The architectural tradeoffs in this table are questions for our experiment, not reproduced findings. Ask learners to distinguish three model identities from three distinct physical actions. A candidate vote can convey agreement while adding no action diversity. The tutorial pays for the whole pool before selecting a trial, so it cannot claim the cost savings of routing a prompt to only one model. The voltage result is a null result about selector advantage, not proof that language interpretation never helps. Next: how can a useful procedure persist when the task or agent changes? Spoken bridge: How can an effective procedure carry over to a new task?

## Frame 59: Reusable skills make the procedure explicit

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 145–146. Handout page: 59.

Visible transition: Which decisions require an enforced authority boundary?

Allow two minutes. A skill packages a procedure, while a tool performs a specific operation. The cited recent study uses PSSE and distinct agent implementations. Our tutorial uses Python tools and does not reproduce its platform or performance. The purpose of this slide is to make the existing numerical workflow reusable without losing assumptions. A language summary may compress details that the state contract must retain exactly. Ask the audience what an OpenDSS verification establishes if the prior record only says PASS. Answer: without model scope and identity they cannot determine which candidate or part of the network passed. The exercise is a review of the existing handoff, not a live mutation of the scientific archive. Next: preserved evidence still needs a defined authority boundary. Spoken bridge: Which decisions require an enforced authority boundary?

## Frame 60: Control-room authority belongs in executable rules

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 147–149. Handout page: 60.

Visible transition: How could we test the benefit of this orchestration fairly?

Allow two minutes. Point to the separation between language capability and runtime enforcement. The cited paper's rule compliance concerns its tested prototype and trusted governance layer. Its authors explicitly reserve measurement of operator benefit for a subsequent study. In our classroom, state and candidate identity allow a reviewer to see exactly what has been checked. A wrong-source result can be perfectly traceable, so provenance and correctness require separate evaluation. Ask learners which acknowledgment should remain valid after changing the voltage threshold: none of the earlier approvals should authorize the changed recommendation. Keep the endpoint advisory. This is the reason the operator screen presents limits, model scope and rejected alternatives alongside the concise Llama explanation. Spoken bridge: How could we test the benefit of this orchestration fairly?

## Frame 61: The next study should isolate workflow value

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 150–151. Handout page: 61.

Visible transition: What time did the extra coordination actually cost?

Allow two minutes. This slide closes the research section with a concrete experimental design. Accept multiple well-defined answers to the exit question, such as fewer incorrect interpretations at equal electrical feasibility and acceptable latency, or fewer unsupported readiness claims under model mismatch. Numerical objective improvement is another possible outcome, but it must be demonstrated rather than assumed. A matched scripted baseline can use the same verifier and numerical solvers. More validation calls must be accounted for. CONDUCTOR motivates a richer analysis surface; our forecast perturbations would be a classroom sensitivity experiment, not a reproduction or a calibrated operational risk estimate. PowerAgentBench-SS motivates separate evidence and physical scores. Operator workload needs an actual human study. Transition to the final operator review: the audience now has a criterion for judging whether to trust, reject or extend the workflow. Spoken bridge: What time did the extra coordination actually cost?

## Frame 62: Latency must be measured where the work actually happens

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 152–153. Handout page: 62.

Visible transition: What can we inspect in one real local Llama call?

157--159 min. Research frontier has occupied 149--157. Read the latency axis and distinguish actual raw call times from a sum of components. Parallel service would have different wall-clock behavior and cannot be inferred from these serial accounts. No latency confidence interval establishes production deadline compliance. Spoken bridge: What can we inspect in one real local Llama call?

## Frame 63: Lab 11: one optional local Llama call, with visible provenance

Route: **core**. Notebook: Classroom_Labs.ipynb.

Presentation pages: 154–156. Handout page: 63.

Visible transition: Which outcomes must we score separately?

159--161 min. Optional instructor live demo only; do not let model download consume class time. The audience can use saved real responses. Show the process boundary: this requests language output from a local runtime, not equipment dispatch. Warm/cold loading and hardware affect measured latency. Explain any invalid JSON or failure transparently. Spoken bridge: Which outcomes must we score separately?

## Frame 64: Evaluate the failure, the recovery and the final outcome separately

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 157. Handout page: 64.

Visible transition: What evidence should reach the operator?

161--162 min. One-minute synthesis of evaluation. These dimensions should be recorded independently. A rejected trial may be evidence the guard worked, yet still consume time. A low false-alarm rate can coexist with missed stealth attacks. Move to the operator capstone. Spoken bridge: What evidence should reach the operator?

## Frame 65: The control room receives a recommendation with an evidence trail

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 158. Handout page: 65.

Visible transition: How does a review become an explicit acknowledgment?

162--164 min. Explain the deployment boundary: notebook, numerical sandbox and advisory review are implemented; operational integration is a concept. Do not suggest the synthetic feeder is a live network. Ask what the operator would need to see before reviewing a change during a busy shift. Spoken bridge: How does a review become an explicit acknowledgment?

## Frame 66: Lab 12: acknowledgment is a state transition, not a generated sentence

Route: **core**. Notebook: Classroom_Labs.ipynb.

Presentation pages: 159–162. Handout page: 66.

Visible transition: Can we reconstruct every stage from one saved trace?

164--168 min. Four minutes hands-on. The operator reviews a specific packet; a language model cannot acknowledge on their behalf. Wrong identity is rejected. If a changed action is not reverified, a prior approval cannot carry over. A completed readback is still not proof the operator understood the evidence; that needs human-factors evaluation. Spoken bridge: Can we reconstruct every stage from one saved trace?

## Frame 67: One trace should answer what happened at every stage

Route: **core**. Notebook: Classroom_Labs.ipynb.

Presentation pages: 163. Handout page: 67.

Visible transition: Which missing evidence changes the operator decision?

168--170 min. L10 is archived five-stage evidence, clearly labeled. The fresh classroom methods are related but are not retroactively given those old language responses. Ask students to find a stage that uses a deterministic method and explain why it still belongs in the agentic workflow. Each role has a responsibility, not necessarily its own model process. Spoken bridge: Which missing evidence changes the operator decision?

## Frame 68: Capstone: would you approve, hold or request another study?

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 164–165. Handout page: 68.

Visible transition: Which architecture fits each kind of operator task?

170--172 min. Ask one row per group. These cards are intentionally distinct: model scope, physical permission and information trust. The correct answer includes a concrete next action rather than simply no. Do not imply that holding a prior setting is always safe after a topology or measurement change. Spoken bridge: Which architecture fits each kind of operator task?

## Frame 69: Match the architecture to the operator task

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 166. Handout page: 69.

Visible transition: Can you explain one complete case using the five stages?

172--174 min. This table is a synthesis, not a ranking of packages. Ask learners to choose the simplest design for their own use case. A deterministic workflow can include the same engineering verifier and operator controls; those features are not exclusive benefits of an LLM. Spoken bridge: Can you explain one complete case using the five stages?

## Frame 70: Explain the full workflow in sixty seconds

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 167. Handout page: 70.

Visible transition: Which comparisons support a scientific claim?

174--176 min. Give one minute per pair, then ask for a concise example. Do not accept merely reciting agent names; require MPC, SAC, MILP, WLS, QP or a numerical model where appropriate. The physical simulation stage does not execute field actions. Spoken bridge: Which comparisons support a scientific claim?

## Frame 71: Three checks for scientific claims about agentic control

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 168–169. Handout page: 71.

Visible transition: What single assumption would you change in the next experiment?

176--178 min. This is the scientific takeaway, not a marketing conclusion. Participants should be able to reject an unfair DRL-versus-agentic comparison where the latter receives a better model or more trials. Ask which ablation they would run next. Spoken bridge: What single assumption would you change in the next experiment?

## Frame 72: Your next experiment: change one assumption and keep an audit trail

Route: **core**. Notebook: Concept / discussion.

Presentation pages: 170. Handout page: 72.

Visible transition: Choose an extension, then use the appendix when you need its derivation.

178--180 min. End with an achievable research task, not additional lecture content. Invite participants to choose one extension and write a hypothesis. The teaching session ends here; the appendix is not part of the time budget. Answer final questions and point to the source package and classroom notebook. Spoken bridge: Choose an extension, then use the appendix when you need its derivation.

## Frame 73: Technical appendix: use after the three-hour class

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 171. Handout page: 73.

Visible transition: Which physical limit couples active and reactive power?

Outside the 180-minute route. Choose individual appendix pages in response to questions or for an advanced follow-up session. The source package retains all original section files, including material not selected into this appendix.

## Frame 74: Two controls share one inverter capability

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 172–173. Handout page: 74.

Visible transition: Which limits turn the request into an optimization problem?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. 37--39 minutes. Ask for a prediction before advancing the overlay. The drawing shows the positive-active-power half of the normalized capability circle, with equal axis scales. Positive generator q means injection and negative q absorption. Neither sign universally improves every constraint. The orange point illustrates a tradeoff, not a measured operating point. Bridge: convert these engineering limits and preferences into an optimization problem. Spoken bridge: Which limits turn the request into an optimization problem?

## Frame 75: Turn the operating request into a checkable problem

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 174. Handout page: 75.

Visible transition: Which quantities can this particular experiment control?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. 39--41 minutes. C_PV penalizes curtailed PV power; C_v penalizes voltage deviation from a declared target; C_q can penalize reactive effort. Explain each symbol next to its use. Phi labels a phase, i a bus, ell a branch and g an inverter. Available PV and per-device reactive limits also constrain the problem and remain in the implementation. Ask whether a very good objective permits violating current: no. Bridge: the general formulation may have many device variables; we use a transparent two-variable reduction for this experiment. Spoken bridge: Which quantities can this particular experiment control?

## Frame 76: What does this teaching experiment actually control?

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 175. Handout page: 76.

Visible transition: What operating point does the numerical optimizer return?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. 41--43 minutes. Walk through the three underbraces: normalized curtailment, reactive effort and mean squared voltage deviation. The coefficients are teaching preferences rather than calibrated economic prices. All 930 devices share the two factors; this is not independent per-inverter optimal control. The declared high-irradiance overlay makes available active power equal to rated kVA. Device kvar bounds and an inner capability polygon are enforced. The algorithm is a sequence of local QPs, not a global nonlinear optimality proof. Bridge: run it and inspect the returned control and fresh check. Spoken bridge: What operating point does the numerical optimizer return?

## Frame 77: V1: ask the optimizer for a better operating point

Route: **reference**. Notebook: Workshop_Step_by_Step.ipynb.

Presentation pages: 176. Handout page: 77.

Visible transition: Which constraint can become worse when voltage improves?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. 43--46 minutes. Give participants time to run V1 and find the same quantities in its returned table. These figures are from the executed selected LinDistFlow route. Negative q means absorption. Do not infer a safety improvement from an infeasible baseline: both baseline and optimized points are feasible in this model. The optimizer's accepted flag includes a fresh backend solve and dispatch-tracking checks. Ask how much P was reduced and whether current moved in the expected direction. Bridge: extrema summarize a point, but a plot makes the simultaneous changes easier to see. Spoken bridge: Which constraint can become worse when voltage improves?

## Frame 78: V2: better voltage can come with higher current

Route: **reference**. Notebook: Workshop_Step_by_Step.ipynb.

Presentation pages: 177. Handout page: 78.

Visible transition: What changes if only reactive power can move?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. 46--48 minutes. Ask participants to identify the baseline and optimized curve before explaining. Horizontal positions are sorted samples, not geographic bus positions. The limit lines use the selected MV model's normal ratings. The plot demonstrates a tradeoff, not a universal sign rule for reactive power. Bridge: hold active power fixed and predict the effect of changing only reactive power. Spoken bridge: What changes if only reactive power can move?

## Frame 79: Hold active power fixed; change only reactive power

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 178. Handout page: 79.

Visible transition: Will the same control pass the fuller model?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. 48--51 minutes. Compare two exact points in a scratch PQBackend without changing stored V1 or V2 output. Both settings satisfy the fleet capability circle. Calling the same scratch model twice permits a controlled P/Q comparison. Do not pass a new load multiplier to the older snapshot LinDistFlow adapter, which intentionally rejects that argument. A prediction need not be right; report what the selected backend returns. Bridge: would the same control pass a wider model boundary? Spoken bridge: Will the same control pass the fuller model?

## Frame 80: V3: does the same control pass a fuller audit?

Route: **reference**. Notebook: Workshop_Step_by_Step.ipynb.

Presentation pages: 179–180. Handout page: 80.

Visible transition: How does a horizon plan extend a single operating point?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. 51--53 minutes. Let participants predict before advancing. The audit evaluates identical controls; its failure is not a secret repair. The separate OpenDSS optimized point has maximum voltage 1.043224 pu and current 99.8913 percent, with zero checked violations. These are recorded comparisons, not a claim that V1 ran both backends. Explain why larger permitted PV in an MV-only model is not automatically a superior full-feeder control result. Bridge: we have considered one instant; the next experiment keeps continuous P/Q controls and adds a planning horizon. Spoken bridge: How does a horizon plan extend a single operating point?

## Frame 81: MPC chooses a continuous P/Q sequence

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 181. Handout page: 81.

Visible transition: How does a learned policy generate a continuous action?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. 53--56 minutes. A horizon is one constrained optimization over a sequence, not three unrelated optimal points. The movement term links neighboring controls. The tool freshly checks all planned stages against the chosen model. The workflow's common gate later evaluates the proposed first action. We inspect one planning decision; no closed-loop stability or recursive-feasibility theorem is claimed. This implementation uses continuous fleet participation factors and local sequential QPs, not the earlier discrete-cap demonstration. Spoken bridge: How does a learned policy generate a continuous action?

## Frame 82: SAC maps the operating state to continuous controls

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 182. Handout page: 82.

Visible transition: Which feedback trains the policy?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. 56--59 minutes. SAC means Soft Actor-Critic. It learns a policy from rewards; inference does not run the MPC optimizer. The observation contains three forecast values, previous a and b, a current-allowance fraction, and the remaining normalized horizon. The deterministic saved actor supplies two real-valued commands without rounding them into a cap catalog. The engineering map is part of the training environment. SAC's entropy is defined in its normalized action coordinates, not claimed to be entropy in the nonlinear physical coordinates. Spoken bridge: Which feedback trains the policy?

## Frame 83: What does SAC learn to reward?

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 183. Handout page: 83.

Visible transition: Does a favorable reward establish engineering feasibility?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. About one minute within the existing 59--61-minute training explanation. This frame supplies the precise reward and entropy interpretation before the learning curves. The training environment has three-step episodes and nominal current allowance only. Its fitted mean-square voltage response supplies the stage cost; no optimal MPC action labels enter replay. Clarify that entropy is in normalized z coordinates, before the nonlinear actuator map. Twin-critic learning and entropy aid learning; neither is an electrical safety certificate. Spoken bridge: Does a favorable reward establish engineering feasibility?

## Frame 84: Training reward and fresh engineering checks answer different questions

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 184. Handout page: 84.

Visible transition: Why choose SAC, and when could PPO be appropriate?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. 59--61 minutes. When the actual plot is present, first identify return on the left and surrogate violations on the right. Neither curve measures fresh AC feasibility. The reward combines the same operating preferences with penalties for predicted voltage/current violations. Training uses nominal current allowance, while the reserve fixture changes that allowance; transfer to the MV-only backend also changes the model. Report raw-policy outcomes separately from the common checker and any MPC fallback. This is a single checkpoint, not a broad benchmark of SAC. Spoken bridge: Why choose SAC, and when could PPO be appropriate?

## Frame 85: Why SAC here, and where would PPO fit?

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 185. Handout page: 85.

Visible transition: What do MPC and the saved SAC actor propose for one case?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. 61--62 minutes. This comparison explains algorithm roles rather than ranking algorithms. The SAC actor uses off-policy reward training and replay. PPO is a reasonable continuous-policy alternative, but no PPO training or performance comparison was run in this package. A clipped objective is not a hard network-safety guarantee. The downstream common verifier makes replacing the proposal method an explicit, testable change. Spoken bridge: What do MPC and the saved SAC actor propose for one case?

## Frame 86: V4: produce an MPC plan and a SAC proposal

Route: **reference**. Notebook: Workshop_Step_by_Step.ipynb.

Presentation pages: 186. Handout page: 86.

Visible transition: Does each proposed action pass a fresh check?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. 62--66 minutes. The operating cases are nominal load, a changing load trajectory, and an eighty-percent current allowance. They were authored before training but use the same feeder and declared domain, not an unseen utility network. Both model routes use the same saved actor. Compare raw controls first; the next checkpoint tells us whether they pass. Setup/training, model solves and online policy inference are different costs and should not be conflated. Spoken bridge: Does each proposed action pass a fresh check?

## Frame 87: V5: a continuous proposal still needs a fresh check

Route: **reference**. Notebook: Workshop_Step_by_Step.ipynb.

Presentation pages: 187. Handout page: 87.

Visible transition: How do the decision variables change after a fault?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. 66--69 minutes. Inspect the actual returned voltage/current/action/dispatch check, rather than inferring success from an actor's output. The plotted controls are measured tool outputs once the numerical study is available. An MV-only pass and a full-feeder AC pass cover different constraints. The workflow's first-action gate does not enforce an arbitrary MPC value-gap threshold and does not establish recursive feasibility. The actual response should distinguish raw policy, model check, and any future fallback. Spoken bridge: How do the decision variables change after a fault?

## Frame 88: Which constraints make a restoration plan feasible?

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 188. Handout page: 88.

Visible transition: Which feasible pickup has the greatest declared value?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. About one minute of the existing 100--103-minute MILP explanation. The signed flows permit either direction on a selected branch. Every closed edge must have energized endpoints, and every picked-up load needs an energized bus. Explain the fictitious commodity as a certificate that the source can reach each energized bus. Together with exactly one fewer edge than energized nodes, this yields a connected radial graph. The source commodity balance is included in the code. Spoken bridge: Which feasible pickup has the greatest declared value?

## Frame 89: R1: choose the most valuable feasible load pickup

Route: **reference**. Notebook: Workshop_Step_by_Step.ipynb.

Presentation pages: 189. Handout page: 89.

Visible transition: Can every supplied load be traced back to a source?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. 100--103 minutes. Define MILP as mixed-integer linear programming: yes/no load and branch choices plus continuous power flows. The solver is HiGHS through SciPy. Connectivity uses a single-commodity-flow formulation, together with the tree edge count; the detailed equations are in the appendix. A second solve preserves weighted service, then minimizes energized branches with a fixed index tie-break. That is not switching operations relative to a previous topology. Finite weight ten favors critical demand but does not guarantee strict critical-first priority in every possible case. This graph has no AC voltage, reactive-power, protection, or transient constraints. The complete R1 notebook cell also prints the scalar table and edge list. Spoken bridge: Can every supplied load be traced back to a source?

## Frame 90: R2: trace the supplied loads back to the source

Route: **reference**. Notebook: Workshop_Step_by_Step.ipynb.

Presentation pages: 190. Handout page: 90.

Visible transition: How does a fuller model change this restoration study?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. 103--106 minutes. Follow node 3 back to source 0 in the limited solution. Node 4 lies on this path but its own 50 kW load is not picked up. Normal weighted service is 1,060; limited service is 1,010. The normal solution sends 210 kW through tie 0--4. In the limited solution, tie 0--4 carries 70 kW and tie 1--5 carries 90 kW. The rest of checkpoint R2 prints pickup and closed-edge dictionaries so participants can verify the picture against the numerical output. The figure displays actual solver output, not a hand-chosen route. Spoken bridge: How does a fuller model change this restoration study?

## Frame 91: R3: keep the decision logic, change the model scope

Route: **reference**. Notebook: Workshop_Step_by_Step.ipynb.

Presentation pages: 191. Handout page: 91.

Visible transition: What changes when the feeder bypass rating is tighter?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. 109--112 minutes. Say: We have seen how restoration can be formulated. Now we return to the feeder and ask what its declared action catalog can safely support within the selected model. Do not call this checkpoint a full-feeder MILP. R1 permits a 400 A short bypass. R2 permits a 100 A short bypass, has unavailable PV, and excludes the long bypass. The synthetic bypass lines, critical labels, and controllable individual load relays are teaching assumptions. BACKEND selects OpenDSS or the independent MV LinDistFlow model. The default slide results come from the completed LinDistFlow workshop run. Spoken bridge: What changes when the feeder bypass rating is tighter?

## Frame 92: R3: the tighter feeder bypass changes the recommendation

Route: **reference**. Notebook: Workshop_Step_by_Step.ipynb.

Presentation pages: 192. Handout page: 92.

Visible transition: Which part of the decision came from the language agent?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. 112--115 minutes. Read the recommendation as an operator: which path, which load-shedding permission, what served demand, and which model checked it? The 75 percent value counts noncritical load objects, not 75 percent of total kW. Exact service is 4,747.46756 and 1,843.61355 kW; critical service is 474.03975 kW in both. Current use is relative to the allowed rating, with maxima 47.7551 and 91.8672 percent. Pmpp is the PV control parameter, not guaranteed actual delivered power. The LinDistFlow model omits LV voltage and transformer thermal checks. This checkpoint does not execute a full-feeder AC audit. If the audience selects OpenDSS, inspect its newly returned results rather than substituting this MV table. Spoken bridge: Which part of the decision came from the language agent?

## Frame 93: R4: what decision did the agent add?

Route: **reference**. Notebook: Workshop_Step_by_Step.ipynb.

Presentation pages: 193–194. Handout page: 93.

Visible transition: Can the workflow interpret a new operator request?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. 115--119 minutes. Pause before the reveal. Say: The optimizer can solve this stated problem. Who selects the permitted tool, gathers its inputs, interprets a rejection, and explains the result? This is the potential coordination role of the framework. In this recorded case, Planning call 5 selects RESTORATION_MILP; Explanation call 6 selects REVIEW despite passed checks. Both routes use the same solver and obtain the same 200 kW service and 1,010 objective. The agent has no numerical optimum or completion advantage here. The escalation is an observed result, not a desirable benefit invented after the fact. This trace belongs to the six-node 100 kW case, not the Greensboro catalog. It reads recorded model output and makes no new Llama call. Spoken bridge: Can the workflow interpret a new operator request?

## Frame 94: R5: can the system understand this operator request?

Route: **reference**. Notebook: Workshop_Step_by_Step.ipynb.

Presentation pages: 195. Handout page: 94.

Visible transition: Which exact fields pass from language to the numerical tool?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. 119--122 minutes. This is the exact h06 request. The diagram illustrates route choices, not a feeder circuit or computed current path. Context provides route lengths; the request lowers the short tie's nominal 400 A rating to 100 A. This is a recorded language study, not a new restoration run in A1. Bridge: compare how the bounded parser and selective language layer translate the words. Spoken bridge: Which exact fields pass from language to the numerical tool?

## Frame 95: R5: the language layer completes a real handoff

Route: **reference**. Notebook: Workshop_Step_by_Step.ipynb.

Presentation pages: 196–197. Handout page: 95.

Visible transition: How do the request cases compare under the same rules?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. 122--125 minutes. Exact interpretation: READY, rating_fraction 1.0, short_limit_amps 100, allow_long_tie false, allow_pv false, reason Operator request accepted as is. The parser says Need one stated short-path current ceiling. Ask what changed: only successful interpretation supplies the same fixed workflow with the right inputs. Reveal served 1843.61355 kW, critical 474.03975 kW, voltage 1.005461--1.0299999 pu and current 95.5555 percent; offline intended-constraint gate passes. Shedding 0.75 counts noncritical objects, not 75 percent of kW. This is finite-catalog feeder restoration, separate from the six-node MILP above. No measured operator-time saving or better optimum is claimed. Bridge: evaluate beyond one useful example. Spoken bridge: How do the request cases compare under the same rules?

## Frame 96: R5: compare the restoration requests as a group

Route: **reference**. Notebook: Workshop_Step_by_Step.ipynb.

Presentation pages: 198. Handout page: 96.

Visible transition: What should happen when an operation is prohibited?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. 125--129 minutes. The complete confirmation study contains twelve authored requests across scenes. Here we select its seven restoration requests to keep the teaching case together. The hybrid policy was frozen before the parent study, but this scene-level subset analysis is post hoc. Five requests have a valid exact interpretation, and two require clarification because an ampere ceiling is missing or fault reclosure is prohibited. Both methods correctly clarify those two. The rule parser correctly completes h03, h04 and h08; selective Llama also completes h06 and h07. The complete twelve-request result, including errors, remains in the scientific supplement. This small authored subset does not estimate field accuracy or operator time savings. Spoken bridge: What should happen when an operation is prohibited?

## Frame 97: R5: a prohibited restoration request needs clarification

Route: **reference**. Notebook: Workshop_Step_by_Step.ipynb.

Presentation pages: 199–200. Handout page: 97.

Visible transition: How can corrupted measurements affect the inferred state?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. 129--132 minutes. Reserve three minutes before revealing the recorded response. The issue is a prohibited operation, not simply missing numerical data. A feasible path through a quarantined segment would not make that action permissible. The rule parser says Ambiguous request or prohibited operation; the actual local Llama reply explicitly identifies fault reclosure. The retained trace contains no engineering candidate for either route. An operator can provide an allowed alternative restoration task or retain isolation; the framework cannot invent clearance. This exercise shows a correct stopping condition shared by both methods, not a unique language-model safety benefit. Spoken bridge: How can corrupted measurements affect the inferred state?

## Frame 98: Fit the readings, then examine what the fit leaves unexplained

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 201. Handout page: 98.

Visible transition: How do residuals produce an alarm and a suspect reading?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. 137--140 minutes. Let the audience answer before the reveal. Explain z as the eight measurements, H as their linear dependence on the three angles, and R as the declared noise covariance. The implementation checks full column rank and uses weighted least squares, rather than explicitly inverting the normal matrix. An isolated error may fail consistency, while a coordinated error may not. The next checkpoint quantifies this distinction; the following plot makes the failure visible. Spoken bridge: How do residuals produce an alarm and a suspect reading?

## Frame 99: From residuals to an alarm and a suspect measurement

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 202. Handout page: 99.

Visible transition: What happens when one detector sees three corruption cases?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. About one minute within the existing 140--143-minute detector explanation. The covariance expression explains why dividing residuals by raw sensor standard deviations is not the same localization statistic. Assumptions matter: the nominal chi-square calibration is exact for this linear full-rank Gaussian construction, not a universal guarantee for a nonlinear AC estimator. The code flags undefined residual normalizations and checks rank after removal. Spoken bridge: What happens when one detector sees three corruption cases?

## Frame 100: C1: use one detector on three measurement cases

Route: **reference**. Notebook: Workshop_Step_by_Step.ipynb.

Presentation pages: 203. Handout page: 100.

Visible transition: Can the residual remain small while the state estimate shifts?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. 140--143 minutes. The chi-square threshold uses five residual degrees of freedom and alpha 0.01. This is a nominal calibration, not a measured false-alarm rate from three trials. All cases use the same model and fixed noise sample. The isolated corruption adds 0.08 p.u. to flow 1--2, measurement index 1. Its largest normalized residual identifies that measurement in this fixture, and control is held. The stealth case uses a=Hc with c=(0.01,0.025,0) radians. Detailed residual covariance and localization equations are in the appendix. Spoken bridge: Can the residual remain small while the state estimate shifts?

## Frame 101: C2: a small residual can accompany a large state error

Route: **reference**. Notebook: Workshop_Step_by_Step.ipynb.

Presentation pages: 204–205. Handout page: 101.

Visible transition: What independent information supports recovery?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. 143--146 minutes. Pause before the reason. The isolated statistic is 277.4974, above the 15.0863 threshold. Nominal and stealth statistics are both 3.9202, below it. Their state error norms differ: 0.000237 versus 0.026780 radians. The full identity is z'=z+Hc, xhat'=xhat+c, hence z'-H xhat'=r. The stealth construction assumes knowledge of H and access to the unprotected channels required by a. It is a designed negative control, not a detection-rate survey. The right-hand state error uses known synthetic truth. Spoken bridge: What independent information supports recovery?

## Frame 102: Recovery needs new evidence before it needs a new action

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 206. Handout page: 102.

Visible transition: What actions follow from the different information sets?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. 146--150 minutes. Say: The residual test cannot distinguish these two states. What additional information could break that ambiguity? Introduce the explicitly protected angle measurements with H sub T equal to I3. Full rank identifies the state, while three measurements for three unknowns gives zero residual degrees of freedom; there is no chi-square detection redundancy in this protected set. The numerical experiment assumes trust and does not implement authentication. The scalar control uses the DC flow map F and injection sensitivity F B inverse d2. Bounds, finite values, and predicted constraints are checked after the solve. The 0.01 p.u. margin is an engineering choice, not a calibrated uncertainty guarantee. This is a small DC control problem, not AC feeder redispatch. Spoken bridge: What actions follow from the different information sets?

## Frame 103: C3: compare the actions, then evaluate their consequences

Route: **reference**. Notebook: Workshop_Step_by_Step.ipynb.

Presentation pages: 207. Handout page: 103.

Visible transition: Does the recovery action satisfy every branch limit?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. 150--153 minutes. The corrupted estimate predicts a feasible state and chooses u=0, but actual toy flow remains 0.24 p.u. The protected estimate chooses u=0.1216936673 p.u. Its predicted flow is 0.17 p.u.; evaluation against synthetic truth gives 0.1704607616 p.u., below 0.18. The small prediction/evaluation difference is due to protected measurement noise. Explain that the experiment evaluates both actions under the same known physical toy state, which prevents a favorable result merely because an estimate reports its own constraints as feasible. Spoken bridge: Does the recovery action satisfy every branch limit?

## Frame 104: C3: check every branch against its own limit

Route: **reference**. Notebook: Workshop_Step_by_Step.ipynb.

Presentation pages: 208. Handout page: 104.

Visible transition: Which claims can the language agent support with this evidence?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. 153--156 minutes. Point to flow 1--2 above its limit under the stealth action and below it after protected-data redispatch. Then check the other branches. The branch limits are 0.35, 0.18, 0.35, 0.35 p.u. The chart uses known synthetic truth, not field measurements. The result omits voltage magnitudes, unbalance, reactive capability, protection, and communication authentication. The printed protected-set residual degrees of freedom are zero; this is not a detector success claim for that set. Spoken bridge: Which claims can the language agent support with this evidence?

## Frame 105: C4: the agent can explain evidence, but cannot establish trust

Route: **reference**. Notebook: Workshop_Step_by_Step.ipynb.

Presentation pages: 209. Handout page: 105.

Visible transition: How can we isolate the contribution of response selection?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. 156--159 minutes. This is a recorded trace, not a new Llama call. Planning call 7 selects WLS_TRUSTED_REDISPATCH. Explanation call 8 selects REVIEW despite the passed numerical checks. The fixed comparator returns MODEL_RECOMMEND. The control and detector are identical, so this trial establishes no agent advantage in detection or control quality. The wrapper explicitly supplies the trusted-data branch; it does not discover which sensors deserve trust. Separate the deterministic numerical metric card from the actual model's qualitative response. This visible separation is a useful design property even when the agent escalates unnecessarily. Spoken bridge: How can we isolate the contribution of response selection?

## Frame 106: E1: a separate frozen experiment for the revised optimizer

Route: **reference**. Notebook: LLM_Response_Selection.ipynb.

Presentation pages: 210. Handout page: 106.

Visible transition: Where do MPC and SAC enter the fixed experimental protocol?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. Introduce the E experiment separately from the previous P reference. This corrects the old candidate omission by placing MPC in the initial pool. Scenario splits were frozen before numerical collection. Five learning orders are algorithm sensitivity runs over the same 24 cases, not 120 independent cases. The saved data contain all operation outcomes for audit; the trainer opens only its chosen feedback at each update. This is simulated partial-feedback replay, not logged field data. Spoken bridge: Where do MPC and SAC enter the fixed experimental protocol?

## Frame 107: E2: MPC enters planning directly alongside SAC

Route: **reference**. Notebook: LLM_Response_Selection.ipynb.

Presentation pages: 211. Handout page: 107.

Visible transition: What do three actual models propose for the same evidence?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. The snippet is copied from the exact collection source. MPC is not an optional tool that a language model must remember to request. The two numerical actions are checked on the same context. All observed MV MPC plans have empty horizon-plan failure lists, but the response-refinement gate and ranking remain first-action/current-step operations. Source implementation names INITIAL_MPC and INITIAL_SAC are provenance, not separate LLM agents. Spoken bridge: What do three actual models propose for the same evidence?

## Frame 108: E3: three models respond to the same numerical evidence

Route: **reference**. Notebook: LLM_Response_Selection.ipynb.

Presentation pages: 212. Handout page: 108.

Visible transition: How are different phrasings grouped into physical actions?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. Keep the reasons verbatim and ask students which statements can be checked against available evidence. These are public model outputs, not hidden reasoning. Test 01 is a fixed illustration; the notebook exposes every response and reports aggregate outcomes. Identical prompts and distinct model configurations do not establish independent errors. Spoken bridge: How are different phrasings grouped into physical actions?

## Frame 109: E3: canonical actions make the vote reproducible

Route: **reference**. Notebook: LLM_Response_Selection.ipynb.

Presentation pages: 213. Handout page: 109.

Visible transition: When does the selector receive its numerical reward?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. Run the whole E3 cell, not just the excerpt. Canonicalization rejects malformed replies and duplicate model identities. The SHA tie-break is deterministic and has no physical preference. A fixed response from the common pool is a controlled selection comparator, not a single-model deployment runtime. Full raw call payloads remain in the journal. Spoken bridge: When does the selector receive its numerical reward?

## Frame 110: E4: the reward is revealed only after a response is selected

Route: **reference**. Notebook: LLM_Response_Selection.ipynb.

Presentation pages: 214. Handout page: 110.

Visible transition: How do training records differ from frozen evaluation?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. This is executable notebook code, and its first operation/reward is checked against the recorded training trace. The outcomes exist in a separate file for audit, but the operation is selected before that file is opened. No test outcome enters training, and the independent AC audit is excluded from the MV reward. All response-generation cost has already been incurred, so the reward does not pretend that selecting one response saves the other calls. Spoken bridge: How do training records differ from frozen evaluation?

## Frame 111: E4: actual learning records and frozen evaluation

Route: **reference**. Notebook: LLM_Response_Selection.ipynb.

Presentation pages: 215. Handout page: 111.

Visible transition: Does the learned selector beat voting on held-out cases?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. SAC training and response-selection training have separate checkpoints. These curves show the bandit, not the 12,000-transition SAC training experiment. Training rewards can be negative even for a feasible trial because the improvement is small relative to the fixed trial penalty. The uncertainty bonus supports exploration during training; frozen evaluation uses predicted reward only. Spoken bridge: Does the learned selector beat voting on held-out cases?

## Frame 112: E5: learned selection ties voting on the held-out cases

Route: **reference**. Notebook: LLM_Response_Selection.ipynb.

Presentation pages: 216. Handout page: 112.

Visible transition: Can a rejected trial still end in a feasible recommendation?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. This is the central selector result. The interval against voting collapses to zero because every paired outcome is identical. The graph gives all-responses extra trial budget and labels it accordingly. A small improvement over a particular fixed operation is not evidence that learning or LLM generation is necessary. E5 also displays a post-hoc diagnostic of every permitted fixed numerical rule; always relaxing Q matches the selected pattern without language calls. The twelve contexts are the statistical units. Spoken bridge: Can a rejected trial still end in a feasible recommendation?

## Frame 113: E5: trial rejection and final quality are different outcomes

Route: **reference**. Notebook: LLM_Response_Selection.ipynb.

Presentation pages: 217. Handout page: 113.

Visible transition: Which constraints become visible in the broader model?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. Keep the objective and rejection metrics separate. The fixed increase operation is often rejected under AC constraints but in one context finds a larger improvement. Majority and learned selection favor the smaller Q refinement and are identical in this transfer set. Zero rejected trials therefore does not imply the best objective. All numbers are conditional on the declared method and twelve scenarios; final full-feeder PASS is not a field guarantee. Spoken bridge: Which constraints become visible in the broader model?

## Frame 114: E6: the model determines which constraints are visible

Route: **reference**. Notebook: LLM_Response_Selection.ipynb.

Presentation pages: 218. Handout page: 114.

Visible transition: What inference and solver time does each method consume?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. The plotted controls are the initial MV incumbent and separately optimized OpenDSS MPC plan, while the sentence reports final learned-workflow gates. The notebook exposes both. Avoid claiming the learned selector caused the AC benefit: the numerical model and acceptance contract changed. The selector trained on MV scenarios is frozen for AC transfer, so this is not separately trained in-domain learning on AC. Operator review must show both scope and failed broader-model checks. Spoken bridge: What inference and solver time does each method consume?

## Frame 115: E7: actual inference time belongs in the comparison

Route: **reference**. Notebook: LLM_Response_Selection.ipynb.

Presentation pages: 219. Handout page: 115.

Visible transition: What should the operator see after this comparison?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. The plot shows actual local call latency, including model loading and residency effects. Calls were collected in model batches. Total policy durations are reconstructed sums of observed components, not direct online end-to-end stopwatch measurements. Fixed numerical generates no language pool. Cached notebook execution makes no new model calls and must not be reported as inference speed. Do not compare AC component totals excluding reused planning with MV totals including planning. Spoken bridge: What should the operator see after this comparison?

## Frame 116: E8: the operator sees the recommendation and its scope

Route: **reference**. Notebook: LLM_Response_Selection.ipynb.

Presentation pages: 220. Handout page: 116.

Visible transition: Can a feasible incumbent still benefit from one bounded trial?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. The cell creates a compact operator report with exact candidate and evidence hashes. A full-feeder recommendation is held when the MV action fails the separate AC audit. The accepted AC action still requires human review and an authorized operating process. An acknowledgment is not generated by the experiment. The notebook also prints each stage method and actual returned output, making the abstraction traceable to recorded code and evidence. Spoken bridge: Can a feasible incumbent still benefit from one bounded trial?

## Frame 117: A passed candidate can still be improved

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 221. Handout page: 117.

Visible transition: How do we enforce an equal maximum trial budget?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. Use this after the five-module overview. Awareness and Planning have already produced the initial candidates. Simulation and Verification create candidate-specific evidence. A rejected candidate supplies a reason for repair; an accepted candidate may still have poor objective value and invite refinement. The fifth proposal module handles both branches. Under contract revision 1.1, the first bounded refinement is required when valid tools are available. A later iteration may stop through KEEP_INCUMBENT, an exhausted operation set or the maximum budget. This scheduled first refinement is a shared protocol rule, not a freely selected agent behavior. Call or tool failures still lead to REVIEW. A valid shortlist is ranked, and the chosen action is simulated and verified once more before recommendation. If the process requests review or the final check fails, no recommendation is issued. The older eight named helper responsibilities organize execution and explanation; they do not replace these five core proposal modules. Spoken bridge: How do we enforce an equal maximum trial budget?

## Frame 118: Optimize over tested candidates under the same maximum budget

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 222. Handout page: 118.

Visible transition: Which claims belong to the public reason and which to the solver?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. This is a common finite-search formulation, not a guarantee of the global continuous or mixed-integer optimum. The numerical adapters define J, the model and the constraints separately for each physical task. Contract revision 1.1 allows at most two refinement evaluations after two shared seed candidates and requires the first refinement when valid tools are available. Later search may stop early, so actual counts can differ. The fixed and language-guided routes share this rule; the language model chooses among permitted operations rather than freely choosing whether to perform the required first refinement. A failed call or numerical tool can stop with REVIEW. The retained initial contract pilot and revised run must not be pooled as a repeated benchmark. A final independent recheck is outside the search set and is recorded separately; it duplicates the selected physical action and does not add a new optimization candidate. Awareness and MPC preparation can call the electrical model internally, so do not label the four-candidate search cap as a four-power-flow cap. An empty feasible set or held review produces REVIEW. Compare accepted objective values, budget use, failures and full workflow cost, not ticks alone. Spoken bridge: Which claims belong to the public reason and which to the solver?

## Frame 119: The public Llama reason and the numerical evidence have different jobs

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 223. Handout page: 119.

Visible transition: Where is the bounded decision loop implemented?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. No invented model quotation is shown on this concept slide. Later slides display actual returned reason strings and their call IDs. These are public explanations generated by Llama, not hidden internal chain-of-thought and not a physical proof. The shared contract schedules a required first refinement when valid tools are available; Llama chooses its allowed operation, not the existence of every stage. The ranking schema permits every feasible ID exactly once. The implementation records whether Llama's ordering agrees with cost, but numerical minimum cost determines the selected action; language cannot promote a rejected candidate or override the objective. Wrong structure or IDs force review. A cost-order disagreement remains visible for the operator and evaluation rather than being silently presented as correct language reasoning. Latency, token counts, model settings and errors belong to the same trace record. Spoken bridge: Where is the bounded decision loop implemented?

## Frame 120: Initial supervisor code 1/9: a bounded loop controls what can happen next

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 224. Handout page: 120.

Visible transition: How does the operator request become a numerical contract?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. Optional implementation detail. Begin with the literal range(2), rather than another abstract architecture drawing. The initial planner is allowed VERIFY_SAC_FIRST or REVIEW. After a failed first check, a validated MPC plan can be offered once. A planner REVIEW is terminal for candidate evaluation. Execution here means a numerical proposal, not field dispatch. Ask the audience to locate the two restrictions that prevent arbitrary tool loops: the finite attempt count and the expected tool name. Spoken bridge: How does the operator request become a numerical contract?

## Frame 121: Initial supervisor code 2/9: the request becomes a numerical contract

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 225. Handout page: 121.

Visible transition: How do several roles share one local model service?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. Optional. In the current P3 case, rating_fraction is 0.8, so the returned allowance is 80 percent, not an 80 percent reserve. The participation action is shared across the inverter fleet and is not an independently optimized command at every inverter. Contract validation checks form and declared numerical ranges. It does not establish that a request was interpreted correctly or that the sensors are authenticated. This is why readback remains necessary. Spoken bridge: How do several roles share one local model service?

## Frame 122: Initial supervisor code 3/9: named roles share one local Llama service

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 226. Handout page: 122.

Visible transition: How is the language choice restricted to permitted tools?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. Optional. Explain that an agent architecture can impose useful separation of responsibilities without creating statistically independent judgments. This implementation makes no independence claim. One additional role can add another model call and another failure opportunity. The scientific question is whether the resulting interpretation or routing improves a measured task outcome after accounting for errors and cost. Spoken bridge: How is the language choice restricted to permitted tools?

## Frame 123: Initial supervisor code 4/9: the language tool chooses from a restricted menu

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 227. Handout page: 123.

Visible transition: Which checks follow valid JSON?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. Optional. These excerpts are two separate portions of the actual ask method, not a reconstructed prompt. The call also includes definitions of the permitted actions from CHOICE_DEFINITIONS. The prompt states the policy, while program logic enforces the available routes and numerical gate. A prompt alone cannot establish electrical feasibility. The user-visible reason is stored model output, not a reconstruction of hidden reasoning. Spoken bridge: Which checks follow valid JSON?

## Frame 124: Initial supervisor code 5/9: valid JSON is only the first acceptance test

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 228. Handout page: 124.

Visible transition: How does a passing result retain its model scope?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. Optional. The exception path is part of the workflow, not an LLM response. It must not be reported as successful model reasoning. Give the concrete counterexample from the intake study: a perfectly valid structured reply can misread a current reserve. A physical solver operating under that incorrect limit cannot recover the original human intent. The current numerical workflow receives an already approved structured case. Spoken bridge: How does a passing result retain its model scope?

## Frame 125: Initial supervisor code 6/9: a passing result always carries its model scope

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 229. Handout page: 125.

Visible transition: What can a fresh solve reject that prose cannot detect?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. Optional. Tie this source excerpt to the current P3 example: the MV model accepts the common SAC action, while full AC requires an MPC fallback. This does not establish that the linear MV prediction is inaccurate on the MV buses. It demonstrates why a result must expose its coverage. Plan-level screening also checks that the stored plan backend matches the selected backend. Fresh checking reuses the selected physical model, so it is not independent model validation. Spoken bridge: What can a fresh solve reject that prose cannot detect?

## Frame 126: Initial supervisor code 7/9: a fresh solve can reject a plausible proposal

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 230. Handout page: 126.

Visible transition: How does the code preserve the operator review boundary?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. Optional. Emphasize the difference between the model's own accepted flag and the deterministic gate that reconstructs the checks from the returned arrays. The checker requires nonempty finite data, identities, fresh convergence, valid scope, the requested case, voltage and current bounds, and actual versus commanded P/Q tracking. This is a first-action check. The MPC plan has separate horizon evidence, and neither proves stability or robustness to unknown disturbances. Spoken bridge: How does the code preserve the operator review boundary?

## Frame 127: Initial supervisor code 8/9: the final authority stays with the operator

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 231. Handout page: 127.

Visible transition: Which saved call produced the displayed response?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. Optional. The operator remains a person, not another Llama role. The final dashboard is local and has no SCADA dispatch API. Hashing supports record identity but does not authenticate the human, sensors, model or source files. A future operational integration would need separate authority and assurance work. Ask the audience which displayed quantity would reveal a mistaken interpretation of a 20 percent current reserve. Spoken bridge: Which saved call produced the displayed response?

## Frame 128: Initial supervisor code 9/9: match the displayed response to its recorded call

Route: **reference**. Notebook: Agent_Trace_and_Latency.ipynb.

Presentation pages: 232. Handout page: 128.

Visible transition: Which two clocks appear in the recorded trace?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. Optional. This is the bridge from architecture to inspectable experiments: every claim on the later case slides should point to a numerical return or an actual recorded language response. The call ID is local to its journal, so the source path and unique matching rule also matter. Deterministic stages do not acquire invented LLM reasons or invented per-stage timings. The notebooks are evidence readers unless the main experiment explicitly launches a live call. Spoken bridge: Which two clocks appear in the recorded trace?

## Frame 129: Trace review 1/3: read token counts and two distinct clocks

Route: **reference**. Notebook: Agent_Trace_and_Latency.ipynb.

Presentation pages: 233. Handout page: 129.

Visible transition: How does measured cost relate to the actual outcome?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. Optional. Explain that token throughput, if inspected in the table, is output count divided by eval_duration converted to seconds. It is a generation-rate measure, not total application throughput. For the current AC Planner this is about 74.3 generated tokens per second. Do not infer network overhead, queueing, hardware effects or cache causality from the difference of these aggregate intervals. The h06 client call is distinct from its slightly longer intake wrapper, and its downstream numerical runtime is a third interval. Spoken bridge: How does measured cost relate to the actual outcome?

## Frame 130: Trace review 2/3: compare cost with the recorded outcome

Route: **reference**. Notebook: Agent_Trace_and_Latency.ipynb.

Presentation pages: 234. Handout page: 130.

Visible transition: What should the next controlled study measure?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. Optional. These are descriptive observations on one machine, not matched repeated statistical benchmarks. Compare fixed and agentic within each recorded pair, but do not pool protocols or rank backend speed from differently timed runs. The difference between total workflow time and summed client calls is only other work inside that interval, not a measured solver-stage timer. The positive h06 intake example demonstrates language coverage with errors elsewhere in the study; it does not turn these timing results into a speed advantage. Spoken bridge: What should the next controlled study measure?

## Frame 131: Trace review 3/3: audit this record; design the next study

Route: **reference**. Notebook: Agent_Trace_and_Latency.ipynb.

Presentation pages: 235. Handout page: 131.

Visible transition: How are the three phases coupled in the linear approximation?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. Optional. There are eight source files in the current evidence collection, but the count is not hard-coded here so the notebook remains authoritative if packaging adds records. Store an external trusted reference if authenticity matters. Distinguish a file hash from the recommendation-field hash used by the dashboard. For a repeated experiment, predeclare handling of timeouts, failed schemas, incorrect READY replies and correct abstentions. Do not silently drop slow calls or failed tasks before reporting latency. This page proposes future methodology; it claims no new measurements. Spoken bridge: How are the three phases coupled in the linear approximation?

## Frame 132: Optional reference: coupled three-phase LinDistFlow

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 236. Handout page: 132.

Visible transition: How do objective terms and constraints define voltage support?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. Optional, outside the three-hour timing. Explain dimensions before the multiplication: ohms times VA gives volts squared. The displayed equation uses physical units; multiplying kVA directly by ohms without converting would be wrong. The real-part expression retains phase coupling. Approximate reported losses are separate from the lossless balance. Model coverage, approximation error and solver convergence are different questions. Spoken bridge: How do objective terms and constraints define voltage support?

## Frame 133: Optional reference: voltage-control objective and constraints

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 237. Handout page: 133.

Visible transition: What exactly is the implemented finite-horizon plan?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. Optional. The first equations describe a general problem; the final paragraph defines the actual two-variable reduction. Available P equals rated S only under the supplied high-irradiance overlay. A sequential local sensitivity solve, inscribed capability polygon and fresh checks do not provide global AC optimality. The general model can be extended to individual inverter decisions, but that larger optimization was not executed here. Spoken bridge: What exactly is the implemented finite-horizon plan?

## Frame 134: Optional reference: the executed continuous horizon plan

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 238. Handout page: 134.

Visible transition: How do policy outputs map to physical inverter controls?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. Optional. Six real control variables are optimized. The three forecast loads and movement penalty couple the stages, but storage dynamics are absent. Fresh horizon feasibility is tool evidence; the common workflow gate checks the chosen first action. There is no recursive-feasibility, stability, uncertainty-robustness or global-optimality certificate. A small voltage-objective value on an MV-only model cannot certify LV service voltage. Spoken bridge: How do policy outputs map to physical inverter controls?

## Frame 135: Optional reference: SAC objective, action mapping and reward

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 239. Handout page: 135.

Visible transition: Which restoration variables enforce service and radiality?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. Optional. The entropy coefficient is fixed, not automatically learned. The actor and critic optimize the declared surrogate environment. Training return, fit-validation error and fresh physical evaluation are different evidence sets. The action map enforces the device circle but cannot enforce voltage or line-current constraints. The nominal current used in the training penalty is intentional; it makes the reserve case a distribution shift. Spoken bridge: Which restoration variables enforce service and radiality?

## Frame 136: Optional reference: restoration MILP variables and topology

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 240. Handout page: 136.

Visible transition: How is the residual statistic calibrated?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. Optional. The balance sign follows the chosen edge orientation, with outgoing flow subtracted from incoming flow at non-source buses. Binary y, s and z have different meanings. Edge count alone would permit a disconnected cycle; the commodity constraints exclude it. Capacity is active power here, not a three-phase thermal calculation. The secondary objective is not switch operations from a prior topology. Spoken bridge: How is the residual statistic calibrated?

## Frame 137: Optional reference: WLS, residual covariance and calibration

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 241. Handout page: 137.

Visible transition: Why can a coordinated corruption leave the residual unchanged?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. Optional. Distinguish m measurements from n unknown states, and explain whitening through R. The displayed alpha is a nominal false-alarm probability under the stated model, not a measured attack-detection rate. The largest normalized residual is a localization heuristic. Zero residual variance gives an undefined normalized statistic, and a rank-deficient retained set does not support the same estimator. Spoken bridge: Why can a coordinated corruption leave the residual unchanged?

## Frame 138: Optional reference: why a coordinated corruption can be invisible

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 242. Handout page: 138.

Visible transition: How does protected information enter constrained control?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. Optional. Substitute the shifted estimate directly into the residual and cancel Hc. This exact cancellation is a property of this linear model with an unchanged matrix, not a blanket statement about nonlinear AC state estimation. The protected-set rank argument rules out this particular Hc shift when the stated channels are trustworthy; it does not authenticate channels or address every attack class. Spoken bridge: How does protected information enter constrained control?

## Frame 139: Optional reference: trusted-data estimation and constrained control

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 243. Handout page: 139.

Visible transition: Which assumptions still limit the scientific claim?

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. Optional. F and B use the fixture's signed branch-incidence convention; using the same convention in both yields the action sensitivity b. The decision is a scalar DC injection, not feeder-wide AC cyber recovery. Synthetic truth is available to the evaluator, not to an actual operator. The trusted set is an explicit premise, and Llama cannot establish it. Spoken bridge: Which assumptions still limit the scientific claim?

## Frame 140: Study boundaries and the next scientific comparisons

Route: **reference**. Notebook: Concept / discussion.

Presentation pages: 244. Handout page: 140.

Visible transition: Choose one matched comparison to investigate after class.

Optional historical/detail reference, outside the current 180-minute route. Original notebook IDs and experiment scopes are preserved. Optional. Keep these experiments separate whenever stating a benefit. A successful tool call, correct intent, physical feasibility, good objective and suitable human review are different outcomes. Nothing here establishes field reliability, globally optimal AC control, an authenticated dispatch system, or human time savings. These denominators and limitations are essential to interpreting the observed Llama results in each lesson. Spoken bridge: Choose one matched comparison to investigate after class.

