# Editable LaTeX teaching slides

**17 October 2026 classroom edition.** Present `Agentic_Grid_Lecture.pdf`: 72 logical frames covering 180 minutes, including the ten-minute break. The executable companions are `../Graph_Workflow_Lab.ipynb` (G0–G5, real LangGraph toy example) and `../Classroom_Labs.ipynb` (L0–L12, engineering cases). All required methods are introduced before their results.

`Agentic_Grid_Workshop.pdf` adds a separately placed 68-frame appendix, giving 140 logical frames. `Agentic_Grid_Workshop_Handout.pdf` contains one completed page per frame; `Agentic_Grid_Lecture_Handout.pdf` contains only the 72 classroom frames. Presentation versions include progressive reveals of diagrams, symbols, equations and outcomes. Every frame has a visible Next question and a short PDF fade transition. Use page advance for each reveal; fades require a supporting viewer. Handouts show the complete content without hidden overlays. PDF page counts can therefore exceed logical frame counts.

The green theme and question/reveal teaching style follow the supplied teaching reference. Equations define their symbols, native diagrams explain mechanisms, and code excerpts are copied from exact notebook cells. Sources are at slide bottoms; each frame contains a timed teaching note and a spoken bridge. The first lesson distinguishes acyclic dependency graphs from bounded feedback graphs, then teaches state updates, reducers, routing and human checkpoints before running the code. Current research covers the 2025–October 2026 grid-agent literature, coordination, skills, governance and evaluation.

## Edit and compile

Edit `sections/classroom_*.tex`; `Agentic_Grid_Workshop.tex` fixes their teaching order. The appendix is a curated static selection of the original section files. The remaining original section files are preserved as optional source, but not all are included in the new PDF.

From the tutorial folder, run `python latex_slides/sync_from_notebook.py` after changing notebooks or excerpts. It updates snippets and validates every displayed range. Compile from this directory:

```text
tectonic --keep-intermediates --keep-logs Agentic_Grid_Lecture.tex
tectonic --keep-intermediates --keep-logs Agentic_Grid_Lecture_Handout.tex
tectonic --keep-intermediates --keep-logs Agentic_Grid_Workshop.tex
tectonic --keep-intermediates --keep-logs Agentic_Grid_Workshop_Handout.tex
```

Rerun the synchronizer after compilation to refresh `frame_pages.json`, `Slide_Notebook_Map.md` and `Instructor_Notes.md`. The `.nav` file supplies presentation page ranges. Use `latexmk -pdf` in a full TeX environment if preferred. First-time TeX resources may require downloads.

The standalone source ZIP includes local copies of figures and snippets, and does not need Python, numerical solvers or Ollama to compile. The source synchronizer requires the full tutorial notebooks and belongs to the complete tutorial package.

## Evidence labels

G cells: real LangGraph teaching example using a declared toy formula and no LLM. L cells: numerical classroom with the existing custom supervisor. E cells: frozen three-model response-selector study. P cells: separate all-stage reference. Other named cells: original numerical and timing lessons. These are not one aggregate experiment. Current notebook default runs fresh numerical calculations with saved model weights and genuine recorded LLM responses. The optional current Llama test has its own record and time. See the instructor guide before interpreting results.
