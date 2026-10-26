"""Check, regenerate and build the current hands-on workshop from a clone.

Examples (from the repository root):
  python scripts/build-workshop.py check
  python scripts/build-workshop.py content
  python scripts/build-workshop.py pdf
  python scripts/build-workshop.py all
"""
from pathlib import Path
import argparse,hashlib,json,os,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
DECK=ROOT/'agentic_operator_cases_tutorial'
RECEIPT=DECK/'research/presenter/build_receipt.json'
PDFS=['Three_Operator_Cases.pdf','Teaching_and_Source_Guide.pdf','Participant_Lab_Guide.pdf','Presenter_Script.pdf']
MODULES=['opening','voltage','restoration','cyber','closing']
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def require(ok,message):
 if not ok:raise ValueError(message)
def executable(env_name,default):
 name=os.environ.get(env_name) or default
 found=shutil.which(name)
 if not found and Path(name).is_file():found=str(Path(name).resolve())
 if not found:raise ValueError(f'{default} is unavailable. Put it on PATH or set {env_name} to its executable path.')
 return found
def run(args,cwd=DECK):
 print('Running:',Path(str(args[0])).name,' '.join(str(a) for a in args[1:]),flush=True)
 subprocess.run([str(a) for a in args],cwd=cwd,check=True)
def validate(check_pdfs=False):
 authored=[s for m in MODULES for s in read(DECK/'content'/(m+'.json'))]
 slides=read(DECK/'lesson_content.json');cues=read(DECK/'content/presenter_script.json')['slides']
 require(len(authored)==len(slides)==len(cues)==83,'The workshop and script must contain eighty-three slides.')
 require([s['title'] for s in authored]==[s['title'] for s in slides],'Run content: generated slide order differs from the authored modules.')
 require(len({c['title'] for c in cues})==83 and {c['title'] for c in cues}=={s['title'] for s in slides},'Every current slide needs one presenter cue.')
 require(all(s['say'] and s['action'] for s in cues),'Each presenter cue needs spoken text and a delivery action.')
 require(sum(s['minutes'] for s in slides)==90,'The workshop must total 90 teaching minutes.')
 require(sum(s['minutes'] for s in slides[:10])==7,'The short concept opening must total seven minutes.')
 require([i for i,s in enumerate(slides,1) if s['kind']=='exercise']==[25,45,61],'Exercise locations differ from the current teaching route.')
 require(all(s['minutes']==3 and slides[i+1].get('answer_for')==s['title'] and slides[i+1]['minutes']==1 for i,s in enumerate(slides) if s['kind']=='exercise'),'Each exercise needs three question minutes followed by one answer minute.')
 book=ROOT/'agentic_grid_workflow_tutorial/Classroom_Labs.ipynb';nb=read(book);cell_map={c.get('id'):c for c in nb['cells']};count=0
 for i,s in enumerate(slides,1):
  for key in ['image','diagram']:
   if s.get(key):
    p=DECK/('images' if key=='image' else 'diagrams')/(s[key] if key=='image' else s[key]+'.svg')
    require(p.is_file(),'Missing visual: '+str(p))
  spec=s.get('notebook_cell')
  if spec:
   require(spec['id'] in cell_map,'Notebook cell is missing: '+spec['id']);cell=cell_map[spec['id']];text=cell['source'];text=text if isinstance(text,str) else ''.join(text)
   require(s['code_lines']==text.splitlines()[spec['start']-1:spec['end']],f'Slide {i} no longer matches its notebook source.')
   require(s['notebook_source']['notebook_sha256']==sha(book),'Run content: canonical notebook hash has changed.');count+=1
 require(count==13,'Expected thirteen exact notebook excerpts.')
 if check_pdfs and RECEIPT.is_file():
  receipt=read(RECEIPT)
  require(receipt['lesson_sha256']==sha(DECK/'lesson_content.json'),'Run pdf: compiled PDFs belong to older lesson content.')
  require(receipt['script_cues_sha256']==sha(DECK/'content/presenter_script.json'),'Run pdf: presenter PDF belongs to older cues.')
  for name,hash_value in receipt['pdf_sha256'].items():require((DECK/name).is_file() and sha(DECK/name)==hash_value,'Run pdf: download changed after its verified build: '+name)
 print(json.dumps({'slides':83,'minutes':90,'presenter_cues':83,'exact_notebook_excerpts':count,'exercises':[25,45,61],'pdf_receipt_checked':check_pdfs and RECEIPT.is_file()}),flush=True)
def content():
 run([sys.executable,'-X','utf8','build_cases.py'])
 run([sys.executable,'-X','utf8','build_presenter_script.py'])
 validate()
def pdf():
 tectonic=executable('TECTONIC','tectonic');pop=executable('PDFTOPPM','pdftoppm');os.environ['PDFTOPPM']=pop
 content()
 run([sys.executable,'-X','utf8','research/lab_teaching/build_participant_guide.py'])
 run([sys.executable,'-X','utf8','build_presenter_script.py','--pdf'])
 for stem in ['main','teaching_guide']:
  run([tectonic,'-X','compile','--keep-logs','--keep-intermediates',stem+'.tex'],DECK/'latex')
  text=(DECK/'latex'/(stem+'.log')).read_text(encoding='utf-8',errors='replace')
  require('Overfull' not in text and 'Missing character' not in text,'Fix the LaTeX layout diagnostics in '+stem+'.log')
 run([sys.executable,'-X','utf8','package_cases.py','--pdf-only'])
 receipt=dict(lesson_sha256=sha(DECK/'lesson_content.json'),script_cues_sha256=sha(DECK/'content/presenter_script.json'),pdf_sha256={n:sha(DECK/n) for n in PDFS})
 RECEIPT.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
 shutil.copy2(RECEIPT,DECK/'slidev/public/research/presenter/build_receipt.json')
 validate(check_pdfs=True)
def site(base):
 require(RECEIPT.is_file(),'Run pdf or all once to record the generated downloads.')
 validate(check_pdfs=True)
 run([executable('NODE','node'),'scripts/build-pages.mjs','--base',base],ROOT)
def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('command',nargs='?',default='check',choices=['check','content','pdf','site','all']);parser.add_argument('--base',default='/GridGuard-Agentic-AI-Tutorials/');args=parser.parse_args()
 if args.command=='check':validate(check_pdfs=True)
 elif args.command=='content':content()
 elif args.command=='pdf':pdf()
 elif args.command=='site':site(args.base)
 else:pdf();site(args.base)
if __name__=='__main__':
 try:main()
 except (ValueError,subprocess.CalledProcessError) as error:
  print('Workshop build stopped:',error,file=sys.stderr);sys.exit(1)
