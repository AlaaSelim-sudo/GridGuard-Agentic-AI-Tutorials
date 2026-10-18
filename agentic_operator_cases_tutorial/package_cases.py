"""Package the verified presentation, editable source, teaching guide and evidence."""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
import hashlib,html,json,os,shutil
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

def main():
    manifest=json.loads((ROOT/'build_manifest.json').read_text())
    assert manifest['main_slides']==59 and manifest['minutes']==120
    assert manifest['exercise_slides']==[17,37,54] and len(manifest['visual_slides'])==49
    assert len(manifest['real_screenshots'])==12 and len(manifest['code_slides'])==3
    assert manifest['tables']==manifest['click_reveals']==manifest['viewing_cues']==0
    assert len(PdfReader(ROOT/'latex/main.pdf').pages)==59
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
    for directory in ['slidev/public','slidev/dist']:
        shutil.copy2(ROOT/'Teaching_and_Source_Guide.pdf',ROOT/directory/'Full_Reading_Guide.pdf')
        shutil.copy2(ROOT/'Full_Reading_Guide.html',ROOT/directory/'Full_Reading_Guide.html')
        shutil.copy2(ROOT/'Code_and_Record_Guide.html',ROOT/directory/'Code_and_Record_Guide.html')
        shutil.copytree(ROOT/'research',ROOT/directory/'research',dirs_exist_ok=True)
    slides=json.loads((ROOT/'lesson_content.json').read_text(encoding='utf-8'))
    exercises=[(i,s) for i,s in enumerate(slides,1) if s['kind']=='exercise']
    worksheet='<!doctype html><meta charset="utf-8"><title>Three Operator Cases: exercises</title><style>body{font:20px/1.5 Arial;color:#003b5c;max-width:1050px;margin:35px auto}h1,h2{color:#00629b}section{break-after:page;margin-bottom:70px}img{width:100%;height:290px;object-fit:contain}li{margin:15px 0}.space{height:140px;border-bottom:1px solid #bbb}</style><h1>Three Operator Cases: exercises</h1><p>Four minutes each: read, discuss in pairs, then name a decision and one supporting check.</p>'
    for i,s in exercises:
        worksheet+='<section><h2>'+html.escape(s['title'])+'</h2><p>Presentation slide '+str(i)+'.</p>'
        if s.get('diagram'):worksheet+='<img src="diagrams/'+s['diagram']+'.svg">'
        worksheet+='<ul>'+''.join('<li>'+html.escape(p)+'</li>' for p in s['points'])+'</ul><p>Decision, reason and next step:</p><div class="space"></div></section>'
    (ROOT/'Exercises.html').write_text(worksheet,encoding='utf-8')
    for directory in ['slidev/public','slidev/dist']:
        shutil.copy2(ROOT/'Exercises.html',ROOT/directory/'Exercises.html')
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
    result={**manifest,'teaching_guide_pages':len(PdfReader(ROOT/'Teaching_and_Source_Guide.pdf').pages),'files':{}}
    for path in [source,complete,ROOT/'Three_Operator_Cases.pdf',ROOT/'Teaching_and_Source_Guide.pdf']:
        result['files'][path.name]={'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
    (ROOT/'deliverables.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ['main_slides','minutes','exercise_slides','teaching_guide_pages','files']},indent=2))
if __name__=='__main__':main()
