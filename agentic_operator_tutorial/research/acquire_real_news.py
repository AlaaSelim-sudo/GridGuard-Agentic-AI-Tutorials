"""Acquire genuine official news-page screenshots and original source assets.

No news cards are reconstructed. Browser captures use original live DOM/CSS and
viewport clipping only. PDF captures use original published pages and Poppler.
Run with bundled Python; Chrome, Node, Playwright and Poppler paths can be set
with NEWS_CHROME, NEWS_NODE, NEWS_PLAYWRIGHT and NEWS_PDFTOPPM.
"""
from pathlib import Path
from urllib.request import Request, urlopen
import hashlib
import json
import os
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parents[1]
PACKAGES = ROOT / 'diagrams' / '_rigorous_build' / 'pythonpackages'
sys.path.insert(0, str(PACKAGES))
from PIL import Image

RUNTIME = Path.home() / '.cache' / 'codex-runtimes' / 'codex-primary-runtime' / 'dependencies'
NODE = os.environ.get('NEWS_NODE', str(RUNTIME / 'node' / 'bin' / 'node.exe'))
PLAYWRIGHT = os.environ.get('NEWS_PLAYWRIGHT', str(RUNTIME / 'node' / 'node_modules' / 'playwright'))
CHROME = os.environ.get('NEWS_CHROME', 'C:/Program Files/Google/Chrome/Application/chrome.exe')
PDFTOPPM = os.environ.get('NEWS_PDFTOPPM', str(RUNTIME / 'native' / 'poppler' / 'Library' / 'bin' / 'pdftoppm.exe'))
OUT = ROOT / 'images'
OUT.mkdir(exist_ok=True)
SOURCES = json.loads((ROOT / 'research' / 'source_map.json').read_text(encoding='utf-8'))
ACCESSED = '2026-10-18'

