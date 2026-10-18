"""Acquire unmodified original static HyperQ assets for visual review."""
from pathlib import Path
from urllib.request import Request, urlopen
import hashlib
import json
import shutil
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
TEMP = ROOT.parents[1] / 'tmp' / 'operator_tutorial'
TEMP.mkdir(parents=True, exist_ok=True)
CANDIDATES = {
    'hyperq_candidate_summary': 'https://cdn.sanity.io/images/bhywzdze/production/ee934ed00f306c6f3c2d0b5a92ab78dcb6278584-1257x651.png',
    'hyperq_candidate_report': 'https://cdn.sanity.io/images/bhywzdze/production/0c21c14ffa7bb92404856d42e4af8350ac596979-1994x1729.png',
    'hyperq_candidate_agents': 'https://cdn.sanity.io/images/bhywzdze/production/6938a86df3687b0a96a951e8dcf1dbb08b31a7f6-2010x2915.png',
}
for name, url in CANDIDATES.items():
    target = TEMP / (name + '.png')
    if not target.exists():
        with urlopen(Request(url, headers={'User-Agent':'Mozilla/5.0'}), timeout=45) as response:
            payload = response.read()
        target.write_bytes(payload)
    with Image.open(target) as picture:
        picture.verify()
    with Image.open(target) as picture:
        print(name, picture.size, target.stat().st_size)

SELECTED = [
    {
        'candidate':'hyperq_candidate_summary',
        'file':'power_news_hyperq_dashboard.png',
        'credit':'Tapestry, HyperQ field notes, June 11, 2026',
        'source_page_url':'https://www.tapestryenergy.com/en/projects/field-notes-hyperq-deployment-in-pjm-s-cycle-1',
        'direct_image_url':CANDIDATES['hyperq_candidate_summary'],
        'asset_type':'Original publisher site-control performance infographic; not an application-report screenshot',
        'evidence_limit':'Supplier-reported deployment metrics. Processing time excludes document transmission and human validation. 9,312 macro-assessments are not 9,312 applications.',
        'source_refs':['N01'],
        'caption':'Original Tapestry performance dashboard for HyperQ site-control processing. Computational timing excludes transmission and human validation.',
    },
    {
        'candidate':'hyperq_candidate_agents',
        'file':'power_news_hyperq_agents.png',
        'credit':'Tapestry, HyperQ technical white paper, Figure B',
        'source_page_url':'https://www.tapestryenergy.com/en/projects/how-agentic-ai-can-help-grid-operators-speed-up-interconnection',
        'direct_image_url':CANDIDATES['hyperq_candidate_agents'],
        'asset_type':'Original publisher agent workflow diagram',
        'evidence_limit':'Conceptual product workflow illustration, not a photograph, live control-room screen or measured correctness result. The 6,000-page tariff label belongs to the publisher illustration.',
        'source_refs':['N02'],
        'caption':'Original HyperQ workflow: agents inspect application, tariff and supporting-document evidence before presenting readiness assessments to an engineer.',
    },
]
OUT = ROOT / 'images'
OUT.mkdir(exist_ok=True)
manifest=[]
for record in SELECTED:
    candidate=TEMP/(record.pop('candidate')+'.png')
    target=OUT/record['file']
    shutil.copyfile(candidate,target)
    with Image.open(target) as picture:
        record['width'],record['height']=picture.size
        record['original_aspect_ratio']=picture.width/picture.height
    record['transformation']='None: original static PNG bytes, unmodified; no cropping, resizing, retouching, or GIF-frame conversion.'
    record['license']='No explicit open-reuse license stated on source page; original publisher asset with Tapestry attribution.'
    record['license_url']=None
    record['downloaded_on']='2026-10-17'
    record['sha256']=hashlib.sha256(target.read_bytes()).hexdigest()
    record['visually_inspected']=True
    manifest.append(record)
(OUT/'power_news_manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('Saved two original static PNGs and power_news_manifest.json')
