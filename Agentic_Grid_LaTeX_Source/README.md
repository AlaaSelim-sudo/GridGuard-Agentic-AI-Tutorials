# Editable LaTeX: agentic grid workshop

Graph-teaching edition, 17 October 2026. All figures, exact notebook excerpts, editable technical diagrams and teaching notes are included locally.

- `Agentic_Grid_Lecture.tex`: 72 logical frames, 180 minutes including the break and exercises.
- `Agentic_Grid_Lecture_Handout.tex`: completed version of each lecture frame.
- `Agentic_Grid_Workshop.tex`: lecture plus 68 separate appendix frames, 140 logical frames total.
- `Agentic_Grid_Workshop_Handout.tex`: complete 140-page study handout.

Compile a wrapper with Tectonic or a full TeX installation:

```text
tectonic --keep-intermediates Agentic_Grid_Lecture.tex
tectonic --keep-intermediates Agentic_Grid_Workshop.tex
tectonic --keep-intermediates Agentic_Grid_Workshop_Handout.tex
```

No parent tutorial directory, Python or LLM is required to compile. First-time TeX resources may download. `sections/classroom_*.tex` are the current lecture. The other sections remain as reference source. The source synchronizer belongs to the full tutorial package because it reads the notebooks.

Use page advance to reveal diagram steps, symbols, equations and evidence. Each frame has a Next question and a teaching note with a spoken bridge. Short PDF fades are embedded, but fade support depends on the viewer. Reveal pages work with normal page advance; the handouts show every item at once.

The full tutorial ZIP supplies two executed classroom notebooks: G0–G5 introduce a real LangGraph runtime using a declared toy equation; L0–L12 perform the existing grid exercises. The main engineering workflow remains a custom Python supervisor. The graph example demonstrates scheduling, state, bounded retries and a simulated human pause/resume. It neither calls an LLM nor establishes electrical feasibility.

Exact code mappings and hashes are in `checkpoints.json` and `Slide_Notebook_Map.md`. The source package includes the extracted snippets and can compile without executing notebooks. Current literature is linked at the bottom of the relevant slides. Recorded pilot comparisons retain their own model scope and experiment identity.
