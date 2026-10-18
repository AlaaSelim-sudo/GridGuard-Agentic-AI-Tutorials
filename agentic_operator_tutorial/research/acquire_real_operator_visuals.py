"""Retrieve original source visuals; preserve original source bytes beside displays."""
from pathlib import Path
from urllib.request import Request,urlopen
from PIL import Image
from pypdf import PdfReader,PdfWriter
import subprocess,json,hashlib
ROOT=Path(__file__).resolve().parent.parent
IMAGES=ROOT/'images'
TMP=ROOT.parents[1]/'tmp/operator_tutorial/real-source-originals'
TMP.mkdir(parents=True,exist_ok=True)
POPPLER=Path(r'C:/Users/f00863x/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe')
def fetch(url,path):
    if path.exists():return path
    with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=60) as response:
        path.write_bytes(response.read())
    return path
def record(file,refs,page,direct,credit,caption,kind,limit,transformation='Original image; format conversion only where required.'):
    return dict(file=file,source_refs=refs,source_page_url=page,direct_image_url=direct,
        credit=credit,caption=caption,asset_type=kind,evidence_limit=limit,
        transformation=transformation,sha256=hashlib.sha256((IMAGES/file).read_bytes()).hexdigest())
records=[]
source='https://aima.cs.berkeley.edu/4th-ed/pdfs/newchap02.pdf'
paper=fetch(source,TMP/'aima_chapter02.pdf')
subprocess.run([str(POPPLER),'-f','2','-l','2','-png','-scale-to','1600',str(paper),str(TMP/'aima')],check=True)
# Figure 2.1 is cropped from the author's hosted older chapter, printed p.33.
page=PdfReader(paper).pages[1]
page.mediabox.lower_left=(206,518)
page.mediabox.upper_right=(495,700)
page.cropbox=page.mediabox
page.pop('/Annots',None)
writer=PdfWriter();writer.add_page(page)
target=IMAGES/'real_concept_classical_agent.pdf'
with target.open('wb') as stream:writer.write(stream)
subprocess.run([str(POPPLER),'-png','-singlefile','-r','240','-cropbox',str(target),str(target.with_suffix(''))],check=True)
records.append(record('real_concept_classical_agent.png',['DEF01'],source,source,
    'Stuart J. Russell and Peter Norvig, Artificial Intelligence: A Modern Approach, second edition, Chapter 2, Figure 2.1, printed p.33; author-hosted chapter draft.',
    'The textbook agent observes through sensors and acts through actuators. Software agents use software inputs and actions.',
    'Original published textbook figure, native PDF crop',
    'A general agent model, not a utility deployment or an LLM-specific architecture.',
    'Native PDF page clipped around Figure 2.1; no figure labels or connections redrawn.'))
jobs=[
 ('real_ops_frequency','https://www.caiso.com/content/images/blog/blog-graphics/controlcentermodernization-rtdms.webp',
  'https://www.caiso.com/about/news/energy-matters-blog/control-center-modernization-is-enhancing-reliability',['O05'],
  'California ISO, John Phipps, Control center modernization is enhancing reliability, 10 September 2025.',
  'California ISO published oscillation-monitoring screens. These are operator tools, not evidence of an agent deployment.',
  'Original operational software screenshot'),
 ('real_ops_training','https://www.caiso.com/content/images/blog/blog-graphics/training2.webp',
  'https://www.caiso.com/about/news/energy-matters-blog/iso-now-has-expanded-training-and-emergency-operations-facilities',['O03'],
  'California ISO, Tricia Johnstone, ISO now has expanded training and emergency operations facilities, 20 February 2025.',
  'California ISO operator-training facility. The photo provides context for testing an assistant with operators.',
  'Original utility training-facility photograph')]
for stem,url,page,refs,credit,caption,kind in jobs:
    original=fetch(url,IMAGES/(stem+'.webp'))
    Image.open(original).convert('RGB').save(IMAGES/(stem+'.png'))
    records.append(record(stem+'.png',refs,page,url,credit,caption,kind,
        'Context photograph or conventional operator tool; no agent performance or control authority is implied.'))
gen_url='https://www.nvidia.com/content/nvidiaGDC/us/en_US/glossary/generative-ai/_jcr_content/root/responsivegrid/nv_container_871136465/nv_image.coreimg.svg/1787296939413/usecases.svg'
fetch(gen_url,IMAGES/'real_concept_genai_modalities.svg')
records.append(record('real_concept_genai_modalities.svg',['VIS01'],
    'https://www.nvidia.com/en-us/glossary/generative-ai/',gen_url,
    'NVIDIA, What Is Generative AI?, Figure 4: Generative AI use cases; accessed 18 October 2026.',
    'NVIDIA’s published examples show that generated content can include text, audio, code and images.',
    'Original published explanatory illustration',
    'Illustrates output types; it does not define an agent control loop or report utility performance.','Original SVG bytes retained.'))
(IMAGES/'power_real_operator_manifest.json').write_text(json.dumps({'images':records},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'assets':[i['file'] for i in records]}))
