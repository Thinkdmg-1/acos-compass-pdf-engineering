import sys, os
sys.path.insert(0,'/tmp/acos-pdf-tools-20261006')
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, NumberObject, ArrayObject, DictionaryObject, DecodedStreamObject, TextStringObject
src,dst,icc=sys.argv[1:]
r=PdfReader(src); w=PdfWriter()
for p in r.pages:
    mb=p.mediabox
    p[NameObject('/TrimBox')]=ArrayObject([NumberObject(float(mb.left)),NumberObject(float(mb.bottom)),NumberObject(float(mb.right)),NumberObject(float(mb.top))])
    p[NameObject('/ArtBox')]=p['/TrimBox']
    w.add_page(p)
# Copy document info, then add implementation-facing PDF/X identification.
info=dict(r.metadata or {})
info['/GTS_PDFXVersion']='PDF/X-6'
info['/GTS_PDFXConformance']='PDF/X-6'
w.add_metadata(info)
# Minimal XMP packet with PDF/X identification. This is deliberately an implementation test, not a standards assertion.
xmp='''<?xpacket begin="﻿" id="W5M0MpCehiHzreSzNTczkc9d"?>\n<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="ACOS disposable probe">\n<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"><rdf:Description xmlns:pdfxid="http://www.npes.org/pdfx/ns/id/" ><pdfxid:GTS_PDFXVersion>PDF/X-6</pdfxid:GTS_PDFXVersion><pdfxid:GTS_PDFXConformance>PDF/X-6</pdfxid:GTS_PDFXConformance></rdf:Description><rdf:Description /></rdf:RDF></x:xmpmeta>\n<?xpacket end="w"?>'''.encode('utf-8')
x=DecodedStreamObject(); x.set_data(xmp); x[NameObject('/Type')]=NameObject('/Metadata'); x[NameObject('/Subtype')]=NameObject('/XML'); xref=w._add_object(x)
w._root_object[NameObject('/Metadata')]=xref
# Embed an RGB ICC profile as an output intent.
with open(icc,'rb') as f: data=f.read()
prof=DecodedStreamObject(); prof.set_data(data); prof[NameObject('/N')]=NumberObject(3); profref=w._add_object(prof)
oi=DictionaryObject(); oi[NameObject('/Type')]=NameObject('/OutputIntent'); oi[NameObject('/S')]=NameObject('/GTS_PDFX'); oi[NameObject('/OutputConditionIdentifier')]=TextStringObject('sRGB IEC61966-2.1'); oi[NameObject('/Info')]=TextStringObject('sRGB IEC61966-2.1'); oi[NameObject('/DestOutputProfile')]=profref
w._root_object[NameObject('/OutputIntents')]=ArrayObject([w._add_object(oi)])
with open(dst,'wb') as f: w.write(f)
