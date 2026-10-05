import json,hashlib
from pathlib import Path
base=Path(__file__).parent; d=json.loads((base/'tounicode-inspection.json').read_text())
checks={'pdf_hash_matches':d['pdf_sha256']==hashlib.sha256((base/'shaping-fixture.pdf').read_bytes()).hexdigest(),'three_true_type_maps':sum(v['has_tounicode'] for v in d['fonts'].values())==3,'all_maps_have_cmap':all(v.get('begincmap')==1 for v in d['fonts'].values() if v['has_tounicode']),'font_without_map_recorded':d['fonts']['/F1']['has_tounicode'] is False,'map_streams_distinct':len({v['stream_sha256'] for v in d['fonts'].values() if v['has_tounicode']})==3}
out={'checks':checks,'all_pass':all(checks.values())}; (base/'tounicode-independent-check.json').write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
if not out['all_pass']: raise SystemExit(1)
