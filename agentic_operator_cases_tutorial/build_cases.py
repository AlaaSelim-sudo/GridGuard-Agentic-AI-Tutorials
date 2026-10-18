"""Build the separate three-case operator tutorial in LaTeX and Slidev."""
from pathlib import Path
from types import SimpleNamespace
import ast,hashlib,html,json,re,shutil,textwrap
import renderer as r

ROOT=Path(__file__).resolve().parent
WORKSHOP=Path(r'C:/Users/f00863x/OPRO/output/agentic_grid_workflow_tutorial')
MODULES=['opening','voltage','restoration','cyber','closing']

def load(path):return json.loads(path.read_text(encoding='utf-8-sig'))
def dump(path,value):path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def resolve_local(value):
    p=Path(value)
    if not p.is_absolute():p=ROOT/p
    if p.is_relative_to(WORKSHOP):
        relative=p.relative_to(WORKSHOP)
        packaged=ROOT/'research/evidence'/relative
        return (packaged if packaged.is_file() else p),relative
    if p.is_relative_to(ROOT/'research/evidence'):
        return p,p.relative_to(ROOT/'research/evidence')
    if p.is_relative_to(ROOT/'images'):
        return p,Path('replots')/p.name
    return p,Path('additional')/p.name
def safe_text(value):
    replacements={'λ':'lambda','ρ':'rho','δ':'delta','σ':'sigma','χ':'chi','θ':'theta','ε':'epsilon','α':'alpha',
                  'β':'beta','∥':'||','≈':'about ','∈':' in ','∞':'infinity','∑':'sum ','₂':'2','₁':'1',
                  '₀':'0','²':'^2','³':'^3','⁻':'-','⁺':'+','𝑢':'u','ϵ':'epsilon','−':'-'}
    text=str(value or '')
    for a,b in replacements.items():text=text.replace(a,b)
    return text

def readable_tex_escape(original,value):
    # Long record hashes, paths and schema tokens must wrap in the reading guide.
    parts=re.split(r'(\S{45,})',safe_text(value))
    return ''.join((r'\allowbreak{}'.join(original(part[i:i+16]) for i in range(0,len(part),16))
                    if len(part)>=45 and not re.search(r'\s',part) else original(part)) for part in parts)

