"""Original, editable tutorial diagrams; no product UI or deployment claim."""
from pathlib import Path
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from pypdf import PdfReader
from PIL import Image

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = ROOT / 'diagrams'
BUILD = HERE / 'build'
BUILD.mkdir(parents=True, exist_ok=True)
spec = importlib.util.spec_from_file_location('existing_diagram_builder', ROOT / 'build_diagrams.py')
compiler = importlib.util.module_from_spec(spec)
sys.dont_write_bytecode = True
spec.loader.exec_module(compiler)

COLORS = r'''\begingroup
\hyphenpenalty=10000\exhyphenpenalty=10000
\definecolor{IEEEBlue}{HTML}{00629B}\definecolor{Cyan}{HTML}{00A6B2}
\definecolor{Navy}{HTML}{003B5C}\definecolor{Slate}{HTML}{526470}
\definecolor{BridgeRed}{HTML}{B83136}\definecolor{BridgeAmber}{HTML}{A66610}
\definecolor{BridgeGreen}{HTML}{287449}
'''
START = r'''\begin{tikzpicture}[x=1cm,y=1cm,font=\sffamily\fontsize{9}{11}\selectfont,
every node/.style={text=Navy},
flow/.style={-{Stealth[length=2mm]},draw=IEEEBlue,line width=1.1pt},
muted/.style={draw=Slate!55,line width=.6pt},
bridgebox/.style={draw=IEEEBlue,line width=.85pt,fill=white,align=center,minimum height=.9cm,inner sep=5pt},
plain/.style={align=center,inner sep=2pt},
small/.style={font=\sffamily\fontsize{8.5}{10.5}\selectfont},
stop/.style={draw=BridgeRed,fill=BridgeRed!4,text=BridgeRed,line width=1pt,align=center,minimum height=.9cm,inner sep=5pt}]
'''
END = '\\end{tikzpicture}\n\\endgroup\n'
PILOT = r'\node[small,text=Slate] at (7.1,-.24) {Proposed advisory pilot --- teaching design};'

items = []
def add(id, title, caption, body, refs, pilot=False, caveat=''):
    items.append(dict(id=id,title=title,caption=caption,body=body + ('\n'+PILOT if pilot else ''),source_refs=refs,
                      kind='Original native TikZ teaching illustration',
                      credit='Original tutorial design. Illustration, not product UI or a reported deployment.',
                      evidence_limit=caveat or 'Conceptual teaching design; not a measurement of an operational AI system.'))

add('bridge_request','From an operator question to a reviewed study',
    'A plain-language question becomes a bounded study request and a reviewable result; it does not confer operating authority.',r'''
\node[step,text width=3.2cm] (r) at (1.95,1.9) {Operator question\\``Check this feeder\\after the alarm.''};
\node[step,text width=3.5cm] (s) at (7.1,1.9) {Study list\\Read approved case\\Run required checks};
\node[step,text width=3.1cm] (h) at (12.15,1.9) {Operator review\\What was checked?\\What is missing?};
\draw[flow] (r)--(s);\draw[flow] (s)--(h);
\node[plain,text=Slate] at (7.1,.35) {The requested output is a study proposal with evidence.};
\node[plain,text=IEEEBlue] at (7.1,3.15) {Question $\longrightarrow$ bounded work $\longrightarrow$ review};
''',['DEF03','OT01'])

