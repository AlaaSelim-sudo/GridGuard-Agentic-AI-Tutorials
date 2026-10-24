"""Original TikZ teaching aids, with conceptual sources recorded per diagram."""
from pathlib import Path
import importlib.util,json,os
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('diagram_compiler',ROOT/'build_diagrams.py')
compiler=importlib.util.module_from_spec(spec);spec.loader.exec_module(compiler)
compiler.TECTONIC=Path(os.environ.get('OPERATOR_TECTONIC',r'C:/Users/f00863x/OPRO/tmp/tectonic_017/unpacked/tectonic.exe'))
START=r'''\begingroup
\begin{tikzpicture}[x=1cm,y=1cm,font=\sffamily\fontsize{9.5}{12}\selectfont,
every node/.style={text=Navy,align=center},
flow/.style={-{Stealth[length=2mm]},draw=IEEEBlue,line width=1.2pt},
label/.style={text width=2.5cm,align=center},
box/.style={draw=IEEEBlue,line width=1pt,fill=white,inner sep=7pt,minimum height=1cm},
small/.style={font=\sffamily\fontsize{8}{10}\selectfont},
stop/.style={draw=Red,text=Red,fill=Red!4,line width=1pt,inner sep=6pt}]
\path[use as bounding box] (-.05,-.1) rectangle (14.5,4.0);
'''
END='\n\\end{tikzpicture}\n\\endgroup\n'
items=[]
def add(id,body,refs,caption):items.append(dict(id=id,body=body,refs=refs,caption=caption))

add('lab_stanford_steps',r'''
\node[text=IEEEBlue] at (7.2,3.6) {One large request becomes a sequence of smaller jobs};
\foreach \x/\n/\t/\d in {1.2/1/Read/Goal and data,4.2/2/Choose/Allowed tool,7.2/3/Calculate/Numerical result,10.2/4/Check/Limits and scope,13.2/5/Explain/Evidence and gaps} {
\node[circle,draw=IEEEBlue,line width=1pt,minimum size=.65cm] at (\x,2.6) {\n};
\node[label,font=\sffamily\bfseries] at (\x,1.85) {\t};
\node[label,small] at (\x,1.15) {\d};}
\foreach \a/\b in {1.6/3.8,4.6/6.8,7.6/9.8,10.6/12.8}{\draw[flow] (\a,2.6)--(\b,2.6);}
\node[text=Slate,small] at (7.2,.25) {Our lab: each saved output lets us inspect one part of that sequence.};
''',['ST01','ST02'],'Original power-system teaching adaptation of task decomposition; Lam, CS224V introduction, p.19. This notebook does not implement WikiChat.')

add('lab_claim_evidence',r'''
\node[text=IEEEBlue,font=\sffamily\bfseries] at (3.4,3.5) {Find the rule};
\draw[IEEEBlue] (1.2,1.5) rectangle (5.6,3.0);
\node[text width=4cm] at (3.4,2.25) {Study input:\\Allowed-current threshold = 100\%};
\node[text=IEEEBlue,font=\sffamily\bfseries] at (10.9,3.5) {Test the proposal};
\draw[Cyan,line width=1pt] (8.0,1.5) rectangle (13.8,3.0);
\node[text width=5.2cm] at (10.9,2.25) {Recorded P3 tool result:\\99.604410\% of allowed current};
\draw[flow] (5.7,2.25)--(7.9,2.25);
\node[text=Slate,text width=6cm] at (3.4,.75) {Reading a rule does not measure current.};
\node[text=Cyan,text width=5.8cm] at (10.9,.75) {This check passes. Review the other required checks.};
''',['ST01','ST02','LRV'],'Evidence-based teaching analogy inspired by WikiChat. The numerical value is from the separate recorded P3 study, not a new Colab result.')