def normalize_registry():
    sources={}
    for file in sorted((ROOT/'content').glob('*_sources.json')):sources.update(load(file))
    (ROOT/'research/evidence').mkdir(parents=True,exist_ok=True)
    evidence_manifest=[]
    for key,source in sources.items():
        source.setdefault('date',str(source.get('year','2026')))
        if not source.get('authors') and source.get('author'):source['authors']=source['author']
        paths=source.get('local_evidence_paths') or source.get('local_paths') or source.get('evidence_paths') or []
        if isinstance(paths,str):paths=[paths]
        paths=list(paths)
        if source.get('local_path'):paths.append(source['local_path'])
        paths+=source.get('related_local_paths',[])
        if source.get('url') and re.match(r'^[A-Za-z]:[/\\]',source['url']):
            paths.append(source['url']);source['url']=None
        elif (source.get('url') or '').startswith('research/evidence/'):
            paths.append(source['url']);source['url']=None
        paths=list(dict.fromkeys(paths))
        local=[]
        for original in paths:
            src,relative=resolve_local(original)
            if not src.is_file():raise FileNotFoundError((key,str(src)))
            dst=ROOT/'research/evidence'/relative;dst.parent.mkdir(parents=True,exist_ok=True)
            if src.resolve()!=dst.resolve():shutil.copy2(src,dst)
            local.append('research/evidence/'+relative.as_posix())
            evidence_manifest.append({'file':dst.relative_to(ROOT).as_posix(),'original':str(src),
                'sha256':hashlib.sha256(src.read_bytes()).hexdigest()})
            if src.suffix=='.ipynb' and src.with_suffix('.html').is_file():
                rendered=src.with_suffix('.html');target=dst.with_suffix('.html')
                if rendered.resolve()!=target.resolve():shutil.copy2(rendered,target)
                local.append(target.relative_to(ROOT).as_posix())
                evidence_manifest.append({'file':target.relative_to(ROOT).as_posix(),'original':str(rendered),
                    'sha256':hashlib.sha256(rendered.read_bytes()).hexdigest()})
        source['packaged_evidence']=local
        if not source.get('url'):
            source['authors']='GridGuard teaching materials'
            source['url']='research/source_'+key+'.html'
        if local:
            intro=html.escape(r.full_citation(source))
            links=''.join('<li><a href="'+html.escape(p.removeprefix('research/'))+'">'+html.escape(p.removeprefix('research/evidence/'))+'</a></li>' for p in local)
            content='<!doctype html><meta charset="utf-8"><title>'+html.escape(source['title'])+'</title><style>body{font:18px/1.5 Arial;max-width:1000px;margin:40px auto;padding:0 25px;color:#003b5c}a{color:#00629b;overflow-wrap:anywhere}</style><h1>'+html.escape(source['title'])+'</h1><p>'+intro+'</p><p>'+html.escape(str(source.get('scope',source.get('evidence_limit',''))))+'</p><ul>'+links+'</ul>'
            (ROOT/'research'/('source_'+key+'.html')).write_text(content,encoding='utf-8')
    # Exact shared laboratory evidence accompanies the common workflow references.
    shared=['Classroom_Labs.ipynb','Classroom_Labs.html','Workshop_Instructor_Guide.md',
            'src/classroom_labs.py','src/standard_formulations.py','results/standard_formulations.json']
    for name in shared:
        dst=ROOT/'research/evidence'/name;src=dst if dst.is_file() else WORKSHOP/name
        dst.parent.mkdir(parents=True,exist_ok=True)
        if src.resolve()!=dst.resolve():shutil.copy2(src,dst)
        evidence_manifest.append({'file':dst.relative_to(ROOT).as_posix(),'original':str(src),
            'sha256':hashlib.sha256(src.read_bytes()).hexdigest()})
    text='# Existing GridGuard workshop evidence\n\nRecorded teaching examples, inspected 18 October 2026. No new aggregate agent benchmark is claimed.\n\n'
    text+='\n'.join('- '+v for v in shared)
    text+='\n\nVoltage uses a synthetic SMART-DS feeder. Restoration uses a separate six-node active-power transport model. Cyber uses a separate four-bus DC/WLS fixture.\n'
    (ROOT/'research/workshop_evidence.md').write_text(text,encoding='utf-8')
    # Keep image references in preserved source notebooks usable offline.
    for doc in (ROOT/'research/evidence').glob('*.html'):
        for name in re.findall(r'<img[^>]+src=["\']([^"\']+)',doc.read_text(encoding='utf-8',errors='replace')):
            if name.startswith(('http:','https:','data:','/')):continue
            src=WORKSHOP/name;dst=doc.parent/name
            if src.is_file() and not dst.is_file():
                dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
                evidence_manifest.append({'file':dst.relative_to(ROOT).as_posix(),'original':str(src),'sha256':hashlib.sha256(src.read_bytes()).hexdigest()})
    dump(ROOT/'research/evidence_manifest.json',list({x['file']:x for x in evidence_manifest}.values()))
    dump(ROOT/'research/source_map.json',sources)
    return sources

