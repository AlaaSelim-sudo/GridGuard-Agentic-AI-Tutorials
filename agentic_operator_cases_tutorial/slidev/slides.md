---
theme: default
title: "Hands-on: Three Operator Cases"
info: Follow Classroom Labs through voltage support, service restoration and cyber response, with three exercises
author: GridGuard teaching tutorial
transition: none
aspectRatio: 16/9
canvasWidth: 1280
colorSchema: light
fonts:
  sans: Arial
  provider: none
mdc: false
drawings:
  persist: false
download: false
---

<div class="lesson teaching rigorous cover-slide cover">

<h1>Hands-on:<br>Three Operator Cases</h1>
<p>Run three cases and see how Llama choices connect to engineering checks.</p>
<p>180 minutes · one CPU notebook · three short exercises</p>
<p>IEEE ComSoc theme / Predict, run, change and explain</p>
<img class="cover-logo" src="/branding/comsoc-lockup.png" alt="IEEE Communications Society lockup"><small>Independent educational material · IEEE ComSoc theme adaptation</small>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.</a></div>
<span class="pageno">1 / 80</span></div>

<!--
Open Classroom Labs before the workshop. Participants will run fresh numerical calculations and inspect clearly labeled archived model replies. Use the same notebook for all three cases. If devices are limited, work in pairs: one person runs the cells while the other checks the evidence. The deck uses the IEEE ComSoc theme. The classroom cycle is run, change, check and explain. This expanded edition includes a new L10B replay and a proposed control-room advisory pilot. The scheduled teaching time is 180 minutes; allow breaks outside that total.
Takeaway: 
Nominal duration: 0.5 minutes.

Full sources:
Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md

IEEE Communications Society. IEEE Communications Society: official resources and network presentation template. Reviewed 17 October 2026.
Full source: https://www.comsoc.org/about/brand-experience/resources
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>What would an operator ask an assistant to do?</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/bridge_request.svg" alt="Illustrative study request and review path. The operator retains the decision." style="height:330px;max-height:330px"><figcaption>Illustrative study request and review path. The operator retains the decision.</figcaption></figure><ul><li>Ask for a study: compare allowed options and show the checks needed for a decision.</li><li>The assistant returns a reviewable proposal linked to the input data and tool results.</li></ul></div>
<div class="sources">Source: <a href="https://www.anthropic.com/research/building-effective-agents">Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.</a></div>
<span class="pageno">2 / 80</span></div>

<!--
Start with the operator’s job, not the model name. Read the illustrative request aloud. Ask participants to name the information they would need before making the study. This is a teaching design for an advisory assistant. The classroom notebook provides numerical counterparts for selected steps, not a live control-room connection.
Takeaway: 
Nominal duration: 2.5 minutes.

Full sources:
Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/research/building-effective-agents

Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>What makes this an LLM agent?</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/bridge_script_agent.svg" alt="Same engineering tools, different source of the next-step choice. Both paths require checks." style="height:330px;max-height:330px"><figcaption>Same engineering tools, different source of the next-step choice. Both paths require checks.</figcaption></figure><ul><li>A fixed script follows choices written in code. An LLM agent can choose a permitted next tool.</li><li>Both can branch and use the same solvers. We must test whether model choice adds value.</li></ul></div>
<div class="sources">Source: <a href="https://www.anthropic.com/research/building-effective-agents">Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.</a></div>
<span class="pageno">3 / 80</span></div>

<!--
Use Anthropic’s attributed architectural distinction. A conventional program can contain feedback, branches, rules and sophisticated optimization. Those alone do not demonstrate an LLM agent. A generative model can also just write an explanation. In these records Llama makes bounded choices from an allowed list, receives tool evidence and may select another step. This is narrow agency, not unrestricted autonomy. The default class replays those choices.
Takeaway: 
Nominal duration: 2.5 minutes.

Full sources:
Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/research/building-effective-agents

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Llama, Python and the operator have different jobs</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/bridge_llama_tools.svg" alt="Roles in the recorded teaching workflow. The classroom route shows saved Llama choices." style="height:330px;max-height:330px"><figcaption>Roles in the recorded teaching workflow. The classroom route shows saved Llama choices.</figcaption></figure><ul><li>Llama chooses and explains. Python calculates, checks limits and rejects failed proposals.</li><li>The operator reviews the evidence and decides whether another study or review is needed.</li></ul></div>
<div class="sources">Source: <a href="https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py">Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.</a></div>
<span class="pageno">4 / 80</span></div>

<!--
Llama is the language model, Ollama is the local service used to run it, and the application controls which tools can execute. Our recorded wrappers return schema-constrained JSON choices. They do not use Ollama’s native tool_calls protocol. Python validates and interprets the choice before calling numerical functions. Good JSON formatting does not make a claim physically correct. No classroom cell sends an equipment command.
Takeaway: 
Nominal duration: 2.5 minutes.

Full sources:
Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

Ollama documentation maintainers. Structured Outputs: generating structured JSON with a schema. Official Ollama documentation. Reviewed 24 October 2026.
Full source: https://docs.ollama.com/capabilities/structured-outputs

Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/research/building-effective-agents
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>An agent needs a goal, tools and a place to stop</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/bridge_agent_parts.svg" alt="Teaching model of a bounded agent. Each result updates the case record before the next choice." style="height:330px;max-height:330px"><figcaption>Teaching model of a bounded agent. Each result updates the case record before the next choice.</figcaption></figure><ul><li>Give the agent approved data, a small tool list and a saved record of what has been tried.</li><li>After each result, let it choose the next permitted step within explicit check and stop rules.</li></ul></div>
<div class="sources">Source: <a href="https://www.anthropic.com/research/building-effective-agents">Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.</a></div>
<span class="pageno">5 / 80</span></div>

<!--
Walk around the loop once. State means the saved case record: input snapshot, selected candidate, tool outcomes and remaining study budget. A tool is an application function, such as running a power-flow check or solving a restoration problem. The engineering model, allowed actions, limits and stop conditions belong to the application. A model can request REVIEW when the permitted route cannot resolve a problem. In the original P3 record only two candidate checks are allowed.
Takeaway: 
Nominal duration: 2.5 minutes.

Full sources:
Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/research/building-effective-agents

Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>A useful explanation makes a claim we can check</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/bridge_reason_check.svg" alt="Check the explanation against the recorded facts and tool output." style="height:330px;max-height:330px"><figcaption>Check the explanation against the recorded facts and tool output.</figcaption></figure><ul><li>Read the returned reason. Identify its evidence and the tool result that could support it.</li><li>A clear explanation can still be wrong. Keep the numerical check and the original reply.</li></ul></div>
<div class="sources">Source: <a href="https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py">Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.</a></div>
<span class="pageno">6 / 80</span></div>

<!--
We show only the public reasons returned in the recorded JSON. We do not expose or infer private internal reasoning. Ask whether the statement matches the input, respects the allowed choices and survives the numerical check. Later the restoration reply says it sorted costs correctly while returning the wrong order. That specific error is an opportunity to inspect the application’s guard.
Takeaway: 
Nominal duration: 2.5 minutes.

Full sources:
Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Six terms we will use in the notebook</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/bridge_words.svg" alt="Plain-language meanings. The detailed equations stay in the notebooks and source guide." style="height:330px;max-height:330px"><figcaption>Plain-language meanings. The detailed equations stay in the notebooks and source guide.</figcaption></figure><ul><li>Each term describes one job. The language model chooses among tools that do these jobs.</li><li>A passing result applies only to the inputs, limits and parts of the network that were checked.</li></ul></div>
<div class="sources">Source: <a href="https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.</a></div>
<span class="pageno">7 / 80</span></div>

<!--
MPC plans controls using a forecast. SAC supplies a proposal from a previously trained controller. MILP chooses whole loads while respecting the stated constraints. WLS finds the state that best fits the weighted readings. Evidence binding checks that inputs and command still match a stored result. Model scope means which network parts and physical effects were included. Also define p.u. as a value divided by its stated base: 1.0 p.u. is that base value. A thermal limit here is a current or flow limit. The objective or cost is the numerical score to optimize after required checks pass.
Takeaway: 
Nominal duration: 2.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Know what is running and what is being replayed</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/bridge_modes.svg" alt="Three explicitly labeled teaching modes used throughout this workshop." style="height:330px;max-height:330px"><figcaption>Three explicitly labeled teaching modes used throughout this workshop.</figcaption></figure><ul><li>Green: run a numerical calculation now. Amber: read an actual saved Llama reply in L10B.</li><li>Blue: discuss a proposed advisory pilot for a control room after the hands-on work.</li></ul></div>
<div class="sources">Source: <a href="https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md">Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.</a></div>
<span class="pageno">8 / 80</span></div>

<!--
Point to these evidence modes throughout the session. Default classroom cells calculate fresh results without a live language-model call. L10B displays verified historical Llama choices, original reasons and associated recorded results. Changing your L2 or L6 input does not change those old replies. The final control-room diagrams are a proposed teaching design, not evidence of a deployed utility platform. No new equipment operation occurs in any of these modes.
Takeaway: 
Nominal duration: 2.5 minutes.

