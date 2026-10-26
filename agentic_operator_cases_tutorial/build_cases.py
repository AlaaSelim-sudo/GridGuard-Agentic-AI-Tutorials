"""Build the separate three-case operator tutorial in LaTeX and Slidev."""
from pathlib import Path,PureWindowsPath
from types import SimpleNamespace
import ast,hashlib,html,json,re,shutil,textwrap
import renderer as r
from latin_modern import style_html,copy_web_fonts
from build_presenter_script import presenter_note

ROOT=Path(__file__).resolve().parent
WORKSHOP=Path(r'C:/Users/f00863x/OPRO/output/agentic_grid_workflow_tutorial')
NOTEBOOK_ROOT=ROOT.parent/'agentic_grid_workflow_tutorial'
MODULES=['opening','voltage','restoration','cyber','closing']

def load(path):return json.loads(path.read_text(encoding='utf-8-sig'))
def dump(path,value):path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def notebook_cell_excerpt(spec,lab_label=''):
    """Read a stable cell ID from the canonical notebook, never the archived copy."""
    relative=Path(spec['file'])
    base=NOTEBOOK_ROOT.resolve()
    src=(base/relative).resolve()
    if relative.is_absolute() or not src.is_relative_to(base) or src.suffix!='.ipynb':
        raise ValueError('Notebook source must be a relative .ipynb path in the canonical workshop')
    notebook=load(src)
    matches=[(i,cell) for i,cell in enumerate(notebook['cells']) if cell.get('id')==spec['id']]
    if len(matches)!=1:raise ValueError(('Expected one stable notebook cell ID',str(src),spec['id']))
    index,cell=matches[0]
    if cell.get('cell_type')!='code':raise ValueError(('Notebook excerpt must select a code cell',spec['id']))
    source=cell.get('source',[])
    source=source if isinstance(source,str) else ''.join(source)
    lines=source.splitlines()
    start,end=spec.get('start',1),spec.get('end',len(lines))
    if not isinstance(start,int) or not isinstance(end,int) or not 1<=start<=end<=len(lines):
        raise ValueError(('Invalid inclusive notebook source-line range',spec['id'],start,end,len(lines)))
    label=(str(lab_label).strip()+' ') if lab_label else ''
    return {'file':relative.as_posix(),'path':str(src),'cell_id':spec['id'],'cell_index_zero_based':index,
            'start':start,'end':end,'code_lines':lines[start-1:end],
            'code_caption':relative.name+' '+label+'('+spec['id']+'), source lines '+str(start)+'–'+str(end)+'.',
            'notebook_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
            'cell_source_sha256':hashlib.sha256(source.encode('utf-8')).hexdigest()}

def module_schedule(slides):
    labels={'opening':'Agent concepts and Colab setup','voltage':'Voltage support','restoration':'Service restoration',
            'cyber':'Cyber response','closing':'Llama walkthrough and operator practice'}
    return [{'module':module,'label':labels[module],
             'slides':sum(s['module']==module for s in slides),
             'minutes':sum(s['minutes'] for s in slides if s['module']==module)} for module in MODULES]

