"""Frame the original Studio review form without changing its pixels."""
from pathlib import Path
from PIL import Image
from reportlab.pdfgen.canvas import Canvas
import base64,json
ROOT=Path(__file__).resolve().parent.parent
IMAGES=ROOT/'images'
original=IMAGES/'real_framework_langgraph_interrupt_form_original.png'
x,y,w,h=80,235,740,355
stem='real_framework_langgraph_review_detail'
data=base64.b64encode(original.read_bytes()).decode('ascii')
(IMAGES/(stem+'.svg')).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="{x} {y} {w} {h}"><image x="0" y="0" width="900" height="800" href="data:image/png;base64,{data}"/></svg>',encoding='utf-8')
c=Canvas(str(IMAGES/(stem+'.pdf')),pagesize=(w,h))
c.drawImage(str(original),-x,y+h-800,width=900,height=800)
c.showPage();c.save()
p=IMAGES/'power_real_framework_manifest.json';m=json.loads(p.read_text(encoding='utf-8'))
r=next(r for r in m['images'] if r['file']=='real_framework_langgraph_interrupt_form.svg').copy()
r.update(file=stem+'.svg',id=stem,width=w,height=h,crop_viewport=[x,y,w,h],
  caption='Original LangGraph Studio review form, focused on the approval response and Resume button.',
  transformation='Viewport-only excerpt of the original approval form. Original image bytes embedded unchanged. Surrounding request and unused page whitespace excluded; no interface values edited.')
m['images']=[v for v in m['images'] if v['file']!=r['file']]+[r]
p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
