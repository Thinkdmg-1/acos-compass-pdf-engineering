from pathlib import Path
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, TextStringObject, DecodedStreamObject, DictionaryObject, ArrayObject, ByteStringObject
src=Path('../variant-combined-artifact-repair.pdf')
# Run from the experiment directory or resolve against this script.
if not src.exists(): src=Path('reports/pfe611-tagged-repair-2026-10-06/variant-combined-artifact-repair.pdf')
base=Path('/Users/quickwhitt/Documents/Codex/2026-10-05/referenced-chatgpt-conversation-this-is-an/outputs/acos-compass-pdf-engineering-repo')
fixture=PdfReader(str(base/'reports/production-pdfa4-2026-10-05/fixture-repaired2.pdf'))
r=PdfReader(str(base/'reports/pfe611-tagged-repair-2026-10-06/variant-combined-artifact-repair.pdf')); w=PdfWriter(); w.clone_document_from_reader(r)
w._header=b'%PDF-2.0'
root=w._root_object; root[NameObject('/Version')]=NameObject('/2.0')
# PDF/A-4 forbids an Info dictionary unless PieceInfo is present; omit it.
w._info=None
w._ID=ArrayObject([ByteStringObject(b'ACOS-PFE-20261006'),ByteStringObject(b'ACOS-PFE-20261006')])
# Copy the repaired fixture's ICC output profile bytes and PDF/A output intent semantics.
oi=fixture.trailer['/Root']['/OutputIntents'][0].get_object(); icc=oi['/DestOutputProfile'].get_object(); profile=DecodedStreamObject(); profile.set_data(icc.get_data()); profile[NameObject('/N')]=icc['/N']; profile_ref=w._add_object(profile)
new_oi=DictionaryObject({NameObject('/Type'):NameObject('/OutputIntent'),NameObject('/S'):oi['/S'],NameObject('/OutputConditionIdentifier'):oi['/OutputConditionIdentifier'],NameObject('/Info'):oi['/Info'],NameObject('/DestOutputProfile'):profile_ref}); root[NameObject('/OutputIntents')]=ArrayObject([w._add_object(new_oi)])
# Add PDF/A-4 identification alongside PDF/UA identification.
xmp=b'''<?xpacket begin="\xef\xbb\xbf" id="W5M0MpCehiHzreSzNTczkc9d"?>\n<x:xmpmeta xmlns:x="adobe:ns:meta/">\n<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"><rdf:Description xmlns:pdfuaid="http://www.aiim.org/pdfua/ns/id/" pdfuaid:part="2" pdfuaid:rev="2024" xmlns:pdfaid="http://www.aiim.org/pdfa/ns/id/" pdfaid:part="4" pdfaid:rev="2020"><dc:title xmlns:dc="http://purl.org/dc/elements/1.1/"><rdf:Alt><rdf:li xml:lang="x-default">PDF engineering specimen</rdf:li></rdf:Alt></dc:title></rdf:Description></rdf:RDF></x:xmpmeta>\n<?xpacket end="w"?>'''
meta=DecodedStreamObject();meta.set_data(xmp);meta[NameObject('/Type')]=NameObject('/Metadata');meta[NameObject('/Subtype')]=NameObject('/XML');root[NameObject('/Metadata')]=w._add_object(meta)
out=Path('reports/pfe611-tagged-repair-2026-10-06/pdfa4-ua2-experiment/combined-pdfa4-ua2.pdf');
with out.open('wb') as f:w.write(f)
print(out)
