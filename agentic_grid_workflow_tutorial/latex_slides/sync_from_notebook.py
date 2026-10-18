"""Extract notebook and full implementation code; map the expanded slide routes.

Run from any directory: python latex_slides/sync_from_notebook.py
Only Python's standard library is required. Recompile after syncing.
"""
from pathlib import Path
import hashlib
import json
import re

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
manifest=[]
outputs={}
notebooks=['Graph_Workflow_Lab.ipynb','Classroom_Labs.ipynb','Workshop_Step_by_Step.ipynb']
if (ROOT/'Agent_Trace_and_Latency.ipynb').exists():notebooks.append('Agent_Trace_and_Latency.ipynb')
if (ROOT/'Proposal_Complete_Workflow.ipynb').exists():notebooks.append('Proposal_Complete_Workflow.ipynb')
if (ROOT/'LLM_Response_Selection.ipynb').exists():notebooks.append('LLM_Response_Selection.ipynb')
for notebook in notebooks:
    nb=json.loads((ROOT/notebook).read_text(encoding='utf-8'))
    code_ordinal=0
    for index,cell in enumerate(nb['cells']):
        if cell.get('cell_type')=='code':code_ordinal+=1
        key=cell.get('metadata',{}).get('checkpoint')
        if not key:continue
        assert cell.get('cell_type')=='code',(notebook,key,'checkpoint must identify code')
        assert re.fullmatch(r'[A-Z]+\d+',key),(notebook,key,'invalid checkpoint')
        assert not any(row['checkpoint']==key for row in manifest),(notebook,key,'duplicate checkpoint')
        code=cell['source'];code=''.join(code) if isinstance(code,list) else code
        if not code.endswith('\n'):code+='\n'
        outputs[HERE/'snippets'/f'{key}.py']=code.encode('utf-8')
        manifest.append({'checkpoint':key,'title':cell['metadata'].get('title',key),'notebook':notebook,
                         'cell_index':index,'code_ordinal':code_ordinal,
                         'lines':len(code.splitlines()),'sha256':hashlib.sha256(code.encode()).hexdigest()})
lookup={row['checkpoint']:row for row in manifest}

def expand(path):
    text=path.read_text(encoding='utf-8')
    return re.sub(r'\\input\{([^}]+)\}',lambda m:expand(HERE/m[1]) if m[1]!='preamble.tex' else '',text)
master=expand(HERE/'Agentic_Grid_Workshop.tex')
frames=list(re.finditer(r'\\begin\{frame\}(?:\[[^\]]*\])?(?:\{([^\n]+)\})?([\s\S]*?)\\end\{frame\}',master))
nav=HERE/'Agentic_Grid_Workshop.nav'
page_ranges=re.findall(r'\\beamer@framepages\s*\{(\d+)\}\s*\{(\d+)\}',nav.read_text(encoding='utf-8')) if nav.exists() else []
compiled=len(page_ranges)==len(frames)
def pages(number):
    if not compiled:return 'Recompile to refresh'
    first,last=page_ranges[number-1]
    return first if first==last else f'{first}–{last}'
appendix=master.find('\\appendix')
appendix=len(master) if appendix<0 else appendix
main_frames=sum(m.start()<appendix for m in frames)
def route(match):
    if match.start()>=appendix:return 'reference'
    return 'deepdive' if re.search(r'^\s*\\deepdive\s*(?:%[^\n]*)?$',match[2],re.MULTILINE) else 'core'
core_frames=sum(route(m)=='core' for m in frames)
deepdive_frames=sum(route(m)=='deepdive' for m in frames)
reference_frames=sum(route(m)=='reference' for m in frames)
route_summary=(f'{core_frames} core frames form the 180-minute route, including a ten-minute break; '
               f'{deepdive_frames} optional detail frames and {reference_frames} reference frames are outside that timed route.')
