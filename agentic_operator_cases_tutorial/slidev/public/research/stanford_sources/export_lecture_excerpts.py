"""Extract attributed vector figure selections from the presenter-supplied lecture.

Use --source path/to/l-introduction.pdf. No contents within either crop are
redrawn or changed. Full source, page, crop and SHA-256 are recorded.
"""
from pathlib import Path
import argparse,hashlib,json,subprocess
from pypdf import PdfReader,PdfWriter
ROOT=Path(__file__).resolve().parents[2]
POP=Path(r'C:/Users/f00863x/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe')
URL='https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf'
EXCERPTS=[('stanford_agentic_capabilities',2,[643,135,1221,397]),
          ('stanford_language_decision',53,[225,302,1235,411])]
def main():
 parser=argparse.ArgumentParser();parser.add_argument('--source',type=Path,required=True);args=parser.parse_args()
 data=args.source.read_bytes();reader=PdfReader(args.source);assert len(reader.pages)==58
 manifest=[]
 for name,number,rect in EXCERPTS:
  page=reader.pages[number-1];w=float(page.mediabox.width);h=float(page.mediabox.height)
  x0,y0,x1,y1=rect;page.cropbox.lower_left=(x0*w/1280,h-y1*h/720)
  page.cropbox.upper_right=(x1*w/1280,h-y0*h/720);page.mediabox=page.cropbox
  writer=PdfWriter();writer.add_page(page);pdf=ROOT/'images'/(name+'.pdf')
  with pdf.open('wb') as f:writer.write(f)
  subprocess.run([str(POP),'-singlefile','-png','-scale-to-x','1800','-scale-to-y','-1',str(pdf),str(pdf.with_suffix(''))],check=True,capture_output=True)
  image=pdf.with_suffix('.png')
  manifest.append(dict(file=image.name,vector_file=pdf.name,original_page=number,
   original_pdf_sha256=hashlib.sha256(data).hexdigest(),source_url=URL+'#page='+str(number),
   crop_pixels_at_1280_by_720=rect,image_sha256=hashlib.sha256(image.read_bytes()).hexdigest(),
   credit='Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026.',
   transformation='Unchanged contents within the selected rectangle of the supplied lecture. Vector PDF crop and Poppler PNG rendering.',
   evidence_limit='Source lecture examples. The application to power-system studies is our teaching adaptation; no Stanford runtime is executed in the classroom notebook.'))
 (ROOT/'research/stanford_sources/excerpt_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'excerpts':len(manifest),'pages':[e['original_page'] for e in manifest]}))
if __name__=='__main__':main()