add('bridge_script_agent','A script and an agent can use the same tools',
    'Under the attributed workflow/agent convention, code fixes a script’s next-step logic while an LLM can select an allowed next operation. Both can branch; branching alone does not establish agency.',r'''
\node[plain,anchor=east,text=IEEEBlue] at (1.5,2.65) {Script};
\node[step,text width=2.25cm] (sr) at (3.0,2.65) {Same study\\request};
\node[step,text width=3.5cm] (sc) at (7.25,2.65) {Code rules choose\\the next step\\Branches are allowed};
\node[step,text width=2.9cm] (st) at (12.0,2.65) {Read a case\\or run a study};
\draw[flow] (sr)--(sc);\draw[flow] (sc)--(st);
\node[plain,anchor=east,text=Cyan] at (1.5,1.05) {Agent\\design};
\node[step,text width=2.25cm] (ar) at (3.0,1.05) {Same study\\request};
\node[step,text width=3.5cm,draw=Cyan] (ac) at (7.25,1.05) {Model chooses the next\\permitted tool};
\node[step,text width=2.9cm] (at) at (12.0,1.05) {Read a case\\or run a study};
\draw[flow] (ar)--(ac);\draw[flow] (ac)--(at);
\node[plain,small,text=Slate] at (7.1,-.05) {Both can branch. Agent row is proposed; default notebook uses Python.};
''',['DEF03'],caveat='Proposed architectural comparison. Default notebook cells use ordinary Python and do not make a fresh LLM decision.')

add('bridge_llama_tools','Language, calculations and review have different jobs',
    'A proposed bounded design assigns language tasks to Llama, numerical work to Python tools and the review decision to an operator. The default notebook does not run a new Llama call.',r'''
\node[plain,text=IEEEBlue] at (2.05,3.05) {Llama};
\draw[IEEEBlue,line width=1.5pt] (.4,2.72)--(3.7,2.72);
\node[plain,text width=3.2cm] (l) at (2.05,1.75) {Read the request\\Choose an allowed tool\\Explain tool evidence};
\node[plain,text=Cyan] at (7.1,3.05) {Python tools};
\draw[Cyan,line width=1.5pt] (5.45,2.72)--(8.75,2.72);
\node[plain,text width=3.2cm] (p) at (7.1,1.75) {Calculate results\\Check stated limits\\Return values + scope};
\node[plain,text=IEEEBlue] at (12.15,3.05) {Operator};
\draw[IEEEBlue,line width=1.5pt] (10.5,2.72)--(13.8,2.72);
\node[plain,text width=3.1cm] (o) at (12.15,1.75) {Review the study\\Ask for more evidence\\Accept or reject study};
\draw[flow] (l.east)--(p.west);\draw[flow] (p.east)--(o.west);
\node[plain,small,text=Slate] at (7.1,.22) {Proposed agent concept; default notebook uses Python + archived model replies.};
''',['DEF03','H00'])

add('bridge_agent_parts','The parts of a bounded agent',
    'An original conceptual architecture joins a goal, approved context, a language model, allowed tools, saved case state and explicit check/stop rules. It is a proposed design, not the default notebook runtime.',r'''
\node[plain,text=Slate] at (7.1,3.45) {Proposed bounded-agent concept};
\node[step,text width=2.0cm] (goal) at (1.3,2.55) {Goal};
\node[step,text width=2.0cm] (ctx) at (1.3,1.0) {Approved\\context};
\node[circle,draw=IEEEBlue,line width=1.1pt,minimum size=1.6cm,align=center] (lm) at (4.7,1.95) {Llama};
\node[step,text width=2.5cm] (tools) at (8.4,1.95) {Allowed tools};
\node[step,text width=2.6cm] (gate) at (12.15,1.95) {Check / stop\\rules};
\node[plain,text width=3.2cm,text=Cyan] (state) at (6.5,.38) {Saved case state};
\draw[flow] (goal.east)--(lm.north west);\draw[flow] (ctx.east)--(lm.south west);
\draw[flow] (lm)--(tools);\draw[flow] (tools)--(gate);
\draw[flow,draw=Cyan] (tools.south)|-(state.east);\draw[flow,draw=Cyan] (state.west)-|(lm.south);
\node[small,plain,text=Slate] at (11.95,.45) {Review, retry or HOLD};
''',['DEF03','OT01','EVAL01'])

