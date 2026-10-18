# Research refresh for the three-hour grid-operator lecture

Checked **17 October 2026** against primary papers and official documentation. This is a focused teaching selection, not a systematic review. Paper results below are author-reported and were not reproduced here. Exercises are recommendations for this tutorial, not claims that the cited packages are installed or that their algorithms have been reproduced.

The strongest new teaching theme is **an agentic system is an engineered decision process**: language interpretation, explicit state, tool contracts, numerical computation, bounded recovery, evidence and human authority. Its advantage must be measured at the workflow level as well as the electrical level. A larger team or more fluent explanation does not by itself improve control quality.

## Ten mechanisms worth teaching

### 1. Typed tools turn language into inspectable operations

**Primary sources.** Qian Zhang and Le Xie, *PowerAgent: A Road Map Toward Agentic Intelligence in Power Systems: Foundation Model, Model Context Protocol, and Workflow*, IEEE Power and Energy Magazine 23(5), 93–101, 2025, [DOI](https://doi.org/10.1109/MPE.2025.3579718). Current implementation evidence: [PowerMCP official repository](https://github.com/Power-Agent/PowerMCP), [PowerWF official repository](https://github.com/Power-Agent/PowerWF). Publisher full text was not accessible in this session; use repositories for implementation claims.

**Verified mechanism.** PowerMCP supplies interfaces to engineering programs including OpenDSS; PowerWF collects domain workflows. The [MCP tool specification, 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/server/tools) defines tool discovery, invocation and input/output schemas. Protocol interoperability alone does not validate electrical models or authorize field action.

**Code experience.** Show one JSON proposal with `tool`, typed `arguments`, `case_id` and units; deliberately change a limit to a string or use an unknown tool. Compare the raw Llama response, parser result and deterministic rejection. Keep the engineering calculation unchanged.

**Transition.** “Valid JSON is useful. But can a valid call still use the wrong state?”

### 2. State dependencies must be enforced before the tool runs

**Source.** Emmanuel O. Badmus and Amritanshu Pandey, *PowerDAG: Reliable Agentic AI System for Automating Distribution Grid Analysis*, [arXiv:2603.17418v1](https://arxiv.org/html/2603.17418v1), 18 March 2026, especially §§III–V.

**Verified mechanism.** Adaptive retrieval selects expert query/workflow exemplars; a just-in-time supervisor checks prerequisite writes and blocks a covered tool when prerequisites are absent. Its rule library covers a subset of tools. The reported benchmark uses 30 unseen queries, 50 exemplars and 82 tools. Tool success can otherwise conceal stale-state errors.

**Code experience.** Change a load, retain the old voltage result, then attempt to report it. Use `state_version` and `solved_version` to reject the stale result, rerun the solver and resume. Show before/after state and one blocked call. This is an inspired minimal illustration, not a reproduction of PowerDAG retrieval.

**Boundary.** Correct sequencing is different from correct power-flow assumptions or electrical feasibility. Do not label the prerequisite supervisor a universal safety certificate.

**Transition.** “Now the tools see current data. How do we coordinate a request involving several different studies?”

### 3. Hierarchical orchestration separates intent, coordination and execution

**Source.** Yihan (Logon) Wen and Xin Chen, *X-GridAgent: An LLM-Powered Agentic AI System for Assisting Power Grid Analysis*, [arXiv:2512.20789v1](https://arxiv.org/html/2512.20789v1), 23 December 2025.

**Verified mechanism.** Planning, coordination and action layers use domain retrieval and eight pandapower-backed MCP servers. Its tests comprise 11 representative queries repeated 30 times with GPT-5 at temperature zero. The paper reports all repeated queries successful, with outputs checked against manually obtained conventional answers.

**Code experience.** Decompose “restore the critical loads and explain remaining violations” into a typed task list. Show the same state passed to awareness, optimizer and verifier, with different allowed tools. A single Llama backbone may fill several language roles; role separation is not independence.

**Boundary.** Eleven queries repeated many times do not equal hundreds of distinct tasks; cross-paper percentages are not a common leaderboard. Steady-state findings do not certify transient stability.

**Transition.** “A plan must become a numerical candidate before it can become an operator recommendation.”

### 4. Sandboxed trial, fresh verification and rollback have distinct jobs

**Source.** Yan Zhang, Ahmad Mohammad Saber, Amr Youssef and Deepa Kundur, *Grid-Agent: An LLM-Powered Multi-Agent System for Power Grid Control*, [arXiv:2508.05702v3](https://arxiv.org/html/2508.05702v3), 8 September 2025. This supersedes the tutorial's cited v2 for a current literature review.

**Verified mechanism.** Five roles—Topology, Planner, Executor, Validator and Summarizer—use sandbox simulation and rollback after unsuccessful changes. IEEE 30/69 and CIGRE MV cases compare LLM backbones within the architecture.

**Code experience.** Make MPC and SAC propose controls; execute each in a model copy; record constraint margins; reject a bad trial and retain the incumbent. Show that SAC supplies an action while the simulator computes its consequence. Give the final verifier a fresh candidate/state binding.

**Boundary.** The tutorial cannot claim novelty for five roles, solver integration or rollback. v3 no longer contains v2's numbered VI-D RL subsection: do not retain that section reference. Its methods do not establish that our SAC or selector is superior, or that steady-state checking proves stability.

**Transition.** “Passing at one operating point does not tell us what happens when the forecast changes.”

### 5. Uncertainty changes which analysis the orchestrator should request

**Source.** Antonio Alcántara, Aysegül Kahraman, Anosh Arshad Sundhu and Spyros Chatzivasileiadis, *CONDUCTOR: An LLM-Orchestrated Digital Twin for Uncertainty-Aware Distribution Grid Operations*, [arXiv:2606.24609v1](https://arxiv.org/html/2606.24609v1), 23 June 2026, §§2–4.

**Verified mechanism.** The LLM orchestrates unchanged numerical engines, including probabilistic security assessment and robust corrective dispatch. Evaluation replays one year of Bornholm 60-kV measurements. The authors' 68-prompt behavioral catalog reports 67 first-attempt successes. An ablation keeps the same pass rate but changes which boundary request fails and whether tool use is disclosed.

**Code experience.** After voltage support, perturb load/generation scenarios and plot voltage envelopes plus observed violation fractions. Have the agent request a scenario audit before recommending a margin. Call classroom fractions empirical sample results, not calibrated real-world probabilities.

**Boundary.** The evaluated orchestrator uses a hosted model; local deployment is supported but not evaluated. Bornholm measurements are not redistributed. The case's look-ahead uses recorded realized measurements; it is not a forecast-performance result. Human trust and long-term deployment remain future work.

**Transition.** “Even a well-specified analysis needs an honest report of what was actually checked.”

### 6. Evaluate evidence-supported outcomes, not just plausible answers

**Source.** Costas Mylonas, Magda Foti, Andrea Pomarico, Matheus Duarte, Qian Zhang and Emmanouel Varvarigos, *PowerAgentBench-SS: A Benchmark for Agentic AI in Power System Steady-State Studies*, [arXiv:2606.18789v1](https://arxiv.org/html/2606.18789v1), 17 June 2026.

**Verified mechanism.** Public tools and fixed budgets are separated from hidden revalidation. The benchmark distinguishes discovered, submitted and evidence-supported contingencies, mitigation outcomes and tool-use diagnostics. Its pilot covers eight IEEE-39 operating points, 1,035 N-2 contingencies per point and 80 validation calls; electrical scope is DC thermal security with islanding penalties.

**Code experience.** Compare the same controller with fixed orchestration, one LLM, multi-role orchestration and response selection under equal candidate budgets. Compute electrical pass rate, objective, unsupported claims, rejected tool calls and latency separately. Add one report containing a true but unvalidated claim and show why evidence-supported reporting differs from answer accuracy.

**Boundary.** It is a benchmark, not another controller. Its DC outcomes do not cover AC voltage/reactive constraints. Hidden evaluation must not leak into prompts, selector features or training feedback.

### 7. Human authority is a runtime invariant, not a sentence in a prompt

**Recent source.** Costas Mylonas, Magda Foti and Emmanouel Varvarigos, *A Governance-Aware Large Language Model Orchestrated Agentic Digital Twin for Transmission System Operator Control Room Decision Support*, [arXiv:2609.22476v1](https://arxiv.org/html/2609.22476v1), 18 September 2026, §§3, 5–6.

**Verified mechanism.** An external layer enforces whitelisted tools, step budgets, approval for side effects and backend-rendered typed numerical facts. The paper distinguishes 93.7% conservative task success from 100% invariant compliance in its 590-run primary campaign. Its 1,416-run cross-model study also preserves the rules. These are tested behaviors of a trusted layer in a prototype, not a universal safety theorem or human benefit study.

**Code experience.** Show `PROPOSED → VERIFIED → AWAITING_ACK → ACKNOWLEDGED`; change a candidate after approval and invalidate the old acknowledgment. Give the operator a unit, timestamp, model scope and rejected alternatives. Use an advisory simulation with no dispatch endpoint.

**Boundary.** Correct provenance can still point to the wrong source, and an approved action can be the wrong requested action. The benchmark has 87 unique request texts among 118 templated instances. The paper explicitly leaves operator-benefit measurement to a later study.

**Implementation reading.** [LangGraph interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts), accessed 17 October 2026, illustrates checkpoint/resume and warns that code before an interrupt may rerun; side effects should be idempotent or separated. This tutorial can teach that state-machine concept without introducing a LangGraph dependency.

### 8. Context engineering and reusable procedures reduce avoidable handoff loss

**Sources.** Anthropic, [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), 29 September 2025 (official engineering guidance, not peer-reviewed evidence); Pavel Etingov and Shuchismita Biswas, *Skill-Based AI Agents for Power-System Studies*, [arXiv:2609.40272v2](https://arxiv.org/abs/2609.40272v2), revised 1 October 2026 (preprint, submitted to the 2027 IEEE PES Grid Edge conference).

**Verified mechanism.** The engineering guidance treats context as a finite resource managed through selective retrieval, compaction and structured notes. The recent power-study paper uses reusable skills, subagents and MCP-connected PSSE functions across two agent implementations. Its abstract assesses completion, output accuracy and expert intervention; no numerical speedup is imported here because only its abstract was inspected.

**Code experience.** Build a compact evidence packet containing topology version, trusted measurements, units, limits, allowed tools and last verified action. Remove a required field and show why an agent should abstain. Contrast persistent scientific state with the prose conversation summary.

**Boundary.** Retrieved instructions are data unless explicitly trusted. More context can introduce irrelevant or malicious content; a skill does not certify its contained procedure.

### 9. Verification-driven repair should address a specific detected fault

**Source.** Buxin She, Brian Chen, Luanzheng Guo and Fangxing Li, *PFAgent: A Tractable and Self-Evolving Power-Flow Agent for Interactive Grid Analysis*, [arXiv:2604.10846v1](https://arxiv.org/html/2604.10846v1), 12 April 2026.

**Verified mechanism.** Intent parsing, retrieval, execution and reporting are coupled with verification-driven refinement, human feedback and execution-error debugging. Its evaluation distinguishes task success, convergence validity, numerical consistency and explanation quality. Demonstrations include IEEE case changes, voltage violations and N-1 analysis.

**Code experience.** Present a recorded Llama explanation that claims “stability” from a static voltage check. Ask learners to identify the unsupported claim, then revise the public explanation using only returned numerical facts. Alternatively trigger a malformed argument and permit one bounded correction.

**Boundary.** A better explanation need not change the physical action; repairing code execution need not improve feasibility. Reserve “learning” for an actual parameter or persistent-policy update, not an ordinary retry.

### 10. More agents can add coordination cost and shared errors

**Sources.** Mert Cemri et al., *Why Do Multi-Agent LLM Systems Fail?*, [arXiv:2503.13657v3](https://arxiv.org/html/2503.13657v3), 26 October 2025; Yubin Kim et al., *Towards a Science of Scaling Agent Systems*, [arXiv:2512.08296v3](https://arxiv.org/html/2512.08296v3), 8 April 2026. The [authors' repository](https://github.com/ybkim95/agent-scaling/) now cites the published version as *Capable language models can outgrow the benefits of collaboration*, Nature Machine Intelligence 8, 1157–1172, 2026, [DOI](https://doi.org/10.1038/s42256-026-01268-y). Publisher text was inaccessible; numerical findings here refer to inspected arXiv v3.

**Verified findings.** MAST classifies 14 failure modes into system design, inter-agent misalignment and task verification, with over 1,600 annotated traces across seven frameworks. Scaling v3 examines 260 configurations across six benchmarks with controlled tools/prompts/compute; returns depend on task structure and base-model capability. Do not reuse v1's 180-configuration numbers.

**Code experience.** Canonicalize three LLM suggestions into physical operations; count distinct candidates rather than votes alone. Compare fixed, majority and learned selection with the same trial budget and plot actual latency. Then identify whether the selected responses differ at all.

**Boundary.** General-agent benchmarks do not estimate grid safety. In the tutorial's existing pilot, learned selection ties majority voting, and a post-hoc fixed reactive-power rule reproduces those actions. Teach this as an informative null result.

## Suggested compact comparison for the foundation slides

Use two small tables or a diagram plus one table. Avoid a large tick matrix that conflates a roadmap, software ecosystem, research controller and benchmark. A tick means a mechanism is documented, never that its quality is superior. If using capability marks, use **NR** for not reported; absence of evidence is not a proved absence.

| Work | Main design lesson | Scope that the audience must remember |
|---|---|---|
| PowerAgent / PowerMCP | Standardize access to engineering tools | Ecosystem with workflow-specific capabilities |
| PowerDAG | Enforce prerequisite state transitions | Rule coverage and benchmark are bounded |
| Grid-Agent | Trial, validate and roll back | Numerical sandbox; no field safety proof |
| X-GridAgent | Hierarchical coordination and retrieval | 11 distinct representative queries |
| PowerAgentBench-SS | Evaluate evidence and physical outcomes separately | DC thermal pilot; benchmark rather than controller |
| CONDUCTOR | Route uncertainty questions to appropriate numerical methods | One measurement-driven network; author-built catalog |
| Governance-aware TSO twin | Keep authorization and typed numerical facts outside the LLM | Prototype invariants and task correctness differ |
| This tutorial | Expose all stages, MPC/SAC candidates, two model scopes and operator acknowledgment | Educational experiments; no broad superiority claim |

Recommended claim: **“The framework organizes interpretation, computation, verification and review into an auditable workflow. The experiments test when that orchestration helps and when it adds cost without improving the numerical solution.”**

Do not claim the proposed architecture is the first verified grid multi-agent workflow; do not imply that conventional optimizers cannot encode critical-load priorities; do not use paper-reported success rates as head-to-head results against this tutorial.

## Additional recent primary papers for optional reading

- Samim Konjicija and Slaven Peles, [*Integrating Agentic Artificial Intelligence with High-Performance Computing for Grid Planning*](https://arxiv.org/abs/2609.04544), 3 September 2026. AgentiGrid uses ExaGO and supports mid-search steering and concurrent variant exploration. Only abstract inspected; do not import convergence/speed claims into our benchmarks.
- Biswas Rudra Jyoti Arka, Sadman Sakib, Md. Zahidul Islam and Shamsun Nahar Edib, [*Explainable Post-Disaster Grid Observability Recovery Using Human-Oversight Agentic LLMs*](https://arxiv.org/html/2609.16774v1), 15 September 2026. Backend tools coordinate PMU restoration, observability assessment and operator verification. This is **observability recovery**, distinct from restoring served load; suitable adjacent reading after the restoration chapter.
- Anthropic, [*Demystifying evals for AI agents*](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), 9 January 2026. Official engineering guidance distinguishes grader types and “at least one success” from “all repeated runs succeed.” Use its repeated-trial lesson, not a vendor benchmark as a grid result.

## Recommended lecture use

Teach mechanisms 1–4 with a small concrete workflow before case studies. Insert uncertainty and evidence scoring immediately after voltage results. Introduce numerical provenance, human authority and context trust before the cyber case and operator dashboard. Reserve long surveys and detailed literature metrics for optional reading. Each taught mechanism should have a prediction question, a short code change, a visible returned artifact and a debrief that identifies one benefit and one limit.

The learner should finish able to: trace one request through all five proposed stages; distinguish MPC/SAC/LLM/simulator responsibilities; reject stale or unsupported evidence; compare a workflow against a matched baseline; and explain why an operator may acknowledge, reject or defer the final recommendation.
