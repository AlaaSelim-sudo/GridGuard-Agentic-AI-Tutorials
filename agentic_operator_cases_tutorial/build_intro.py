"""Static introductory lecture and separate full reading guide renderer."""
from pathlib import Path
import importlib.util
import json
import html
import shutil
import hashlib
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
REVIEWED = "17 October 2026"


def esc(value):
    value = str(value or "")
    value = (value.replace("²", "2").replace("→", " to ").replace("·", " / ")
             .replace("’", "'").replace("“", '"').replace("”", '"')
             .replace("–", "--").replace("—", "---").replace("\u00a0", " "))
    mapping = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$",
               "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}",
               "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}
    return "".join(mapping.get(c, c) for c in value)


def he(value):
    return html.escape(str(value or ""), quote=True)


def load_json(path, default=None):
    if not path.exists() and default is not None:
        return default
    return json.loads(path.read_text(encoding="utf-8-sig"))


def unique(values):
    return list(dict.fromkeys(values))


def local_research(url):
    for prefix in ("../research/", "/research/", "research/"):
        if str(url).startswith(prefix):
            name = str(url)[len(prefix):]
            if Path(name).is_absolute() or ".." in Path(name).parts:
                raise ValueError("Unsafe local research path: " + str(url))
            return name
    return None


def href(url, target):
    name = local_research(url)
    if name is None:
        return str(url)
    return {"slidev": "/research/", "latex": "../research/", "guide": "research/"}[target] + name


def texlink(url, label):
    target = href(url, "latex").replace("%", r"\%").replace("#", r"\#")
    return r"\href{" + target + "}{" + esc(label) + "}"


def full_url_tex(url):
    target = href(url, "latex").replace("%", r"\%").replace("#", r"\#")
    label = "".join(esc(c) + (r"\allowbreak{}" if c in "/-_.?=&%" else "") for c in str(url))
    return r"\href{" + target + r"}{\small\ttfamily " + label + "}"


def points_tex(points, compact=False):
    if not points:
        return ""
    return ("{" + (r"\small" if compact else "") + r"\begin{itemize}" + "\n"
            + (r"\setlength{\itemsep}{.2em}" + "\n" if compact else "")
            + "".join(r"\item " + esc(p) + "\n" for p in points)
            + r"\end{itemize}}" + "\n")


def table_tex(table, compact=False):
    if not table:
        return ""
    n = len(table[0])
    if any(len(row) != n for row in table):
        raise ValueError("Ragged table")
    widths = (.24, .35, .34) if n == 3 else (.29, .64) if n == 2 else (.93 / n,) * n
    cols = "".join(r">{\raggedright\arraybackslash}p{" + str(w) + r"\linewidth}" for w in widths)
    out = ["{" + (r"\scriptsize" if compact else r"\small")
           + r"\setlength{\tabcolsep}{4pt}\renewcommand{\arraystretch}{1.13}"
           + r"\begin{tabular}{@{}" + cols + r"@{}}\toprule" + "\n"]
    for i, row in enumerate(table):
        cells = [esc(x) for x in row]
        if i == 0:
            cells = [r"\textbf{" + x + "}" for x in cells]
        out.append(" & ".join(cells) + r" \\" + "\n")
        if i == 0:
            out.append(r"\midrule" + "\n")
    return "".join(out) + r"\bottomrule\end{tabular}}" + "\n"


def picture_tex(name, caption, height):
    return (r"\begin{center}\includegraphics[width=\linewidth,height=" + height
            + r",keepaspectratio]{images/" + name + "}\n"
            + r"\par{\fontsize{6.8}{8}\selectfont\color{Slate} " + esc(caption)
            + r"}\end{center}" + "\n")


