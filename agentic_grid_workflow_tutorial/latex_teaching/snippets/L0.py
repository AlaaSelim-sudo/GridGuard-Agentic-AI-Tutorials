from pathlib import Path
from copy import deepcopy
from dataclasses import asdict
import json, time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display, Markdown
from src import classroom_labs as lab

RUN_OPENDSS = False       # True: fresh full-model audit + separate AC MPC solve in L5
RUN_LOCAL_LLAMA = False   # True: one optional local call in L11
ROOT = Path.cwd()
assert (ROOT / 'data/lindistflow3_network.json').exists(), 'Start Jupyter in the tutorial folder'
plt.rcParams.update({'figure.dpi': 120, 'font.size': 10, 'axes.spines.top': False,
                     'axes.spines.right': False})
pd.set_option('display.max_colwidth', None)
timings = {}
print('Default: fresh linear numerical labs; recorded LLM examples; no training or network.')