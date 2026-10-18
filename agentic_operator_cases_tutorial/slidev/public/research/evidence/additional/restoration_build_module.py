"""Author only the restoration module and its native teaching figures."""
import ast
import hashlib
import json
import math
from copy import deepcopy
from itertools import product
from pathlib import Path
import numpy as np

OLD = Path('C:/Users/f00863x/OPRO/output/agentic_grid_workflow_tutorial')
NEW = Path('C:/Users/f00863x/OPRO/output/agentic_operator_cases_tutorial')
TMP = Path('C:/Users/f00863x/OPRO/tmp/operator_cases')
CONTENT = NEW / 'content'
DIAGRAMS = NEW / 'diagrams'
CONTENT.mkdir(parents=True, exist_ok=True)
DIAGRAMS.mkdir(parents=True, exist_ok=True)

# Run the actual small-case enumeration and binding functions without importing
# the unrelated SciPy solver module. Saved MILP outputs remain separately labeled.
def load_functions(path, names, namespace):
    tree = ast.parse(path.read_text(encoding='utf-8'))
    functions = [item for item in tree.body if isinstance(item, ast.FunctionDef) and item.name in names]
    exec(compile(ast.Module(body=functions, type_ignores=[]), str(path), 'exec'), namespace)
    return namespace

numeric = load_functions(OLD / 'src/standard_formulations.py',
    {'restoration_graph', '_enumerate_restoration'}, {'math': math, 'np': np, 'product': product})
fresh = []
for capacity in (40., 60., 80., 100., 120.):
    graph = numeric['restoration_graph'](capacity)
    for label in ('priority-weighted', 'unweighted'):
        trial = deepcopy(graph)
        if label == 'unweighted':
            trial['priority'] = [0., 1., 1., 1., 1., 1.]
        outcome = numeric['_enumerate_restoration'](trial)
        pickup = outcome['solution']['pickup']
        fresh.append({'tie_capacity_kw': capacity, 'policy': label,
            'total_kw': sum(d*x for d, x in zip(graph['demand_kw'], pickup)),
            'critical_kw': sum(graph['demand_kw'][i]*pickup[i] for i in (2, 5)),
            'objective': outcome['objective'], 'pickup': pickup,
            'closed_edges': outcome['solution']['closed_edges']})

binding = load_functions(OLD / 'src/classroom_labs.py',
    {'digest', 'bind_evidence', 'bound_to'}, {'hashlib': hashlib, 'json': json, 'deepcopy': deepcopy})
graph = numeric['restoration_graph'](40.)
request = {'task': 'restoration', 'model': 'six_node_active_transport',
    'graph_snapshot': graph, 'topology_revision': 'T1', 'revision': 1,
    'critical_nodes': [2, 5]}
candidate = {'pickup': [0, 1, 1, 0, 0, 1],
    'closed_edges': ['source_healthy', 'section_25', 'tie_15']}
evidence = binding['bind_evidence'](request, candidate,
    {'weighted_objective': 940., 'total_kw': 130., 'critical_kw': 90.})
changed_topology = deepcopy(request)
changed_topology['topology_revision'] = 'T2'
changed_topology['revision'] = 2
# An unused available branch is removed, so failure of the binding does NOT
# establish infeasibility of the former candidate. It establishes a new contract.
changed_topology['graph_snapshot']['edges'][2]['available'] = False
binding_check = {'label': 'Fresh teaching extension of L7, executed 2026-10-18',
    'actual_functions': str(OLD / 'src/classroom_labs.py'),
    'original_binding': binding['bound_to'](request, candidate, evidence),
    'changed_topology_with_old_evidence': binding['bound_to'](changed_topology, candidate, evidence),
    'change': 'section_23 becomes unavailable and topology/revision changes; candidate does not use section_23',
    'limitation': 'Identity/integrity binding, not authentication, physical feasibility, freshness attestation or switching permission.'}
assert binding_check['original_binding'] is True
assert binding_check['changed_topology_with_old_evidence'] is False
verification = {'label': 'Fresh exhaustive enumeration of the existing six-node fixture',
    'date': '2026-10-18', 'records': fresh, 'topology_binding_extension': binding_check,
    'milp_evidence': 'Existing executed Classroom_Labs.ipynb L6, not a fresh MILP run in this helper.'}
(TMP / 'restoration_verified_evidence.json').write_text(json.dumps(verification, indent=2) + '\n', encoding='utf-8')

