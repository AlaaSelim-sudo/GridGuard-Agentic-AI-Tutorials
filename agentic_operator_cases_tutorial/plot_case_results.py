"""Large IEEE-colored charts from exactly recorded classroom/pilot outputs."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent
DATA=ROOT/'research/voltage_plot_data.json'

def save(fig,stem):
    fig.savefig(ROOT/'images'/(stem+'.png'),dpi=180,bbox_inches='tight',pad_inches=.08)
    fig.savefig(ROOT/'images'/(stem+'.pdf'),bbox_inches='tight',pad_inches=.08)
    plt.close(fig)

def main():
    data=json.loads(DATA.read_text(encoding='utf-8'))
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':17,'axes.spines.top':False,
                         'axes.spines.right':False,'axes.labelcolor':'#003b5c','text.color':'#003b5c',
                         'xtick.color':'#526470','ytick.color':'#003b5c','axes.edgecolor':'#526470'})
    rows=data['fresh_L2_notebook']['rows']
    fig,ax=plt.subplots(figsize=(11.8,3.2))
    values=[v['max_allowed_current_pct'] for v in rows]
    ax.barh([1,0],values,color=['#00629b','#00a6b2'],height=.47)
    ax.set_yticks([1,0],['MPC','Saved SAC actor'])
    ax.set_xlim(0,111);ax.set_xticks([0,20,40,60,80,100])
    ax.set_xlabel('Largest current / allowed current (%)')
    ax.axvline(100,color='#b83136',ls='--',lw=1.6)
    ax.text(100,1.46,'Limit',ha='center',color='#b83136',fontsize=16)
    for y,v in zip([1,0],values):ax.text(v+1.2,y,f'{v:.2f}%',va='center',fontsize=19,fontweight='bold')
    ax.spines['left'].set_visible(False);ax.tick_params(axis='y',length=0,pad=12)
    ax.grid(axis='x',alpha=.16);ax.set_axisbelow(True);fig.tight_layout()
    save(fig,'voltage_current_comparison')
    rows=data['paired_ac_active_participation'];x=list(range(1,len(rows)+1))
    fig,ax=plt.subplots(figsize=(11.8,3.45))
    ax.plot(x,[r['mv_a'] for r in rows],'-o',color='#00629b',label='MV incumbent',lw=2.1)
    ax.plot(x,[r['ac_a'] for r in rows],'-s',color='#00a6b2',label='Full-feeder AC MPC',lw=2.1)
    ax.set_ylim(0,1.09);ax.set_yticks([0,.25,.5,.75,1])
    ax.set_xticks(x);ax.set_xlabel('Matched test context');ax.set_ylabel('Active participation a')
    ax.legend(loc='upper center',bbox_to_anchor=(.5,1.34),ncol=2,frameon=False,fontsize=17)
    ax.grid(alpha=.17);ax.set_axisbelow(True);fig.tight_layout()
    save(fig,'voltage_scope_commands')
    path=ROOT/'content/voltage.json';slides=json.loads(path.read_text(encoding='utf-8'))
    slides[3].update(image_source_path=str(ROOT/'images/voltage_current_comparison.png'),
                     image_transformation='New larger vector chart from the stored six-decimal L2 output values; no new numerical experiment.',
                     caption='Replotted stored L2 current checks. 100% is the declared allowed-current limit.')
    slides[3].pop('image_crop',None)
    slides[10].update(image_source_path=str(ROOT/'images/voltage_scope_commands.png'),
                      image_transformation='New larger vector chart from the paired 12-context command records; values unchanged.',
                      caption='Replotted paired command records. Each curve uses a separately planned control; this is not a solver-error plot.')
    path.write_text(json.dumps(slides,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
if __name__=='__main__':main()
