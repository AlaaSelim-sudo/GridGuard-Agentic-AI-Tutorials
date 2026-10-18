"""Editable diagrams of documented power-study workflows and tool interfaces."""
from pathlib import Path
import json,os,runpy,shutil,subprocess,tempfile,sys
ROOT=Path(__file__).resolve().parent
BASE=runpy.run_path(str(ROOT/'build_revision_graphs.py'))
PRE,POST,WRAP,SVG=BASE['PRE'],BASE['POST'],BASE['WRAP'],BASE['SVG_FROM_PDF']
DIAGRAMS={
'va_powerwf':dict(title='One PowerWF grid-impact study',source_refs=['PA06','PA03'],
 caption='Teaching diagram of the author-maintained PowerWF Grid Impact Evaluation example. LangGraph stores the study state; the analysis steps request PowerWorld tools. Baseline and added-load studies run in the documented order.',
 assumptions='The internal tool-call/return routing and completion flags are simplified. No performance or deployed-utility claim is made. This is one documented PowerWF example, not a claim that every PowerAgent component uses LangGraph.',
 tex=r'''
\node[rp] (input) at (1.45,2.75) {};
\node[rp] (base) at (4.7,2.75) {};
\node[rp] (load) at (8.4,2.75) {};
\node[rp] (report) at (12.5,2.75) {};
\node[rl] at (1.45,3.43) {Inputs};
\node[rn] at (1.45,2.03) {case, bus, MW};
\node[rl] at (4.7,3.65) {Baseline\\flow + N$-$1};
\node[rl] at (8.4,3.65) {Added load\\flow + N$-$1};
\node[rl] at (12.5,3.43) {Report};
\node[rn] at (12.5,2.03) {compare results};
\draw[rf] (input.east) -- (base.west);
\draw[rf] (base.east) -- (load.west);
\draw[rf] (load.east) -- (report.west);
\node[rp] (tools) at (6.55,.9) {};
\node[rl] at (6.55,.37) {PowerWorld tools};
\draw[draw=rBlue,line width=1.1pt,{Latex[length=2mm]}-{Latex[length=2mm]}] (base.south) -- (4.7,.9) -- (tools.west);
\draw[draw=rBlue,line width=1.1pt,{Latex[length=2mm]}-{Latex[length=2mm]}] (load.south) -- (8.4,.9) -- (tools.east);
'''),
'va_dragent':dict(title='DrAgent plans calls to domain tools',source_refs=['D01'],
 caption='Teaching view of DrAgent: the plan selects tools for the question. Recorded-signal tools supply measurements; manual search supplies product information. The manual path is needed only for relevant questions.',
 assumptions='This is a high-level adaptation rather than the paper’s exact graph. The two branches do not imply parallel execution or that both are required for every answer. No numerical fault result is invented.',
 tex=r'''
\node[rp] (question) at (1.3,2.1) {};
\node[rl] at (1.3,2.82) {Question};
\node[rp] (plan) at (4.35,2.1) {};
\node[rl] at (4.35,2.82) {Plan};
\draw[rf] (question.east) -- (plan.west);
\node[rp] (fault) at (8.1,3.15) {};
\node[rl] at (8.1,3.85) {Signal tools};
\node[rn] at (8.1,2.62) {COMTRADE record};
\node[rp] (manual) at (8.1,.95) {};
\node[rl] at (8.1,1.55) {Manual search};
\node[rn] at (8.1,.35) {product documents};
\draw[rf] (plan.east) -- (5.6,2.1) |- (fault.west);
\draw[rf,dashed] (plan.east) -- (5.6,2.1) |- (manual.west);
\node[rp] (answer) at (12.35,2.1) {};
\node[rl] at (12.35,2.82) {Answer};
\node[rn] at (12.35,1.48) {with evidence};
\draw[rf] (fault.east) -- (10.55,3.15) |- (answer.west);
\draw[rf,dashed] (manual.east) -- (10.55,.95) |- (answer.west);
'''),
'va_simulation_feedback':dict(title='Simulation code with an error-feedback loop',source_refs=['E02'],
 caption='Simplified study-generation workflow from Jia, Cui and Hug. Execution errors return to retrieval and code repair. A run without a software error still needs a check against the requested study settings.',
 assumptions='The diagram does not claim that the paper includes an automatic proof that the code meets every engineering requirement. Grading and numerical task validity remain separate from error-free MATLAB execution.',
 tex=r'''
\node[rp] (task) at (1.05,2.7) {};
\node[rp] (lookup) at (3.8,2.7) {};
\node[rp] (code) at (6.7,2.7) {};
\node[rp] (run) at (9.55,2.7) {};
\node[rp] (output) at (12.65,2.7) {};
\node[rl] at (1.05,3.4) {Task};
\node[rl] at (3.8,3.55) {Find functions\\and settings};
\node[rl] at (6.7,3.4) {Write code};
\node[rn] at (6.7,2.05) {MATLAB};
\node[rl] at (9.55,3.4) {Run};
\node[rl] at (12.65,3.4) {Output};
\draw[rf] (task.east) -- (lookup.west);
\draw[rf] (lookup.east) -- (code.west);
\draw[rf] (code.east) -- (run.west);
\draw[rf] (run.east) -- (output.west);
\draw[rw] (run.south) -- (9.55,.68) -- (3.8,.68) -- (lookup.south);
\node[rn,text=rOrange] at (6.7,1.25) {Error: find settings\\and repair code};
'''),
'va_xgrid':dict(title='X-GridAgent coordinates specialized services',source_refs=['E01'],
 caption='Teaching view of X-GridAgent’s planner, coordinator and tool services. Eight MCP servers cover the paper’s listed functions. Pandapower supplies numerical studies; other services also read, edit and plot data.',
 assumptions='This is an architecture summary, not the exact runtime trace. Only numerical calls are shown passing to pandapower; the illustration does not claim that all eight services are solvers or that X-GridAgent uses LangGraph.',
 tex=r'''
\node[rp] (query) at (1.15,2.9) {};
\node[rp] (plan) at (4.2,2.9) {};
\node[rp] (coord) at (7.55,2.9) {};
\node[rp] (mcp) at (11.2,2.9) {};
\node[rl] at (1.15,3.6) {Request};
\node[rl] at (4.2,3.6) {Planner};
\node[rl] at (7.55,3.6) {Coordinator};
\node[rl] at (11.2,3.6) {MCP services};
\node[rn,anchor=east] at (10.75,2.12) {eight tool groups};
\draw[rf] (query.east) -- (plan.west);
\draw[rf] (plan.east) -- (coord.west);
\draw[rf] (coord.east) -- (mcp.west);
\node[rp] (solver) at (11.2,.7) {};
\node[rl] at (11.2,.12) {pandapower};
\draw[rf] (mcp.south) -- (solver.north);
\node[rn,anchor=east] at (10.8,1.4) {numerical calls};
\draw[rf] (solver.west) -- (7.55,.7) -- (coord.south);
\node[rn] at (6.25,.9) {results};
'''),
'va_mcp':dict(title='MCP is the connection to a callable tool',source_refs=['T08','T09','E01'],
 caption='Original teaching view of the MCP client/server connection. The application chooses a call, the client sends it to a server, and the server invokes the allowed capability. The returned result is evidence for the next step.',
 assumptions='This is a conceptual interface diagram, not a network-security guarantee or one application’s exact deployment. The application must still check permissions, arguments, case versions and the meaning of returned results.',
 tex=r'''
\node[rp] (agent) at (1.4,2.7) {};
\node[rp] (client) at (5.0,2.7) {};
\node[rp] (server) at (8.7,2.7) {};
\node[rp] (tool) at (12.4,2.7) {};
\node[rl] at (1.4,3.43) {Agent};
\node[rl] at (5.0,3.43) {MCP client};
\node[rl] at (8.7,3.43) {MCP server};
\node[rl] at (12.4,3.43) {Grid tool};
\node[rn,anchor=east] at (11.95,2.03) {e.g. power flow};
\draw[draw=rBlue,line width=1.15pt,{Latex[length=2mm]}-{Latex[length=2mm]}] (agent.east) -- (client.west);
\draw[draw=rBlue,line width=1.15pt,{Latex[length=2mm]}-{Latex[length=2mm]}] (client.east) -- (server.west);
\draw[draw=rBlue,line width=1.15pt,{Latex[length=2mm]}-{Latex[length=2mm]}] (server.east) -- (tool.west);
\node[rn] at (6.9,1.45) {Request: name + inputs $\rightarrow$};
\node[rn] at (6.9,.62) {$\leftarrow$ Response: status + results};
'''),
}

