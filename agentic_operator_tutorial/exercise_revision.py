"""Show questions first, then a complete worked answer on the next slide."""
from pathlib import Path
import json
def revise(slides):
    answers=json.loads((Path(__file__).parent/'content/exercise_answers.json').read_text(encoding='utf-8'))
    out=[];index=0
    for raw in slides:
        s=dict(raw)
        if s['kind']=='exercise':
            answer=dict(answers[index]);answer['answer_for']=s['title'];index+=1
            s['minutes']-=answer['minutes']
            s['note']='Show only the question during the activity. Use the following worked-answer slide for the debrief. '+s['note'].replace('Keep these answers in the speaker notes.','').strip()
            s['eyebrow']='Work in pairs / 5 minutes, then 1-minute answer' if index==1 else 'Group exercise / 6 minutes, then 2-minute answer'
            out.extend([s,answer])
        else:out.append(s)
    assert index==2 and len(out)==80
    assert sum(s['minutes'] for s in out)==165
    return out
