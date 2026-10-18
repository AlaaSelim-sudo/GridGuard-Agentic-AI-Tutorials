# Live Llama Greensboro tutorial, version 2

This revision runs Llama through the existing Ollama service as the main path.
Default model: llama3.1:8b. Set MODEL to llama3.2:3b to compare.

1. Extract the complete bundle into a writable directory.
2. Install `python -m pip install -r requirements.txt` using Python 3.10+.
3. Start Ollama with an installed Llama model.
4. Launch Jupyter from this directory and open Greensboro_Llama_MultiAgent_Tutorial.ipynb.
5. Run all cells. Missing Ollama/model causes an explicit error, never a fake LLM fallback.

The executed notebook and HTML companion contain recorded live responses and figures.
The full transcript is results/llama_transcript.json. PNG and SVG plots are in results/figures.
The main study records 27 real Llama 3.1 8B calls. A separate preserved Llama 3.2 3B
run supports a single-run comparison. Direct voltage search failed in both runs;
the explicitly labeled physics-guided Llama extension found a passing 33.125% PV
cap. Llama 8B proposed a 50% storage charging action that restored 4.747 MW of
nominal load under the relative restoration check. The malicious-message example
caused an unsafe model proposal, which the independent gate rejected.

Read `Greensboro_Llama_Tutorial.html` to see every plot without running Jupyter.
The updated 15-slide presentation is `Greensboro_Llama_Tutorial_Presentation.pptx`.
`Recorded_Llama3B_Run.ipynb` preserves the earlier model's failures and outputs.
The source subset is SMART-DS uhs20_1247 (three local feeders), not all Greensboro.
Voltage control isolates udt8894. Restoration uses the parent model and a relative
pre-contingency envelope. Parent violations remain. This is not field control.

The episodes are separate reset snapshots, not a time-series day. Llama selects
candidate values, while OpenDSS and Python independently calculate and verify results.
Critical-load priorities, transformer/protection checks and battery duration remain extensions.
One malicious prompt and a few metadata injections cannot establish general cyber robustness.

Source data: https://data.openei.org/submissions/2981
API references: https://docs.ollama.com/api/chat and https://docs.ollama.com/capabilities/structured-outputs
