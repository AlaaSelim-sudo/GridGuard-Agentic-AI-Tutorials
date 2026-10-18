from pathlib import Path
import json
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
from src.selector_display import (DATA, read, scenario_table, initial_candidates,
    response_table, canonical_pool, latency_table, plot_latency,
    model_comparison, plot_model_comparison)
from src.response_selector import LinUCB
from src.selector_pilot_analysis import reward_from_selected_feedback
protocol = read('protocol.json')
analysis = read('selector_analysis.json')
contexts = {c['id']: c for c in read('contexts.json')}
assert analysis['test']['test_updates'] == 0
assert analysis['ac_transfer']['no_retraining_or_tuning']
display(scenario_table().groupby('split', sort=False).size().rename('scenarios').to_frame())
display(scenario_table().tail(4))
print('Actual model configurations:', protocol['models'])
print('Dataset kind:', protocol['data_kind'])
