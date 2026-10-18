# Case evidence memo

Verified against primary sources on 17 October 2026. Reference IDs map to full URLs in `cases.json`. These are evidence labels, not a claim that every example is a production agentic deployment.

## Recommended teaching order

1. **CAISO / OATI: strongest utility agent example.** The customer describes a RAG-plus-multi-agent pilot in July 2025 (C01). OATI subsequently reports production operation from 24 June 2026, with 500+ next-day outage requests analyzed in under eight minutes each night (C02–C03). Cite this metric as vendor reported. The workflow flags, explains, and prepares evidence; operators keep final authority. The independent-autonomous-control interpretation is unsupported.
2. **GE Aerospace / Palantir: actual industrial workflow deployment.** GE's 12 March 2026 announcement explicitly says agentic AI is being deployed and AIP is used across selected supply-chain functions (C05). A sustainment pilot began in early 2024, but the release does not date when that pilot became agentic. Do not claim a numeric improvement absent from the release.
3. **GE Vernova / Alabama Power: operational substrate.** GridOS integrates operational software and governed data. The 3 February 2026 release attributes more than 112 million avoided customer-minutes of interruption in 2025 to the platform (C07). This is an AI/automation foundation, not proof that an LLM agent created the reliability benefit.
4. **Duke Energy: deployed adjacent AI.** AI scans public online channels for customer scams and flags takedowns (12 February 2026, C08). Duke does not disclose a planning/tool-use agent architecture. Use it to teach the distinction between AI detection and a goal-driven agent.
5. **Siemens / U.S. Prism Systems: engineering agent.** Product generally available 20 April 2026 after over 100 pilots. Prism used it to create, modify, and import SCL code in seconds (C09). Show the verified cycle: project context → execute → validate → iterate → engineer review. This is engineering software, not live factory control.
6. **EPRI: research and risk reduction.** Open Power AI launched 20 March 2025; SAFERai.power was announced 6 August 2026 (C10–C12). Treat these as consortium/sandbox/governance initiatives. Membership does not prove deployment. SAFERai's future toolkit and pilot roadmap should not be presented as finished products.
7. **Optional Schneider product case.** Resource Advisor+ launched 20 January 2026 with Sera coordinating specialist agents (C14). This is a commercial product announcement; no named U.S. customer outcome is verified here. The 2025 Boston announcement was an initiative, not proof of launch (C13).

## Useful research tool

DOE CESER and LLNL announced **Stormbreaker**, a dynamic LLM/agentic-AI testbed for power systems and OT, on 16 July 2026 (C15). This supports a contemporary “test before connection to operational systems” segment; it is not a deployed utility operator.

## Images

Exact corporate-source image URLs and attribution are in `cases.json` (I01–I07). Best real photographs: OATI's control-room photograph (I02), its live demonstration (I01), the IEEE PES field-experience panel (I03), and GE Aerospace manufacturing/services photographs (I04–I05). Caption as context photographs, not evidence that the pictured screen or machine is agent controlled. Image licenses were not found; retain attribution and source links. Parent should inspect the images before using detailed visual captions. CAISO's maintenance-volume chart is available as I07.

## Evidence cautions for slides

- Put a status chip on each case: **production assistant**, **selected industrial deployment**, **automation foundation**, **adjacent AI**, **customer pilot / product launch**, or **research initiative**.
- Keep one concise claim per case with a reference footer. Preserve GE Aerospace vs. GE Vernova as separate organizations.
- Do not mix the 500+/8-minute nightly batch metric with the separate OATI marketing description of week-long workflows reduced to 15 minutes.
- Tutorial architecture drawings may add permission gateways, simulators, logging, and human approval as recommended design. Label those drawings **illustrative reference architecture** unless the cited source discloses that exact design.