def prepare_slides():
    slides=[];images={};code_records=[]
    for module in MODULES:
        items=load(ROOT/'content'/(module+'.json'))
        if isinstance(items,dict):items=items.get('slides',items.get('items'))
        for item in items:
            s=dict(item);s['module']=module
            if s.get('code_lines'):
                spec=s['code_source'];src,relative=resolve_local(spec['path'])
                source_lines=src.read_text(encoding='utf-8').splitlines()
                ranges=spec.get('ranges') or [[spec['start'],spec['end']]]
                original=[line for a,b in ranges for line in source_lines[a-1:b]]
                display=s['code_lines']
                if s.get('code_format')=='same_statements':
                    a=ast.dump(ast.parse(textwrap.dedent('\n'.join(original))),include_attributes=False)
                    b=ast.dump(ast.parse('\n'.join(display)),include_attributes=False)
                    assert a==b,('Code statement/source mismatch',s['title'])
                else:
                    assert display==original,('Code/source mismatch',s['title'])
                    display=textwrap.dedent('\n'.join(original)).splitlines()
                dest=ROOT/'research/code'/(module+'_'+src.stem+'_L'+str(spec['start'])+'-'+str(spec['end'])+'.py')
                dest.parent.mkdir(parents=True,exist_ok=True)
                dest.write_text('\n'.join(display)+'\n',encoding='utf-8')
                s['code_file']=dest.relative_to(ROOT).as_posix()
                s['code_gobble']=0
                s['code_lines']=display
                code_records.append({'module':module,'source':'research/evidence/'+relative.as_posix(),
                    'start':spec['start'],'end':spec['end'],'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
                    'source_ranges':ranges,'statement_equivalence_verified':s.get('code_format')=='same_statements',
                    'excerpt':s['code_file'],'excerpt_sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),
                    'display_change':'Source statements preserved; leading indentation removed and long calls wrapped for readability.'})
            if s.get('diagram_spec') and isinstance(s['diagram_spec'],dict) and not s.get('diagram'):
                s['diagram']=s['diagram_spec'].get('id')
            if len(s.get('points',[]))==3 and (s.get('diagram') or s.get('image_source_path')):
                s['points']=[s['points'][0],s['points'][1]+' '+s['points'][2]]
            if s.get('image_source_path'):
                src,relative_source=resolve_local(s['image_source_path']);assert src.is_file(),str(src)
                evidence=ROOT/'research/evidence'/relative_source
                evidence.parent.mkdir(parents=True,exist_ok=True)
                if src.resolve()!=evidence.resolve():shutil.copy2(src,evidence)
                name=src.name;target=ROOT/'images'/name
                if s.get('image_crop'):
                    from PIL import Image
                    x,y,w,h=s['image_crop']
                    name=module+'_'+src.stem+'_detail.png';target=ROOT/'images'/name
                    Image.open(src).crop((x,y,x+w,y+h)).save(target)
                    shutil.copy2(src,ROOT/'images'/src.name)
                elif src.resolve()!=target.resolve():shutil.copy2(src,target)
                if src.with_suffix('.pdf').is_file() and not s.get('image_crop'):
                    pdf=src.with_suffix('.pdf');dst=ROOT/'images'/pdf.name
                    if pdf.resolve()!=dst.resolve():shutil.copy2(pdf,dst)
                screenshot=bool(s.get('walkthrough_step'))
                images[name]={'file':name,'credit':'GridGuard project: browser capture of archived executed notebook/dashboard' if screenshot else ('Original teaching replot using existing GridGuard records' if s.get('image_transformation') else 'Existing GridGuard workshop numerical figure'),
                    'original_file':src.name if s.get('image_crop') else None,
                    'source_page_url':'research/source_'+s['refs'][0]+'.html',
                    'direct_image_url':'research/evidence/'+relative_source.as_posix(),
                    'asset_type':'Actual local GridGuard screenshot' if screenshot else ('Recorded numerical teaching figure' if 'feeder' not in name else 'Synthetic feeder visualization'),
                    'transformation':s.get('image_transformation') or ('Existing HTML rendered in a browser; selected element crop; text enlarged without changing recorded values. Full provenance: research/screenshots/capture_manifest.json.' if screenshot else ('Selected original panel without changing plotted values.' if s.get('image_crop') else 'Unchanged original plot.')),
                    'evidence_limit':s.get('caption',''),'sha256':hashlib.sha256(target.read_bytes()).hexdigest()}
                s['image']=name
                if s['kind']!='exercise':s['kind']='figure'
            if s.get('diagram'):
                assert (ROOT/'diagrams'/(s['diagram']+'.tex')).is_file(),s['diagram']
                assert (ROOT/'diagrams'/(s['diagram']+'.svg')).is_file(),s['diagram']+' needs SVG'
            s.setdefault('caption','');s.setdefault('note','');s.setdefault('takeaway','')
            s.setdefault('visual_height_cm',3.8 if s.get('diagram') else 3.65)
            s.setdefault('visual_height_px',330 if s.get('diagram') else 330)
            s.setdefault('eyebrow','')
            if module in ['voltage','restoration','cyber'] and s.get('module_slide')==1:
                s['eyebrow']={'voltage':'Case 1 / Voltage support','restoration':'Case 2 / Service restoration','cyber':'Case 3 / Cyber response'}[module]
                s['visual_height_cm']=3.45;s['visual_height_px']=305
            for field in ['points','refs']:s.setdefault(field,[])
            # Plain text never contains hidden answers or motion/notice prompts.
            assert not s.get('notice') and 'table' not in s and 'answer' not in s
            slides.append(s)
    dump(ROOT/'images/image_manifest.json',{'images':list(images.values())})
    dump(ROOT/'research/code_manifest.json',code_records)
    slides=r.normalized_slides(SimpleNamespace(SLIDES=slides))
    assert len(slides)==59,len(slides)
    assert sum(s['minutes'] for s in slides)==120
    assert sum(s['kind']=='exercise' for s in slides)==3
    return slides