def resolve_local(value):
    p=Path(value)
    # Historical records retain their original Windows paths. Build from the
    # packaged snapshots first, including on Linux/macOS and fresh clones.
    legacy=PureWindowsPath(str(value))
    if legacy.is_absolute():
        normalized=legacy.as_posix()
        marker='/agentic_grid_workflow_tutorial/'
        if marker in normalized:
            relative=Path(normalized.split(marker,1)[1])
            packaged=ROOT/'research/evidence'/relative
            if not packaged.resolve().is_relative_to((ROOT/'research/evidence').resolve()):
                raise ValueError('Evidence path must stay inside the packaged archive')
            if packaged.is_file():return packaged,relative
            current=NOTEBOOK_ROOT/relative
            if current.is_file():return current,relative
        if not p.is_file():
            for folder in ['additional','replots']:
                candidate=ROOT/'research/evidence'/folder/legacy.name
                if candidate.is_file():return candidate,Path(folder)/legacy.name
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
    text=str(value or '').replace('…','...')
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
            # Current Colab notebooks have extra setup cells. Preserve historical snapshots.
            if src.suffix=='.ipynb' and dst.is_file():src=dst
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
            source.setdefault('authors','Local teaching materials')
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
            if s.get('notebook_cell'):
                record=notebook_cell_excerpt(s['notebook_cell'],s.get('lab_label',''))
                filename=module+'_'+Path(record['file']).stem+'_'+record['cell_id']+'_L'+str(record['start'])+'-'+str(record['end'])+'.py'
                dest=ROOT/'research/code'/filename;dest.parent.mkdir(parents=True,exist_ok=True)
                dest.write_text('\n'.join(record['code_lines'])+'\n',encoding='utf-8')
                s['code_lines']=record['code_lines'];s['code_caption']=record['code_caption']
                s['code_file']=dest.relative_to(ROOT).as_posix();s['code_gobble']=0
                s['notebook_source']={k:v for k,v in record.items() if k not in ['code_lines','path','code_caption']}
                code_records.append({'module':module,'source_kind':'notebook_cell',
                    'source':'../agentic_grid_workflow_tutorial/'+record['file'],
                    **s['notebook_source'],'lab_label':s.get('lab_label',''),
                    'excerpt':s['code_file'],'excerpt_sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),
                    'display_change':'Exact source lines from the identified canonical notebook cell; no statements changed.'})
            elif s.get('code_lines'):
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
                    'source_page_url':s.get('image_source_url') or s.get('notebook_url') or 'research/source_'+s['refs'][0]+'.html',
                    'direct_image_url':'research/evidence/'+relative_source.as_posix(),
                    'asset_type':'Actual local GridGuard screenshot' if screenshot else ('Recorded numerical teaching figure' if 'feeder' not in name else 'Synthetic feeder visualization'),
                    'transformation':s.get('image_transformation') or ('Existing HTML rendered in a browser; selected element crop; text enlarged without changing recorded values. Full provenance: research/screenshots/capture_manifest.json.' if screenshot else ('Selected original panel without changing plotted values.' if s.get('image_crop') else 'Unchanged original plot.')),
                    'evidence_limit':s.get('caption',''),'sha256':hashlib.sha256(target.read_bytes()).hexdigest()}
                if name.startswith('hands_on_'):
                    images[name].update(credit='Classroom Labs: actual executed notebook output, Python 3.12',
                        source_page_url='research/hands_on/index.html',
                        asset_type='Executed notebook plot or browser capture',
                        transformation='Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.')
                if name.startswith('llama_'):
                    images[name].update(credit='Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved',
                        source_page_url='research/llama_replay/index.html',
                        asset_type='Browser-rendered selection of verified recorded fields',
                        transformation=s['image_transformation'],
                        provenance_note='Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.')
                if s.get('image_credit'):
                    images[name].update(credit=s['image_credit'],asset_type=s.get('image_asset_type','Attributed external figure'),provenance_note='Cropped from the supplied Stanford lecture PDF. Original author and page retained in the caption and full source guide.')
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
    assert len(slides)==83,len(slides)
    assert sum(s['minutes'] for s in slides)==90
    assert sum(s['kind']=='exercise' for s in slides)==3
    return slides

