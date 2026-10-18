# Introductory tutorial: Agentic AI for Utility Operators

Recommended main route: **28 slides, 47 minutes including discussion**. This is the motivation and vocabulary session. A separate follow-on presentation covers the three detailed use cases. Keep the present LaTeX/Slidev identity and authentic photographs; use one idea per slide and modest step reveals. Reference pages and optional details are outside the timed route.

## Three evidence-grounded motivation claims

1. **Operators face a changing planning envelope.** PJM's January 2026 forecast projects average summer-peak growth of **3.6% annually over ten years**, reaching **222,106 MW in 2036**, a forecast increase of **65,733 MW**. This is a planning forecast, not an observed increase, and does not by itself establish a staffing shortage or a need for autonomous control. Teaching inference: more changing assumptions create value in organized, traceable evidence. [M01]
2. **A larger resource fleet still requires situational awareness.** CAISO reported **more than 30 GW of new resources onboarded since 2020** in its 4 May 2026 summer assessment article. It also identified wildfire, extended heat, hydrology, and new-load timing risks. Teaching inference: operators need current context across models, assets, weather, and procedures. Do not imply new resources reduce reliability. [M02]
3. **The first useful agent job is often coordination of evidence.** CAISO's actual environment includes five-minute RTCA and Watch Duty fire/line overlays [O05]; its own AI-pilot description targets maintenance-request validation with RAG and multiple agents [C01]. Teaching inference: an agent can connect information and approved tools around an existing operator decision. Five minutes is RTCA's documented analysis cadence, not an agent response-time guarantee.

Optional additional informative fact: PJM's January 2026 forecast used weather data from 1994–2024 to generate **403 scenarios** (printed report page 4). It illustrates scenario-based modeling; it is not a claim that an operator manually handles 403 scenarios each shift. [M01]

## Main route and timing

| # | Slide and teaching purpose | Time | Evidence / reuse |
|---|---|---:|---|
| 1 | **Agentic AI for Utility Operators.** Introduce the question: what can an agent do for an operator? | 0.5 min | Existing cover; 45–50-minute label |
| 2 | **What this session enables.** Understand, distinguish, and assess; preview the separate three-use-case session. | 1 min | Replace current implementation-heavy goals |
| 3 | **Inside the operator's working day.** Use Duke photograph plus PJM team coverage and core duties. | 2 min | O01; existing I02 photograph |
| 4 | **A control room is a team.** Three grouped functions: balance/reserves, network security/outages, coordination/oversight. | 1.5 min | O02; keep desk details in notes |
| 5 | **Why now: the planning envelope is changing.** One large PJM forecast number with clear date/forecast label. | 1.5 min | M01 |
| 6 | **Why now: more resources and changing context.** CAISO resource-growth fact plus weather and operating context. | 1.5 min | M02 |
| 7 | **What operators already use.** Watch Duty photograph/screenshot and five-minute RTCA; motivate integration. | 1.5 min | O05; existing screenshot |
| 8 | **Where an agent could help.** Briefing, investigation, record screening, and study explanation as proposed tasks. | 2 min | Illustrative task map; no detailed prompts |
| 9 | **From AI to generative AI to agentic AI.** Predict/classify, generate, then choose tools and iterate. | 2 min | Teaching definitions; T01/T02 |
| 10 | **The agent loop.** Goal → plan → tool → observation → check; reveal each step. | 2 min | Existing bounded-loop content |
| 11 | **What is inside the system?** Model, retrieval, tools, state, and authority shown in one diagram. | 2 min | T01/T02; no package code |
| 12 | **Assistant, agent, and controller.** Clarify why fluent text and physical control are different capabilities. | 1.5 min | Existing comparison |
| 13 | **One agent or several?** Explain specialization and coordination costs without recommending swarms. | 1.5 min | Harvard Kempner handbook M04 |
| 14 | **How to judge a public claim.** Production, pilot, product, adjacent AI, and research labels. | 1 min | Existing evidence taxonomy |
| 15 | **CAISO: a real operator workflow.** RAG/multi-agent outage review; draw evidence → assessment → reviewer. | 2 min | C01/C02 |
| 16 | **CAISO: what the reported metric means.** 500+ next-day records nightly in <8 minutes; vendor-reported throughput. | 1.5 min | C02/C03; no blackout-risk extrapolation |
| 17 | **GE: two businesses, two evidence types.** GE Vernova/Alabama operational foundation versus GE Aerospace selected agentic supply-chain deployment. | 2 min | C05/C07; paired existing images |
| 18 | **Siemens and U.S. Prism Systems.** Task execution, validation, iteration, and engineer review. | 1.5 min | C09; named pilot customer/product launch |
| 19 | **Broader company landscape.** Duke scam-detection AI and Schneider Sera product: label differences clearly. | 1.5 min | C08/C14; one compact comparison |
| 20 | **Today's framework map.** LangGraph, Microsoft Agent Framework, OpenAI Agents SDK, Google ADK: what each category supplies. | 2 min | T01–T07; no installation/version deep dive |
| 21 | **Harvard's ToolUniverse.** A verified scientific-agent framework; explain Tool Finder and Tool Caller and domain limits. | 1.5 min | M03; not a grid-control framework |
| 22 | **MCP and A2A.** Tool connection versus agent-to-agent task exchange; one simple diagram. | 1.5 min | T08–T10 |
| 23 | **Research is building shared foundations.** EPRI Open Power AI and SAFERai.power as research and assessment initiatives. | 1.5 min | C10–C12 |
| 24 | **How research checks agent behavior.** DOE/LLNL Stormbreaker plus one benchmark example, without a literature tour. | 1.5 min | C15; optionally T14 |
| 25 | **What makes an output usable?** Sources, timestamps, model identity, result, missing checks, and named reviewer. | 1.5 min | Proposed review packet |
| 26 | **A practical adoption path.** Replay → shadow → bounded pilot; measure decision quality and reviewer effort. | 1.5 min | Proposed engineering route; no detailed release-gate exercise |
| 27 | **What comes next.** Name the separate presentation's three use cases only; explain that it will supply worked evidence/tool sequences. | 0.5 min | Do not invent the user's three titles |
| 28 | **Discussion: what would you delegate?** Recap goal, evidence, tools, limits, and human ownership; take questions. | 5.5 min | Discussion and close |

