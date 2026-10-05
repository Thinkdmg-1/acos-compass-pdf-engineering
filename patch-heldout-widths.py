from pypdf import PdfReader,PdfWriter
from pypdf.generic import NameObject,NumberObject,ArrayObject
from pathlib import Path
b=Path('/Users/quickwhitt/Documents/Codex/2026-10-05/referenced-chatgpt-conversation-this-is-an/outputs/acos-compass-pdf-engineering-repo/reports/pfe602-pdf-fixture-lab-2026-10-06');r=PdfReader(str(b/'shaping-fixture-heldout-nested-tagged.pdf'));w=PdfWriter();w.clone_document_from_reader(r);page=w.pages[0]
# Values are measured from the fresh veraPDF width diagnostics for this held-out subset.
patch={'/F2+0':{132:512.20703125},'/F3+0':{132:401},'/F4+0':{132:820.80078125,139:660.15625}}
for key,vals in patch.items():
 f=page['/Resources']['/Font'][NameObject(key)].get_object();a=ArrayObject(f['/Widths']);first=int(f['/FirstChar'])
 for code,width in vals.items():a[code-first]=NumberObject(width)
 f[NameObject('/Widths')]=a
out=b/'shaping-fixture-heldout-nested-widthpatched-tagged.pdf';w.write(str(out));print(out)