Full sources:
Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).
Full source: https://doi.org/10.6028/NIST.SP.800-82r3
Full paper: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf
Publication: https://csrc.nist.gov/pubs/sp/800/82/r3/final
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<h1>Open one notebook for all three cases</h1>
<div class="content"><p class="activity-link"><a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Open Classroom Labs in Google Colab</a></p><p class="callout">Classroom_Labs.ipynb</p><ul><li>Open Classroom Labs from the source link or the website’s first Colab button.</li><li>Save a copy in Drive to keep your changes and results.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.</a></div>
<span class="pageno">9 / 80</span></div>

<!--
Open https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/#notebooks and choose the first notebook, Classroom Labs. The LangGraph and trace notebooks are separate companions. Keep the slides in one tab and Classroom Labs in another.
Takeaway: 
Nominal duration: 1.5 minutes.

Full sources:
Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<h1>Connect a CPU and run setup</h1>
<div class="content"><ul><li>Choose a standard CPU. Run “Set up Google Colab (CPU)” and wait for Ready.</li><li>Setup gets the data, saved model weights and records, then installs the needed packages.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.</a></div>
<span class="pageno">10 / 80</span></div>

<!--
For a paced workshop, run the setup cell first, then run each named lesson cell when prompted. Runtime > Run all also works, but it reveals later outputs before the prediction questions. The default route needs no GPU, API key or LLM download. If setup stops, reconnect the runtime and rerun setup before starting L0.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<h1>Find each task by its L label</h1>
<div class="content"><ul><li>Use the headings L0 through L12 to find each task.</li><li>Run the whole cell with its play button or Shift+Enter. Later cells need earlier results.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.</a></div>
<span class="pageno">11 / 80</span></div>

