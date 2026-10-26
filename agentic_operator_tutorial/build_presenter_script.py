"""Build and validate the foundations speaking script against the accepted deck.

python agentic_operator_tutorial/build_presenter_script.py --pdf
python agentic_operator_tutorial/build_presenter_script.py --check
Only script outputs are generated. The presentation and notebook sources are read-only.
"""
from pathlib import Path
import argparse, hashlib, html, json, re, shutil, unicodedata
import latin_modern

ROOT=Path(__file__).resolve().parent
SITE='https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/'
WEB=SITE+'foundations/'
PRESENTERS='Alaa Selim, MIT/Dartmouth; Mohamed Chehada, UT Austin.'
GROUPS=[('concepts',1,8,'1. Agents, tools and workflows'),
        ('industry',9,17,'2. What power-sector organizations report'),
        ('operators',18,27,'3. Operator tasks and evidence checks'),
        ('workflow',28,43,'4. Research foundations, LangGraph and PowerDAG'),
        ('simulation',44,55,'5. Simulation feedback and valid reuse'),
        ('benchmarks',56,67,'6. Power-system benchmarks and failure modes'),
        ('evaluation',68,77,'7. Statistics, integration and evaluation'),
        ('handoff',78,80,'8. Prepare for the three-case workshop')]
FIELDS=['say','visual','question','answer','transition']
GLOSSARY=[
 ('AI agent','A system that observes an environment and chooses actions. A software agent can observe records and act through software interfaces.'),
 ('Agentic system','Here, a system that uses feedback to pursue a goal. The cited engineering convention includes both programmed workflows and LLM-directed agents.'),
 ('Generative AI and LLM','Generative AI produces synthetic content. A large language model handles language and can support content creation or decisions within an agent system.'),
 ('Tool and tool call','A tool performs a defined operation. A tool call is a request with specified inputs. The solver or service returns evidence for the agent to use.'),
 ('Workflow and orchestration','The process and software rules that coordinate steps, routing, saved state and stopping. Some choices can be fixed in code and some assigned to a model.'),
 ('Retrieval and RAG','Retrieval finds records. Retrieval-augmented generation supplies selected source text to a language model when it constructs an answer.'),
 ('DAG','A directed acyclic graph. Arrows show required dependencies and cannot form a directed loop. A task DAG is different from the electrical network.'),
 ('LangGraph and state','LangGraph runs stateful workflows. State holds information used by later steps. The application defines what the stored fields mean and how updates combine.'),
 ('Reducer','An application-defined rule for combining state updates. In a parallel study it should preserve result identity and reveal missing or duplicate cases.'),
 ('Checkpoint, thread and interrupt','A checkpoint saves progress, a thread ID identifies the same run, and an interrupt pauses for outside input. Resumption still needs current-input checks.'),
 ('Idempotency','Handling a repeated request without unintentionally applying its effect again. This matters when a paused node restarts.'),
 ('Cache and input fingerprint','A cache stores results for reuse. A key or content hash must identify relevant inputs. Matching an incomplete key can still return a wrong result.'),
 ('MCP','Model Context Protocol: a standard connection between applications and tool servers. It does not choose studies or prove numerical correctness.'),
 ('Snapshot, topology and model version','The data time, electrical connection pattern and model revision that define a study. A result should identify all relevant inputs.'),
 ('Bus and feeder','A bus is a connection point in a power-system model. A feeder is a local distribution network. An electrical edge has a different meaning from a workflow edge.'),
 ('Power flow','A numerical calculation of a steady operating condition for specified inputs. Its result does not establish dynamic stability.'),
 ('OPF and ACOPF','Optimal power flow chooses allowed variables while meeting modeled constraints. ACOPF uses alternating-current network equations.'),
 ('Dynamic study','A simulation of system behavior over time, including equipment and controller response. Conclusions depend on the model and events tested.'),
 ('N-1 contingency','A study of a selected single-component outage. A completed selected list is not automatically every relevant N-1 case.'),
 ('Dispatch and unit commitment','Dispatch sets output of selected units. Unit commitment changes which units are on. Changing both enlarges a dispatch-only decision space.'),
 ('Reactive power and per unit','Reactive power is part of an AC study, commonly expressed in var or Mvar. Per unit is a value divided by a compatible base quantity.'),
 ('Solver residual and tolerance','A residual measures remaining equation error. A tolerance specifies accepted numerical error. These checks need the correct problem and inputs.'),
 ('Nonconvergence and infeasibility','Nonconvergence means the solve did not obtain an acceptable result. It alone does not prove no feasible solution exists.'),
 ('Surrogate and reduced-order model','An approximation that can reduce computational work. Its validity must be checked for the intended task and conditions.'),
 ('Pass@1','Success on the first evaluated attempt under a specified scoring rule. Its meaning depends on the benchmark and is not a generic safety measure.'),
 ('Joint, field and macro accuracy','Joint accuracy requires the complete answer. Field accuracy gives partial credit. A macro average gives groups equal weight rather than pooling all cases.'),
 ('Confidence interval','An interval procedure with stated repeated-sample coverage under assumptions. It is not proof of performance on changed tasks or settings.'),
 ('False approval','Accepting a case that should fail the stated criteria. Always name the denominator, such as all infeasible cases or all accepted cases.'),
 ('Shadow mode','Saving assistant proposals while the existing decision process continues. It allows comparison before the assistant receives greater authority.'),
 ('Data, engineering and decision validity','Respectively: correct evidence identity and consistency; the required numerical checks; and sufficient evidence and authority for the next decision.')]

