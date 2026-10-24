"""Prepare the public tutorial's small CPU notebook routes in Google Colab.

Called by the first cell in each current notebook. Git sparse checkout retrieves
only the selected source/data/evidence files; archived evidence is never edited.
"""
from importlib import invalidate_caches, metadata
from pathlib import Path
import os
import subprocess
import sys

WORKSHOP = 'agentic_grid_workflow_tutorial'
TRACE_FILES = (
    'results/workshop_run_opendss.json',
    'results/continuous_llama_opendss_20260927T161223523552Z.json',
    'results/workshop_run_lindistflow3.json',
    'results/continuous_llama_lindistflow3_20260927T161120781113Z.json',
    'results/standard_agent_workflow.json',
    'results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json',
    'results/confirmation.json',
    'results/confirmation_calls.json',
)
CLASSROOM_FILES = (
    'data/',
    'models/continuous_sac/',
    'results/ensemble_voltage_pilot/contexts.json',
    'results/ensemble_voltage_pilot/responses.json',
    'results/ensemble_voltage_pilot/selector_models/linucb_seed_270927.json',
    'results/proposal_complete_workflow.json',
)
PROFILES = {
    'classroom': {
        'files': CLASSROOM_FILES,
        'requirements': 'requirements_colab.txt',
        'packages': ('numpy', 'scipy', 'pandas', 'matplotlib', 'requests'),
        'message': 'Ready: run L0–L12 in order for voltage, restoration and cyber.',
    },
    'graph': {
        'files': ('figures/graph_runtime_flow.svg',),
        'requirements': 'requirements_colab_graph.txt',
        'packages': ('langgraph', 'langchain-core'),
        'message': 'Ready: run G0–G5 in order for the graph and simulated review.',
    },
    'traces': {
        'files': TRACE_FILES,
        'requirements': 'requirements_colab.txt',
        'packages': ('pandas', 'matplotlib'),
        'message': 'Ready: run T1–T9 in order to inspect archived actual records.',
    },
}


def prepare(checkout, profile):
    """Expand an existing sparse clone, install prerequisites and select its cwd."""
    if profile not in PROFILES:
        raise ValueError('Choose classroom, graph or traces.')
    checkout = Path(checkout).resolve()
    if not (checkout / '.git').is_dir():
        raise ValueError('Expected the tutorial Git clone created by the setup cell.')
    settings = PROFILES[profile]
    files = ('src/', settings['requirements'], *settings['files'])
    patterns = ''.join(f'/{WORKSHOP}/{file}\n' for file in files)
    # Add patterns so re-running setup retains files from earlier preparations.
    subprocess.run(
        ['git', '-C', str(checkout), 'sparse-checkout', 'add', '--stdin'],
        input=patterns, text=True, check=True,
    )
    folder = checkout / WORKSHOP
    missing = [file for file in files if not (folder / file).exists()]
    if missing:
        raise FileNotFoundError(f'Supporting files are missing: {missing}')
    print('Preparing packages for a CPU runtime. No GPU or model download is needed.')
    subprocess.run(
        [sys.executable, '-m', 'pip', 'install', '--quiet',
         '-r', str(folder / settings['requirements'])],
        check=True,
    )
    invalidate_caches()
    os.chdir(folder)
    if str(folder) not in sys.path:
        sys.path.insert(0, str(folder))
    os.environ['LANGCHAIN_TRACING_V2'] = 'false'
    os.environ['LANGSMITH_TRACING'] = 'false'
    commit = subprocess.check_output(
        ['git', '-C', str(checkout), 'rev-parse', '--short', 'HEAD'], text=True,
    ).strip()
    print(f'Files: {folder}\nSource revision: {commit}\nPython: {sys.version.split()[0]}')
    print('Packages:', ', '.join(f'{name} {metadata.version(name)}' for name in settings['packages']))
    print(settings['message'])
    print('Setup used the internet. Default lesson cells make no new LLM call.')
    return folder
