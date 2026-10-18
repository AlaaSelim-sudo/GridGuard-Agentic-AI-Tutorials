"""Create credited viewing excerpts, preserving original pixels or native PDF text."""
from pathlib import Path
from copy import deepcopy
import base64, json, subprocess,hashlib
from PIL import Image
from pypdf import PdfReader, PdfWriter, Transformation, PageObject
from reportlab.pdfgen.canvas import Canvas

ROOT=Path(__file__).resolve().parent.parent
IMAGES=ROOT/'images'
POPPLER=r'C:/Users/f00863x/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe'

def record(original,stem,description,manifest,**extra):
    path=IMAGES/manifest
    records=json.loads(path.read_text(encoding='utf-8'))
    entries=records if isinstance(records,list) else records['images']
    found=next((v for v in entries if v['file']==original),None)
    if found is None:
        alternatives=json.loads((IMAGES/'power_disturbance_manifest.json').read_text(encoding='utf-8'))
        found=next(v for v in alternatives if v['file']==original)
    r=deepcopy(found)
    r.update(file=stem,original_file=original,caption=description,
             transformation=description+' Original labels and colors are unchanged. The full source image is included.',**extra)
    r['sha256']=hashlib.sha256((IMAGES/stem).read_bytes()).hexdigest()
    r['pdf']=Path(stem).with_suffix('.pdf').name
    if stem.endswith('.png'):r['width'],r['height']=Image.open(IMAGES/stem).size
    entries[:]=[v for v in entries if v['file']!=stem]+[r]
    path.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def raster_excerpt(original,stem,box,description):
    img=Image.open(IMAGES/original);width,height=img.size
    x,y,w,h=box
    data=base64.b64encode((IMAGES/original).read_bytes()).decode('ascii')
    (IMAGES/(stem+'.svg')).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="{x} {y} {w} {h}"><image width="{width}" height="{height}" href="data:image/png;base64,{data}"/></svg>',encoding='utf-8')
    c=Canvas(str(IMAGES/(stem+'.pdf')),pagesize=(w,h))
    c.drawImage(str(IMAGES/original),-x,y+h-height,width=width,height=height)
    c.showPage();c.save()
    record(original,stem+'.svg',description,'power_real_news_manifest.json',width=w,height=h,crop_viewport=box)

def native_piece(original,box):
    width,height=Image.open(IMAGES/original).size
    page=PdfReader(IMAGES/Path(original).with_suffix('.pdf')).pages[0]
    left,bottom,right,top=map(float,page.cropbox)
    x,y,w,h=box
    l=left+(right-left)*x/width;t=top-(top-bottom)*y/height
    rw=(right-left)*w/width;rh=(top-bottom)*h/height
    piece=PageObject.create_blank_page(width=rw,height=rh)
    page.cropbox.lower_left=(l,t-rh);page.cropbox.upper_right=(l+rw,t)
    page.mediabox=page.cropbox;page.pop('/Annots',None)
    piece.merge_transformed_page(page,Transformation().translate(-l,-t+rh))
    return piece,rw,rh

def native_excerpt(original,stem,box,description):
    page,_,_=native_piece(original,box)
    writer=PdfWriter();writer.add_page(page)
    with (IMAGES/(stem+'.pdf')).open('wb') as f:writer.write(f)
    subprocess.run([POPPLER,'-png','-singlefile','-scale-to','1800',str(IMAGES/(stem+'.pdf')),str(IMAGES/stem)],check=True)
    record(original,stem+'.png',description,'power_real_paper_manifest.json',crop_viewport=box)

def response_excerpts():
    original='real_paper_gridmind2025_response.png';stem='real_paper_gridmind2025_status_detail'
    # Two separate complete status fields. The rest of the long response stays in the full original.
    pieces=[native_piece(original,(0,136,718,22)),native_piece(original,(0,161,580,21))]
    scale=pieces[0][1]/718
    canvas=PageObject.create_blank_page(width=750*scale,height=115*scale)
    for (piece,w,h),y in zip(pieces,(72,25)):
        canvas.merge_transformed_page(piece,Transformation().translate(8*scale,y*scale))
    writer=PdfWriter();writer.add_page(canvas)
    with (IMAGES/(stem+'.pdf')).open('wb') as f:writer.write(f)
    subprocess.run([POPPLER,'-png','-singlefile','-scale-to','1800',str(IMAGES/(stem+'.pdf')),str(IMAGES/stem)],check=True)
    record(original,stem+'.png','Two enlarged original response excerpts: solve status and the opening balance-error warning. Excerpts are separated by white space; the warning continues in the full figure.',
           'power_real_paper_manifest.json',crop_viewports=[[0,136,718,22],[0,161,580,21]])

def disturbance_excerpt():
    original='power_dragent_waveform.png';stem='real_paper_dragent_il3_detail'
    trace,tw,th=native_piece(original,(40,240,960,111))
    axis,aw,ah=native_piece(original,(40,689,960,68))
    scale=tw/960
    page=PageObject.create_blank_page(width=tw,height=190*scale)
    page.merge_transformed_page(trace,Transformation().translate(0,79*scale))
    page.merge_transformed_page(axis,Transformation())
    writer=PdfWriter();writer.add_page(page)
    with (IMAGES/(stem+'.pdf')).open('wb') as f:writer.write(f)
    subprocess.run([POPPLER,'-png','-singlefile','-scale-to','1900',str(IMAGES/(stem+'.pdf')),str(IMAGES/stem)],check=True)
    record(original,stem+'.png','Original DrAgent Figure 2 excerpts: the IL3 current channel and its unchanged corresponding time axis, on the same horizontal scale. Other channels are omitted.',
           'power_real_paper_manifest.json',crop_viewports=[[40,240,960,111],[40,689,960,68]])

if __name__=='__main__':
    raster_excerpt('real_news_pjm_hyperq_header.png','real_news_pjm_headline_detail',(210,145,1020,194),
                   'Original Tapestry article headline excerpt naming HyperQ deployment in PJM Cycle 1.')
    raster_excerpt('real_news_eversource_job_header.png','real_news_eversource_vacancy_detail',(58,630,825,214),
                   'Original Eversource job title, publication date and locations. The employer is identified in the source credit.')
    raster_excerpt('real_news_nypa_ataccama_header.png','real_news_nypa_speaker_detail',(418,675,270,100),
                   'Original webinar speaker-card excerpt retaining Saptaparna Gupta, Data Quality Lead and New York Power Authority.')
    native_excerpt('real_paper_powerbench_dataset.png','real_paper_powerbench_generation_detail',(452,0,885,388),
                   'Original PowerBench Figure 1 excerpt: telemetry synthesis, verification and document generation. Other pipeline stages are outside this excerpt.')
    response_excerpts()
    disturbance_excerpt()