add('bridge_reason_check','Explain a decision with facts and tests',
    'A public explanation connects a claim to returned evidence and an explicit test, then reports the decision and remaining limits. This requests an evidence summary, not private chain-of-thought.',r'''
\node[step,text width=2.65cm] (c) at (1.65,1.9) {Claim\\``Voltage passes.''};
\node[step,text width=2.65cm] (f) at (5.25,1.9) {Supporting fact\\Solver returns\\voltage extrema};
\node[step,text width=2.65cm] (t) at (8.85,1.9) {Tool test\\Compare extrema\\with stated limits};
\node[step,text width=2.65cm] (e) at (12.45,1.9) {Public explanation\\Pass or reject;\\name tested limit};
\draw[flow] (c)--(f);\draw[flow] (f)--(t);\draw[flow] (t)--(e);
\node[plain,text=Slate] at (7.1,.35) {Explain the evidence and decision; private reasoning is not requested.};
\node[plain,text=IEEEBlue] at (7.1,3.1) {One passed test does not replace the other required checks.};
''',['DEF03','EVAL01','H02'])

add('bridge_words','Six technical words connected to familiar pictures',
    'Six original mini-illustrations pair workshop terms with their plain meanings. SAC is a saved controller, binding is content consistency, and scope specifies represented network parts.',r'''
% Six independent mini-illustrations, not a table.
\foreach \x/\a/\b in {1.15/Forecast plan/MPC,3.5/Saved controller/SAC,5.85/Whole-load choices/MILP,8.2/Fit readings/WLS,10.55/Result belongs\\to inputs/Binding,12.9/Which network\\parts/Model scope} {
  \node[plain,text width=2.15cm] at (\x,3.15) {\a};
  \node[plain,text=IEEEBlue,text width=2.1cm] at (\x,.28) {\b};
}
% Forecast horizon.
\draw[muted] (.25,1.15)--(2.05,1.15);\draw[muted] (.25,1.15)--(.25,2.35);
\draw[flow] (.4,1.4)--(.95,2.05)--(1.45,1.8)--(1.95,2.2);
\draw[Cyan,dashed] (.93,1.13)--(.93,2.5);
% Saved policy weights produce a proposal.
\draw[IEEEBlue] (2.76,1.35) rectangle (3.58,2.25);
\draw[IEEEBlue] (2.93,2.06)--(3.4,2.06);\draw[IEEEBlue] (2.93,1.84)--(3.4,1.84);
\draw[IEEEBlue] (2.93,1.62)--(3.4,1.62);\draw[flow] (3.62,1.8)--(4.18,1.8);
\fill[Cyan] (4.23,1.8) circle (.09);
% Whole on/off blocks.
\foreach \x in {5.05,5.63} {\draw[IEEEBlue,fill=Cyan!18] (\x,1.3) rectangle +(0.42,1.0);}
\draw[Slate,dashed] (6.21,1.3) rectangle +(0.42,1.0);
% Noisy observations and a fitted line.
\draw[IEEEBlue] (7.36,1.25)--(9.02,2.25);
\foreach \x/\y in {7.55/1.55,7.84/1.44,8.14/1.88,8.48/1.83,8.78/2.3} {\fill[Cyan] (\x,\y) circle (.065);}
% Request and result linked by a content binding.
\draw[IEEEBlue] (9.67,1.25) rectangle +(0.6,1.05);\draw[IEEEBlue] (10.84,1.25) rectangle +(0.6,1.05);
\draw[Cyan,line width=1.3pt] (10.13,1.78)--(10.98,1.78);
\draw[Cyan,line width=1.3pt] (10.13,1.6)--(10.98,1.6);
% Network with an explicitly bounded covered portion.
\draw[IEEEBlue] (12.15,1.3)--(12.7,1.8)--(13.3,2.3);\draw[Slate] (12.7,1.8)--(13.65,1.4);
\foreach \x/\y in {12.15/1.3,12.7/1.8,13.3/2.3,13.65/1.4} {\fill[IEEEBlue] (\x,\y) circle (.065);}
\draw[Cyan,dashed,line width=1pt] (11.93,1.06) rectangle (13.45,2.52);
''',['H01','H02','H06','H08'],caveat='Original terminology aids, not mathematical formulations or product icons. A saved SAC policy is not an LLM; matching evidence hashes do not authenticate measurements.')

