import json,hashlib
from pathlib import Path
b=Path(__file__).parent;d=json.loads((b/'namespace-linkage-experiments.json').read_text()); checks={}
for v in d['variants']:
 p=b/v['file'];checks[v['name']+'_exists']=p.exists();checks[v['name']+'_hash']=p.exists() and hashlib.sha256(p.read_bytes()).hexdigest()==v['sha256'];checks[v['name']+'_reported_state']=v['failed_rules']>0 and v['failed_checks']>0 and bool(v['failed_clauses'])
print(json.dumps({'checks':checks,'all_pass':all(checks.values()),'interpretation':d['interpretation']},indent=2));assert all(checks.values())
