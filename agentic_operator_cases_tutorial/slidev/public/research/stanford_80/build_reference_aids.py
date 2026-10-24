"""Export two attributed Stanford lecture excerpts and an original grid review aid.

Re-extract with --source path/to/l-introduction.pdf. The supplied excerpt PDFs
also allow a portable PNG regeneration without redistributing the full lecture.
"""
from pathlib import Path
import argparse,hashlib,importlib.util,json,subprocess
from pypdf import PdfReader,PdfWriter
ROOT=Path(__file__).resolve().parents[2]
POP=Path(r'C:/Users/f00863x/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe')
SOURCE_URL='https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf'
EXCERPTS=[('stanford_wikichat_steps',19,[85,150,1190,560]),('stanford_genie_specification',40,[145,267,1220,540])]
REVIEW=r'''\begingroup
\begin{tikzpicture}[x=1cm,y=1cm,font=\sffamily\fontsize{9.5}{12}\selectfont,
every node/.style={text=Navy,align=center}]
\path[use as bounding box] (0,0) rectangle (14.5,4.1);
\foreach \x/\n/\head/\question in {1.8/1/Evidence/Which tool result supports the claim?,5.4/2/Assumptions/Which inputs and model were used?,9.0/3/Rules/Were the same limits and priorities kept?,12.6/4/Next step/What does the operator still need to review?}{
 \node[circle,draw=IEEEBlue,line width=1pt,minimum size=.7cm] at (\x,2.8) {\n};
 \node[text=IEEEBlue,font=\sffamily\bfseries] at (\x,2.05) {\head};
 \node[text width=3.1cm] at (\x,1.15) {\question};
}
\end{tikzpicture}
\endgroup
'''
def main():
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path);args=p.parse_args()
 manifest=[]
 if args.source:
  reader=PdfReader(args.source);source_sha=hashlib.sha256(args.source.read_bytes()).hexdigest()
  assert len(reader.pages)==58
  for name,number,rect in EXCERPTS:
   page=reader.pages[number-1];width=float(page.mediabox.width);height=float(page.mediabox.height)
   x0,y0,x1,y1=rect
   page.cropbox.lower_left=(x0*width/1280,height-y1*height/720)
   page.cropbox.upper_right=(x1*width/1280,height-y0*height/720)
   page.mediabox=page.cropbox
   writer=PdfWriter();writer.add_page(page)
   with (ROOT/'images'/f'{name}.pdf').open('wb') as f:writer.write(f)
   manifest.append(dict(file=f'{name}.png',original_pdf_sha256=source_sha,original_page=number,
    crop_pixels_at_1280_by_720=rect,source_url=SOURCE_URL+'#page='+str(number),
    credit='Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026.',
    transformation='Cropped vector excerpt from the supplied lecture PDF, with all contents inside the selected rectangle unchanged.'))
  (ROOT/'research/stanford_80/excerpt_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
 for name,_,_ in EXCERPTS:
  subprocess.run([str(POP),'-singlefile','-png','-scale-to-x','1600','-scale-to-y','-1',str(ROOT/'images'/f'{name}.pdf'),str(ROOT/'images'/name)],check=True,capture_output=True)
 src=ROOT/'diagrams/lab_review_questions.tex';src.write_text(REVIEW,encoding='utf-8')
 spec=importlib.util.spec_from_file_location('compiler',ROOT/'build_diagrams.py');compiler=importlib.util.module_from_spec(spec);spec.loader.exec_module(compiler)
 compiler.TECTONIC=Path(r'C:/Users/f00863x/OPRO/tmp/tectonic_017/unpacked/tectonic.exe')
 compiler.compile_one(src)
 log=(compiler.BUILD/'lab_review_questions_wrapper.log').read_text(encoding='utf-8',errors='replace')
 assert 'Overfull' not in log and 'Missing character' not in log
 print('Two original Stanford excerpts and one grid review diagram ready.')
if __name__=='__main__':main()