PRE = r'''\begingroup
\hyphenpenalty=10000\exhyphenpenalty=10000
\definecolor{IEEEBlue}{HTML}{00629B}
\definecolor{Cyan}{HTML}{00A6B2}
\definecolor{Navy}{HTML}{003B5C}
\definecolor{Slate}{HTML}{526470}
\definecolor{RestRed}{HTML}{B83136}
\definecolor{RestAmber}{HTML}{A66610}
\begin{tikzpicture}[x=.90cm,y=.82cm,font=\fontsize{11}{12}\selectfont,
  every node/.style={text=Navy},
  flow/.style={-{Stealth[length=2mm]},line width=1pt,draw=IEEEBlue},
  bus/.style={circle,draw=IEEEBlue,line width=1pt,minimum size=5.5mm,inner sep=1pt,fill=white},
  textblock/.style={align=center,inner sep=1pt},
  pass/.style={draw=Cyan,line width=2pt},
  available/.style={draw=Slate,line width=.8pt},
  optional/.style={draw=RestAmber,dashed,line width=1pt}]
'''
POST = '\\end{tikzpicture}\n\\endgroup\n'

def diagram(name, body):
    (DIAGRAMS / (name + '.tex')).write_text(PRE + body + '\n' + POST, encoding='utf-8')

def network(mode='fault'):
    # All maps use the same six-node geometry and the declared fixture edges.
    # Geometry is an explanatory schematic, never a switching sequence.
    lines = [r'''\node[bus] (r0) at (0.8,1.55) {0};
\node[bus] (r1) at (2.8,2.3) {1};
\node[bus,draw=RestAmber] (r2) at (5.5,2.3) {2};
\node[bus] (r3) at (8.1,1.55) {3};
\node[bus] (r4) at (5.5,.55) {4};
\node[bus,draw=RestAmber] (r5) at (2.8,.55) {5};
\draw[available] (r0)--(r1);
\draw[RestRed,dashed,line width=1.4pt] (r1)--(r2);
\node[text=RestRed,fill=white] at (3.45,1.86) {fault open};
\draw[available] (r2)--(r3)--(r4);
\draw[available] (r2)--(r5);
\draw[optional] (r1)--node[left=1mm,fill=white,text=RestAmber] {100 kW}(r5);
\draw[optional] (r0) to[out=-60,in=200] (r4);
\node[anchor=west,text=RestAmber] at (.2,-.5) {tie 0--4: 40 kW};
\node[above=1mm of r1] {40 kW};
\node[above=1mm of r2,text=RestAmber] {60 kW critical};
\node[above=1mm of r3] {70 kW};
\node[right=1mm of r4] {50 kW};
\node[anchor=west,text=RestAmber] at (3.3,-.15) {30 kW critical};
\node[left=1mm of r0] {source};''']
    if mode == 'routes':
        lines.append(r'''\draw[pass,-{Stealth[length=2mm]}] (r0)--(r1);
\draw[pass,-{Stealth[length=2mm]}] (r1)--(r5);
\draw[pass,-{Stealth[length=2mm]}] (r5)--(r2);
\node[textblock,text width=2.8cm,text=RestRed] at (10.9,2.05) {50 kW block\\does not fit\\a 40 kW tie};
\node[textblock,text width=3.2cm] at (10.9,.45) {Whole load blocks\\no partial pickup};''')
    elif mode == 'plan':
        lines.append(r'''\draw[pass] (r0)--(r1)--(r5)--(r2);
\node[bus,fill=Cyan!20] at (0.8,1.55) {0};
\node[bus,fill=Cyan!20] at (2.8,2.3) {1};
\node[bus,draw=RestAmber,fill=RestAmber!15] at (5.5,2.3) {2};
\node[bus,draw=RestAmber,fill=RestAmber!15] at (2.8,.55) {5};
\node[textblock,text width=2.8cm] at (10.9,2.1) {Picked up: 1, 2, 5\\130 kW total};
\node[textblock,text width=3.2cm,text=RestAmber] at (10.9,.45) {Critical service\\90 kW};''')
    else:
        lines.append(r'''\node[textblock,text width=3.2cm] at (10.9,2.1) {Critical demand\\60 + 30 = 90 kW};
\node[textblock,text width=3.2cm,text=Slate] at (10.9,.45) {Dashed ties: options\\not commands};''')
    return '\\begin{scope}[x=.88cm]\n' + '\n'.join(lines) + '\n\\end{scope}'

