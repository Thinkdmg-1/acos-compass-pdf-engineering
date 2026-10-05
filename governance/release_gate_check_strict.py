"""Fail-closed release-state check for the ACOS PDF-engineering repository.

This check validates governance language and hard-gate state. It is not a
standards validator and cannot award points or replace human review.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read_governed(relative: str) -> str:
    """Read the canonical path, with a public-snapshot root fallback."""
    canonical = ROOT / relative
    if canonical.exists():
        return canonical.read_text()
    fallback = ROOT / Path(relative).name
    if fallback.exists():
        return fallback.read_text()
    raise FileNotFoundError(f"missing governed input: {relative}")

gate = read_governed("governance/source-quality-gate.md")
hard = read_governed("governance/remaining-hard-gates.md")
score = read_governed("sources/provisional-scorecard.md")
inventory = read_governed("sources/frozen-claim-inventory.md")
matrix = read_governed("sources/claim-evidence-matrix.md")
expected_claims = {f"C-{i:03d}" for i in range(1, 17)}
expected_hard_gates = {
    "Authorized normative custody",
    "Clause mappings",
    "PDF/X-6 preflight",
    "Human accessibility",
    "Production equivalence",
    "Doctoral completion",
}
hard_gate_names = {line.split("|", 2)[1].strip() for line in hard.splitlines() if line.startswith("| ") and "| OPEN" in line}

checks = {
    "gate_is_changes_required": "CHANGES_REQUIRED" in gate and "CHANGES_REQUIRED" in hard,
    "provisional_score_is_796": bool(re.search(r"\| \*\*796\*\* \|", score)),
    "hard_gate_rows_remain_open": hard.count("| OPEN") >= 6,
    "hard_gate_names_exact": hard_gate_names == expected_hard_gates,
    "authorization_dependency_explicit": "authorization" in hard.lower() and "EULA" in read_governed("evidence/standards-authorization-pending-2026-10-06.md"),
    "pdfx6_dependency_explicit": "PDF/X-6" in hard and "authorized tool/runtime dependency" in hard,
    "human_review_dependency_explicit": "human accessibility" in hard.lower() and "second reviewer" in hard.lower(),
    "unqualified_995_claim_absent": "must not claim 995/1000" in hard and "995 target" in gate,
    "release_gate_not_marked_complete": '"status": "CHANGES_REQUIRED"' in read_governed("governance/source-quality-gate.json"),
    "frozen_inventory_is_c001_to_c016": set(re.findall(r"\bC-\d{3}\b", inventory)) == expected_claims,
    "claim_matrix_is_c001_to_c016": set(re.findall(r"\bC-\d{3}\b", matrix)) == expected_claims,
    "legacy_claim_scope_absent": not re.search(r"C-001 through C-0(?:14|15)", "\n".join([inventory, matrix, gate, hard, score])),
}
result = {"checks": checks, "all_pass": all(checks.values()), "release_allowed": False}
print(json.dumps(result, indent=2))
if not result["all_pass"]:
    raise SystemExit(1)
