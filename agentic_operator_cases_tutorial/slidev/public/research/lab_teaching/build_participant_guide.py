"""Build a short participant workbook from the same lesson and notebook labels."""
from pathlib import Path
import html,json,shutil,subprocess
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.utils import ImageReader
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF

ROOT=Path(__file__).resolve().parents[2]
BUILD=ROOT/'research/lab_teaching/_build';BUILD.mkdir(exist_ok=True)
COLAB='https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb'
SITE='https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/'
GH='https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/'
POP=Path(r'C:/Users/f00863x/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe')
slides=json.loads((ROOT/'lesson_content.json').read_text(encoding='utf-8'))
exercise={s['lab_label']:i for i,s in enumerate(slides,1) if s['kind']=='exercise'}
sections=[
 dict(title='Start with one notebook',subtitle='Classroom Labs / participant guide',diagram='lab_colab_workbook',body=[
  '<b>Presenters:</b> Alaa Selim, MIT/Dartmouth; Mohamed Chehada, UT Austin.',
  'Open <b>Classroom_Labs.ipynb</b>. It covers voltage, restoration, cyber and the saved Llama replays. The website’s other notebooks are companion resources.',
  '<b>1. Keep your copy.</b> Sign in and save a copy in Drive, or download your notebook when you finish.',
  '<b>2. Connect a CPU.</b> Run the first setup cell. Wait for <b>Ready</b>, then run <b>L0</b> and <b>L1</b>. Keep both switches False.',
  '<b>3. Follow the slides.</b> Run each named cell when prompted. You will change one number in each case. No coding experience or live LLM service is required.',
  'The runtime is a temporary computer. Saving the notebook does not keep its temporary files or variables. After a reset, rerun setup and earlier cells.'
 ],prompt='Before the first case, show your partner where the code, play button and output appear.'),
 dict(title='Learn with one small experiment',subtitle='Predict / run / read / change / explain',diagram='lab_cell_loop',body=[
  '<b>Read the input.</b> Find the L heading in the notebook. The slide shows selected lines; run the full cell.',
  '<b>Predict first.</b> Tell your partner what you expect before revealing the result.',
  '<b>Run and wait.</b> Use the play button beside that cell. Read the new table or plot underneath it.',
  '<b>Change one input.</b> Rerun the cell, compare outputs and explain which check supports your next step.',
  '<b>Use the labels.</b> Fresh means calculated now. Recorded replay means an actual old model reply with its original context. A saved controller can produce a new proposal from old weights.',
  '<b>Common messages:</b> HOLD means a required condition is missing or unmet. REVIEW means a person still needs to assess it. L11 SKIPPED is expected when the live-model switch is False.',
  '<b>If a variable is missing:</b> rerun the required earlier cells. Editing a number does not update an old output until you rerun.'
 ],prompt='Work in pairs: one person runs, one checks. Swap roles for the next case.'),
 dict(title='Case 1: voltage support',subtitle=f'L2–L5 / exercise on slide {exercise["L2"]}',image='hands_on_L2_plot.png',body=[
  '<b>Goal:</b> compare two control proposals, then check their voltage and current limits.',
  '<b>Run L2 at the defaults:</b> LOAD_SCALE = 1.0 and RATING_FRACTION = 0.80. Read feasible, current_step_J and max_allowed_current_pct.',
  '<b>Read the plots:</b> the left plot shows sorted modeled voltages. The right plot compares current use with the 100% allowed-current line.',
  '<b>Four-minute task:</b> change only RATING_FRACTION to <b>0.75</b>. Predict, rerun all of L2 and compare both methods. Check limits before comparing the score J.',
  '<b>Reset:</b> restore 0.80 and rerun L2. Then follow L3–L5. Those cells use the separate original test_01 archive; your edited L2 does not rewrite it.',
  '<b>Model coverage:</b> the default check covers the MV model. It does not prove that every LV device or dynamic limit passes.'
 ],prompt='Record: the changed allowance, each current percentage, pass/fail, and what the model does not cover.'),
 dict(title='Case 2: restoring service',subtitle=f'L6–L7 / exercise on slide {exercise["L6"]}',image='hands_on_L6_plot.png',body=[
  '<b>Goal:</b> see why restoring the most kW can differ from serving critical loads.',
  '<b>Run L6:</b> compare served_kw and critical_kw for the priority-weighted plan and the maximum-kW plan. Both use the same six-node graph.',
  '<b>Read the plots together:</b> total service is on the left; critical service is on the right. Explain the tradeoff at 40 kW.',
  '<b>Four-minute task:</b> append <b>180.</b> to CAPACITIES_KW. Keep <b>40.</b> first. Predict, rerun L6 and compare the 40 kW and 180 kW outcomes.',
  '<b>Reset before L7:</b> restore the original capacity list and rerun L6. L7 uses the first record, then tests a changed request with the old evidence.',
  '<b>Meaning of HOLD:</b> old evidence no longer matches. That does not prove a newly calculated plan would fail. The model also omits AC voltage and physical switching order.'
 ],prompt='Record: total and critical kW at both capacities. Explain which service goal each plan follows.'),
 dict(title='Case 3: checking suspicious readings',subtitle=f'L8–L9 / exercise on slide {exercise["L8"]}',image='hands_on_L8_plot.png',body=[
  '<b>Goal:</b> distinguish a reading that fits the model from a reading that is true.',
  '<b>Run L8:</b> compare isolated bias with coordinated Hc shifts. The residual alarm measures mismatch. State error uses known simulation truth for teaching.',
  '<b>Four-minute task:</b> add <b>.10</b> to ATTACK_SCALES. Predict, rerun L8 and compare the alarm with the state error at that scale.',
  '<b>Reset before L9:</b> restore the original scale list and rerun L8. L9 is a separate fixed recovery case; its correction does not follow your changed sweep.',
  '<b>Run L9:</b> no trusted replacement data gives HOLD. Assuming the additional readings are trusted allows a PROPOSE result. The calculation does not authenticate those readings.',
  '<b>Discuss:</b> a small residual or clear model explanation alone cannot establish sensor trust.'
 ],prompt='Record: residual J, alarm flag, state error and the condition needed before a recovery proposal.'),
 dict(title='Read Llama’s choices',subtitle='L10 / L10B / L11 / L12',diagram='agent_roles_simple',body=[
  '<b>The opening and case slides preview saved agent examples.</b> Follow the notebook in order; run the replays here after the three cases.',
  '<b>Run L10, then L10B:</b> set SCENARIO = "voltage", then "restoration" and "cyber", rerunning each time. These use separate recorded studies.',
  '<b>Follow the agentic loop:</b> goal, Llama tool choice, returned evidence, next choice. The replay makes no new model call.',
  '<b>Restoration challenge:</b> find the wrong Llama ranking. Explain why the numerical guard keeps the lower-cost passed candidate.',
  '<b>L11:</b> keep the live call disabled. <b>L12:</b> inspect the full-scope HOLD, the wrong-ID rejection and the simulated readback. equipment_dispatch stays False.',
  '<b>Exit ticket:</b> explain one result using input, tool, result, check and operator decision. Save the changed inputs and outputs.'
 ],prompt='Choose one case. Which decision did Llama make, which fact came from a tool, and what must the operator still review?')
]
BLUE=HexColor('#00629b');INK=HexColor('#003b5c');SLATE=HexColor('#526470');TEAL=HexColor('#00a6b2')
styles={
 'body':ParagraphStyle('body',fontName='Helvetica',fontSize=11.2,leading=15.8,textColor=INK,spaceAfter=10),
 'small':ParagraphStyle('small',fontName='Helvetica',fontSize=8.5,leading=11.5,textColor=SLATE,splitLongWords=True),
 'prompt':ParagraphStyle('prompt',fontName='Helvetica-Bold',fontSize=11.5,leading=16,textColor=BLUE)}
