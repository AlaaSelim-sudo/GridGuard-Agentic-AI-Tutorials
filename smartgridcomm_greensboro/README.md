# Greensboro multi-agent grid tutorial

Open `Greensboro_MultiAgent_Tutorial.ipynb` for the complete executed tutorial.
Open `Greensboro_Tutorial_Presentation.pptx` for the accompanying editable slides.
The selected area is SMART-DS `uhs20_1247`, not all Greensboro. Voltage uses its
`udt8894` leaf feeder; restoration retains three local feeders for the tie source.

## Run locally
1. Unzip the complete bundle to a writable directory.
2. Use Python 3.10 or later and install `python -m pip install -r requirements.txt`.
3. Launch `jupyter lab`, open the notebook, and run all cells in order.

## Run in Colab
Upload and unzip the bundle, change into the extracted directory and run
`%pip install -r requirements.txt`. Open or copy the notebook cells into Colab.
No local Ollama service is reachable from Colab unless you explicitly configure one.

The default run needs no model, credentials or GPU. Optional live LLM cells need
an Ollama server and an installed model selected using OLLAMA_MODEL.
Do not expose an unauthenticated model endpoint to the public internet.

The subset includes original SMART-DS input files (about 4 MB). Compatibility
overlays rebuild on each machine; original input files remain unchanged.
Source: https://data.openei.org/submissions/2981 (synthetic network data).

Results are static simulations, not field control. The restoration certificate is
relative to a pre-contingency envelope with existing violations. Absolute radiality,
transformer/protection coordination, battery duration and critical-load optimization
are not demonstrated. Cyber examples are controlled interface and policy injections.
The default results do not measure LLM performance or operator time savings.

`results/study_summary.json` links the presentation to computed evidence.
The HTML notebook companion permits reading results without a Jupyter installation.
