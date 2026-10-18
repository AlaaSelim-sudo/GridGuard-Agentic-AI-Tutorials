"""Normalize the verified revision source records into the shared registry."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent
path=ROOT/'source_map.json'
sources=json.loads(path.read_text(encoding='utf-8'))
sources.update(json.loads((ROOT/'poweragent_powerdag_sources.json').read_text(encoding='utf-8')))
sources.update(json.loads((ROOT/'utility_news_revision.json').read_text(encoding='utf-8'))['source_additions'])
for item in json.loads((ROOT/'agent_definitions_revision.json').read_text(encoding='utf-8'))['sources']:
    item=dict(item)
    item['authors']=item.get('authors') or item.get('authors_as_credited') or item.get('author') or item.get('organization')
    item['date']=item.get('date') or str(item.get('year','Undated'))
    item['pdf_url']=item.get('full_text_url','')
    item['location']='; '.join(item.get('locators',[]))
    sources[item['id']]=item
sources['DEF01']['publisher']='Prentice Hall, second edition, Chapter 2, pp. 32–58'
sources['DEF02']['publisher']='The Knowledge Engineering Review, 10(2), pp. 115–152'
sources['DEF03']['publisher']='Anthropic Engineering'
sources['DEF04']['title']='LangGraph overview'
sources['DEF04']['publisher']='Docs by LangChain, Python open-source documentation'
sources['DEF06']=dict(id='DEF06',title='Tools',authors='LangChain maintainers',
    publisher='Docs by LangChain, Python open-source documentation',date='Accessed 17 October 2026',
    url='https://docs.langchain.com/oss/python/langchain/tools',type='Official tool-interface documentation')
path.write_text(json.dumps(sources,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
