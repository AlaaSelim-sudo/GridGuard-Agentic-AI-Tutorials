# Figure provenance

The lecture uses native LaTeX/TikZ drawings and recorded numerical plots. It does not include AI-generated illustrations, photographs of a simulated control room, or screenshots used in place of editable slide text.

## Native drawings

The chapter `.tex` files contain the editable geometry and labels for the operator workflow, scalar example, dependency graph, electrical-network comparison, branches and bounded repair, inverter circuit, sign convention, rolling MPC horizon, capability circle, three-phase coupling, restoration topology and capacity allocation, measurement examples, protected-data response, latency and advisory operator handoff. The sources cited at the bottom of the associated frame support the scientific concept. The drawings are explanatory adaptations, not reproductions of reported experimental figures.

## Numerical plots

| File | Meaning and source |
|---|---|
| `feeder.png` | The tutorial's selected synthetic SMART-DS Greensboro feeder, `uhs20_1247--udt8894`. Source dataset: https://data.openei.org/submissions/2981. It is not a map of the entire city or a live utility model. |
| `classroom_voltage.png` | Recorded classroom voltage/model comparison. Read the accompanying frame for the same-action versus replanning distinction and network coverage. |
| `classroom_restoration.png` | Fresh classroom six-node restoration capacity sweep. Total and critical service are different metrics. |
| `classroom_cyber.png` | Classroom four-bus DC/WLS response. Synthetic truth is available only for offline evaluation. |

These plot files are copied from the parent tutorial's `figures/` directory. Their experiment sources are `Classroom_Labs.ipynb`, `src/classroom_labs.py` and the recorded `results/` files. The slide footers identify the relevant notebook checkpoints and papers.

## Guide figures

Selected study-guide figures import completed pages from `handout.pdf` as vector PDF artwork. They therefore preserve the native LaTeX diagrams, math and text. Compile the handout before compiling the study guide.

Paper artwork retained in the older Slidev folder is not required by this LaTeX lecture and is not included in the LaTeX source archive.

## Control-room extension

D01–D09 use editable TikZ diagrams and native tables. The operator screens are teaching storyboards, not screenshots of a deployed utility system. Recorded numerical results and Llama responses are labeled separately from illustrative requests. Deployment diagrams are proposed designs informed by NLR ADMS laboratory work, NIST OT and AI risk-management guidance, and DOE control-room research. References appear on the individual slides.
