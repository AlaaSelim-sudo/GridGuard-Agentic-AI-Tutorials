import scipy
network = json.loads((ROOT / 'data/lindistflow3_network.json').read_text())
casebook = {case.id: case for case in cases()}
continuous_casebook = {case.id: case for case in continuous_cases()}
training = json.loads((ROOT / 'models/continuous_sac/training.json').read_text())
print('Python', platform.python_version(), '| NumPy', np.__version__, '| SciPy', scipy.__version__)
print('Selected model:', BACKEND, '| Saved policy:', training['configuration']['algorithm'])
print('Training transitions:', training['configuration']['steps'], '| Seed:', training['configuration']['seed'])
print('Continuous actor provenance:', training['actor_sha256'])
print('Synthetic data and overlays: data/DATA_SOURCE.md; model limits: appendix/Scientific_Notes.md')
