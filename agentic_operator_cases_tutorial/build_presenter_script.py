"""Build the speaker-ready script from authored cues and the current slide order."""
from pathlib import Path
import argparse,hashlib,html,json,shutil
ROOT=Path(__file__).resolve().parent
SITE='https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/'
COLAB='https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb'
LABELS={'opening':'1. Stanford concepts and Colab setup','voltage':'2. Voltage support','restoration':'3. Service restoration','cyber':'4. Cyber response','closing':'5. Llama replay and operator review'}

def load(name):return json.loads((ROOT/name).read_text(encoding='utf-8-sig'))
def stamp(minutes):
 n=round(minutes*60);return f'{n//3600:02}:{n%3600//60:02}:{n%60:02}'
def plain(t):
 for a,b in {'–':'-','—':'-','→':' then ','’':"'",'‘':"'",'“':'"','”':'"','≤':'<=','≥':'>='}.items():t=t.replace(a,b)
 return t

def prepare():
 slides=load('lesson_content.json');authored=load('content/presenter_script.json')['slides']
 cues={x['title']:x for x in authored}
 if len(cues)!=80 or set(cues)!={s['title'] for s in slides}:raise ValueError('Update presenter_script.json for every current slide title.')
 assert len(slides)==80 and sum(s['minutes'] for s in slides)==180
 elapsed=0;rows=[]
 for n,s in enumerate(slides,1):
  row=dict(cues[s['title']],number=n,module=s['module'],minutes=s['minutes'],start=stamp(elapsed),end=stamp(elapsed+s['minutes']),
   slide_url=SITE+'operator-cases/#/'+str(n),presenter_url=SITE+'operator-cases/#/presenter/'+str(n),
   notebook_cell=s.get('notebook_cell'),lab_label=s.get('lab_label',''),source_link=s.get('action_link') if 'ST01' in s.get('refs',[]) else None)
  rows.append(row);elapsed+=s['minutes']
 return slides,rows

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--pdf',action='store_true',help='Also create the printable presenter script.');args=parser.parse_args()
 slides,rows=prepare();groups=[(m,[r for r in rows if r['module']==m]) for m in LABELS]
 intro='Use Say for the spoken explanation and Do / discuss for demonstrations and audience prompts. Timings include code execution, pair work and discussion; add breaks outside the 180-minute teaching schedule.'
 route='Start with the twelve-minute Stanford concept block, then seven minutes of Colab setup. Follow one Classroom Labs notebook in order through L0-L12, including L10B after L10. Leave both live-tool switches False for the standard route.'
 evidence='Python calculates fresh numerical results. L10B replays saved Llama replies and their original tool results. The recorded studies are separate from learner edits. L12 is a simulated readback and equipment_dispatch remains False.'
 md=['# Presenter script: three operator cases','', '**Alaa Selim, MIT/Dartmouth; Mohamed Chehada, UT Austin.**','', '80 slides / 180 teaching minutes / one required notebook / three four-minute exercises.','',intro,'',route,'',evidence,'',f'[Slides]({SITE}operator-cases/#/1) · [Presenter view]({SITE}operator-cases/#/presenter/1) · [Classroom Labs]({COLAB}) · [Full sources]({SITE}operator-cases/Full_Reading_Guide.html)','', '## Session route','']
 for m,group in groups:md.append(f'- [{LABELS[m]}](#module-{m}): slides {group[0]["number"]}-{group[-1]["number"]}, {group[0]["start"]}-{group[-1]["end"]}.')
 md+=['','Exercises: slides 25, 44 and 59. Run one four-minute timer for each. Reset the changed input before continuing.','']
 css='''body{font:19px/1.65 Arial,sans-serif;max-width:1080px;margin:35px auto;padding:0 24px;color:#003b5c}h1,h2,h3{line-height:1.25;color:#00629b}h1{font-size:39px}h2{font-size:29px;border-top:3px solid #00a6b2;padding-top:25px;margin-top:60px}h3{font-size:25px;margin-bottom:8px}a{color:#00629b;overflow-wrap:anywhere}nav ul{padding-left:24px}.slide{padding:12px 0 24px;border-bottom:1px solid #d6e2e9;scroll-margin-top:15px}.meta{color:#526470;font-size:16px}.action{padding-left:16px;border-left:3px solid #00a6b2}details{font-size:16px}li{margin:8px 0}@media(max-width:550px){body{font-size:18px;padding:0 17px}h1{font-size:31px}h3{font-size:23px}}@media print{body{font-size:11pt;max-width:none;margin:0}nav,.downloads,.slide-links,details{display:none}.slide{break-inside:avoid}h2{break-before:page}h1{font-size:24pt}h3{font-size:15pt}a{color:inherit;text-decoration:none}}'''
 web=['<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Presenter script: Three Operator Cases</title><style>'+css+'</style>', '<a href="'+SITE+'">Tutorial home</a><h1>Presenter script: three operator cases</h1><p><strong>Alaa Selim, MIT/Dartmouth; Mohamed Chehada, UT Austin.</strong></p><p>80 slides / 180 teaching minutes / one notebook / three exercises</p>', '<p>'+html.escape(intro)+'</p><p>'+html.escape(route)+'</p><p>'+html.escape(evidence)+'</p>', '<p class="downloads"><a href="Presenter_Script.pdf">Download script PDF</a> · <a href="Presenter_Script.md">Download editable script</a> · <a href="'+COLAB+'">Open Classroom Labs</a> · <a href="'+SITE+'operator-cases/#/presenter/1">Open presenter view</a></p><nav aria-label="Script sections"><h2>Session route</h2><ul>']
 for m,g in groups:web.append('<li><a href="#module-'+m+'">'+html.escape(LABELS[m])+'</a> / slides '+str(g[0]['number'])+'-'+str(g[-1]['number'])+' / '+g[0]['start']+'-'+g[-1]['end']+'</li>')
 web.append('</ul></nav><p>Exercises: slides 25, 44 and 59. Each lasts four minutes.</p>')
 for m,group in groups:
  md+=['<a id="module-'+m+'"></a>','', '## '+LABELS[m],'']
  web.append('<h2 id="module-'+m+'">'+html.escape(LABELS[m])+'</h2>')
  for row in group:
   n=row['number'];meta=f'{row["start"]}-{row["end"]} / {row["minutes"]:g} minutes'
   md += [f'### Slide {n}. {row["title"]}','',meta,'', '**Say:** '+row['say'],'','**Do / discuss:** '+row['action'],'']
   web.append('<section class="slide" id="slide-'+str(n)+'"><h3>Slide '+str(n)+'. '+html.escape(row['title'])+'</h3><p class="meta">'+meta+'</p><p><strong>Say:</strong> '+html.escape(row['say'])+'</p><p class="action"><strong>Do / discuss:</strong> '+html.escape(row['action'])+'</p>')
   if row['notebook_cell']:
    spec=row['notebook_cell'];text=f'Run the full {row["lab_label"]} cell. Stable ID: {spec["id"]}; slide excerpt: source lines {spec["start"]}-{spec["end"]}.'
    md += ['Notebook: '+text,''];web.append('<p class="meta">'+html.escape(text)+'</p>')
   if row['source_link']:
    a=row['source_link'];md += [f'[{a["label"]}]({a["url"]})',''];web.append('<p><a href="'+html.escape(a['url'],quote=True)+'">'+html.escape(a['label'])+'</a></p>')
   md += [f'[Open slide]({row["slide_url"]}) · [Presenter view]({row["presenter_url"]})','']
   web.append('<p class="slide-links"><a href="'+row['slide_url']+'">Open slide</a> · <a href="'+row['presenter_url']+'">Presenter view</a></p></section>')
 registry=load('research/source_map.json');sources=[registry[k] for k in ['ST01','ST02','ST03','DEF03']]
 md+=['## Reading and source credits','', 'Original source figures and our grid adaptations remain labeled on the slides. The lab uses custom Python, not the Stanford frameworks. Complete numerical sources, figure credits and evidence limits are in the [Teaching and Source Guide]('+SITE+'operator-cases/Full_Reading_Guide.html).','']
 web.append('<h2>Reading and source credits</h2><p>Source figures and grid adaptations remain labeled. The lab uses custom Python. <a href="'+SITE+'operator-cases/Full_Reading_Guide.html">Read complete numerical sources, figure credits and evidence limits.</a></p>')
 citations=[]
 for rec in sources:
  authors=rec.get('authors',rec.get('author',''));authors=', '.join(authors) if isinstance(authors,list) else authors
  citation=f'{authors}. {rec["title"]}. {rec.get("publisher","")}. {rec.get("date",rec.get("year",""))}.'
  citations.append((citation,rec['url']));md+=['- '+citation+' [Read full source]('+rec['url']+').']
  web.append('<p>'+html.escape(citation)+' <a href="'+html.escape(rec['url'],quote=True)+'">Read full source</a>.</p>')
 web.append('</html>')
 (ROOT/'Presenter_Script.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
 (ROOT/'Presenter_Script.html').write_text('\n'.join(web),encoding='utf-8')
 if args.pdf:write_pdf(rows,groups,intro,route,evidence,citations)
 for name in ['Presenter_Script.md','Presenter_Script.html']+(['Presenter_Script.pdf'] if args.pdf else []):shutil.copy2(ROOT/name,ROOT/'slidev/public'/name)
 manifest=dict(slides=len(rows),minutes=sum(r['minutes'] for r in rows),lesson_sha256=hashlib.sha256((ROOT/'lesson_content.json').read_bytes()).hexdigest(),script_cues_sha256=hashlib.sha256((ROOT/'content/presenter_script.json').read_bytes()).hexdigest(),entries=[{k:r[k] for k in ['number','title','minutes','start','end','lab_label']} for r in rows])
 dest=ROOT/'research/presenter/presenter_manifest.json';dest.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
 (ROOT/'slidev/public/research/presenter').mkdir(parents=True,exist_ok=True);shutil.copy2(dest,ROOT/'slidev/public/research/presenter'/dest.name)
 print(json.dumps({'script_slides':len(rows),'minutes':180,'pdf':args.pdf}))

def write_pdf(rows,groups,intro,route,evidence,citations):
 from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,KeepTogether
 from reportlab.lib.styles import ParagraphStyle
 from reportlab.lib.colors import HexColor
 BLUE=HexColor('#00629b');INK=HexColor('#003b5c');SLATE=HexColor('#526470')
 styles={
  'title':ParagraphStyle('Title',fontName='Helvetica-Bold',fontSize=29,leading=33,textColor=BLUE,spaceAfter=18),
  'module':ParagraphStyle('Module',fontName='Helvetica-Bold',fontSize=22,leading=26,textColor=BLUE,spaceAfter=20),
  'slide':ParagraphStyle('Slide',fontName='Helvetica-Bold',fontSize=14,leading=18,textColor=BLUE,spaceAfter=5),
  'body':ParagraphStyle('Body',fontName='Helvetica',fontSize=11.1,leading=15.3,textColor=INK,spaceAfter=9),
  'small':ParagraphStyle('Small',fontName='Helvetica',fontSize=8.6,leading=11.2,textColor=SLATE,spaceAfter=8)}
 def p(t,style='body'):return Paragraph(html.escape(plain(t)),styles[style])
 def link(url,label):return Paragraph('<link href="'+html.escape(url,quote=True)+'" color="#00629b">'+html.escape(plain(label))+'</link>',styles['small'])
 story=[p('Presenter script: three operator cases','title'),p('Alaa Selim, MIT/Dartmouth; Mohamed Chehada, UT Austin.'),p('80 slides / 180 teaching minutes / one notebook / three exercises'),p(intro),p(route),p(evidence),Spacer(1,10),p('Session route','slide')]
 for m,g in groups:story.append(p(f'{LABELS[m]}: slides {g[0]["number"]}-{g[-1]["number"]}, {g[0]["start"]}-{g[-1]["end"]}.'))
 story += [p('Exercises: slides 25, 44 and 59. Give each four minutes; reset the input afterward.'),link(COLAB,'Open Classroom Labs in Colab'),link(SITE+'operator-cases/#/presenter/1','Open presenter view'),link(SITE+'operator-cases/Presenter_Script.html','Open the searchable web script')]
 for m,group in groups:
  story.extend([PageBreak(),p(LABELS[m],'module')])
  for r in group:
   block=[p(f'Slide {r["number"]}. {r["title"]}','slide'),p(f'{r["start"]}-{r["end"]} / {r["minutes"]:g} minutes','small'),p('Say: '+r['say']),p('Do / discuss: '+r['action'])]
   if r['notebook_cell']:
    x=r['notebook_cell'];block.append(p(f'Notebook: run full {r["lab_label"]}; stable cell {x["id"]}, excerpt lines {x["start"]}-{x["end"]}.','small'))
   if r['source_link']:block.append(link(r['source_link']['url'],r['source_link']['label']))
   block.append(link(r['slide_url'],'Open slide '+str(r['number'])));block.append(Spacer(1,12));story.append(KeepTogether(block))
 story.extend([PageBreak(),p('Reading and source credits','module'),p('The original Stanford figures and the grid teaching adaptations remain labeled. The classroom notebook uses custom Python, rather than WikiChat, Genie Worksheets or a theorem prover. Numerical model limits and trust premises remain explicit.'),link(SITE+'operator-cases/Full_Reading_Guide.html','Complete teaching notes, numerical sources and figure credits')])
 for citation,url in citations:story.extend([p(citation),link(url,url),Spacer(1,8)])
 def footer(c,doc):
  c.saveState();c.setStrokeColor(HexColor('#00a6b2'));c.setLineWidth(1);c.line(46,754,566,754)
  c.setFillColor(SLATE);c.setFont('Helvetica',8);c.drawString(46,765,'Three Operator Cases / presenter script / IEEE ComSoc theme')
  c.drawString(46,29,'Delivery cues; timings include demonstrations and discussion.');c.drawRightString(566,29,str(doc.page));c.restoreState()
 doc=SimpleDocTemplate(str(ROOT/'Presenter_Script.pdf'),pagesize=(612,792),leftMargin=46,rightMargin=46,topMargin=52,bottomMargin=49,title='Presenter script: Three Operator Cases',author='Alaa Selim (MIT/Dartmouth); Mohamed Chehada (UT Austin)')
 doc.build(story,onFirstPage=footer,onLaterPages=footer)

if __name__=='__main__':main()
