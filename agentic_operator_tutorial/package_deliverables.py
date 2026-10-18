"""Package the integrated teaching edition and verify portable source links."""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
from urllib.parse import urlparse,unquote
import hashlib,json,shutil,os
from pypdf import PdfReader,PdfWriter
from pypdf.generic import TextStringObject
import build_teaching

ROOT=Path(__file__).resolve().parent
build=json.loads((ROOT/'build_manifest.json').read_text(encoding='utf-8'))
assert build['edition']=='power-systems'
assert build['main_slides']==build['core_slides']==80
assert build['minutes']==165 and not build['extension_slides']
assert build['tables']==0 and build['exercise_slides']==[26,53]
assert build['source_image_slide_count']>build['main_slides']/2
assert len(PdfReader(ROOT/'latex/main.pdf').pages)==build['main_slides']
for stem in ('main','reading_guide'):
    log=(ROOT/f'latex/{stem}.log').read_text(encoding='utf-8',errors='replace')
    assert 'Overfull' not in log and 'Missing character' not in log,stem

shutil.copy2(ROOT/'latex/main.pdf',ROOT/'latex/presentation.pdf')
# The same guide is delivered beside the project root and in the web root.
# Rebase the few local URI annotations from the compiler's latex/ directory.
guide=PdfWriter(clone_from=ROOT/'latex/reading_guide.pdf')
for page in guide.pages:
    for annot in page.get('/Annots',[]):
        action=annot.get_object().get('/A')
        if action and str(action.get('/URI','')).startswith('../research/'):
            action[TextStringObject('/URI')]=TextStringObject(str(action['/URI'])[3:])
with (ROOT/'Full_Reading_Guide.pdf').open('wb') as handle:guide.write(handle)
for folder in ('slidev/public','slidev/dist'):
    shutil.copy2(ROOT/'Full_Reading_Guide.pdf',ROOT/folder/'Full_Reading_Guide.pdf')
shutil.copy2(ROOT/'Full_Reading_Guide.html',ROOT/'slidev/dist/Full_Reading_Guide.html')

images=set(build['used_images'])|set(build.get('used_auxiliary_assets',[]))
images.update({'source_anthropic_augmented_llm.png','source_anthropic_autonomous_agent.png'})
all_image_records={item['file']:item for item in build_teaching.combined_image_manifest()['images']}
# Preserve source screenshots/figures behind the selected display viewports.
while True:
    originals={all_image_records.get(name,{}).get('original_file') for name in images}
    originals.discard(None)
    expanded=images|originals
    expanded.update(Path(name).with_suffix('.pdf').name for name in originals
                    if (ROOT/'images'/Path(name).with_suffix('.pdf').name).is_file())
    if expanded==images:break
    images=expanded
brand={'comsoc-lockup.png','image7.png'}
diagrams=set(build['used_diagrams'])|set(build.get('supporting_editable_diagrams',[]))
sources_all=json.loads((ROOT/'research/source_map.json').read_text(encoding='utf-8'))
sources={key:sources_all[key] for key in build['reading_source_ids']}
local_sources=['GridGuard_source_snapshot.txt','Follow_on_workshop_source.txt']
image_manifest={'images':[item for item in build_teaching.combined_image_manifest()['images'] if item['file'] in images]}
diagram_manifest={key:value for key,value in build_teaching.diagram_records().items() if key in diagrams}
stats={}
for pattern in ('rigor_statistics.json','expanded_*_statistics.json','power_*_statistics.json'):
    for file in (ROOT/'images').glob(pattern):stats.update(json.loads(file.read_text(encoding='utf-8')))
