from pathlib import Path
from fontTools.ttLib import TTCollection
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter
work=Path('/tmp/acos-pdf-fixture-lab-20261006');work.mkdir(exist_ok=True)
for src,out,idx in [('/System/Library/Fonts/NotoSerifMyanmar.ttc',work/'NotoSerifMyanmar.ttf',0),('/System/Library/Fonts/NotoSansOriya.ttc',work/'NotoSansOriya.ttf',0)]:TTCollection(src).fonts[idx].save(out)
pdfmetrics.registerFont(TTFont('ArialUnicode','/Library/Fonts/Arial Unicode.ttf'));pdfmetrics.registerFont(TTFont('Myanmar',str(work/'NotoSerifMyanmar.ttf')));pdfmetrics.registerFont(TTFont('Oriya',str(work/'NotoSansOriya.ttf')))
out=Path('/Users/quickwhitt/Documents/Codex/2026-10-05/referenced-chatgpt-conversation-this-is-an/outputs/acos-compass-pdf-engineering-repo/reports/pfe602-pdf-fixture-lab-2026-10-06/shaping-fixture-heldout.pdf');c=canvas.Canvas(str(out),pagesize=letter);c.setTitle('PFE 602 held-out shaping case');y=740
for font,text in [('ArialUnicode','PFE 602 held-out case'),('ArialUnicode','A\u030a / אבגדה'),('Myanmar','မြန်မာ စမ်းသပ်'),('Oriya','ଓଡ଼ିଆ ପରୀକ୍ଷା'),('ArialUnicode','Plain fallback text')]:c.setFont(font,20);c.drawString(72,y,text);y-=48
c.save();print(out)