def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def stamp(m):
 s=round(60*m);return f'{s//3600:02}:{s%3600//60:02}:{s%60:02}'
def esc(t):return html.escape(str(t),quote=True)
def plain(t):
 for a,b in {'\u2013':'-','\u2014':'-','\u2212':'-','\u2019':"'",'\u2018':"'",'\u201c':'"','\u201d':'"','\u2192':' to ','\u2264':'<=','\u2265':'>=','\u03b1':'alpha','\u03b2':'beta','\u03c0':'pi','\u03bc':'mu'}.items():t=t.replace(a,b)
 return unicodedata.normalize('NFKD',t).encode('ascii','ignore').decode()
def source_url(url):
 for prefix in ['../research/','/research/','research/']:
  if url.startswith(prefix):return WEB+'research/'+url[len(prefix):]
 return url
def citation(rec):
 if rec.get('bibliographic_citation'):return rec['bibliographic_citation']
 author=rec.get('authors') or rec.get('author') or rec.get('organization') or rec.get('publisher','')
 if isinstance(author,list):author=', '.join(author)
 publisher=rec.get('publisher') or rec.get('organization','')
 parts=[author,rec['title']]
 if publisher and publisher!=author:parts.append(publisher)
 parts.append(str(rec.get('date',rec.get('year',''))))
 return '. '.join(str(p).rstrip('.') for p in parts if p)+'.'

def prepare():
 slides=load('lesson_content.json');cues=load('content/presenter_script.json')['slides'];sources=load('research/source_map.json')
 if len(slides)!=80 or len(cues)!=80:raise ValueError('Expect eighty slide explanations.')
 if len({c['title'] for c in cues})!=80:raise ValueError('Duplicate script title.')
 cue_map={c['title']:c for c in cues}
 if set(cue_map)!={s['title'] for s in slides}:raise ValueError('Slide titles changed: update the authored script.')
 if sum(s['minutes'] for s in slides)!=165:raise ValueError('Expected 165 teaching minutes.')
 if [n for n,s in enumerate(slides,1) if s['kind']=='exercise']!=[26,54]:raise ValueError('Check exercise locations.')
 rows=[];elapsed=0
 for n,s in enumerate(slides,1):
  c=cue_map[s['title']]
  if c['number']!=n:raise ValueError('Slide order changed: review narration and transitions.')
  if any(not c.get(k,'').strip() for k in FIELDS):raise ValueError('Missing teaching cue on '+str(n))
  for ref in s.get('refs',[]):
   if ref not in sources:raise ValueError('Unregistered source '+ref)
  image=s.get('image') or ('diagrams/'+s['diagram']+'.svg' if s.get('diagram') else '')
  if s.get('image'):image='images/'+image
  if image and not (ROOT/'slidev/public'/image).is_file():raise ValueError('Missing published figure '+image)
  rows.append(dict(c,slide=s,start=stamp(elapsed),end=stamp(elapsed+s['minutes']),minutes=s['minutes'],image=image))
  elapsed+=s['minutes']
 return rows,sources

