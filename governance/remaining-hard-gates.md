# Remaining hard gates — 2026-10-06

This register is the completion audit's actionable dependency list. A gate is cleared only by the evidence named here; a compatible experiment, search result, validator summary, or generated paraphrase is insufficient.

| Gate | Evidence required to clear it | Current evidence | State |
|---|---|---|---|
| Authorized normative custody | Authorized copies or permitted extracts of ISO 32000-2:2020, ISO 14289-2:2024, ISO 15930-9:2020, and ISO 19005-4:2020, with edition, digest, custody, and license record | Official identity/status records, previews, public companion material, and access-path receipts are preserved; complete authorized text has not been obtained | OPEN — authorization-dependent |
| Clause mappings | Claim-by-claim mappings from the frozen inventory to exact normative clauses, including exceptions and scope limits | Claim matrix exists, but normative clause locations remain marked missing for material PDF/PDF-UA/PDF-X/PDF-A claims | OPEN — follows normative custody |
| PDF/X-6 preflight | An accepted PDF/X-6 validator or preflight implementation, pinned version/profile, reproducible command, report, and independent challenge | PDF Oxide source-level X6 probe and controlled variants are preserved; the PDF Association lists Enfocus PitStop Library Container as a PDF/X-6 preflight candidate, but no licensed runtime, profile package, or authorized execution is available; veraPDF's built-in profiles do not include PDF/X-6 | OPEN — authorized tool/runtime dependency |
| Human accessibility | Screen-reader, keyboard/navigation, visual reading-order, alternative-text, table, link, and artifact review by an equipped human reviewer, with independent second review | Machine checks and bounded visual inspection exist; human review and second reviewer are absent | OPEN — human-review dependency |
| Production equivalence | Declared production export path, representative production fixture, preflight output, preservation checks, and independent review | Office-export and repaired-fixture experiments exist; production-path equivalence is unproven | OPEN — production fixture dependency |
| Doctoral completion | Completed curriculum gates, qualifying examination, candidacy/dissertation evidence, and external examination | Curriculum and bounded study evidence exist; no institutional degree or completed doctoral program is claimed | OPEN — research/assessment dependency |

## Release effect

The source-quality gate remains `CHANGES_REQUIRED` at the conservative provisional score recorded in `sources/provisional-scorecard.md`. The repository must not claim 995/1000, standards conformance, a PhD, or production release while any row above is open.

## Independence rule

The machine receipts in `evidence/final-machine-verification-2026-10-06.md` and the public structural receipt establish reproducibility for their stated scopes. They do not close the human, normative-custody, validator-authority, or production-equivalence rows by inference.
