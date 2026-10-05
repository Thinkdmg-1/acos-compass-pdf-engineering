from pypdf import PdfReader,PdfWriter
from pypdf.generic import NameObject,ArrayObject,DecodedStreamObject
from pathlib import Path
b=Path('/Users/quickwhitt/Documents/Codex/2026-10-05/referenced-chatgpt-conversation-this-is-an/outputs/acos-compass-pdf-engineering-repo/reports/pfe602-pdf-fixture-lab-2026-10-06')
base=PdfReader(str(b/'shaping-fixture-heldout-nested-widthpatched-tagged.pdf')); outline=PdfReader(str(b/'shaping-fixture-heldout-shaped-outline.pdf'));w=PdfWriter();w.clone_document_from_reader(base);page=w.pages[0]
hidden=page['/Contents'].get_object().get_data().replace(b'BT',b'BT 3 Tr')
hs=DecodedStreamObject();hs.set_data(hidden);href=w._add_object(hs)
vis=outline.pages[0]['/Contents'].get_object().get_data();vs=DecodedStreamObject();vs.set_data(b'/Artifact BMC\n'+vis+b'\nEMC\n');vref=w._add_object(vs)
page[NameObject('/Contents')]=ArrayObject([href,vref]);out=b/'shaping-fixture-heldout-shaped-semantic-tagged.pdf';w.write(str(out));print(out)
