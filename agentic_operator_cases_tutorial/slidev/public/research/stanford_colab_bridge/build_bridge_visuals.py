"""Original editable grid teaching aids linking Stanford concepts to the three labs."""
from pathlib import Path
import importlib.util,json,os
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('diagram_compiler',ROOT/'build_diagrams.py')
compiler=importlib.util.module_from_spec(spec);spec.loader.exec_module(compiler)
compiler.TECTONIC=Path(os.environ.get('OPERATOR_TECTONIC',r'C:/Users/f00863x/OPRO/tmp/tectonic_017/unpacked/tectonic.exe'))
START=r'''\begingroup
\begin{tikzpicture}[x=1cm,y=1cm,font=\sffamily\fontsize{10}{12}\selectfont,
every node/.style={text=Navy,align=center},
flow/.style={-{Stealth[length=2.2mm]},draw=IEEEBlue,line width=1.3pt},
box/.style={draw=IEEEBlue,line width=1.1pt,inner sep=7pt,minimum height=.95cm},
small/.style={font=\sffamily\fontsize{8.5}{11}\selectfont}]
'''
END='\n\\end{tikzpicture}\n\\endgroup\n'
items=[]
def add(id,body,refs,caption):items.append(dict(id=id,body=body,refs=refs,caption=caption))
add('stanford_colab_voltage',r'''
\node[text=IEEEBlue,font=\sffamily\bfseries] at (2,4.0) {L2: define the case};
\node[text width=3.4cm] (input) at (2,2.65) {Load case\\Current allowance};
\node[box,text width=3.0cm] (tool) at (6.85,2.65) {Calculate a plan\\Check the current};
\draw[flow] (input)--(tool);
\draw[flow] (tool.east)--(9.35,2.65);
\node[text=IEEEBlue,font=\sffamily\bfseries] at (11.55,4.0) {Read the tool result};
\fill[IEEEBlue] (9.65,2.35) rectangle (12.5948,2.95);
\draw[Red,dashed,line width=1.1pt] (13.65,1.95)--(13.65,3.45);
\node[small,text=Red] at (13.45,3.65) {100\% limit};
\node[small,text=white] at (11.12,2.65) {73.62\%};
\node[small] at (9.65,1.65) {0\%};
\node[small,text width=4.6cm] at (11.65,1.1) {Percent of allowed current\\Reference L2 MPC result};
\node[text=Cyan,text width=13.5cm] at (7.1,.25) {This current check passes. Review voltage and model coverage too.};
''',['ST01','ST02','H02'],'Grid teaching adaptation of evidence checking in WikiChat. Reference fresh L2 MPC current: 73.619901% at LOAD_SCALE=1.0, RATING_FRACTION=0.80, rounded to 73.62%.')
add('stanford_colab_restoration',r'''
\node[text=Slate,small] at (7.2,4.0) {L6 / varied tie: 40 kW / fixed tie: 100 kW / totals include upstream load};
\node[text width=4.0cm,align=left,font=\sffamily\bfseries] at (2.2,2.9) {Give critical service\\more weight};
\node[text width=4.0cm,align=left,font=\sffamily\bfseries] at (2.2,1.5) {Serve the most\\total kW};
\fill[Cyan] (5.2,2.55) rectangle (9.7,3.25);
\fill[IEEEBlue] (9.7,2.55) rectangle (11.7,3.25);
\node[text=Navy,font=\sffamily\bfseries] at (7.45,2.9) {90};
\node[text=white,font=\sffamily\bfseries] at (10.7,2.9) {40};
\node[anchor=west] at (12.0,2.9) {130 kW total};
\fill[Cyan] (5.2,1.15) rectangle (6.7,1.85);
\fill[IEEEBlue] (6.7,1.15) rectangle (12.2,1.85);
\node[text=Navy,font=\sffamily\bfseries] at (5.95,1.5) {30};
\node[text=white,font=\sffamily\bfseries] at (9.45,1.5) {110};
\node[anchor=west] at (12.5,1.5) {140 kW total};
\fill[Cyan] (4.1,.25) rectangle (4.5,.6);\node[anchor=west,small] at (4.65,.425) {Critical service};
\fill[IEEEBlue] (8.2,.25) rectangle (8.6,.6);\node[anchor=west,small] at (8.75,.425) {Other service};
''',['ST01','ST03','H06'],'Grid teaching adaptation of explicit task rules in Genie Worksheets. Bar lengths show the exact L6 default 40 kW outcomes, including upstream node 1: 130 total/90 critical versus 140 total/30 critical kW.')
add('stanford_colab_cyber',r'''
\node[anchor=west,text=IEEEBlue,font=\sffamily\bfseries] at (.2,4.35) {L8: do the readings fit the model?};
\node[text width=2.4cm] (data) at (1.65,3.5) {Readings};
\node[box,text width=3.4cm] (fit) at (7.2,3.5) {Python fits the model};
\node[text width=3.6cm] (res) at (12.6,3.5) {Small mismatch\\can still hide an error};
\draw[flow] (data)--(fit);\draw[flow] (fit)--(res);
\draw[Slate!35] (.2,2.6)--(14.4,2.6);
\node[anchor=west,text=IEEEBlue,font=\sffamily\bfseries] at (.2,2.2) {L9: is recovery supported?};
\node[text width=5.5cm] (trust) at (7.2,1.3) {Trusted data assumed\\and recovery check passes?};
\node[draw=Red,text=Red,inner sep=7pt,line width=1.1pt] (hold) at (1.6,1.3) {HOLD};
\node[draw=Cyan,text=Cyan,inner sep=7pt,line width=1.1pt] (propose) at (12.8,1.3) {PROPOSE};
\draw[flow] (trust.west)--node[above,small]{No}(hold.east);
\draw[flow] (trust.east)--node[above,small]{Yes}(propose.west);
\node[small,text=Slate,text width=14cm] at (7.2,.2) {L9 assumes those extra readings are trusted. The numerical tool does not authenticate them.};
''',['ST01','H08','H09'],'Grid teaching adaptation of separating language from decision checks. L8 fit is not authentication. L9 needs an explicit trusted-data premise plus its numerical checks.')

def main():
 for item in items:
  src=ROOT/'diagrams'/(item['id']+'.tex');src.write_text(START+item['body']+END,encoding='utf-8')
  compiler.compile_one(src)
  log=(compiler.BUILD/(item['id']+'_wrapper.log')).read_text(encoding='utf-8',errors='replace')
  assert 'Overfull' not in log and 'Missing character' not in log,item['id']
 (ROOT/'diagrams/stanford_colab_bridge_manifest.json').write_text(json.dumps([{k:v for k,v in x.items() if k!='body'} for x in items],indent=2)+'\n',encoding='utf-8')
if __name__=='__main__':main()
