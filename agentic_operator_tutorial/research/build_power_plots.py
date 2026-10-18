"""Rebuild the three measured power-agent research figures from audited source records.

Writes only images/expanded_power_* and the dedicated statistics dictionary.
Run with the bundled Python; shared tutorial builders and manifests are untouched.
"""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "diagrams" / "_rigorous_build" / "pythonpackages"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np

OUT = ROOT / "images"
OUT.mkdir(exist_ok=True)
SOURCE = json.loads((ROOT / "research" / "expanded_power.json").read_text(encoding="utf-8"))
PAPERS = {p["id"]: p for p in SOURCE["papers"]}
BLUE, CYAN, ORANGE, NAVY, GRAY = "#00629B", "#00A8C8", "#B65B14", "#003B5C", "#A6B2BA"
GRID = "#DCE6EC"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 17,
    "axes.labelsize": 17, "axes.titlesize": 18,
    "axes.spines.top": False, "axes.spines.right": False,
    "svg.fonttype": "path", "pdf.fonttype": 42,
    "text.color": NAVY, "axes.labelcolor": NAVY,
    "xtick.color": NAVY, "ytick.color": NAVY
})
records = {}

def finish(fig, basename):
    fig.patch.set_facecolor("white")
    for ext in ("png", "pdf", "svg"):
        fig.savefig(OUT / f"{basename}.{ext}", dpi=220, facecolor="white")
    plt.close(fig)

def style(ax, horizontal=False):
    ax.set_axisbelow(True)
    ax.grid(axis="x" if horizontal else "y", color=GRID, linewidth=.8)
    ax.spines["left"].set_color(GRID)
    ax.spines["bottom"].set_color(GRID)

# P01: compliant full-suite sessions and effort are distinct measured outcomes.
data = PAPERS["P01"]["evaluation"]["results"]
assert [(r["successes"], r["trials"]) for r in data] == [(10,10), (10,10), (9,10)]
ys = np.array([2,1,0])
fig, axes = plt.subplots(1, 2, figsize=(13.2, 4.3),
                         gridspec_kw={"width_ratios":[1.65,1]})
fig.subplots_adjust(left=.16, right=.98, top=.80, bottom=.22, wspace=.26)
ax = axes[0]
for y,r in zip(ys,data):
    ax.barh(y,r["successes"],color=BLUE,height=.48)
    if r["successes"] < r["trials"]:
        ax.barh(y,r["trials"]-r["successes"],left=r["successes"],
                color=ORANGE,height=.48)
    ax.text(r["successes"]/2,y,f'{r["successes"]}/{r["trials"]}',
            ha="center",va="center",fontweight="bold",color="white",fontsize=21)
ax.set(yticks=ys,yticklabels=[r["model"] for r in data],
       xlim=(0,10.25),xticks=[0,2,4,6,8,10],ylim=(-.5,2.5),
       xlabel="Full-suite successes (10 sessions/model)")
ax.legend(handles=[Patch(color=BLUE,label="Passed"),
                   Patch(color=ORANGE,label="Did not pass")],
          frameon=False,loc="lower left",bbox_to_anchor=(-.02,1.05),
          ncol=2,fontsize=15)
style(ax,True)
ax = axes[1]
ax.scatter([r["median_updates"] for r in data],ys,s=135,color=CYAN,zorder=3)
for y,r in zip(ys,data):
    ax.text(r["median_updates"]+.22,y,str(r["median_updates"]),
            va="center",fontweight="bold",fontsize=21)
ax.set(yticks=ys,yticklabels=[],xlim=(0,5.4),xticks=[0,1,2,3,4,5],
       ylim=(-.5,2.5),xlabel="Median model updates")
style(ax,True)
name="expanded_power_dynamic"
finish(fig,name)
records[name]={
 "id":name,"title":"Dynamic-model repair within a restricted action space",
 "caption":"PowerAgentBench-Dyn DMQ case: ten independent sessions per model on one modified WECC solar PV dynamic model. Full-suite compliant success is 10/10 for Opus 4.8, 10/10 for Sonnet 4.6, and 9/10 for Haiku 4.5. Median updates are 1, 1 and 2. Eight quality tests and a maximum of five parameter updates define this case. No confidence interval or fleet-level performance is claimed.",
 "data":data,"source_refs":["P01"],"source_url":SOURCE["source_additions"]["P01"]["url"],
 "locator":"Table II and section III-C, PDF p.3",
 "assumptions":"Author-reported counts and medians reproduced, not independently rerun. One fixed corrupted model; no human or deterministic search comparator.",
 "file":name+".png","pdf":name+".pdf","svg":name+".svg",
 "credit":"Original chart from cited author-reported research results"
}

# P02: preserve the authors' different aggregation definitions and intervals.
data = PAPERS["P02"]["evaluation"]["selected_results"]
fig,ax=plt.subplots(figsize=(13.2,4.5))
fig.subplots_adjust(left=.25,right=.98,top=.75,bottom=.20)
for y,r in zip(ys,data):
    for metric,ci,color,offset,label in [
        ("macro_ja","macro_ja_ci95",BLUE,.14,"Macro joint accuracy"),
        ("overall_fa","overall_fa_ci95",ORANGE,-.14,"Mean field accuracy")]:
        v=r[metric];lo,hi=r[ci]
        assert 0 <= lo <= v <= hi <= 100
        ax.errorbar(v,y+offset,xerr=np.array([[v-lo],[hi-v]]),fmt="o",
                    color=color,ms=9,capsize=5,elinewidth=2,
                    label=label if y==2 else None)
        ax.text(hi+1.4,y+offset,f"{v:.1f}%",va="center",fontsize=16.5,color=color)
