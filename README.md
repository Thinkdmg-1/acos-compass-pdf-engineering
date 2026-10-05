# Repository integrity receipt

**Date:** 2026-10-05; rerun after the PDF/X-6 capability probe
**Purpose:** independently check that the source register, claim matrix, local evidence paths, Markdown handoff package, and release-state records are internally consistent. This is a repository-integrity check, not a standards-conformance or 995 score.

## Frozen method

A fresh Python process parsed the Markdown source register and claim matrix, extracted every `S-###` reference, checked referenced local paths, reopened the handoff ZIP, enumerated its entries, calculated its SHA-256, and searched the source-quality gate for the declared release state. The ZIP was then checked with assertions for exactly 17 entries, all ending in `.md`.

## Receipt

```json
{
  "source_register_ids": 21,
  "claim_matrix_ids": ["S-001", "S-002", "S-003", "S-004", "S-005", "S-006", "S-007", "S-008", "S-009", "S-010", "S-011", "S-012", "S-013", "S-014", "S-015", "S-016", "S-017", "S-018", "S-020", "S-021"],
  "missing_source_ids": [],
  "referenced_local_paths": 1,
  "missing_local_paths": [],
  "package_entries": 17,
  "package_non_markdown": [],
  "package_sha256": "1b30a3455587d94ed4289019900b7272d036d9f7f502703fc831deb83cd887e5",
  "gate_state": "CHANGES_REQUIRED"
}
```

## Interpretation

All source IDs used by the claim matrix resolve to the source register, the checked local path resolves, and the handoff package is Markdown-only with the recorded digest. These checks remove repository-linkage uncertainty; they do not remove the hard veto for missing authorized normative text, clause mappings, PDF/X-6 preflight, or human accessibility review.
