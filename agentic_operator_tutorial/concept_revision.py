"""Put a short conceptual video in the existing opening, keeping the route intact."""
from pathlib import Path
import json
def revise(slides):
    video=json.loads((Path(__file__).parent/'content/concept_video.json').read_text(encoding='utf-8'))
    out=[];replaced=0;retimed=0
    for raw in slides:
        s=dict(raw)
        if s['title']=='Workflow or agent: who chooses the next step?':
            s=dict(video);replaced+=1
        elif s['title']=='LangGraph Studio: watch an agent use tools':
            s['minutes']=2.5
            s['note']='Use this time to follow one visible tool-call loop, then pause and discuss. '+s['note']
            retimed+=1
        out.append(s)
    assert replaced==retimed==1
    assert len(out)==80 and sum(s['minutes'] for s in out)==165
    return out
