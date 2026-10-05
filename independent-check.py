import json,hashlib,subprocess
from pathlib import Path
base=Path(__file__).parent; r=json.loads((base/'results.json').read_text()); checks={}
checks['fixture_hash']=hashlib.sha256((base/'shaping-fixture.pdf').read_bytes()).hexdigest()==r['fixture_sha256']
checks['single_page']=r['pages']==1
checks['two_extractors_disagree']=r['pypdf_text_sha256']!=r['poppler_text_sha256']
checks['pypdf_reveals_missing_glyphs']='\u0000' in r['pypdf_text']
checks['poppler_preserves_combining_sequence']='e\u0301' in r['poppler_text']
checks['poppler_reports_rtl_marks']='םולש' in r['poppler_text']
checks['fixture_untagged']=r['tagged'] is False and '/StructTreeRoot' not in r['catalog']
out={'checks':checks,'all_pass':all(checks.values())}
(base/'independent-check.json').write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
if not out['all_pass']: raise SystemExit(1)
