"""Extract original executed notebook output; preserve source bytes and provenance."""
from pathlib import Path
import base64
import hashlib
import html
import json
import re
import shutil
import os

SOURCE = Path(os.environ.get('CLASSROOM_EXECUTED_NOTEBOOK',r'C:\Users\f00863x\OPRO\tmp\colab_publication_qa\Classroom_Labs.executed.ipynb'))
HERE = Path(__file__).resolve().parent
CASES = HERE.parent.parent
IMAGES = CASES / 'images'
HERE.mkdir(parents=True, exist_ok=True)
IMAGES.mkdir(exist_ok=True)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def joined(value):
    return ''.join(value) if isinstance(value, list) else value

source_bytes = SOURCE.read_bytes()
notebook = json.loads(source_bytes)
cells = {cell['id']: cell for cell in notebook['cells']}
shutil.copyfile(SOURCE, HERE / SOURCE.name)
assert (HERE / SOURCE.name).read_bytes() == source_bytes

CSS = '''
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; background: white; color: #172b40; }
body { font-family: Arial, Helvetica, sans-serif; }
#capture { width: 1100px; padding: 24px 28px 26px; border-top: 7px solid #006699; background: white; }
.eyebrow { font-size: 17px; color: #006699; font-weight: 700; letter-spacing: .02em; margin: 0 0 9px; }
h1 { font-size: 25px; line-height: 1.16; color: #003b60; margin: 0 0 11px; font-weight: 700; }
.provenance { font-size: 16px; line-height: 1.35; color: #536273; margin: 0 0 16px; }
.selection { font-size: 16px; color: #536273; margin: -5px 0 13px; }
table.dataframe { border-collapse: collapse !important; border: none !important; width: 100% !important; table-layout: fixed; font-size: 18px !important; line-height: 1.25 !important; color: #172b40 !important; }
table.dataframe thead { background: #e7f2f7 !important; color: #003b60 !important; }
table.dataframe th, table.dataframe td { border: none !important; border-bottom: 1px solid #c8dce6 !important; padding: 11px 8px !important; text-align: left !important; vertical-align: middle !important; overflow-wrap: anywhere; word-break: normal; }
table.dataframe thead th { font-weight: 700 !important; }
table.dataframe tbody tr:nth-child(even) { background: #f5f8fa !important; }
table.dataframe tbody th, table.dataframe thead th:first-child { width: 35px !important; color: #617483; }
pre.actual-stream { white-space: pre-wrap; overflow-wrap: anywhere; margin: 2px 0 0; font: 20px/1.55 'Consolas', 'Courier New', monospace; color: #172b40; padding: 15px 18px; border-left: 4px solid #00a3c7; background: #f3f8fb; }
'''

specs = [
    ('L1_binding', 'classroom-004', 0, 'classroom-003', None),
    ('L2_table', 'classroom-007', 1, 'classroom-006', None),
    ('L4_checks', 'classroom-013', 1, 'classroom-012', None),
    ('L5_scope', 'classroom-016', 0, 'classroom-015', None),
    ('L6_table', 'classroom-018', 0, 'classroom-017', None),
    ('L6_table_full', 'classroom-018', 0, 'classroom-017', None),
    ('L7_binding', 'classroom-021', 0, 'classroom-020', None),
    ('L9_trust', 'classroom-026', 0, 'classroom-025', None),
    ('L12_packet', 'classroom-033', 0, 'classroom-032', ['state','evidence_matches','engineering_pass','scope_matches','scope','acknowledged','equipment_dispatch']),
    ('L12_packet_full', 'classroom-033', 0, 'classroom-032', None),
]

