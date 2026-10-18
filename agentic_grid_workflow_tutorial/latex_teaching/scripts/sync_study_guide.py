from pathlib import Path
import re,json,hashlib
project=Path(__file__).resolve().parents[1]
root=project.parent

def argument(s,pos):
    while pos<len(s) and s[pos].isspace():pos+=1
    if s[pos]!='{':raise ValueError((s[pos:pos+40],pos))
    start=pos+1;depth=1;pos+=1
    while depth:
        if s[pos]=='\\':pos+=2;continue
        if s[pos]=='{':depth+=1
        elif s[pos]=='}':depth-=1
        pos+=1
    return s[start:pos-1],pos
def macro(s,name):
    m=re.search(r'\\'+name+r'(?![A-Za-z])\s*\{',s)
    return argument(s,m.end()-1)[0] if m else ''
def frames(s):
    for m in re.finditer(r'\\begin\{frame\}(?:\[[^\]]*\])?\s*\{',s):
        title,end=argument(s,m.end()-1)
        stop=s.index(r'\end{frame}',end)
        yield title,s[end:stop]

chapters=[('Foundations','foundations.tex'),('Voltage support','voltage.tex'),('Restoration','restoration.tex'),('Cyber response','cyber.tex'),('Evaluation and operator decisions','closing.tex')]
allframes=[]
for chapter,filename in chapters:
    text=(project/'chapters'/filename).read_text(encoding='utf-8')
    for title,body in frames(text):
        allframes.append({'chapter':chapter,'file':filename,'title':title,'body':body,'id':macro(body,'label').replace('f:','')})
    if filename=='voltage.tex':
        text=(project/'main.tex').read_text(encoding='utf-8')
        for title,body in frames(text):
            allframes.append({'chapter':'Break','file':'main.tex','title':title,'body':body,'id':'BREAK'})