def teaching_guide(slides,sources):
    sections=[('How to teach this follow-on session',[
        ('Format','59 static slides / 120 minutes. Opening 6 minutes; each case 36 minutes including a four-minute exercise; closing 6 minutes.'),
        ('Prerequisite','Use the restored foundations tutorial first. The follow-on starts with concrete operating questions and assumes the terms agent, tool, solver and workflow are already familiar.'),
        ('Evidence modes','Recorded numerical studies, archived genuine LLM replies, and illustrative workflow/version diagrams are labeled separately. No live utility control, new field evaluation, new training or live model call is performed by the deck.'),
        ('Preparation','Present the built Slidev version or the PDF. No model account or installation is needed. Exercises use the supplied slide evidence. Full notebook/source records are available in the source package.'),
        ('Facilitation','For each four-minute exercise: one minute to read, two minutes in pairs, one minute to prepare a decision and one supporting check. The next slide supplies the debrief.')],[])]
    elapsed=0
    for i,s in enumerate(slides,1):
        end=elapsed+s['minutes']
        fields=[('Timing',r.reading.stamp(elapsed)+'–'+r.reading.stamp(end)+' ('+str(s['minutes'])+' minutes)'),
                ('Slide content','\n'.join(s['points'])),('Teaching notes',s['note'])]
        if s.get('caption'):fields.append(('Figure scope',s['caption']))
        if s.get('diagram'):fields.append(('Editable figure','diagrams/'+s['diagram']+'.tex'))
        if s.get('image'):fields.append(('Figure asset','images/'+s['image']))
        if s.get('code_file'):
            fields.append(('Exact source excerpt',s['code_caption']+'\n'+'\n'.join(s['code_lines'])))
            fields.append(('Source alignment','research/code_manifest.json records source hashes, original line ranges and syntax-tree equivalence checks. research/code/ contains the readable display fragment. The complete original file is preserved in research/evidence/src/.'))
        links=[('['+key+'] '+r.full_citation(sources[key]),sources[key]['url']) for key in s['refs']]
        sections.append((str(i)+'. '+s['title'],fields,links));elapsed=end
    used=list(dict.fromkeys(key for s in slides for key in s['refs']))
    sections+=r.reading.reading_sections(used,sources,slides,r.reading.load_json(ROOT/'images/image_manifest.json'))
    md,web,tex=r.reading.reading_guides(sections)
    for a,b in [('Full Reading Guide','Teaching and Source Guide'),
                ('Agentic AI for Utility Operators — introductory lecture.','Agentic AI: Three Operator Cases — follow-on tutorial.'),
                ('Agentic AI for Utility Operators','Agentic AI: Three Operator Cases')]:
        md=md.replace(a,b);web=web.replace(a,b);tex=tex.replace(a,b)
    # Notes may span pages. Keep headings with their first paragraph without boxing the whole lesson.
    tex=tex.replace(r'\setbox\readingEntry=\vbox\bgroup\hsize=\linewidth\subsection*{',r'\subsection*{')
    tex=tex.replace(r'\egroup\par\noindent\box\readingEntry\par\medskip',r'\par\medskip')
    (ROOT/'Teaching_Guide.md').write_text(md,encoding='utf-8')
    (ROOT/'Full_Reading_Guide.html').write_text(web,encoding='utf-8')
    (ROOT/'latex/teaching_guide.tex').write_text(tex,encoding='utf-8')

