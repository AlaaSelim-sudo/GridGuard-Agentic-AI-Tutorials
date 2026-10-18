"""Enlarge the original webinar artwork so the NYPA speaker is readable."""
from pathlib import Path
from reportlab.pdfgen.canvas import Canvas
import base64,json,hashlib
ROOT=Path(__file__).resolve().parent.parent;IMAGES=ROOT/'images'
original=IMAGES/'real_news_nypa_ataccama_header.png'
x,y,w,h=35,439,674,378
stem='real_news_nypa_webinar_detail'
data=base64.b64encode(original.read_bytes()).decode('ascii')
(IMAGES/(stem+'.svg')).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="{x} {y} {w} {h}"><image x="0" y="0" width="740" height="840" href="data:image/png;base64,{data}"/></svg>',encoding='utf-8')
c=Canvas(str(IMAGES/(stem+'.pdf')),pagesize=(w,h));c.drawImage(str(original),-x,y+h-840,width=740,height=840);c.showPage();c.save()
p=IMAGES/'power_real_news_manifest.json';m=json.loads(p.read_text(encoding='utf-8'))
r=next(i for i in m if i['file']==original.name).copy()
r.update(file=stem+'.svg',original_file=original.name,width=w,height=h,
  caption='Original Ataccama webinar artwork names NYPA’s data-quality lead, 14 October 2026.',
  transformation='Viewport-only excerpt of the original webinar artwork. Page heading/date remain in the retained original screenshot; no artwork text or portraits changed.',
  sha256=hashlib.sha256((IMAGES/(stem+'.svg')).read_bytes()).hexdigest())
m=[i for i in m if i['file']!=r['file']]+[r]
p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