def frame_tex(s, sources):
    kind = s.get("kind", "normal")
    # Stop Beamer from treating a leading font group as a frame subtitle.
    out = [r"\begin{frame}[t]{" + ("" if kind == "cover" else esc(s["title"])) + "}\n\\relax\n"]
    if kind == "cover":
        out.append(r"\vspace{.65cm}{\fontsize{30}{34}\selectfont\color{IEEEBlue}"
                   r"\bfseries Agentic AI for\\Utility Operators}\par\vspace{.42cm}" + "\n")
        out.extend(r"{\large " + esc(p) + r"}\par\medskip" + "\n" for p in s["points"])
        out.append(r"\vfill\includegraphics[width=4cm]{images/comsoc-lockup.png}\par"
                   r"{\tiny Independent educational material / IEEE ComSoc theme adaptation}" + "\n")
    elif kind == "figure":
        figure_height = "4.35cm" if s["title"] == "Workflow or agent?" else "3.4cm"
        out.append(picture_tex(s["image"], s.get("caption", ""), figure_height))
        out.append(points_tex(s["points"], True))
        out.append(table_tex(s.get("table"), True))
    elif kind == "pair":
        out.append(r"\begin{columns}[T,onlytextwidth]" + "\n")
        for image, caption in (("image", "caption"), ("image2", "caption2")):
            out.append(r"\begin{column}{.485\textwidth}" + "\n"
                       + picture_tex(s[image], s.get(caption, ""), "1.9cm")
                       + r"\end{column}" + "\n")
        out.append(r"\end{columns}" + "\n" + points_tex(s["points"], True) + table_tex(s.get("table"), True))
    elif s.get("image"):
        out.append(r"\begin{columns}[T,onlytextwidth]\begin{column}{.515\textwidth}" + "\n"
                   + points_tex(s["points"]) + table_tex(s.get("table"), True)
                   + r"\end{column}\begin{column}{.445\textwidth}" + "\n"
                   + picture_tex(s["image"], s.get("caption", ""), "4.05cm")
                   + r"\end{column}\end{columns}" + "\n")
    else:
        out.append(points_tex(s["points"]) + table_tex(s.get("table")))
    if kind == "closing":
        out.append(r"\medskip{\large\href{../Full_Reading_Guide.html}{Open the Full Reading Guide}}\par"
                   r"{\small\href{reading_guide.pdf}{Separate reading-guide PDF}}" + "\n")
    out.append(r"\vfill" + "\n")
    if s.get("takeaway") and kind not in ("cover", "figure"):
        out.append(r"{\small\color{IEEEBlue}\textbf{" + esc(s["takeaway"]) + r"}\par}\smallskip" + "\n")
    if s["refs"]:
        refs = [texlink(sources[k]["url"], "[" + k + "] " + sources[k].get("short", sources[k]["title"])) for k in s["refs"]]
        out.append(r"{\fontsize{6.3}{7.5}\selectfont\color{Slate} Sources: " + " / ".join(refs) + r"\par}" + "\n")
    out.append(r"\note{" + esc(s.get("note", "")) + " Takeaway: " + esc(s.get("takeaway", "")) + "}\n"
               + r"\end{frame}" + "\n\n")
    return "".join(out)


def points_html(points):
    return "<ul>" + "".join("<li>" + he(p) + "</li>" for p in points) + "</ul>" if points else ""


def table_html(table):
    if not table:
        return ""
    return ("<table><thead><tr>" + "".join("<th>" + he(x) + "</th>" for x in table[0])
            + "</tr></thead><tbody>" + "".join("<tr>" + "".join("<td>" + he(x) + "</td>" for x in row)
            + "</tr>" for row in table[1:]) + "</tbody></table>")


def picture_html(name, caption):
    return '<figure><img src="/images/' + he(name) + '" alt="' + he(caption) + '"><figcaption>' + he(caption) + "</figcaption></figure>"