diagram('restoration_contract', r'''
\node[textblock,anchor=west,text width=4.0cm] (q) at (0,1.9) {\textbf{Operator request}\\Restore eligible load;\\keep fault 1--2 isolated.};
\node[textblock,anchor=west,text width=3.4cm] (c) at (4.7,1.9) {\textbf{Study contract}\\T1 + ratings\\priorities + scope};
\node[textblock,anchor=west,text width=3.2cm] (p) at (9.0,1.9) {\textbf{Requested output}\\A checked proposal\\for operator review};
\draw[flow] (q.east)--(c.west);
\draw[flow] (c.east)--(p.west);
\draw[RestRed,line width=1pt] (0,.8)--(12.3,.8);
\node[textblock,anchor=west,text=RestRed] at (.1,.4) {Study authority only: no automatic physical switching};
''')
diagram('restoration_fault_map', network('fault'))
diagram('restoration_routes', network('routes'))
diagram('restoration_plan', network('plan'))
diagram('restoration_priority', r'''
\node[anchor=west] at (0,3.1) {\textbf{100 kW tie budget; node 1 adds 40 kW upstream}};
\fill[RestAmber!28] (0,1.95) rectangle (3.6,2.6);
\fill[Cyan!25] (3.6,1.95) rectangle (5.4,2.6);
\draw[Slate] (0,1.95) rectangle (6,2.6);
\node at (1.8,2.27) {2: 60 critical};
\node at (4.5,2.27) {5: 30};
\node[anchor=west] at (6.5,2.27) {\textbf{130 total / 90 critical kW}};
\fill[Slate!20] (0,.65) rectangle (4.2,1.3);
\fill[Cyan!25] (4.2,.65) rectangle (6,1.3);
\draw[Slate] (0,.65) rectangle (6,1.3);
\node at (2.1,.97) {3: 70 ordinary};
\node at (5.1,.97) {5: 30};
\node[anchor=west] at (6.5,.97) {\textbf{140 total / 30 critical kW}};
\node[anchor=west,text=Slate] at (0,.05) {Same graph and limits; different service objectives.};
''')
diagram('restoration_verify', r'''
\node[textblock,text width=3.2cm] (a) at (1.7,2.1) {\textbf{MILP candidate}\\Loads + edges\\priority score};
\node[textblock,text width=4.3cm] (b) at (6.3,2.1) {\textbf{Separate check}\\Fault open\\source paths + tree\\balance + capacities};
\node[textblock,text width=2.8cm] (c) at (10.9,2.1) {\textbf{Bind evidence}\\Request + candidate\\result + revision};
\draw[flow] (a.east)--(b.west);
\draw[flow] (b.east)--(c.west);
\draw[Slate,line width=.8pt] (.1,.6)--(12.4,.6);
\node[textblock,text width=11.4cm] at (6.2,.0) {Transport check only; AC operation and switching remain unverified.};
''')
diagram('restoration_stale', r'''
\node[textblock,text width=3.4cm] at (1.8,2.35) {\textbf{Verified case}\\40 kW + T1\\candidate + evidence};
\node[textblock,text width=3.5cm] at (6.0,2.35) {\textbf{Request changes}\\L7: 40 to 20 kW\\Extension: T2};
\node[textblock,text width=3.0cm,text=RestRed] at (10.5,2.35) {\textbf{HOLD}\\Old evidence fails\\request fresh solve};
\draw[flow] (3.6,2.35)--(4.15,2.35);
\draw[flow,draw=RestRed] (7.9,2.35)--(8.85,2.35);
\node[textblock,text width=11.4cm] at (6.1,.8) {Original: \textbf{True}\qquad Changed request: \textbf{False}};
\node[textblock,text width=11.4cm,text=Slate] at (6.1,.1) {Binding failure means stale evidence; it does not prove physical infeasibility.};
''')
diagram('restoration_packet', r'''
\node[textblock,text width=3.7cm] at (1.9,2.25) {\textbf{Proposed service}\\Loads 1, 2, 5; paths\\130 total kW\\90 critical kW};
\node[textblock,text width=3.5cm] at (6.4,2.25) {\textbf{Attached evidence}\\T1 + ratings + fault open\\solver + check};
\node[textblock,text width=3.1cm] at (10.9,2.25) {\textbf{Readback}\\Confirm conditions\\accept or revise\\or reject};
\draw[flow] (3.9,2.25)--(4.45,2.25);
\draw[flow] (8.3,2.25)--(9.0,2.25);
\node[textblock,text width=11.4cm,text=RestRed] at (6.1,.55) {A reviewed proposal still needs the separate authorized operating procedure.};
''')

