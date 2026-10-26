# Edit and rebuild the hands-on workshop

Use this guide to update the current 80-slide workshop, its presenter script, handouts and website. The standard build uses the supplied figures and archived evidence; it does not run a live model or train a controller.

## Where to make changes

- **Slides:** the five module JSON files in `content/`: `opening`, `voltage`, `restoration`, `cyber`, `closing`.
- **Presenter wording:** `content/presenter_script.json`. Each cue is matched to an exact slide title.
- **Colab delivery:** each cue has `say`, `show`, `colab.mode`, exact stable `cell_ids`, an instruction and expected output. `content/colab_run_route.json` is the quick run sheet. Previews do not run cells.
- **Fonts:** licensed Latin Modern files in `fonts/`, shared helpers in `latin_modern.py`, and web faces in `slidev/styles/latin-modern.css`. The editable slides, script and guides use LaTeX fonts. Original source figures retain their typography.
- **Numerical code:** the canonical sibling `../agentic_grid_workflow_tutorial/Classroom_Labs.ipynb` and its `src/` folder. Thirteen slide excerpts are read by stable cell ID.
- **Sources:** `content/*_sources.json` and the preserved records in `research/`.
- **Figures:** editable TikZ in `diagrams/` and supplied image assets in `images/`. Regenerate matching PDF/SVG assets when changing a diagram.
- **Five-role summary visuals:** `research/plain_language/build_framework_visuals.py`. These map the actual saved L10 records, rather than combining the different L2, L6 and L10B studies.
- **Notebook reading copy:** run `node scripts/export-classroom-notebook.mjs` from the repository root after changing the canonical notebook. This refreshes its HTML and current notebook-download copies without changing the code.
- **Website:** `../web/index.html`, `../web/assets/site.css` and `../scripts/build-pages.mjs`.

`slidev/slides.md`, `latex/frames.tex`, the guides and presenter-script outputs are generated. Edit their source files above for changes that survive a rebuild.

## Authoring setup

From the repository root, use Python with the supplied authoring requirements, Node.js 24 and pnpm 11.25.0:

```text
python -m pip install -r agentic_operator_cases_tutorial/requirements-authoring.txt
pnpm --dir agentic_operator_tutorial/slidev install --frozen-lockfile
pnpm --dir agentic_operator_cases_tutorial/slidev install --frozen-lockfile
```

For PDF generation, install **Tectonic** and Poppler’s **pdftoppm**. Put both executables on PATH, or set `TECTONIC` and `PDFTOPPM` to their executable paths. `NODE` can override the Node executable. These are authoring tools; participants use the one Colab notebook instead.

The main build can use the provided figure PDFs and SVGs. Historical screenshot and diagram-export helpers under `research/` may require their original Windows browser or Poppler DLL configuration; use them when updating those assets.

## Commands

Run these commands from the repository root:

```text
python scripts/build-workshop.py check
python scripts/build-workshop.py content
python scripts/build-workshop.py pdf
python scripts/build-workshop.py site
python scripts/build-workshop.py all
```

- **check:** read-only checks of slide/script coverage, 90-minute timing, three exercises, figure files and thirteen exact notebook excerpts. When a PDF build receipt exists, it also checks that downloads match that build.
- **content:** regenerate Slidev, LaTeX source, source/code guides, and the Markdown/HTML presenter script. PDFs are refreshed by the next command.
- **pdf:** run the content build, regenerate the participant guide and printable presenter script, compile the slide/source PDFs and package downloads. Stops on LaTeX overflow or missing characters.
- **site:** validate the recorded PDF build and assemble both existing decks and the website under `_site/`.
- **all:** run `pdf`, then `site`. This is the full workshop rebuild.

The default website prefix is `/GridGuard-Agentic-AI-Tutorials/`. Override it with `--base /YourRepositoryName/` when building another Pages project.

For slide-only authoring, enter `agentic_operator_cases_tutorial/slidev/` and run `pnpm dev`. Its normal development port is 3044.

## Outputs

- `agentic_operator_cases_tutorial/Three_Operator_Cases.pdf`: the 80-slide deck.
- `Presenter_Script.md`, `.html`, `.pdf`: the 80-slide delivery script.
- `latex/presenter_script.tex`: the editable LaTeX script. Its PDF uses one page per slide cue, a run sheet and three detailed role maps.
- `Participant_Lab_Guide.pdf` and `.html`: learner instructions.
- `Teaching_and_Source_Guide.pdf` and `Full_Reading_Guide.html`: detailed explanations, references and credits.
- `Code_and_Record_Guide.html`: exact notebook sources and recorded-result links.
- `Exercises.html`: the three four-minute tasks.
- `research/presenter/build_receipt.json`: hashes tying the generated PDFs to the current lesson and speaker cues.
- `_site/`: the complete locally built website.

## Review and publish

1. Run `check` and `all` after editing.
2. Inspect the PDF and browser views, especially changed slides, script entries, source links and exercise locations.
3. Keep the full source captions and new/saved/simulated labels intact. Check the 90-minute route and all fifteen notebook code cells in the run sheet.
4. Commit and push the source and generated deliverables to `main` when ready. The existing GitHub Actions Pages workflow publishes them.

The build helper does not make a Git commit, push to GitHub or operate equipment. The foundations source content stays separate; the site build includes its existing presentation.
