import json, hashlib
from pathlib import Path
b=Path(__file__).parent
d=json.loads((b/'structure-linkage-experiments.json').read_text())
checks={}
for v in d['variants']:
 p=b/v['file']; checks[v['name']+'_exists']=p.exists()
 if p.exists(): checks[v['name']+'_hash']=hashlib.sha256(p.read_bytes()).hexdigest()==v['sha256']
 checks[v['name']+'_residual_state']=v['failed_rules']==2 and v['failed_checks']==6 and v['failed_clauses']==['8.2.2','8.4.5.8']
print(json.dumps({'checks':checks,'all_pass':all(checks.values()),'interpretation':d['interpretation']},indent=2))
if not all(checks.values()): raise SystemExit(1)
