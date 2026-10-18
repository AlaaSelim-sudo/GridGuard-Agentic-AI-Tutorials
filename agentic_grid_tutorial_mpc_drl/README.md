# Agentic AI for grid operators: three-hour tutorial

Start with **Agentic_Grid_3Hour_MPC_DRL.html** for a readable preview, or open **Agentic_Grid_3Hour_MPC_DRL.ipynb** in Jupyter for the full laboratory. Present with **Agentic_Grid_3Hour_MPC_DRL_Presentation.pptx**. The deck contains 46 slides with timed speaker notes. **Instructor_Guide.md** provides the teaching plan and interpretation guidance.

This standalone implementation follows the supplied multi-agent proposal. It uses one synthetic Greensboro feeder, real local Llama inference, OpenDSS simulation and independent verification. It contains two voltage cases, two restoration cases and 14 cyber/benign fixtures, including three actual prompt-injection trials.

## Local setup

Use Python 3.11 or newer. From the extracted tutorial directory:

```text
python -m venv .venv
```

Activate the environment using the command appropriate for your system, then:

```text
python -m pip install -r requirements.txt
jupyter lab
```

Run Ollama with `llama3.1:8b` available. If it is already running, reuse it. The notebook defaults to `http://localhost:11434`. `ollama list` shows installed models; `ollama pull llama3.1:8b` downloads it if needed. The model is about 5 GB in the recorded installation. The supplied model digest and installed package versions are in `results/metadata.json` and `results/environment.json`.

Open the notebook from this folder. It runs a seven-call live R2 demonstration by default, while loading the complete recorded benchmark for comparison. To study without Ollama, set `RUN_LIVE_DEMO=False` and use its saved actual transcript. There is no fake-response fallback. A remote notebook's localhost is not your laptop's Ollama service.

## Reproduce the study

Run these from the extracted tutorial directory with the environment active:

```text
python -m src.validate
python -m src.experiments
python -m src.plots
```

The experiment command overwrites the benchmark records with a fresh study, including 123 actual model calls. Copy the `results` directory before a new experiment if you want to retain the supplied evidence. The plotting command regenerates the figures. The PowerPoint contains a snapshot of the supplied results and does not automatically update after a rerun.

The notebook's `RUN_FULL_BENCHMARK=True` runs both experiments and plot regeneration. New model/runtime versions or hardware can change action sequences despite fixed seeds. The notebook demonstration logs to separate files and preserves the benchmark.

## Contents

- `src/power_tools.py`: independent feeder reset, simulation, electrical metrics and checks.
- `src/framework.py`: action catalog, scenario definitions, Llama API client and bounded role orchestration.
- `src/experiments.py`: baselines, two-seed comparisons, catalog reference and cyber fixtures.
- `src/plots.py`: nine scientific figures, exported as PNG and SVG.
- `src/validate.py`: regression checks for key electrical and policy boundaries.
- `data/greensboro_udt8894`: the original selected SMART-DS feeder inputs.
- `generated`: compatible working copies of the DSS inputs, recreated by the tools if absent.
- `results`: raw histories, exact model messages, source manifest and model metadata.

## Interpretation

The catalog reference is exhaustive only over the declared actions. It is not a global AC OPF solution. Four-slot methods have equal candidate opportunities but different inference costs. The rule-based search is a strong informed baseline and is much faster on these small cases. Report feasibility alongside conditional objective gap.

Bypasses, priority labels and individual load-relay control are explicit teaching assumptions. Cyber evidence fields are injected fixtures, not an authenticated telemetry or intrusion-detection implementation. The notebook documents the unimplemented engineering constraints and a stealth-bias test that passes the simple residual check.

## Data and research sources

Electrical data: [SMART-DS, OEDI submission 2981](https://data.openei.org/submissions/2981), selected Greensboro `uhs20_1247 / udt8894` feeder, extreme-solar/high-storage source case. Original source files are retained and hashed. Consult the source repository's terms when redistributing the data.

The notebook and slide notes cite ReAct, OPRO, branch-flow modeling, restoration radiality research, NIST adversarial-machine-learning terminology, OpenDSSDirect and Ollama documentation. The scientific claims about this implementation come from the included experimental records.


## New MPC and DRL comparison

Read `Comparison_Lab.md` for the design, measured findings and attribution limits. The new implementation includes finite-action receding-horizon economic MPC and three independently trained DQNs (two hidden layers, replay, target network). Updated MPC and shielded DQN receive the same checker/constraints as the agentic supervisor.

Reproduce from this folder:

```text
python -m src.conventional
python -m src.event_interpretation
python -m src.conventional_plots
```

Existing DQN weight files are reused. To retrain, move each `results/conventional/dqn_seed_*.npz` file to a backup folder first. The 18,000-step training history for each of three seeds is included. The new numerical controller experiment is voltage-only; the original restoration and cyber lessons remain separate.

The shared AC table makes controller timing a cached-model measurement. Read `table_cost.json` and the training records for offline costs. New Llama calls use separate transcripts. Interpreted maintenance notes are proposals only and were not applied to the numerical experiment.