ax.set(yticks=ys,yticklabels=[r["model"] for r in data],
       xlim=(0,100),xticks=[0,20,40,60,80,100],ylim=(-.5,2.5),
       xlabel="Reported score (%)")
ax.legend(frameon=False,loc="lower left",bbox_to_anchor=(-.02,1.03),
          ncol=2,fontsize=15.5)
style(ax,True)
fig.text(.25,.94,"Whiskers: author-reported 95% bootstrap intervals",fontsize=14.5)
name="expanded_power_benchmark"
finish(fig,name)
records[name]={
 "id":name,"title":"Complete answers and partial credit measure different outcomes",
 "caption":"Selected PowerBench Table 4 results. Macro Joint Accuracy equally weights the three task families, with 60 temporal, 90 contextual and 150 comparative questions; it is not a correct-count divided by 300. Overall Field Accuracy is the mean per-question fraction of correct fields. Whiskers are author-reported 95% bootstrap intervals, not newly calculated intervals. All three configurations used the same 300-question benchmark and 50-call/300-second retrieval-and-reasoning budgets.",
 "data":data,"questions_per_model":300,"task_family_sizes":{"TRR":60,"CRR":90,"CoRR":150},
 "source_refs":["P02"],"source_url":SOURCE["source_additions"]["P02"]["url"],
 "locator":"Table 4, PDF p.8; aggregation definitions section 4.1 and Appendix D",
 "assumptions":"Different aggregation rules are retained. Partial field credit is not full-task success. Do not infer pairwise significance from marginal interval overlap. Benchmark results are synthetic and author-reported; public runnable release not verified.",
 "file":name+".png","pdf":name+".pdf","svg":name+".svg",
 "credit":"Original chart from cited author-reported scores and bootstrap intervals"
}

# P03: use the same seven queries in both arms of the reported ablation.
ev=PAPERS["P03"]["evaluation"]
assert ev["baseline_stage_executions"] == ev["session_queries"]*ev["stages_per_full_query"]
assert sum(q["stages_run"] for q in ev["query_trace"]) == ev["reuse_stage_executions"]
speed=ev["baseline_wall_seconds"]/ev["reuse_wall_seconds"]
reduction=100*(1-ev["reuse_wall_seconds"]/ev["baseline_wall_seconds"])
assert round(speed,2)==2.12
fig,axes=plt.subplots(1,2,figsize=(13.2,4.3))
fig.subplots_adjust(left=.085,right=.98,top=.80,bottom=.18,wspace=.28)
for ax,vals,title,unit,ylim in [
    (axes[0],[35,14],"60% fewer stage executions","Executed stages",(0,41)),
    (axes[1],[1432.6,677.1],"2.12× wall-time speedup","Session wall time (seconds)",(0,1690))]:
    bars=ax.bar([0,1],vals,color=[GRAY,BLUE],width=.53)
    for bar,v in zip(bars,vals):
        label=str(v) if isinstance(v,int) else f"{v:,.1f}"
        ax.text(bar.get_x()+bar.get_width()/2,v+ylim[1]*.035,label,
                ha="center",fontweight="bold",fontsize=21)
    ax.set(xticks=[0,1],xticklabels=["Full rerun","Artifact reuse"],ylim=ylim,ylabel=unit)
    ax.set_title(title,loc="left",pad=16,fontweight="bold",fontsize=18)
    style(ax)
name="expanded_power_gridmind"
finish(fig,name)
records[name]={
 "id":name,"title":"Artifact reuse saves executions and wall time",
 "caption":"GridMind weather-risk workflow, same seven-query session on a synthetic Texas 2000-bus case. Full-rerun ablation executes 35 stages and takes 1432.6 s; content-addressed reuse executes 14 stages and takes 677.1 s. The stage-count reduction is 60%; the calculated wall-time speedup is 2.1158× (2.12× rounded), corresponding to 52.7363% less wall time. These are different metrics, not two descriptions of the same percentage. No repeated-session uncertainty estimate is reported.",
 "data":{"baseline_stages":35,"reuse_stages":14,"baseline_wall_seconds":1432.6,"reuse_wall_seconds":677.1,
         "stage_reduction_percent":60,"wall_speedup_calculated":speed,"wall_time_reduction_percent_calculated":reduction},
 "source_refs":["P03"],"source_url":SOURCE["source_additions"]["P03"]["pdf_url"],
 "locator":"Table 1 and sections 4.2–4.3, PDF p.4",
 "assumptions":"Same reported query sequence; full-rerun arm uses fresh namespaces. Single simulation session, surrogate screening and reduced-order cascade models. No live utility operation or independently repeated performance claim.",
 "file":name+".png","pdf":name+".pdf","svg":name+".svg",
 "credit":"Original chart from cited author-reported session/ablation measurements"
}
(OUT/"expanded_power_statistics.json").write_text(json.dumps(records,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print("Created three measured-result figures in PNG/PDF/SVG and expanded_power_statistics.json")
