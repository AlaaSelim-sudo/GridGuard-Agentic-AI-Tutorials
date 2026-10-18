"""Redraw the GPT-5.5 PowerDAG v4 same-model configuration comparison."""
from pathlib import Path
import json
import os
import sys
import tempfile

ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'diagrams'/'_rigorous_build'/'pythonpackages'))
os.environ.setdefault('MPLCONFIGDIR',str(Path(tempfile.gettempdir())/'power_revision_matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image

IMAGES=ROOT/'images'
STEM='powerdag_revision_result'
data=json.loads((ROOT/'research'/'poweragent_powerdag_revision.json').read_text(encoding='utf-8'))
spec=data['powerdag']['table_II']['selected_same_model_ablation']
rows=spec['rows']

def main():
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':15,'svg.fonttype':'path','pdf.fonttype':42})
    fig,ax=plt.subplots(figsize=(12,3.6),facecolor='white')
    fig.subplots_adjust(left=.27,right=.97,top=.96,bottom=.25)
    labels=['ReAct baseline','Retrieval only','JIT only','Full PowerDAG']
    values=[r[1] for r in rows]
    ax.barh(range(4),values,height=.48,color=['#74828C','#00629B','#B65B14','#00A8C8'])
    ax.set_yticks(range(4),labels,fontsize=21,color='#003B5C')
    ax.invert_yaxis()
    ax.set_xlim(0,109)
    ax.set_xticks([0,20,40,60,80,100])
    ax.tick_params(axis='y',length=0,pad=12)
    ax.tick_params(axis='x',labelsize=15,colors='#74828C')
    ax.set_xlabel('Workflow Pass@1 (%)',fontsize=19,color='#003B5C',labelpad=9)
    ax.set_axisbelow(True)
    ax.grid(axis='x',color='#D9E3E9',linewidth=.8)
    for spine in ax.spines.values():spine.set_visible(False)
    for y,v in enumerate(values):
        ax.text(v+1.3,y,f'{v:.2f}',va='center',fontsize=23,weight='bold',color='#003B5C')
    fig.canvas.draw()
    renderer=fig.canvas.get_renderer()
    width,height=fig.canvas.get_width_height()
    for artist in fig.findobj(matplotlib.text.Text):
        if artist.get_visible() and artist.get_text().strip():
            b=artist.get_window_extent(renderer)
            assert b.x0>=-1 and b.y0>=-1 and b.x1<=width+1 and b.y1<=height+1,(artist.get_text(),b.bounds)
    for ext in ('png','pdf','svg'):
        fig.savefig(IMAGES/f'{STEM}.{ext}',dpi=220,facecolor='white',metadata={'Creator':'Power-system tutorial research chart builder'})
    plt.close(fig)
    record={
        'id':STEM,'plot_id':STEM,'file':STEM+'.png','pdf':STEM+'.pdf','svg':STEM+'.svg',
        'source_refs':['PD01','PD02'],'source_url':'https://arxiv.org/pdf/2603.17418v4',
        'source_locator':'PowerDAG v4 TableII, PDF p.8; evaluation definition sectionV.E, pp.6–7',
        'metric':'Workflow Pass@1 (%)','model':'GPT-5.5','denominator':150,
        'data':[{'configuration':r[0],'reported_percent':r[1]} for r in rows],
        'caption':'PowerDAG v4 same-model comparison on150 held-out distribution-grid queries: GPT-5.5 ReAct77.33%, adaptive-retrieval-only92.67%, JIT-supervision-only96.00%, fullPowerDAG98.00%. Each query is run once per model/configuration; no experiments rerun.',
        'assumptions':'Pass@1 checks expert tool coverage, compatible arguments and dependency ordering. Four real-world feeder models and ten task families; within-family holdout, not field reliability. No run-to-run interval is inferred. Public network-dependent reruns require proprietary data/tools; only3of10families are fully runnable publicly.',
        'credit':'Original vector plot redrawn from author-reported PowerDAG v4 numerical results',
        'value_status':'Author-reported percentages; plotted values are not reconstructed success counts',
        'uncertainty_intervals':None,
    }
    (IMAGES/'power_revision_statistics.json').write_text(json.dumps({'powerdag_result':record},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    with Image.open(IMAGES/(STEM+'.png')) as im:
        assert im.size==(2640,792)
        im.verify()
    assert b'/Subtype /Image' not in (IMAGES/(STEM+'.pdf')).read_bytes()
    assert '<image' not in (IMAGES/(STEM+'.svg')).read_text(encoding='utf-8')
    print(json.dumps({'chart':STEM,'formats':['png','pdf','svg'],'manifest':'images/power_revision_statistics.json'}))

if __name__=='__main__':main()
