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
        elif s['title']=='LangGraph demo: pause, inspect and continue':
            s['minutes']=2.5
            s['note']='Use the remaining fifty-one seconds to connect the inspected state to engineering checks. '+s['note']
            retimed+=1
        out.append(s)
    demo=next(s for s in out if s.get('video_id')=='5vEC0Y4sV8g')
    out.remove(demo)
    position=next(i for i,s in enumerate(out) if s['title']=='LangGraph can pause to inspect a run')
    out.insert(position+1,demo)
    assert replaced==retimed==1
    assert len(out)==80 and sum(s['minutes'] for s in out)==165
    return out