add('lab_workflow_spec',r'''
\node[text=IEEEBlue,font=\sffamily\bfseries] at (3.0,3.55) {Before using a tool, define the task};
\node[box,text width=4.9cm] (s) at (3.0,1.9) {Input: case + current limits\\Goal: the requested study\\Tools: the allowed functions\\Stop: missing data or failed checks};
\node[box,text width=3.2cm] (gate) at (8.0,1.9) {Are required inputs\\and checks available?};
\node[text=Cyan,text width=2.8cm] (run) at (12.3,2.8) {Yes: run the\\permitted study};
\node[stop,text width=2.8cm] (hold) at (12.3,.8) {No: HOLD\\name what is missing};
\draw[flow] (s)--(gate);\draw[flow] (gate.east)--++(.65,0)|-(run.west);\draw[flow] (gate.east)--++(.65,0)|-(hold.west);
''',['ST01','ST03','H01'],'Original analogy to developer-specified workflows in Genie Worksheets; Lam p.40. No Genie runtime or theorem prover is used in this notebook.')

add('lab_colab_workbook',r'''
% Workbook pages and temporary computer are deliberately different pictures.
\draw[IEEEBlue,line width=1.1pt] (.8,.9)--(.8,3.05)--(2.5,2.78)--(4.2,3.05)--(4.2,.9)--(2.5,.62)--cycle;
\draw[IEEEBlue] (2.5,.65)--(2.5,2.78);
\node[small,text width=1.3cm] at (1.65,1.95) {Text\\Code};
\node[small,text width=1.3cm] at (3.35,1.95) {Plots\\Results};
\node[text=IEEEBlue] at (2.5,3.55) {Your notebook};
\draw[Cyan,line width=1.1pt] (9.1,.85) rectangle (13.2,3.1);
\draw[IEEEBlue] (9.55,1.25) rectangle (12.75,2.7);
\node[text width=2.8cm] at (11.15,2.0) {Temporary CPU\\Runs Python};
\foreach \x in {9.8,10.5,11.2,11.9,12.6}{\draw[Cyan] (\x,.65)--(\x,.85);\draw[Cyan] (\x,3.1)--(\x,3.3);}
\node[text=IEEEBlue] at (11.15,3.65) {Computer supplied by Colab};
\draw[flow] (4.5,2.5)--node[above]{Run code}(8.8,2.5);
\draw[flow] (8.8,1.3)--node[below]{Return output}(4.5,1.3);
\node[small,text=Slate,text width=6.4cm] at (3.2,.12) {Save your notebook copy in Drive or download it.};
\node[small,text=Slate,text width=6.3cm] at (11.0,.12) {A reset clears variables and temporary files.};
''',['COL01','H00'],'Original illustration of a notebook and its runtime, based on the Google Colab FAQ. Saving the notebook does not preserve temporary runtime files.')

add('lab_cell_loop',r'''
\node[text=IEEEBlue,font=\sffamily\bfseries] at (2.7,3.55) {1. Input};
\node[box,text width=4.5cm,font=\ttfamily\fontsize{9}{12}\selectfont] (code) at (2.7,2.0) {LOAD\_SCALE = 1.0\\RATING\_FRACTION = 0.80};
\node[text=IEEEBlue] at (7.2,3.55) {2. Run the whole cell};
\draw[IEEEBlue,fill=Cyan!10,line width=1.2pt] (7.2,2.0) circle (.65);
\fill[IEEEBlue] (6.98,1.67)--(6.98,2.33)--(7.51,2.0)--cycle;
\node[box,text width=3.4cm] (result) at (12.2,2.0) {Table + plot\\Read the limit check};
\node[text=IEEEBlue,font=\sffamily\bfseries] at (12.2,3.55) {3. Read the output};
\draw[flow] (code.east)--(6.5,2);\draw[flow] (7.9,2)--(result.west);
\node[small,text=Slate,text width=13cm] at (7.2,.5) {The play button executes Python. The saved text below a cell is its output.};
''',['COL01','H02'],'Teaching illustration, not a Colab interface screenshot. The two input statements are exact L2 source lines; run the full L2 cell.')

add('lab_try_observe',r'''
\node[text=IEEEBlue,font=\sffamily\bfseries] at (3.1,3.5) {L2: change one number};
\node[box,text width=4.6cm] at (3.1,2.0) {RATING\_FRACTION\\0.80 becomes 0.75\\Predict, then rerun L2};
\draw[flow] (5.7,2.0)--(7.0,2.0);
\draw[Slate] (7.6,.8)--(14.0,.8);
\draw[Red,dashed] (7.6,2.95)--(14,2.95);
\node[small,text=Red,anchor=east] at (14,3.25) {100\% limit};
\fill[IEEEBlue!85] (8.5,.8) rectangle (10.0,2.3838);
\fill[Cyan!85] (11.3,.8) rectangle (12.8,2.4894);
\node[small] at (9.25,2.65) {73.62\%};\node[small] at (12.05,2.75) {78.53\%};
\node[small] at (9.25,.38) {Default};\node[small] at (12.05,.38) {Changed allowance};
\node[small,text=Slate,text width=6cm] at (3.1,.48) {Reference MPC results. Both checks still pass.};
''',['H02'],'Original plot of the verified L2 exercise results. These are reference values for the stated inputs; rerun the notebook to calculate your result.')

