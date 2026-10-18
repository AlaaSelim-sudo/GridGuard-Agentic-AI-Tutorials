"""Compile the editable TikZ teaching diagrams and make matching vector SVGs."""
from pathlib import Path
import ctypes,json,os,re,shutil,subprocess
from PIL import Image,ImageChops
from pypdf import PdfReader,PdfWriter

ROOT=Path(__file__).resolve().parent
DIAGRAMS=ROOT/'diagrams';BUILD=DIAGRAMS/'_build'
BUILD.mkdir(exist_ok=True)
RUNTIME=Path(os.environ.get('OPERATOR_RUNTIME',r'C:/Users/f00863x/.cache/codex-runtimes/codex-primary-runtime/dependencies'))
POPPLER=RUNTIME/'native/poppler/Library/bin'
TECTONIC=Path(os.environ.get('OPERATOR_TECTONIC',r'C:/Users/f00863x/OPRO/tmp/tectonic-0.17.0/tectonic.exe'))
ENV=dict(os.environ,TECTONIC_CACHE_DIR=os.environ.get('TECTONIC_CACHE_DIR',r'C:/Users/f00863x/OPRO/tmp/tectonic_cache_017_fresh'))
PRE=r'''\documentclass{article}
\usepackage[paperwidth=16.5cm,paperheight=8cm,margin=.12cm]{geometry}
\usepackage[T1]{fontenc}\usepackage{lmodern,amsmath,amssymb,tikz}
\DeclareMathSizes{12}{10}{10}{10}
\DeclareMathSizes{11}{10}{10}{10}
\DeclareMathSizes{10.95}{10}{10}{10}
\DeclareMathSizes{10}{10}{10}{10}
\usetikzlibrary{arrows.meta,positioning,calc,shapes.geometric,fit,backgrounds,decorations.pathreplacing}
\definecolor{IEEEBlue}{HTML}{00629B}\definecolor{Cyan}{HTML}{00A6B2}
\definecolor{Navy}{HTML}{003B5C}\definecolor{Slate}{HTML}{526470}
\definecolor{Red}{HTML}{B83136}\definecolor{Amber}{HTML}{A66610}
\colorlet{red}{Red}\colorlet{amber}{Amber}\colorlet{navy}{Navy}\colorlet{slate}{Slate}
\colorlet{teal}{Cyan}\colorlet{blue}{IEEEBlue}\colorlet{pale}{Cyan!6}
\pagestyle{empty}\setlength{\parindent}{0pt}
\begin{document}\noindent
'''

def svg_from_pdf(pdf,svg):
    dll_dir=os.add_dll_directory(str(POPPLER))
    cairo=ctypes.CDLL(str(POPPLER/'cairo.dll'))
    poppler=ctypes.CDLL(str(POPPLER/'poppler-glib.dll'))
    gobject=ctypes.CDLL(str(POPPLER/'gobject-2.0-0.dll'))
    ptr=ctypes.c_void_p
    cairo.cairo_svg_surface_create.argtypes=[ctypes.c_char_p,ctypes.c_double,ctypes.c_double];cairo.cairo_svg_surface_create.restype=ptr
    cairo.cairo_create.argtypes=[ptr];cairo.cairo_create.restype=ptr
    cairo.cairo_surface_finish.argtypes=[ptr];cairo.cairo_destroy.argtypes=[ptr];cairo.cairo_surface_destroy.argtypes=[ptr]
    poppler.poppler_document_new_from_file.argtypes=[ctypes.c_char_p,ctypes.c_char_p,ptr];poppler.poppler_document_new_from_file.restype=ptr
    poppler.poppler_document_get_page.argtypes=[ptr,ctypes.c_int];poppler.poppler_document_get_page.restype=ptr
    poppler.poppler_page_get_size.argtypes=[ptr,ctypes.POINTER(ctypes.c_double),ctypes.POINTER(ctypes.c_double)]
    poppler.poppler_page_render_for_printing.argtypes=[ptr,ptr];gobject.g_object_unref.argtypes=[ptr]
    doc=poppler.poppler_document_new_from_file(pdf.as_uri().encode(),None,None)
    if not doc:raise RuntimeError(str(pdf))
    page=poppler.poppler_document_get_page(doc,0);w,h=ctypes.c_double(),ctypes.c_double()
    poppler.poppler_page_get_size(page,ctypes.byref(w),ctypes.byref(h))
    surface=cairo.cairo_svg_surface_create(str(svg).encode(),w.value,h.value);context=cairo.cairo_create(surface)
    poppler.poppler_page_render_for_printing(page,context)
    cairo.cairo_destroy(context);cairo.cairo_surface_finish(surface);cairo.cairo_surface_destroy(surface)
    gobject.g_object_unref(page);gobject.g_object_unref(doc);dll_dir.close()
    text=svg.read_text(encoding='utf-8')
    text=re.sub(r'<svg ([^>]*?)width="[^"]+" height="[^"]+"',lambda m:f'<svg {m.group(1)}width="1280" height="{round(1280*h.value/w.value)}"',text,count=1)
    svg.write_text(text,encoding='utf-8')

def compile_one(source):
    wrapper=BUILD/(source.stem+'_wrapper.tex')
    wrapper.write_text(PRE+'\\input{../'+source.name+'}\n\\end{document}\n',encoding='utf-8')
    p=subprocess.run([str(TECTONIC),'--only-cached','--keep-logs',wrapper.name],cwd=BUILD,env=ENV,capture_output=True,text=True)
    if p.returncode:raise RuntimeError(source.name+'\n'+p.stdout+'\n'+p.stderr)
    pdf=wrapper.with_suffix('.pdf')
    reader=PdfReader(pdf)
    pages=[p for p in reader.pages if (p.extract_text() or '').strip()]
    assert len(pages)==1,(source.name,len(pages))
    writer=PdfWriter();writer.add_page(pages[0])
    temporary=BUILD/(source.stem+'_one.pdf')
    with temporary.open('wb') as f:writer.write(f)
    raster=BUILD/(source.stem+'_bounds')
    subprocess.run([str(POPPLER/'pdftoppm.exe'),'-png','-singlefile','-r','100',str(temporary),str(raster)],check=True,capture_output=True)
    im=Image.open(raster.with_suffix('.png')).convert('RGB')
    diff=ImageChops.difference(im,Image.new('RGB',im.size,'white')).convert('L').point(lambda x:255 if x>30 else 0)
    bounds=diff.getbbox();assert bounds,source.name
    x0,y0,x1,y1=bounds
    page=writer.pages[0];l,b,r,t=map(float,page.mediabox);sx=(r-l)/im.width;sy=(t-b)/im.height
    pad=4
    page.mediabox.lower_left=(max(l,l+x0*sx-pad),max(b,t-y1*sy-pad))
    page.mediabox.upper_right=(min(r,l+x1*sx+pad),min(t,t-y0*sy+pad));page.cropbox=page.mediabox
    output=DIAGRAMS/(source.stem+'.pdf')
    with output.open('wb') as f:writer.write(f)
    svg_from_pdf(output,DIAGRAMS/(source.stem+'.svg'))
    print('Ready:',source.stem,flush=True)

if __name__=='__main__':
    import sys
    selected=sys.argv[1:]
    for source in sorted(DIAGRAMS.glob('*.tex')):
        if selected and source.stem not in selected:continue
        if not selected and source.with_suffix('.svg').exists() and source.with_suffix('.svg').stat().st_mtime>source.stat().st_mtime:continue
        compile_one(source)
