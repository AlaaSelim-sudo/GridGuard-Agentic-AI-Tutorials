"""Editable diagrams mapping the actual saved five-role workflow to each case."""
from pathlib import Path
import hashlib,importlib.util,json,os

ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('compiler',ROOT/'build_diagrams.py')
compiler=importlib.util.module_from_spec(spec);spec.loader.exec_module(compiler)
compiler.TECTONIC=Path(os.environ.get('TECTONIC',r'C:/Users/f00863x/OPRO/tmp/tectonic_017/unpacked/tectonic.exe'))
HEAD=r'''\begingroup
\begin{tikzpicture}[x=1cm,y=1cm,font=\sffamily\fontsize{9}{10.5}\selectfont,
every node/.style={align=center,text=Navy},
role/.style={draw=IEEEBlue,line width=1.1pt,text width=2.55cm,minimum height=1.95cm,inner sep=4pt},
flow/.style={-{Stealth[length=2.3mm]},draw=IEEEBlue,line width=1.3pt},
loop/.style={-{Stealth[length=2.3mm]},draw=Cyan,line width=1.4pt},
small/.style={font=\sffamily\fontsize{8.6}{10.5}\selectfont}]
'''
ITEMS=[
 dict(id='multi_agent_roles',title='Five roles with structured handoffs',
      nodes=[('Awareness','Python','Read case facts\\and limits'),('Planning','Llama + tools','Request two\\proposals'),('Simulation','Python','Calculate\\the effects'),('Verification','Python','Check limits\\and case match'),('Optimizer','Llama','Choose a trial\\or rank results')],
      line='Same case facts, candidate IDs and tool results pass between roles.',
      result='Default Colab: replay of saved roles and results. No new LLM run.'),
 dict(id='multi_agent_voltage',title='Voltage: the five roles in the L10 MV archive',
      nodes=[('Awareness','Python','Load and\\current limit'),('Planning','Llama + tools','Request MPC\\and SAC trials'),('Simulation','Python','Calculate voltage\\and current'),('Verification','Python','Check voltage\\and current'),('Optimizer','Llama','Less Q; then\\more PV power')],
      line='Changed settings return to the same simulation and verification steps.',
      result='Final recheck: 50.75\\% allowed-current use. MV only. Human review pending.'),
 dict(id='multi_agent_restoration',title='Restoration: the five roles in the L10 feeder catalog',
      nodes=[('Awareness','Python','Fault, ties and\\critical loads'),('Planning','Llama + tools','Request two\\restoration plans'),('Simulation','Python','Calculate service\\and current'),('Verification','Python','Reject failed\\plans'),('Optimizer','Llama','Try two levels\\of load shedding')],
      line='Python rejects the failed trial and corrects the wrong cost order.',
      result='Selected: 1,843.61 kW served, 474.04 kW critical, 91.87\\% current use.'),
 dict(id='multi_agent_cyber',title='Cyber: the five roles in the L10 DC archive',
      nodes=[('Awareness','Python','Readings and\\assumed trust'),('Planning','Llama + tools','Request two\\response options'),('Simulation','Python','Estimate state;\\calculate action'),('Verification','Python','Check trust rule\\and flow limits'),('Optimizer','Llama','Try QP with\\trusted data')],
      line='Trusted channels are assumed. No role authenticates the sensors.',
      result='Selected correction: u = 0.121694 p.u. Predicted flow = 0.17000 p.u.'),
]

def make(item):
 out=[HEAD]
 for j,(name,method,detail) in enumerate(item['nodes']):
  detail=detail.replace(chr(92),chr(92)*2)
  x=1.5+3.13*j;fill=',fill=Cyan!7' if j in (1,4) else ''
  out.append('\\node[role'+fill+'] (r'+str(j)+') at ('+str(x)+',2.5) {\\textbf{'+name+'}\\\\{\\small '+method+'}\\\\[3pt]'+detail+'};\n')
  if j:out.append(f'\\draw[flow] (r{j-1}.east)--(r{j}.west);\n')
 out.extend([
  r'\draw[loop] (r4.north)--(14.02,4.0)--node[above,small,text=Cyan]{New trial returns for calculation and checking}(7.76,4.0)--(r2.north);'+'\n',
  r'\node[role,minimum height=.65cm,text width=4.1cm] (final) at (9.2,-.1) {\textbf{Final numerical recheck}};'+'\n',
  r'\node[role,minimum height=.65cm,text width=3cm] (human) at (13.6,-.1) {\textbf{Operator review}};'+'\n',
  r'\draw[flow] (r4.east)--(15.65,2.5)--(15.65,.62)--node[above,small]{Selected option}(9.2,.62)--(final.north);'+'\n',
  r'\draw[flow] (final.east)--(human.west);'+'\n',
  r'\node[align=left,text width=6.1cm,small] at (3.0,-.1) {Only passed candidates can be ranked.\\Human review stays separate from dispatch.};'+'\n',
  r'\node[text width=15.6cm,font=\sffamily\bfseries\fontsize{10.5}{13}\selectfont,text=IEEEBlue] at (7.76,-1.0) {'+item['result']+'};\n',
  '\\end{tikzpicture}\n\\endgroup\n'])
 return ''.join(out)

def main():
 entries=[]
 for item in ITEMS:
  file=ROOT/'diagrams'/(item['id']+'.tex');file.write_text(make(item),encoding='utf-8');compiler.compile_one(file)
  entries.append({k:v for k,v in item.items() if k!='nodes'}|{'credit':'Original teaching diagram of the actual recorded Python workflow','sources':['WF01','H10'],'scope':'Custom five-role orchestrator. One Llama model in two roles. Saved execution, not a new model call.','sha256':{ext:hashlib.sha256(file.with_suffix('.'+ext).read_bytes()).hexdigest() for ext in ['tex','pdf','svg']}})
 (ROOT/'diagrams/five_role_manifest.json').write_text(json.dumps({'items':entries},indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'diagrams':len(entries),'source':'proposal_workflow.py and saved proposal_complete_workflow.json'}))

if __name__=='__main__':main()