add('lab_one_notebook',r'''
\node[box,text width=5.1cm,font=\ttfamily\fontsize{10}{12}\selectfont] (book) at (7.2,3.2) {Classroom\_Labs.ipynb};
\node[text=IEEEBlue,text width=3.4cm] (v) at (2.3,1.7) {Voltage\\L2--L5};
\node[text=IEEEBlue,text width=3.4cm] (r) at (7.2,1.7) {Restoration\\L6--L7};
\node[text=IEEEBlue,text width=3.4cm] (c) at (12.1,1.7) {Cyber\\L8--L9};
\draw[flow] (book.south)--(7.2,2.5)-|(v.north);\draw[flow] (book.south)--(r.north);\draw[flow] (7.2,2.5)-|(c.north);
\node[small,text width=4.3cm] at (2.3,.75) {Change a current allowance};
\node[small,text width=4.3cm] at (7.2,.75) {Change a tie capacity};
\node[small,text width=4.3cm] at (12.1,.75) {Change a data bias};
\node[small,text=Slate] at (7.2,.05) {L10B replays Llama choices in the same file. Each case uses a separate teaching network.};
''',['H00'],'One required notebook covers all three cases and the L10B replay. Companion graph and trace notebooks are not required for this workshop.')

add('lab_ready',r'''
\foreach \x/\n/\t/\d in {1.6/1/Open/Use the Colab link,5.3/2/Keep/Save a Drive copy,9.0/3/Connect/CPU runtime,12.7/4/Prepare/Run setup to Ready} {
\node[circle,draw=IEEEBlue,line width=1pt,minimum size=.7cm] at (\x,2.7) {\n};
\node[text=IEEEBlue] at (\x,1.95) {\t};\node[small,text width=3.0cm] at (\x,1.2) {\d};}
\foreach \a/\b in {2.1/4.8,5.8/8.5,9.5/12.2}{\draw[flow] (\a,2.7)--(\b,2.7);}
\node[text=Slate,small,text width=13.7cm] at (7.2,.25) {For the guided workshop, run each named lesson when prompted. Run all is a useful setup check.};
''',['COL01','H00'],'Original setup sequence based on this notebook and the Google Colab FAQ. Default lessons need no GPU, API key or live LLM service.')

add('lab_record',r'''
\node[text=IEEEBlue,font=\sffamily\bfseries] at (3.4,3.5) {One person runs};
\node[text=IEEEBlue,font=\sffamily\bfseries] at (11.0,3.5) {One person checks};
\node[text width=5.7cm] at (3.4,2.25) {Predict the change\\Edit one number\\Run the cell};
\node[text width=5.7cm] at (11.0,2.25) {Read the result\\Check its limits and model\\Explain the next step};
\draw[flow] (6.0,2.25)--(8.4,2.25);
\draw[Cyan,line width=1pt] (.7,1.0)--(13.8,1.0);
\node[small,text width=13cm] at (7.2,.45) {Save four things: input changed, result, check outcome and next decision. Swap roles in the next case.};
''',['H00'],'Original pair-work teaching aid. Save enough information for another person to repeat the experiment.')

def main():
 for item in items:
  src=ROOT/'diagrams'/(item['id']+'.tex');src.write_text(START+item['body']+END,encoding='utf-8')
  compiler.compile_one(src)
  log=(compiler.BUILD/(item['id']+'_wrapper.log')).read_text(encoding='utf-8',errors='replace')
  assert 'Overfull' not in log and 'Missing character' not in log,item['id']
 (ROOT/'diagrams/lab_teaching_manifest.json').write_text(json.dumps([{k:v for k,v in x.items() if k!='body'} for x in items],indent=2)+'\n',encoding='utf-8')
if __name__=='__main__':main()