def slide_html(s, number, total, sources):
    kind = s.get("kind", "normal")
    cls = {"cover": "cover", "figure": "figure-slide", "pair": "pair-slide", "closing": "closing"}.get(kind, "")
    if len(s.get("table") or []) >= 6:
        cls += " dense"
    out = ['<div class="lesson ' + cls + '">\n']
    if kind == "cover":
        out.append("<h1>Agentic AI for<br>Utility Operators</h1>" + "".join("<p>" + he(p) + "</p>" for p in s["points"]))
        out.append('<img class="cover-logo" src="/branding/comsoc-lockup.png" alt="IEEE Communications Society lockup">'
                   "<small>Independent educational material · IEEE ComSoc theme adaptation</small>")
    else:
        out.append("<h1>" + he(s["title"]) + "</h1>\n")
        body = points_html(s["points"]) + table_html(s.get("table"))
        if kind == "figure":
            out.append('<div class="content"><div class="wide-figure">'
                       + picture_html(s["image"], s.get("caption", "")) + "</div>" + body + "</div>")
        elif kind == "pair":
            out.append('<div class="content"><div class="photo-pair">' + picture_html(s["image"], s.get("caption", ""))
                       + picture_html(s["image2"], s.get("caption2", "")) + "</div>" + body + "</div>")
        elif s.get("image"):
            out.append('<div class="content with-photo"><div>' + body + "</div>"
                       + picture_html(s["image"], s.get("caption", "")) + "</div>")
        else:
            out.append('<div class="content">' + body + "</div>")
        if kind == "closing":
            out.append('<p class="reading-link"><a href="/Full_Reading_Guide.html">Open the Full Reading Guide</a></p>')
    if s["refs"]:
        out.append('<div class="sources">Sources: ' + " · ".join('<a href="' + he(href(sources[k]["url"], "slidev"))
                   + '">[' + k + "] " + he(sources[k].get("short", sources[k]["title"])) + "</a>" for k in s["refs"]) + "</div>")
    if s.get("takeaway") and kind not in ("cover", "figure"):
        out.append('<div class="takeaway">' + he(s["takeaway"]) + "</div>")
    out.append('<span class="pageno">' + str(number) + " / " + str(total) + "</span></div>\n\n<!--\n"
               + s.get("note", "").replace("-->", "--&gt;") + "\nTakeaway: " + s.get("takeaway", "")
               + "\nNominal duration: " + str(s["minutes"]) + " minutes.\n-->\n")
    return "\n".join(out)


def source_fields(record):
    publisher = record.get("publisher") or record.get("organization")
    if not publisher:
        publisher = "GridGuard project / local snapshot" if local_research(record["url"]) else urlparse(record["url"]).netloc
    authors = record.get("authors") or record.get("author") or record.get("organization") or publisher
    if isinstance(authors, list):
        authors = ", ".join(authors)
    fields = [("Authors / issuer", str(authors)), ("Publisher / venue", publisher),
              ("Date", record.get("date") or "Undated; reviewed " + REVIEWED)]
    for key in ("type", "evidence_type", "location", "version_note", "license"):
        if record.get(key):
            fields.append((key.replace("_", " ").capitalize(), str(record[key])))
    return fields


def reading_sections(ids, sources, slides, image_manifest):
    sections = []
    for key in ids:
        r = sources[key]
        links = [("Full source URL", r["url"])]
        for field, label in (("pdf_url", "Full paper PDF"), ("code_url", "Source code"), ("publication_url", "Publication")):
            if r.get(field) and r[field] != r["url"]:
                links.append((label, r[field]))
        fields = source_fields(r)
        if key == "B01":
            fields.append(("Theme assets", "comsoc-lockup.png and image7.png; independent educational adaptation"))
        sections.append(("[" + key + "] " + r["title"], fields, links))
    records = {r["file"]: r for r in image_manifest.get("images", [])}
    images = unique(name for s in slides for name in (s.get("image"), s.get("image2")) if name)
    for name in images:
        r = dict(records.get(name, {}))
        uses = [(i, s) for i, s in enumerate(slides, 1) if name in (s.get("image"), s.get("image2"))]
        caption = uses[0][1].get("caption" if uses[0][1].get("image") == name else "caption2", "")
        fields = [("Caption", caption), ("Credit", r.get("credit", "Existing GridGuard workshop source")),
                  ("Used on", "; ".join(str(i) + ". " + s["title"] for i, s in uses))]
        for field in ("asset_type", "transformation", "provenance_note", "evidence_limit", "license_or_permission_status", "license_notice"):
            if r.get(field):
                fields.append((field.replace("_", " ").capitalize(), str(r[field])))
        links = [(label, r[field]) for field, label in
                 (("source_page_url", "Original source / page"), ("publication_url", "Full publication"),
                  ("direct_image_url", "Original figure / image URL")) if r.get(field)]
        if not links:
            links = [("Local workshop source", "research/Follow_on_workshop_source.txt")]
        sections.append(("Visual credit: " + name, fields, links))
    return sections


