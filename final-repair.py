"""Reproduce the bounded PDF/UA-2 machine-pass repair experiment.

This intentionally produces an experimental copy. It removes invalid outlines and
one stray table integer, and marks only the initial page-background paint as an
artifact. It is not a production repair recipe.
"""
from pathlib import Path
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, ArrayObject, NumberObject, DecodedStreamObject

src = Path("reports/pfe611-tagged-repair-2026-10-06/truetype-tagged-metadata-repaired.pdf")
out = Path("reports/pfe611-tagged-repair-2026-10-06/variant-combined-artifact-repair.pdf")
r = PdfReader(str(src)); w = PdfWriter(); w.clone_document_from_reader(r)
root = w._root_object
root.pop(NameObject('/Outlines'), None)
struct = root['/StructTreeRoot'].get_object()
found = 0

def walk(obj):
    global found
    if not hasattr(obj, 'get'):
        return
    if obj.get('/S') == '/Table':
        arr = obj.get('/K').get_object()
        obj[NameObject('/K')] = ArrayObject([x for x in arr if not isinstance(x, NumberObject)])
        found += 1
    kids = obj.get('/K')
    if isinstance(kids, list):
        for item in kids:
            walk(item.get_object() if hasattr(item, 'get_object') else item)
    elif hasattr(kids, 'get_object'):
        walk(kids.get_object())

walk(struct)
assert found == 1
page = w.pages[0]
data = page.get_contents().get_data()
marker = b'q\n3.125 0 0 3.125 0 0 cm\n.9686'
assert data.count(marker) == 1
data = data.replace(marker, b'/Artifact BMC\n' + marker, 1)
needle = b'0 0 1056 816 re\nf\nQ\nq\n0 0 3300 2550 re'
assert data.count(needle) == 1
data = data.replace(needle, b'0 0 1056 816 re\nf\nQ\nEMC\nq\n0 0 3300 2550 re', 1)
stream = DecodedStreamObject(); stream.set_data(data)
page[NameObject('/Contents')] = w._add_object(stream)
with out.open('wb') as handle:
    w.write(handle)
print(out)
