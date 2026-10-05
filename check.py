from __future__ import annotations
import hashlib, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = ROOT / 'reports/verapdf-runtime-rerun-2026-10-06'
fixtures = {
    'production-repaired': ROOT / 'reports/production-pdfa4-2026-10-05/fixture-repaired2.pdf',
    'truetype-tagged': pathlib.Path('/Users/quickwhitt/Documents/Codex/2026-10-05/referenced-chatgpt-conversation-this-is-an/outputs/pdf-engineering/truetype-tagged.pdf'),
}
expected = {
    'production-repaired-4.json': (True, 109, 0, 375, 0),
    'production-repaired-ua2.json': (False, 1721, 6, 310, 8),
    'truetype-tagged-4.json': (False, 103, 6, 1362, 276),
    'truetype-tagged-ua2.json': (False, 1722, 5, 2532, 7),
}
summary = []
for name, (compliant, pr, fr, pc, fc) in expected.items():
    doc = json.loads((R / name).read_text())
    v = doc['report']['jobs'][0]['validationResult'][0]
    d = v['details']
    observed = (v['compliant'], d['passedRules'], d['failedRules'], d['passedChecks'], d['failedChecks'])
    assert observed == (compliant, pr, fr, pc, fc), (name, observed)
    summary.append({'report': name, 'profile': v['profileName'], 'observed': observed})
for key, path in fixtures.items():
    assert path.exists(), path
summary.append({'fixture_sha256': {key: hashlib.sha256(path.read_bytes()).hexdigest() for key, path in fixtures.items()}})
profiles = (R / 'profile-list.txt').read_text()
assert '4 - PDF/A-4 validation profile' in profiles
assert 'ua2 - PDF/UA-2 + Tagged PDF validation profile' in profiles
assert 'PDF/X-6' not in profiles
summary.append({'profile_inventory_assertions': {'pdfa4_present': True, 'pdfua2_present': True, 'pdfx6_absent': True}})
print(json.dumps({'independent_check': 'PASS', 'summary': summary}, indent=2, sort_keys=True))