def teaching_guide(slides,sources):
    schedule=module_schedule(slides)
    route='; '.join(item['label']+': '+str(item['slides'])+' slides / '+str(item['minutes'])+' minutes' for item in schedule)+'.'
    sections=[('Using the lab and source guide',[
        ('Format',str(len(slides))+' slides, one notebook and three operator cases. Follow along during the session or finish the experiments afterward.'),
        ('Prerequisite','Use the foundations tutorial first. This session follows the current Classroom Labs notebook through voltage support, service restoration and cyber response.'),
        ('Evidence modes','Run the selected numerical cells to calculate results for your inputs. Archived model-response pools and historical evaluation records remain separately labeled. Editing L2 does not change the archived test_01 used by L3–L5, and editing the L8 sweep does not change the fixed L9 recovery fixture. No default cell calls an LLM or operates equipment.'),
        ('Setup','Open Classroom Labs, save a copy in Drive and connect a CPU. Run setup, wait for Ready, then run L0 and L1. Keep both switches False. No API key, LLM download or GPU is needed.'),
        ('Lab order','Voltage L2-L5, restoration L6-L7, cyber L8-L9, then saved agent records L10-L10B and simulated readback L12. Leave L11 disabled.'),
        ('Source figures','Monica Lam, CS224V Agentic AI, Lecture 1: Introduction, Stanford University, Fall 2026, pp.2, 19, 40 and 53. Original excerpts keep their source credits. Grid diagrams are teaching adaptations. This notebook does not run WikiChat, Genie Worksheets or a theorem prover.'),
        ('Five-role workflow','Slides 77-80 map the custom Python workflow to all three recorded L10 cases. One Llama model fills the planning and optimizer roles. Python runs awareness, simulation and verification. The notebook replays these saved stages; it does not launch five independent LLM agents.')],[])]
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
            if s.get('notebook_cell'):
                fields.append(('Source alignment','This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.'))
            else:
                fields.append(('Source alignment','research/code_manifest.json records source hashes, original line ranges and syntax-tree equivalence checks. research/code/ contains the readable display fragment. The complete historical source remains preserved in research/evidence/src/.'))
        if s.get('source_label'):fields.append(('Notebook / source locator',s['source_label']))
        links=[('['+key+'] '+r.full_citation(sources[key]),sources[key]['url']) for key in s['refs']]
        if s.get('notebook_url'):links.insert(0,('Open the notebook',s['notebook_url']))
        sections.append((str(i)+'. '+s['title'],fields,links));elapsed=end
    used=list(dict.fromkeys(key for s in slides for key in s['refs']))
    sections+=r.reading.reading_sections(used,sources,slides,r.reading.load_json(ROOT/'images/image_manifest.json'))
    md,web,tex=r.reading.reading_guides(sections)
    for a,b in [('Full Reading Guide','Teaching and Source Guide'),
                ('Agentic AI for Utility Operators — introductory lecture.','Hands-on: Three Operator Cases — notebook-aligned tutorial.'),
                ('Agentic AI for Utility Operators','Hands-on: Three Operator Cases')]:
        md=md.replace(a,b);web=web.replace(a,b);tex=tex.replace(a,b)
    # Notes may span pages. Keep headings with their first paragraph without boxing the whole lesson.
    tex=tex.replace(r'\setbox\readingEntry=\vbox\bgroup\hsize=\linewidth\subsection*{',r'\subsection*{')
    tex=tex.replace(r'\egroup\par\noindent\box\readingEntry\par\medskip',r'\par\medskip')
    (ROOT/'Teaching_Guide.md').write_text(md,encoding='utf-8')
    (ROOT/'Full_Reading_Guide.html').write_text(style_html(web),encoding='utf-8')
    (ROOT/'latex/teaching_guide.tex').write_text(tex,encoding='utf-8')

def alignment_guide(slides,sources):
    out=['<!doctype html><meta charset="utf-8"><title>Three Operator Cases: notebook cells and results</title><style>body{font:20px/1.55 Arial;color:#003b5c;max-width:1080px;margin:40px auto;padding:0 28px}h1,h2{color:#00629b}h2{border-top:3px solid #00a6b2;padding-top:28px;margin-top:50px}pre{font:19px/1.5 Consolas,monospace;white-space:pre-wrap;overflow-wrap:anywhere;background:#f2f7fa;padding:22px}a{color:#00629b;overflow-wrap:anywhere}li{margin:12px 0}.source{font-size:16px;color:#526470}</style><h1>Three Operator Cases: notebook cells and results</h1><p>Follow the current notebook by L label and stable cell ID. Selected source lines below come directly from the canonical notebook. Run the cells to calculate results for the stated inputs; distinguish those calculations from the separately labeled archived reply pools and evaluation records.</p><p>Adding a setup cell can change a numerical cell index. Stable cell IDs, source-line ranges and notebook hashes identify the exact source used to build these slides. Historical snapshots in research/evidence remain unchanged.</p>']
    for i,s in enumerate(slides,1):
        if not (s.get('lab_label') or s.get('notebook_cell') or s.get('code_file')):continue
        out.append('<h2 id="slide-'+str(i)+'">Slide '+str(i)+': '+html.escape(s['title'])+'</h2>')
        if s.get('lab_label'):out.append('<p><b>Notebook step: '+html.escape(str(s['lab_label']))+'</b></p>')
        out.append('<p>'+html.escape(' '.join(s['points']))+'</p>')
        if s.get('notebook_cell'):
            spec=s['notebook_cell'];record=s['notebook_source']
            out.append('<p>'+html.escape(s['code_caption'])+'</p><pre>'+html.escape('\n'.join(s['code_lines']))+'</pre>')
            out.append('<p class="source">Notebook SHA-256: '+html.escape(record['notebook_sha256'])+'<br>Stable cell ID: '+html.escape(spec['id'])+'; current zero-based index: '+str(record['cell_index_zero_based'])+'; source lines '+str(record['start'])+'–'+str(record['end'])+' inclusive.</p>')
        elif s.get('code_file'):
            out.append('<p>'+html.escape(s['code_caption'])+'</p><pre>'+html.escape('\n'.join(s['code_lines']))+'</pre>')
        key=s.get('main_ref') or (s['refs'][0] if s['refs'] else None)
        url=s.get('notebook_url') or (sources[key]['url'] if key else None)
        if url:out.append('<p><a href="'+html.escape(url)+'">Open the notebook or source</a></p>')
        if s.get('source_label'):out.append('<p class="source">'+html.escape(s['source_label'])+'</p>')
        if key:out.append('<p class="source">'+html.escape(r.full_citation(sources[key]))+'</p>')
    out.append('<h2>Check the alignment</h2><p><a href="research/code_manifest.json">Code manifest</a> records each canonical notebook SHA-256, stable cell ID and inclusive source-line range. The selected code statements are unchanged. Older Python-file excerpts, when used, retain their own source hashes and syntax-tree equivalence checks.</p><p>Classroom numerical cells perform fresh calculations when run. Displaying archived model replies does not call an LLM. Editing an earlier classroom parameter does not automatically change an independent archived study or fixed recovery fixture. The notebook and slide notes explain those boundaries.</p>')
    (ROOT/'Code_and_Record_Guide.html').write_text(style_html('\n'.join(out)),encoding='utf-8')