add('bridge_modes','Three modes that must remain visibly separate',
    'Green means newly computed numerical work; amber means an actual archived Llama reply tied to its old input; blue means a proposed future advisory-pilot design. Replaying a reply makes no fresh model call.',r'''
\node[circle,draw=BridgeGreen,line width=1.4pt,text=BridgeGreen,minimum size=1.05cm] at (2.2,2.2) {RUN};
\node[plain,text=BridgeGreen] at (2.2,3.18) {Fresh calculation};
\node[plain,text width=3.8cm] at (2.2,.9) {Fresh numerical checks\\Saved weights: inference};
\node[circle,draw=BridgeAmber,line width=1.4pt,text=BridgeAmber,minimum size=1.05cm] at (7.1,2.2) {REPLAY};
\node[plain,text=BridgeAmber] at (7.1,3.18) {Actual recorded Llama};
\node[plain,text width=3.8cm] at (7.1,.9) {Old reply + original input\\No new model call};
\node[circle,draw=IEEEBlue,line width=1.4pt,text=IEEEBlue,minimum size=1.05cm] at (12.0,2.2) {PILOT};
\node[plain,text=IEEEBlue] at (12.0,3.18) {Proposed control-room pilot};
\node[plain,text width=3.8cm] at (12.0,.9) {Advisory teaching design\\Not a reported deployment};
''',['H00','H03','DEF03','OT01'])

add('ops_request_snapshot','Freeze a relevant study snapshot before asking a tool',
    'Illustrative F12 request: a copied case predating a topology-changing event does not support the new study. HOLD requests a relevant approved snapshot, not an arbitrary universal age threshold.',r'''
\node[plain,text=Slate] at (7.1,3.25) {Illustrative F12 example; no actual utility data};
\node[step,text width=2.65cm] (r) at (1.65,1.9) {Study F12\\Alarm 15:02\\Review 15:05};
\node[step,text width=2.75cm] (s) at (5.3,1.9) {Approved copy: 14:35\\Topology v42\\Limits L3};
\node[step,text width=2.55cm] (c) at (8.95,1.9) {Topology now v43\\Copy remains v42\\Case mismatch};
\node[stop,text width=2.5cm] (h) at (12.45,1.9) {HOLD\\Refresh approved\\snapshot};
\draw[flow] (r)--(s);\draw[flow] (s)--(c);\draw[flow,draw=BridgeRed] (c)--(h);
\node[plain,small,text=Slate] at (7.1,.55) {The topology mismatch invalidates this copy for the requested study.};
''',['OT01','EVAL01'],pilot=True,caveat='Invented F12 timestamps, topology tokens and limit label are teaching examples, not utility data or a defined freshness policy.')

add('ops_tool_boundary','Keep study tools separate from operating authority',
    'Proposed advisory architecture: an assistant can request allowed study tools through a validating, logged gateway using an approved read-only copy. Physical commands follow a separate authorized process.',r'''
\node[plain,anchor=east,text=IEEEBlue] at (1.65,3.3) {Operator};
\node[plain,anchor=east,text=IEEEBlue] at (1.65,2.4) {Assistant};
\node[plain,anchor=east,text=IEEEBlue] at (1.65,1.35) {Tools};
\node[plain,anchor=east,text=BridgeRed] at (1.65,.35) {Authority};
\node[plain] (r) at (3.75,3.3) {Ask for a study};
\node[plain] (review) at (11.6,3.3) {Review study evidence};
\node[plain,text width=3.8cm] (a) at (5.0,2.4) {Llama requests an allowed tool};
\node[step,text width=2.7cm] (copy) at (3.75,1.35) {Approved\\read-only copy};
\node[step,text width=3.0cm] (gate) at (8.1,1.35) {Tool gateway\\Validate + log};
\node[step,text width=2.3cm] (solver) at (12.1,1.35) {Numerical\\study tool};
\draw[flow] (r.south)--(a.north west);\draw[flow] (a.east)-|(gate.north);
\draw[flow] (copy)--(gate);\draw[flow] (gate)--(solver);\draw[flow] (solver.north)--(review.south);
\draw[BridgeRed,dashed,line width=.9pt] (2.1,.8)--(13.6,.8);
\node[plain,text=BridgeRed] at (8.0,.26) {Physical commands: a separate authorized operating process};
''',['OT01','EVAL01','DEF03'],pilot=True,caveat='Tutorial architecture proposal, not a certified OT architecture, utility deployment, direct command path or product integration.')