CASES = [
 dict(file='real_news_pjm_hyperq_header.png', mode='web', ref='N01', slides=[9], height=820,
      credit='Tapestry, HyperQ Field Notes, June 11, 2026',
      caption='Original Tapestry field-notes header and a still of its published animated hero, reporting HyperQ use in PJM Cycle 1.',
      evidence_limit='Supplier report of deployment. PJM separately confirmed earlier testing. The hero is a still captured from the publisher\'s animation, not an independently verified live PJM application record.'),
 dict(file='real_news_pjm_customer_header.png', mode='web', ref='N06', slides=[9], height=780,
      credit='PJM Interconnection, Inside Lines, March 16, 2026',
      caption='Original PJM customer news page about interconnection reforms and HyperQ testing.',
      evidence_limit='Customer report of testing in March 2026. Do not use this earlier page as evidence for later supplier runtime results.'),
 dict(file='real_news_hyperq_performance.png', mode='image', ref='N01', slides=[10],
      direct='https://cdn.sanity.io/images/bhywzdze/production/ee934ed00f306c6f3c2d0b5a92ab78dcb6278584-1257x651.png',
      credit='Tapestry, HyperQ Field Notes, June 11, 2026',
      caption='Original Tapestry performance infographic for HyperQ site-control processing.',
      evidence_limit='Supplier-reported computational timing excludes document transfer, human validation and final determinations. 9,312 assessments are not applications.'),
 dict(file='real_news_caiso_header.png', mode='web', ref='C01', slides=[11], height=820,
      credit='California ISO, Energy Matters, July 28, 2025',
      caption='Original California ISO article introducing its AI pilot with OATI.',
      evidence_limit='The customer page describes the July 2025 pilot. OATI C02 supplies the later 2026 production and batch-processing claims.'),
 dict(file='real_news_duke_aws_header.png', mode='web', ref='U02', slides=[12], height=820,
      credit='Amazon Web Services, announcement, September 17, 2026',
      caption='Original AWS announcement naming Duke Energy in its Agentic Grid Planning program.',
      evidence_limit='Reported planning-study coordination and preparation benefit. No exact final-hour count, disclosed runtime stack or live grid-control deployment follows from this header.'),
 dict(file='real_news_siemens_gridscale_header.png', mode='web', ref='N03', slides=[13], height=820,
      credit='Siemens AG, press release, May 5, 2026',
      caption='Original Siemens press release announcing agentic transmission-planning capabilities.',
      evidence_limit='Product announcement. The separately named Alliander platform migration does not prove production use of the new agentic PSS E capability.'),
 dict(file='real_news_national_grid_transcript.png', mode='pdf', ref='N04', slides=[14], page=1,
      credit='National Grid, Full Year Results 2025/26 webcast transcript, May 14, 2026',
      caption='Original National Grid results-transcript cover identifying the corporate disclosure.',
      evidence_limit='The capital-control-tower discussion occurs later in the transcript, PDF p.10. Cover identifies the source and is not itself an agent workflow or measured result.'),
 dict(file='real_news_nypa_ataccama_header.png', mode='web', ref='N09', slides=[15], height=900,
      credit='Ataccama, original webinar report with NYPA Data Quality Lead Saptaparna Gupta, October 14, 2026',
      caption='Original Ataccama webinar page discussing NYPA data-quality gates and a separate Genie/MCP demonstration.',
      evidence_limit='NYPA discusses meter-data quality checks. The separate product/reorder demo does not establish a production NYPA grid-control agent.'),
 dict(file='real_news_eversource_job_header.png', mode='web', ref='N07', slides=[16], height=800,
      credit='Eversource Energy, official engineering vacancy, October 5, 2026',
      caption='Original Eversource engineering vacancy naming distribution-system modeling and automation.',
      evidence_limit='Engineering skill requirement and integration intent. The posting later explicitly mentions agentic MATLAB workflows, but a vacancy does not prove deployment.'),
 dict(file='real_news_eversource_mathworks_header.png', mode='web', ref='N11', slides=[16], height=840,
      credit='MathWorks, named Eversource engineering collaboration, April 29, 2025',
      caption='Original MathWorks report on Eversource probabilistic-load-flow automation.',
      evidence_limit='Conventional MATLAB/Synergi numerical automation. Any simulation-time improvement must not be relabeled an agentic-AI outcome.'),
 dict(file='real_news_ge_vernova_header.png', mode='web', ref='C07', slides=[17], height=850,
      credit='GE Vernova, GridOS for Distribution announcement, February 3, 2026',
      caption='Original GE Vernova GridOS for Distribution announcement naming Alabama Power.',
      evidence_limit='Grid platform/customer context. It does not establish a specific autonomous LLM controller or isolate an agent-caused reliability benefit.'),
 dict(file='real_news_pjm_control_room_facts.png', mode='pdf', ref='O01', slides=[18], page=1,
      credit='PJM Interconnection, What Happens in the Control Room fact sheet, April 16, 2026',
      caption='Original PJM fact sheet showing the work and responsibilities of a real grid control room.',
      evidence_limit='Operator-role context. PJM control-room facts and the PNNL 20-operator survey Q01 are separate sources and populations.'),
]

# Tight source-preserving display crops. Omit inaccessible sources rather than
# reconstructing their headers. The Siemens PDF is linked by its original page.
CASES = [c for c in CASES if c['ref'] not in {'N04', 'N11'}]
ADJUST = {
 'N01': dict(height=880, from_top=True),
 'N06': dict(height=1000, from_top=True, crop=[150, 0, 1290, 620]),
 'C01': dict(height=900, from_top=True, crop=[0, 0, 1440, 660]),
 'U02': dict(crop=[70, 0, 1080, 500]),
 'N03': dict(mode='pdf', page=1, crop=[0, 0, 1273, 485], direct='https://assets.new.siemens.com/siemens/assets/api/uuid:fb613ac9-42b5-4e56-85be-0881ab9e95b8/HQSIPR202604177385EN.pdf'),
 'N09': dict(height=1000, from_top=True, crop=[100, 110, 840, 950]),
 'N07': dict(height=1000, from_top=True, crop=[0, 0, 1440, 875]),
 'C07': dict(height=1000, from_top=True, crop=[40, 0, 1080, 510]),
}
for case in CASES:
    if case['ref'] in ADJUST and case['mode'] != 'image':case.update(ADJUST[case['ref']])
