from pypdf import PdfReader,PdfWriter
from pypdf.generic import NameObject,NumberObject,BooleanObject,DictionaryObject,ArrayObject,TextStringObject,DecodedStreamObject
from pathlib import Path
import re
b=Path('/Users/quickwhitt/Documents/Codex/2026-10-05/referenced-chatgpt-conversation-this-is-an/outputs/acos-compass-pdf-engineering-repo/reports/pfe602-pdf-fixture-lab-2026-10-06');r=PdfReader(str(b/'shaping-fixture-noemoji.pdf'));w=PdfWriter();w.clone_document_from_reader(r);root=w._root_object;page=w.pages[0]
root[NameObject('/Lang')]=TextStringObject('en-US');root[NameObject('/MarkInfo')]=DictionaryObject({NameObject('/Type'):NameObject('/MarkInfo'),NameObject('/Marked'):BooleanObject(True)});root[NameObject('/ViewerPreferences')]=w._add_object(DictionaryObject({NameObject('/DisplayDocTitle'):BooleanObject(True)}))
xmp=b'''<?xpacket begin="\xef\xbb\xbf" id="W5M0MpCehiHzreSzNTczkc9d"?><x:xmpmeta xmlns:x="adobe:ns:meta/"><rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"><rdf:Description xmlns:pdfuaid="http://www.aiim.org/pdfua/ns/id/" pdfuaid:part="2" pdfuaid:rev="2024"><dc:title xmlns:dc="http://purl.org/dc/elements/1.1/"><rdf:Alt><rdf:li xml:lang="x-default">PFE 602 corrected shaping fixture</rdf:li></rdf:Alt></dc:title></rdf:Description></rdf:RDF></x:xmpmeta><?xpacket end="w"?>''';m=DecodedStreamObject();m.set_data(xmp);m[NameObject('/Type')]=NameObject('/Metadata');m[NameObject('/Subtype')]=NameObject('/XML');root[NameObject('/Metadata')]=w._add_object(m)
raw=page['/Contents'].get_object().get_data();n=0
def repl(mt):
 global n
 body=mt.group(2);i=n;n+=1
 if i==0:return b'/Artifact BMC\nBT'+body+b'ET\nEMC'
 return b'/NonStruct <</MCID '+str(i-1).encode()+b'>> BDC\nBT'+body+b'ET\nEMC'
cs=DecodedStreamObject();cs.set_data(re.sub(rb'([^B]*)BT(.*?)ET',repl,raw,flags=re.S));page[NameObject('/Contents')]=w._add_object(cs);page[NameObject('/StructParents')]=NumberObject(0)
leaves=[];parents=[]
for i,role in enumerate(['/H1','/P','/P','/P']):
 leaf=w._add_object(DictionaryObject({NameObject('/Type'):NameObject('/StructElem'),NameObject('/S'):NameObject('/NonStruct'),NameObject('/Pg'):page.indirect_reference,NameObject('/K'):NumberObject(i)}));par=w._add_object(DictionaryObject({NameObject('/Type'):NameObject('/StructElem'),NameObject('/S'):NameObject(role),NameObject('/K'):leaf}));leaf.get_object()[NameObject('/P')]=par;leaves.append(leaf);parents.append(par)
group=w._add_object(DictionaryObject({NameObject('/Type'):NameObject('/StructElem'),NameObject('/S'):NameObject('/NonStruct'),NameObject('/K'):ArrayObject(parents)}));doc=w._add_object(DictionaryObject({NameObject('/Type'):NameObject('/StructElem'),NameObject('/S'):NameObject('/Document'),NameObject('/K'):group}));group.get_object()[NameObject('/P')]=doc
for par in parents:par.get_object()[NameObject('/P')]=group
ptarr=w._add_object(ArrayObject(leaves));pt=w._add_object(DictionaryObject({NameObject('/Type'):NameObject('/ParentTree'),NameObject('/Nums'):ArrayObject([NumberObject(0),ptarr])}));ns=w._add_object(DictionaryObject({NameObject('/Type'):NameObject('/Namespace'),NameObject('/NS'):TextStringObject('http://iso.org/pdf2/ssn')}));st=w._add_object(DictionaryObject({NameObject('/Type'):NameObject('/StructTreeRoot'),NameObject('/K'):doc,NameObject('/ParentTree'):pt,NameObject('/ParentTreeNextKey'):NumberObject(1),NameObject('/Namespaces'):ArrayObject([ns])}));root[NameObject('/StructTreeRoot')]=st;doc.get_object()[NameObject('/P')]=st;doc.get_object()[NameObject('/NS')]=ns
for key in ['/F3+0','/F4+0']:
 f=page['/Resources']['/Font'][NameObject(key)].get_object();a=ArrayObject(f['/Widths']);a[132-int(f['/FirstChar'])]=NumberObject(0);f[NameObject('/Widths')]=a
out=b/'shaping-fixture-noemoji-nested-tagged.pdf';w.write(str(out));print(out)