<!--
The added Colab setup cells changed the numerical cell positions. Use the L headings and stable cell IDs to find the same source in Colab, Jupyter and these slides. A slide shows only the relevant code fragment. Students should run the complete matching notebook cell.
Takeaway: 
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L0 · classroom-002</div>
<h1>Run L0: choose the classroom route</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L0 (classroom-002), source lines 11–14.</p><pre class="teaching-code">RUN_OPENDSS = False       # True: fresh full-model audit + separate AC MPC solve in L5
RUN_LOCAL_LLAMA = False   # True: one optional local call in L11
ROOT = Path.cwd()
assert (ROOT / &#x27;data/lindistflow3_network.json&#x27;).exists(), &#x27;Start Jupyter in the tutorial folder&#x27;</pre><ul><li>Keep both switches False: new numerical checks, saved controller and archived model replies.</li><li>If the data check fails, rerun setup before continuing.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004.</a></div>
<span class="pageno">12 / 80</span></div>

<!--
Run all of L0 to import the helpers, configure the plots and initialize the timing record. Keep RUN_OPENDSS=False and RUN_LOCAL_LLAMA=False. These settings skip the optional full-feeder OpenDSS route and local model service. They do not make the calculations prerecorded: L2 and L4 through L9 run fresh numerical calculations or checks, while L12 checks the evidence binding and simulated readback.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>New results, saved controller, old replies</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/common_operator_loop.svg" alt="Proposed roles in an advisory workflow; the default notebook uses Python and saved records." style="height:305px;max-height:305px"><figcaption>Proposed roles in an advisory workflow; the default notebook uses Python and saved records.</figcaption></figure><ul><li>FRESH means calculated now. SAVED POLICY uses old weights to make a new control proposal.</li><li>ARCHIVED ACTUAL LLM means an old model reply, shown with its original input and timing.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004.</a></div>
<span class="pageno">13 / 80</span></div>

<!--
A script follows rules written in code. An LLM agent can choose the next allowed tool from a task and the returned results. The diagram shows proposed responsibilities, not a live agent run in this notebook. Ordinary Python functions do the engineering calculations here; the notebook does not run through LangGraph. A saved policy uses learned weights to calculate a new proposal without retraining. Displaying an old language-model reply does not make a new model call. A language model does not replace the power-flow calculation, load-selection solver or state estimator.
Takeaway: 
Nominal duration: 1.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L1 · classroom-004</div>
<h1>Run L1: does the evidence still match?</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L1_binding.png" alt="Reference L1 output: only the unchanged request and command match the evidence." style="max-height:345px;height:auto"><figcaption>Reference L1 output: only the unchanged request and command match the evidence.</figcaption></figure></div><ul><li>Read binding_pass: does the record match the same inputs and command?</li><li>Expect True, False, False. Changing the load or command breaks that match.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004.</a></div>
<span class="pageno">14 / 80</span></div>

<!--
Evidence binding means matching a checked record to the exact inputs, proposed command and returned result, using content hashes. Treat L1 as a same-content check, not a test that a physical action passes its limits. The first row keeps the request and command unchanged. The next two rows change a request field or command field, so binding_pass is True, False, False. A failed match calls for new evidence; it does not prove the changed action fails its limits. A matching hash also does not authenticate a sensor.
Takeaway: 
Nominal duration: 1.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Use the same experiment cycle</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/common_evidence_binding.svg" alt="Keep the request, proposed command and checked result together." style="height:305px;max-height:305px"><figcaption>Keep the request, proposed command and checked result together.</figcaption></figure><ul><li>Predict, run the default, read the result, change one input and rerun.</li><li>Name the next allowed step and the evidence for it.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004.</a></div>
<span class="pageno">15 / 80</span></div>

<!--
Pause before showing each output. Ask pairs to write one sentence predicting the change, then compare it with the calculated result. Keep the input values and evidence together. Change only one parameter in the first experiment.
Takeaway: 
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<h1>Keep a short experiment record</h1>
<div class="content"><ul><li>Write down the L label and the value you changed.</li><li>Record the result, what the model covers, and your next step: continue, recheck or HOLD.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.</a></div>
<span class="pageno">16 / 80</span></div>

<!--
Participants can add a text cell below an output or use paper notes; no extra software is needed. Each pair should finish with one changed-input experiment that another person can repeat. Explain the result and one limit on the claim. The three cases use different networks and do not form a single utility deployment study. Model scope means which parts of the network, quantities and physical effects the calculation covers.
Takeaway: 
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L2 · classroom-007</div>
<h1>Voltage: open L2</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/feeder.png" alt="Synthetic SMART-DS teaching feeder; not an operating utility circuit." style="max-height:345px;height:auto"><figcaption>Synthetic SMART-DS teaching feeder; not an operating utility circuit.</figcaption></figure></div><ul><li>MPC makes a forecast-based plan. SAC is a saved learned controller.</li><li>Check limits first. Then compare penalty score J; smaller is preferred after the checks pass.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">17 / 80</span></div>

<!--
The feeder is a synthetic SMART-DS Greensboro-area example, not a measured utility circuit. The command sets active- and reactive-power participation for an inverter fleet. MPC, model predictive control, uses a system model and a short forecast to calculate a plan under limits; here the proposed command is the first step of that plan. SAC, Soft Actor–Critic, is a saved controller learned from rewards. It produces a proposal from old weights without training again. The default calculation covers medium-voltage (MV) phases and MV line currents, with simplified low-voltage (LV) aggregation. Feasible means the proposal passes the limits represented by that model. Compare the penalty score J only after checking those limits; smaller J is preferred for this stated objective. Run L0 and L1 first.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Existing GridGuard workshop / SMART-DS synthetic-feeder extraction. Synthetic Greensboro feeder uhs20_1247–udt8894: model map and declared study scope. Existing teaching snapshot reviewed 18 October 2026.
Full source: https://data.openei.org/submissions/2981
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L2 · classroom-007</div>
<h1>Control settings and limits</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/voltage_capability.svg" alt="Active and reactive settings share the inverter’s power limit." style="height:305px;max-height:305px"><figcaption>Active and reactive settings share the inverter’s power limit.</figcaption></figure><ul><li>a sets active-power participation; b sets reactive-power participation.</li><li>Check the inverter limits, modeled voltages and allowed line current.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">18 / 80</span></div>

<!--
Active power delivers net energy; reactive power supports the AC voltage and current balance. The command uses P_i = a S_i and Q_i = b S_i. Its bounds are 0 <= a <= 1, |b| <= 0.44 and a^2 + b^2 <= 1. Modeled voltages must be between 0.95 and 1.05 per unit (p.u.), where values are divided by a stated base. RATING_FRACTION=0.80 sets allowed current to 80% of the nominal rating. The displayed current percentage uses this reduced allowance as its denominator. Passing the inverter bounds alone does not show that network limits pass.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L2 · classroom-007</div>
<h1>Run L2 with the default inputs</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L2 (classroom-007), source lines 1–4.</p><pre class="teaching-code">LOAD_SCALE = 1.0
RATING_FRACTION = 0.80
started = time.perf_counter()
voltage = lab.voltage_lab(LOAD_SCALE, RATING_FRACTION)</pre><ul><li>Run all of L2 to calculate the MPC plan and check the saved SAC controller’s proposal.</li><li>Read feasible, current_step_J and max_allowed_current_pct.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">19 / 80</span></div>

<!--
Start with LOAD_SCALE=1.0 and RATING_FRACTION=0.80. The saved SAC actor produces a new proposal by inference; it is not trained in this cell. Both proposals pass the default classroom checks. MPC has the lower current-step J for this case and objective. This single result does not establish a universal control advantage. The output field feasible reports whether the modeled limits pass; current_step_J is this step’s penalty score, and max_allowed_current_pct is maximum current as a percentage of the reduced allowance.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

James B. Rawlings; David Q. Mayne; Moritz M. Diehl. Model Predictive Control: Theory, Computation, and Design, second edition. Nob Hill Publishing. 2017.
Full source: https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-1st-printing.pdf

Tuomas Haarnoja; Aurick Zhou; Pieter Abbeel; Sergey Levine. Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor. Proceedings of the 35th International Conference on Machine Learning, PMLR 80, pp. 1861–1870. 2018.
Full source: https://proceedings.mlr.press/v80/haarnoja18b.html
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L2 · classroom-007</div>
<h1>Read the voltage and current plots</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L2_plot.png" alt="Reference L2 plots; rerun L2 to calculate plots for your inputs." style="max-height:345px;height:auto"><figcaption>Reference L2 plots; rerun L2 to calculate plots for your inputs.</figcaption></figure></div><ul><li>Left: compare the sorted modeled voltages with the allowed band.</li><li>Right: compare line current with the 100% allowed-current limit.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">20 / 80</span></div>

<!--
The left panel sorts each voltage curve separately. The same horizontal position means the same rank, not necessarily the same physical bus. The right panel reports current relative to the reduced allowance. Use the output table for exact extrema and feasibility; do not decide acceptance from a plot alone.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L2 · classroom-007</div>
<h1>Check limits before comparing scores</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L2_table.png" alt="Reference L2 output with LOAD_SCALE=1.0 and RATING_FRACTION=0.80." style="max-height:345px;height:auto"><figcaption>Reference L2 output with LOAD_SCALE=1.0 and RATING_FRACTION=0.80.</figcaption></figure></div><ul><li>Default MPC passes: current use 73.62%, penalty score J about 0.03110.</li><li>Default saved SAC passes: current use 51.68%, J about 0.43643.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">21 / 80</span></div>

<!--
In the reference execution, MPC returns a=0.960307 and b=-0.111114, with Vmin=1.023874 and Vmax=1.038709 p.u. SAC returns a=0.340066 and b=0.014024, with Vmin=1.013243 and Vmax=1.030000 p.u. Values may vary slightly with the solver or dependency version. Lower current use need not mean lower J, because the objective also includes service and control terms. Check feasibility before comparing J. Both voltage extrema are within the stated 0.95–1.05 p.u. band for this represented MV model.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous exercise-slide">

<div class="eyebrow">Classroom Labs · L2 · classroom-007</div>
<h1>Exercise 1: tighten the current allowance</h1>
<div class="content"><pre class="source-excerpt">RATING_FRACTION = 0.75</pre><ul><li>In L2, change only RATING_FRACTION from 0.80 to 0.75. Predict, then rerun.</li><li>For each method, report feasible, allowed-current use and current_step_J.</li><li>Does a PASS cover the full medium- and low-voltage network? Explain.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">22 / 80</span></div>

<!--
Allow one minute to predict, two minutes to edit and run, and one minute to report. Keep LOAD_SCALE=1.0. Reference allowed-current use is 78.527895% for MPC and 54.854158% for SAC; both remain feasible. Do not ask learners to find a rejection that this edit does not produce. The default model still covers MV only.
Takeaway: 
Nominal duration: 4 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L2 · classroom-007</div>
<h1>Debrief: both proposals still pass</h1>
<div class="content"><p class="callout">Both candidates still pass</p><ul><li>At 0.75, both pass: MPC uses about 78.53% of the allowance; SAC uses about 54.85%.</li><li>The tighter allowance raises current use as a percentage, but does not cause failure here.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">23 / 80</span></div>

<!--
An incorrect prediction is useful evidence, not a failed exercise. Compare the hypothesis with the actual output. Both candidates retain enough headroom in this case. An optimizer may change its command when a constraint changes, so a simple fixed-ratio argument does not apply to every scenario. The model scope has not expanded.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L2 · classroom-007</div>
<h1>Reset L2 before reading old model choices</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L2 (classroom-007), source lines 1–2.</p><pre class="teaching-code">LOAD_SCALE = 1.0
RATING_FRACTION = 0.80</pre><ul><li>Restore the default values and rerun L2.</li><li>L3–L5 use the original test_01 case, separate from your changed L2 experiment.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">24 / 80</span></div>

<!--
Make the experiment boundary explicit. L3 loads a separate preserved context into pool. It does not inherit the fresh L2 case or the participant's edits. Do not pair an edited L2 result with the test_01 model explanation as though the model had seen those new inputs.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L3 · classroom-010</div>
<h1>L3 opens a separate recorded case</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L3 (classroom-010), source lines 1–2.</p><pre class="teaching-code">pool = lab.saved_pool(&#x27;test_01&#x27;)
display(pd.DataFrame(pool[&#x27;responses&#x27;])[[&#x27;model_id&#x27;, &#x27;operation_id&#x27;, &#x27;reason&#x27;, &#x27;seconds&#x27;, &#x27;source&#x27;]])</pre><ul><li>Run L3. Read the original case ID, requested operations and recorded seconds.</li><li>These reasons are old model replies. Displaying them makes no new model call.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context.</a></div>
<span class="pageno">25 / 80</span></div>

<!--
The output contains three actual replies from the frozen response-selection study. Ask learners to identify the operation and numerical parameters requested by each reply. The reported seconds measure the original model calls, not today's display cell. Keep this archived context separate from the fresh L2 comparison.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L3 · classroom-010</div>
<h1>What did the models choose?</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/voltage_canonical_trial.svg" alt="Three old replies request two distinct operations; two votes select reactive-power relaxation." style="height:305px;max-height:305px"><figcaption>Three old replies request two distinct operations; two votes select reactive-power relaxation.</figcaption></figure><ul><li>Different wording can request the same tool and numbers.</li><li>The notebook groups matching trials. An explanation alone does not show that limits pass.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context.</a></div>
<span class="pageno">26 / 80</span></div>

<!--
The three old replies reduce to two distinct operations after matching their tool names and numerical parameters. The vote keeps one contribution per model. In test_01, two models vote for the Q-relaxation trial, which relaxes a reactive-power restriction in that declared test. This diagram shows the old input and choices; it is not a new vote after a learner edits L2. Grouping matching trials avoids counting different wording as different physical proposals.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L4 · classroom-013</div>
<h1>Run L4: check the old choice again</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L4 (classroom-013), source lines 5–9.</p><pre class="teaching-code">started = time.perf_counter()
selected_trials = lab.trial_saved_selection(pool)
timings[&#x27;L4 new verification of archived choices&#x27;] = time.perf_counter() - started
display(selected_trials[&#x27;table&#x27;])
assert pool[&#x27;frozen&#x27;] and pool[&#x27;training_updates&#x27;] == 24</pre><ul><li>After L3, run L4. Python checks the selected proposal again for its original case.</li><li>Compare majority vote with the saved LinUCB selector on that same case.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices.</a></div>
<span class="pageno">27 / 80</span></div>

<!--
The selector is frozen and makes no training updates in this lesson. L4 applies the archived selected operation to its original test context and runs a fresh numerical check. This is a replay with new verification, not a new language-model decision or an online learning experiment. LinUCB is a learned selector that scores the available choices from context; its saved settings stay fixed here.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L4 · classroom-013</div>
<h1>Separate the old choice from the new check</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L4_checks.png" alt="Reference L4 output: old selector choices, new numerical checks of the original case." style="max-height:345px;height:auto"><figcaption>Reference L4 output: old selector choices, new numerical checks of the original case.</figcaption></figure></div><ul><li>Both selectors choose the same reactive-power relaxation trial and pass the new MV check.</li><li>Predicted reward is a learned score. Read new_check_passes for the engineering check.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices.</a></div>
<span class="pageno">28 / 80</span></div>

<!--
The reference J is about 0.031082 for both selectors. The predicted reward is around -0.0075. It is a learned score, not a feasibility flag. Read new_check_passes for the engineering result. This one case does not show that learned selection is better than voting.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L5 · classroom-016</div>
<h1>Run L5: check what the model covers</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L5 (classroom-016), source lines 1–4.</p><pre class="teaching-code">started = time.perf_counter()
scope_audit = lab.backend_audit(pool, run_opendss=RUN_OPENDSS)
timings[&#x27;L5 selected model scope checks&#x27;] = time.perf_counter() - started
display(scope_audit[&#x27;table&#x27;])</pre><ul><li>Keep RUN_OPENDSS=False. Run L5 and read the table and optional_mode message.</li><li>L5 checks the original test_01 MV-MPC plan. OpenDSS is disabled.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model.</a></div>
<span class="pageno">29 / 80</span></div>

<!--
L5 rebuilds the original test_01 case and runs a new check on its original MV-MPC incumbent, meaning the baseline plan saved with that case. This is not the reactive-power-relaxation candidate checked in L4. With RUN_OPENDSS=False, L5 checks only the reduced model and reports that OpenDSS is disabled. This CPU route performs no new full-feeder AC check. A wider-model study saved earlier is not a result calculated today. Model scope means the network parts and physical effects that a check represents.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L5 · classroom-016</div>
<h1>A PASS covers only the model checked</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L5_scope.png" alt="Reference L5 output: a medium-voltage check with OpenDSS disabled." style="max-height:345px;height:auto"><figcaption>Reference L5 output: a medium-voltage check with OpenDSS disabled.</figcaption></figure></div><ul><li>This check covers medium-voltage (MV) phases and currents, not all low-voltage (LV) equipment.</li><li>For a full MV/LV request, get the wider check or HOLD.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model.</a></div>
<span class="pageno">30 / 80</span></div>

<!--
Ask a participant to read the explicit scope message aloud. A PASS is conditional on the model and action that were checked. The default model does not cover every LV constraint. A more confident explanation cannot supply the missing model coverage.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Preview · L12 after all three cases</div>
<h1>Preview the L12 handover</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/voltage_operator_packet.svg" alt="Preview only: L12 checks model coverage before a simulated readback." style="height:305px;max-height:305px"><figcaption>Preview only: L12 checks model coverage before a simulated readback.</figcaption></figure><ul><li>L12 uses selected_trials from L4, not the new L2 comparison.</li><li>Finish L6–L11 first. Run L12 at the end, in notebook order.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only.</a></div>
<span class="pageno">31 / 80</span></div>

<!--
Preview the purpose of the final handoff without asking participants to jump ahead. L12 will use selected_trials from L4, not the fresh L2 comparison. It contrasts a full MV/LV request with an explicit MV-only teaching request. Continue to L6 after the voltage checkpoint, finish L6–L11, and run L12 once in the closing section. The readback is a simulated teaching event with no equipment dispatch.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Preview · L12 · run at the end</div>
<h1>Preview the two handover outcomes</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L12_packet.png" alt="Reference L12 output; run this cell at the end of the workshop." style="max-height:345px;height:auto"><figcaption>Reference L12 output; run this cell at the end of the workshop.</figcaption></figure></div><ul><li>Full MV/LV request: HOLD. An explicit MV teaching request can pass a simulated readback.</li><li>A wrong recommendation ID is rejected. equipment_dispatch stays False.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only.</a></div>
<span class="pageno">32 / 80</span></div>

<!--
This screenshot previews the executed default L12 result; students have not run L12 yet. At the final step they will check the returned state and acknowledgment fields. The full-coverage request remains HOLD; the explicit MV teaching scope allows a simulated readback. The simulation does not complete human approval of an archived study and does not dispatch equipment.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L5 · classroom-016</div>
<h1>Voltage checkpoint: say what ran</h1>
<div class="content"><ul><li>L2 makes new proposals; L3 shows old replies; L4–L5 run new checks on test_01.</li><li>Report the inputs, proposal, model coverage and result before naming the next step.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model.</a></div>
<span class="pageno">33 / 80</span></div>

<!--
Give pairs 30 seconds to describe the sequence without calling every step an AI decision. L2 calculates an MPC plan and a saved-policy proposal for the current classroom inputs. L3 displays old model replies. L4 runs new checks of the selected trials; L5 checks the original archived plan and its model coverage. Numerical tools provide the physical evidence. The old model choices select a permitted trial; they do not replace these checks. The operator receives an advisory record whose stated coverage must match the request.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>Restoration: open L6</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/restoration_fault_map.svg" alt="Six-node active-power teaching graph with whole-load pickup and one unavailable branch." style="height:305px;max-height:305px"><figcaption>Six-node active-power teaching graph with whole-load pickup and one unavailable branch.</figcaption></figure><ul><li>Use the six-node teaching graph. Keep the faulted branch unavailable.</li><li>Compare total restored load with restored critical load.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">34 / 80</span></div>

<!--
This six-node graph is separate from the voltage feeder. It represents active-power transport, not AC power flow or a time-ordered field switching procedure. Loads are picked up as whole blocks. A tie is an alternative connection that can supply load; CAPACITIES_KW sets its transfer limit in kilowatts.
Takeaway: 
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>Choose the service goal before the plan</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/restoration_priority.svg" alt="Different service goals can select different loads on the same network." style="height:305px;max-height:305px"><figcaption>Different service goals can select different loads on the same network.</figcaption></figure><ul><li>The priority goal gives more weight to two critical loads.</li><li>The comparison goal serves the most total kW, using the same network and pickup rules.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">35 / 80</span></div>

<!--
Critical demand totals 90 kW: 60 kW at node 2 and 30 kW at node 5. The objective is the service goal encoded as a score. The priority score gives more weight to these critical loads, while the comparison score maximizes total kW. The difference in selected service comes from that goal. Both numerical methods use the same graph, capacities and whole-load pickup rules. Neither needs a language model to solve this declared problem.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>Run L6: change the tie capacity</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L6 (classroom-018), source lines 1–5.</p><pre class="teaching-code">CAPACITIES_KW = (40., 60., 80., 100., 120.)
started = time.perf_counter()
restoration = lab.restoration_sweep(CAPACITIES_KW)
timings[&#x27;L6 fresh MILP sweep + independent enumeration&#x27;] = time.perf_counter() - started
display(restoration[&#x27;table&#x27;].drop(columns=&#x27;pickup&#x27;))</pre><ul><li>Run all of L6. MILP chooses whole loads; an exhaustive search checks its priority score.</li><li>Read served_kw, critical_kw and MILP_matches_exhaustive_check.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">36 / 80</span></div>

<!--
MILP means mixed-integer linear programming. Here it is a whole-load chooser: on/off choices decide which load blocks are served, while linear constraints enforce the stated network rules. Start with tie capacities of 40, 60, 80, 100 and 120 kW. The solver enforces active-power balance, capacity limits, connection to a source, no loops in the energized graph, and exclusion of the faulted branch. An independent exhaustive search checks the priority score on this small graph. Agreement supports this formulation; it does not check the AC physics left out of the model.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>Read both service plots</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L6_plot.png" alt="Reference L6 plots; rerun L6 to compare your chosen tie capacities." style="max-height:345px;height:auto"><figcaption>Reference L6 plots; rerun L6 to compare your chosen tie capacities.</figcaption></figure></div><ul><li>Left: total load served in kW. Right: critical load served in kW.</li><li>Overlapping markers mean the two plans give the same result at that tested capacity.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">37 / 80</span></div>

<!--
The markers show sampled capacities rather than a continuous ramp between whole-load pickup plans. A higher capacity may still be too small to add another complete load block. Read both total and critical service before choosing the policy that matches the request.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>The tradeoff at a 40 kW tie limit</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L6_table.png" alt="Reference L6 results at a 40 kW tie limit: compare total and critical load served." style="max-height:345px;height:auto"><figcaption>Reference L6 results at a 40 kW tie limit: compare total and critical load served.</figcaption></figure></div><ul><li>Priority goal: 130 kW total, including 90 kW of critical load.</li><li>Most-total-kW goal: 140 kW total, including 30 kW of critical load.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">38 / 80</span></div>

<!--
Compare the first two output rows, where tie_capacity_kw=40. The priority plan serves 10 kW less total demand while preserving 60 kW more critical demand. These results compare two service objectives, not AI with no AI.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>How Python checks the plan</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/restoration_verify.svg" alt="Python checks the stated graph constraints, then compares the priority score independently." style="height:305px;max-height:305px"><figcaption>Python checks the stated graph constraints, then compares the priority score independently.</figcaption></figure><ul><li>Check paths to a source, capacity limits, power balance and the faulted branch.</li><li>Then compare the MILP service score with the independent exhaustive search.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">39 / 80</span></div>

<!--
Numerical checks and same-content evidence matching answer different questions. A record can match the inputs exactly while still omitting AC voltage, reactive-power or protection limits. Comparing the MILP score with every permitted plan is an independent check of this small stated problem. Minimizing energized branches does not calculate the number or order of physical switching steps.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Ying Wang, Yin Xu, Jiaxu Li, Jinghan He, Xiaojun Wang. On the Radiality Constraints for Distribution System Restoration and Reconfiguration Problems. Author preprint, arXiv:1912.05185v3. 15 March2020(v3); first submitted11 December2019.
Full source: https://arxiv.org/abs/1912.05185v3
Full paper: https://arxiv.org/pdf/1912.05185v3

Bo Chen, Chen Chen, Jianhui Wang, Karen L. Butler-Purry. Sequential Service Restoration for Unbalanced Distribution Systems and Microgrids. IEEE Transactions on Power Systems33(2),1507–1520. March2018.
Full source: https://doi.org/10.1109/TPWRS.2017.2720122
-->

---
transition: none
---

<div class="lesson teaching rigorous exercise-slide">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>Exercise 2: add more tie capacity</h1>
<div class="content"><pre class="source-excerpt">CAPACITIES_KW = (40., 60., 80., 100., 120., 180.)</pre><ul><li>Add 180. to CAPACITIES_KW, keeping 40. first. Predict, then rerun L6.</li><li>Compare total and critical load served at 40 and 180 kW.</li><li>At which of these two capacities do the service goals give the same result?</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">40 / 80</span></div>

<!--
Allow one minute to predict, two minutes to edit and run, and one minute to report. At 180 kW, both methods serve 250 kW total and 90 kW critical demand. Keep 40 kW first in the list because L7 binds the first result to the first capacity. Do not reorder the list for this exercise.
Takeaway: 
Nominal duration: 4 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>Debrief: the tradeoff disappears here</h1>
<div class="content"><p class="callout">250 kW total / 90 kW critical</p><ul><li>At 180 kW, both methods serve 250 kW total and 90 kW of critical load.</li><li>Priority helps in the constrained case. It does not improve every case.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">41 / 80</span></div>

<!--
Compare the 180 kW result with the 40 kW case before generalizing. Equal service at 180 kW follows from this small graph and its demands; it is not a universal threshold. A single success percentage would hide the service-policy question.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L7 · classroom-021</div>
<h1>Reset the capacity list, then run L7</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L7 (classroom-021), source lines 1–3.</p><pre class="teaching-code">rest_record = restoration[&#x27;records&#x27;][0][&#x27;weighted&#x27;]
rest_request = {&#x27;task&#x27;: &#x27;restoration&#x27;, &#x27;capacity_kw&#x27;: CAPACITIES_KW[0],
                &#x27;critical_nodes&#x27;: [2, 5], &#x27;model&#x27;: &#x27;six_node_active_transport&#x27;, &#x27;revision&#x27;: 1}</pre><ul><li>Restore the original CAPACITIES_KW list and rerun L6.</li><li>L7 checks the first 40 kW record, then changes the request to 20 kW.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding.</a></div>
<span class="pageno">42 / 80</span></div>

<!--
Keeping 40 kW first already preserves the L7 example. Resetting the list also makes the saved notebook easy to compare with the default. L7 changes the request capacity and revision without solving a new case. It tests whether the old evidence can still be used.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L7 · classroom-021</div>
<h1>Read the evidence-match test</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L7_binding.png" alt="Reference L7 output: changed request, unchanged evidence, so a new check is needed." style="max-height:345px;height:auto"><figcaption>Reference L7 output: changed request, unchanged evidence, so a new check is needed.</figcaption></figure></div><ul><li>Original request: True. Changed rating with the old evidence: False.</li><li>HOLD the old recommendation and request a new solve.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding.</a></div>
<span class="pageno">43 / 80</span></div>

<!--
This output reports evidence binding, not physical infeasibility. A separate fresh solve at 20 kW still gives the 130 kW total and 90 kW critical priority outcome on this graph. L7 itself does not run that solve. Replace the stale evidence because it belongs to a different request, even when the old plan might remain feasible.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L7 · classroom-021</div>
<h1>Changed inputs need a new check</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/restoration_stale.svg" alt="L7 changes capacity and revision; extra topology labels are teaching examples." style="height:305px;max-height:305px"><figcaption>L7 changes capacity and revision; extra topology labels are teaching examples.</figcaption></figure><ul><li>“The evidence is old” does not mean “the changed plan fails its limits.”</li><li>Update the request, solve and check it, then match the new evidence to that request.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding.</a></div>
<span class="pageno">44 / 80</span></div>

<!--
Evidence binding asks whether a record matches the exact request, proposed plan and returned result. The diagram’s extra topology labels are teaching illustrations. The runnable L7 example changes only the request capacity and revision; students do not change topology in that cell. Old evidence is unusable for a changed request even if the old plan might still pass its limits. Ask which new numerical check would establish that for the changed request.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>Proposed agent role: keep the service goal</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/restoration_plan.svg" alt="Proposed agent responsibilities; the current notebook cell runs Python." style="height:305px;max-height:305px"><figcaption>Proposed agent responsibilities; the current notebook cell runs Python.</figcaption></figure><ul><li>This cell runs Python: the operator sets the goal and limits; MILP chooses the whole loads.</li><li>A proposed agent would request that solve and explain the returned tradeoff.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">45 / 80</span></div>

<!--
This is a proposed role for an agent, not a new model decision in the default notebook. The current supervisor is ordinary Python. A future language-model agent could request the allowed solve and explain the returned tradeoff. It must preserve the operator’s service goal and limits, rather than quietly changing weights or making up load values. A different service goal requires an explicit new request and solve. The numerical difference here comes from the optimization objective.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>What this model does not check</h1>
<div class="content"><ul><li>This active-power graph does not check AC voltage, reactive power or protection.</li><li>The energized branches do not give the order of field switching steps.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">46 / 80</span></div>

<!--
State this boundary clearly and briefly. The result is useful within its declared transport formulation. Actual restoration requires the utility's engineering checks, operating procedure and separate authority.
Takeaway: 
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L7 · classroom-021</div>
<h1>Restoration checkpoint: name the next step</h1>
<div class="content"><ul><li>At 40 kW, explain 130 total / 90 critical versus 140 total / 30 critical, all in kW.</li><li>For a changed request, keep HOLD until evidence for the current request is available.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding.</a></div>
<span class="pageno">47 / 80</span></div>

<!--
Ask each pair to give one number and one condition. They should distinguish three decisions: selecting a service policy, checking current evidence and authorizing a physical switching operation.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L8 · classroom-023</div>
<h1>Cyber: open L8</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/cyber_network.svg" alt="Four-bus linear DC teaching model; known synthetic truth is used only for offline comparison." style="height:305px;max-height:305px"><figcaption>Four-bus linear DC teaching model; known synthetic truth is used only for offline comparison.</figcaption></figure><ul><li>Use the separate four-bus DC model and its supplied readings.</li><li>Compare a residual alarm, which checks fit, with error against the known teaching truth.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">48 / 80</span></div>

<!--
The separate four-bus linear DC model has three unknown voltage angles, measured relative to a reference bus, and eight readings. This DC approximation is not a full AC estimator, malware detector or sensor-authentication system. Synthetic truth is known for the offline classroom comparison only. A residual checks how well the estimate fits the supplied readings; state error checks how far the estimate is from the known teaching truth.
Takeaway: 
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L8 · classroom-023</div>
<h1>Best fit and true state are different</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/cyber_residual.svg" alt="A good fit to readings does not show that those readings are authentic." style="height:305px;max-height:305px"><figcaption>A good fit to readings does not show that those readings are authentic.</figcaption></figure><ul><li>WLS finds the best fit to readings, giving more weight to lower stated uncertainty.</li><li>Residual J measures fit mismatch. State error uses teaching truth unavailable to an operator.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">49 / 80</span></div>

<!--
WLS means weighted least squares: find the state that best fits the readings, giving more influence to readings with smaller stated uncertainty. That weighting does not authenticate a reading. Here J is the residual mismatch statistic, not the voltage case’s penalty score. Its chi-square alarm threshold is about 15.086272 for five residual degrees of freedom at a 1% significance level. This calibration depends on the stated linear model and noise assumptions. An operator does not have the synthetic truth used to calculate the plotted state error. A small J does not establish that the readings are authentic.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Fred C. Schweppe, J. Wildes. Power System Static-State Estimation, Part I: Exact Model. IEEE Transactions on Power Apparatus and Systems, PAS-89(1), pp. 120–125. January 1970.
Full source: https://doi.org/10.1109/TPAS.1970.292678
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L8 · classroom-023</div>
<h1>Run L8: compare two data attacks</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L8 (classroom-023), source lines 1–5.</p><pre class="teaching-code">ATTACK_SCALES = (0., .25, .5, 1., 1.5)
started = time.perf_counter()
cyber = lab.cyber_sweep(ATTACK_SCALES)
timings[&#x27;L8 fresh WLS attack sweep&#x27;] = time.perf_counter() - started
display(cyber[&#x27;table&#x27;])</pre><ul><li>Run all of L8 with its default scale list.</li><li>Compare one biased reading with the coordinated Hc shift in the table and plots.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">50 / 80</span></div>

<!--
L8 runs new WLS calculations. An isolated bias changes one reading. The coordinated Hc shift changes readings in a pattern consistent with a different modeled state. This counterexample assumes knowledge of the linear measurement matrix H and access to the modeled unprotected channels. It is a declared defensive teaching model, not evidence of an incident at a utility.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L8 · classroom-023</div>
<h1>Read both cyber plots</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L8_plot.png" alt="Reference L8 plots; rerun L8 to calculate results for your chosen attack scales." style="max-height:345px;height:auto"><figcaption>Reference L8 plots; rerun L8 to calculate results for your chosen attack scales.</figcaption></figure></div><ul><li>Left: residual J and its alarm threshold. Right: error against the known teaching truth.</li><li>Follow the coordinated curve across both plots before calling a quiet alarm reassuring.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">51 / 80</span></div>

<!--
The left plot uses a symmetric-log scale. The right plot compares the estimate with known synthetic truth. As the coordinated shift grows, the residual stays unchanged while the state error increases. These plots answer different questions; they do not express the same quantity in different units.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L8 · classroom-023</div>
<h1>At scale 1, the alarm misses a state error</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/cyber_stealth.svg" alt="Simple consistency illustration; the numerical values come from the eight-reading L8 model." style="height:305px;max-height:305px"><figcaption>Simple consistency illustration; the numerical values come from the eight-reading L8 model.</figcaption></figure><ul><li>One biased reading: J about 277.50, so the residual alarm is True.</li><li>Coordinated Hc: J about 3.92, no alarm, but state error is about 0.02678 rad.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">52 / 80</span></div>

<!--
The diagram is a simple scalar illustration of coordinated consistency, not the numerical eight-measurement system. Read the numerical values from L8. A larger false-data shift need not increase the residual when the shift lies in the modeled measurement subspace. The state error is measured in radians; it is available here because this is an offline test with known synthetic truth.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Yao Liu, Peng Ning, Michael K. Reiter. False Data Injection Attacks against State Estimation in Electric Power Grids. ACM Transactions on Information and System Security, 14(1), Article 13, 33 pages. May 2011.
Full source: https://doi.org/10.1145/1952982.1952995
Full paper: https://reitermk.github.io/papers/2011/TISSEC2.pdf
-->

---
transition: none
---

<div class="lesson teaching rigorous exercise-slide">

<div class="eyebrow">Classroom Labs · L8 · classroom-023</div>
<h1>Exercise 3: add a small isolated bias</h1>
<div class="content"><pre class="source-excerpt">ATTACK_SCALES = (0., .10, .25, .5, 1., 1.5)</pre><ul><li>Add .10 to ATTACK_SCALES. Predict, then rerun L8.</li><li>At scale 0.10, read J, the alarm flag and the error against known teaching truth.</li><li>Does “no alarm” mean the reading is correct? Use both plots to explain.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">53 / 80</span></div>

<!--
Allow one minute to predict, two minutes to edit and run, and one minute to report. For isolated bias at scale 0.10, J is about 10.143237, below the 15.086272 threshold. The alarm is False despite nonzero state error. The coordinated residual stays about 3.920222. This added scale remains within the notebook's plot limits.
Takeaway: 
Nominal duration: 4 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L8 · classroom-023</div>
<h1>Debrief: no alarm does not prove truth</h1>
<div class="content"><p class="callout">10.14 &lt; 15.09 → no residual alarm</p><ul><li>At scale 0.10, the isolated-bias J is about 10.14, below the 15.09 threshold.</li><li>A small bias can miss the threshold. A coordinated shift can preserve the fit.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">54 / 80</span></div>

<!--
Separate the two mechanisms. A small isolated bias can stay below a statistical threshold. A coordinated Hc shift can preserve residual consistency by construction. Neither result establishes trusted telemetry. The state-error curve uses offline synthetic truth, not an input available to an online detector.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L8 · classroom-023</div>
<h1>Reset L8 before the recovery example</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L8 (classroom-023), source lines 1–3.</p><pre class="teaching-code">ATTACK_SCALES = (0., .25, .5, 1., 1.5)
started = time.perf_counter()
cyber = lab.cyber_sweep(ATTACK_SCALES)</pre><ul><li>Restore the original ATTACK_SCALES list and rerun L8.</li><li>L9 uses a fixed recovery case, separate from the scale you changed.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">55 / 80</span></div>

<!--
Explain the boundary before comparing the recovery output. Changing ATTACK_SCALES changes the residual and state-error sweep. It does not change the fixed recovery scenario held inside the demo object.
Takeaway: 
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L9 · classroom-026</div>
<h1>L9 uses a fixed recovery case</h1>
<div class="content"><ul><li>Check the same case with and without replacement readings assumed to be trusted.</li><li>Its control value does not follow your L8 scale change.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">56 / 80</span></div>

<!--
The helper uses the fixed run_wls_demo recovery fixture. The cyber object holds both the sweep results and this shared fixed demo. The comparison tests the trust premise under controlled conditions; it is not a controller reacting continuously to each plotted scale.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L9 · classroom-026</div>
<h1>Trusted readings are an assumption</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/cyber_trusted.svg" alt="Three trusted angle readings are assumed, not authenticated by this calculation." style="height:305px;max-height:305px"><figcaption>Three trusted angle readings are assumed, not authenticated by this calculation.</figcaption></figure><ul><li>The example assumes three independent angle readings are trustworthy.</li><li>The residual check and a model’s explanation cannot authenticate those readings.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">57 / 80</span></div>

<!--
The example assumes three protected angle readings determine the three unknown angles, leaving zero residual degrees of freedom. Independent trusted information must come from a justified source outside this numerical calculation. A zero residual in this exactly determined system adds no detection guarantee. Neither a good model fit nor a language-model explanation establishes authenticity.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L9 · classroom-026</div>
<h1>Run L9: compare HOLD and PROPOSE</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L9 (classroom-026), source lines 1–2.</p><pre class="teaching-code">without_trust = lab.trusted_response(cyber, protected_available=False)
with_trust = lab.trusted_response(cyber, protected_available=True)</pre><ul><li>Run the whole L9 cell, including its assertions.</li><li>Read status first, then the proposed injection and the offline limit-violation count.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">58 / 80</span></div>

<!--
The two calls use the same fixed fixture and change only protected_available. Without the trusted channels, the result is HOLD. With the assumed trusted set, it is PROPOSE. A proposal is neither an acknowledgment nor a dispatch command.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L9 · classroom-026</div>
<h1>Read the two decision states</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L9_trust.png" alt="Reference L9 output for the fixed recovery case, not the edited L8 scale." style="max-height:325px;height:auto"><figcaption>Reference L9 output for the fixed recovery case, not the edited L8 scale.</figcaption></figure></div><ul><li>No trusted replacement readings: HOLD, with no proposed injection.</li><li>Trusted readings assumed: PROPOSE; u ≈ 0.121694 p.u.; zero offline toy-model violations.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">59 / 80</span></div>

<!--
Read the condition column together with the returned state. The PROPOSE outcome depends on the supplied trust assumption and fixed model. The recovery record keeps dispatch=False. It does not use the equipment_dispatch field from the separate L12 readback example.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L9 · classroom-026</div>
<h1>Check the numerical correction</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/cyber_qp.svg" alt="Fixed L9 correction: compare the predicted branch flow with the offline truth check." style="height:305px;max-height:305px"><figcaption>Fixed L9 correction: compare the predicted branch flow with the offline truth check.</figcaption></figure><ul><li>The QP solver minimizes effort, subject to branch limits and a 0.01 p.u. margin.</li><li>Predicted flow12: 0.17000; offline actual: about 0.17046, below the 0.18000 rating.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">60 / 80</span></div>

<!--
QP means quadratic programming: this numerical solver minimizes a quadratic effort score while enforcing the declared branch limits and a 0.01 p.u. margin. The flexible injection is u=0.1216936673 p.u., balanced by the reference bus. Predicted flow12 is 0.17000 p.u.; the offline actual flow is about 0.17046 p.u., below the 0.18000 p.u. rating. The actual-flow comparison uses synthetic truth for this fixed case. It does not guarantee AC behavior omitted by the model or trustworthy field telemetry.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L9 · classroom-026</div>
<h1>What makes the recovery possible?</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/cyber_handoff.svg" alt="Trusted information and numerical checks have separate roles." style="height:305px;max-height:305px"><figcaption>Trusted information and numerical checks have separate roles.</figcaption></figure><ul><li>Assumed trusted readings support the estimate. The solver calculates a limited correction.</li><li>The explanation must keep those conditions clear and leave the proposal for review.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">61 / 80</span></div>

<!--
Do not attribute recovered information or numerical feasibility to confident prose. The workflow can coordinate the estimator, constrained correction and evidence checks. It cannot invent an independent trusted measurement source.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L9 · classroom-026</div>
<h1>Proposed agent role: request and explain</h1>
<div class="content"><ul><li>This cell runs Python. A proposed agent would request the approved estimate and control check.</li><li>The operator must confirm the trust basis and review the returned proposal.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">62 / 80</span></div>

<!--
The default classroom calls are ordinary deterministic Python functions, so this cell makes no new language-model decision. The slide states a proposed agent responsibility: request the allowed estimator and control tool, then explain the exact conditions returned. The operator must establish the basis for trusting the replacement readings and review the limited proposal through the authorized process. The old model explanations in L10 come from a separate historical study and are not replies to this participant’s changed inputs.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L9 · classroom-026</div>
<h1>Cyber checkpoint: explain why PROPOSE is allowed</h1>
<div class="content"><ul><li>Report the trust assumption, model, proposed u and the checks that passed or failed.</li><li>Without independent trusted information, keep HOLD and name what is missing.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">63 / 80</span></div>

<!--
Ask pairs to state the outcome and its condition in the same sentence. For example: 'The fixture proposes u when the supplied trusted channels are available.' Do not say: 'The AI proved that the telemetry is safe.'
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L10 · classroom-028</div>
<h1>Run L10 before the Llama walkthrough</h1>
<div class="content"><ul><li>Run L10 to inspect its separate archived five-stage study.</li><li>Continue to L10B for the recorded Llama choices, then run L11 with its default False setting.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030.</a></div>
<span class="pageno">64 / 80</span></div>

<!--
L10 reads the archived proposal_complete_workflow study. It includes feeder-catalog restoration and is separate from the L6 six-node MILP and your edited classroom inputs. L10B, inserted immediately after L10, then gives readable verified replay episodes for all three cases. Run L11 after those replays; the default False setting skips a new local model request.
Takeaway: 
Nominal duration: 3 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L10B · classroom-llama-walkthrough</div>
<h1>Run L10B: watch Llama choose a tool</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L10B (classroom-llama-walkthrough), source lines 1–5.</p><pre class="teaching-code">SCENARIO = &quot;voltage&quot;  # Change to &quot;restoration&quot; or &quot;cyber&quot;, then rerun this cell.
from IPython.display import HTML, display
from src.llama_walkthrough import load_episodes, render_episode_html
replay_episodes = load_episodes(ROOT)
display(HTML(render_episode_html(replay_episodes[SCENARIO])))</pre><ul><li>Run the whole L10B cell. Change SCENARIO to inspect each saved episode.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L10B; cell classroom-llama-walkthrough; src/llama_walkthrough.py.</a></div>
<span class="pageno">65 / 80</span></div>

<!--
Run L10 first. In the new L10B cell the helper validates the original JSON reply against the parsed journal and trace, then displays the recorded episode. Change only SCENARIO to inspect the other two episodes. The following slides show selected fields from the same replay. This cell makes no model request and performs no new electrical solve. At the end, run L11 at its default False setting before L12. Llama reasons are historical public returned text. Their correctness must be judged against the input and tool results. SCENARIO can be voltage, restoration or cyber. The full cell is shown.
Takeaway: 
Nominal duration: 2.5 minutes.

Full sources:
Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

Ollama documentation maintainers. Structured Outputs: generating structured JSON with a schema. Official Ollama documentation. Reviewed 24 October 2026.
Full source: https://docs.ollama.com/capabilities/structured-outputs
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>Voltage: Llama asks to check the saved controller</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_voltage_1.png" alt="L10B recorded voltage episode. Selected fields; full record and sources in the guide." style="max-height:380px;height:auto"><figcaption>L10B recorded voltage episode. Selected fields; full record and sources in the guide.</figcaption></figure></div><ul><li>Llama identifies the missing check. The current failure forces a new trial.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: voltage replay, recorded call 1; full record in source guide.</a></div>
<span class="pageno">66 / 80</span></div>

<!--
Read the exact reason. The model was offered VERIFY_SAC_FIRST or REVIEW. The application then checks the saved SAC action in OpenDSS. 111.966607% refers to the allowed current, which was 80% of nominal, so this exceeds the configured allowance. The numerical result records two current violations. This P3 full supplied MV/LV study is separate from L2 and L3 test_01. Ask the audience to predict the next allowed step before advancing.
Takeaway: 
Nominal duration: 2.5 minutes.

Full sources:
Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>Voltage: Llama chooses the existing fallback plan</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_voltage_2.png" alt="L10B recorded voltage episode. Selected fields; full record and sources in the guide." style="max-height:380px;height:auto"><figcaption>L10B recorded voltage episode. Selected fields; full record and sources in the guide.</figcaption></figure></div><ul><li>Llama chooses an existing MPC plan. Python checks whether the result passes.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: voltage replay, recorded call 2; full record in source guide.</a></div>
<span class="pageno">67 / 80</span></div>

<!--
The model selects USE_MPC_PLAN from two allowed choices, the other being REVIEW. It does not invent or solve MPC. The recorded context already supplies a plan and its eligibility. The application performs a fresh numerical check at that historical time. The result is just below the allowed current threshold. No operating permission follows from this check alone. Ask which evidence, rather than wording, makes the fallback eligible for review.
Takeaway: 
Nominal duration: 2.5 minutes.

Full sources:
Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>Voltage: the checks pass and human review remains</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_voltage_3.png" alt="L10B recorded voltage episode. Selected fields; full record and sources in the guide." style="max-height:380px;height:auto"><figcaption>L10B recorded voltage episode. Selected fields; full record and sources in the guide.</figcaption></figure></div><ul><li>Human review remains pending. The fixed script returned the same numerical result.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: voltage replay, recorded call 3; full record in source guide.</a></div>
<span class="pageno">68 / 80</span></div>

<!--
Read the exact REVIEW_EVIDENCE choice and distinguish it from the overall status. The proposed controls are 2387.157 kW and +325.738 kvar. The supplied full MV/LV feeder check returned voltage 1.001783–1.035026 p.u. and zero listed violations. The fixed supervisor used the same SAC-to-MPC sequence with identical numerical output. Recorded workflow intervals were 0.346053 s fixed and 3.110454 s agentic, excluding precomputed MPC/SAC preparation. These are single recorded timings, not performance distributions or a measured reduction in operator workload.
Takeaway: 
Nominal duration: 2.5 minutes.

Full sources:
Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>Restoration: Llama chooses a useful new trial</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_restoration_14.png" alt="L10B recorded restoration episode. Selected fields; full record and sources in the guide." style="max-height:380px;height:auto"><figcaption>L10B recorded restoration episode. Selected fields; full record and sources in the guide.</figcaption></figure></div><ul><li>The new trial serves more load, keeps critical service and passes the current check.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: restoration replay, recorded call 14; full record in source guide.</a></div>
<span class="pageno">69 / 80</span></div>

<!--
Switch L10B to restoration. This is the separate L10 feeder-catalog restoration study, not the L6 six-node MILP. The recorded protocol requires a first refinement but Llama chooses between the offered fractions. SHED_075 disconnects 75% of the ordered noncritical load objects, not 75% of load kW. The exact reason calls improvement a possibility. Python evaluates the trial and finds improved service while the tie loading remains 91.867215% of its allowance. A useful hypothesis becomes evidence only after that check.
Takeaway: 
Nominal duration: 2.5 minutes.

Full sources:
Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>Restoration: the next trial crosses the current limit</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_restoration_15.png" alt="L10B recorded restoration episode. Selected fields; full record and sources in the guide." style="max-height:380px;height:auto"><figcaption>L10B recorded restoration episode. Selected fields; full record and sources in the guide.</figcaption></figure></div><ul><li>The next trial fails the current limit. Keep the previous passed candidate.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: restoration replay, recorded call 15; full record in source guide.</a></div>
<span class="pageno">70 / 80</span></div>

<!--
Keep the actual returned reason visible. It refers to a target in the objective, but its claim should not be accepted as a proved fact. In this record the next trial is numerically rejected for a thermal failure. Restoring more load does not make a failed current check acceptable. Ask participants to explain why the previous passed candidate must remain in the case record. The model’s trial budget is bounded.
Takeaway: 
Nominal duration: 2.5 minutes.

Full sources:
Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>Restoration: catch Llama’s wrong ranking</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_restoration_16.png" alt="L10B recorded restoration episode. Selected fields; full record and sources in the guide." style="max-height:380px;height:auto"><figcaption>L10B recorded restoration episode. Selected fields; full record and sources in the guide.</figcaption></figure></div><ul><li>The returned order is wrong. Python chooses the smaller cost and rechecks the plan.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: restoration replay, recorded call 16; full record in source guide.</a></div>
<span class="pageno">71 / 80</span></div>

<!--
Let pairs answer before discussing the result. Smaller cost is better, so E03 must rank before E02. Llama returns [E02,E03] while its explanation claims lowest score first. The recorded language_order_agrees_with_cost field is False. A deterministic guard retains E03 and rechecks it as E05, with no recorded failures. Human acknowledgment and dispatch remain False. The paired fixed workflow reaches the same final action and cost. This example motivates verification rather than an unsupported superiority claim.
Takeaway: 
Nominal duration: 2.5 minutes.

Full sources:
Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>Cyber: Llama selects the tool already allowed</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_cyber_7.png" alt="L10B recorded cyber episode. Selected fields; full record and sources in the guide." style="max-height:380px;height:auto"><figcaption>L10B recorded cyber episode. Selected fields; full record and sources in the guide.</figcaption></figure></div><ul><li>The task supplies the tool and trust assumption. Python computes the correction.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: cyber replay, recorded call 7; full record in source guide.</a></div>
<span class="pageno">72 / 80</span></div>

<!--
Switch L10B to cyber. This standard four-bus DC record is separate from L10’s proposal-complete cyber record, and matches the Agent Trace notebook T6 archive. The route is narrow: the prompt already authorizes the tool and supplies the trusted-sensor assumption. The three angle readings give full rank but zero residual redundancy, so a good fit is not an independent trust test. u is the flexible injection correction in per unit. Offline synthetic-truth flow is available to the experimenter, not guaranteed available to a real operator.
Takeaway: 
Nominal duration: 2.5 minutes.

Full sources:
Workshop recorded model replies and numerical study records. Standard four-bus cyber study: Llama 3.1:8b tool selection and REVIEW calls 7–8. Public teaching archive. 21 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>Cyber: a passing calculation still needs review</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_cyber_8.png" alt="L10B recorded cyber episode. Selected fields; full record and sources in the guide." style="max-height:350px;height:auto"><figcaption>L10B recorded cyber episode. Selected fields; full record and sources in the guide.</figcaption></figure></div><ul><li>Keep REVIEW visible. The operator must resolve the trust assumption and missing checks.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: cyber replay, recorded call 8; full record in source guide.</a></div>
<span class="pageno">73 / 80</span></div>

<!--
Read the actual reply, including the REVIEW choice. Numerical verification is PASS, but the overall result remains REVIEW and human acknowledgment is PENDING. The fixed comparator obtains the same numerical state estimate and correction without Llama. This replay demonstrates permitted tool routing and a report decision. It does not demonstrate better estimation, authenticated measurements, AC network security or operating authority. Run L11 with the default False setting, then proceed to L12.
Takeaway: 
Nominal duration: 2.5 minutes.

Full sources:
Workshop recorded model replies and numerical study records. Standard four-bus cyber study: Llama 3.1:8b tool selection and REVIEW calls 7–8. Public teaching archive. 21 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L12 · classroom-033</div>
<h1>Finish L12: practice the readback</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L12 (classroom-033), source lines 9–10.</p><pre class="teaching-code">wrong_id = lab.acknowledge(mv_scope, &#x27;wrong-id&#x27;, &#x27;Student operator&#x27;)
readback = lab.acknowledge(mv_scope, mv_scope[&#x27;recommendation_id&#x27;], &#x27;Student operator&#x27;)</pre><ul><li>Run all of L12 after completing L0–L11 in notebook order.</li><li>Check wrong-ID rejection, simulated acknowledgment and equipment_dispatch=False.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only.</a></div>
<span class="pageno">74 / 80</span></div>

<!--
This cell returns to the original test_01 voltage result through selected_trials. It does not use the restoration or cyber sweeps. Read both scope outcomes and explain why the full MV/LV request remains HOLD. The new simulated acknowledgment grants no physical operating authority and does not complete the review of an old record. Readback means repeating the recommendation ID and conditions so the acknowledgment can be matched to the same proposal. In this exercise it is simulated. Check the wrong-ID rejection, the correct simulated acknowledgment and equipment_dispatch=False.
Takeaway: 
Nominal duration: 4 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Proposed advisory pilot · teaching design</div>
<h1>Start a control-room pilot with a clear study request</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/ops_request_snapshot.svg" alt="Proposed advisory pilot — teaching design. F12 is an illustrative identifier." style="height:330px;max-height:330px"><figcaption>Proposed advisory pilot — teaching design. F12 is an illustrative identifier.</figcaption></figure><ul><li>Use an approved copy of the network data with a time stamp, topology version and limits.</li><li>If required data are missing or too old, return HOLD and name the missing information.</li></ul></div>
<div class="sources">Source: <a href="https://doi.org/10.6028/NIST.SP.800-82r3">Teaching proposal informed by NIST OT guidance and the cited notebook checks.</a></div>
<span class="pageno">75 / 80</span></div>

<!--
Proposed advisory pilot, not a deployment claim. F12 is an illustrative teaching feeder name. Read the study request aloud: compare the allowed voltage-support options, keep the stated current and voltage limits, show the worst margins and missing checks, and return a recommendation for review. The data owner defines acceptable age, source and quality rules. L1 and L7 illustrate matching inputs to results, but hashes alone do not authenticate those sources.
Takeaway: 
Nominal duration: 4 minutes.

Full sources:
Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).
Full source: https://doi.org/10.6028/NIST.SP.800-82r3
Full paper: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf
Publication: https://csrc.nist.gov/pubs/sp/800/82/r3/final

Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Proposed advisory pilot · teaching design</div>
<h1>Give the assistant a small, controlled tool list</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/ops_tool_boundary.svg" alt="Proposed advisory pilot — teaching design. Classroom functions are not live control-room interfaces." style="height:330px;max-height:330px"><figcaption>Proposed advisory pilot — teaching design. Classroom functions are not live control-room interfaces.</figcaption></figure><ul><li>An approved interface supplies read-only data and study tools. Log every request and result.</li><li>Keep equipment commands in the utility’s separate authorized operating process.</li></ul></div>
<div class="sources">Source: <a href="https://doi.org/10.6028/NIST.SP.800-82r3">Teaching proposal informed by NIST OT guidance and the cited notebook checks.</a></div>
<span class="pageno">76 / 80</span></div>

<!--
Proposed advisory pilot. Walk through the lanes: operator, assistant, application-controlled tool gateway and engineering tools. Llama requests one permitted function; the application checks the request and executes the tool. A snapshot identifier binds the result to the input. The workshop Python functions are teaching counterparts, not SCADA adapters. NIST OT guidance supports controlled information flows, least privilege and logging. The exact pilot architecture is our teaching recommendation, not a NIST-certified design.
Takeaway: 
Nominal duration: 4 minutes.

Full sources:
Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).
Full source: https://doi.org/10.6028/NIST.SP.800-82r3
Full paper: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf
Publication: https://csrc.nist.gov/pubs/sp/800/82/r3/final

Ollama documentation maintainers. Structured Outputs: generating structured JSON with a schema. Official Ollama documentation. Reviewed 24 October 2026.
Full source: https://docs.ollama.com/capabilities/structured-outputs

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Proposed advisory pilot · teaching design</div>
<h1>Check three things before returning a proposal</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/ops_three_gates.svg" alt="Proposed advisory pilot — teaching design. A PASS is limited to its tested model and inputs." style="height:330px;max-height:330px"><figcaption>Proposed advisory pilot — teaching design. A PASS is limited to its tested model and inputs.</figcaption></figure><ul><li>Check that the inputs match, the required limits pass and the required network parts were modeled.</li><li>Example: an MV-only PASS stays on HOLD when the request requires the full MV/LV network.</li></ul></div>
<div class="sources">Source: <a href="https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Teaching proposal informed by NIST OT guidance and the cited notebook checks.</a></div>
<span class="pageno">77 / 80</span></div>

<!--
Proposed advisory pilot. Current data and a matching evidence packet are the first gate. The second gate checks stated engineering limits with approved tools. The third asks whether the calculations cover the request, including excluded low-voltage parts or required protection and dynamic studies. This is not a universal complete security checklist. It illustrates why L12 can produce a passing local calculation and still HOLD a broader request. Make missing evidence visible instead of allowing fluent text to fill the gap.
Takeaway: 
Nominal duration: 4 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).
Full source: https://doi.org/10.6028/NIST.SP.800-82r3
Full paper: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf
Publication: https://csrc.nist.gov/pubs/sp/800/82/r3/final
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Proposed advisory pilot · teaching design</div>
<h1>Give the operator a short evidence packet</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/ops_review.svg" alt="Proposed advisory pilot — teaching design. Review of a study is distinct from operating equipment." style="height:330px;max-height:330px"><figcaption>Proposed advisory pilot — teaching design. Review of a study is distinct from operating equipment.</figcaption></figure><ul><li>Show the input snapshot, selected option, worst margins, rejected trials and missing checks.</li><li>The reviewer can ask for another study, reject the proposal or accept it for the next review step.</li></ul></div>
<div class="sources">Source: <a href="https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Teaching proposal informed by NIST OT guidance and the cited notebook checks.</a></div>
<span class="pageno">78 / 80</span></div>

<!--
Proposed advisory pilot. Use three review questions: Does this match the current equipment, inputs and model? Did the required checks pass, with missing checks clear? What exactly am I approving, who owns the next step, and where is the record? Record the reviewer, reason, case snapshot and tool versions. Accepting a study result does not itself issue an equipment command. Authorized operating procedures and roles determine any later physical action. L12 practices only a simulated ID-bound readback.
Takeaway: 
Nominal duration: 4 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).
Full source: https://doi.org/10.6028/NIST.SP.800-82r3
Full paper: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf
Publication: https://csrc.nist.gov/pubs/sp/800/82/r3/final

National Institute of Standards and Technology. Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. 26 January 2023.
Full source: https://doi.org/10.6028/NIST.AI.100-1
Full paper: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Proposed advisory pilot · teaching design</div>
<h1>Adopt it in stages and measure the benefit</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/ops_pilot.svg" alt="Proposed advisory pilot — teaching design. Benefits must be measured against an appropriate baseline." style="height:330px;max-height:330px"><figcaption>Proposed advisory pilot — teaching design. Benefits must be measured against an appropriate baseline.</figcaption></figure><ul><li>Begin with past cases, then read-only shadow work, then a limited pilot with named reviewers.</li><li>Compare against the same tools in a fixed script: correct studies, missed checks, time and rework.</li></ul></div>
<div class="sources">Source: <a href="https://doi.org/10.6028/NIST.AI.100-1">Teaching proposal informed by NIST OT guidance and the cited notebook checks.</a></div>
<span class="pageno">79 / 80</span></div>

<!--
Proposed advisory pilot. Historical replay lets engineers define expected outcomes and failure cases. Shadow use compares recommendations alongside the existing process without relying on them for equipment control. A limited pilot needs a named owner, training, an agreed scope and a way to stop use. Measure end-to-end elapsed time including review, correct completed studies, missed or stale inputs, overlooked limits and reviewer changes. Compare the same engineering tools with and without Llama. Our paired records show identical final numerical results, so there is no basis yet to promise higher accuracy, less operator workload or faster decisions. NIST AI RMF supports human roles, evaluation under realistic conditions and deactivation; these particular pilot metrics are our recommendation.
Takeaway: 
Nominal duration: 4 minutes.

Full sources:
National Institute of Standards and Technology. Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. 26 January 2023.
Full source: https://doi.org/10.6028/NIST.AI.100-1
Full paper: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf

Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json

Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json

Workshop recorded model replies and numerical study records. Standard four-bus cyber study: Llama 3.1:8b tool selection and REVIEW calls 7–8. Public teaching archive. 21 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json
-->

---
transition: none
---

<div class="lesson teaching rigorous closing-slide closing">

<h1>Save a workshop record others can repeat</h1>
<div class="content"><ul><li>Save your changed inputs and results, labeled new, archived or simulated.</li><li>Explain the request, tool call, result, checks and next decision.</li></ul></div>
<p class="reading-link"><a href="/Full_Reading_Guide.html">Open the Full Reading Guide</a></p>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.</a></div>
<span class="pageno">80 / 80</span></div>

<!--
Use the final five minutes for pair reports and saving. Each pair names one changed parameter, compares its predicted and observed result, and states one evidence limit. Another person should be able to repeat the experiment from the saved notebook. The reading guide supplies the full source links, stable cell map and debrief answers.
Takeaway: 
Nominal duration: 5 minutes.

Full sources:
Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md
-->
