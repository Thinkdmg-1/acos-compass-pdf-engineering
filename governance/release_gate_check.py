"""Fail-closed release-state check for the ACOS PDF-engineering repository."""
import json
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
gate = (ROOT / "governance/source-quality-gate.md").read_text()
hard = (ROOT / "governance/remaining-hard-gates.md").read_text()
score = (ROOT / "sources/provisional-scorecard.md").read_text()
inventory = (ROOT / "sources/frozen-claim-inventory.md").read_text()
matrix = (ROOT / "sources/claim-evidence-matrix.md").read_text()
expected_claims = {f"C-{i:03d}" for i in range(1, 17)}
checks = {
 "gate_is_changes_required": "CHANGES_REQUIRED" in gate and "CHANGES_REQUIRED" in hard,
 "provisional_score_is_796": bool(re.search(r"\\| \\*\\*796\\*\\* \\|", score)),
 "hard_gate_rows_remain_open": hard.count("| OPEN") >= 6,
 "authorization_dependency_explicit": "authorization" in hard.lower() and "EULA" in (ROOT / "evidence/standards-authorization-pending-2026-10-06.md").read_text(),
 "pdfx6_dependency_explicit": "PDF/X-6" in hard and "authorized tool/runtime dependency" in hard,
 "human_review_dependency_explicit": "human accessibility" in hard.lower() and "second reviewer" in hard.lower(),
 "unqualified_995_claim_absent": "must not claim 995/1000" in hard and "995 target" in gate,
 "release_gate_not_marked_complete": '"status": "CHANGES_REQUIRED"' in (ROOT / "governance/source-quality-gate.json").read_text(),
 "frozen_inventory_is_c001_to_c016": set(re.findall(r"\\bC-\\d{3}\\b", inventory)) == expected_claims,
 "claim_matrix_is_c001_to_c016": set(re.findall(r"\\bC-\\d{3}\\b", matrix)) == expected_claims,
 "legacy_claim_scope_absent": not re.search(r"C-001 through C-0(?:14|15)", "\\n".join([inventory, matrix, gate, hard, score])),
}
result={"checks":checks,"all_pass":all(checks.values()),"release_allowed":False}
print(json.dumps(result,indent=2))
if not result["all_pass"]: raise SystemExit(1)