preamble=r'''\documentclass[11pt]{article}
\usepackage[a4paper,margin=20mm]{geometry}
\usepackage[T1]{fontenc}\usepackage{lmodern}
\usepackage{amsmath,amssymb,graphicx,xcolor,booktabs,array,longtable,listings,hyperref}
\definecolor{teal}{HTML}{08734F}\definecolor{navy}{HTML}{173F37}\definecolor{pale}{HTML}{EDF5F0}\definecolor{slate}{HTML}{52635E}\definecolor{amber}{HTML}{A66610}\definecolor{red}{HTML}{B83136}
\hypersetup{colorlinks=true,linkcolor=teal,urlcolor=teal,pdftitle={Agentic AI for Grid Operators: Study Guide}}
\setlength{\parindent}{0pt}\setlength{\parskip}{5pt}\setlength{\emergencystretch}{2em}
\raggedright
\renewcommand{\arraystretch}{1.2}
\lstdefinestyle{python}{language=Python,basicstyle=\ttfamily\footnotesize,keywordstyle=\color{teal}\bfseries,commentstyle=\color{slate},stringstyle=\color{amber},backgroundcolor=\color{pale},columns=fullflexible,keepspaces=true,showstringspaces=false,breaklines=true,tabsize=4,xleftmargin=3mm,xrightmargin=3mm}
\newcommand{\yesmark}{\textcolor{teal}{\checkmark}}\newcommand{\nomark}{---}\newcommand{\partmark}{\ensuremath{\triangle}}
\newcommand{\Checkpoint}[2]{\paragraph{Notebook #1}#2}
\newcommand{\Code}[1]{\lstinputlisting[style=python]{snippets/#1}}
\begin{document}
\hypersetup{pageanchor=false}
\begin{titlepage}
\vspace*{18mm}{\color{teal}\Large Three-hour teaching workshop}\par\bigskip
{\Huge\bfseries\color{navy} Agentic AI for\\Grid Operators}\par\bigskip
{\Large A worked teaching sequence}\par\medskip
Voltage support, restoration and cyber response\par\bigskip
This guide explains the ideas behind the native LaTeX slides. It connects physical decisions to numerical tools, workflow stages and the notebook experiments. Read the small example first, then the formal method, then the result.
\vfill
\textbf{How to use it}\par
Keep the completed-slide PDF beside this guide. The frame numbers below match that PDF. Use the lecture PDF for progressive reveals. Run the complete notebook cells in order; excerpts on slides are reading aids.
\par\medskip
All drawings in the teaching sequence use editable LaTeX/TikZ or recorded numerical plots. The introductory examples are labeled illustrative. No AI-generated imagery is used.
\end{titlepage}
\hypersetup{pageanchor=true}
\tableofcontents\clearpage
\section*{Before the terminology: one complete decision}
\addcontentsline{toc}{section}{Before the terminology: one complete decision}
Suppose an operator has a proposed control setting and wants to know whether it respects a current limit. We first use an intentionally simple model so that every step can be calculated by hand:
\[
 i=0.4+0.8u,\qquad i\leq0.8.
\]
Here $u$ is the toy control setting and $i$ is the model's current indicator. These numbers teach the workflow; they are not a feeder power-flow equation or a device setting.
\begin{center}\begin{tabular}{p{.24\linewidth}p{.62\linewidth}}\toprule
Responsibility & Observable calculation or result\\\midrule
Initial information & Proposed $u=0.75$; current limit $0.8$.\\
Simulation & $i=0.4+0.8(0.75)=1.0$.\\
Verification & $1.0>0.8$: reject this proposal.\\
Allowed repair & Reduce the control by $0.25$: new $u=0.50$.\\
New simulation & $i=0.4+0.8(0.50)=0.80$.\\
New verification & $0.80\leq0.80$: the toy current condition passes.\\
Operator record & Identify the exact checked proposal before acknowledgment.\\\bottomrule
\end{tabular}\end{center}
The graph notebook implements this example with ordinary Python functions inside LangGraph. The repair is a specified rule, not an LLM inference. This makes it possible to test the orchestration separately from the engineering method.

An agentic workflow becomes useful when the next permitted study depends on returned evidence or on an operator request that needs interpretation. The language model can propose a tool call or explain a result. The numerical method still calculates the electrical consequence. A check still decides whether the result meets its stated requirements.

\subsection*{Five stage names, with concrete jobs}
\textbf{Awareness} constructs the current problem: measurements, topology, limits and the requested study. \textbf{Planning} produces candidate actions using an appropriate method, such as MPC or a restoration MILP. \textbf{Simulation} computes the consequence of those actions in a stated model. \textbf{Verification} checks the numerical limits, data binding and required scope. The \textbf{LLM Optimizer} proposes or selects a permitted refinement, or retains the current choice. Any changed action needs new evidence. Human review follows these stages.

The method changes across cases. Continuous inverter settings suit MPC and continuous-action policies such as SAC. Binary restoration choices suit a mixed-integer formulation. Cyber response starts with measurement estimation and explicit trust assumptions before a constrained corrective action. Giving all these tools an ``agent'' label does not change their mathematics.

\subsection*{A diagram-reading key}
A box names an operation and its input/output. An arrow identifies what must happen before the next operation can use its result. A branch shows an explicit decision rule. A return arrow means repeat a study after a changed proposal. A limit on repeats prevents an open-ended loop. In the lecture, the same physical drawing stays visible while each calculation or branch appears.

\subsection*{Preparation and timing}
Use Python 3.12 and start Jupyter from the parent tutorial folder. Prepare separate environments from \texttt{requirements\_graph\_lab.txt} and \texttt{requirements\_linear.txt}. The executed HTML notebooks provide a reading route when a kernel is unavailable. Install the full OpenDSS requirements before class if you plan to enable that path. Prepare the existing Ollama service and model before enabling L11; the tutorial does not require an in-class model download.
\begin{center}\begin{tabular}{ll}\toprule Minutes & Topic\\\midrule
0--40 & Foundations and G0--G5; L0--L1\\
40--80 & Voltage support and L2--L5\\
80--90 & Break\\
90--115 & Restoration and L6--L7\\
115--142 & Cyber response and L8--L9\\
142--150 & Evaluation, optional L11 and latency\\
150--180 & Control-room examples, deployment, L12 and synthesis\\\bottomrule
\end{tabular}\end{center}
The actual archived five-stage responses in L10 are revisited during the case discussions. A saved response is distinct from a fresh numerical calculation and from a new live language-model call.
\clearpage
'''
out=[preamble];last=None; mapping=[]
illustrate={'F03','F05A','F12','F15','V04','V07','V10','R01','R04','R09','C03','C08','O02','D01','D02','D04','D04B','D06','D08','S01'}
for i,f in enumerate(allframes,1):
    if f['chapter']!=last:
        out.append(r'\clearpage\section{'+f['chapter']+'}\n');last=f['chapter']
    out.append(r'\subsection*{Frame '+str(i)+': '+f['title']+'}\n')
    if f['id'] in illustrate:
        out.append(r'\begin{center}\includegraphics[page='+str(i)+r',width=.96\linewidth]{handout.pdf}\end{center}'+'\n')
    note=macro(f['body'],'note')
    if not note:raise ValueError('Missing note '+f['id'])
    out.append(note+r'\par'+'\n')
    for name,heading in [('Question','Predict before revealing'),('Answer','Explanation')]:
        val=macro(f['body'],name)
        if val:out.append(r'\paragraph{'+heading+'}'+val+'\n')
    code=[]
    for m in re.finditer(r'\\lstinputlisting(?:\[([^\]]*)\])?\{([^}]+)\}',f['body']):
        code.append((m.group(0),m.group(2),m.group(1) or ''))
    for m in re.finditer(r'\\Code\{([^}]+)\}',f['body']):
        code.append((m.group(0),'snippets/'+m.group(1),''))
    for command,file,options in code:
        path=project/file
        lines=path.read_text(encoding='utf-8').splitlines()
        first=re.search(r'firstline=(\d+)',options);end=re.search(r'lastline=(\d+)',options)
        start=int(first.group(1)) if first else 1; stop=int(end.group(1)) if end else len(lines)
        excerpt='\n'.join(lines[start-1:stop])
        assert start>=1 and stop<=len(lines),(f['id'],file,start,stop)
        mapping.append({'frame':i,'id':f['id'],'title':f['title'],'file':file,'firstline':start,'lastline':stop,'sha256':hashlib.sha256(excerpt.encode()).hexdigest()})
        out.append(r'\par\noindent\begin{minipage}{\linewidth}\textbf{Notebook excerpt.} Run the complete cell in context.\par '+command+r'\end{minipage}\par'+'\n')
    source=macro(f['body'],'Source')
    out.append(r'\par\nopagebreak\begin{minipage}{\linewidth}{\footnotesize\color{slate}\textbf{Sources.} '+source+r'\par}\end{minipage}\par\medskip'+'\n')
out.append(r'\end{document}')
(project/'study_guide.tex').write_text(''.join(out),encoding='utf-8')
(project/'Slide_Notebook_Map.json').write_text(json.dumps(mapping,indent=2),encoding='utf-8')
(project/'frame_manifest.json').write_text(json.dumps([{k:v for k,v in f.items() if k!='body'}|{'frame':i} for i,f in enumerate(allframes,1)],indent=2),encoding='utf-8')
print('Guide frames',len(allframes),'code excerpts',len(mapping))