CASES.extend([
 dict(file='real_news_eversource_agentic_requirement.png',mode='web',ref='N07',slides=[16],height=1000,
      target_text='Integration of agentic and AI-based workflows in MATLAB',element_capture_parent=True,
      credit='Eversource Energy, official engineering vacancy, October 5, 2026',
      caption='Original Eversource job requirements explicitly include agentic MATLAB workflows.',
      evidence_limit='Advertised engineering skills. This is hiring/integration intent, not proof of a production agent platform.'),
 dict(file='real_news_pjm_control_room_photo.png',mode='pdf',ref='O01',slides=[18],page=1,crop=[163, 356, 770, 729],
      credit='PJM Interconnection, official control-room fact sheet, April 16, 2026',
      caption='Original PJM control-room photograph from the operator fact sheet.',
      evidence_limit='Real operator context. The photograph does not depict a PNNL survey participant or an agent deployment.'),
])

JAVASCRIPT = r'''
const {chromium} = require(process.env.NEWS_PLAYWRIGHT);
const fs = require('fs');
(async()=>{
 const input=JSON.parse(fs.readFileSync(0,'utf8'));
 const browser=await chromium.launch({headless:true,executablePath:process.env.NEWS_CHROME});
 const output=[];
 async function acquire(item){
  let context,page;
  try{
   context=await browser.newContext({viewport:{width:1440,height:item.height},deviceScaleFactor:1,locale:'en-US'});
   page=await context.newPage();
   const response=await page.goto(item.url,{waitUntil:'domcontentloaded',timeout:55000});
   await page.waitForTimeout(1800);
   await Promise.race([page.evaluate(()=>document.fonts.ready),page.waitForTimeout(3000)]);
   const reject=page.getByRole('button',{name:/^(Reject all|Reject All|Decline all|Decline All|Reject optional cookies)$/});
   if(await reject.count())try{await reject.first().click({timeout:1000});}catch{}
   const title=await page.title();
   const h1s=await page.locator('h1').allTextContents();
   if(!response||response.status()>=400||/access denied|just a moment|not available|page not found/i.test(title))throw Error(`Blocked or missing source: ${response?.status()} ${title}`);
   let main=page.locator('h1').filter({hasText:item.headingNeedle||/.+/}).first();
   if(item.target_text){
    await page.getByRole('link',{name:'Job Description',exact:true}).first().click();
    await page.waitForTimeout(800);
    const candidates=page.getByText(item.target_text,{exact:true});
    let found=false;
    for(let j=0;j<await candidates.count();j++)if(await candidates.nth(j).isVisible()){main=candidates.nth(j);found=true;break;}
    if(!found)throw Error('Required published job-description text is not visible');
   }
   let box=await main.boundingBox();
   if(!box)box={x:0,y:0,width:1440,height:100};
   // Scroll only; do not edit DOM, CSS, article text, imagery or page layout.
   const currentY=await page.evaluate(()=>window.scrollY);
   const y=item.from_top?0:Math.max(0,Math.floor(box.y+currentY-(item.target_text?220:150)));
   await page.evaluate(v=>window.scrollTo(0,v),y);
   await page.waitForTimeout(500);
   if(item.element_capture_parent){
    // Anchor navigation uses smooth scrolling. Playwright waits for the genuine
    // source element to settle before capturing its original two-bullet list.
    await main.scrollIntoViewIfNeeded();
    await page.waitForTimeout(1200);
    await main.locator('..').screenshot({path:item.path,animations:'disabled'});
   }else await page.screenshot({path:item.path,animations:'disabled'});
   output.push({file:item.file,ok:true,title,headings:h1s,url:page.url(),http_status:response.status(),capture_type:item.element_capture_parent?'Original source element screenshot':'Original webpage viewport screenshot',crop:item.element_capture_parent?null:{x:0,y,width:1440,height:item.height},viewport:{width:1440,height:item.height},locator:item.element_capture_parent?'Job Description: original two-item MATLAB engineering-skills list, including the explicit agentic-workflow requirement':'Original website headline and surrounding masthead/date/hero region'});
  }catch(error){output.push({file:item.file,ok:false,error:String(error)});}
  finally{if(context)await context.close();}
 }
 for(let i=0;i<input.length;i+=3)await Promise.all(input.slice(i,i+3).map(acquire));
 await browser.close();
 process.stdout.write(JSON.stringify(output));
})().catch(e=>{console.error(e);process.exit(1)});
'''