CSS='''body{font:19px/1.65 'Latin Modern Roman',serif;max-width:1080px;margin:32px auto;padding:0 24px;color:#003b5c}h1,h2,h3{line-height:1.25;color:#00629b}h1{font-size:39px}h2{font-size:29px;border-top:3px solid #00a6b2;padding-top:24px;margin-top:54px}h3{font-size:26px}a{color:#00629b;overflow-wrap:anywhere}li{margin:8px 0}.slide{padding:12px 0 28px;border-bottom:1px solid #d6e2e9;scroll-margin-top:20px}.meta,.credit{font-size:16px;color:#526470}.cue{border-left:3px solid #00a6b2;padding-left:16px}.question{padding:12px 17px;background:#edf6fa}details{margin:14px 0}summary{cursor:pointer;color:#00629b}figure{margin:18px 0}figure img{display:block;max-width:100%;max-height:500px;width:auto;height:auto;margin:auto}figcaption{font-size:15px;color:#526470}input{font:inherit;padding:10px;width:100%;box-sizing:border-box;border:1px solid #aabfc9;border-radius:5px}label{display:block;margin:20px 0 8px}#search-status{font-size:16px}.sources p{font-size:16px}.glossary dt{font-weight:bold;margin-top:18px}.glossary dd{margin-left:0}.exercise{border-top:4px solid #00a6b2}[hidden]{display:none!important}@media(max-width:550px){body{font-size:18px;padding:0 17px}h1{font-size:30px}h3{font-size:23px}}@media print{body{font-size:11pt;max-width:none;margin:0}.search,nav,.downloads,.slide-links,details.visual{display:none}h2{break-before:page}.slide{break-before:page}a{color:inherit;text-decoration:none}}'''

