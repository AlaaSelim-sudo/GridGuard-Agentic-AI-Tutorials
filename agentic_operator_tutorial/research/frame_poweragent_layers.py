"""Select the three layer panels from the original author roadmap."""
from pathlib import Path
from pypdf import PdfReader,PdfWriter
import json,subprocess
ROOT=Path(__file__).resolve().parent.parent
IMAGES=ROOT/'images'
original=IMAGES/'real_paper_poweragent_roadmap.pdf'
page=PdfReader(original).pages[0]
box=page.cropbox;left,bottom,right,top=map(float,box)
# Pixels refer to the source display, 2320 x1127. Native PDF crop preserves text.
x,y,w,h=100,5,650,770
newleft=left+(right-left)*x/2320
newright=left+(right-left)*(x+w)/2320
newtop=top-(top-bottom)*y/1127
newbottom=top-(top-bottom)*(y+h)/1127
page.mediabox.lower_left=(newleft,newbottom);page.mediabox.upper_right=(newright,newtop)
page.cropbox=page.mediabox;page.pop('/Annots',None)
writer=PdfWriter();writer.add_page(page)
stem='real_paper_poweragent_three_layers'
with (IMAGES/(stem+'.pdf')).open('wb') as f:writer.write(f)
poppler=r'C:/Users/f00863x/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe'
subprocess.run([poppler,'-png','-singlefile','-cropbox','-scale-to','1500',str(IMAGES/(stem+'.pdf')),str(IMAGES/stem)],check=True)
p=IMAGES/'power_real_paper_manifest.json';m=json.loads(p.read_text(encoding='utf-8'))
records=m if isinstance(m,list) else m['images']
r=next(r for r in records if r['file']=='real_paper_poweragent_roadmap.png').copy()
r.update(file=stem+'.png',original_file='real_paper_poweragent_roadmap.png',
    caption='Original author roadmap excerpt: agentic workflows, agent–tool integration and foundation models.',
    transformation='Native PDF crop selects the three layer panels from the author roadmap. No text or connectors redrawn; the full source figure is retained.',
    source_locator='Author presentation slide 11; three layer panels in the left column')
records[:]=[v for v in records if v['file']!=r['file']]+[r]
p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
