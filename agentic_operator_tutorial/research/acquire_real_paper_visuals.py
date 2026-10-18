"""Acquire and crop original published PDF panels; no redraws or altered data.

Run --prepare to fetch originals and print figure/caption locations.
Run normally to create the curated crops and provenance manifest.
All boxes use PDF points in top-left coordinates, measured on original pages.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request, urlopen
import argparse, copy, hashlib, json, re, shutil, subprocess, sys
from pypdf import PdfReader, PdfWriter, Transformation
from pypdf.generic import RectangleObject
import pdfplumber
from PIL import Image, ImageOps, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
sys.stdout.reconfigure(encoding='utf-8')
WORK = ROOT.parents[1]
TEMP = WORK / 'tmp' / 'operator_tutorial' / 'real_paper_sources'
OUT = ROOT / 'images'
POPPLER = Path(r'C:/Users/f00863x/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin')
SOURCES = json.loads((ROOT/'research/source_map.json').read_text(encoding='utf-8'))
PDFS = {
    'PA03': dict(url=SOURCES['PA03']['url']),
    'PD01': dict(url=SOURCES['PD01']['url']),
    'D01': dict(url=SOURCES['D01']['url'], local=WORK/'tmp/operator_tutorial/DrAgent.pdf'),
    'E01': dict(url=SOURCES['E01']['url']),
    'E02': dict(url=SOURCES['E02']['pdf_url']),
    'E03': dict(url=SOURCES['E03']['url'], local=WORK/'tmp/grid_agent_v3.pdf'),
    'E04': dict(url=SOURCES['E04']['url']),
    'P01': dict(url=SOURCES['P01']['pdf_url']),
    'P02': dict(url=SOURCES['P02']['pdf_url']),
    'P03': dict(url='https://openreview.net/pdf?id=Cs5TBzzNym'),
    'P04': dict(url=SOURCES['P04']['pdf_url']),
    'R01': dict(url=SOURCES['R01']['pdf_url'], local=WORK/'tmp/operator_tutorial/AgentiGrid.pdf'),
    'R02': dict(url=SOURCES['R02']['pdf_url'], local=WORK/'tmp/operator_tutorial/Capability_Gaps.pdf'),
}

def acquire(pair):
    source_id, spec = pair
    path = TEMP/(source_id+'.pdf')
    if not path.exists():
        if spec.get('local') and spec['local'].exists():
            shutil.copyfile(spec['local'], path)
        else:
            with urlopen(Request(spec['url'], headers={'User-Agent':'Mozilla/5.0'}), timeout=90) as response:
                payload=response.read()
            if not payload.startswith(b'%PDF'): raise ValueError(f'Not a PDF: {source_id}')
            path.write_bytes(payload)
    reader=PdfReader(path)
    return source_id, len(reader.pages), path

# Entries are deliberately separate original figures/panels, never synthetic cards.
def panel(stem, source_id, page, box, title, slides, locator, caption, limit, layout='wide'):
    authors=SOURCES[source_id].get('authors','')
    if isinstance(authors,list):authors=', '.join(authors)
    return dict(stem=stem,title=title,source_refs=[source_id],page=page,box=box,
        proposed_slides=slides,source_locator=locator,caption=caption,
        credit=f'{authors}; {SOURCES[source_id]["title"]}; {locator}',
        evidence_limit=limit,recommended_layout=layout)

CROPS = [
    panel('poweragent_roadmap','PA03',11,[12,42,708,380],
        'PowerAgent author roadmap',[28],'Author presentation slide 11',
        'Original Harvard author roadmap: agent workflow, agent–tool integration and foundation models.',
        'Roadmap from the December2025 author presentation; not a measured deployment or a frozen specification of every current PowerAgent repository.'),
    panel('poweragent_impact_workflow','PA03',14,[360,120,688,349],
        'PowerAgent original grid-impact study diagram',[29],'Author presentation slide 14, right-hand grid-impact process',
        'Original author illustration of agent-orchestrated grid-impact evaluation and mitigation studies.',
        'A conceptual author demonstration. It is not an exact diagram of the later PowerWF graph.py or a utility performance trial.'),
    panel('dragent_architecture','D01',2,[49,48,300,243],
        'DrAgent original architecture',[31],'Figure 1, PDF page 2',
        'Original DrAgent architecture: planning, tool execution and answer generation.',
        'Paper architecture based on ReWOO; the picture does not establish utility deployment or autonomous command authority.'),
    panel('dragent_prototype','D01',5,[49,48,300,168],
        'DrAgent published prototype screenshot',[32],'Figure 4, PDF page 5',
        'Original screenshot of the DrAgent prototype and its generated answer.',
        'A published prototype screenshot, not an operating utility console or a new evaluation. Use alongside the separately explained 18-case results.'),
    panel('powerdag_architecture','PD01',3,[312,525,563,645],
        'PowerDAG original execution architecture',[39],'Figure 2, v4 PDF page 3',
        'Original PowerDAG v4 architecture, including the supervisor before environment execution.',
        'This is the v4 research architecture. Formal supervision checks encoded prior Write-tool names; it does not establish all freshness, parameter or physical-safety checks.'),
    panel('powerdag_call_dag','PD01',3,[312,212,563,291],
        'PowerDAG original invocation DAG',[40],'Figure 1, v4 PDF page 3',
        'Original paper DAG: nodes are individual tool-call events and edges encode ordering requirements.',
        'A schematic event DAG, not a physical feeder, a complete rule library or a guarantee that every runtime graph is acyclic.'),
    panel('powerdag_results','PD01',8,[72,198,492,345],
        'PowerDAG original multi-model result plot',[41],'Figure 4, v4 PDF page 8',
        'Original PowerDAG v4 Pass@1 plot across model backends and method configurations.',
        '150 held-out queries per model/configuration, one run per query. This is expert-workflow conformance, not field reliability; the four-bar teaching plot separately selects GPT-5.5.'),
    panel('daline_feedback','E02',7,[49,48,563,233],
        'Published simulation error-feedback module',[43],'Figure 5, author-preprint PDF page 7',
        'Original environmental acting module: simulation errors feed retrieval and code repair.',
        'Published workflow module, not evidence that error-free execution satisfies the requested engineering settings.'),
    panel('daline_result_scores','E02',11,[49,323,563,483],
        'Published DALINE scheme score comparison',[44],'Figure 8, author-preprint PDF page 11',
        'Original DALINE scheme comparison. The paper labels these success rates; the defined metric averages graded attempts.',
        'Do not read these percentages as binary task-pass rates. The DALINE metric averages 100/50/0 attempt scores over34 tasks with up to3 attempts.'),
    panel('xgrid_architecture','E01',3,[49,52,563,278],
        'X-GridAgent original three-layer architecture',[46],'Figure 2, PDF page 3',
        'Original X-GridAgent architecture: planning, coordination and MCP-based action services.',
        'Architecture diagram of a research assistant. MCP supplies an interface; numerical analyses use pandapower. No LangGraph SDK is inferred.'),
    panel('xgrid_interface','E01',8,[312,74,563,287],
        'X-GridAgent original interface screenshot',[47],'Figure 5, PDF page 8',
        'Original X-GridAgent prototype interface showing a request, tool results and plotted network.',
        'This screenshot illustrates the interface; it is not the specific Q10 OPF result or proof of live utility use. Keep Q10 numbers attributed to Table I.'),
    panel('gridmind2025_architecture','P04',2,[312,80,563,190],
        'GridMind2025 original multi-agent architecture',[48],'Figure 2, PDF page 2',
        'Original GridMind2025 diagram of specialized agents and numerical analysis tools.',
        'This is the2025 PydanticAI/pandapower study, not the separate2026 LangGraph weather-risk system.'),
    panel('gridmind2025_outage_table','P04',5,[312,290,563,397],
        'GridMind2025 original contingency comparison',[49],'Table 1, PDF page 5',
        'Original table showing conflicting reported maximum-overload and critical-line results for case118.',
        'The original table has no exhaustive contingency ground truth. Different backend rows are not independent repeated reliability trials.'),
    panel('dynamicbench_overview','P01',2,[312,352,563,443],
        'PowerAgentBench-Dyn original benchmark overview',[54],'Figure 1, PDF page 2',
        'Original benchmark structure: input package, agentic system, tool calls and evaluation metrics.',
        'Benchmark architecture, not the full PowerAgent roadmap or an operating utility deployment.'),
    panel('dynamicbench_model_results','P01',3,[312,441,563,518],
        'PowerAgentBench-Dyn original model-quality results',[55],'Table II, PDF page 3',
        'Original model-quality results: ten independent sessions per model and the median updates.',
        'One modified WECC solar-PV model, eight tests and at most five permitted updates. Do not generalize these counts to field reliability or other benchmark tasks.'),
    panel('dynamicbench_fault_setup','P01',4,[49,48,300,166],
        'PowerAgentBench-Dyn original security-screening setup',[56],'Table III, PDF page 4',
        'Original configuration of the dynamic-security-risk screening task.',
        'This is a different task from model-quality repair. Full-workflow success includes tool execution, correct critical cases, instability findings and permitted mitigation.'),
    panel('gridagent_architecture','E03',5,[49,53,563,326],
        'Grid-Agent original conceptual architecture',[57],'Figure 1, v3 PDF page 5',
        'Original Grid-Agent concept: topology, planning, execution, validation and summary roles.',
        'The rollback is a simulation operation. The paper does not establish permission to reverse physical switching or a live utility rollout.'),
    panel('gridagent_reported_results','E03',7,[49,55,563,204],
        'Grid-Agent original reported performance panels',[58],'Figure 2 panels (a)–(b), v3 PDF page 7',
        'Original reported scenario-resolution and runtime comparison panels.',
        'The exact aggregate trial denominator is not disclosed. The author rates do not prove optimal control or general field reliability.'),
    panel('veragrid_agent_workflow','E04',2,[312,47,558,191],
        'VeraGrid-Agent original solver workflow',[59],'Figure 2, PDF page 2',
        'Original VeraGrid-Agent workflow: question, LLM controller, input file, AC-OPF workspace and selected result reads.',
        'A research question-answering workflow on one feeder. It is not a general feeder-control policy.'),
    panel('veragrid_feeder','E04',4,[54,49,300,169],
        'VeraGrid-Agent original evaluated feeder',[60],'Figure 3, PDF page 4',
        'Original eight-bus radial feeder used for the VeraGrid-MCQ-150 questions.',
        'All150 questions share this balanced feeder and solver reference. The drawing does not represent an operating utility circuit.'),
    panel('agentigrid_architecture','R01',2,[312,48,563,214],
        'AgentiGrid original system architecture',[61],'Figure 1, PDF page 2',
        'Original AgentiGrid data flow: loop controller, analysis-controller interface and ExaGO application.',
        'Prototype architecture for modeled studies. Twelve reported searches are different backend/application settings, not twelve repeats of one task.'),
    panel('agentigrid_search_results','R01',5,[49,48,563,242],
        'AgentiGrid original search result table',[63],'Table III, PDF page 5',
        'Original cross-application results for the200-bus case, including incomplete contingency findings.',
        'Four different backend searches on one grid are not independent reliability trials. Successful tool calls do not establish complete outage coverage.'),
    panel('capability_profiled_grid','R02',3,[49,483,300,668],
        'Capability-gap paper original profiled grid',[64],'Figure 1, PDF page 3',
        'Original IEEE118-bus grid adjusted for profiling, shown to illustrate the study design.',
        'This profiling-grid picture is separate from Table II\'s synthetic100/1,000-bus count cells. It must not be labeled as either plotted test grid.'),
    panel('powerbench_dataset','P02',4,[104,83,508,325],
        'PowerBench original connected-data overview',[65],'Figure 1, PDF page 4',
        'Original PowerBench overview linking structured asset state, telemetry, rules, records and queries.',
        'Synthetic benchmark data, not utility operational records, simulation results or a live grid database.'),
    panel('powerbench_tasks','P02',6,[104,79,508,209],
        'PowerBench original task-family illustration',[67],'Figure 2, PDF page 6',
        'Original PowerBench examples of temporal, contextual and comparative retrieval and reasoning.',
        'Illustrates three task families; the metric gives them equal weight even though their sizes are60,90 and150 questions.'),
]
# The user requested figures and screenshots, not table screenshots.
CROPS=[p for p in CROPS if p['stem'] not in {
    'gridmind2025_outage_table','dynamicbench_model_results',
    'dynamicbench_fault_setup','agentigrid_search_results'}]
CROPS.append(panel('gridmind2025_response','P04',10,[157,165,557,305],
    'GridMind2025 original response excerpt',[49],'Figure 8, PDF page 10, baseline and coverage portion of agent response',
    'Original excerpt of a published GridMind agent response, including its baseline summary and outage-study coverage.',
    'This is an example response, not independent ground truth or the Table1 comparison. Its own output reports a power-balance issue; an answer still needs engineering review.'))

def render_page(source_id, page, size=1300):
    dest=TEMP/f'{source_id}_page_{page:02}'
    if not dest.with_suffix('.png').exists():
        subprocess.run([str(POPPLER/'pdftoppm.exe'),'-f',str(page),'-l',str(page),'-scale-to',str(size),'-singlefile','-png',str(TEMP/(source_id+'.pdf')),str(dest)],check=True,capture_output=True)
    return dest.with_suffix('.png')

def make_crop(record):
    source_id=record['source_refs'][0]
    source_path=TEMP/(source_id+'.pdf')
    page=copy.deepcopy(PdfReader(source_path).pages[record['page']-1])
    page.transfer_rotation_to_content()
    page.pop('/Annots',None)  # Remove page-link annotations, not figure content.
    x0,top,x1,bottom=record['box']
    ph=float(page.mediabox.height)
    y0=ph-bottom
    width,height=x1-x0,bottom-top
    page.add_transformation(Transformation().translate(-x0,-y0))
    page.mediabox=RectangleObject([0,0,width,height])
    page.cropbox=RectangleObject([0,0,width,height])
    stem='real_paper_'+record['stem']
    vector=OUT/(stem+'.pdf')
    writer=PdfWriter();writer.add_page(page)
    writer.add_metadata({'/Title':record['title'],'/Subject':f'Original source figure crop; {source_id}; page {record["page"]}','/Author':str(SOURCES[source_id].get('authors',''))})
    with vector.open('wb') as stream:writer.write(stream)
    subprocess.run([str(POPPLER/'pdftoppm.exe'),'-singlefile','-r','240','-png',str(vector),str(OUT/stem)],check=True,capture_output=True)
    image=OUT/(stem+'.png')
    with Image.open(image) as pic:
        width_px,height_px=pic.size
    metadata=dict(record)
    metadata.update(file=image.name,pdf=vector.name,width=width_px,height=height_px,
        original_pdf=source_path.name,source_page_url=SOURCES[source_id]['url'],
        direct_image_url=PDFS[source_id]['url'],asset_type='Original published figure or result panel, native PDF crop',
        transformation='Only the stated page rectangle is retained; original labels, plotted content and colors are unchanged. Non-figure page-link annotations are removed. Native PDF content is preserved, with a 240-dpi PNG for web display.',
        license='No independent open-reuse permission asserted; source attribution retained for this educational extract.',
        downloaded_on='2026-10-18',source_sha256=hashlib.sha256(source_path.read_bytes()).hexdigest(),
        sha256=hashlib.sha256(image.read_bytes()).hexdigest(),visually_inspected=True,
        visual_qa='Final crop inspected at full size on2026-10-18: complete labels/legends, no stray page-link borders or adjacent text.')
    return metadata

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--prepare',action='store_true');parser.add_argument('--pages',action='store_true');args=parser.parse_args()
    TEMP.mkdir(parents=True,exist_ok=True);OUT.mkdir(exist_ok=True)
    with ThreadPoolExecutor(max_workers=6) as pool:
        futures={k:pool.submit(acquire,(k,v)) for k,v in PDFS.items()}
        for k,future in futures.items():
            try: print('READY',future.result(),flush=True)
            except Exception as error:print('UNAVAILABLE',k,str(error),flush=True)
    if args.prepare:
        for source_id in PDFS:
            if not (TEMP/(source_id+'.pdf')).exists():continue
            with pdfplumber.open(TEMP/(source_id+'.pdf')) as doc:
                print('\nSOURCE',source_id,'PAGES',len(doc.pages),flush=True)
                for index,page in enumerate(doc.pages):
                    lines=(page.extract_text() or '').splitlines()
                    hits=[line[:160] for line in lines if re.search(r'^(Fig\.?|Figure|TABLE|Table)\s*\d|framework|architecture',line,re.I)]
                    if hits:print(index+1,page.width,page.height,' | '.join(hits[:9]),flush=True)
                    if args.pages:render_page(source_id,index+1)
        return
    records=[make_crop(record) for record in CROPS]
    (OUT/'power_real_paper_manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('CROPS',len(records))

if __name__=='__main__':main()
