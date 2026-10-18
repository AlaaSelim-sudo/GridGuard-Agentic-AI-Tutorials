from pathlib import Path
import json
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from IPython.display import display, Markdown
from src.trace_latency import (load_recorded_evidence, stage_rows,
    plot_workflow_latency, plot_call_latency)
ROOT = Path.cwd()
evidence = load_recorded_evidence(ROOT)
pd.set_option('display.max_colwidth', 180)
print(f"Matched {len(evidence['calls'])} calls; {len(evidence['workflows'])} workflow intervals.")
print(evidence['caveat'])
