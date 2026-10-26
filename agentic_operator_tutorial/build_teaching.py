"""Render the integrated power-system teaching deck, with static diagrams and no tables.

Content is supplied by power_content.py. The source registry and reading-guide
format remain shared with the introductory edition; this file does not edit them.
"""
from pathlib import Path
import importlib.util
import json
import hashlib
import re
import shutil
import latin_modern

ROOT = Path(__file__).resolve().parent
KINDS = {"cover", "normal", "photo", "figure", "diagram", "exercise", "closing", "video"}


def module_from_file(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot load " + str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


reading = module_from_file("teaching_reading_helpers", ROOT / "build_intro.py")
he = reading.he


def esc(value):
    value = str(value or "").replace("τ", "tau").replace("≤", "<=")
    value = value.replace("≥", ">=").replace("\u2011", "-").replace("\u202f", " ")
    value = value.replace('•',' / ')
    return (reading.esc(value).replace("≠", r"\ensuremath{\ne}")
            .replace("−", "-").replace("×", r"\ensuremath{\times}"))


def points_tex(points, compact=False):
    if not points:
        return ""
    size = r"\small" if compact else r"\normalsize"
    return ("{\n" + size + r"\begin{itemize}" + "\n"
            + (r"\setlength{\itemsep}{.25em}" + "\n" if compact else "")
            + "".join(r"\item " + esc(point) + "\n" for point in points)
            + r"\end{itemize}\par}" + "\n")


def picture_tex(name, caption, height):
    vector = Path(name).with_suffix(".pdf").name
    print_name = vector if Path(name).suffix.lower() in {'.png','.svg'} and (ROOT / "images" / vector).is_file() else name
    return (r"\begingroup\centering\includegraphics[width=\linewidth,height=" + height
            + r",keepaspectratio]{images/" + print_name + "}\n"
            + (r"\par{\fontsize{7}{8.3}\selectfont\color{Slate} " + esc(caption) + "}\n" if caption else "")
            + r"\par\endgroup\smallskip" + "\n")


def diagram_tex(diagram, caption, width=".96", height="4.2cm"):
    return (r"\begingroup\begin{minipage}[c][" + height + r"][c]{\linewidth}\centering\setbox0=\hbox{\resizebox{" + width
            + r"\linewidth}{!}{\input{diagrams/" + diagram + r".tex}}}"
            + r"\ifdim\dimexpr\ht0+\dp0\relax>"+height+r"\resizebox{!}{"+height+r"}{\box0}\else\box0\fi\par\end{minipage}" + "\n"
            + (r"{\fontsize{7}{8.3}\selectfont\color{Slate} " + esc(caption) + r"\par}" + "\n" if caption else "")
            + r"\endgroup\smallskip" + "\n")


def visual_height(s, web=False):
    """A numeric cm/px content field; aliases retain the author's short names."""
    if web:
        value = s.get("visual_height_px", s.get("web_visual_height", 330 if s.get("diagram") else 360))
        return f"{float(value):g}px"
    value = s.get("visual_height_cm", s.get("visual_height", 3.8 if s["kind"] == "exercise" else 4.0 if s.get("diagram") else 3.9))
    return f"{float(value):g}cm"


def extra_tex(s):
    """Trusted math, literal excerpt and a flat statistic; never a UI card."""
    out = []
    if s.get("callout"):
        out.append(r"{\fontsize{25}{29}\selectfont\color{IEEEBlue}\bfseries "
                   + esc(s["callout"]) + r"\par}\medskip" + "\n")
    if s.get("math_tex"):
        body = s["math_tex"].strip()
        display = body if body.startswith((r"\[", r"\begin{")) else r"\[\displaystyle " + body + r"\]"
        out.append(r"{\fontsize{19}{23}\selectfont " + display + "}\n")
    if s.get("excerpt"):
        out.append(r"\begingroup\fontsize{10}{13}\selectfont\ttfamily\raggedright" + "\n")
        for line in s["excerpt"]:
            out.append(r"\noindent\strut\mbox{" + esc(line).replace(" ", "~") + r"}\par" + "\n")
        out.append(r"\endgroup\medskip" + "\n")
    return "".join(out)


def full_citation(record):
    """A full bibliographic entry, with all recorded authors and the complete title."""
    publisher=record.get('publisher') or record.get('organization') or ''
    authors=record.get('authors') or record.get('author') or record.get('organization') or publisher
    if isinstance(authors,list):authors=', '.join(authors)
    date=record.get('citation_date') or record.get('date','Undated')
    if len(date)>65:
        year=re.search(r'\b20\d{2}\b',date)
        date=year.group() if year else date
    parts=[str(authors),record['title']]
    if publisher and publisher!=authors:parts.append(publisher)
    parts.append(date)
    return ('. '.join(parts)+'.').replace('•',' / ')


def complete_sources(refs,sources):
    return '\n\n'.join(full_citation(sources[key])+'\nFull source: '+sources[key]['url']
        + ('\nFull paper: '+sources[key]['pdf_url'] if sources[key].get('pdf_url') and sources[key]['pdf_url']!=sources[key]['url'] else '')
        + ('\nPublication: '+sources[key]['publication_url'] if sources[key].get('publication_url') and sources[key]['publication_url']!=sources[key]['url'] else '')
        for key in refs)


def sources_tex(refs, sources, main_ref=None):
    if not refs:
        return ""
    record=sources[main_ref or refs[0]]
    return (r"{\fontsize{6.3}{7.5}\selectfont\color{Slate} Source: "
            + reading.texlink(record['url'],full_citation(record))
            + r"\par}" + "\n")


def render_frame(s, sources):
    kind = s["kind"]
    # Beamer would consume a leading braced body as the optional frame subtitle.
    out = [r"\begin{frame}[t]{" + ("" if kind == "cover" else esc(s["title"])) + "}\n\\relax\n"]
    if kind == "cover":
        out.append(r"\vspace{.55cm}{\fontsize{30}{34}\selectfont\color{IEEEBlue}"
                   r"\bfseries Agentic AI for\\Utility Operators}\par\vspace{.38cm}" + "\n")
        out.extend(r"{\large " + esc(p) + r"}\par\medskip" + "\n" for p in s["points"])
        if s.get('presenters'):
            out.append(r'\medskip\begin{columns}[T,onlytextwidth]'+'\n')
            for person in s['presenters']:
                out.append(r'\begin{column}{.48\textwidth}{\large\bfseries '+esc(person['name'])+r'\par}{\normalsize '+esc(person['affiliation'])+r'\par}\end{column}'+'\n')
            out.append(r'\end{columns}\medskip'+'\n')
        out.append(r"\vfill\includegraphics[width=4cm]{images/comsoc-lockup.png}\par"
                   r"{\tiny Independent educational material / IEEE ComSoc theme adaptation}" + "\n")
    else:
        if s.get("eyebrow"):
            out.append(r"{\scriptsize\color{Slate}\textbf{" + esc(s["eyebrow"]) + r"}\par}\smallskip" + "\n")
        if kind == 'video':
            trim=',trim=0 45 0 45,clip' if s['video_id']=='pLPJoFvq4_M' else ''
            out.append(r'\begin{columns}[T,onlytextwidth]\begin{column}{.64\textwidth}\centering'+'\n')
            out.append(r'\href{'+s['video_url']+r'}{\includegraphics[width=\linewidth,height=4cm,keepaspectratio'+trim+r']{images/'+s['image']+r'}}\par'+'\n')
            out.append(r'\smallskip{\small\href{'+s['video_url']+r'}{Watch official video}\par}'+ '\n')
            out.append(r'\end{column}\begin{column}{.32\textwidth}'+points_tex(s['points'],compact=True)+r'\end{column}\end{columns}'+'\n')
        elif s.get('layout')=='news-detail':
            out.append(r'\begin{columns}[T,onlytextwidth]\begin{column}{.56\textwidth}'+'\n'
                       +picture_tex(s['image'],s.get('caption',''),'3.6cm')
                       +r'\end{column}\begin{column}{.40\textwidth}'+'\n'
                       +points_tex(s['points'],compact=True)+r'\end{column}\end{columns}'+'\n'
                       +picture_tex(s['image2'],s.get('caption2',''),'.45cm'))
        elif s.get('layout')=='source-focus':
            out.append(r'\begin{columns}[T,onlytextwidth]\begin{column}{.64\textwidth}'+'\n'
                       +picture_tex(s['image'],s.get('caption',''),str(s.get('focus_height_cm',4.65))+'cm')
                       +r'\end{column}\begin{column}{.32\textwidth}'+'\n'
                       +points_tex(s['points'],compact=True)+r'\end{column}\end{columns}'+'\n')
        elif s.get("diagram"):
            out.append(diagram_tex(s["diagram"], s.get("caption", ""), ".86" if kind == "exercise" else ".96", visual_height(s)))
            out.append(extra_tex(s))
            out.append(points_tex(s["points"], compact=True))
        elif kind == "figure":
            out.append(picture_tex(s["image"], s.get("caption", ""), visual_height(s)))
            out.append(extra_tex(s))
            out.append(points_tex(s["points"], compact=True))
        elif s.get("image2"):
            out.append(r"\begin{columns}[T,onlytextwidth]" + "\n")
            for image, caption in (("image", "caption"), ("image2", "caption2")):
                out.append(r"\begin{column}{.485\textwidth}" + "\n"
                           + picture_tex(s[image], s.get(caption, ""), "2.55cm")
                           + r"\end{column}" + "\n")
            out.append(r"\end{columns}\smallskip" + "\n" + extra_tex(s) + points_tex(s["points"], compact=True))
        elif s.get("image"):
            out.append(extra_tex(s))
            out.append(r"\begin{columns}[T,onlytextwidth]\begin{column}{.515\textwidth}" + "\n"
                       + points_tex(s["points"])
                       + r"\end{column}\begin{column}{.445\textwidth}" + "\n"
                       + picture_tex(s["image"], s.get("caption", ""), str(s.get('photo_height_cm',3.85))+"cm")
                       + r"\end{column}\end{columns}" + "\n")
        else:
            out.append(extra_tex(s) + points_tex(s["points"]))
        if kind == "closing":
            out.append(r"\medskip{\large\href{../Full_Reading_Guide.html}{Open the Full Reading Guide}}\par"
                       r"{\small\href{reading_guide.pdf}{Separate reading-guide PDF}}" + "\n")
    out.append(r"\vfill" + "\n")
    if s.get("takeaway") and kind not in {"cover", "figure", "diagram"} and not s.get("diagram") and s.get('layout') not in {'source-focus','news-detail'}:
        out.append(r"{\small\color{IEEEBlue}\textbf{" + esc(s["takeaway"]) + r"}\par}\smallskip" + "\n")
    out.append(sources_tex(s["refs"], sources,s.get('main_ref')))
    out.append(r"\note{" + esc(s.get("note", "")) + " Takeaway: " + esc(s.get("takeaway", ""))
               + '\n\n'+esc(complete_sources(s['refs'],sources))+ "}\n")
    out.append(r"\end{frame}" + "\n\n")
    return "".join(out)


def points_html(points):
    return "<ul>" + "".join("<li>" + he(point) + "</li>" for point in points) + "</ul>" if points else ""


def picture_html(name, caption, height=None):
    sizing = ' style="max-height:' + height + ';height:auto"' if height else ""
    return ('<figure><img src="/images/' + he(name) + '" alt="' + he(caption) + '"' + sizing
            + '><figcaption>' + he(caption) + "</figcaption></figure>")


def extra_html(s):
    out = []
    if s.get("callout"):
        out.append('<p class="callout">' + he(s["callout"]) + "</p>")
    if s.get("math_html"):
        # math_html is trusted tutorial source, not user-supplied runtime input.
        out.append('<div class="math-display" role="math">' + s["math_html"] + "</div>")
    if s.get("excerpt"):
        out.append('<pre class="source-excerpt">' + he("\n".join(s["excerpt"])) + "</pre>")
    return "".join(out)


def render_slide(s, number, total, sources):
    kind = s["kind"]
    classes = ["lesson", "teaching", "rigorous", kind + "-slide"]
    if kind == "cover":
        classes.append("cover")
    if kind == "closing":
        classes.append("closing")
    if s.get("diagram"):
        classes.append("has-diagram")
    if s.get("image2"):
        classes.append("has-pair")
    out = ['<div class="' + " ".join(classes) + '">\n']
    if kind == "cover":
        out.append("<h1>Agentic AI for<br>Utility Operators</h1>")
        out.extend("<p>" + he(point) + "</p>" for point in s["points"])
        if s.get('presenters'):
            out.append('<div class="presenters">'+''.join('<div><strong>'+he(p['name'])+'</strong><span>'+he(p['affiliation'])+'</span></div>' for p in s['presenters'])+'</div>')
        out.append('<img class="cover-logo" src="/branding/comsoc-lockup.png" alt="IEEE Communications Society lockup">'
                   "<small>Independent educational material · IEEE ComSoc theme adaptation</small>")
    else:
        if s.get("eyebrow"):
            out.append('<div class="eyebrow">' + he(s["eyebrow"]) + "</div>")
        out.append("<h1>" + he(s["title"]) + "</h1>")
        if kind == 'video':
            out.append('<div class="content"><PlatformVideo embed-url="'+he(s['embed_url'])+'" watch-url="'+he(s['video_url'])+'" poster="'+he(s['image'])+'" title="'+he(s['title'])+'" /><div class="video-points">'+points_html(s['points'])+'</div></div>')
        elif s.get('layout')=='news-detail':
            out.append('<div class="content"><div class="source-focus news-detail">'+picture_html(s['image'],s.get('caption',''),'330px')
                       +'<div>'+points_html(s['points'])+'</div></div><div class="news-strip">'
                       +picture_html(s['image2'],s.get('caption2',''),'44px')+'</div></div>')
        elif s.get('layout')=='source-focus':
            out.append('<div class="content source-focus">'+picture_html(s['image'],s.get('caption',''),str(s.get('focus_height_px',430))+'px')
                       +'<div>'+points_html(s['points'])+'</div></div>')
        elif s.get("diagram"):
            out.append('<div class="content"><figure class="native-diagram"><img src="/diagrams/'
                       + he(s["diagram"]) + '.svg" alt="' + he(s.get("caption") or s["title"])
                       + '" style="height:' + visual_height(s, web=True) + ';max-height:'
                       + visual_height(s, web=True) + (';width:86%;margin:0 auto' if kind == "exercise" else "")
                       + '"><figcaption>' + he(s.get("caption", "")) + "</figcaption></figure>"
                       + extra_html(s) + points_html(s["points"]) + "</div>")
        elif kind == "figure":
            out.append('<div class="content"><div class="wide-figure">'
                       + picture_html(s["image"], s.get("caption", ""), visual_height(s, web=True)) + "</div>"
                       + extra_html(s) + points_html(s["points"]) + "</div>")
        elif s.get("image2"):
            out.append('<div class="content"><div class="photo-pair">'
                       + picture_html(s["image"], s.get("caption", ""))
                       + picture_html(s["image2"], s.get("caption2", "")) + "</div>"
                       + extra_html(s) + points_html(s["points"]) + "</div>")
        elif s.get("image"):
            out.append('<div class="content">'+extra_html(s)+'<div class="with-photo"><div>' + points_html(s["points"]) + "</div>"
                       + picture_html(s["image"], s.get("caption", ""),str(s.get('photo_height_px',360))+'px') + "</div></div>")
        else:
            out.append('<div class="content">' + extra_html(s) + points_html(s["points"]) + "</div>")
        if kind == "closing":
            out.append('<p class="reading-link"><a href="/Full_Reading_Guide.html">Open the Full Reading Guide</a></p>')
    if s["refs"]:
        record=sources[s.get('main_ref') or s['refs'][0]]
        out.append('<div class="sources">Source: <a href="'+he(reading.href(record['url'],'slidev'))+'">'
                   +he(full_citation(record))+'</a></div>')
    if s.get("takeaway") and kind not in {"cover", "figure", "diagram"} and not s.get("diagram") and s.get('layout') not in {'source-focus','news-detail'}:
        out.append('<div class="takeaway">' + he(s["takeaway"]) + "</div>")
    out.append('<span class="pageno">' + str(number) + " / " + str(total) + "</span></div>")
    out.append("\n<!--\n" + s.get("note", "").replace("-->", "--&gt;")
               + "\nTakeaway: " + s.get("takeaway", "")
               + "\nNominal duration: " + str(s["minutes"]) + " minutes.\n\nFull sources:\n"
               +complete_sources(s['refs'],sources)+"\n-->\n")
    return "\n".join(out)


def normalized_slides(content):
    slides = []
    for i, raw in enumerate(content.SLIDES, 1):
        if "table" in raw:
            raise ValueError(f"Slide {i} contains a prohibited table field")
        if "answer" in raw:
            raise ValueError(f"Slide {i}: exercise answers belong only in note")
        s = dict(raw)
        for field, default in (("points", []), ("refs", []), ("image", None), ("image2", None),
                               ("caption", ""), ("caption2", ""), ("diagram", None),
                               ("eyebrow", ""), ("note", ""), ("takeaway", ""), ("kind", "normal"),
                               ("math_tex", ""), ("math_html", ""), ("excerpt", []), ("callout", "")):
            s.setdefault(field, default)
        if not s.get("title") or s["kind"] not in KINDS:
            raise ValueError(f"Slide {i} has an invalid title or kind")
        if not isinstance(s["points"], list) or not isinstance(s["refs"], list):
            raise ValueError(f"Slide {i}: points and refs must be lists")
        if not isinstance(s.get("minutes"), (int, float)) or s["minutes"] <= 0:
            raise ValueError(f"Slide {i}: minutes must be positive")
        if s["kind"] == "diagram" and not s.get("diagram"):
            raise ValueError(f"Slide {i}: diagram kind needs a diagram ID")
        if s["kind"] == "figure" and not s.get("image"):
            raise ValueError(f"Slide {i}: figure kind needs an image")
        if s["kind"] == "exercise" and len(s["points"]) > 3:
            raise ValueError(f"Slide {i}: exercise slides allow at most 3 short points")
        if (s.get("diagram") or s["kind"] == "figure" or s.get("math_tex") or s.get("excerpt")) and s["kind"] != "exercise" and len(s["points"]) > 2:
            raise ValueError(f"Slide {i}: diagrams, figures, math and excerpts allow at most 2 short points")
        if bool(s["math_tex"]) != bool(s["math_html"]):
            raise ValueError(f"Slide {i}: provide both math_tex and math_html for equivalent editions")
        if not isinstance(s["excerpt"], list) or any(not isinstance(line, str) for line in s["excerpt"]):
            raise ValueError(f"Slide {i}: excerpt must be a list of literal text lines")
        if s["excerpt"] and not 3 <= len(s["excerpt"]) <= 5:
            raise ValueError(f"Slide {i}: excerpts must contain 3–5 short lines")
        for field in ("visual_height_cm", "visual_height", "visual_height_px", "web_visual_height"):
            if field in s and (not isinstance(s[field], (int, float)) or s[field] <= 0):
                raise ValueError(f"Slide {i}: {field} must be a positive number")
        if s.get("image2") and not s.get("image"):
            raise ValueError(f"Slide {i}: image2 requires image")
        if s.get("diagram") and not re.fullmatch(r"[A-Za-z0-9_-]+", s["diagram"]):
            raise ValueError(f"Slide {i}: unsafe diagram ID")
        if s['kind']=='video':
            if not s.get('embed_url','').startswith(('https://www.youtube-nocookie.com/embed/','https://video.sw.siemens.com/embed/')):raise ValueError('Invalid video host')
            if len(s['points'])>2:raise ValueError('Video slides allow two short points')
        slides.append(s)
    return slides


def diagram_records():
    records = {}
    for name in ("diagram_manifest.json", "rigor_manifest.json", "power_graph_manifest.json", "revision_graph_manifest.json", "visual_aid_manifest.json", "domain_visual_manifest.json"):
        path = ROOT / "diagrams" / name
        if not path.exists():
            continue
        manifest = reading.load_json(path)
        entries = manifest.get("diagrams", manifest.get("items", manifest)) if isinstance(manifest, dict) else manifest
        if isinstance(entries, dict):
            records.update(entries)
        else:
            credit = manifest.get("credit", "") if isinstance(manifest, dict) else ""
            records.update({str(item.get("id") or item.get("name")): dict({"credit": credit}, **item) for item in entries})
    return records


def diagram_readings(diagram_ids, slides, sources):
    records = diagram_records()
    sections = []
    for diagram in diagram_ids:
        info = records.get(diagram, {})
        if not isinstance(info, dict):
            info = {"description": str(info)}
        uses = [(i, s) for i, s in enumerate(slides, 1) if s.get("diagram") == diagram]
        fields = [("Credit", info.get("credit", "Original educational diagram created for this tutorial")),
                  ("Used on", "; ".join(str(i) + ". " + s["title"] for i, s in uses)),
                  ("Caption", info.get("caption") or info.get("description") or uses[0][1].get("caption", "")),
                  ("Format", "Native TikZ in the LaTeX edition; vector SVG in the web edition")]
        links = [("SVG diagram", "diagrams/" + diagram + ".svg"),
                 ("Editable TikZ source", "diagrams/" + diagram + ".tex")]
        for key in info.get("refs", info.get("source_refs", [])):
            if key in sources:
                links.append(("Concept source [" + key + "]", sources[key]["url"]))
        sections.append(("Original diagram: " + info.get("title", diagram), fields, links))
    return sections


def combined_image_manifest():
    """Keep original photographs and generated plot provenance in one view."""
    manifest = reading.load_json(ROOT / "images/image_manifest.json", {"images": []})
    records = {item["file"]: dict(item) for item in manifest.get("images", [])}
    for extra_manifest in (ROOT/'images').glob('power_*_manifest.json'):
        extra=reading.load_json(extra_manifest,{})
        entries=extra if isinstance(extra,list) else extra.get('images',extra.get('items',[]))
        if isinstance(entries,dict):entries=entries.values()
        for item in entries:
            if item.get('file'):records[item['file']]=dict(item)
    statistics = reading.load_json(ROOT / "images/rigor_statistics.json", {})
    for extra_manifest in (ROOT / 'images').glob('expanded_*_statistics.json'):
        statistics.update(reading.load_json(extra_manifest, {}))
    for extra_manifest in (ROOT/'images').glob('power_*_statistics.json'):
        statistics.update(reading.load_json(extra_manifest,{}))
    for item in statistics.values():
        if not isinstance(item, dict) or not item.get("file"):
            continue
        record = dict(records.get(item["file"], {}))
        record.update({
            "file": item["file"],
            "credit": item.get("credit", "Original educational plot created for this tutorial"),
            "asset_type": "Original quantitative teaching figure",
            "provenance_note": item.get("caption", ""),
            "evidence_limit": item.get("assumptions", ""),
            "direct_image_url": "images/" + item["file"],
        })
        if item.get("source_url"):
            record["source_page_url"] = item["source_url"]
        records[item["file"]] = record
    for record in records.values():
        for target,source in (('source_page_url','source_url'),('direct_image_url','original_image_url'),
                              ('evidence_limit','assumptions'),('transformation','modifications'),
                              ('license_or_permission_status','reuse_license')):
            if not record.get(target) and record.get(source):record[target]=record[source]
    return {"images": list(records.values())}


def instructor_notes(slides,sources):
    total = sum(s["minutes"] for s in slides)
    out = [f"# Instructor guide — agentic AI for power systems\n\n{len(slides)} static slides in one integrated {total:g}-minute teaching route. "
           + "Evidence reviewed " + reading.REVIEWED + ".\n\n"
           + "All slide content is visible at once. There are no slide transitions, motion effects, click reveals or tables. "
           + "Exercise answers appear only in speaker notes. The separate Full Reading Guide is untimed.\n\n"
           + "Every slide belongs to the session. The paper studies address power-system analysis, operation, planning or evidence tasks. LangGraph and DAG concepts are taught through those applications. The next workshop contains the detailed three GridGuard use cases.\n\n"
           + "## Cumulative teaching route\n\n"]
    elapsed = 0
    for i, s in enumerate(slides, 1):
        end = elapsed + s["minutes"]
        out.append(f"- {reading.stamp(elapsed)}–{reading.stamp(end)} · {i}. {s['title']} ({s['minutes']:g} min)\n")
        elapsed = end
    elapsed = 0
    for i, s in enumerate(slides, 1):
        end = elapsed + s["minutes"]
        out.append(f"\n## {i}. {s['title']}\n\n**Timing:** {reading.stamp(elapsed)}–{reading.stamp(end)} "
                   + f"({s['minutes']:g} minutes).\n\n" + s["note"]
                   + ("\n\n**Takeaway:** " + s["takeaway"] if s["takeaway"] else "")
                   + ("\n\n**Full sources:**\n\n" + complete_sources(s['refs'],sources) if s["refs"] else "") + "\n")
        elapsed = end
    return "".join(out)


def main():
    content = module_from_file("power_content", ROOT / "power_content.py")
    slides = normalized_slides(content)
    sources = reading.load_json(ROOT / "research/source_map.json")
    images = reading.unique(name for s in slides for name in (s["image"], s["image2"]) if name)
    auxiliary_assets = reading.unique(
        Path(name).with_suffix(suffix).name for name in images for suffix in (".pdf", ".svg")
        if Path(name).suffix.lower() in {'.png','.svg'} and Path(name).with_suffix(suffix).name!=name
        and (ROOT / "images" / Path(name).with_suffix(suffix).name).is_file())
    diagrams = reading.unique(s["diagram"] for s in slides if s["diagram"])
    supporting_diagrams=reading.unique(s['alternative_tikz'] for s in slides if s.get('alternative_tikz') and s['alternative_tikz'] not in diagrams)
    source_images={r['file'] for r in combined_image_manifest()['images']
                   if str(r.get('source_page_url','')).startswith('https://')
                   and r.get('asset_type')!='Original quantitative teaching figure'}
    source_image_slides=[i for i,s in enumerate(slides,1) if any(s.get(field) in source_images for field in ('image','image2'))]
    reading_ids = reading.unique([key for s in slides for key in s["refs"]]
                                + list(getattr(content, "READING_IDS", []))
                                + list(getattr(content, "EXTRA_READING_REFS", [])))
    for key in reading_ids:
        if key not in sources:
            raise ValueError("Unresolved reading source: " + key)
    for name in images:
        if Path(name).name != name or not (ROOT / "images" / name).is_file():
            raise ValueError("Missing or unsafe image: " + name)
    for diagram in diagrams:
        for suffix in (".tex", ".svg"):
            if not (ROOT / "diagrams" / (diagram + suffix)).is_file():
                raise ValueError("Missing native diagram asset: " + diagram + suffix)
    for name in ("comsoc-lockup.png", "image7.png"):
        if not (ROOT / "branding" / name).is_file():
            raise ValueError("Missing branding: " + name)
    for key in reading_ids:
        local = reading.local_research(sources[key]["url"])
        if local and not (ROOT / "research" / local).is_file():
            raise ValueError("Missing local source snapshot: " + local)
    for directory in ("latex/images", "latex/diagrams", "slidev/public/images",
                      "slidev/public/diagrams", "slidev/public/branding", "slidev/public/research"):
        (ROOT / directory).mkdir(parents=True, exist_ok=True)
    for name in images + auxiliary_assets:
        for directory in ("latex/images", "slidev/public/images"):
            shutil.copy2(ROOT / "images" / name, ROOT / directory / name)
    for diagram in diagrams:
        for suffix in (".tex", ".svg"):
            for directory in ("latex/diagrams", "slidev/public/diagrams"):
                shutil.copy2(ROOT / "diagrams" / (diagram + suffix), ROOT / directory / (diagram + suffix))
    for name in ("comsoc-lockup.png", "image7.png"):
        shutil.copy2(ROOT / "branding" / name, ROOT / "latex/images" / name)
        shutil.copy2(ROOT / "branding" / name, ROOT / "slidev/public/branding" / name)
    for key in reading_ids:
        local = reading.local_research(sources[key]["url"])
        if local:
            target = ROOT / "slidev/public/research" / local
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / "research" / local, target)
    latin_modern.copy_web_fonts(ROOT / "slidev/public/fonts")
    frames = "\n".join(line.rstrip() for line in "".join(render_frame(s, sources) for s in slides).splitlines()) + "\n"
    front = """---
theme: default
title: Agentic AI for Utility Operators — Power Systems and Agent Workflows
info: Integrated power-system tutorial with deployment news, LangGraph, DAGs, measured paper results and complete readings
author: Alaa Selim (MIT/Dartmouth) and Mohamed Chehada (UT Austin)
transition: none
aspectRatio: 16/9
canvasWidth: 1280
colorSchema: light
fonts:
  sans: Latin Modern Roman
  serif: Latin Modern Roman
  mono: Latin Modern Mono
  provider: none
mdc: false
drawings:
  persist: false
download: false
---

"""
    deck = front + "\n---\ntransition: none\n---\n\n".join(
        render_slide(s, i, len(slides), sources) for i, s in enumerate(slides, 1))
    for token in ("v-click", "v-motion", r"\transfade", r"\uncover<", r"\item<", r"\pause",
                  r"\begin{tabular}", "<table"):
        if token in frames or token in deck:
            raise ValueError("Unexpected table or non-static content: " + token)
    sections = reading.reading_sections(reading_ids, sources, slides, combined_image_manifest())
    sections += diagram_readings(diagrams, slides, sources)
    markdown, guide_html, guide_tex = reading.reading_guides(sections)
    markdown = markdown.replace("introductory lecture", "integrated power-system engineering tutorial")
    guide_html = guide_html.replace("introductory lecture", "integrated power-system engineering tutorial")
    guide_tex = guide_tex.replace("introductory lecture", "integrated power-system engineering tutorial")
    guide_html=latin_modern.style_html(guide_html)
    outputs = {
        "latex/frames.tex": frames, "slidev/slides.md": deck,
        "Instructor_Guide.md": instructor_notes(slides,sources),
        "lesson_content.json": json.dumps(slides, ensure_ascii=False, indent=2) + "\n",
        "latex/reading_guide.tex": guide_tex, "References.md": markdown,
        "Full_Reading_Guide.html": guide_html, "slidev/public/Full_Reading_Guide.html": guide_html,
    }
    for name, text in outputs.items():
        (ROOT / name).write_text(text, encoding="utf-8")
    manifest = {
        "edition": "power-systems",
        "main_slides": len(slides), "minutes": sum(s["minutes"] for s in slides),
        "core_slides": len(slides),
        "extension_slides": [],
        "extension_minutes": 0,
        "reading_sources": len(reading_ids), "reading_source_ids": reading_ids,
        "used_images": images, "used_auxiliary_assets": auxiliary_assets,
        "used_diagrams": diagrams, "transitions": "none",
        "supporting_editable_diagrams":supporting_diagrams,
        "source_image_slides":source_image_slides,"source_image_slide_count":len(source_image_slides),
        "click_reveals": 0, "tables": 0, "reading_guide_timed": False,
        "exercise_slides": [i for i, s in enumerate(slides, 1) if s["kind"] == "exercise"],
        "source_content": "power_content.py", "source_registry": "research/source_map.json",
        "source_content_sha256": hashlib.sha256((ROOT / "power_content.py").read_bytes()).hexdigest(),
        "outputs": list(outputs),
    }
    (ROOT / "build_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: manifest[key] for key in
                      ("main_slides", "minutes", "reading_sources", "used_diagrams", "transitions", "tables")}))


if __name__ == "__main__":
    main()

