"""Acquire publisher-authored framework illustrations without changing their content.

Network access is required only to reacquire originals. Display variants trim
blank margins via a viewport and retain an embedded copy of the original bytes.
"""
from pathlib import Path
import base64, hashlib, io, json, urllib.parse, urllib.request
from html.parser import HTMLParser
from PIL import Image, ImageChops

ROOT=Path(__file__).resolve().parents[1]
IMAGES=ROOT/'images'
class Images(HTMLParser):
    def __init__(self): super().__init__();self.items=[]
    def handle_starttag(self,t,attrs):
        if t=='img': self.items.append(dict(attrs))
PAGES={
 'anthropic':'https://www.anthropic.com/engineering/building-effective-agents',
 'workflow':'https://docs.langchain.com/oss/python/langgraph/workflows-agents',
 'checkpoints':'https://docs.langchain.com/oss/python/langgraph/checkpointers',
 'interrupt':'https://docs.langchain.com/oss/python/langgraph/interrupts',
 'nvidia2026':'https://developer.nvidia.com/blog/building-for-the-rising-complexity-of-agentic-systems-with-extreme-co-design/',
 'nvidia2023':'https://developer.nvidia.com/blog/introduction-to-llm-agents/',
}
SPECS=[
 ('anthropic_prompt_chain','anthropic',2,'The prompt chaining workflow','Workflow: Prompt chaining',['DEF03'],[20],
  'Anthropic shows fixed model calls with a gate between them. A gate checks an intermediate result before the sequence continues.',
  'A generic content-workflow pattern, not a physical-feasibility or utility-safety guarantee.'),
 ('anthropic_routing','anthropic',3,'The routing workflow','Workflow: Routing',['DEF03'],[6],
  'Anthropic shows a router selecting one specialized path. A conditional route alone does not make an entire application autonomous.',
  'The picture illustrates routing; it does not establish an implemented power-system workflow.'),
 ('anthropic_parallel','anthropic',4,'The parallelization workflow','Workflow: Parallelization',['DEF03'],[38],
  'Anthropic shows independent calls joined by an aggregator. The power-study example also has to track which outage results arrived.',
  'The aggregator picture does not imply that missing results are automatically detected.'),
 ('anthropic_orchestrator','anthropic',5,'The orchestrator-workers workflow','Workflow: Orchestrator-workers',['DEF03'],[2],
  'Anthropic shows an orchestrator assigning work and combining worker results. Multiple agents are one possible pattern, not a requirement for agentic AI.',
  'One practitioner pattern; not a universal definition and not a utility deployment diagram.'),
 ('anthropic_evaluator','anthropic',6,'The evaluator-optimizer workflow','Workflow: Evaluator-optimizer',['DEF03'],[19],
  'Anthropic shows generation, evaluation and revision. In a grid application, software and engineering checks must test the recommendation too.',
  'An LLM evaluator does not prove grid feasibility, permission or fresh input data.'),
 ('langgraph_workflow_agent','workflow','Agent Workflow','Agent tool-and-feedback loop','Opening workflow comparison: selected Agent panel',['LG04'],[6],
  'The agent panel in the official LangGraph guide shows a model choosing a tool action and reading feedback before another step.',
  'This documentation convention concerns LLM applications, not all classical AI agents.'),
 ('langgraph_checkpoint','checkpoints','Checkpoints','Saved checkpoints in a thread','Opening checkpoint illustration',['LG05','LG02'],[37],
  'LangGraph saves state at graph super-step boundaries. A checkpoint supports resuming a run; data freshness still needs a separate check.',
  'Saved software state does not prove that an external grid snapshot remains current.'),
 ('langgraph_state','checkpoints','State','Inspecting state history','Get state history',['LG05','LG02'],[36],
  'The official figure shows saved states linked to execution steps. A grid study must also record the case, time and evidence identifiers.',
  'The extra grid identifiers are tutorial requirements; they are not fields proven by this generic illustration.'),
 ('langgraph_interrupt_form','interrupt','Studio interrupt form','Human response to a paused workflow','Interrupt response schema / Studio form',['LG03'],[7],
  'The official Studio screenshot shows a person providing a response to a paused workflow. A utility would define its own permitted response and review rules.',
  'This is a generic software demonstration, not an operator dispatch interface or a utility deployment.'),
 ('langgraph_static_interrupt','interrupt','image','A graph paused at a breakpoint','Debugging with interrupts',['LG03'],[35],
  'The official documentation screenshot shows a graph paused for inspection. Runtime control and review are separate from the power model.',
  'A static debug breakpoint differs from a dynamic interrupt requesting human input.'),
 ('nvidia_interaction_patterns','nvidia2026','A diagram comparing three AI interaction patterns','Chat, tools and agentic interaction patterns','Figure 1',['NV01'],[3],
  'NVIDIA compares a chatbot exchange, a tool-using exchange and a longer agentic sequence. An agent can use a generative model to choose its next action.',
  'The three examples show interaction patterns, not a universal taxonomy or a claim that tool use alone proves autonomy.'),
 ('nvidia_agent_components','nvidia2023','Architecture diagram of an LLM-powered agent.','Components of one LLM-agent architecture','Figure 1: General components of an agent',['NV02'],[5],
  'NVIDIA places an agent core between the request, tools, planning and memory. The model requests work; connected tools perform the requested operations.',
  'This is a published conceptual design; separate memory or planning modules are not required in every AI agent.'),
]