manifest = {
    'schema_version': 1,
    'source_notebook': str(SOURCE),
    'source_notebook_sha256': sha(source_bytes),
    'source_notebook_bytes': len(source_bytes),
    'preserved_copy': 'Classroom_Labs.executed.ipynb',
    'preserved_copy_sha256': sha((HERE / SOURCE.name).read_bytes()),
    'output_indexing': 'Zero-based index into the source cell outputs array.',
    'capture_description': 'Browser screenshots of actual executed output, with original lab heading and provenance added outside the output. These are not Colab UI screenshots.',
    'capture_css': CSS,
    'capture_css_sha256': sha(CSS.encode()),
    'assets': [],
}

for lab, cellid, outindex, headingid, selection in specs:
    cell = cells[cellid]
    output = cell['outputs'][outindex]
    heading_source = joined(cells[headingid]['source'])
    heading = heading_source.splitlines()[0].lstrip('# ').strip()
    extra_css = ''
    if lab in {'L2_table', 'L4_checks', 'L6_table', 'L6_table_full'}:
        extra_css += '\ntable.dataframe { table-layout: auto; } table.dataframe tbody td { white-space: nowrap; }'
    if lab == 'L2_table':
        extra_css += '\ntable.dataframe thead th:nth-child(3), table.dataframe thead th:nth-child(10) { white-space: nowrap; }'
    if lab in {'L6_table', 'L6_table_full'}:
        extra_css += '\ntable.dataframe th, table.dataframe td { padding: 7px 7px !important; }'
    if lab == 'L6_table':
        extra_css += '\ntable.dataframe tbody tr:nth-child(n+3) { display: none !important; }'
    if 'text/html' in output.get('data', {}):
        mime = 'text/html'
        payload = joined(output['data'][mime])
        output_html = payload
        if selection:
            # Preserve the actual source HTML verbatim; hide unselected columns via CSS.
            # The source index plus seven contiguous data columns are retained.
            headers = re.findall(r'<th>(.*?)</th>', payload.split('</thead>')[0], flags=re.S)
            labels = [re.sub('<[^>]+>', '', h) for h in headers]
            selected_positions = [labels.index(label) + 1 for label in selection]
            kept = {1, *selected_positions}
            hidden = [pos for pos in range(1, len(labels) + 1) if pos not in kept]
            extra_css += '\n'.join(f'table.dataframe tr > :nth-child({pos}) {{ display: none !important; }}' for pos in hidden)
            extra_css += '\ntable.dataframe { table-layout: auto; }'
    else:
        mime = 'text/plain'
        payload = joined(output['text'])
        output_html = '<pre class="actual-stream">' + html.escape(payload) + '</pre>'
    stem = 'hands_on_' + lab
    raw = HERE / (stem + '.output.' + ('html' if mime == 'text/html' else 'txt'))
    raw.write_bytes(payload.encode('utf-8'))
    selection_note = ''
    if selection:
        selection_note = '<p class="selection">Contiguous columns: state through equipment_dispatch; original row order and row index.</p>'
    if lab == 'L6_table':
        selection_note = '<p class="selection">Actual output header and rows 0–1 · tie_capacity_kw = 40.0</p>'
    page = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{html.escape(stem)}</title><style>{CSS}\n{extra_css}</style></head><body>'
            '<main id="capture"><p class="eyebrow">Executed notebook output</p>'
            f'<h1>{html.escape(heading)}</h1>'
            f'<p class="provenance">{cellid} · output {outindex} (zero-based) · recorded execution {cell.get("execution_count")}</p>'
            + selection_note + '<section class="actual-output">' + output_html + '</section></main></body></html>')
    pagepath = HERE / (stem + '.capture.html')
    pagepath.write_bytes(page.encode('utf-8'))
    manifest['assets'].append({
        'id': stem, 'kind': 'browser_capture',
        'file': f'../../images/{stem}.png',
        'capture_page': pagepath.name,
        'raw_output': raw.name,
        'source_cell_id': cellid,
        'source_cell_index': notebook['cells'].index(cell),
        'source_heading_cell_id': headingid,
        'source_heading': heading,
        'output_index': outindex,
        'execution_count': cell.get('execution_count'),
        'mime_type': mime,
        'source_mime_content_sha256': sha(payload.encode()),
        'capture_page_sha256': sha(page.encode()),
        'capture_css': CSS + '\n' + extra_css,
        'capture_css_sha256': sha((CSS + '\n' + extra_css).encode()),
        'formatting_only_dom_changes': 'Browser inserts wbr elements after existing underscores in table labels and text, permitting logical line breaks without changing any characters. Source output HTML remains unchanged.',
        'selected_columns': selection,
        'selected_rows': [0, 1] if lab == 'L6_table' else None,
        'selection_method': ('CSS hides rows after original rows 0 and 1, retaining the complete header and every column; source HTML unchanged.' if lab == 'L6_table' else 'CSS hides columns outside one contiguous data-column range, retaining original row index; source HTML unchanged.' if selection else 'Entire actual output.'),
        'credit': 'Original recorded classroom notebook output; captured from the byte-preserved executed notebook.',
    })