def reading_guides(sections):
    def guide_esc(value):
        # Keep scientific symbols legible with the reading guide's text font.
        value=str(value).replace('§','section ').replace('±',' plus or minus ')
        value=value.replace('×',' times ').replace('≤',' <= ').replace('≥',' >= ')
        value=value.replace('•',' / ')
        return esc(value)
    intro = ("Agentic AI for Utility Operators — introductory lecture. Evidence reviewed " + REVIEWED
             + ". The full reading guide is separate from the timed main talk. Corporate issuers are listed when no individual author is recorded. "
             + "Original figures, page locations and image-source credits are included. Attribution alone is not a blanket reuse license.")
    md = ["# Full Reading Guide\n\n" + intro + "\n"]
    web = ['<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
           '<title>Full Reading Guide — Agentic AI for Utility Operators</title><style>'
           'body{font:17px/1.55 Arial,sans-serif;color:#173f55;max-width:1050px;margin:40px auto;padding:0 24px}'
           'h1,h2{color:#00629b}h1{border-bottom:3px solid #00a6b2;padding-bottom:12px}h2{font-size:21px}'
           'a{color:#00629b;overflow-wrap:anywhere;word-break:break-word}article{border-bottom:1px solid #dce5eb;padding-bottom:20px;margin:26px 0}'
           'dt{font-weight:bold;margin-top:10px}dd{margin-left:0;white-space:pre-wrap}'
           '@media print{body{font-size:10pt;margin:0}article{break-inside:avoid}}'
           '</style></head><body><h1>Full Reading Guide</h1><p>' + he(intro) + "</p>"]
    tex = [r"""\documentclass[10pt,letterpaper]{article}
\usepackage[margin=.75in]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{xcolor}
\usepackage[hyphens]{url}
\usepackage[colorlinks=true,urlcolor=blue,linkcolor=blue]{hyperref}
\urlstyle{same}
\Urlmuskip=0mu plus 1mu
\setlength{\parindent}{0pt}
\setlength{\parskip}{.45em}
\emergencystretch=3em
\sloppy
\newbox\readingEntry
\hypersetup{pdftitle={Full Reading Guide: Agentic AI for Utility Operators}}
\begin{document}
{\LARGE\bfseries Full Reading Guide}\par
""", guide_esc(intro) + r"\par" + "\n"]
    for title, fields, links in sections:
        md.append("\n## " + title + "\n")
        web.append("<article><h2>" + he(title) + "</h2><dl>")
        tex.append(r"\setbox\readingEntry=\vbox\bgroup\hsize=\linewidth\subsection*{" + guide_esc(title) + "}\n")
        for label, value in fields:
            if not value:
                continue
            md.append("\n**" + label + ":** " + value + "\n")
            web.append("<dt>" + he(label) + "</dt><dd>" + he(value) + "</dd>")
            tex.append(r"\textbf{" + guide_esc(label) + ":} " + guide_esc(value) + r"\par" + "\n")
        for label, url in links:
            if local_research(url) is not None:
                url = href(url, "guide")
            md.append("\n**" + label + ":** [" + url + "](" + href(url, "guide") + ")\n")
            web.append("<dt>" + he(label) + '</dt><dd><a href="' + he(href(url, "guide")) + '">' + he(url) + "</a></dd>")
            tex.append(r"\textbf{" + guide_esc(label) + r":} " + full_url_tex(url) + r"\par" + "\n")
        web.append("</dl></article>")
        tex.append(r"\egroup\par\noindent\box\readingEntry\par\medskip"+'\n')
    web.append("</body></html>\n")
    tex.append(r"\end{document}" + "\n")
    return "".join(md), "".join(web), "".join(tex)


def stamp(minutes):
    secs = round(minutes * 60)
    return f"{secs//60:02d}:{secs%60:02d}"


