"""Projection-sized native teaching diagrams for the concrete agentic opening."""
from pathlib import Path
import importlib.util,json,os
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('diagram_compiler',ROOT/'build_diagrams.py')
compiler=importlib.util.module_from_spec(spec);spec.loader.exec_module(compiler)
compiler.TECTONIC=Path(os.environ.get('OPERATOR_TECTONIC',r'C:/Users/f00863x/OPRO/tmp/tectonic_017/unpacked/tectonic.exe'))
START=r'''\begingroup
\begin{tikzpicture}[x=1cm,y=1cm,font=\sffamily\fontsize{10}{12}\selectfont,
every node/.style={text=Navy,align=center},
flow/.style={-{Stealth[length=2.2mm]},draw=IEEEBlue,line width=1.4pt},
feedback/.style={-{Stealth[length=2.2mm]},draw=Cyan,line width=1.6pt},
box/.style={draw=IEEEBlue,line width=1.1pt,fill=white,inner sep=7pt,minimum height=.95cm},
small/.style={font=\sffamily\fontsize{8.5}{11}\selectfont}]
'''
END='\n\\end{tikzpicture}\n\\endgroup\n'
items=[]
def add(id,body,refs,caption):items.append(dict(id=id,body=body,refs=refs,caption=caption))
add('agent_goal_loop',r'''
\node[align=left,text width=2.8cm] (goal) at (1.35,2.6) {\textbf{Goal}\\Find a plan that\\passes the limits};
\node[box,text width=3.1cm,fill=Cyan!7] (model) at (5.2,2.6) {\textbf{LLM agent}\\Choose the next tool};
\node[box,text width=3.2cm] (tool) at (11.9,2.6) {\textbf{Numerical tool}\\Calculate and check};
\draw[flow] (goal.east)--(model.west);
\draw[flow] (model.east)--node[above,small]{Request}(tool.west);
\draw[feedback] (tool.south)--(11.9,.95)--node[below,small,text=Cyan]{Read the result; choose again}(5.2,.95)--(model.south);
\node[small,text=Slate,text width=3.9cm] at (5.2,4.0) {Keeps the goal, case facts\\and previous tool results};
\node[small,text=Slate,text width=4.1cm] at (11.9,4.0) {Only permitted functions\\with fixed input checks};
\node[small,text=IEEEBlue] at (7.25,.05) {When ready: return evidence for review. If a required check is missing: HOLD.};
''',['DEF03','LR0'],'Original bounded LLM-agent teaching loop; architecture adapted from Anthropic, Building effective agents. This workshop replays the LLM choices.')
add('agent_text_tool',r'''
\node[anchor=west,text=IEEEBlue,font=\sffamily\bfseries] at (.15,4.1) {Text-only interaction};
\node[text width=2.1cm] (q) at (1.7,3.1) {Question};
\node[box,text width=2.1cm] (m) at (6.4,3.1) {LLM};
\node[text width=3.0cm] (a) at (12.2,3.1) {Written reply};
\draw[flow] (q)--(m);\draw[flow] (m)--(a);
\draw[Slate!35] (.15,2.35)--(14.3,2.35);
\node[anchor=west,text=Cyan,font=\sffamily\bfseries] at (.15,1.95) {Tool-using agent};
\node[text width=2.5cm] (g) at (1.7,.9) {Goal + case facts};
\node[box,text width=2.5cm,fill=Cyan!7] (am) at (6.4,.9) {LLM chooses\\a permitted step};
\node[box,text width=2.5cm] (t) at (12.2,.9) {Run tool\\Return result};
\draw[flow] (g)--(am);\draw[flow] (am.east)--node[above,small]{Tool request}(t.west);
\draw[feedback] (t.south)--(12.2,-.15)--node[below,small,text=Cyan]{Result changes the next choice}(6.4,-.15)--(am.south);
''',['DEF03','LR0'],'Two interaction patterns, not a claim that every chatbot lacks tools. Ordinary programs can also loop; here the LLM selects the permitted next action.')
add('agent_recorded_trace',r'''
\node[anchor=west,text=Slate,small] at (.1,4.05) {Recorded voltage study P3 / Llama 3.1:8b / OpenDSS};
\node[text width=3.2cm,font=\sffamily\bfseries] at (1.65,3.5) {Llama chooses};
\node[text width=3.2cm,font=\sffamily\bfseries] at (5.35,3.5) {Tool returns};
\node[text width=3.2cm,font=\sffamily\bfseries] at (9.05,3.5) {Llama chooses};
\node[text width=3.2cm,font=\sffamily\bfseries] at (12.75,3.5) {Tool returns};
\node[box,text width=2.5cm] (a) at (1.65,2.25) {Check the\\SAC proposal};
\node[box,draw=Red,text width=2.5cm] (b) at (5.35,2.25) {\textcolor{Red}{\textbf{111.97\%}}\\Current check fails};
\node[box,text width=2.5cm] (c) at (9.05,2.25) {Check the\\MPC fallback};
\node[box,draw=Cyan,text width=2.5cm] (d) at (12.75,2.25) {\textcolor{Cyan}{\textbf{99.60\%}}\\Current check passes};
\draw[flow] (a)--(b);\draw[feedback] (b)--(c);\draw[flow] (c)--(d);
\node[small,text=Slate,text width=10cm] at (5.7,1.05) {Percent of allowed current / limit = 100\% / rounded values};
\draw[flow] (d.south)--(12.75,.45)--(10.3,.45);
\node[anchor=east,text width=9cm] at (10.25,.45) {\textbf{Next: evidence for human review. Acknowledgment is still pending.}};
''',['LRV','LR0'],'Exact recorded P3 current checks rounded to two decimals. This is a preview of a saved L10B episode, separate from the fresh L2 exercise.')
add('agent_roles_simple',r'''
% Three distinct symbols communicate language choice, computation and human review.
\draw[IEEEBlue,line width=1.2pt,rounded corners=3pt] (.5,2.2) rectangle (3.7,3.8);
\draw[IEEEBlue,line width=1.2pt] (1.2,2.2)--(1.0,1.8)--(1.8,2.2);
\node[text=IEEEBlue,font=\sffamily\bfseries] at (2.1,3.0) {Llama};
\draw[Cyan,line width=1.2pt] (5.9,2.0) rectangle (9.0,3.9);
\node[font=\ttfamily\fontsize{12}{14}\selectfont,text=Cyan] at (7.45,3.0) {f(x) = y};
\draw[IEEEBlue,line width=1.2pt] (12.3,3.5) circle (.4);
\draw[IEEEBlue,line width=1.2pt] (11.6,2.0)--(11.6,2.65) arc (180:0:.7)--(13.0,2.0);
\node[text width=4.2cm,font=\sffamily\bfseries] at (2.1,1.15) {Choose and explain};
\node[text width=4.2cm,font=\sffamily\bfseries] at (7.45,1.15) {Calculate and check};
\node[text width=4.2cm,font=\sffamily\bfseries] at (12.3,1.15) {Review and decide};
\node[small,text width=4cm] at (2.1,.35) {Select a permitted next step};
\node[small,text width=4cm] at (7.45,.35) {Python / OpenDSS enforce limits};
\node[small,text width=4cm] at (12.3,.35) {Operator keeps authority};
\draw[flow] (3.9,3.0)--(5.6,3.0);\draw[flow] (9.3,3.0)--(11.4,3.0);
''',['DEF03','LR0','OLL1'],'Roles in the bounded recorded workflows. The default notebook calculates new numerical results and displays saved Llama replies; it sends no equipment commands.')
add('agent_mpc_sac',r'''
\node[text=IEEEBlue,font=\sffamily\bfseries] at (2.9,4.0) {MPC: plan from a model};
\node[box,text width=4.8cm] (mpc) at (2.9,2.9) {Case + short forecast\\Optimize the next control settings};
\node[text=Cyan,font=\sffamily\bfseries] at (11.5,4.0) {SAC: use a learned controller};
\node[box,draw=Cyan,text width=4.8cm] (sac) at (11.5,2.9) {Case + saved policy weights\\Produce the next control settings};
\node[box,text width=6.7cm] (check) at (7.2,.95) {\textbf{The same numerical check}\\Do voltage and current stay within the limits?};
\draw[flow] (mpc.south)--(2.9,.95)--(check.west);
\draw[flow] (sac.south)--(11.5,.95)--(check.east);
\node[small,text=Slate] at (7.2,-.05) {These are two control tools. The outer LLM agent can choose which tool to request next.};
''',['H02','VMPC','VSAC','LRV'],'Original diagram of the two controller roles. L2 calculates both proposals directly. Recorded Llama coordination is shown separately; no policy training occurs in L2.')
add('agent_python_tool',r'''
\node[text=IEEEBlue,font=\sffamily\bfseries] at (1.9,3.8) {Inputs};
\node[text width=3.4cm] (input) at (1.9,2.55) {Load scale: 1.0\\Allowance: 0.80};
\node[box,text width=5.0cm] (func) at (7.0,2.55) {\textbf{Python function}\\\texttt{lab.voltage\_lab(...)}\\Calculate proposals and checks};
\node[text=IEEEBlue,font=\sffamily\bfseries] at (12.6,3.8) {Returned results};
\node[text width=3.5cm] (output) at (12.6,2.55) {Control settings\\Voltages and currents\\Pass / fail};
\draw[flow] (input)--(func);\draw[flow] (func)--(output);
\draw[Cyan,line width=1pt] (.2,1.25)--(14.4,1.25);
\node[text width=13.6cm] at (7.2,.55) {\textbf{In L2, your cell calls this function directly.}\\In the recorded agent study, Python checks Llama's choice before running an allowed tool.};
''',['H02','LR0'],'A tool is executable software with defined inputs and returned evidence. The L2 function call is direct; the recorded agent gateway is a separate workflow.')

def main():
 for item in items:
  src=ROOT/'diagrams'/(item['id']+'.tex');src.write_text(START+item['body']+END,encoding='utf-8')
  compiler.compile_one(src)
  log=(compiler.BUILD/(item['id']+'_wrapper.log')).read_text(encoding='utf-8',errors='replace')
  assert 'Overfull' not in log and 'Missing character' not in log,item['id']
 (ROOT/'diagrams/agentic_opening_manifest.json').write_text(json.dumps([{k:v for k,v in x.items() if k!='body'} for x in items],indent=2)+'\n',encoding='utf-8')
if __name__=='__main__':main()
