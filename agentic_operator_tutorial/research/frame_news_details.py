"""Show the exact short agentic requirement from Eversource's original vacancy."""
from pathlib import Path
from PIL import Image
from reportlab.pdfgen.canvas import Canvas
import base64,json,hashlib
ROOT=Path(__file__).resolve().parent.parent;IMAGES=ROOT/'images'
original=IMAGES/'real_news_eversource_agentic_requirement.png'
x,y,w,h=0,48,490,28
stem='real_news_eversource_agentic_line'
data=base64.b64encode(original.read_bytes()).decode('ascii')
(IMAGES/(stem+'.svg')).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="{x} {y} {w} {h}"><image x="0" y="0" width="1240" height="76" href="data:image/png;base64,{data}"/></svg>',encoding='utf-8')
c=Canvas(str(IMAGES/(stem+'.pdf')),pagesize=(w,h))
c.drawImage(str(original),-x,y+h-76,width=1240,height=76);c.showPage();c.save()
p=IMAGES/'power_real_news_manifest.json';m=json.loads(p.read_text(encoding='utf-8'))
r=next(i for i in m if i['file']==original.name).copy()
r.update(file=stem+'.svg',original_file=original.name,width=w,height=h,
  caption='Original Eversource requirement: Integration of agentic and AI-based workflows in MATLAB.',
  transformation='Viewport selects the single complete agentic-workflow requirement from the original source-element screenshot. Original image bytes retained unchanged.',
  sha256=hashlib.sha256((IMAGES/(stem+'.svg')).read_bytes()).hexdigest())
m=[v for v in m if v['file']!=r['file']]+[r]
p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
