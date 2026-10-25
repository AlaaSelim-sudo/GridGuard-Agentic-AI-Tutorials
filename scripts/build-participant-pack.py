"""Package only the current participant notebooks and required support files."""
from pathlib import Path
import ast, hashlib, io, json, re, zipfile

ROOT=Path(__file__).resolve().parents[1]
LAB=ROOT/'agentic_grid_workflow_tutorial'
DEST=ROOT/'participant_downloads/GridGuard-Participant-Labs.zip'
SITE='https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/'
REPO='https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/'
BOOKS=[('Classroom_Labs',''),('Graph_Workflow_Lab','companions/'),('Agent_Trace_and_Latency','companions/')]

def main():
 modules={p.stem:p for p in (LAB/'src').glob('*.py')}
 needed={'classroom_labs','graph_workflow_lab','trace_latency','llama_walkthrough'};todo=list(needed)
 while todo:
  name=todo.pop()
  for n in ast.walk(ast.parse(modules[name].read_text(encoding='utf-8-sig'))):
   if isinstance(n,ast.ImportFrom) and n.level==1 and n.module in modules and n.module not in needed:needed.add(n.module);todo.append(n.module)
 paths=['src/'+name+'.py' for name in sorted(needed|{'__init__'})]
 paths += [p.relative_to(LAB).as_posix() for p in (LAB/'data').rglob('*') if p.is_file()]
 paths += ['models/continuous_sac/actor_numpy.npz','models/continuous_sac/training.json',
  'results/ensemble_voltage_pilot/contexts.json','results/ensemble_voltage_pilot/responses.json','results/ensemble_voltage_pilot/selector_models/linucb_seed_270927.json',
  'results/proposal_complete_workflow.json','results/workshop_run_opendss.json','results/continuous_llama_opendss_20260927T161223523552Z.json',
  'results/workshop_run_lindistflow3.json','results/continuous_llama_lindistflow3_20260927T161120781113Z.json',
  'results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json','results/standard_agent_workflow.json','results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json',
  'results/confirmation.json','results/confirmation_calls.json','figures/graph_runtime_flow.svg','requirements_colab.txt','requirements_colab_graph.txt']
 files={p:(LAB/p).read_bytes() for p in dict.fromkeys(paths)}
 manifest={'main_notebook':'Classroom_Labs.ipynb','notebook_code_unchanged':True,'support_modules':sorted(needed),'source_files':{p:hashlib.sha256(data).hexdigest() for p,data in files.items()},'notebooks':{}}
 for name,folder in BOOKS:
  path=LAB/(name+'.ipynb');nb=json.loads(path.read_text(encoding='utf-8-sig'))
  code_before={c['id']:''.join(c['source']) for c in nb['cells'] if c['cell_type']=='code'}
  for c in nb['cells']:
   if c['cell_type']=='code':c['outputs']=[];c['execution_count']=None
   else:
    text=''.join(c['source']).replace('Instructor answer','Answer check')
    if c['id']=='colab-start':text='# '+('Classroom Labs: three operator cases' if name=='Classroom_Labs' else 'Companion lab')+'\n\nRun from the extracted folder containing src and data. For Colab, open the canonical notebook linked in README.md and run setup.\n'
    if c['id']=='classroom-031':text='### Advanced live-model path\n\nLeave RUN_LOCAL_LLAMA=False for the standard activities. L3, L10 and L10B display the saved model records needed for the workshop.\n'
    def link(m):
     label,target=m.groups()
     if target.startswith(('http','#')) or target in files:return m.group(0)
     return label
    text=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',link,text);c['source']=text.splitlines(keepends=True)
  assert code_before=={c['id']:''.join(c['source']) for c in nb['cells'] if c['cell_type']=='code'}
  target=folder+name+'.ipynb';files[target]=(json.dumps(nb,ensure_ascii=False,indent=1)+'\n').encode()
  manifest['notebooks'][target]={'canonical_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'code_cells':len(code_before),'all_code_cells_preserved':True}
 # The canonical Colab setup remains available in a local extraction as well.
 files['scripts/colab_setup.py']=(ROOT/'scripts/colab_setup.py').read_bytes()
 files['requirements_local.txt']=b'-r requirements_colab.txt\n-r requirements_colab_graph.txt\njupyterlab>=4,<5\nnbformat>=5,<6\nnbclient>=0.10,<1\nipykernel>=6,<8\n'
 files['README.md']=f'''# GridGuard participant labs

**Alaa Selim, MIT/Dartmouth; Mohamed Chehada, UT Austin.**

Start with **Classroom_Labs.ipynb**. It covers all three hands-on cases.

## Run in Colab

[Open Classroom Labs](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb).

Save a Drive copy, connect a CPU runtime, run setup and wait for Ready. Start at L0 and continue through L12, including L10B. Keep RUN_OPENDSS and RUN_LOCAL_LLAMA False. No GPU, API key or language-model download is needed.

## Run locally

1. Extract this folder and create/activate a Python virtual environment.
2. Open a terminal in this folder, where src and data are visible.
3. Run `python -m pip install -r requirements_local.txt`.
4. Run `python -m jupyter lab Classroom_Labs.ipynb`.

## Explore

- Voltage L2-L5: compare proposals and check model limits.
- Restoration L6-L7: compare total and critical load served.
- Cyber L8-L9: compare residual consistency and state error.
- L10-L10B: inspect actual saved agent choices and tool results.
- L12: inspect the simulated recommendation readback.

Change one exercise input at a time and reset before continuing. The two notebooks in companions are separate graph and evidence activities. Start Jupyter from this root folder when opening them.

## Supporting files

src, data, models and results are supporting files; you do not need to edit them. Sources and model limits are documented in the code, records and data/DATA_SOURCE.md. PARTICIPANT_MANIFEST.json identifies the supplied files.

The cases use synthetic or reduced networks. Python makes fresh calculations; saved model replies are labeled separately. L10B makes no new model call or electrical solve. No lab operates equipment. Advanced live-model or OpenDSS paths need separately prepared software and study files.

[Presentations and references]({SITE}) · [Source code]({REPO}).
'''.encode()
 files['PARTICIPANT_MANIFEST.json']=(json.dumps(manifest,indent=2)+'\n').encode()
 DEST.parent.mkdir(exist_ok=True)
 with zipfile.ZipFile(DEST,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
  for name,data in sorted(files.items()):
   if '..' in Path(name).parts or Path(name).is_absolute():raise ValueError('Unsafe archive path')
   info=zipfile.ZipInfo('GridGuard-Participant-Labs/'+name,date_time=(2026,10,25,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;archive.writestr(info,data,compresslevel=9)
 with zipfile.ZipFile(DEST) as archive:
  assert archive.testzip() is None
  assert not any(x.endswith(('.pdf','.tex','.pptx')) or 'Presenter_Script' in x for x in archive.namelist())
 print(json.dumps({'archive':str(DEST),'files':len(files),'compressed_bytes':DEST.stat().st_size,'uncompressed_bytes':sum(map(len,files.values())),'code_cells':sum(x['code_cells'] for x in manifest['notebooks'].values()),'core_code_preserved':True}))
if __name__=='__main__':main()