def exercise_handout(slides):
    """Keep the question sheet and its next-slide solution links in sync."""
    file=ROOT/'Exercises.html'
    prefix=file.read_text(encoding='utf-8').split('<section>',1)[0]
    out=[prefix]
    base='https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/'
    for i,s in enumerate(slides,1):
        if s['kind']!='exercise':continue
        solution=slides[i]
        assert solution.get('answer_for')==s['title']
        out.append('<section><h2>'+html.escape(s['title'])+'</h2><p>Question slide '+str(i)+' / answer slide '+str(i+1)+'. Four minutes total: predict and run for three, then discuss for one.</p>')
        if s.get('excerpt'):out.append('<pre>'+html.escape('\n'.join(s['excerpt']))+'</pre>')
        out.append('<ul>'+''.join('<li>'+html.escape(p)+'</li>' for p in s['points'])+'</ul><p>Record your result and supporting check before revealing the answer.</p><div class="space"></div>')
        out.append('<p><a href="'+base+str(i+1)+'">Reveal the worked answer</a></p></section>')
    text='\n'.join(out)
    file.write_text(text,encoding='utf-8')
    (ROOT/'slidev/public/Exercises.html').write_text(text,encoding='utf-8')

def main():
    for folder in ['research','images','latex/images','latex/diagrams','slidev/public/images','slidev/public/diagrams','slidev/public/branding']:
        (ROOT/folder).mkdir(parents=True,exist_ok=True)
    r.reading.REVIEWED='24 October 2026'
    original_escape=r.reading.esc
    r.reading.esc=lambda value:readable_tex_escape(original_escape,value)
    sources=normalize_registry()
    slides=prepare_slides()
    for i,s in enumerate(slides,1):
        assert all(key in sources for key in s['refs']),(i,s['refs'])
        if s.get('main_ref'):assert s['main_ref'] in s['refs']
    # The same renderer and theme used by the preceding edition.
    cues={c['title']:c for c in load(ROOT/'content/presenter_script.json')['slides']}
    assert set(cues)=={s['title'] for s in slides}
    presented=[dict(s,note=presenter_note(cues[s['title']])) for s in slides]
    frames=''.join(r.render_frame(s,sources) for s in presented).replace('{reading_guide.pdf}','{teaching_guide.pdf}')
    frames="\n".join(line.rstrip() for line in frames.splitlines())+"\n"
    front='''---
theme: default
title: Hands-on — Three Operator Cases
info: Follow Classroom Labs through voltage support, service restoration and cyber response, with three exercises
author: Alaa Selim (MIT/Dartmouth) and Mohamed Chehada (UT Austin)
transition: none
aspectRatio: 16/9
canvasWidth: 1280
colorSchema: light
fonts:
  sans: Latin Modern Roman
  serif: Latin Modern Roman
  mono: Latin Modern Mono
  provider: none
mdc: false
drawings:
  persist: false
download: false
---

'''
    front=front.replace('title: Hands-on — Three Operator Cases','title: '+json.dumps(slides[0]['title'],ensure_ascii=False))
    web=front+'\n---\ntransition: none\n---\n\n'.join(r.render_slide(s,i,len(slides),sources) for i,s in enumerate(presented,1))
    web=web.replace('Separate reading-guide PDF','Teaching and source guide PDF')
    for token in ['What to notice','v-click','v-motion',r'\pause',r'\uncover<',r'\transfade','<table',r'\begin{tabular}']:
        assert token not in frames+web,token
    (ROOT/'latex/frames.tex').write_text(frames,encoding='utf-8')
    (ROOT/'slidev/slides.md').write_text(web,encoding='utf-8')
    dump(ROOT/'lesson_content.json',slides)
    route='; '.join(item['label']+': '+str(item['slides'])+' slides / '+str(item['minutes'])+' minutes' for item in module_schedule(slides))
    notes='# Instructor Guide: Hands-on Three Operator Cases\n\n'+str(len(slides))+' static slides / '+str(sum(s['minutes'] for s in slides))+' minutes. '+route+'. Follow the L labels and stable notebook cell IDs; predict, run, edit and interpret each result. The three exercises have separate teacher notes and debriefs. Numerical calculations and archived model replies remain distinct. No tables, transitions or click reveals.\n\n'
    elapsed=0
    for i,s in enumerate(slides,1):
        end=elapsed+s['minutes']
        notes+='## '+str(i)+'. '+s['title']+'\n\n'+r.reading.stamp(elapsed)+'–'+r.reading.stamp(end)+' / '+str(s['minutes'])+' minutes.\n\n'+s['note']+'\n\nFull sources:\n\n'+r.complete_sources(s['refs'],sources)+'\n\n'
        if s.get('code_file'):notes+='Exact displayed excerpt ('+s['code_caption']+'):\n\n```python\n'+'\n'.join(s['code_lines'])+'\n```\n\n'
        elapsed=end
    (ROOT/'Instructor_Guide.md').write_text(notes,encoding='utf-8')
    teaching_guide(slides,sources)
    alignment_guide(slides,sources)
    exercise_handout(slides)
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
    copy_web_fonts(ROOT/'slidev/public/fonts')
    exercise_slides=[i for i,s in enumerate(slides,1) if s['kind']=='exercise']
    manifest={'edition':'plain-language-llama-and-operator-practice','main_slides':len(slides),'minutes':sum(s['minutes'] for s in slides),
        'exercise_slides':exercise_slides,'exercise_count':len(exercise_slides),
        'exercise_answer_slides':[i for i,s in enumerate(slides,1) if s.get('answer_for')],
        'exercise_minutes':{str(i):s['minutes'] for i,s in enumerate(slides,1) if s['kind']=='exercise'},
        'tables':0,'transitions':'none','click_reveals':0,'viewing_cues':0,
        'used_images':list(dict.fromkeys(s['image'] for s in slides if s['image'])),
        'used_diagrams':list(dict.fromkeys(s['diagram'] for s in slides if s['diagram'])),
        'reading_source_ids':list(dict.fromkeys(key for s in slides for key in s['refs']))}
    manifest['visual_slides']=[i for i,s in enumerate(slides,1) if s.get('image') or s.get('diagram')]
    manifest['recorded_llama_replays']=[{'slide':i,'scenario':s['replay_scenario'],'recorded_call':s['replay_call']}
        for i,s in enumerate(slides,1) if s.get('replay_call')]
    manifest['proposed_pilot_slides']=[i for i,s in enumerate(slides,1) if str(s.get('diagram','')).startswith('ops_')]
    manifest['recorded_walkthroughs']={case:[i for i,s in enumerate(slides,1) if s['module']==case and s.get('walkthrough_step')] for case in ['voltage','restoration','cyber']}
    manifest['code_slides']=[i for i,s in enumerate(slides,1) if s.get('code_file')]
    manifest['real_screenshots']=[s['image'] for s in slides if s.get('walkthrough_step') and s.get('image')]
    manifest['module_schedule']=module_schedule(slides)
    manifest['notebook_actions']=[{'slide':i,'module':s['module'],'lab_label':s.get('lab_label',''),
        **s['notebook_source'],'excerpt':s['code_file'],'notebook_url':s.get('notebook_url')}
        for i,s in enumerate(slides,1) if s.get('notebook_cell')]
    manifest['lab_slides']=[{'slide':i,'lab_label':s['lab_label'],'notebook_url':s.get('notebook_url')}
        for i,s in enumerate(slides,1) if s.get('lab_label')]
    dump(ROOT/'build_manifest.json',manifest)
    print(json.dumps({k:manifest[k] for k in ['main_slides','minutes','exercise_slides','visual_slides']},ensure_ascii=False))

if __name__=='__main__':main()
