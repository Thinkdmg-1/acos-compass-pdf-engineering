import json, hashlib
from pathlib import Path
b=Path(__file__).parent
raw=json.loads((b/'noemoji-widthpatched-parenttype-ua2.json').read_text()); v=raw['report']['jobs'][0]['validationResult'][0]; d=v['details']; p=json.loads((b/'noemoji-preservation-check.json').read_text())
checks={
 'ua2_failed_rules_exactly_1': d['failedRules']==1,
 'ua2_failed_checks_exactly_4': d['failedChecks']==4,
 'remaining_clause_only_8_2_2': [x['clause'] for x in d['ruleSummaries'] if x['ruleStatus']=='FAILED']==['8.2.2'],
 'page_count_preserved': p['comparisons']['pages'] is True,
 'geometry_preserved': p['comparisons']['mediabox'] is True,
 'text_hash_preserved': p['comparisons']['text_sha256'] is True,
 'raster_hash_preserved': p['comparisons']['raster_sha256'] is True,
 'artifact_hash_matches_receipt': hashlib.sha256((b/'shaping-fixture-noemoji-widthpatched-parenttype-tagged.pdf').read_bytes()).hexdigest()==p['tagged']['sha256'],
}
print(json.dumps({'checks':checks,'all_pass':all(checks.values()),'interpretation':'Controlled source-corrected fixture removes the invalid zero-valued ToUnicode mapping and width inconsistency; structure linkage remains unresolved.'},indent=2))
if not all(checks.values()): raise SystemExit(1)
