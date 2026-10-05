import sys
sys.path.insert(0,'/tmp/acos-pdf-tools-20261006')
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, NumberObject, ArrayObject, DictionaryObject, DecodedStreamObject, TextStringObject
src,dst=sys.argv[1:]
r=PdfReader(src); w=PdfWriter(clone_from=r)
for p in w.pages:
    mb=p.mediabox; box=ArrayObject([NumberObject(float(mb.left)),NumberObject(float(mb.bottom)),NumberObject(float(mb.right)),NumberObject(float(mb.top))]); p[NameObject('/TrimBox')]=box; p[NameObject('/ArtBox')]=ArrayObject(box)
# Preserve the source PDF/A output intent and reuse its embedded profile for a second implementation-facing PDF/X intent.
root=w.root_object; intents=root['/OutputIntents']; existing=intents[0].get_object(); profile=existing['/DestOutputProfile']
xi=DictionaryObject(); xi[NameObject('/Type')]=NameObject('/OutputIntent'); xi[NameObject('/S')]=NameObject('/GTS_PDFX'); xi[NameObject('/OutputConditionIdentifier')]=TextStringObject('sRGB IEC61966-2.1'); xi[NameObject('/Info')]=TextStringObject('sRGB IEC61966-2.1'); xi[NameObject('/DestOutputProfile')]=profile; intents.append(w._add_object(xi))
# Preserve PDF/UA and PDF/A identifiers and add PDF/X identification plus title.
xmp='''<?xpacket begin="﻿" id="W5M0MpCehiHzreSzNTczkc9d"?>\n<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="ACOS dual-profile probe">\n<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"><rdf:Description xmlns:pdfuaid="http://www.aiim.org/pdfua/ns/id/" pdfuaid:part="2" pdfuaid:rev="2024" xmlns:pdfaid="http://www.aiim.org/pdfa/ns/id/" pdfaid:part="4" pdfaid:rev="2020" xmlns:pdfxid="http://www.npes.org/pdfx/ns/id/"><pdfxid:GTS_PDFXVersion>PDF/X-6</pdfxid:GTS_PDFXVersion><pdfxid:GTS_PDFXConformance>PDF/X-6</pdfxid:GTS_PDFXConformance><dc:title xmlns:dc="http://purl.org/dc/elements/1.1/"><rdf:Alt><rdf:li xml:lang="x-default">ACOS dual-profile PDF/A-4 PDF/UA-2 PDF/X-6 probe</rdf:li></rdf:Alt></dc:title></rdf:Description></rdf:RDF></x:xmpmeta>\n<?xpacket end="w"?>'''.encode()
x=DecodedStreamObject(); x.set_data(xmp); x[NameObject('/Type')]=NameObject('/Metadata'); x[NameObject('/Subtype')]=NameObject('/XML'); root[NameObject('/Metadata')]=w._add_object(x)
w.add_metadata({'/GTS_PDFXVersion':'PDF/X-6','/GTS_PDFXConformance':'PDF/X-6'})
with open(dst,'wb') as f:w.write(f)