Timing: the table totals **47 minutes**. Keep reference pages available through navigation but outside the spoken route. This leaves room within a 45–50-minute slot without requiring rapid passage through dense tables.

## Material to move out of the main route

Move these to the separate use-case presentation or an optional appendix: full handover/distribution/transmission prompts; GridGuard graph internals; the detailed verification/scope slide; numerical 1.067→1.043 voltage examples; both exercises and their answers; tool-contract field tables; full authority ladder; detailed framework lifecycle notes; individual benchmark-method slides; test-family matrices; release-gate and metric definitions. The introductory deck should preview these ideas in diagrams rather than run the three use cases.

Preserve the detailed research citations, image credits, and source records as an appendix. Retain qualifications in speaker notes; do not place a long caveat on every slide. For animation, reveal a loop or evidence packet progressively; avoid motion during source-reading or control-room photographs.

## New primary-source readings

- **M01 — PJM, _2026 Load Forecast Report_, posted 14 January 2026.** Printed pages 4 and 6 (PDF pages 6 and 8). Use the report over the companion blog: the blog's winter-peak sentence appears inconsistent with the report, while the summer values agree. https://www.pjm.com/-/media/DotCom/library/reports-notices/load-forecast/2026-load-report.pdf
- **M02 — Aditya Jayam Prabhakar / California ISO, _Summer Assessment confirms continued strengthening of the grid; with additional resources improving overall reliability_, 4 May 2026.** Date verified in CAISO's official newsroom. The solar/wind/storage subtotals include projected additions through 30 June; use the explicit >30-GW-since-2020 statement without turning forecasts into completed additions. https://www.caiso.com/about/news/energy-matters-blog/summer-assessment-confirms-continued-strengthening-of-the-grid-with-additional-resources-improving-overall-reliability
- **M03 — Shanghua Gao, Richard Zhu, Marinka Zitnik / Harvard Kempner Institute, _From Models to Scientists: Building AI Agents for Scientific Discovery_, 9 October 2025.** Harvard explicitly calls ToolUniverse a framework for scientific agents, describes Tool Finder/Tool Caller and MCP integration, and reports >600 tools at that date. Do not present that historical count as the current catalog. https://kempnerinstitute.harvard.edu/research/deeper-learning/from-models-to-scientists-building-ai-agents-for-scientific-discovery/
- **M04 — Harvard Kempner Institute Computing Handbook, _Multi-Agent Orchestration_, live documentation reviewed 17 October 2026.** Useful practical reading on starting with one agent and adding orchestration when measured benefits justify cost; this is research computing guidance, not utility operating policy. https://handbook.eng.kempnerinstitute.harvard.edu/s5b_agentic_ai_workflows/multi_agent_orchestration.html
- **ToolUniverse official documentation / Harvard Zitnik Lab:** https://zitniklab.hms.harvard.edu/bioagent/index.html
- **ToolUniverse author-maintained repository:** https://github.com/mims-harvard/ToolUniverse

## Essential existing readings for learners

- **PJM, _What Happens in the Control Room_, 16 April 2026 [O01]:** https://www.pjm.com/-/media/DotCom/about-pjm/newsroom/fact-sheets/what-happens-in-the-control-room-fact-sheet.pdf
- **PJM, _CB006 Control Room Interactions_, Revision 9, 11 August 2025 [O02]:** https://www.pjm.com/-/media/DotCom/library/whitepapers/compliance/cb006-pjm-control-room-interactions.ashx?la=en
- **John Phipps / CAISO, _Control center modernization is enhancing reliability_, 10 September 2025 [O05]:** https://www.caiso.com/about/news/energy-matters-blog/control-center-modernization-is-enhancing-reliability
- **CAISO, _Exploring AI to support smarter grid management_, 28 July 2025 [C01]:** https://www.caiso.com/about/news/energy-matters-blog/exploring-ai-to-support-smarter-grid-management
- **OATI, _Generative and Agentic AI in Grid Operations: Field Lessons…_, 2026 [C02]:** https://www.oati.com/ai-for-energy/
- **GE Aerospace, partnership expansion announcement, 12 March 2026 [C05]:** https://www.geaerospace.com/news/press-releases/ge-aerospace-and-palantir-expand-partnership-transform-military-aircraft-readiness
- **GE Vernova, GridOS for Distribution launch, 3 February 2026 [C07]:** https://www.gevernova.com/news/press-releases/ge-vernova-launches-gridos-distribution-industrys
- **EPRI, SAFERai.power framework and roadmap [C12]:** https://msites.epri.com/saferai
- **U.S. DOE CESER, Stormbreaker announcement, 16 July 2026 [C15]:** https://www.energy.gov/ceser/articles/ceser-releases-new-testbed-advance-llm-and-agentic-ai-evaluation-critical

The existing case/source registries retain full references for Siemens, Duke, Schneider, framework documentation, and benchmark papers. Use primary-source claims sparingly: existing and new facts should stay within each source's summarization budget across slide bodies and speaker notes.