for lab, cellid, outindex in [('L2','classroom-007',2), ('L6','classroom-018',1), ('L8','classroom-023',1)]:
    payload = joined(cells[cellid]['outputs'][outindex]['data']['image/png'])
    rawbytes = base64.b64decode(payload)
    file = IMAGES / f'hands_on_{lab}_plot.png'
    file.write_bytes(rawbytes)
    from PIL import Image
    with Image.open(file) as image:
        dims = list(image.size)
    manifest['assets'].append({
        'id': f'hands_on_{lab}_plot', 'kind': 'original_png_output',
        'file': f'../../images/{file.name}',
        'source_cell_id': cellid,
        'source_cell_index': notebook['cells'].index(cells[cellid]),
        'output_index': outindex,
        'mime_type': 'image/png',
        'image_sha256': sha(rawbytes),
        'source_decoded_png_sha256': sha(rawbytes),
        'bytes': len(rawbytes),
        'dimensions_px': dims,
        'transformations': 'None. Exact base64-decoded image/png bytes.',
        'credit': 'Original plot embedded in the executed classroom notebook; extracted without redrawing, rescaling or restyling.',
    })

# Review page: render every original source cell and every recorded output.
# Raw Markdown is retained in an expandable block to avoid losing any original text.
def inline(text):
    text = html.escape(text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'<a href="\2">\1</a>', text)
    return text

def markdown_basic(source):
    result, paragraph, in_code = [], [], False
    def flush():
        if paragraph:
            result.append('<p>' + '<br>'.join(inline(x) for x in paragraph) + '</p>')
            paragraph.clear()
    for line in source.splitlines():
        if line.startswith('```'):
            flush()
            result.append('</pre>' if in_code else '<pre class="source">')
            in_code = not in_code
        elif in_code:
            result.append(html.escape(line) + '\n')
        elif re.match(r'^#{1,6}\s', line):
            flush()
            level = min(len(line)-len(line.lstrip('#')), 3)
            result.append(f'<h{level}>' + inline(line.lstrip('# ').strip()) + f'</h{level}>')
        elif not line.strip():
            flush()
        else:
            paragraph.append(line)
    flush()
    if in_code:
        result.append('</pre>')
    return '\n'.join(result)