slides = [
    {'title': 'Restoration starts with a specific operator request', 'kind': 'diagram', 'minutes': 2,
     'points': ['Restore eligible load after isolating fault 1–2.',
                'Use topology T1, the stated tie ratings and critical-load priorities.',
                'Return a checked proposal for operator review.'],
     'diagram': 'restoration_contract', 'refs': ['RST01', 'RST02', 'RST03'],
     'caption': 'Illustrative operator request for the existing six-node classroom fixture.',
     'note': 'Read the operator request before naming a solver: “Restore eligible load after fault 1–2. Keep the fault isolated. Use the declared ratings and priorities; return a proposal for review.” The explicit request is a teaching contract, not an actual dispatch instruction. T1 is a tutorial snapshot label added for this follow-on module. The tools may select a plan, calculate and report evidence; they have no physical switching authority. The six-node transport example is separate from the archived Greensboro feeder and its ampere-based bypass catalog. Spend two minutes identifying the goal, constraints and expected output.'},
    {'title': 'Lock the fault, topology and load priorities', 'kind': 'diagram', 'minutes': 2,
     'points': ['Fault 1–2 remains unavailable throughout this study.',
                'Node 0 supplies the network. Nodes 2 and 5 carry 90 kW of critical demand.',
                'Dashed ties are planning options, not issued switching commands.'],
     'diagram': 'restoration_fault_map', 'refs': ['RST01', 'RST02', 'RST03'],
     'caption': 'Original teaching schematic of the exact synthetic six-node graph; all demands are kW.',
     'note': 'Demand is [0,40,60,70,50,30] kW at nodes 0–5. Priority weights are [0,1,10,1,1,10]. Healthy source edge 0–1 has 300 kW capacity; faulted edge 1–2 is unavailable even though its nominal capacity is 250 kW. Sections 2–3, 3–4 and 2–5 each have 250 kW capacity. Tie 1–5 is 100 kW; tie 0–4 is the capacity varied in the experiment. This map fixes a transparent classroom topology; it is not an extracted Greensboro switching diagram. Ask learners to identify the isolated edge and the two critical loads. Fault isolation is an assumed input to this study, not a protection diagnosis performed by the agent.'},
    {'title': 'Trace the routes before choosing a pickup plan', 'kind': 'diagram', 'minutes': 2,
     'points': ['The route 0–1–5–2 avoids the fault and uses the 100 kW tie.',
                'The other tie is only 40 kW in the first case.',
                'A 50 kW load block cannot fit through a 40 kW path alone.'],
     'diagram': 'restoration_routes', 'refs': ['RST02', 'RST03'],
     'caption': 'Highlighted route is a feasible path explanation, not a time-ordered switching sequence.',
     'note': 'Trace the source-to-critical-node path. The 100 kW tie must carry downstream load assigned behind it; node 1’s 40 kW is upstream of that bottleneck. The 40 kW tie alone cannot serve the indivisible 50 kW load at node 4. Local load pickup is all-or-nothing. A bus can be energized for transit while its local load remains disconnected; energized and served are different decisions. The optional arrows illustrate static paths only. They neither tell a crew which device to operate first nor establish interlocks, dead-line checks, protection coordination or equipment status.'},
    {'title': 'More restored kW can mean less critical service', 'kind': 'diagram', 'minutes': 2,
     'points': ['At the 40 kW tie setting, priority weighting restores 130 kW total, including all 90 critical kW.',
                'Maximizing total kW restores 140 kW, but only 30 critical kW.',
                'The objective changes who receives service.'],
     'diagram': 'restoration_priority', 'refs': ['RST01', 'RST02', 'RST03'],
     'caption': 'Hand-checkable choices on the same graph and constraints; this is a policy comparison.',
     'note': 'Behind tie 1–5, critical loads 2 and 5 require 60+30=90 kW. Add 40 kW at node 1 upstream: 130 total and 90 critical. The unweighted choice serves loads 3 and 5 behind that tie: 70+30=100 kW, plus the same upstream 40, giving 140 total but 30 critical. Weights 10 for nodes 2 and 5 produce scores 940 versus 410 weighted kW; these are priority scores, not actual power. A finite weight of ten is not universal lexicographic critical-first service. The comparison changes the objective, so it does not measure an LLM benefit. Both methods are conventional exact optimizers on this fixture.'},
    {'title': 'Ask the solver for a plan tied to this case', 'kind': 'diagram', 'minutes': 2,
     'points': ['A mixed-integer linear program (MILP) chooses whole loads and connected branches.',
                'The 40 kW priority plan serves nodes 1, 2 and 5: 130 total, 90 critical kW.',
                'Record the chosen edges and per-branch flows.'],
     'diagram': 'restoration_plan', 'refs': ['RST02', 'RST03'],
     'caption': 'One declared feasible priority plan: edges 0–1, 1–5 and 5–2; fault 1–2 stays open.',
     'note': 'The highlighted plan uses source_healthy, tie_15 and section_25. Flow is 130 kW on 0–1, 90 on 1–5 and 60 from 5 to 2. The source-file orientation of section_25 is 2→5, so its signed flow is −60 kW. Negative flow is a direction convention, not a violation. Nodes 3 and 4 remain unenergized in this particular minimal-edge plan. The MILP first maximizes priority-weighted pickup, then preserves that optimum while minimizing energized branch count with a small index tie-breaker. This second solve is not a minimum switching-operation sequence. Different feasible or optimal edge sets can exist; the figure states an explicit checked plan rather than claiming uniqueness.'},
    {'title': 'Check capacity, source paths and the objective', 'kind': 'diagram', 'minutes': 2,
     'points': ['Every picked-up load needs a source-connected path; the energized network must be a tree.',
                'Check branch capacities, active-power balance and fault isolation.',
                'Independent enumeration must agree with the small-case MILP objective.'],
     'diagram': 'restoration_verify', 'refs': ['RST02', 'RST03', 'RSTL01'],
     'caption': 'Numerical verification and evidence binding perform different jobs.',
     'note': 'The model uses separate binary variables for energized nodes, picked-up loads and closed edges. Pickup requires an energized node; a selected edge requires energized endpoints. Fictitious commodity flow establishes source connectivity, and the edge count then enforces a tree. Counting edges alone is insufficient. The fictitious flow is not electrical kW. Electrical transport balance and signed capacity inequalities are checked separately. The actual independent routine enumerates pickup and edge choices, verifies source reachability/tree structure and branch demand, and compares the weighted optimum. This is tractable because the fixture is tiny. Agreement validates the finite transport calculation, not the coverage of AC voltage, reactive power, losses, protection or switching dynamics. Wang et al. sections III–IV explain why reachability and edge count are distinct requirements.'},
    {'title': 'A higher tie rating does not always restore another load', 'kind': 'figure', 'minutes': 2,
     'points': ['At both 80 and 100 kW, the weighted plan serves 200 kW total and all 90 critical kW.',
                'Whole load blocks and available routes create plateaus.',
                'These are sampled capacities, not a continuous response curve.'],
     'image_source_path': str(OLD / 'figures/classroom_restoration.png'),
     'refs': ['RST02', 'RST03', 'RST05'],
     'caption': 'Existing computed Classroom Labs L6 figure; both objectives use the same feasible network.',
     'note': 'Inspect both panels and the discrete markers. The saved executed L6 cell reports weighted total/critical service 130/90,180/90,200/90,200/90,250/90 at tie capacities 40,60,80,100,120 kW. The unweighted totals/critical values are 140/30,190/30,200/90,200/90,250/90. Fresh exhaustive enumeration of the same source functions reconfirmed those values for this module. The saved notebook’s MILP agrees with exhaustive checks; no fresh SciPy MILP is claimed here. At 80/100, one feasible plan supplies nodes 2 and 5 through the 100 kW tie (90 kW), node 3 through tie 0–4 and edge 4–3 (70 kW), and node 1 upstream (40 kW); node 4 is energized for transit but its own 50 kW load is shed. These static paths explain the plateau and are not a switching sequence.'},
    {'title': 'A changed topology or rating makes old evidence stale', 'kind': 'diagram', 'minutes': 2,
     'points': ['A changed rating or topology revision invalidates the old evidence binding.',
                'L7 returns True for the original 40 kW request and False after it changes to 20 kW.',
                'HOLD and recheck; binding failure alone does not prove infeasibility.'],
     'diagram': 'restoration_stale', 'refs': ['RST02', 'RST04', 'RST06'],
     'caption': 'L7 changes the rating/revision; the explicit topology-change test is a separately labeled teaching extension.',
     'note': 'Actual L7 binds request, candidate and result using SHA-256 digests, then changes capacity from 40 to 20 kW and revision from 1 to 2; bound_to returns True then False. This module additionally executes the same unmodified binding functions on a request containing the full graph snapshot and topology_revision. It removes unused section_23 and changes T1/revision1 to T2/revision2; old evidence returns False. The previous plan did not use that branch, illustrating why identity failure does not itself establish physical infeasibility. The explicit graph snapshot is essential: a hash can only bind fields that are included. Hashes do not authenticate the data source, prove measurement freshness or grant operational authority. HOLD the old recommendation and obtain fresh checks under the changed request.'},
    {'title': 'Give the operator a packet that can be checked and read back', 'kind': 'diagram', 'minutes': 2,
     'points': ['Show picked-up loads, selected paths and total/critical service.',
                'Attach topology and rating revisions, candidate identity, solver output and independent checks.',
                'Ask the operator to confirm conditions before accepting, revising or rejecting the proposal.'],
     'diagram': 'restoration_packet', 'refs': ['RST01', 'RST02', 'RST04'],
     'caption': 'Illustrative review packet, not a switching order or a deployed control-room interface.',
     'note': 'An example readback is: “For topology T1, fault 1–2 isolated, tie 1–5 at 100 kW and tie 0–4 at 40 kW, I understand this proposes serving nodes 1,2,5:130 kW total and 90 critical. Transport and enumeration checks match this candidate. AC/security and switching authorization are outside this packet.” The packet also records shed loads, limitations and any unsuccessful checks. A readback is a tutorial communication step, not proof that a field procedure has been completed. Acceptance of the calculation must remain separate from switching authorization. Missing status, failed binding, failed checks or conflicting instructions produce HOLD rather than an action request.'},
    {'title': 'Exercise: choose the service policy and handle a changed case', 'kind': 'exercise', 'minutes': 4,
     'points': ['With tie 0–4 at 40 kW, compare loads 2+5 with loads 3+5 behind the 100 kW tie.',
                'Add node 1’s 40 kW. Report total and critical service for each choice.',
                'The topology changes after verification. Should the old packet be accepted?'],
     'diagram': 'restoration_fault_map', 'refs': ['RST02', 'RST03', 'RST04'],
     'caption': 'Four-minute pair exercise. Work from the map; answers appear in the debrief.',
     'note': 'Allow the complete four minutes. First minute: identify demands and which loads are critical. Second minute: calculate both service outcomes and explain the preferred policy. Third minute: check a feasible source path and the 100 kW bottleneck. Fourth minute: decide what a topology change does to the evidence. Answers: 2+5 gives90 kW through the tie, plus upstream40 =130 total/90 critical. 3+5 gives100 through the tie, plus40 =140 total/30 critical. The declared priority-weighted policy chooses the first outcome. Fault1–2 cannot be reclosed. A topology change requires HOLD of the old bound packet and a new check; it does not by itself prove the old candidate infeasible. No participant should invent a field switching order from the static map. Keep answers off this exercise slide.'},
    {'title': 'Debrief: keep the priority and the evidence current', 'kind': 'diagram', 'minutes': 2,
     'points': ['The priority choice serves 130/90 kW total/critical; the maximum-total choice serves 140/30.',
                'Both can satisfy this transport model while serving different policies.',
                'After a topology change, HOLD the old packet and bind fresh evidence.'],
     'diagram': 'restoration_priority', 'refs': ['RST02', 'RST03', 'RST04', 'RST06'],
     'caption': 'Two-minute debrief: the objective and evidence validity are separate checks.',
     'note': 'Spend the first minute asking one pair to explain the arithmetic and the 100 kW tie budget. Use the second minute to explain the stale-evidence response. The difference between130 and140 kW is not a solver error: objectives differ. The original critical weighting yields940 versus410 weighted kW in these example plans. It is not a measured benefit of an LLM. A correct numerical answer from the old request is not current evidence after the request changes. If a learner says “the old plan is definitely infeasible,” correct that: changed identity requires rechecking; only fresh engineering evaluation answers feasibility. A finite priority weight does not guarantee universal strict priority.'},
    {'title': 'Stop at the boundary of the model and the operator’s authority', 'kind': 'normal', 'minutes': 2,
     'points': ['This fixture checks lossless active-power transport, source connectivity and stated branch capacities.',
                'It does not certify AC voltage, reactive power, losses, protection or a switching sequence.',
                'A reviewed proposal still needs the utility’s separate authorization and operating procedure.'],
     'refs': ['RST01', 'RST03', 'RST04', 'RSTL02'],
     'caption': '',
     'note': 'Conclude with a scope readback. The agent can preserve the requested priorities, select allowed tools, assemble evidence, detect a stale binding and ask for review. The conventional optimizer chooses a transport plan; no field improvement is established by this case. A larger real restoration model may need three-phase AC checks, cold-load pickup, DER availability, dynamic limits, protection coordination and a time-ordered procedure. Chen et al. is a background reference on sequential restoration, not the source of these six-node numbers. Do not import the separate archived feeder’s ampere ratings, served-kW figures or Llama latencies into this module. The next case can ask what happens when the measurements feeding a correct optimizer are wrong.'},
]