def download(url):
    req=Request(url,headers={'User-Agent':'Mozilla/5.0'})
    with urlopen(req,timeout=75) as response:
        return response.read()

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    web=[]
    for case in CASES:
        if case['mode']=='web':
            web.append(dict(file=case['file'],url=SOURCES[case['ref']]['url'],path=str(OUT/case['file']),height=case['height'],from_top=case.get('from_top',False),target_text=case.get('target_text'),element_capture_parent=case.get('element_capture_parent',False)))
    env=dict(os.environ,NEWS_PLAYWRIGHT=PLAYWRIGHT,NEWS_CHROME=CHROME)
    run=subprocess.run([NODE,'-e',JAVASCRIPT],input=json.dumps(web),text=True,encoding='utf-8',capture_output=True,env=env,timeout=360)
    if run.returncode:
        raise RuntimeError(run.stderr)
    results={x['file']:x for x in json.loads(run.stdout)}
    manifest=[]
    with tempfile.TemporaryDirectory(prefix='codex_real_news_') as td:
        for case in CASES:
            path=OUT/case['file']
            source=SOURCES[case['ref']]
            mode=case['mode']
            record=dict(file=case['file'],source_refs=[case['ref']],suggested_slides=case['slides'],source_page_url=source['url'],
                        credit=case['credit'],caption=case['caption'],evidence_limit=case['evidence_limit'],accessed_date=ACCESSED,
                        source_title=source['title'],license_or_permission_status='Original publisher content. No explicit open-reuse license independently verified. Attribution records the source and does not assert permission.',
                        visually_inspected=False)
            try:
                if mode=='web':
                    result=results[case['file']]
                    if not result['ok']:
                        print(json.dumps(result));continue
                    record.update(asset_type='Genuine browser screenshot of original official source page',direct_image_url=None,
                                  transformation='Viewport crop of the live original webpage only. No text reconstruction, added labels, retouching, content changes or synthetic card.',
                                  source_locator=result['locator'],capture=result)
                    if case.get('element_capture_parent'):
                        record.update(asset_type='Genuine browser element screenshot of original published job requirements',
                                      transformation='Original two-item MATLAB skills list captured directly from the published webpage. No text reconstruction, added labels, padding, retouching or content changes.')
                elif mode=='image':
                    payload=download(case['direct']);path.write_bytes(payload)
                    record.update(asset_type='Unmodified original publisher performance infographic',direct_image_url=case['direct'],
                                  transformation='None. Original downloaded PNG bytes preserved.',source_locator='HyperQ site-control performance / original inline infographic')
                else:
                    pdf_url=case.get('direct',source['url'])
                    payload=download(pdf_url);pdf=Path(td)/(case['ref']+'.pdf');pdf.write_bytes(payload)
                    prefix=Path(td)/case['file'].removesuffix('.png')
                    subprocess.run([PDFTOPPM,'-f',str(case['page']),'-singlefile','-scale-to','1800','-png',str(pdf),str(prefix)],check=True,capture_output=True)
                    path.write_bytes(prefix.with_suffix('.png').read_bytes())
                    record.update(asset_type='Faithful rendering of original official PDF page',direct_image_url=pdf_url,
                                  transformation='Original PDF page rendered by Poppler at aspect-preserving 1800px maximum dimension. No content edited.',
                                  source_locator=f'Original PDF page {case["page"]}',source_pdf_sha256=hashlib.sha256(payload).hexdigest())
                if 'crop' in case:
                    with Image.open(path) as original:
                        box=tuple(case['crop'])
                        box=(box[0],box[1],min(box[2],original.width),min(box[3],original.height))
                        record['uncropped_dimensions']=[original.width,original.height]
                        record['uncropped_capture_sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
                        cropped=original.crop(box)
                    cropped.save(path)
                    record['pixel_crop_box']=list(box)
                    record['transformation']+=' Source-preserving rectangular pixel crop '+str(list(box))+'. Original text/image pixels unchanged; omitted surrounding page body, form or cookie-consent areas.'
                with Image.open(path) as im:
                    record.update(width=im.width,height=im.height,aspect_ratio=im.width/im.height)
                record['sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
                manifest.append(record)
                print(case['file'],record['width'],record['height'])
            except Exception as exc:
                print('FAILED',case['file'],str(exc))
    (OUT/'power_real_news_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Manifest entries',len(manifest))

if __name__=='__main__':main()