review_css = '''
:root { color-scheme: light; } *{box-sizing:border-box} body{margin:0;background:#f4f7fa;color:#172b40;font:18px/1.5 Arial,Helvetica,sans-serif}main{max-width:1180px;margin:auto;padding:32px 32px 70px}header{border-top:7px solid #006699;padding:25px;background:white;margin-bottom:25px}h1,h2,h3{color:#003b60;line-height:1.2}h1{font-size:32px}h2{font-size:27px}h3{font-size:22px}.cell{background:white;border:1px solid #d8e1e8;border-left:4px solid #c7dce7;padding:22px 24px;margin:22px 0;overflow:auto}.cellid{font:15px/1.4 Consolas,monospace;color:#536273;margin-bottom:15px}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:15px/1.45 Consolas,monospace}.source{padding:18px;background:#f1f5f8}.output{margin:20px 0;padding:12px 0;overflow:auto;border-top:1px solid #d8e1e8}.output-label{font:14px Consolas,monospace;color:#536273}table.dataframe{border-collapse:collapse;font-size:16px;min-width:600px}table.dataframe th,table.dataframe td{padding:9px 10px;border:1px solid #d5e1e9;text-align:left;vertical-align:top}table.dataframe thead{background:#e7f2f7;color:#003b60}table.dataframe tbody tr:nth-child(even){background:#f5f8fa}.plot{max-width:100%;height:auto}a{color:#006699}code{font-size:.9em;background:#eef3f7;padding:1px 4px}summary{cursor:pointer;color:#006699}.hash{font:14px/1.5 Consolas,monospace;overflow-wrap:anywhere}.notice{font-size:17px;color:#536273}
'''
parts = [f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Executed classroom notebook — review</title><style>{review_css}</style></head><body><main>',
         '<header><h1>Executed classroom notebook</h1><p>Original source cells and recorded outputs, preserved for audience review. This page displays executed results; it does not execute code.</p>',
         '<p><a href="Classroom_Labs.executed.ipynb">Download the byte-preserved executed notebook</a> · <a href="hands_on_manifest.json">Output provenance and hashes</a></p>',
         f'<p class="hash">Notebook SHA-256: {sha(source_bytes)}</p><p class="notice">Browser captures are labeled “Executed notebook output” and do not reproduce the Colab interface. Tables below retain all recorded columns and rows; wide tables scroll horizontally.</p></header>']
for ci, cell in enumerate(notebook['cells']):
    source = joined(cell.get('source', ''))
    parts.append(f'<article class="cell" id="{cell["id"]}"><div class="cellid">Cell {ci} · {cell["id"]} · {cell["cell_type"]}' + (f' · recorded execution {cell.get("execution_count")}' if cell['cell_type']=='code' else '') + '</div>')
    if cell['cell_type'] == 'markdown':
        parts.append(markdown_basic(source))
        parts.append('<details><summary>Original Markdown source</summary><pre class="source">' + html.escape(source) + '</pre></details>')
    else:
        parts.append('<details><summary>Original code cell</summary><pre class="source">' + html.escape(source) + '</pre></details>')
        for oi, output in enumerate(cell.get('outputs', [])):
            parts.append(f'<section class="output"><p class="output-label">Executed output {oi} (zero-based)</p>')
            data = output.get('data', {})
            if 'image/png' in data:
                parts.append('<img class="plot" alt="Original plot output from ' + cell['id'] + '" src="data:image/png;base64,' + joined(data['image/png']) + '">')
            elif 'text/html' in data:
                parts.append(joined(data['text/html']))
            elif 'text/plain' in data:
                parts.append('<pre>' + html.escape(joined(data['text/plain'])) + '</pre>')
            elif 'text' in output:
                parts.append('<pre>' + html.escape(joined(output['text'])) + '</pre>')
            elif output.get('output_type') == 'error':
                parts.append('<pre>' + html.escape('\n'.join(output.get('traceback', []))) + '</pre>')
            parts.append('</section>')
    parts.append('</article>')
parts.append('</main></body></html>')
review = '\n'.join(parts)
(HERE / 'index.html').write_bytes(review.encode('utf-8'))
manifest['review_page'] = {'file':'index.html','sha256':sha(review.encode()),'source_cells':len(notebook['cells']),'preserves':'Every original source cell and recorded output; all original HTML table columns and rows; exact embedded plot PNG bytes. Code is displayed only, not executed.'}
(HERE / 'hands_on_manifest.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding='utf-8')
print(json.dumps({'raw_plots':3, 'capture_pages':len(specs), 'source_sha256':sha(source_bytes), 'review_cells':len(notebook['cells'])}, indent=2))