diagram_specs = {
    'restoration_contract': 'Three plain stages: operator request → locked study contract → reviewable proposal. A separate authority line states study-only authority.',
    'restoration_fault_map': 'Consistent exact six-node synthetic graph, demands and critical labels. Failed1–2red/open; tie1–5 100kW and tie0–4 40kW dashed as options.',
    'restoration_routes': 'Same graph with the source→1→5→2 route highlighted. State why the indivisible50kW block cannot fit a40kW path alone.',
    'restoration_priority': 'Two100kW budget bars: critical60+30 versus ordinary70+critical30. Add upstream40 to show130/90 and140/30 total/critical.',
    'restoration_plan': 'Same graph; only0–1,1–5,5–2highlighted as the explicit feasible130/90kW priority plan. All other edges are context.',
    'restoration_verify': 'Candidate→separate exhaustive verification→identity-bound evidence. Explicit fault/path/tree/balance/capacity checks; no safety-certification claim.',
    'restoration_stale': 'Verified40kW/T1contract→rating/revision change or explicitT2extension→HOLD. True/Falseidentity checks clearly separated from feasibility.',
    'restoration_packet': 'Proposed load/path/service→attached current evidence→operator readback. This is a review packet, not an issued switching sequence.',
}
for index, slide in enumerate(slides, 1):
    slide['module'] = 'restoration'
    slide['module_slide'] = index
    slide['main_ref'] = slide['refs'][0]
    if slide.get('diagram'):
        slide['diagram_source_path'] = str(DIAGRAMS / (slide['diagram'] + '.tex'))
        slide['diagram_spec'] = diagram_specs[slide['diagram']]
    words = sum(len(point.split()) for point in slide['points'])
    assert 1 <= len(slide['points']) <= 3
    assert words <= 50, (index, words)
