"""Package the verified presentation, editable source, teaching guide and evidence."""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
import argparse,hashlib,html,json,math,os,shutil
from pypdf import PdfReader,PdfWriter
from pypdf.generic import TextStringObject
ROOT=Path(__file__).resolve().parent

def files(directory):
    for base,dirs,names in os.walk(directory,followlinks=False):
        dirs[:]=[d for d in dirs if d not in {'node_modules','_build','__pycache__'}]
        for name in names:yield Path(base)/name
def portable(text):
    return text.replace('../research/','research/').replace('../Full_Reading_Guide.html','Full_Reading_Guide.html')
def json_portable(value):
    if isinstance(value,list):return [json_portable(v) for v in value]
    if isinstance(value,dict):return {k:json_portable(v) for k,v in value.items()}
    if isinstance(value,str):
        normalized=value.replace('\\','/')
        workshop='C:/Users/f00863x/OPRO/output/agentic_grid_workflow_tutorial/'
        project=ROOT.as_posix()+'/'
        if normalized.startswith(workshop):return 'research/evidence/'+normalized[len(workshop):]
        if normalized.startswith(project):return normalized[len(project):]
    return value
def archive_file(z,path,relative):
    if path.suffix=='.json' and (str(relative).startswith('content') or str(relative)=='lesson_content.json'):
        value=json.loads(path.read_text(encoding='utf-8-sig'))
        z.writestr(str(relative).replace('\\','/'),json.dumps(json_portable(value),ensure_ascii=False,indent=2)+'\n')
    else:z.write(path,str(relative).replace('\\','/'))

def require(condition,message):
    if not condition:raise ValueError(message)

def validate_manifest(manifest,slides):
    """Check the current lesson rather than assuming a previous slide layout."""
    require(isinstance(slides,list) and bool(slides),'The lesson must contain slides')
    minutes=[s['minutes'] for s in slides]
    require(all(type(value) in (int,float) and math.isfinite(value) and value>0 for value in minutes),
            'Each slide needs a finite positive duration')
    require(manifest['main_slides']==len(slides),'Manifest slide count differs from the lesson')
    require(math.isclose(manifest['minutes'],sum(minutes),rel_tol=0,abs_tol=1e-8),
            'Manifest duration differs from the lesson')
    exercises=[(i,s) for i,s in enumerate(slides,1) if s['kind']=='exercise']
    expected={
        'exercise_slides':[i for i,_ in exercises],
        'visual_slides':[i for i,s in enumerate(slides,1) if s.get('image') or s.get('diagram')],
        'code_slides':[i for i,s in enumerate(slides,1) if s.get('code_file')],
        'real_screenshots':[s['image'] for s in slides if s.get('walkthrough_step') and s.get('image')],
        'used_images':list(dict.fromkeys(s['image'] for s in slides if s.get('image'))),
        'used_diagrams':list(dict.fromkeys(s['diagram'] for s in slides if s.get('diagram'))),
        'reading_source_ids':list(dict.fromkeys(key for s in slides for key in s['refs'])),
    }
    for key,value in expected.items():
        require(manifest[key]==value,'Manifest '+key+' differs from the lesson')
    if 'recorded_walkthroughs' in manifest:
        expected_walkthroughs={case:[i for i,s in enumerate(slides,1)
            if s.get('module')==case and s.get('walkthrough_step')]
            for case in manifest['recorded_walkthroughs']}
        require(manifest['recorded_walkthroughs']==expected_walkthroughs,
                'Manifest recorded walkthroughs differ from the lesson')
    if 'exercise_minutes' in manifest:
        declared=manifest['exercise_minutes']
        actual=[s['minutes'] for _,s in exercises]
        if isinstance(declared,list):
            require(declared==actual,'Manifest exercise durations differ from the lesson')
        elif isinstance(declared,dict):
            require(declared=={str(i):s['minutes'] for i,s in exercises},
                    'Manifest exercise durations differ from the lesson')
        else:
            require(all(value==declared for value in actual),
                    'Manifest common exercise duration differs from the lesson')
    require(manifest['tables']==manifest['click_reveals']==manifest['viewing_cues']==0,
            'The presentation must remain static and without tables or viewing cues')
    require(len(PdfReader(ROOT/'latex/main.pdf').pages)==len(slides),
            'Compiled PDF slide count differs from the lesson')
    return exercises

def write_exercises(exercises):
    worksheet='<!doctype html><meta charset="utf-8"><title>Three Operator Cases: exercises</title><style>body{font:20px/1.5 Arial;color:#003b5c;max-width:1050px;margin:35px auto;padding:0 24px}h1,h2{color:#00629b}section{break-after:page;margin-bottom:70px}img{width:100%;height:290px;object-fit:contain}li{margin:15px 0}.space{height:140px;border-bottom:1px solid #bbb}</style><h1>Three Operator Cases: exercises</h1><p>Follow each task, record the result, and explain one supporting check. Each exercise has its own time allowance.</p>'
    worksheet+='<p><a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Open Classroom Labs in Google Colab</a>. Run setup, L0 and L1 first; follow each case in order.</p>'
    for i,s in exercises:
        duration=f"{s['minutes']:g}"
        worksheet+='<section><h2>'+html.escape(s['title'])+'</h2><p>Presentation slide '+str(i)+' · '+duration+' minutes.</p>'
        if s.get('diagram'):
            worksheet+='<img alt="Exercise diagram" src="diagrams/'+html.escape(s['diagram'],quote=True)+'.svg">'
        elif s.get('image'):
            worksheet+='<img alt="Exercise figure" src="images/'+html.escape(s['image'],quote=True)+'">'
        if s.get('excerpt'):worksheet+='<pre>'+html.escape('\n'.join(s['excerpt']))+'</pre>'
        worksheet+='<ul>'+''.join('<li>'+html.escape(p)+'</li>' for p in s['points'])+'</ul><p>Result, supporting check, and next step:</p><div class="space"></div></section>'
    (ROOT/'Exercises.html').write_text(worksheet,encoding='utf-8')

