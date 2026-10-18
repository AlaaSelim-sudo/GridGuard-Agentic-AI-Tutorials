"""Extract the original DrAgent waveform and plot audited published cell counts."""
from pathlib import Path
import json, os, sys, tempfile, subprocess
from pypdf import PdfReader, PdfWriter

ROOT=Path(__file__).resolve().parent.parent
IMAGES=ROOT/'images'
sys.path.insert(0,str(ROOT/'diagrams/_rigorous_build/pythonpackages'))
os.environ.setdefault('MPLCONFIGDIR',str(Path(tempfile.gettempdir())/'power_study_matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

URL='https://www.manuscriptlink.com/society/kics/media?key=kics%2Fconference%2Ficaiic2025%2Fpresentation%2F1571098105.pdf'
paper=ROOT.parents[1]/'tmp/operator_tutorial/DrAgent.pdf'
page=PdfReader(paper).pages[3]
# Native PDF clipping only; no traces are reconstructed or modified.
page.mediabox.lower_left=(316,562)
page.mediabox.upper_right=(558,744)
page.cropbox=page.mediabox
writer=PdfWriter();writer.add_page(page)
with (IMAGES/'power_dragent_waveform.pdf').open('wb') as handle:writer.write(handle)
poppler=Path(r'C:/Users/f00863x/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe')
subprocess.run([str(poppler),'-png','-singlefile','-r','300','-cropbox',str(IMAGES/'power_dragent_waveform.pdf'),str(IMAGES/'power_dragent_waveform')],check=True)

audit=json.loads((ROOT/'research/dragent_count_audit.json').read_text(encoding='utf-8'))
rows=[('Fault inception (Q2)','Q2'),('Maximum current (Q5)','Q5'),('Clearance / timing (Q6)','Q6')]
fig,ax=plt.subplots(figsize=(12,3.6))
fig.subplots_adjust(left=.32,right=.96,top=.87,bottom=.25)
for i,(label,key) in enumerate(rows):
    item=audit['results'][key]
    for j,(field,color,legend) in enumerate([('baseline_correct','#00629B','Non-agent baseline'),('agent_correct','#00A8C8','DrAgent')]):
        y=i*1.2+(-.2 if j==0 else .2)
        value=item[field]
        ax.barh(y,value,height=.33,color=color,label=legend if i==0 else None)
        ax.text(value+.18,y,f'{value}/18',ha='left',va='center',fontsize=18,weight='bold',color='#003B5C')
ax.set_yticks([0,1.2,2.4],[x[0] for x in rows]);ax.invert_yaxis()
ax.set_xlim(0,20.8);ax.set_xticks([0,3,6,9,12,15,18])
ax.set_xlabel('Correct answers under the expert rubric (score >= 2)',fontsize=18,color='#003B5C',labelpad=9)
ax.tick_params(axis='y',length=0,pad=12,labelsize=20,colors='#003B5C')
ax.tick_params(axis='x',labelsize=15,colors='#74828C')
ax.set_axisbelow(True);ax.grid(axis='x',color='#D9E3E9',linewidth=.8)
for spine in ax.spines.values():spine.set_visible(False)
ax.legend(loc='lower left',bbox_to_anchor=(0,1.01),ncols=2,frameon=False,fontsize=17,labelcolor='#003B5C',borderaxespad=0)
for ext in ('png','pdf','svg'):fig.savefig(IMAGES/f'power_dragent_counts.{ext}',dpi=220,facecolor='white')
plt.close(fig)
manifest=[dict(file='power_dragent_waveform.png',credit='Saha, V and Naidu / Hitachi Energy, DrAgent, ICAIIC 2025, Figure 2',
 source_page_url=URL,direct_image_url=URL,asset_type='Original scientific figure, native PDF crop',
 caption='DrAgent Figure 2, PDF p.4: recorded current and voltage traces. Original trace data and event markers preserved.',
 evidence_limit='A sample disturbance record from a research paper; not a live utility operating display.',
 transformation='Clipped to the original figure boundary; caption excluded and credited separately; no plotted data changed.',source_refs=['D01'])]
(IMAGES/'power_disturbance_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
stats={'power_dragent_counts':dict(file='power_dragent_counts.png',source_refs=['D01'],source_url=URL,
 source_locator='PDF p.6 Table IV and p.8 Appendix; score definitions p.5 Table II; Q6 exception p.7 footnote 8',
 caption=audit['proposed_plot_caption'],assumptions=' '.join(audit['limits'])+' Q6 printed mean is inconsistent; audited cell counts are used instead.',
 data={key:{k:item[k] for k in ('baseline_correct','agent_correct','denominator')} for key,item in audit['results'].items()},
 credit='Original educational plot derived from published DrAgent score cells; no experiments rerun.')}
(IMAGES/'power_disturbance_statistics.json').write_text(json.dumps(stats,indent=2)+'\n',encoding='utf-8')