add('ops_three_gates','Three checks before a study can be reviewed',
    'The review path requires the exact current case, every required limit and the full required model scope. An MV-only PASS cannot satisfy an MV/LV request.',r'''
\foreach \x/\n in {2.0/1,7.1/2,12.2/3} {\node[circle,draw=IEEEBlue,text=IEEEBlue,minimum size=.6cm,inner sep=1pt] at (\x,3.05) {\n};}
\node[plain,text width=3.8cm] (a) at (2.0,2.15) {Same request, command\\and current case version?};
\node[plain,text width=3.8cm] (b) at (7.1,2.15) {All required limits\\actually checked?};
\node[plain,text width=3.8cm] (c) at (12.2,2.15) {Full required\\model scope?};
\draw[flow] (a)--(b);\draw[flow] (b)--(c);
\node[plain,text=IEEEBlue] (mv) at (2.0,.75) {MV-only PASS};
\node[plain] (need) at (7.1,.75) {Request requires MV + LV};
\node[stop,text width=3.0cm,minimum height=.65cm] (hold) at (12.2,.75) {HOLD: LV checks missing};
\draw[flow] (mv)--(need);\draw[flow,draw=BridgeRed] (need)--(hold);
''',['H01','H05','H12','EVAL01'],pilot=True,caveat='The MV/MV-LV scope contrast is grounded in the classroom check, but the complete control-room review sequence is a proposed teaching design.')

add('ops_review','Accepting a study is a bounded review decision',
    'A proposed reviewer checks case consistency, required limits and model scope, then asks for more evidence, rejects the study or accepts it for the separate operating process.',r'''
\node[step,text width=3.05cm] (p) at (1.9,1.95) {Study packet\\Inputs + command\\Checks + model scope\\Missing evidence};
\node[plain,text width=3.9cm] (q) at (7.0,1.95) {Reviewer asks:\\Same case?\\All required limits?\\Right model scope?};
\node[plain,text=BridgeAmber,anchor=west] (more) at (11.0,2.9) {Request more};
\node[plain,text=BridgeRed,anchor=west] (reject) at (11.0,1.95) {Reject study};
\node[plain,text=IEEEBlue,anchor=west] (accept) at (11.0,1.0) {Accept study};
\draw[flow] (p)--(q);
\draw[flow,draw=BridgeAmber] (q.east)--(more.west);\draw[flow,draw=BridgeRed] (q.east)--(reject.west);\draw[flow] (q.east)--(accept.west);
\node[plain,text=Slate] at (7.1,.33) {Accepted study $\ne$ permission to operate equipment.};
''',['OT01','EVAL01','H12'],pilot=True)

add('ops_pilot','Advance a pilot only with comparable evidence',
    'Suggested pilot stages compare an assistant with a fixed-script baseline using the same engineering tools. Proposed measures are correct work, missed checks, time and reviewer changes; an accountable owner can stop the pilot.',r'''
\node[step,text width=3.3cm] (r) at (2.0,2.65) {Historical replay\\Known cases and outcomes};
\node[step,text width=3.3cm] (s) at (7.1,2.65) {Read-only shadow\\No operational commands};
\node[step,text width=3.3cm] (p) at (12.2,2.65) {Reviewed advisory pilot\\Human review of each study};
\draw[flow] (r)--(s);\draw[flow] (s)--(p);
\foreach \x/\label in {1.65/Correct work,5.25/Missed checks,8.85/Time,12.45/Reviewer changes} {
\fill[Cyan] (\x,1.42) circle (.06);\node[plain] at (\x,1.03) {\label};}
\node[plain,text=Slate] at (7.1,.28) {Compare with a fixed script + the same tools. The owner can stop the pilot.};
''',['DEF03','OT01','EVAL01'],pilot=True,caveat='Suggested evaluation design and candidate measures only; no deployment, measured improvement, acceptance target or automatic rollout is asserted.')

