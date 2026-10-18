"""Final source-image placements, after the plain-language teaching revision."""
from pathlib import Path
from copy import deepcopy
import json
ROOT=Path(__file__).resolve().parent

def revise(slides):
    result=deepcopy(slides)
    plan=json.loads((ROOT/'research/real_image_slide_plan.json').read_text(encoding='utf-8'))
    for change in plan:
        item=result[change['slide']-1]
        assert item['title']==change['expected_title'],(change['slide'],item['title'])
        if change.get('replace_visual'):
            if item.get('diagram'):item['alternative_tikz']=item['diagram']
            item.update(diagram=None,image2=None,math_tex='',math_html='',excerpt=[],callout='')
        for field,value in change['changes'].items():item[field]=value
        for old,new in change.get('note_replacements',{}).items():
            assert old in item['note'],(change['slide'],old)
            item['note']=item['note'].replace(old,new)
        for ref in change.get('add_refs',[]):
            if ref not in item['refs']:item['refs'].append(ref)
        item['note']+=(' '+change.get('source_note',''))
    return result