def fetch(url):
    req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
    return urllib.request.urlopen(req,timeout=45).read()

def main():
    parsed={}
    for key,url in PAGES.items():
        p=Images();p.feed(fetch(url).decode('utf8'));parsed[key]=p.items
    result=[]
    for stem,page,index,title,locator,refs,slides,caption,limit in SPECS:
        imgs=parsed[page]
        item=imgs[index] if isinstance(index,int) else next(x for x in imgs if (x.get('alt')==index or x.get('alt','').startswith(index)))
        url=item['src']
        if url.startswith('/_next/image'):
            url=urllib.parse.parse_qs(urllib.parse.urlparse(url).query)['url'][0]
        # Request original publisher file rather than an optimized thumbnail.
        if url.startswith('https://mintcdn.com/'): url=url.split('?')[0]
        if stem=='nvidia_agent_components':
            url='https://developer-blogs.nvidia.com/wp-content/uploads/2023/11/agent-components.png'
        raw=fetch(url);im=Image.open(io.BytesIO(raw));ext='jpg' if im.format=='JPEG' else 'png'
        name='real_framework_'+stem
        original=IMAGES/(name+'_original.'+ext);original.write_bytes(raw)
        rgb=im.convert('RGB');inner=rgb.crop((5,5,im.width-5,im.height-5))
        diff=ImageChops.difference(inner,Image.new('RGB',inner.size,'white'))
        # Preserve every original element, including faint gray arrows; 24px safe padding.
        mask=diff.point(lambda v:255 if v>7 else 0).convert('L');box=mask.getbbox() or (0,0,*im.size)
        x0,y0,x1,y1=box;x0=max(0,x0+5-24);y0=max(0,y0+5-24);x1=min(im.width,x1+5+24);y1=min(im.height,y1+5+24)
        selected_excerpt=False
        if stem=='langgraph_workflow_agent':
            # Only the original agent panel, excluding the source's dense comparison grid.
            x0,y0,x1,y1=2960,480,4480,1280;selected_excerpt=True
        elif stem=='langgraph_checkpoint':
            x0,y0,x1,y1=15,0,1520,650;selected_excerpt=True
        elif stem=='langgraph_state':
            x0,y0,x1,y1=780,265,1580,750;selected_excerpt=True
        w,h=x1-x0,y1-y0
        mime='image/jpeg' if ext=='jpg' else 'image/png'
        svg=(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="{x0} {y0} {w} {h}">'
             f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="white"/>'
             f'<image width="{im.width}" height="{im.height}" href="data:{mime};base64,{base64.b64encode(raw).decode()}"/></svg>')
        (IMAGES/(name+'.svg')).write_text(svg,encoding='utf8')
        # Companion PDF places the unchanged original image behind the same viewport.
        from reportlab.pdfgen.canvas import Canvas
        from reportlab.lib.utils import ImageReader
        c=Canvas(str(IMAGES/(name+'.pdf')),pagesize=(w,h))
        c.drawImage(ImageReader(io.BytesIO(raw)),-x0,y1-im.height,width=im.width,height=im.height)
        c.save()
        result.append(dict(id=name,title=title,file=name+'.svg',path='images/'+name+'.svg',
          original_file=original.name,width=w,height=h,original_width=im.width,original_height=im.height,
          bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),source_page_url=PAGES[page],direct_image_url=url,
          source_url=PAGES[page],original_image_url=url,source_locator=locator,source_refs=refs,proposed_slides=slides,
          credit=('Source: Anthropic, Building effective agents (December 19, 2024).' if page=='anthropic' else 'Source: NVIDIA Technical Blog, Figure 1.' if page.startswith('nvidia') else 'Source: LangChain documentation maintainers, official LangGraph documentation. Accessed October 18, 2026.'),
          caption=caption,evidence_limit=limit,assumptions=limit,
          transformation=('Selected original figure panel excerpt; no labels, arrows or pixels edited. Entire original image retained separately.' if selected_excerpt else 'Only blank outer margins trimmed by display viewport; original image bytes are embedded unchanged and also retained as a separate original file.'),
          crop_viewport=[x0,y0,w,h],license_or_permission_status='Publisher attribution supplied. No separate permission or unrestricted reuse license claimed.',
          recommended=True,
          visual_qa='Pending full-size inspection.'))
        print(name,im.size,'display',(w,h))
    manifest=IMAGES/'power_real_framework_manifest.json'
    if manifest.exists():
        result += [x for x in json.loads(manifest.read_text(encoding='utf8'))['images'] if x['id'].startswith('real_framework_mcp_')]
    manifest.write_text(json.dumps({'images':result},indent=2),encoding='utf8')
if __name__=='__main__': main()
