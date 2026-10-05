from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.pens.reportLabPen import ReportLabPen
from reportlab.graphics.shapes import Path as RLPath, Drawing
from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import uharfbuzz as hb
from reportlab.pdfbase import pdfmetrics
base=Path('/Users/quickwhitt/Documents/Codex/2026-10-05/referenced-chatgpt-conversation-this-is-an/outputs/acos-compass-pdf-engineering-repo/reports/pfe602-pdf-fixture-lab-2026-10-06');work=Path('/tmp/acos-pdf-fixture-lab-20261006')
fonts={'ArialUnicode':Path('/Library/Fonts/Arial Unicode.ttf'),'Myanmar':work/'NotoSerifMyanmar.ttf','Oriya':work/'NotoSansOriya.ttf'}
objs={}
for name,path in fonts.items():
 data=path.read_bytes();tt=TTFont(str(path));tt.flavor=None;glyphset=tt.getGlyphSet();order=tt.getGlyphOrder();upem=tt['head'].unitsPerEm;face=hb.Face(data);font=hb.Font(face);font.scale=(upem,upem);objs[name]=(tt,glyphset,order,upem,font)
def draw_shaped(c,name,text,x,y,size):
 tt,glyphset,order,upem,hfont=objs[name];buf=hb.Buffer();buf.add_str(text);buf.guess_segment_properties();hb.shape(hfont,buf,{});infos=buf.glyph_infos;poss=buf.glyph_positions;penx=0
 for info,pos in zip(infos,poss):
  gid=info.codepoint
  if gid>=len(order):continue
  path=RLPath();ReportLabPen(glyphset,path).moveTo((0,0)) if False else None
  glyphset[order[gid]].draw(ReportLabPen(glyphset,path))
  d=Drawing(1000,1000);d.add(path);c.saveState();c.translate(x+penx+pos.x_offset*size/upem,y+pos.y_offset*size/upem);c.scale(size/upem,size/upem);renderPDF.draw(d,c,0,0);c.restoreState();penx += pos.x_advance*size/upem
 return penx
out=base/'shaping-fixture-heldout-shaped-outline.pdf';c=canvas.Canvas(str(out),pagesize=letter);c.setTitle('PFE 602 held-out shaped outline visual control');y=740
for name,text in [('ArialUnicode','PFE 602 shaped outline'),('ArialUnicode','A\u030a / אבגדה'),('Myanmar','မြန်မာ စမ်းသပ်'),('Oriya','ଓଡ଼ିଆ ପରୀକ୍ଷା'),('ArialUnicode','Plain fallback text')]:draw_shaped(c,name,text,72,y,20);y-=48
c.save();print(out)