def alignment_guide(slides,sources):
    out=['<!doctype html><meta charset="utf-8"><title>GridGuard: code and recorded results</title><style>body{font:20px/1.55 Arial;color:#003b5c;max-width:1080px;margin:40px auto;padding:0 28px}h1,h2{color:#00629b}h2{border-top:3px solid #00a6b2;padding-top:28px;margin-top:50px}pre{font:19px/1.5 Consolas,monospace;white-space:pre-wrap;overflow-wrap:anywhere;background:#f2f7fa;padding:22px}a{color:#00629b;overflow-wrap:anywhere}li{margin:12px 0}.source{font-size:16px;color:#526470}</style><h1>GridGuard: code and recorded results</h1><p>These are the actual tutorial supervisors and preserved records used in the presentation. Each model reply selects a permitted workflow step; Python numerical tools calculate and check the action.</p><p>The archived workshop uses custom Python supervisors. The separate current GridGuard application uses LangGraph. These records establish the behavior of the dated tutorial runs.</p>']
    for module,key,label in [('voltage','TRACE_VOLT','Voltage / P3 OpenDSS / 27 September 2026'),('restoration','TRACE_REST','Restoration / six-node graph / 21 September 2026'),('cyber','TRACE_CYBER','Cyber / four-bus DC / 21 September 2026')]:
        items=[(i,s) for i,s in enumerate(slides,1) if s['module']==module and s.get('walkthrough_step')]
        out.append('<h2>'+html.escape(label)+'</h2><ol>')
        for i,s in items:
            out.append('<li><b>Slide '+str(i)+': '+html.escape(s['title'].split('. ',1)[-1])+'</b><br>'+html.escape(' '.join(s['points']))+'</li>')
        out.append('</ol>')
        s=next(s for _,s in items if s.get('code_file'));spec=s['code_source']
        _,relative=resolve_local(spec['path']);full='research/evidence/'+relative.as_posix()
        out.append('<p>'+html.escape(s['code_caption'])+'</p><pre>'+html.escape('\n'.join(s['code_lines']))+'</pre><p><a href="'+html.escape(full)+'">Read the complete original Python file</a> · <a href="research/source_'+key+'.html">Open the executed notebook, raw call journal and result record</a></p>')
        out.append('<p class="source">'+html.escape(r.full_citation(sources[key]))+'</p>')
    out.append('<h2>Check the alignment</h2><p><a href="research/code_manifest.json">Code manifest</a> records original source hashes, line ranges and verified equivalent Python statements. Display line breaks and indentation improve readability. The surrounding function is in the complete source.</p><p><a href="research/screenshots/capture_manifest.json">Screenshot manifest</a> records original HTML hashes, selected regions and unchanged output text. Screenshots show real archived notebook or dashboard views; they do not imply field deployment or a new live run.</p><p>The original model prompts and raw replies are linked in each source index. Opening a saved record makes no model call. The archived operator acknowledgment remains pending in all three walkthroughs.</p>')
    (ROOT/'Code_and_Record_Guide.html').write_text('\n'.join(out),encoding='utf-8')