rows=[];by_checkpoint={key:[] for key in lookup};frame_data=[];implementation={}
notes=['# Instructor notes: core workshop and optional code routes','',
       'Begin with Graph_Workflow_Lab.ipynb (G0–G5), then use Classroom_Labs.ipynb (L0–L12) for the engineering cases. G is a real LangGraph toy example. L uses the existing custom Python engineering workflow. All other notebook checkpoints in the technical appendix are explicitly separate recorded experiments or detailed method companions. Implementation excerpts are exact source copies, not standalone cells.', '',
       f'Each logical frame can have several presentation pages for progressive reveals. The handout shows one completed page per frame. Stop the taught route after frame {core_frames}; the technical appendix follows as one separate block. Every frame has a visible Next bridge and a short PDF fade transition. Reveal pages work with normal page advance; fade support depends on the viewer.', '',route_summary,'']
for number,match in enumerate(frames,1):
    title=match[1] or 'Agentic grid workflows';body=match[2]
    transitions=re.findall(r'\\slidetransition\{([^{}]+)\}',body)
    assert len(transitions)==1,(number,'Each frame needs exactly one visible transition')
    assert '\\sources{' in body,(number,'Missing source footer')
    keys=[]
    labels=(re.findall(r'\\checkpoint\{([^}]+)\}',body)+
            re.findall(r'\\(?:cellcode|cellall)\{([^}]+)\}',body)+
            re.findall(r'^([A-Z]\d+(?:--[A-Z]\d+)?):',title))
    for label in labels:
        span=re.fullmatch(r'([A-Z])(\d+)--\1(\d+)',label)
        expanded=[f'{span[1]}{k}' for k in range(int(span[2]),int(span[3])+1)] if span else [label]
        keys.extend(k for k in expanded if k not in keys)
    for key in keys:
        assert key in lookup,(number,key)
        by_checkpoint[key].append(number)
    for key,start,end in re.findall(r'\\cellcode\{([^}]+)\}\{(\d+)\}\{(\d+)\}',body):
        assert key in lookup and 1<=int(start)<=int(end)<=lookup[key]['lines'],(number,key,start,end)
    for key in re.findall(r'\\cellall\{([^}]+)\}',body):assert key in lookup,(number,key)
    if '\\deepdive' in body:
        assert re.search(r'^\s*\\deepdive\s*(?:%[^\n]*)?$',body,re.MULTILINE),(number,'deepdive must be standalone')
    excerpts=[]
    for stem,start,end in re.findall(r'\\implcode\{([^}]+)\}\{(\d+)\}\{(\d+)\}',body):
        assert re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*',stem),(number,stem,'invalid source module')
        if stem not in implementation:
            source=ROOT/'src'/f'{stem}.py';data=source.read_bytes()
            snippet=HERE/'snippets'/f'impl_{stem}.py'
            outputs[snippet]=data
            implementation[stem]={'module':stem,'source':f'src/{stem}.py',
                'snippet':f'snippets/impl_{stem}.py','lines':len(data.decode('utf-8').splitlines()),
                'sha256':hashlib.sha256(data).hexdigest(),'copy_exact':True,'excerpts':[]}
        start,end=int(start),int(end)
        assert 1<=start<=end<=implementation[stem]['lines'],(number,stem,start,end)
        implementation[stem]['excerpts'].append({'frame':number,'start':start,'end':end})
        excerpts.append({'module':stem,'start':start,'end':end})
    frame_notebooks=list(dict.fromkeys(lookup[key]['notebook'] for key in keys))
    frame_route=route(match)
    frame_data.append({'frame':number,'presentation_pages':pages(number),'handout_page':number,
                       'title':title,'route':frame_route,'checkpoints':keys,'notebooks':frame_notebooks,
                       'transition':transitions[0],
                       'implementation_excerpts':excerpts})
    # Notes are balanced TeX groups, not a greedy regular-expression capture.
    at=body.find('\\note{')
    if at>=0:
        i=at+6;depth=1;start=i
        while depth and i<len(body):
            if body[i]=='{' and body[i-1]!='\\':depth+=1
            elif body[i]=='}' and body[i-1]!='\\':depth-=1
            i+=1
        assert depth==0,(number,'unbalanced speaker note')
        note=body[start:i-1].replace('\\_','_').replace('\\%','%').replace('~',' ')
        note=re.sub(r'\\(?:texttt|textbf|emph)\{([^{}]*)\}',r'\1',note)
        notes.extend([f'## Frame {number}: {title}', '',f'Route: **{frame_route}**. Notebook: {", ".join(frame_notebooks) or "Concept / discussion"}.','',f'Presentation pages: {pages(number)}. Handout page: {number}.','',f'Visible transition: {transitions[0]}','',note,''])
    else:raise AssertionError(f'Missing speaker note on slide {number}')
    source_ranges='; '.join(f'{e["module"]}.py:{e["start"]}–{e["end"]}' for e in excerpts)
    rows.append(f'| {number} | {pages(number)} | {frame_route} | {title} | {", ".join(frame_notebooks) or "—"} | {", ".join(keys) or "Concept / discussion"} | {source_ranges or "—"} |')
