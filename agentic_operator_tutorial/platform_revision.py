"""Replace overlapping GridAgent paper blocks with two official platform demos."""
from pathlib import Path
import json

def revise(slides):
    videos=json.loads((Path(__file__).parent/'content/platform_videos.json').read_text(encoding='utf-8'))
    replacements=[]
    for v in videos:
        replacements.append(dict(kind='video',title=v['title'],eyebrow='Official developer demo' if v['id']=='VID01' else 'Official grid-platform video / 79 seconds',minutes=4,
            image=v['image'],video_id=v['video_id'],video_url=v['video_url'],embed_url=v['embed_url'],
            points=v['points'],refs=[v['id']],caption=v['publisher']+' / '+v['date'],
            takeaway='',note=v['say']+' Play the official video on click or use the direct watch link. Pause to identify the selected tool, its returned result and the next decision. Ask: '+v['question']+' Answer: '+v['answer']))
    output=[]
    for slide in slides:
        if slide['title'].startswith('X-GridAgent divides'):output.extend(replacements)
        elif slide['title'].startswith(('X-GridAgent results','Grid-Agent tests','Grid-Agent results')):continue
        else:
            slide=dict(slide)
            if slide['title'].startswith('MCP connects'):
                slide['refs']=[key for key in slide['refs'] if key!='E01']
                slide['note']='MCP standardizes messages between an application and its tool servers. It does not select the correct study, validate a solver result or authorize an operating action. Those checks belong to the application and operator.'
            output.append(slide)
    # Keep source credits clear after the change to wider Roman letterforms.
    for n,height in {30:3.9,32:2.9,34:3.8,40:3.7,49:2.55,51:3.6,52:3.2,55:3.5,58:3.2,64:3.65}.items():
        output[n-1]['visual_height_cm']=height
    output[14]['focus_height_cm']=4.4
    output[14]['points']=[
        'NYPA describes checks on meter data before AI uses it.',
        'A separate MCP demo uses product data. It does not show NYPA grid control.'
    ]
    for n in (52,55,58):output[n-1]['visual_height_px']=300
    output[46]['note']=videos[1]['say']+' After the video, ask which study inputs and numerical checks a planner would need. The overview does not show a complete tool-call trace. Question: '+videos[1]['question']+' Answer: '+videos[1]['answer']
    output[37]['refs']=[key for key in output[37]['refs'] if key!='E01']
    output[37]['main_ref']='LG01'
    output[37]['note']='Independent outage studies should use the same frozen starting case. Collect results by outage ID, compare the returned IDs with the requested set, and preserve failed or missing studies as unresolved. The original parallel-workflow figure illustrates coordination; it does not establish complete electrical coverage.'
    assert len(output)==78
    assert sum(s['minutes'] for s in output)==165
    return output
