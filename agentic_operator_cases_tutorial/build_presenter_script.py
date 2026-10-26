"""Build the aligned presenter script, run sheet and LaTeX PDF from authored cues."""
from pathlib import Path
import argparse,hashlib,html,json,os,shutil,subprocess
from latin_modern import css,copy_web_fonts

ROOT=Path(__file__).resolve().parent
SITE='https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/'
COLAB='https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb'
LABELS={'opening':'Agent concepts and Colab setup','voltage':'Voltage support','restoration':'Service restoration','cyber':'Cyber response','closing':'Agent workflow and operator review'}

def load(name):return json.loads((ROOT/name).read_text(encoding='utf-8-sig'))
def stamp(minutes):
    n=round(minutes*60);return f'{n//60:02}:{n%60:02}'
def duration(minutes):return f'{minutes:g} '+('minute' if minutes==1 else 'minutes')
def esc(t):
    for a,b in {'–':'-','—':'-','’':"'",'‘':"'",'“':'"','”':'"','→':' then ','≤':'<=','≥':'>='}.items():t=str(t).replace(a,b)
    return ''.join({'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_\allowbreak{}','/':r'/\allowbreak{}','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}'}.get(c,c) for c in t)

def prepare():
    slides=load('lesson_content.json');data=load('content/presenter_script.json');authored={c['title']:c for c in data['slides']}
    assert len(slides)==len(authored)==80
    assert set(authored)=={s['title'] for s in slides}
    assert sum(s['minutes'] for s in slides)==data['session_minutes']==90
    book=json.loads((ROOT.parent/'agentic_grid_workflow_tutorial/Classroom_Labs.ipynb').read_text(encoding='utf-8-sig'))
    code={c['id'] for c in book['cells'] if c['cell_type']=='code'};covered=set();elapsed=0;rows=[]
    for n,s in enumerate(slides,1):
        cue=authored[s['title']];c=cue['colab'];assert cue['say'] and cue['show'] and c['instruction']
        assert set(c['cell_ids'])<=code
        if c['mode']!='PREVIEW ONLY':covered.update(c['cell_ids'])
        rows.append(dict(cue,number=n,module=s['module'],minutes=s['minutes'],start=stamp(elapsed),end=stamp(elapsed+s['minutes']),slide_url=SITE+'operator-cases/#/'+str(n)))
        elapsed+=s['minutes']
    assert covered==code,('Uncovered code cells',code-covered)
    return slides,rows

def presenter_note(cue):
    c=cue['colab'];parts=['**Say**\n\n'+cue['say'],'**Show**\n\n'+cue['show'],'**Colab: '+c['mode']+'**\n\n'+c['instruction']]
    if c['cell_ids']:parts.append('Exact cells: '+', '.join(c['cell_ids'])+'. Run the whole cell, not only the slide excerpt.')
    if c.get('expected'):parts.append('**Expected result**\n\n'+c['expected'])
    if cue.get('question'):parts.extend(['**Ask**\n\n'+cue['question'],'**Answer**\n\n'+cue['answer']])
    return '\n\n'.join(parts)