stats={key:value for key,value in stats.items() if isinstance(value,dict) and value.get('file') in images}
provenance={'images':image_manifest['images'],'diagrams':diagram_manifest,'quantitative_data':stats}
(ROOT/'visual_provenance.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def portable(text):
    return text.replace('../Full_Reading_Guide.html','Full_Reading_Guide.html').replace('../research/','research/')

def write_json(archive,name,value):
    archive.writestr(name,json.dumps(value,ensure_ascii=False,indent=2)+'\n')

def iter_files(directory):
    for base,dirs,names in os.walk(directory):
        dirs[:]=[name for name in dirs if name not in {'node_modules','__pycache__','_build','_rigorous_build'}]
        for name in names:yield Path(base)/name

research_files={
    'rigor_benchmarks.json','rigor_benchmarks.md',
    'expanded_power.json','expanded_power.md','build_power_plots.py',
    'power_intro_news.json','power_intro_news.md','acquire_power_news_visuals.py',
    'power_only_papers.json','power_only_papers.md','power_only_sources.json',
    'dragent_count_audit.json','build_disturbance_assets.py','build_power_study_plots.py',
    'agent_definitions_revision.json','agent_definitions_revision.md',
    'poweragent_powerdag_revision.json','poweragent_powerdag_revision.md','poweragent_powerdag_sources.json',
    'utility_news_revision.json','utility_news_revision.md','merge_revision_sources.py','build_power_revision_plots.py',
    'visual_revision_plan.json',
    'real_image_slide_plan.json','real_framework_sources.json',
    'acquire_real_news.py','acquire_real_paper_visuals.py','acquire_real_framework_visuals.py',
    'capture_real_framework_diagrams.mjs','acquire_real_operator_visuals.py',
    'frame_review_detail.py','frame_poweragent_layers.py','frame_news_details.py','frame_nypa_webinar.py',
    *local_sources,
}

source=ROOT/'LaTeX_Source.zip'
with ZipFile(source,'w',ZIP_DEFLATED) as archive:
    for file in (ROOT/'latex').glob('*.tex'):
        archive.writestr(file.name,portable(file.read_text(encoding='utf-8')))
    for name in images:archive.write(ROOT/'images'/name,'images/'+name)
    for name in brand:archive.write(ROOT/'branding'/name,'images/'+name)
    for name in diagrams:
        for ext in ('.tex','.svg','.pdf'):
            file=ROOT/'diagrams'/(name+ext)
            if file.exists():archive.write(file,'diagrams/'+file.name)
    for name in ('References.md','Instructor_Guide.md','Full_Reading_Guide.html'):
        archive.writestr(name,portable((ROOT/name).read_text(encoding='utf-8')))
    archive.write(ROOT/'Full_Reading_Guide.pdf','Full_Reading_Guide.pdf')
    archive.write(ROOT/'visual_provenance.json','visual_provenance.json')
    write_json(archive,'research/source_map.json',sources)
    for name in local_sources:archive.write(ROOT/'research'/name,'research/'+name)
    archive.writestr('README.txt',
        '80 slides in one integrated 165-minute route. All slides are part of the session. '
        'Two exercises on slides 26 and 53 (six and eight minutes). No tables, transitions or click reveals. '
        'Compile main.tex and reading_guide.tex. Native TikZ snippets and vector figures are included. '
        'Speaker notes, exercise answers and timing are in Instructor_Guide.md. '
        'Complete paper/source URLs and visual credits are in the separate reading guide. '
        'The next workshop covers voltage support, restoration and cyber response.\n')

complete=ROOT/'Agentic_Operator_Tutorial_Complete.zip'
top_files={'README.md','Instructor_Guide.md','References.md','Full_Reading_Guide.html',
           'Full_Reading_Guide.pdf','visual_provenance.json','lesson_content.json','build_manifest.json',
           'build_tutorial.py','build_teaching.py','build_intro.py','power_content.py',
           'power_retained_content.json','revision_content.py','package_deliverables.py',
           'visual_revision.py','plain_language_1.json','plain_language_2.json','real_image_revision.py'}
with ZipFile(complete,'w',ZIP_DEFLATED) as archive:
    for name in top_files:archive.write(ROOT/name,name)
    write_json(archive,'research/source_map.json',sources)
    for name in research_files:archive.write(ROOT/'research'/name,'research/'+name)
    # Include exactly the visual data used by the current edition.
    write_json(archive,'images/image_manifest.json',image_manifest)
    for file in (ROOT/'images').glob('power_real_*_manifest.json'):
        archive.write(file,'images/'+file.name)
    write_json(archive,'images/rigor_statistics.json',stats)
    write_json(archive,'diagrams/rigor_manifest.json',{'items':list(diagram_manifest.values())})
    write_json(archive,'diagrams/power_graph_manifest.json',{key:value for key,value in diagram_manifest.items() if key.startswith('power_')})
    write_json(archive,'diagrams/revision_graph_manifest.json',{key:value for key,value in diagram_manifest.items() if key.startswith('revision_')})
    for name in ('visual_aid_manifest.json','domain_visual_manifest.json'):
        archive.write(ROOT/'diagrams'/name,'diagrams/'+name)
    for folder in ('branding','images','diagrams','latex','slidev'):
        for file in iter_files(ROOT/folder):
            if not file.is_file():continue
            rel=file.relative_to(ROOT)
            if any(part in {'node_modules','__pycache__','_build','_rigorous_build'} for part in rel.parts):continue
            if file.suffix in {'.aux','.log','.nav','.out','.vrb','.xdv','.snm','.toc','.zip'}:continue
            if folder=='branding' and file.name not in brand:continue
            if folder=='images' and file.name not in images:continue
            if folder=='diagrams' and file.stem not in diagrams and file.name not in {'build_rigorous.py','build_power_graphs.py','build_revision_graphs.py','build_visual_aids.py','build_domain_visuals.py'}:continue
            if folder=='latex' and file.suffix not in {'.tex','.pdf','.svg','.png','.jpg','.jpeg'}:continue
            if 'images' in rel.parts and folder!='images' and file.name not in images|brand:continue
            if 'diagrams' in rel.parts and folder!='diagrams' and file.stem not in diagrams:continue
            if file.name=='intro.css':continue
            archive.write(file,str(rel).replace('\\','/'))

# Validate guide source coverage and relative local annotations after rebasing.
reader=PdfReader(ROOT/'Full_Reading_Guide.pdf')
text=''.join(page.extract_text() for page in reader.pages)
assert all('['+key+']' in text for key in build['reading_source_ids'])
for page in reader.pages:
    for annot in page.get('/Annots',[]):
        action=annot.get_object().get('/A')
        uri=str(action.get('/URI','')) if action else ''
        if uri and not urlparse(uri).scheme:
            assert (ROOT/unquote(uri)).is_file(),uri
for file in (source,complete):
    with ZipFile(file) as archive:assert archive.testzip() is None
with ZipFile(complete) as archive:
    names=set(archive.namelist())
    assert {'power_content.py','power_retained_content.json','slidev/dist/index.html','latex/main.pdf'}<=names
    assert not any('foundation' in name or 'science_plots' in name or name.endswith('expanded_content.py') for name in names)
    assert not any(key.startswith(('F0','H0','H1')) for key in json.loads(archive.read('research/source_map.json')))
with ZipFile(source) as archive:
    names=set(archive.namelist())
    for name in diagrams:assert f'diagrams/{name}.tex' in names and f'diagrams/{name}.svg' in names
    assert r'\begin{tabular}' not in archive.read('frames.tex').decode()

result={key:build[key] for key in ('edition','main_slides','core_slides','minutes','extension_slides','extension_minutes','tables','exercise_slides','reading_sources','click_reveals','transitions','used_diagrams','supporting_editable_diagrams','source_image_slide_count','source_image_slides')}
result.update(reading_guide_pages=len(reader.pages),quantitative_plots=len(stats),files={})
for file in (source,complete,ROOT/'latex/main.pdf',ROOT/'Full_Reading_Guide.pdf',ROOT/'slidev/slides.md'):
    result['files'][str(file.relative_to(ROOT)).replace('\\','/')]={'bytes':file.stat().st_size,'sha256':hashlib.sha256(file.read_bytes()).hexdigest()}
(ROOT/'deliverables.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
