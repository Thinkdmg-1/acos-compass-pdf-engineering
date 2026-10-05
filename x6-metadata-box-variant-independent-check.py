from pathlib import Path
import json,hashlib,sys
sys.path.insert(0,'/tmp/acos-pdf-tools-20261006')
from pypdf import PdfReader
b=Path(__file__).parent
src=b/'../pfe602-pdf-fixture-lab-2026-10-06/shaping-fixture-heldout-shaped-semantic-tagged.pdf'; var=b/'x6-metadata-box-variant-v2.pdf'
def inspect(p):
 r=PdfReader(str(p)); page=r.pages[0]
 return {'file':p.name,'pages':len(r.pages),'text_sha256':hashlib.sha256((r.pages[0].extract_text() or '').encode()).hexdigest(),'has_struct_root':'/StructTreeRoot' in r.trailer['/Root'],'has_metadata':'/Metadata' in r.trailer['/Root'],'has_output_intents':'/OutputIntents' in r.trailer['/Root'],'trim_box':list(map(float,page.trimbox)) if '/TrimBox' in page else None,'art_box':list(map(float,page.artbox)) if '/ArtBox' in page else None,'info':{str(k):str(v) for k,v in (r.metadata or {}).items() if 'PDFX' in str(k)}}
s=inspect(src); v=inspect(var)
checks={'page_count_preserved':s['pages']==v['pages'],'text_hash_preserved':s['text_sha256']==v['text_sha256'],'x6_catalog_keys_present':v['has_metadata'] and v['has_output_intents'] and v['trim_box'] is not None,'semantic_structure_preserved':s['has_struct_root']==v['has_struct_root']}
result={'source':s,'variant':v,'checks':checks,'all_expected_checks_pass':all(checks.values()),'interpretation':'Metadata, output-intent and page-box injection reached the Rust X6 implementation path and preserved page count/text extraction, but the pypdf rewrite dropped StructTreeRoot. veraPDF therefore reports PDF/UA-2 and PDF/A-4 failures. This is a controlled negative result, not a conformance claim.'}
(b/'x6-metadata-box-variant-independent-check.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
# Deliberate negative control: the expected-state report must show the structure-loss defect.
assert all(checks[k] for k in ['page_count_preserved','text_hash_preserved','x6_catalog_keys_present'])
assert checks['semantic_structure_preserved'] is False