ROLE_CASES=[
    ('Voltage: L10 MV archive',[
        ('Awareness / Python','Read the load, forecast, current allowance and MV model scope.'),
        ('Planning / numerical tools and Llama','Prepare MPC and saved-SAC candidates. Llama can request the declared initial studies or return review.'),
        ('Simulation / Python','Calculate the effects of each candidate using the declared three-phase linear model.'),
        ('Verification / Python','Check case matching, voltage, current and inverter limits. Only passing candidates receive eligible scores.'),
        ('Optimizer / Llama, with a Python guard','Request less reactive power, then more PV output. Recalculate and check every changed setting. Python selects by verified cost and performs a final recheck.')],
        'Selected final current use: about 50.75% of the allowance. This is the L10 MV archive, not the L2 experiment or P3 OpenDSS replay. The operator still reviews scope and missing checks.'),
    ('Restoration: L10 feeder catalog',[
        ('Awareness / Python','Keep the fault, available ties, critical loads, service goal and model scope in the shared case record.'),
        ('Planning / numerical tools and Llama','Prepare the stated restoration catalog options; request the initial evaluations or review.'),
        ('Simulation / Python','Calculate total and critical service and the current used by each option.'),
        ('Verification / Python','Reject the SHED_065 trial at about 111.01% of allowed current. Keep the passing SHED_075 trial eligible.'),
        ('Optimizer / Llama, with a Python guard','Request bounded catalog changes and rank passing IDs. Python corrects the wrong cost order and rechecks the chosen plan.')],
        'Selected final service: about 1,843.61 kW total and 474.04 kW critical, at 91.87% current use. This is not L6\'s six-node MILP. Physical switching order and operating permissions remain outside the result.'),
    ('Cyber: L10 four-bus DC archive',[
        ('Awareness / Python','Read the measurements, alarm context and declared availability of assumed trusted channels.'),
        ('Planning / numerical tools and Llama','Prepare the permitted response candidates. Llama can request the initial evaluations or review.'),
        ('Simulation / Python','Estimate state and calculate each candidate\'s branch flows and correction.'),
        ('Verification / Python','Test the trust condition, stated branch limits, bounds, evidence match and DC model scope.'),
        ('Optimizer / Llama, with a Python guard','Request bounded trials including TRUSTED_QP. Python ranks only passing candidates and rechecks the selected correction.')],
        'Selected correction: about 0.121694 p.u., with predicted flow 0.17000 p.u. against the 0.18000 p.u. limit. The trusted readings are assumed, not authenticated. Human review is still separate from equipment dispatch.'),
]