def build():
    sys.path.insert(0,str(ROOT/'_rigorous_build/pythonpackages'))
    from pypdf import PdfReader,PdfWriter
    temp_root=ROOT.parents[2]/'tmp'
    qa=temp_root/'operator_tutorial/domain-visuals';qa.mkdir(parents=True,exist_ok=True)
    manifest={}
    with tempfile.TemporaryDirectory(prefix='domain_visuals_',dir=temp_root) as temporary:
        work=Path(temporary).resolve();assert work.is_relative_to(temp_root.resolve())
        for font in ('arial.ttf','arialbd.ttf','consola.ttf'):shutil.copyfile(Path('C:/Windows/Fonts')/font,work/font)
        env=dict(os.environ);env['TECTONIC_CACHE_DIR']=str(temp_root/'tectonic_cache_017_fresh')
        for stem,spec in DIAGRAMS.items():
            tex=ROOT/(stem+'.tex');tex.write_text(PRE+spec['tex']+POST,encoding='utf-8')
            wrapper=work/(stem+'_wrapper.tex');wrapper.write_text(WRAP%tex.as_posix(),encoding='utf-8')
            result=subprocess.run([str(temp_root/'tectonic-0.17.0/tectonic.exe'),'--only-cached','--outdir',str(work),wrapper.name],cwd=work,env=env,capture_output=True,text=True)
            if result.returncode:raise RuntimeError(result.stdout+result.stderr)
            source=PdfReader(wrapper.with_suffix('.pdf'));page=next(p for p in source.pages if (p.extract_text() or '').strip())
            writer=PdfWriter();writer.add_page(page);pdf=ROOT/(stem+'.pdf')
            with pdf.open('wb') as handle:writer.write(handle)
            svg=ROOT/(stem+'.svg');SVG(pdf,svg);assert '<image' not in svg.read_text(encoding='utf-8')
            subprocess.run([r'C:/Users/f00863x/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe','-png','-singlefile','-scale-to-x','1280','-scale-to-y','-1',str(pdf),str(qa/stem)],check=True,capture_output=True)
            item={key:value for key,value in spec.items() if key!='tex'}
            item.update(id=stem,tex=stem+'.tex',pdf=stem+'.pdf',svg=stem+'.svg',file=stem+'.svg',credit='Original editable teaching diagram based on the cited primary source')
            manifest[stem]=item
    (ROOT/'domain_visual_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Built five domain workflow diagrams.')
if __name__=='__main__':build()