def notes(slides):
    minutes = sum(s["minutes"] for s in slides)
    out = [f"# Instructor guide — introduction\n\n{len(slides)} static slides; nominal duration {minutes:g} minutes. "
           + "Evidence reviewed " + REVIEWED + ".\n\nThe three worked use cases belong to the separate practical workshop. "
           + "All content is visible at once; transitions and click reveals are disabled. The Full Reading Guide is untimed.\n\n"
           + "| Slide | Topic | Minutes | Cumulative time |\n|---|---|---:|---|\n"]
    elapsed = 0
    for i, s in enumerate(slides, 1):
        end = elapsed + s["minutes"]
        out.append(f"| {i} | {s['title']} | {s['minutes']:g} | {stamp(elapsed)}–{stamp(end)} |\n")
        elapsed = end
    elapsed = 0
    for i, s in enumerate(slides, 1):
        end = elapsed + s["minutes"]
        out.append(f"\n## {i}. {s['title']}\n\n**Timing:** {stamp(elapsed)}–{stamp(end)} ({s['minutes']:g} minutes).\n\n"
                   + s.get("note", "") + "\n\n**Takeaway:** " + s.get("takeaway", "") + "\n"
                   + ("\n**Readings:** " + ", ".join(s["refs"]) + ".\n" if s["refs"] else ""))
        elapsed = end
    return "".join(out)


def main():
    spec = importlib.util.spec_from_file_location("intro_content", ROOT / "intro_content.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    slides = module.SLIDES
    sources = load_json(ROOT / "research/source_map.json")
    images = unique(name for s in slides for name in (s.get("image"), s.get("image2")) if name)
    used = unique(k for s in slides for k in s["refs"])
    reading_ids = unique(used + ["H02", "H08", "H12"])
    for k in reading_ids:
        if k not in sources:
            raise ValueError("Unresolved source ID: " + k)
    for name in images:
        if Path(name).name != name or not (ROOT / "images" / name).is_file():
            raise ValueError("Missing or unsafe image: " + name)
    for folder in ("latex/images", "slidev/public/images", "slidev/public/branding", "slidev/public/research"):
        (ROOT / folder).mkdir(parents=True, exist_ok=True)
    for name in images:
        for folder in ("latex/images", "slidev/public/images"):
            shutil.copy2(ROOT / "images" / name, ROOT / folder / name)
    for name in ("comsoc-lockup.png", "image7.png"):
        shutil.copy2(ROOT / "branding" / name, ROOT / "latex/images" / name)
        shutil.copy2(ROOT / "branding" / name, ROOT / "slidev/public/branding" / name)
    for k in reading_ids:
        name = local_research(sources[k]["url"])
        if name:
            target = ROOT / "slidev/public/research" / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / "research" / name, target)
    frames = "".join(frame_tex(s, sources) for s in slides)
    front = """---
theme: default
title: Agentic AI for Utility Operators — Introduction
info: Motivation, frameworks and evidence; full readings are separate
author: GridGuard tutorial
transition: none
aspectRatio: 16/9
canvasWidth: 1280
colorSchema: light
fonts:
  sans: Arial
  provider: none
mdc: false
drawings:
  persist: false
download: false
---

"""
    deck = front + "\n---\ntransition: none\n---\n\n".join(slide_html(s, i, len(slides), sources) for i, s in enumerate(slides, 1))
    for token in ("v-click", "v-motion", r"\transfade", r"\uncover<", r"\item<", r"\pause"):
        if token in frames or token in deck:
            raise ValueError("Non-static output: " + token)
    sections = reading_sections(reading_ids, sources, slides, load_json(ROOT / "images/image_manifest.json", {"images": []}))
    markdown, guide_html, guide_tex = reading_guides(sections)
    outputs = {
        "latex/frames.tex": frames, "slidev/slides.md": deck, "Instructor_Guide.md": notes(slides),
        "lesson_content.json": json.dumps(slides, ensure_ascii=False, indent=2) + "\n",
        "latex/reading_guide.tex": guide_tex, "References.md": markdown,
        "Full_Reading_Guide.html": guide_html, "slidev/public/Full_Reading_Guide.html": guide_html,
    }
    for name, content in outputs.items():
        (ROOT / name).write_text(content, encoding="utf-8")
    manifest = {"main_slides": len(slides), "minutes": sum(s["minutes"] for s in slides),
                "reading_sources": len(reading_ids), "reading_source_ids": reading_ids, "used_images": images,
                "transitions": "none", "click_reveals": 0, "reading_guide_timed": False,
                "source_content": "intro_content.py", "source_registry": "research/source_map.json",
                "source_content_sha256": hashlib.sha256((ROOT / "intro_content.py").read_bytes()).hexdigest(),
                "outputs": list(outputs)}
    (ROOT / "build_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: manifest[k] for k in ("main_slides", "minutes", "reading_sources", "transitions", "click_reveals")}))


if __name__ == "__main__":
    main()

