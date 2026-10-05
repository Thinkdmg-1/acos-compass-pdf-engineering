import json,hashlib
from pathlib import Path
b=Path(__file__).parent
checks={}
for name,file,rules,checks_expected in [('ua2_1_30_2','shaped-semantic-ua2.json',1727,805),('ua2_1_28_2','shaped-semantic-verapdf1282-ua2.json',1723,815)]:
 x=json.loads((b/file).read_text());v=x['report']['jobs'][0]['validationResult'][0];d=v['details'];checks[name+'_zero_failed_rules']=d['failedRules']==0;checks[name+'_zero_failed_checks']=d['failedChecks']==0;checks[name+'_expected_rules']=d['passedRules']==rules;checks[name+'_expected_checks']=d['passedChecks']==checks_expected
p=json.loads((b/'shaped-semantic-preservation-check.json').read_text());checks.update({'semantic_text_preserved':p['comparisons']['semantic_text_preserved'],'semantic_geometry_preserved':p['comparisons']['semantic_geometry_preserved'],'outline_raster_equal':p['comparisons']['outline_raster_equal'],'outline_has_no_text':p['comparisons']['outline_has_no_text'],'combined_hash_matches':hashlib.sha256((b/'shaping-fixture-heldout-shaped-semantic-tagged.pdf').read_bytes()).hexdigest()==p['combined']['sha256']})
print(json.dumps({'checks':checks,'all_pass':all(checks.values()),'interpretation':'HarfBuzz-shaped visible outline artifact plus invisible tagged semantic text passes both pinned PDF/UA-2 validators; visual and semantic layers are independently preserved, but this remains a diagnostic export path.'},indent=2));assert all(checks.values())