assert len(slides) == 12
assert sum(slide['minutes'] for slide in slides) == 26
assert sum(bool(slide.get('diagram') or slide.get('image_source_path')) for slide in slides) >= 9
assert len(diagram_specs) == 8
(CONTENT / 'restoration.json').write_text(json.dumps(slides, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

sources = {
 'RST01': {'id': 'RST01', 'authors': ['Existing user-workspace GridGuard workshop; individual author not specified'],
    'title': 'Agentic AI for Grid Operators: restoration teaching chapter, frames R01–R18',
    'publisher': 'Local existing workshop teaching edition', 'date': '17 October 2026 edition', 'url': None,
    'local_evidence_paths': [str(OLD / 'latex_teaching/chapters/restoration.tex'), str(OLD / 'README.md')],
    'locator': 'Frames R01–R14 and R18; archived feeder frames R15–R17 are deliberately not merged into this six-node module.',
    'scope': 'Teaching explanations and illustrative operator handoff. This source does not document deployment.'},
 'RST02': {'id': 'RST02', 'authors': ['Existing user-workspace GridGuard workshop; individual author not specified'],
    'title': 'Classroom Labs: L6 restoration sweep and L7 changed-contract binding',
    'publisher': 'Local executed Jupyter notebook', 'date': '17 October 2026 teaching edition; inspected18 October2026', 'url': None,
    'local_evidence_paths': [str(OLD / 'Classroom_Labs.ipynb'), str(OLD / 'latex_teaching/snippets/L6.py'), str(OLD / 'latex_teaching/snippets/L7.py')],
    'locator': 'Markdown headings L6/L7; code cells CAPACITIES_KW and rest_record; saved text/plain outputs.',
    'scope': 'Saved executed numerical results and binding booleans; L6 makes no live language-model calls.'},
 'RST03': {'id': 'RST03', 'authors': ['Existing user-workspace GridGuard workshop; individual author not specified'],
    'title': 'Six-node restoration graph, MILP and exhaustive enumeration implementation',
    'publisher': 'Local Python source and saved numerical evidence', 'date': 'Existing17 October2026 teaching edition; inspected18 October2026', 'url': None,
    'local_evidence_paths': [str(OLD / 'src/standard_formulations.py'), str(OLD / 'src/classroom_labs.py'), str(OLD / 'results/standard_formulations.json')],
    'locator': 'restoration_graph lines251–262; _enumerate_restoration lines265–298; solve_restoration_milp lines301–363; classroom_labs.restoration_sweep lines149–175.',
    'scope': 'Synthetic lossless active-power transport with binary pickup, selected radial topology and explicit capacities; noAC/protection/switching sequence.'},
 'RST04': {'id': 'RST04', 'authors': ['Existing user-workspace GridGuard workshop; individual author not specified'],
    'title': 'Evidence digest, binding and contract matching functions',
    'publisher': 'Local classroom implementation', 'date': 'Existing17 October2026 teaching edition; inspected18 October2026', 'url': None,
    'local_evidence_paths': [str(OLD / 'src/classroom_labs.py'), str(OLD / 'Classroom_Labs.ipynb')],
    'locator': 'digest, bind_evidence, bound_to lines22–36; notebook L7.',
    'scope': 'Binds included request/candidate/result fields only. Hashes are not authentication, external freshness proof or authority.'},
 'RST05': {'id': 'RST05', 'authors': ['Existing user-workspace GridGuard workshop; individual author not specified'],
    'title': 'Classroom restoration capacity sweep: total and critical service',
    'publisher': 'Original computed local scientific figure', 'date': '17 October2026 teaching edition; inspected18 October2026', 'url': None,
    'local_evidence_paths': [str(OLD / 'figures/classroom_restoration.png'), str(OLD / 'latex_teaching/figures/classroom_restoration.png'), str(OLD / 'Classroom_Labs.ipynb')],
    'locator': 'L6 sampled capacities40,60,80,100,120kW; both weighted and unweighted policies.',
    'scope': 'Existing figure copied unchanged. Coincident markers indicate equal outcomes; noindependent field experiment or continuous capacity curve.'},
 'RST06': {'id': 'RST06', 'authors': ['This follow-on tutorial, using unchanged existing source functions'],
    'title': 'Fresh restoration enumeration and explicit topology-binding teaching check',
    'publisher': 'Local reproducible teaching evidence', 'date': '18 October2026', 'url': None,
    'local_evidence_paths': [str(TMP / 'restoration_verified_evidence.json'), str(TMP / 'restoration_build_module.py'), str(OLD / 'src/classroom_labs.py'), str(OLD / 'src/standard_formulations.py')],
    'locator': 'Actual source function ASTs executed: restoration_graph, _enumerate_restoration, digest, bind_evidence, bound_to.',
    'scope': 'Fresh exhaustive check reconfirms saved service values; explicit topologyT1→T2binding is a new teaching extension, distinct fromL7rating40→20. No freshMILPorLLMrun claimed.'},
 'RSTL01': {'id': 'RSTL01', 'authors': ['Ying Wang','Yin Xu','Jiaxu Li','Jinghan He','Xiaojun Wang'],
    'title': 'On the Radiality Constraints for Distribution System Restoration and Reconfiguration Problems',
    'publisher': 'Author preprint, arXiv:1912.05185v3', 'date': '15 March2020(v3); first submitted11 December2019',
    'url': 'https://arxiv.org/abs/1912.05185v3', 'full_text_url': 'https://arxiv.org/html/1912.05185v3',
    'pdf_url': 'https://arxiv.org/pdf/1912.05185v3', 'local_evidence_paths': [],
    'locator': 'SectionsIII–IV; Conditions1–2 and equations4–6.',
    'scope': 'Primary full text verified18 October2026. Supports separate reachability and edge-count conditions; not the source of six-node numeric results.'},
 'RSTL02': {'id': 'RSTL02', 'authors': ['Bo Chen','Chen Chen','Jianhui Wang','Karen L. Butler-Purry'],
    'title': 'Sequential Service Restoration for Unbalanced Distribution Systems and Microgrids',
    'publisher': 'IEEE Transactions on Power Systems33(2),1507–1520', 'date': 'March2018',
    'url': 'https://doi.org/10.1109/TPWRS.2017.2720122',
    'publisher_url': 'https://ieeexplore.ieee.org/document/7971935/',
    'author_manuscript_url': 'https://www.osti.gov/servlets/purl/1402471', 'local_evidence_paths': [],
    'locator': 'Background reading on sequential restoration; linked in the existing workshop.',
    'scope': 'Primary publisher search metadata verified; publisher page challenged access and OSTIfulltext timed out in this review. Nofigure or uninspected quantitative result is used. Six-node teaching implementation is a different model.'},
}
(CONTENT / 'restoration_sources.json').write_text(json.dumps(sources, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

summary = {'slides': len(slides), 'minutes': sum(s['minutes'] for s in slides),
    'visual_slides': sum(bool(s.get('diagram') or s.get('image_source_path')) for s in slides),
    'native_diagrams': list(diagram_specs), 'point_words': [sum(len(p.split()) for p in s['points']) for s in slides],
    'exercise_minutes': [s['minutes'] for s in slides if s['kind'] == 'exercise'],
    'fresh_enumeration_records': fresh, 'binding': binding_check}
(TMP / 'restoration_validation.json').write_text(json.dumps(summary, indent=2) + '\n', encoding='utf-8')
print(json.dumps({key: summary[key] for key in ('slides','minutes','visual_slides','native_diagrams','point_words','exercise_minutes')}, indent=2))
