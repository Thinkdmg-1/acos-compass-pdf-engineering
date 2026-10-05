import sys
sys.path.insert(0,'/tmp/acos-pdf-tools-20261006')
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, NumberObject, ArrayObject, DictionaryObject, DecodedStreamObject, TextStringObject
src,dst,icc=sys.argv[1:]
r=PdfReader(src); w=PdfWriter(clone_from=r)
# Modify every existing page without rebuilding the page tree.
for p in w.pages:
    mb=p.mediabox
    p[NameObject('/TrimBox')]=ArrayObject([NumberObject(float(mb.left)),NumberObject(float(mb.bottom)),NumberObject(float(mb.right)),NumberObject(float(mb.top))])
    p[NameObject('/ArtBox')]=ArrayObject([NumberObject(float(mb.left)),NumberObject(float(mb.bottom)),NumberObject(float(mb.right)),NumberObject(float(mb.top))])
info=dict(r.metadata or {}); info['/GTS_PDFXVersion']='PDF/X-6'; info['/GTS_PDFXConformance']='PDF/X-6'; w.add_metadata(info)
xmp='''<?xpacket begin="﻿" id="W5M0MpCehiHzreSzNTczkc9d"?>\n<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="ACOS disposable preserving probe">\n<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"><rdf:Description xmlns:pdfxid="http://www.npes.org/pdfx/ns/id/" xmlns:pdfuaid="http://www.aiim.org/pdfua/ns/id/" pdfuaid:part="2" pdfuaid:rev="2024"><pdfxid:GTS_PDFXVersion>PDF/X-6</pdfxid:GTS_PDFXVersion><pdfxid:GTS_PDFXConformance>PDF/X-6</pdfxid:GTS_PDFXConformance><dc:title xmlns:dc="http://purl.org/dc/elements/1.1/"><rdf:Alt><rdf:li xml:lang="x-default">ACOS PDF/X-6 probe</rdf:li></rdf:Alt></dc:title></rdf:Description></rdf:RDF></x:xmpmeta>\n<?xpacket end="w"?>'''.encode('utf-8')
x=DecodedStreamObject(); x.set_data(xmp); x[NameObject('/Type')]=NameObject('/Metadata'); x[NameObject('/Subtype')]=NameObject('/XML'); w.root_object[NameObject('/Metadata')]=w._add_object(x)
with open(icc,'rb') as f: data=f.read()
prof=DecodedStreamObject(); prof.set_data(data); prof[NameObject('/N')]=NumberObject(3); profref=w._add_object(prof)
oi=DictionaryObject(); oi[NameObject('/Type')]=NameObject('/OutputIntent'); oi[NameObject('/S')]=NameObject('/GTS_PDFX'); oi[NameObject('/OutputConditionIdentifier')]=TextStringObject('sRGB IEC61966-2.1'); oi[NameObject('/Info')]=TextStringObject('sRGB IEC61966-2.1'); oi[NameObject('/DestOutputProfile')]=profref
w.root_object[NameObject('/OutputIntents')]=ArrayObject([w._add_object(oi)])
with open(dst,'wb') as f:w.write(f)
