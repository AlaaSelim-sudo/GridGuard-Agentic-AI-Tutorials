"""Verify extraction provenance without rerunning the notebook."""
from pathlib import Path
import base64
import hashlib
import html
import json
from PIL import Image

root = Path(__file__).resolve().parent
manifest = json.loads((root / 'hands_on_manifest.json').read_text(encoding='utf-8'))
sha = lambda data: hashlib.sha256(data).hexdigest()
sourcebytes = Path(manifest['source_notebook']).read_bytes()
notebook = json.loads(sourcebytes)
cells = {c['id']: c for c in notebook['cells']}
joined = lambda x: ''.join(x) if isinstance(x, list) else x
assert sha(sourcebytes) == manifest['source_notebook_sha256']
assert (root / manifest['preserved_copy']).read_bytes() == sourcebytes
verified = []
for item in manifest['assets']:
    output = cells[item['source_cell_id']]['outputs'][item['output_index']]
    imagepath = (root / item['file']).resolve()
    imagebytes = imagepath.read_bytes()
    assert sha(imagebytes) == item['image_sha256'], item['id']
    with Image.open(imagepath) as image:
        assert list(image.size) == item['dimensions_px'], item['id']
        image.verify()
    if item['kind'] == 'original_png_output':
        assert imagebytes == base64.b64decode(joined(output['data']['image/png'])), item['id']
    else:
        expected = joined(output['data']['text/html']) if item['mime_type']=='text/html' else joined(output['text'])
        assert (root / item['raw_output']).read_bytes() == expected.encode(), item['id']
        assert sha(expected.encode()) == item['source_mime_content_sha256'], item['id']
        pagebytes = (root / item['capture_page']).read_bytes()
        assert sha(pagebytes) == item['capture_page_sha256'], item['id']
        assert sha(item['capture_css'].encode()) == item['capture_css_sha256'], item['id']
        assert item['capture_checks']['capture_scroll_width'] <= item['capture_checks']['capture_width'], item['id']
        assert not item['capture_checks']['overflowing_visible_cells'], item['id']
        if item.get('selected_rows'):
            assert item['capture_checks']['table_data_rows_visible'] == len(item['selected_rows'])
        if item.get('selected_columns'):
            assert item['capture_checks']['visible_header_labels'] == [''] + item['selected_columns']
    verified.append(item['id'])
review = (root / 'index.html').read_text(encoding='utf-8')
assert sha(review.encode()) == manifest['review_page']['sha256']
for cell in notebook['cells']:
    assert f'id="{cell["id"]}"' in review
    assert html.escape(joined(cell.get('source',''))) in review
    for output in cell.get('outputs', []):
        data = output.get('data',{})
        if 'text/html' in data:
            assert joined(data['text/html']) in review
        if 'image/png' in data:
            assert joined(data['image/png']) in review
assert manifest['review_page']['browser_checks']['cells'] == len(notebook['cells'])
assert manifest['review_page']['browser_checks']['plots_loaded']
report = {
    'status':'PASS',
    'notebook_byte_preserved':True,
    'notebook_sha256':sha(sourcebytes),
    'asset_count':len(verified),
    'exact_png_outputs':sum(i['kind']=='original_png_output' for i in manifest['assets']),
    'browser_captures':sum(i['kind']=='browser_capture' for i in manifest['assets']),
    'original_source_cells_preserved_in_review':len(notebook['cells']),
    'checks':['Image hashes/dimensions/PNG validity','Original PNG outputs byte-identical','Raw captured outputs match source MIME/text exactly','Capture page and CSS hashes','No browser overflow','Selected rows/columns match recorded region','Every source cell and HTML/image output retained in review'],
    'verified_assets':verified,
}
(root / 'verification_report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