def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pdf-only',action='store_true',
                        help='Refresh PDFs and HTML guides without copying research or creating ZIPs')
    args=parser.parse_args(argv)
    manifest=json.loads((ROOT/'build_manifest.json').read_text(encoding='utf-8-sig'))
    slides=json.loads((ROOT/'lesson_content.json').read_text(encoding='utf-8-sig'))
    exercises=validate_manifest(manifest,slides)
    for stem in ['main','teaching_guide']:
        log=(ROOT/f'latex/{stem}.log').read_text(encoding='utf-8',errors='replace')
        assert 'Overfull' not in log and 'Missing character' not in log,stem
    guide=PdfWriter(clone_from=ROOT/'latex/teaching_guide.pdf')
    for page in guide.pages:
        for annot in page.get('/Annots',[]):
            action=annot.get_object().get('/A')
            if action and str(action.get('/URI','')).startswith('../research/'):
                action[TextStringObject('/URI')]=TextStringObject(str(action['/URI'])[3:])
    with (ROOT/'Teaching_and_Source_Guide.pdf').open('wb') as f:guide.write(f)
    shutil.copy2(ROOT/'latex/main.pdf',ROOT/'Three_Operator_Cases.pdf')
    write_exercises(exercises)
    for directory in ['slidev/public','slidev/dist']:
        destination=ROOT/directory
        if directory=='slidev/public':destination.mkdir(parents=True,exist_ok=True)
        elif not destination.is_dir():continue
        for source_name,target_name in [
            ('Three_Operator_Cases.pdf','Three_Operator_Cases.pdf'),
            ('Teaching_and_Source_Guide.pdf','Full_Reading_Guide.pdf'),
            ('Full_Reading_Guide.html','Full_Reading_Guide.html'),
            ('Code_and_Record_Guide.html','Code_and_Record_Guide.html'),
            ('Exercises.html','Exercises.html'),
        ]:
            shutil.copy2(ROOT/source_name,destination/target_name)
        if not args.pdf_only:
            shutil.copytree(ROOT/'research',destination/'research',dirs_exist_ok=True)
    deliverable_paths=[ROOT/name for name in ['Three_Operator_Cases.pdf','Teaching_and_Source_Guide.pdf',
        'Full_Reading_Guide.html','Code_and_Record_Guide.html','Exercises.html']]
    if not args.pdf_only:
        deliverable_paths=package_archives()+deliverable_paths
    result={**manifest,'packaging_mode':'pdf-only' if args.pdf_only else 'full',
            'teaching_guide_pages':len(PdfReader(ROOT/'Teaching_and_Source_Guide.pdf').pages),'files':{}}
    for path in deliverable_paths:
        result['files'][path.name]={'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
    (ROOT/'deliverables.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ['main_slides','minutes','exercise_slides','teaching_guide_pages','files']},indent=2))

def package_archives():
    """Retain the complete legacy source and evidence packages on full runs."""
    source=ROOT/'Three_Operator_Cases_LaTeX_Source.zip'
    with ZipFile(source,'w',ZIP_DEFLATED) as z:
        for path in (ROOT/'latex').glob('*.tex'):
            z.writestr(path.name,portable(path.read_text(encoding='utf-8')))
        for directory in ['images','diagrams','research']:
            for path in files(ROOT/directory):
                if directory=='diagrams' and path.suffix not in ['.tex','.svg','.pdf']:continue
                z.write(path,path.relative_to(ROOT).as_posix())
        for name in ['comsoc-lockup.png','image7.png']:z.write(ROOT/'branding'/name,'images/'+name)
        for name in ['README.md','Instructor_Guide.md','Teaching_Guide.md','Full_Reading_Guide.html','Code_and_Record_Guide.html','Teaching_and_Source_Guide.pdf','Exercises.html']:
            z.write(ROOT/name,name)
    complete=ROOT/'Three_Operator_Cases_Complete.zip'
    with ZipFile(complete,'w',ZIP_DEFLATED) as z:
        for path in ROOT.iterdir():
            if path.is_file() and path.name!='deliverables.json' and path.suffix in ['.py','.mjs','.md','.html','.json','.pdf']:
                archive_file(z,path,path.relative_to(ROOT))
        for directory in ['content','branding','images','diagrams','research','latex','slidev']:
            for path in files(ROOT/directory):
                if directory=='latex' and path.suffix not in ['.tex','.pdf']:continue
                archive_file(z,path,path.relative_to(ROOT))
    for path in [source,complete]:
        with ZipFile(path) as z:assert z.testzip() is None
    return [source,complete]
if __name__=='__main__':main()
