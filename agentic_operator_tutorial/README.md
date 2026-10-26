# Foundations: agentic AI for utility operators

[Open the presentation](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/foundations/#/1) · [Download slides](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/downloads/foundations.pdf) · [Full references](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/foundations/Full_Reading_Guide.html)

**Alaa Selim, MIT/Dartmouth · Mohamed Chehada, UT Austin**

Learn how AI agents choose actions, use engineering tools and respond to feedback. The examples cover utility developments, power-system research, LangGraph, DAGs, result interpretation and evaluation. Original paper figures, company sources and full citations accompany the material.

Continue with the [hands-on workshop](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/1) and its one required Classroom Labs notebook.

Try each exercise before advancing to its worked answer: slides 26 → 27 and 54 → 55. Each answer explains every question and the checks still needed before an operator acts.

The 80-slide presentation opens with a [Google Cloud Tech concept video on slide 6](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/foundations/#/6). Watch 0:43–3:28 to connect tool use and feedback to an agent’s next decision.

Two platform videos follow on slides 47–48:

- [LangChain’s Studio walkthrough](https://www.youtube.com/watch?v=pLPJoFvq4_M): inspect tool calls, returned results and saved state.
- [Siemens Gridscale X PSS E product video](https://video.sw.siemens.com/embed/682ca322-5d0b-47a0-8d18-77bf9d0fb016): connect agentic software to transmission planning. This 79-second supplier overview is not a complete engineering validation.

Click the preview to load each video, or open its official link. The PDF includes clickable previews and full source credits. Slide text and editable TikZ diagrams use Latin Modern, the LaTeX font family; original source figures retain their published lettering.

## Source files

- `slidev/slides.md`: the presentation source.
- `latex/main.pdf`: the slide PDF.
- `Full_Reading_Guide.html` and `.pdf`: papers, documentation and visual credits.
- `research/source_map.json`: source metadata.

<details>
<summary>Build information</summary>

The content originates in `power_content.py` and the existing revision modules. Run `python build_tutorial.py` to regenerate the presentation sources. The project retains its source-image placements, quantitative plots and native TikZ assets. See `build_manifest.json` and `visual_provenance.json` for provenance. The website build is documented in `../web/README.md`.

</details>

Company disclosures, supplier reports, product announcements, research results and teaching examples have different evidence scopes. The independent IEEE ComSoc theme adaptation does not imply IEEE endorsement.