SOURCES = {
    'DEF03': {'title':'Building effective agents','organization':'Anthropic','date':'2024-12-19','url':'https://www.anthropic.com/research/building-effective-agents','support':'Attributed workflow/agent distinction, tools, feedback, stopping conditions. The live page notes that tooling has changed since 2024.'},
    'OT01': {'title':'Guide to Operational Technology (OT) Security','organization':'NIST','date':'2023-09','url':'https://doi.org/10.6028/NIST.SP.800-82r3','support':'OT responsibilities and controlled system boundaries; the exact pilot architecture is the tutorial author’s proposal.'},
    'EVAL01': {'title':'Artificial Intelligence Risk Management Framework (AI RMF 1.0)','organization':'NIST','date':'2023-01','url':'https://doi.org/10.6028/NIST.AI.100-1','support':'Documentation, evaluation and accountable risk-management context; no NIST approval of this proposed pilot is claimed.'},
}

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def build():
    manifest = {'schema_version':1,'description':'Twelve original editable teaching diagrams, with matching PDF and vector SVG exports. No product UI, deployment or fresh default-notebook LLM claim.','sources':SOURCES,'items':[]}
    qa = []
    for item in items:
        path = OUT / (item['id']+'.tex')
        path.write_bytes((COLORS+START+item['body'].replace('[step,','[bridgebox,')+END).encode('utf-8'))
        compiler.compile_one(path)
        svg = path.with_suffix('.svg')
        text = svg.read_text(encoding='utf-8')
        match = re.search(r'viewBox="([^"]+)"',text)
        box = [float(v) for v in match.group(1).split()]
        width,height = box[2],box[3]
        pixels = [1150,round(1150*height/width)]
        text = re.sub(r'width="1280" height="\d+"', f'width="{pixels[0]}" height="{pixels[1]}"', text,count=1)
        svg.write_bytes(text.encode('utf-8'))
        pdf = path.with_suffix('.pdf')
        reader = PdfReader(pdf)
        assert len(reader.pages)==1
        content = reader.pages[0].extract_text() or ''
        if item['id'].startswith('ops_'):
            assert 'Proposed advisory pilot' in content
        raster = HERE / (item['id']+'.png')
        subprocess.run([str(compiler.POPPLER/'pdftoppm.exe'),'-png','-singlefile','-scale-to-x','1150','-scale-to-y','-1',str(pdf),str(raster.with_suffix(''))],check=True,capture_output=True)
        with Image.open(raster) as image:
            assert image.width == 1150 and image.height > 200
            raster_dims = list(image.size)
        entry = {key:value for key,value in item.items() if key!='body'}
        entry.update({'files':{ext:f'diagrams/{item["id"]}.{ext}' for ext in ['tex','pdf','svg']},'dimensions_px':pixels,'dimensions_pdf_pt':[width,height],'sha256':{ext:digest(path.with_suffix('.'+ext)) for ext in ['tex','pdf','svg']},'editable':'Native TikZ source. SVG uses vector outlines from the compiled PDF.','source_note':'Original teaching design informed by the listed sources; not a reproduction of an official source figure.'})
        manifest['items'].append(entry)
        qa.append({'id':item['id'],'pdf_pages':len(reader.pages),'svg_dimensions_px':pixels,'raster_dimensions_px':raster_dims,'pdf_text':content,'raster_file':raster.name,'nonempty_svg':len(text)>1000})
    (OUT/'visual_bridge_manifest.json').write_bytes(json.dumps(manifest,indent=2,ensure_ascii=False).encode())
    (HERE/'render_qa.json').write_bytes(json.dumps(qa,indent=2,ensure_ascii=False).encode())
    print(json.dumps({'assets':len(items),'ids':[i['id'] for i in items],'manifest':str(OUT/'visual_bridge_manifest.json')},indent=2))

if __name__=='__main__':
    build()
