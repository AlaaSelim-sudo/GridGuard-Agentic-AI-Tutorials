from pathlib import Path
from datetime import datetime, timezone
import json, platform
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display, HTML, Image
from src.standard_formulations import PQBackend, run_voltvar, solve_restoration_milp, run_wls_demo
from src.stage_workflow import ElectricalModel, cases, run_stages
from src.continuous_control import (ContinuousPlant, cases as continuous_cases,
    load_policy as load_continuous_policy, sac_proposal, verify_control,
    optimize_mpc as optimize_continuous_mpc)
from src.continuous_workflow import (workflow_roles, request_contract, review_requirements,
    ContinuousLlama, run_continuous_workflow, point_summary)
from src.workshop_review import SCHEMA, comparison_rows, save_workshop_run
from src.workshop_display import (read_record, show_trace, table_rows, plot_voltage,
    plot_continuous_checks, plot_restoration, plot_cyber, plot_trusted_control)
ROOT = Path.cwd()
BACKEND = 'lindistflow3'  # OpenDSS audience: change to 'opendss'.
LIVE_LLM = True          # False explicitly selects recorded continuous-workflow responses.
assert (ROOT / 'data/lindistflow3_network.json').exists()
assert BACKEND in ('lindistflow3', 'opendss')
plt.rcParams.update({'font.size': 11, 'axes.spines.top': False, 'axes.spines.right': False})
from src.case_comparisons import voltage_comparison, restoration_language_comparison, cyber_comparison
