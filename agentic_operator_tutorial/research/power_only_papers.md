# Additional power-system agent papers and LangGraph teaching evidence

Reviewed 17 October 2026. Full primary papers and official runtime documentation were read; no reported experiments were rerun. Exact numeric series and locators are in `power_only_papers.json`; `power_only_sources.json` is ready to merge into the reading-source map.

Use four complementary mechanisms, without ranking studies across incompatible tasks:

- **E01 X-GridAgent:** hierarchical decomposition, MCP tool interfaces and numeric retrieval.
- **E02 Feedback-driven simulation agents:** retrieve tool details, generate MATLAB code and repair execution errors.
- **E03 Grid-Agent:** structured candidate actions, simulated validation, state and rollback.
- **E04 VeraGrid-Agent:** targeted file access around a numerical solver, with an explicit same-model no-tool comparison.

## E01: X-GridAgent

[Full v1 paper](https://arxiv.org/pdf/2512.20789v1), Yihan (Logon) Wen and Xin Chen, 23 December 2025. Architecture: Figure 2, PDF p.3. Its planner, coordinator and action layer wrap eight pandapower-based MCP servers; no LangGraph SDK is identified. Section II.C–E (pp.4–5) gives a concrete IEEE118 flow → top-three lines → three separate outages trace. Figure 3 (p.6) instead shows prompt refinement; its caption acknowledges that a judge missed a detail later caught by a human. Figure 4 (p.7) explains schema-adaptive numeric sorting before hybrid retrieval.

Table I / Section IV.B reports 11 selected queries, each repeated 30 times at temperature zero, with all outputs judged correct. This is repeatability on selected queries, not 330 independent task types. A stronger instructional result is Q10: IEEE39 base objective 41,872.30; line11-out objective 42,115.34; doubled-load AC OPF did not converge. Keep the third value missing, not zero, and do not invent monetary units. Steady-state simulations are not field deployment evidence. A paper-linked [demonstration](https://www.youtube.com/watch?v=JUqpwO6NncY) is available; public reproducible code was not verified.

Suggested three slides: hierarchy and tools; selected-outage trace; preserve nonconvergence in the answer.

## E02: Feedback-driven power simulation framework

[Full v3 author paper](https://arxiv.org/pdf/2411.16707v3), Mengshuo Jia, Zeyu Cui and Gabriela Hug, 19 May 2025; [IEEE publication](https://doi.org/10.1109/TSG.2025.3589114), online 18 July 2025, TSG16(6),5556–5572. Figure1 (p.2) and Algorithm2 (p.8) link query planning, tool knowledge, generated code and execution feedback. It evaluates34 DALINE and35 MATPOWER tasks, with budgets of3 and5 attempts respectively.

**Metric warning:** the paper calls its metric “success rate,” but Section V.A (p.9) awards100/50/0 points for full clean fulfillment / fulfilled with unnecessary settings / an unmet requirement. It averages over allowed attempt slots, carrying the final executed score into unused slots. Thus93.13% DALINE and96.85% MATPOWER are graded attempt-averaged scores, not raw final-completion fractions. A chart may show DALINE Sole0.00, standard-RAG31.37, ChatGPT-RAG33.82, Full93.13, labeled precisely with34tasks and `gpt-4o-2024-05-13` (Figure8,p.11).

Section V.E (p.14) shows why an execution loop is insufficient: wrong parameter values and omitted options can still run without errors. Manual expert grading checks requirements. The SFT comparison uses a different model version and deliberately includes evaluation tasks in training; do not call it held-out. Public framework code was not verified; the inspected preprint promises a later release.

Suggested three slides: functions/options retrieval; repair versus semantic validation; interpret the graded score.

## E03: Grid-Agent

[Full v3 paper](https://arxiv.org/pdf/2508.05702v3), Yan Zhang, Ahmad Mohammad Saber, Amr Youssef and Deepa Kundur, 8 September 2025. Use the current title, *Grid-Agent: An LLM-Powered Multi-Agent System for Power Grid Control*. Algorithm1(p.4) and Figure1(p.5) show topology, planner, executor, validator and summarizer roles. Actions update switches, add batteries or curtail load in a sandbox, followed by power-flow validation and rollback. This is a good state-cycle diagram; simulator rollback does not make real switching reversible.

Figure2a(p.7) gives reported resolution rates100/100/63/100/100/44% across six planners, but the exact trial denominator and weighting are undisclosed. Seven named scenarios are not an inferred n=7. No solver brand, orchestration SDK or public framework repository was verified. An optimization comparator and formal optimality remain future work (p.9). Prefer architecture teaching over a headline accuracy plot.

## E04: VeraGrid-Agent

[Full v1 paper](https://arxiv.org/pdf/2607.25155v1), Shivanshu Tripathi, Hamed Mohsenian-Rad and Maziar Raissi, 28 July 2026; [author benchmark/code](https://github.com/Shivanshu-11/veragrid-llm-benchmark). The agent writes JSON, executes VeraGrid AC-OPF, reads a result table of contents and selected lines, then answers a numerical MCQ (Figure2,pp.2–3). The public runner uses Cursor Agent CLI, optionally Claude Code; do not relabel these as a LangGraph implementation.

TableI(p.4): GPT-5.2 gets64/150 without tools and149/150 with the solver-agent workflow. All seven model pairs and50-per-tier counts are in JSON. These150 questions are template-derived around one balanced8bus radial feeder,4generators,185MW load. Repeated-run uncertainty is unspecified. TableII includes interpretation errors and one Composer failure to use tools; avoid saying every failure happened after a successful solve. A correct MCQ option is not a dispatch-policy or field reliability metric.

Suggested three slides: write/solve/read/answer; same-model64→149 comparison; execution and interpretation are separate checks.

## LangGraph: teach graph semantics in the power workflow

Use source IDs **LG01–LG03**. Local requested labels L01–L03 are retained in metadata, but existing shared L01/L02 already identify GridGuard; do not overwrite them.

[Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api): StateGraph combines a state schema, nodes and edges. Nodes produce partial updates; default reducers replace key values. Routing can depend on state, fan out or return to an earlier node. LangGraph therefore supports cycles; it is not synonymous with a DAG. Compile checks graph structure, not power-system correctness.

[Persistence](https://docs.langchain.com/oss/python/langgraph/persistence): checkpointers track within-thread state; stores retain application data across threads. RAM-only savers lose state when the process restarts. Checkpointing does not prove that a grid snapshot is still current.

[Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts): resume with `Command(resume=...)` and the same thread identity. The interrupted node restarts at its beginning; preceding side effects may replay. Separate review from downstream effects and use idempotent effects. Approval/freshness/authority checks remain engineering application logic.

Five integrated visual ideas: physical graph versus dependency DAG versus cyclic workflow; one frozen-case contingency DAG; candidate/check/repair state cycle with budget stop; checkpoint and revalidation after human review; isolated review node to explain replay. Label these original illustrative designs, not implementations claimed by E01–E04.
