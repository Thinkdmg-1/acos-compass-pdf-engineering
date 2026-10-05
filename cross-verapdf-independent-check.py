import json
from pathlib import Path
b=Path(__file__).parent
cases={'primary_1_30_2':('noemoji-nested-ua2.json',1727,470),'heldout_1_28_2':('heldout-verapdf1282-ua2.json',1723,667),'primary_1_28_2':('noemoji-verapdf1282-ua2.json',1723,478)}
checks={}; details={}
for name,(file,expected_rules,expected_checks) in cases.items():
 x=json.loads((b/file).read_text());v=x['report']['jobs'][0]['validationResult'][0];d=v['details'];details[name]={'file':file,'profile':v['profileName'],'passedRules':d['passedRules'],'failedRules':d['failedRules'],'passedChecks':d['passedChecks'],'failedChecks':d['failedChecks']};checks[name+'_zero_failed_rules']=d['failedRules']==0;checks[name+'_zero_failed_checks']=d['failedChecks']==0;checks[name+'_expected_passed_rules']=d['passedRules']==expected_rules;checks[name+'_expected_passed_checks']=d['passedChecks']==expected_checks
print(json.dumps({'checks':checks,'details':details,'all_pass':all(checks.values()),'interpretation':'Two pinned veraPDF releases independently report zero PDF/UA-2 failed rules and checks for both the corrected specimen and the held-out case. This corroborates machine validation only.'},indent=2));assert all(checks.values())