def write_outputs(slides,rows,make_pdf):
    groups=[(m,[r for r in rows if r['module']==m]) for m in LABELS]
    run_rows=[r for r in rows if r['colab']['cell_ids']]
    code_cells={}
    for row in run_rows:
        code_cells.update(zip(row['colab']['lessons'],row['colab']['cell_ids']))
    run_sheet={'notebook':'Classroom_Labs.ipynb','session_minutes':90,'all_code_cells':code_cells,
               'run_route':[{'slide':r['number'],**{k:r['colab'][k] for k in ['mode','lessons','cell_ids','instruction','expected']}} for r in run_rows]}
    (ROOT/'content/colab_run_route.json').write_text(json.dumps(run_sheet,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    intro='One notebook, 80 slides, 90 minutes. Use the spoken explanation in your own voice. The run cue says exactly when to open, run, edit, reset or inspect a cell. Run the complete cell identified by its L heading and stable ID.'
    boundary='Python calculates new numerical results. L3, L10 and L10B show separately labeled saved model records. One Llama model fills two roles in the saved five-role Python workflow. L12 is a simulated readback; equipment_dispatch stays False.'
    md=['# Presenter script: three operator cases','', '**Alaa Selim, MIT/Dartmouth; Mohamed Chehada, UT Austin.**','',intro,'',boundary,'','## Session route','']
    styles=css()+'''body{font-size:20px;line-height:1.5;max-width:1020px;margin:38px auto;padding:0 28px;color:#003b5c}h1{font-size:40px;line-height:1.12}h2{font-size:30px;line-height:1.2;margin-top:52px;border-top:2px solid #00a6b2;padding-top:22px}h3{font-size:25px;line-height:1.2}a{color:#00629b;overflow-wrap:anywhere}.slide{border-bottom:1px solid #cad6dc;padding:18px 0 30px;scroll-margin-top:20px}.meta{font-size:17px;color:#526470}.run{border-left:3px solid #00629b;padding-left:18px}.run p{margin:8px 0}li{margin:9px 0}code{font-size:.9em}details{margin:18px 0}summary{cursor:pointer;font-weight:bold}@media(max-width:600px){body{font-size:18px;padding:0 18px}h1{font-size:32px}}@media print{body{font-size:12pt;margin:0}.slide{break-before:page}.nav,.links{display:none}h2{break-before:page}}'''
    web=['<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Presenter script: three operator cases</title><style>'+styles+'</style><h1>Presenter script: three operator cases</h1><p><strong>Alaa Selim, MIT/Dartmouth; Mohamed Chehada, UT Austin.</strong></p><p>'+html.escape(intro)+'</p><p>'+html.escape(boundary)+'</p><p class="links"><a href="Presenter_Script.pdf">Printable script</a> · <a href="'+COLAB+'">Open Classroom Labs</a> · <a href="'+SITE+'operator-cases/#/presenter/1">Slide presenter view</a></p><h2>Session route</h2><ul class="nav">']
    for m,g in groups:
        text=f'{LABELS[m]}: slides {g[0]["number"]}-{g[-1]["number"]}, {g[0]["start"]}-{g[-1]["end"]}'
        md.append('- '+text);web.append('<li><a href="#module-'+m+'">'+html.escape(text)+'</a></li>')
    web.append('</ul><h2>Colab run sheet</h2><p>Follow this order. Preview slides do not ask learners to run ahead.</p>');md+=['','## Colab run sheet','']
    for r in run_rows:
        c=r['colab'];label=f'Slide {r["number"]}: '+', '.join(c['lessons'])+' / '+c['mode']
        md+=['### '+label,'',c['instruction'],'','Exact cells: '+', '.join(c['cell_ids'])+'.','', 'Expected: '+c['expected'],'']
        web.append('<p><strong><a href="#slide-'+str(r['number'])+'">'+html.escape(label)+'</a></strong><br>'+html.escape(c['instruction'])+'<br><span class="meta">Cells: '+html.escape(', '.join(c['cell_ids']))+'</span></p>')
    for m,g in groups:
        md+=['','<a id="module-'+m+'"></a>','## '+LABELS[m],''];web.append('<h2 id="module-'+m+'">'+html.escape(LABELS[m])+'</h2>')
        for r in g:
            n=r['number'];c=r['colab'];meta=f'{r["start"]}-{r["end"]} / '+duration(r['minutes'])
            md += [f'### Slide {n}. {r["title"]}','',meta,'','**Say:** '+r['say'],'','**Show:** '+r['show'],'','**Colab: '+c['mode']+'.** '+c['instruction'],'']
            web.append('<section class="slide" id="slide-'+str(n)+'"><h3>Slide '+str(n)+'. '+html.escape(r['title'])+'</h3><p class="meta">'+meta+'</p><p><strong>Say</strong><br>'+html.escape(r['say'])+'</p><p><strong>Show</strong><br>'+html.escape(r['show'])+'</p><div class="run"><p><strong>Colab: '+html.escape(c['mode'])+'</strong><br>'+html.escape(c['instruction'])+'</p>')
            if c['cell_ids']:
                ids=', '.join(c['cell_ids']);md+=['Exact cells: '+ids+'. Run the whole cell.',''];web.append('<p class="meta">Exact cells: '+html.escape(ids)+'. Run the whole cell.</p>')
            if c.get('expected'):md+=['**Expected:** '+c['expected'],''];web.append('<p><strong>Expected</strong><br>'+html.escape(c['expected'])+'</p>')
            web.append('</div>')
            if r.get('question'):
                md+=['**Ask:** '+r['question'],'','**Answer:** '+r['answer'],''];web.append('<p><strong>Ask</strong><br>'+html.escape(r['question'])+'</p><details><summary>Expected answer</summary><p>'+html.escape(r['answer'])+'</p></details>')
            md+=['[Open slide]('+r['slide_url']+')',''];web.append('<p class="links"><a href="'+r['slide_url']+'">Open slide</a></p></section>')
    md+=['## Agent roles in the three recorded cases',''];web.append('<h2>Agent roles in the three recorded cases</h2>')
    for title,roles,result in ROLE_CASES:
        md+=['### '+title,''];web.append('<h3>'+html.escape(title)+'</h3><ol>')
        for role,job in roles:md+=['- **'+role+':** '+job];web.append('<li><strong>'+html.escape(role)+':</strong> '+html.escape(job)+'</li>')
        md+=['',result,''];web.append('</ol><p>'+html.escape(result)+'</p>')
    registry=load('research/source_map.json');keys=list(dict.fromkeys(k for s in slides for k in s['refs']));citations=[]
    md+=['## Full sources',''];web.append('<h2>Full sources</h2>')
    for key in keys:
        s=registry[key];a=s.get('authors',s.get('author',''));a=', '.join(a) if isinstance(a,list) else a
        citation=f'{a}. {s["title"]}. {s.get("publisher","")}. {s.get("date","")}.';citations.append((key,citation,s['url']))
        md+=['- ['+key+'] '+citation+' '+s['url']];web.append('<p><strong>['+html.escape(key)+']</strong> '+html.escape(citation)+'<br><a href="'+html.escape(s['url'],quote=True)+'">'+html.escape(s['url'])+'</a></p>')
    web.append('</html>');(ROOT/'Presenter_Script.md').write_text('\n'.join(md)+'\n',encoding='utf-8');(ROOT/'Presenter_Script.html').write_text('\n'.join(web),encoding='utf-8')
    write_tex(rows,groups,run_rows,intro,boundary,citations)
    if make_pdf:
        compiler=os.environ.get('TECTONIC') or shutil.which('tectonic')
        if not compiler:raise ValueError('Set TECTONIC or install Tectonic to build the script PDF.')
        subprocess.run([compiler,'-X','compile','--keep-logs','--keep-intermediates','presenter_script.tex'],cwd=ROOT/'latex',check=True)
        log=(ROOT/'latex/presenter_script.log').read_text(errors='replace')
        if 'Overfull' in log or 'Missing character' in log:raise ValueError('Fix the script PDF layout diagnostics.')
        shutil.copy2(ROOT/'latex/presenter_script.pdf',ROOT/'Presenter_Script.pdf')
    copy_web_fonts(ROOT/'slidev/public/fonts')
    for name in ['Presenter_Script.md','Presenter_Script.html']+(['Presenter_Script.pdf'] if make_pdf else []):shutil.copy2(ROOT/name,ROOT/'slidev/public'/name)
    manifest={'slides':80,'minutes':90,'font_family':'Latin Modern Roman; Latin Modern Mono for code','lesson_sha256':hashlib.sha256((ROOT/'lesson_content.json').read_bytes()).hexdigest(),'script_cues_sha256':hashlib.sha256((ROOT/'content/presenter_script.json').read_bytes()).hexdigest(),'entries':[{k:r[k] for k in ['number','title','minutes','start','end']}|{'colab_mode':r['colab']['mode'],'cell_ids':r['colab']['cell_ids']} for r in rows]}
    p=ROOT/'research/presenter/presenter_manifest.json';p.write_text(json.dumps(manifest,indent=2)+'\n');shutil.copy2(p,ROOT/'slidev/public/research/presenter/presenter_manifest.json')
    print(json.dumps({'script_slides':80,'minutes':90,'covered_code_cells':15,'pdf':make_pdf}))

def write_tex(rows,groups,run_rows,intro,boundary,citations):
    out=[r'''\documentclass[12pt,letterpaper]{article}
\usepackage[T1]{fontenc}
\usepackage{lmodern,geometry,xcolor,hyperref,xurl,fancyhdr}
\geometry{margin=.72in,headheight=15pt}
\definecolor{IEEEBlue}{HTML}{00629B}
\definecolor{Slate}{HTML}{526470}
\hypersetup{colorlinks=true,urlcolor=IEEEBlue,linkcolor=IEEEBlue,pdftitle={Presenter script: Three Operator Cases},pdfauthor={Alaa Selim and Mohamed Chehada}}
\urlstyle{tt}
\setlength{\parindent}{0pt}\setlength{\parskip}{7pt}
\linespread{1.08}
\setlength{\emergencystretch}{2em}
\pagestyle{fancy}\fancyhf{}
\fancyhead[L]{\small Three Operator Cases / Presenter Script}
\fancyfoot[L]{\small 90-minute workshop}\fancyfoot[R]{\small\thepage}
\renewcommand{\headrulewidth}{.4pt}
\begin{document}
{\Huge\bfseries\color{IEEEBlue} Presenter script\par}
{\LARGE Three operator cases\par}\bigskip
{\large Alaa Selim, MIT/Dartmouth\par Mohamed Chehada, UT Austin\par}\bigskip
''',esc(intro)+r'\par\medskip'+'\n',esc(boundary)+r'\par\medskip'+'\n',r'\section*{90-minute session route}'+'\n']
    for m,g in groups:out.append(esc(f'{LABELS[m]}: slides {g[0]["number"]}-{g[-1]["number"]}, {g[0]["start"]}-{g[-1]["end"]}.')+r'\par'+'\n')
    out.append(r'\medskip\href{'+COLAB+r'}{Open the one Classroom Labs notebook}\par'+'\n')
    for title,subset in [('Setup and voltage',[r for r in run_rows if r['number']<=33]),('Restoration and cyber',[r for r in run_rows if 33<r['number']<=64]),('Saved agent records and operator readback',[r for r in run_rows if r['number']>64])]:
        out.append(r'\clearpage\section*{Colab run sheet: '+esc(title)+'}\n{\\small\n')
        for r in subset:
            c=r['colab'];out.append(r'\textbf{Slide '+str(r['number'])+': '+esc(', '.join(c['lessons']))+' / '+esc(c['mode'])+r'}\par '+esc(c['instruction'])+r'\par {\footnotesize Cells: '+esc(', '.join(c['cell_ids']))+r'.}\par\medskip'+'\n')
        out.append('}\n')
    for r in rows:
        c=r['colab'];out.extend([r'\clearpage\pdfbookmark[1]{Slide '+str(r['number'])+'. '+esc(r['title'])+'}{slide-'+str(r['number'])+'}\n',r'{\Large\bfseries\color{IEEEBlue} Slide '+str(r['number'])+'. '+esc(r['title'])+r'\par}\medskip'+'\n',r'{\small\color{Slate} '+esc(r['start']+'-'+r['end']+' / '+duration(r['minutes']))+r'\par}\medskip'+'\n'])
        for label,text in [('Say',r['say']),('Show',r['show']),('Colab: '+c['mode'],c['instruction'])]:out.append(r'\textbf{'+esc(label)+r'}\par '+esc(text)+r'\par\medskip'+'\n')
        if c['cell_ids']:out.append(r'{\small\textbf{Exact cells:} \texttt{'+esc(', '.join(c['cell_ids']))+r'}. Run the whole cell.\par}\medskip'+'\n')
        if c.get('expected'):out.append(r'\textbf{Expected result}\par '+esc(c['expected'])+r'\par\medskip'+'\n')
        if r.get('question'):out.append(r'\textbf{Ask}\par '+esc(r['question'])+r'\par\textbf{Expected answer}\par '+esc(r['answer'])+r'\par\medskip'+'\n')
        out.append(r'\vfill\href{'+r['slide_url']+'}{Open slide '+str(r['number'])+r'}\par'+'\n')
    for title,roles,result in ROLE_CASES:
        out.append(r'\clearpage\section*{Agent role map: '+esc(title)+'}\n')
        for role,job in roles:out.append(r'\textbf{'+esc(role)+r'}\par '+esc(job)+r'\par\medskip'+'\n')
        out.append(esc(result)+r'\par'+'\n')
    out.append(r'\clearpage\section*{Full sources}'+'\n'+r'{\small'+'\n')
    for key,citation,url in citations:out.append(r'\textbf{['+esc(key)+']} '+esc(citation)+r'\par\url{'+url.replace('%',r'\%')+r'}\par\medskip'+'\n')
    out.append('}\n\\end{document}\n');(ROOT/'latex/presenter_script.tex').write_text(''.join(out),encoding='utf-8')

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--pdf',action='store_true');args=parser.parse_args();slides,rows=prepare();write_outputs(slides,rows,args.pdf)
if __name__=='__main__':main()
