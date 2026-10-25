# Online tutorial site

The audience home page links to both Slidev presentations, notebooks, PDF downloads and teaching guides.

## Build locally

Use Node.js 24 and pnpm 11.25.0. From the repository root:

```text
pnpm --dir agentic_operator_tutorial/slidev install --frozen-lockfile
pnpm --dir agentic_operator_cases_tutorial/slidev install --frozen-lockfile
node scripts/build-pages.mjs --base /GridGuard-Agentic-AI-Tutorials/
```

Serve `_site` at that same project prefix with a static server. The deck URLs are `foundations/#/1` and `operator-cases/#/1` within the project. Hash routing keeps shared slide addresses working after reload on GitHub Pages.

The build keeps original presentation sources, PDFs and evidence snapshots unchanged. It rebases ordinary source-guide links only in the generated Slidev application. Missing supplemental links in archived notebook views are supplied from the canonical workshop files, or through new redirects to their GitHub notebook views.

## Publish

`.github/workflows/deploy-pages.yml` builds and deploys the site when the presentation or site sources change on `main`. It can also be started manually from GitHub Actions. Repository Settings → Pages uses **GitHub Actions** as its publishing source. No deployment credential is stored in the repository.

The official actions are pinned to reviewed release commits. Build permissions are read-only; the deployment job receives Pages and OpenID Connect permissions. Existing LaTeX PDFs are copied as downloads, so the site workflow does not need to regenerate them.

## Maintain

- Edit the landing page in `web/index.html` and its styles in `web/assets/site.css`.
- Edit the decks in their original Slidev project folders.
- Update the corresponding PDFs when their teaching content changes.
- Retain image credits, source registries and third-party notices.
- Generated `_site` output and installed dependencies stay out of Git.

The learner site links to presentations, one main Colab lab, participant downloads and references. Speaking scripts remain outside the generated audience site. The participant archive is built by `scripts/build-participant-pack.py`.