def render(rows,sources,pdf=False):
 used=load('build_manifest.json')['reading_source_ids']
 if any(k not in sources for k in used):raise ValueError('Unregistered reading source.')
 intro='A speaking and teaching companion for all 80 foundations slides. Follow the existing 165-minute route, including the six-minute exercise across slides 26-27 and the eight-minute exercise across slides 54-55. Add breaks outside this teaching time.'
 how='Use Say as the spoken explanation. Walk the image or concept using Show / explain, then use the quick question when it helps the room. Expected answers are presenter cues. The final sentence bridges to the next slide. The timings include explanation, visual walkthrough and brief discussion; the exercise timings include all group work.'
 scope='This script follows the accepted deck and its 18 October 2026 evidence snapshot. It preserves the distinction between company disclosures, supplier reports, product announcements, research results and invented teaching examples. It makes no new experiment or model call.'
 md=['# Foundations presenter script','', '**'+PRESENTERS+'**','',intro,'',how,'',scope,'',f'[Slides]({WEB}#/1) / [Presenter view]({WEB}#/presenter/1) / [Full reading guide]({WEB}Full_Reading_Guide.html)','', '## Prepare to teach','',
  '- Open the slides and this script in separate windows. Test the presenter view and the source links before the session.',
  '- Ask learners to keep one real work task in mind. Revisit that task in the closing discussion.',
  '- Explain each result by naming its task, denominator, success rule and remaining limitations. Research percentages across different tasks are not a ranking.',
  '- Show each question first, then advance to its worked answer for the debrief. No notebook or model account is needed for this foundations session.',
  '- The next hands-on tutorial uses one required Classroom Labs notebook, with fresh numerical work and separately labeled saved Llama records.','', '## Teaching route','']
 web=['<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Foundations presenter script</title><style>'+CSS+'</style></head><body><main>',
 '<a href="'+SITE+'">Tutorial home</a><h1>Foundations presenter script</h1><p><strong>'+esc(PRESENTERS)+'</strong></p>',
 '<p>'+esc(intro)+'</p><p>'+esc(how)+'</p><p>'+esc(scope)+'</p>',
 '<p class="downloads"><a href="Presenter_Script.pdf">Download printable PDF</a> / <a href="Presenter_Script.md">Download editable script</a> / <a href="'+WEB+'#/presenter/1">Open presenter view</a></p>',
 '<h2>Prepare to teach</h2><ul>']
 for s in md[md.index('## Prepare to teach')+2:md.index('## Teaching route')-1]:
  if s.startswith('- '):web.append('<li>'+esc(s[2:])+'</li>')
 web+=['</ul><nav aria-label="Teaching route"><h2>Teaching route</h2><ul>']
 for key,a,b,label in GROUPS:
  r0,r1=rows[a-1],rows[b-1];route=f'{label}: slides {a}-{b}, {r0["start"]}-{r1["end"]}'
  md.append(f'- [{route}](#module-{key})');web.append('<li><a href="#module-'+key+'">'+esc(route)+'</a></li>')
 md+=['','Exercises: slides 26-27, six minutes; slides 54-55, eight minutes.','', '## Quick glossary','']
 # Keep the glossary after the narration online and in print, while linking it early.
 md=md[:-2]+['[Plain-language glossary](#glossary) / [Full references](#references)','']
 web+=['<li><a href="#glossary">Plain-language glossary</a></li><li><a href="#references">Full references</a></li></ul></nav>',
 '<div class="search"><label for="search">Find a slide, term or paper</label><input id="search" type="search" placeholder="For example: slide 39, PowerDAG, confidence" aria-describedby="search-status"><p id="search-status" aria-live="polite">80 slide explanations</p></div>']
 for key,a,b,label in GROUPS:
  md+=['<a id="module-'+key+'"></a>','', '## '+label,''];web.append('<h2 id="module-'+key+'">'+esc(label)+'</h2>')
  for r in rows[a-1:b]:
   n=r['number'];s=r['slide'];meta=f'{r["start"]}-{r["end"]} / {r["minutes"]:g} minutes'
   md+=[f'### Slide {n}. {r["title"]}','',meta,'']
   web.append('<section class="slide'+(' exercise' if s['kind']=='exercise' else '')+'" id="slide-'+str(n)+'"><h3>Slide '+str(n)+'. '+esc(r['title'])+'</h3><p class="meta">'+meta+'</p>')
   for field,label2 in [('say','Say'),('visual','Show / explain'),('question','Ask'),('answer','Expected answer'),('transition','Transition')]:
    md+=['**'+label2+':** '+r[field],'']
    web.append('<p class="'+('cue' if field=='visual' else 'question' if field=='question' else field)+'"><strong>'+label2+':</strong> '+esc(r[field])+'</p>')
   if r['image']:
    credit=s.get('caption','');web.append('<details class="visual"><summary>Show this slide\'s source visual</summary><figure><img loading="lazy" src="'+esc(r['image'])+'" alt="'+esc(credit or r['title'])+'"><figcaption>'+esc(credit)+'</figcaption></figure></details>')
   refs=s.get('refs',[])
   if refs:
    md+=['Sources: '+', '.join('['+k+'](#source-'+k+')' for k in refs)+'. Full author, title, date and URLs appear in the reference section.','']
    web.append('<details class="sources"><summary>Full source credits and teaching detail</summary><p>'+esc(s.get('note',''))+'</p>')
    for k in refs:
     rec=sources[k];web.append('<p><strong>['+k+']</strong> '+esc(citation(rec))+' <a href="'+esc(source_url(rec['url']))+'">Read full source</a>'+(' / <a href="'+esc(source_url(rec['pdf_url']))+'">Full paper</a>' if rec.get('pdf_url') else '')+'</p>')
    web.append('</details>')
   else:web.append('<p class="credit">Original teaching explanation or worked example; see the slide and instructor guide for its stated assumptions.</p>')
   md+=[f'[Open slide]({WEB}#/{n}) / [Presenter view]({WEB}#/presenter/{n})','']
   web.append('<p class="slide-links"><a href="'+WEB+'#/'+str(n)+'">Open slide '+str(n)+'</a> / <a href="'+WEB+'#/presenter/'+str(n)+'">Presenter view</a> / <a href="#module-'+key+'">Section start</a></p></section>')
 md+=['<a id="glossary"></a>','', '## Plain-language glossary',''];web.append('<h2 id="glossary">Plain-language glossary</h2><dl class="glossary">')
 for term,definition in GLOSSARY:md+=['**'+term+':** '+definition,''];web.append('<dt>'+esc(term)+'</dt><dd>'+esc(definition)+'</dd>')
 web.append('</dl><h2 id="references">Full references and source credits</h2><p>The source entries below follow the deck\'s source order. Original figure captions and detailed evidence limits remain available on each slide and in the reading guide.</p>')
 md+=['<a id="references"></a>','', '## Full references and source credits','', 'The source list follows the accepted deck. Source figures retain their original attribution; detailed visual provenance and evidence limits are in the full reading guide.','']
 for k in used:
  rec=sources[k];url=source_url(rec['url']);md+=['<a id="source-'+k+'"></a>','', '**['+k+']** '+citation(rec),'', 'Full source: '+url,'']
  web.append('<article class="sources" id="source-'+k+'"><h3>['+k+'] '+esc(rec['title'])+'</h3><p>'+esc(citation(rec))+'</p><p><a href="'+esc(url)+'">'+esc(url)+'</a></p>')
  if rec.get('pdf_url'):md+=['Full paper: '+source_url(rec['pdf_url']),''];web.append('<p>Full paper: <a href="'+esc(source_url(rec['pdf_url']))+'">'+esc(source_url(rec['pdf_url']))+'</a></p>')
  web.append('</article>')
 web.append('''</main><script>const field=document.querySelector('#search');const entries=[...document.querySelectorAll('section.slide')];field.addEventListener('input',()=>{const q=field.value.trim().toLowerCase();let count=0;for(const entry of entries){const match=!q||entry.textContent.toLowerCase().includes(q);entry.hidden=!match;if(match)count++;}document.querySelector('#search-status').textContent=count+' of 80 slide explanations';});</script></body></html>''')
 (ROOT/'Presenter_Script.md').write_text('\n'.join(md).rstrip()+'\n',encoding='utf-8')
 latin_modern.copy_web_fonts(ROOT/'slidev/public/fonts')
 (ROOT/'Presenter_Script.html').write_text(latin_modern.style_html('\n'.join(web)+'\n'),encoding='utf-8')
 if pdf:write_pdf(rows,sources,used,intro,how,scope)
 for name in ['Presenter_Script.md','Presenter_Script.html']+(['Presenter_Script.pdf'] if pdf else []):shutil.copy2(ROOT/name,ROOT/'slidev/public'/name)
 manifest=dict(slides=80,minutes=165,exercises=[26,54],source_count=len(used),lesson_sha256=sha('lesson_content.json'),slidev_sha256=sha('slidev/slides.md'),cue_sha256=sha('content/presenter_script.json'),renderer_sha256=sha('build_presenter_script.py'),spoken_words=sum(len(r['say'].split()) for r in rows),entries=[{k:r[k] for k in ['number','title','minutes','start','end']} for r in rows])
 if pdf:manifest['pdf_sha256']=sha('Presenter_Script.pdf')
 dest=ROOT/'research/presenter';dest.mkdir(parents=True,exist_ok=True);(dest/'presenter_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
 public=ROOT/'slidev/public/research/presenter';public.mkdir(parents=True,exist_ok=True);shutil.copy2(dest/'presenter_manifest.json',public/'presenter_manifest.json')
 return manifest

def write_pdf(rows,sources,used,intro,how,scope):
 from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,KeepTogether
 from reportlab.lib.styles import ParagraphStyle
 from reportlab.lib.colors import HexColor
 latin_modern.register_reportlab()
 BLUE=HexColor('#00629b');INK=HexColor('#003b5c');SLATE=HexColor('#526470')
 styles={
  'title':ParagraphStyle('Title',fontName='LMRomanBold',fontSize=29,leading=33,textColor=BLUE,spaceAfter=18),
  'heading':ParagraphStyle('Heading',fontName='LMRomanBold',fontSize=20,leading=24,textColor=BLUE,spaceAfter=16),
  'slide':ParagraphStyle('Slide',fontName='LMRomanBold',fontSize=19,leading=23,textColor=BLUE,spaceAfter=9),
  'label':ParagraphStyle('Label',fontName='LMRomanBold',fontSize=10,leading=13,textColor=BLUE,spaceBefore=7,spaceAfter=3),
  'body':ParagraphStyle('Body',fontName='LMRoman',fontSize=12,leading=16.4,textColor=INK,spaceAfter=7),
  'small':ParagraphStyle('Small',fontName='LMRoman',fontSize=9,leading=12,textColor=SLATE,spaceAfter=7)}
 def p(t,style='body'):return Paragraph(esc(plain(t)),styles[style])
 def link(url,label):return Paragraph('<link href="'+esc(url)+'" color="#00629b">'+esc(plain(label))+'</link>',styles['small'])
 story=[p('Foundations presenter script','title'),p(PRESENTERS),p('80 slides / 165 teaching minutes / two worked exercises'),p(intro),p(how),p(scope),Spacer(1,14),p('Before presenting','heading')]
 for text in ['Open the presentation and script in separate windows. Test presenter view and source links.',
              'Ask learners to keep one real work task in mind. Revisit it in the closing discussion.',
              'Name the task, denominator and scoring rule for every research number. Different tasks do not form a model ranking.',
              'Show questions first and reveal answers on the following slides. Foundations needs no notebook or model account.']:
  story.append(p(text))
 story.extend([link(WEB+'#/1','Open the foundations slides'),link(WEB+'#/presenter/1','Open presenter view'),link('https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_operator_tutorial/Presenter_Script.html','Presenter script source in the repository')])
 story.extend([PageBreak(),p('Teaching route','heading')])
 for key,a,b,label in GROUPS:
  story.append(p(f'{label}: slides {a}-{b}, {rows[a-1]["start"]}-{rows[b-1]["end"]}.'))
 story.extend([Spacer(1,12),p('Exercise pacing','heading'),p('Slides 26-27: five minutes to inspect, work in pairs and share; one minute for the worked answer.'),p('Slides 54-55: six minutes to think, compare and discuss; two minutes for the worked answer.'),p('The printed script gives one page per slide. Full author, title, publication details and source URLs follow the glossary. Source IDs on each teaching page link to that reference list.'),link(WEB+'Full_Reading_Guide.html','Full reading guide and visual provenance'),link(SITE+'operator-cases/#/1','Follow-on hands-on tutorial')])
 group_at={a:label for _,a,_,label in GROUPS}
 for r in rows:
  n=r['number'];story.append(PageBreak())
  if n in group_at:story.append(p(group_at[n],'small'))
  title=p(f'Slide {n}. {r["title"]}','slide');title._bookmark='slide-'+str(n);title._outline=f'Slide {n}. '+plain(r['title']);story.append(title)
  story.append(p(f'{r["start"]}-{r["end"]} / {r["minutes"]:g} minutes','small'))
  for field,label in [('say','Say'),('visual','Show / explain'),('question','Ask'),('answer','Expected answer'),('transition','Transition')]:
   story.append(KeepTogether([p(label,'label'),p(r[field])]))
  refs=r['slide'].get('refs',[])
  if refs:story.append(Paragraph('Sources: '+', '.join('<link href="#source-'+k+'" color="#00629b">['+k+']</link>' for k in refs)+'. Full references follow the glossary.',styles['small']))
  else:story.append(p('Original teaching explanation or worked example. Preserve its stated assumptions.','small'))
  story.append(link(WEB+'#/'+str(n),'Open slide '+str(n)+' online'))
 story.extend([PageBreak(),p('Plain-language glossary','heading')])
 for term,definition in GLOSSARY:story.append(KeepTogether([p(term,'label'),p(definition)]))
 story.extend([PageBreak(),p('Full references and source credits','heading'),p('These '+str(len(used))+' entries follow the accepted deck. The source figures retain their original attribution. The full reading guide includes detailed visual provenance and the original evidence limits.'),link(WEB+'Full_Reading_Guide.html','Full reading guide')])
 for k in used:
  rec=sources[k];label=Paragraph('<a name="source-'+k+'"/>['+k+'] '+esc(plain(citation(rec))),styles['body'])
  label._bookmark='source-'+k;label._outline='['+k+'] '+plain(rec['title'])
  block=[label,link(source_url(rec['url']),source_url(rec['url']))]
  if rec.get('pdf_url'):block.append(link(source_url(rec['pdf_url']),'Full paper: '+source_url(rec['pdf_url'])))
  block.append(Spacer(1,9));story.append(KeepTogether(block))
 def footer(c,doc):
  c.saveState();c.setStrokeColor(HexColor('#00a6b2'));c.line(46,754,566,754);c.setFillColor(SLATE);c.setFont('LMRoman',8)
  c.drawString(46,765,'Foundations / presenter script / IEEE ComSoc theme');c.drawString(46,29,'Alaa Selim (MIT/Dartmouth); Mohamed Chehada (UT Austin)');c.drawRightString(566,29,str(doc.page));c.restoreState()
 class ScriptDoc(SimpleDocTemplate):
  def afterFlowable(self,flowable):
   if getattr(flowable,'_bookmark',None):
    self.canv.bookmarkPage(flowable._bookmark);self.canv.addOutlineEntry(flowable._outline,flowable._bookmark,level=0,closed=False)
 doc=ScriptDoc(str(ROOT/'Presenter_Script.pdf'),pagesize=(612,792),leftMargin=46,rightMargin=46,topMargin=52,bottomMargin=49,title='Foundations presenter script: Agentic AI for Utility Operators',author=PRESENTERS)
 doc.build(story,onFirstPage=footer,onLaterPages=footer)

def check(rows):
 manifest=load('research/presenter/presenter_manifest.json')
 for key,path in [('lesson_sha256','lesson_content.json'),('slidev_sha256','slidev/slides.md'),('cue_sha256','content/presenter_script.json'),('renderer_sha256','build_presenter_script.py')]:
  if manifest[key]!=sha(path):raise ValueError('Regenerate the presenter script after changing '+path)
 if manifest.get('pdf_sha256')!=sha('Presenter_Script.pdf'):raise ValueError('Presenter PDF differs from its generated receipt.')
 md=(ROOT/'Presenter_Script.md').read_text(encoding='utf-8');web=(ROOT/'Presenter_Script.html').read_text(encoding='utf-8')
 if len(re.findall(r'^### Slide \d+\.',md,re.M))!=80 or web.count('<section class="slide')!=80:raise ValueError('Script coverage mismatch.')
 for name in ['Presenter_Script.pdf','Presenter_Script.html','Presenter_Script.md']:
  if (ROOT/name).read_bytes()!=(ROOT/'slidev/public'/name).read_bytes():raise ValueError('Public copy differs: '+name)
 from pypdf import PdfReader
 reader=PdfReader(ROOT/'Presenter_Script.pdf')
 if len(reader.pages)<82:raise ValueError('Missing printed teaching pages.')
 for i,r in enumerate(rows):
  text=reader.pages[i+2].extract_text()
  if f'Slide {i+1}.' not in text or not all(x in text for x in ['Show / explain','Expected answer','Transition']):raise ValueError('Printed slide page missing or overflowed: '+str(i+1))
 print(json.dumps(dict(slides=80,minutes=165,spoken_words=manifest['spoken_words'],sources=manifest['source_count'],pdf_pages=len(reader.pages),one_page_per_slide=True,exercises=[26,54],validated=True)))

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--pdf',action='store_true');parser.add_argument('--check',action='store_true');args=parser.parse_args()
 rows,sources=prepare()
 if args.check:check(rows)
 else:
  manifest=render(rows,sources,args.pdf);print(json.dumps({k:manifest[k] for k in ['slides','minutes','source_count','spoken_words']}))
  if args.pdf:check(rows)

if __name__=='__main__':main()