path=ROOT/'Participant_Lab_Guide.pdf';c=canvas.Canvas(str(path),pagesize=(612,792))
c.setTitle('Participant Lab Guide: Three Operator Cases');c.setAuthor('Alaa Selim (MIT/Dartmouth); Mohamed Chehada (UT Austin)')
def para(text,y,style='body',width=512,x=50):
 p=Paragraph(text,styles[style]);w,h=p.wrap(width,1000);p.drawOn(c,x,y-h);return y-h-10
def diagram_file(id):
 prefix=BUILD/id
 subprocess.run([str(POP),'-singlefile','-png','-scale-to-x','1500','-scale-to-y','-1',str(ROOT/'diagrams'/(id+'.pdf')),str(prefix)],check=True,capture_output=True)
 return prefix.with_suffix('.png')
web=['<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Participant Lab Guide</title><style>body{font:20px/1.6 Arial;max-width:1050px;margin:35px auto;padding:24px;color:#003b5c}h1,h2{color:#00629b}section{border-top:3px solid #00a6b2;margin:45px 0;padding-top:25px}img{max-width:100%;max-height:320px;display:block;margin:20px auto}a{color:#00629b;overflow-wrap:anywhere}.prompt{font-weight:bold;color:#00629b}</style><h1>Participant Lab Guide</h1><p><a href="Participant_Lab_Guide.pdf">Download the printable guide</a> · <a href="'+COLAB+'">Open the one required Colab</a></p>']
for n,s in enumerate(sections,1):
 c.setFillColor(BLUE);c.setFont('Helvetica-Bold',23);c.drawString(50,743,s['title'])
 c.setFillColor(SLATE);c.setFont('Helvetica',10.5);c.drawString(50,719,s['subtitle'])
 c.setStrokeColor(TEAL);c.setLineWidth(1.5);c.line(50,706,562,706);y=690
 imagepath=diagram_file(s['diagram']) if s.get('diagram') else ROOT/'images'/s['image']
 im=ImageReader(str(imagepath));iw,ih=im.getSize();h=min(132,512*ih/iw);w=h*iw/ih
 c.drawImage(im,50+(512-w)/2,y-h,width=w,height=h,mask='auto');y-=h+18
 for body in s['body']:y=para(body,y)
 y=para(s['prompt'],y,'prompt')
 if n==1:
  qr=QrCodeWidget(COLAB);b=qr.getBounds();drawing=Drawing(64,64,transform=[64/(b[2]-b[0]),0,0,64/(b[3]-b[1]),0,0]);drawing.add(qr)
  renderPDF.draw(drawing,c,50,68)
  para('<link href="'+COLAB+'" color="#00629b">Open Classroom Labs in Google Colab</link><br/>Scan the code or use the website’s first Colab button.',126,'small',width=420,x=130)
  assert y>145,('page 1 crowding',y)
 elif n==6:
  refs='Monica Lam. <i>CS224V Agentic AI, Lecture 1: Introduction.</i> Stanford University, Fall 2026, pp.19–20, 40 and 52–53. <link href="https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf" color="#00629b">Full lecture PDF</link>. Teaching ideas adapted to our own grid examples.<br/>Google Colaboratory. <i>Frequently Asked Questions.</i> <link href="https://research.google.com/colaboratory/faq.html" color="#00629b">research.google.com/colaboratory/faq.html</link>.<br/>Full paper citations, figure credits and exact notebook source map: <link href="'+SITE+'operator-cases/Full_Reading_Guide.html" color="#00629b">Teaching and Source Guide</link>.'
  y=para(refs,y,'small')
 else:
  for _ in range(2):c.setStrokeColor(HexColor('#c7d5dd'));c.line(50,y-12,562,y-12);y-=28
 assert y>=43,('Page overflow',n,y)
 c.setFont('Helvetica',8);c.setFillColor(SLATE);c.drawString(50,30,'Three Operator Cases / Participant Lab Guide / 24 October 2026');c.drawRightString(562,30,f'{n}/6')
 c.showPage()
 web.append('<section><h2>'+str(n)+'. '+html.escape(s['title'])+'</h2><p>'+html.escape(s['subtitle'])+'</p><img alt="Teaching illustration for '+html.escape(s['title'])+'" src="'+('diagrams/'+s['diagram']+'.svg' if s.get('diagram') else 'images/'+s['image'])+'">'+''.join('<p>'+b+'</p>' for b in s['body'])+'<p class="prompt">'+s['prompt']+'</p></section>')
c.save()
web.append('<p>Stanford teaching source: Monica Lam, <a href="https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf">CS224V Lecture 1: Introduction</a>, Fall 2026, pp.19–20, 40 and 52–53. <a href="https://research.google.com/colaboratory/faq.html">Google Colab FAQ</a>. <a href="Full_Reading_Guide.html">Full references and figure credits</a>.</p></html>')
(ROOT/'Participant_Lab_Guide.html').write_text('\n'.join(web),encoding='utf-8')
for f in ['Participant_Lab_Guide.pdf','Participant_Lab_Guide.html']:shutil.copy2(ROOT/f,ROOT/'slidev/public'/f)
print(json.dumps({'pdf':path.name,'pages':len(sections),'exercise_slides':exercise}))
