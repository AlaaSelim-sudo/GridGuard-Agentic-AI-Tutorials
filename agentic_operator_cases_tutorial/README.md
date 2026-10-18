# Agentic AI: Three Operator Cases

**59 slides / 120 minutes / three four-minute exercises.** This is the separate follow-on to the restored agentic-AI foundations tutorial. It applies the ideas to voltage support, service restoration and cyber response using the existing GridGuard teaching studies.

The IEEE ComSoc blue/cyan theme matches the foundations deck. Forty-nine slides have large visuals, including 29 editable native TikZ diagrams and six scientific figure assets and twelve real notebook/dashboard screenshots. Slides use short explanatory text, full primary source credits and detailed speaker notes. There are no tables, transitions, click reveals or “What to notice” labels.

## Present

- latex/main.pdf: the complete 59-slide presentation.
- Teaching_and_Source_Guide.pdf: explanations, all three exercise answers, complete references, URLs and figure credits.
- slidev/slides.md: editable Slidev source and presenter notes.
- Instructor_Guide.md: slide-by-slide teaching notes and timings.
- Three_Operator_Cases_LaTeX_Source.zip: portable LaTeX project, diagrams, figures, guide and local evidence.
- Three_Operator_Cases_Complete.zip: both presentation formats, source content, built website, diagrams, evidence and numerical checks.

Start the built web presentation without installing dependencies:

    node slidev/preview-server.mjs

Open **http://127.0.0.1:3044/**. The foundations tutorial remains at port 3043. Internet access is only needed for external readings. No model account, model download or live LLM call is required.

## Teaching route

The opening takes six minutes. Each 36-minute case includes its four-minute exercise and a separate debrief. The closing takes six minutes.

1. **Voltage support — slides 6–22.** Freeze the control meaning and model scope, compare numerical proposals, turn genuine archived model replies into bounded trials, check changed actions, examine MV versus full-feeder AC coverage, and prepare the operator packet. Exercise: slide 17.
2. **Service restoration — slides 23–39.** Lock the fault, network and priorities; trace eligible routes; compare critical service with total service; formulate and check the pickup plan; reject outdated evidence; and prepare a review/readback packet. Exercise: slide 37.
3. **Cyber response — slides 40–56.** Freeze the assessment, estimate the state, interpret residual alarms, understand the linear stealth counterexample, justify independent trusted evidence, calculate a bounded response and audit its consequences. Exercise: slide 54.

Each exercise uses one minute to read, two minutes in pairs and one minute to prepare a decision plus one supporting check. The following slide provides the debrief. Exercises concern advisory-study progress, not field dispatch.

## Evidence and model boundaries

Voltage uses one synthetic SMART-DS Greensboro feeder, uhs20_1247–udt8894. The fresh L2 classroom example, archived test_01 response pool and 12-case held-out study are separate records. The learned selector ties majority voting in that held-out study. The same-action reduced-model versus full-feeder audit differs in both equations and network coverage.

Restoration uses a separate six-node active-power transport graph with indivisible load pickup. It establishes a transparent service-policy tradeoff, not AC feasibility, protection coordination, verified field isolation or a temporal switching procedure. Version labels and the topology-change handoff are explicitly labeled teaching examples.

Cyber uses a separate four-bus linear DC fixture. Its protected measurements are assumed trustworthy; neither the LLM nor the residual test authenticates them. The three protected angles have zero residual redundancy. Synthetic truth appears only in offline evaluation.

All numerical plots distinguish recorded outputs from new illustrative diagrams. Two voltage figures are replotted from unchanged recorded values for larger labels. research/voltage_plot_data.json contains those values and exact source locations. research/numerical_verification.json records a fresh consistency check of the existing small restoration and cyber formulations; it is not a new aggregate test of agent performance. Historical LLM replies are not newly generated.

The local workshop evidence is packaged in research/evidence/, with original-file hashes in research/evidence_manifest.json. Source-specific HTML indexes link to the executed notebooks, source code and result records. The teaching guide contains all remote citations in full. The deck does not operate live SCADA/DMS equipment or establish operating authority.

## Edit and rebuild

Edit the five JSON modules in content/ and their full source registries, then run:

    python build_cases.py

Compile latex/main.tex and latex/teaching_guide.tex using a normal LaTeX installation or Tectonic. The source uses editable TikZ; no shell escape is required. The main document is main.tex.

The companion SVGs are prebuilt for Slidev. build_diagrams.py regenerates them from the native TikZ using TeX and Poppler/Cairo. Its runtime paths can be set with OPERATOR_TECTONIC and OPERATOR_RUNTIME. plot_case_results.py regenerates the two large voltage charts from the packaged data and requires Matplotlib. verify_small_fixtures.py requires NumPy and SciPy and writes only a new verification report.

For Slidev authoring, install the pinned dependencies in slidev/package.json, then run npm run dev or npm run build. The complete package excludes node_modules.

This is an independent educational adaptation of IEEE ComSoc network artwork and its blue/cyan palette. IEEE sponsorship or endorsement is not claimed. Recorded source terms govern external artwork and literature.

## Recorded agent walkthroughs and code

Each case now includes five explicit steps: inputs, actual model choice, Python tool call, recorded result and pending human review. These are slides12–16,30–34 and49–53. The original four-minute exercises remain at17,37 and54.

Code_and_Record_Guide.html connects the slide statements with full source files, raw model-call journals, executed notebooks and numerical records. research/code_manifest.json verifies source hashes and equivalent Python statements after formatting. research/screenshots/capture_manifest.json records the original view hashes and selected regions. Real source views are captured without changing results or entering an operator acknowledgment.

The voltage walkthrough is a separate27 September P3 OpenDSS run, not the preceding test_01 selector experiment. Restoration and cyber use their21 September standard-stage runs. They have identical numerical results to their fixed comparators; actual Llama REVIEW replies hold those recommendations. These records come from the archived workshop custom Python supervisors. The separate current GridGuard app uses LangGraph; the dated runs do not validate that newer runtime.
