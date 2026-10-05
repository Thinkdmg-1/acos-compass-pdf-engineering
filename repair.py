from pathlib import Path
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, TextStringObject, DecodedStreamObject, DictionaryObject, BooleanObject, ArrayObject
src=Path('/Users/quickwhitt/Documents/Codex/2026-10-05/referenced-chatgpt-conversation-this-is-an/outputs/pdf-engineering/truetype-tagged.pdf')
out=Path('reports/pfe611-tagged-repair-2026-10-06/truetype-tagged-metadata-repaired.pdf')
r=PdfReader(str(src)); w=PdfWriter(); w.clone_document_from_reader(r)
root=w._root_object
root[NameObject('/Lang')]=TextStringObject('en')
root[NameObject('/MarkInfo')]=DictionaryObject({NameObject('/Type'):NameObject('/MarkInfo'),NameObject('/Marked'):BooleanObject(True)})
vp=root.get('/ViewerPreferences')
if vp is None: vp=DictionaryObject(); root[NameObject('/ViewerPreferences')]=vp
vp[NameObject('/DisplayDocTitle')]=BooleanObject(True)
struct=root.get('/StructTreeRoot')
if struct:
    struct_obj=struct.get_object()
    ns=DictionaryObject({NameObject('/Type'):NameObject('/Namespace'),NameObject('/NS'):TextStringObject('http://iso.org/pdf2/ssn')})
    ns_ref=w._add_object(ns)
    struct_obj[NameObject('/Namespaces')]=ArrayObject([ns_ref])
    doc=struct_obj.get('/K')
    if doc:
        doc=doc.get_object()
        doc[NameObject('/NS')]=ns_ref
xmp=b'''<?xpacket begin="\xef\xbb\xbf" id="W5M0MpCehiHzreSzNTczkc9d"?>\n<x:xmpmeta xmlns:x="adobe:ns:meta/">\n<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"><rdf:Description xmlns:pdfuaid="http://www.aiim.org/pdfua/ns/id/" pdfuaid:part="2" pdfuaid:rev="2024"><dc:title xmlns:dc="http://purl.org/dc/elements/1.1/"><rdf:Alt><rdf:li xml:lang="x-default">PDF engineering specimen</rdf:li></rdf:Alt></dc:title></rdf:Description></rdf:RDF></x:xmpmeta>\n<?xpacket end="w"?>'''
meta=DecodedStreamObject(); meta.set_data(xmp); meta[NameObject('/Type')]=NameObject('/Metadata'); meta[NameObject('/Subtype')]=NameObject('/XML'); root[NameObject('/Metadata')]=w._add_object(meta)
with out.open('wb') as f: w.write(f)
print(out)