def main():
    for folder in ['research','images','latex/images','latex/diagrams','slidev/public/images','slidev/public/diagrams','slidev/public/branding']:
        (ROOT/folder).mkdir(parents=True,exist_ok=True)
    r.reading.REVIEWED='18 October 2026'
    original_escape=r.reading.esc
    r.reading.esc=lambda value:readable_tex_escape(original_escape,value)
    sources=normalize_registry()
    slides=prepare_slides()
    for i,s in enumerate(slides,1):
        assert all(key in sources for key in s['refs']),(i,s['refs'])
        if s.get('main_ref'):assert s['main_ref'] in s['refs']
    # The same renderer and theme used by the preceding edition.
    frames=''.join(r.render_frame(s,sources) for s in slides).replace('{reading_guide.pdf}','{teaching_guide.pdf}')
    front='''---
theme: default
title: Agentic AI — Three Operator Cases
info: Voltage support, service restoration and cyber response, with operator workflows and three exercises
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

'''
    web=front+'\n---\ntransition: none\n---\n\n'.join(r.render_slide(s,i,len(slides),sources) for i,s in enumerate(slides,1))
    web=web.replace('Separate reading-guide PDF','Teaching and source guide PDF')
    for token in ['What to notice','v-click','v-motion',r'\pause',r'\uncover<',r'\transfade','<table',r'\begin{tabular}']:
        assert token not in frames+web,token
    (ROOT/'latex/frames.tex').write_text(frames,encoding='utf-8')
    (ROOT/'slidev/slides.md').write_text(web,encoding='utf-8')
    dump(ROOT/'lesson_content.json',slides)
    notes='# Instructor Guide: Three Operator Cases\n\n59 static slides / 120 minutes. Each case includes a five-step recorded walkthrough, a four-minute exercise and its debrief. No tables, transitions, click reveals or What to notice labels. All numerical evidence is from the labeled local teaching records.\n\n'
    elapsed=0
    for i,s in enumerate(slides,1):
        end=elapsed+s['minutes']
        notes+='## '+str(i)+'. '+s['title']+'\n\n'+r.reading.stamp(elapsed)+'–'+r.reading.stamp(end)+' / '+str(s['minutes'])+' minutes.\n\n'+s['note']+'\n\nFull sources:\n\n'+r.complete_sources(s['refs'],sources)+'\n\n'
        if s.get('code_file'):notes+='Exact displayed excerpt ('+s['code_caption']+'):\n\n```python\n'+'\n'.join(s['code_lines'])+'\n```\n\n'
        elapsed=end
    (ROOT/'Instructor_Guide.md').write_text(notes,encoding='utf-8')
    teaching_guide(slides,sources)
    alignment_guide(slides,sources)
    for name in set(s['image'] for s in slides if s['image']):
        for destination in ['latex/images','slidev/public/images']:
            shutil.copy2(ROOT/'images'/name,ROOT/destination/name)
            pdf=Path(name).with_suffix('.pdf').name
            if (ROOT/'images'/pdf).is_file():shutil.copy2(ROOT/'images'/pdf,ROOT/destination/pdf)
    for s in slides:
        if s.get('diagram'):
            for ext in ['.tex','.svg','.pdf']:
                for destination in ['latex/diagrams','slidev/public/diagrams']:
                    shutil.copy2(ROOT/'diagrams'/(s['diagram']+ext),ROOT/destination/(s['diagram']+ext))
    for name in ['comsoc-lockup.png','image7.png']:
        shutil.copy2(ROOT/'branding'/name,ROOT/'latex/images'/name)
        shutil.copy2(ROOT/'branding'/name,ROOT/'slidev/public/branding'/name)
    shutil.copytree(ROOT/'research',ROOT/'slidev/public/research',dirs_exist_ok=True)
    shutil.copy2(ROOT/'Full_Reading_Guide.html',ROOT/'slidev/public/Full_Reading_Guide.html')
    shutil.copy2(ROOT/'Code_and_Record_Guide.html',ROOT/'slidev/public/Code_and_Record_Guide.html')
    manifest={'edition':'three-operator-cases','main_slides':len(slides),'minutes':sum(s['minutes'] for s in slides),
        'exercise_slides':[i for i,s in enumerate(slides,1) if s['kind']=='exercise'],
        'exercise_minutes':4,'tables':0,'transitions':'none','click_reveals':0,'viewing_cues':0,
        'used_images':list(dict.fromkeys(s['image'] for s in slides if s['image'])),
        'used_diagrams':list(dict.fromkeys(s['diagram'] for s in slides if s['diagram'])),
        'reading_source_ids':list(dict.fromkeys(key for s in slides for key in s['refs']))}
    manifest['visual_slides']=[i for i,s in enumerate(slides,1) if s.get('image') or s.get('diagram')]
    manifest['recorded_walkthroughs']={case:[i for i,s in enumerate(slides,1) if s['module']==case and s.get('walkthrough_step')] for case in ['voltage','restoration','cyber']}
    manifest['code_slides']=[i for i,s in enumerate(slides,1) if s.get('code_file')]
    manifest['real_screenshots']=[s['image'] for s in slides if s.get('walkthrough_step') and s.get('image')]
    dump(ROOT/'build_manifest.json',manifest)
    print(json.dumps({k:manifest[k] for k in ['main_slides','minutes','exercise_slides','visual_slides']},ensure_ascii=False))

if __name__=='__main__':main()
