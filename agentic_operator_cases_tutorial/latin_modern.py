"""Latin Modern assets shared by the workshop's PDF and HTML documents."""
from pathlib import Path
import shutil

ROOT=Path(__file__).resolve().parent
FONTS=ROOT/'fonts'

def css(prefix='fonts/'):
    faces=[]
    for name,file,weight,style in [
        ('Latin Modern Roman','lmroman10-regular.otf',400,'normal'),
        ('Latin Modern Roman','lmroman10-bold.otf',700,'normal'),
        ('Latin Modern Roman','lmroman10-italic.otf',400,'italic'),
        ('Latin Modern Mono','lmmono10-regular.otf',400,'normal'),
    ]:
        faces.append("@font-face{font-family:'"+name+"';src:url('"+prefix+file+"') format('opentype');font-weight:"+str(weight)+";font-style:"+style+";font-display:block;}")
    return '\n'.join(faces)+"\nbody{font-family:'Latin Modern Roman',serif;font-synthesis:none;}h1,h2,h3,h4,strong,b{font-family:'Latin Modern Roman',serif;}pre,code{font-family:'Latin Modern Mono',monospace;}"

def style_html(text,prefix='fonts/'):
    return text.replace('</style>',css(prefix)+'</style>',1)

def copy_web_fonts(destination):
    destination=Path(destination);destination.mkdir(parents=True,exist_ok=True)
    for file in list(FONTS.glob('*.otf'))+[FONTS/'GUST-FONT-LICENSE.TXT']:
        shutil.copy2(file,destination/file.name)

def register_reportlab():
    from reportlab.pdfbase import pdfmetrics
    for stem,alias in [('lmr10','LMRoman'),('lmbx10','LMRomanBold'),('lmri10','LMRomanItalic'),('lmbxi10','LMRomanBoldItalic')]:
        if alias not in pdfmetrics.getRegisteredFontNames():
            face=pdfmetrics.EmbeddedType1Face(str(FONTS/(stem+'.afm')),str(FONTS/(stem+'.pfb')))
            # Latin Modern AFM metrics use decimal values; ReportLab keeps these as strings.
            for field in ['ascent','descent','capHeight','xHeight','italicAngle','stemV']:
                value=getattr(face,field,None)
                if isinstance(value,str):
                    try:setattr(face,field,float(value))
                    except ValueError:pass
            pdfmetrics.registerTypeFace(face)
            pdfmetrics.registerFont(pdfmetrics.Font(alias,face.name,'WinAnsiEncoding'))
    pdfmetrics.registerFontFamily('LMRoman',normal='LMRoman',bold='LMRomanBold',italic='LMRomanItalic',boldItalic='LMRomanBoldItalic')
