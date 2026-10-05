from pathlib import Path
import re
from pypdf import PdfReader,PdfWriter
from pypdf.generic import NameObject, NumberObject, BooleanObject, DictionaryObject, ArrayObject, TextStringObject, DecodedStreamObject
base=Path('/Users/quickwhitt/Documents/Codex/2026-10-05/referenced-chatgpt-conversation-this-is-an/outputs/acos-compass-pdf-engineering-repo')
src=base/'reports/pfe602-pdf-fixture-lab-2026-10-06/shaping-fixture.pdf'; out=base/'reports/pfe602-pdf-fixture-lab-2026-10-06/shaping-fixture-tagged-repaired.pdf'
r=PdfReader(str(src)); w=PdfWriter(); w.clone_document_from_reader(r); root=w._root_object; page=w.pages[0]
root[NameObject('/Lang')]=TextStringObject('en-US'); root[NameObject('/MarkInfo')]=DictionaryObject({NameObject('/Type'):NameObject('/MarkInfo'),NameObject('/Marked'):BooleanObject(True)})
vp=DictionaryObject({NameObject('/DisplayDocTitle'):BooleanObject(True)}); root[NameObject('/ViewerPreferences')]=w._add_object(vp)
xmp=b'''<?xpacket begin="\xef\xbb\xbf" id="W5M0MpCehiHzreSzNTczkc9d"?>\n<x:xmpmeta xmlns:x="adobe:ns:meta/">\n<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"><rdf:Description xmlns:pdfuaid="http://www.aiim.org/pdfua/ns/id/" pdfuaid:part="2" pdfuaid:rev="2024"><dc:title xmlns:dc="http://purl.org/dc/elements/1.1/"><rdf:Alt><rdf:li xml:lang="x-default">PFE 602 shaping fixture</rdf:li></rdf:Alt></dc:title></rdf:Description></rdf:RDF></x:xmpmeta>\n<?xpacket end="w"?>'''
meta=DecodedStreamObject(); meta.set_data(xmp); meta[NameObject('/Type')]=NameObject('/Metadata'); meta[NameObject('/Subtype')]=NameObject('/XML'); root[NameObject('/Metadata')]=w._add_object(meta)
stream=page['/Contents'].get_object().get_data(); n=0
def repl(m):
 global n
 body=m.group(2); i=n; n+=1
 if i==0: return b'/Artifact BMC\nBT'+body+b'ET\nEMC'
 return b'/P <</MCID '+str(i-1).encode()+b'>> BDC\nBT'+body+b'ET\nEMC'
wrapped=re.sub(rb'([^B]*)BT(.*?)ET',repl,stream,flags=re.S); cs=DecodedStreamObject(); cs.set_data(wrapped); page[NameObject('/Contents')]=w._add_object(cs); page[NameObject('/StructParents')]=NumberObject(0)
# 5 paragraph MCIDs 0..4
els=[]
for i in range(5): els.append(w._add_object(DictionaryObject({NameObject('/Type'):NameObject('/StructElem'),NameObject('/S'):NameObject('/P'),NameObject('/Pg'):page.indirect_reference,NameObject('/K'):NumberObject(i),NameObject('/T'):TextStringObject('Paragraph '+str(i+1))})))
doc=w._add_object(DictionaryObject({NameObject('/Type'):NameObject('/StructElem'),NameObject('/S'):NameObject('/Document'),NameObject('/K'):ArrayObject(els)}))
for ref in els: ref.get_object()[NameObject('/P')]=doc
parent=ArrayObject(els); pt=w._add_object(DictionaryObject({NameObject('/Nums'):ArrayObject([NumberObject(0),parent])}))
ns=w._add_object(DictionaryObject({NameObject('/Type'):NameObject('/Namespace'),NameObject('/NS'):TextStringObject('http://iso.org/pdf2/ssn')}))
struct=w._add_object(DictionaryObject({NameObject('/Type'):NameObject('/StructTreeRoot'),NameObject('/K'):doc,NameObject('/ParentTree'):pt,NameObject('/ParentTreeNextKey'):NumberObject(1),NameObject('/Namespaces'):ArrayObject([ns])})); root[NameObject('/StructTreeRoot')]=struct; doc.get_object()[NameObject('/NS')]=ns
with out.open('wb') as f:w.write(f)
print(out,'mcids',5)
