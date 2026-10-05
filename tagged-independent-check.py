import json, hashlib
from pathlib import Path
base=Path(__file__).parent
raw=json.loads((base/'tagged-repaired-ua2.json').read_text())
vr=raw['report']['jobs'][0]['validationResult'][0]
ua=vr['details']
pres=json.loads((base/'tagged-preservation-check.json').read_text())
checks={
 'ua2_failed_rules_exactly_2': ua['failedRules']==2,
 'ua2_failed_checks_exactly_6': ua['failedChecks']==6,
 'remaining_clauses_exact': sorted({x['clause'] for x in vr['details']['ruleSummaries']}) == ['8.2.2','8.4.5.8'],
 'page_count_preserved': pres['comparisons']['page_count_equal'] is True,
 'geometry_preserved': pres['comparisons']['geometry_equal'] is True,
 'text_hash_preserved': pres['comparisons']['text_hash_equal'] is True,
 'raster_hash_preserved': pres['comparisons']['raster_hash_equal'] is True,
 'artifact_hash_matches_receipt': hashlib.sha256((base/'shaping-fixture-tagged-repaired.pdf').read_bytes()).hexdigest()==pres['tagged_repaired']['sha256'],
}
print(json.dumps({'checks':checks,'all_pass':all(checks.values()),'interpretation':'Expected bounded repair state: exact remaining validator failures are preserved; preservation checks pass.'},indent=2))
if not all(checks.values()): raise SystemExit(1)