# Archive checkpoints without a selected slide remain available in their original notebook.
lines=['# Slide–notebook alignment','',
       'Generated from the LaTeX master and notebooks. Checkpoint labels are stable; execution counts are not. Code ordinals count all code cells within the named notebook, starting at one. Manifest cell_index values are zero-based. Run the complete corresponding cell, including lines omitted from a slide.','',
       'Implementation excerpts use one-based inclusive source lines from full byte-for-byte module copies. implementation_sources.json records source paths, exact SHA-256 hashes and all used ranges.','',
       route_summary+' Handout page numbers equal logical frame numbers. Presentation page ranges include the question and answer reveals.', '',
       '| Checkpoint | Notebook | Code ordinal | Route(s) | Logical frames / handout pages | Presentation pages | Purpose |',
       '|---|---|---:|---|---|---|---|']
for number,row in enumerate(manifest,1):
    key=row['checkpoint'];routes=list(dict.fromkeys(frame_data[n-1]['route'] for n in by_checkpoint[key]))
    lines.append(f'| {key} | [{row["notebook"]}](../{row["notebook"]}) | {row["code_ordinal"]} | {", ".join(routes)} | {", ".join(map(str,by_checkpoint[key]))} | {", ".join(pages(n) for n in by_checkpoint[key])} | {row["title"]} |')
lines+=['','## Every frame','','| Logical frame / handout page | Presentation pages | Route | Frame title | Notebook | Checkpoint | Implementation excerpt |','|---:|---|---|---|---|---|---|']+rows
lines+=['','## Full implementation sources','','| Module | Source | Exact copied snippet | Lines | SHA-256 |','|---|---|---|---:|---|']
for info in implementation.values():
    lines.append(f'| {info["module"]} | {info["source"]} | {info["snippet"]} | {info["lines"]} | {info["sha256"]} |')
outputs[HERE/'Slide_Notebook_Map.md']=('\n'.join(lines)+'\n').encode('utf-8')
outputs[HERE/'Instructor_Notes.md']=('\n'.join(notes)+'\n').encode('utf-8')
outputs[HERE/'checkpoints.json']=(json.dumps(manifest,indent=2)+'\n').encode('utf-8')
outputs[HERE/'implementation_sources.json']=(json.dumps({'sources':list(implementation.values()),'copy_policy':'Full original source bytes; one-based inclusive excerpt ranges.'},indent=2)+'\n').encode('utf-8')
outputs[HERE/'frame_pages.json']=(json.dumps({'logical_frames':len(frames),'main_frames':main_frames,
    'core_frames':core_frames,'deepdive_frames':deepdive_frames,'reference_frames':reference_frames,
    'appendix_frames':reference_frames,'notebooks':notebooks,
    'presentation_pages':int(page_ranges[-1][1]) if compiled and page_ranges else None,'frames':frame_data},indent=2)+'\n').encode('utf-8')
# All notebooks, references, speaker notes and excerpt ranges passed before writes.
for path,data in outputs.items():
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_bytes(data)
print(f'Synced {len(manifest)} checkpoint cells from {len(notebooks)} notebooks; validated {len(frames)} logical frames ({core_frames} core, {deepdive_frames} optional deep dives, {reference_frames} reference), {len(implementation)} exact implementation sources and all code excerpt ranges; compiled page map: {compiled}.')
