# ACOS Compass: doctoral PDF engineering curriculum

This repository is the durable learning home for Echo's Compass. It turns the three-failure recovery rule into a repeatable curriculum for PDF engineering: standards study, university coursework, controlled laboratories, independent challenge, qualifying examinations, candidacy, and dissertation research.

The curriculum is intentionally stronger than a production checklist. It requires a learner to understand the PDF object model, typography and shaping, layout algorithms, accessibility, color science, print production, preservation, reproducible software, research methods, and original contribution. A polished export does not count as doctoral evidence.

## Repository map

- `curriculum/doctoral-curriculum.md` — four-year, 60-credit doctoral-equivalent sequence and gates.
- `governance/three-failure-recovery.md` — ACOS Compass recovery rule.
- `governance/study-plan.json` — ordered plan with inputs, methods, verification, and stop conditions.
- `governance/source-quality-gate.md` — 995/1000 source gate and release rules.
- `sources/source-register.md` — source inventory and required inspections.
- `sources/official-source-verification.md` — official ISO status and scope checks.
- `sources/claim-evidence-matrix.md` — claim-by-claim evidence states and remaining hard vetoes.
- `sources/frozen-claim-inventory.md` — frozen claim IDs, evidence classes, release conditions, and explicit hard-veto items.
- `sources/independent-source-challenge.md` — second-path identity, version, scope, and conflict challenge for the source register.
- `sources/provisional-scorecard.md` — conservative factor-by-factor score with hard-veto status; explicitly not a release score.
- `evidence/foundation-study.md` — actual completed foundation study.
- `evidence/independent-challenge.md` — independent technical challenge and limits.
- `evidence/pfe611-accessibility-review-2026-10-05.md` — structured tagged-PDF review with completed checks and unavailable human checks separated.
- `evidence/retained-pdf-lessons.md` — scoped reusable lessons.
- `evidence/standards-access-recheck-2026-10-06.md` — current sponsored-access, public-model, and errata recheck with custody boundaries.
- `evidence/arlington-object-model-lab-2026-10-06.md` — pinned Arlington TSV inspection and independent catalog/structure comparison.
- `evidence/pdf2normrefs-graph-lab-2026-10-06.md` — pinned PDF 2.0 normative-reference graph traversal and integrity receipt.
- `evidence/public-errata-profile-recheck-2026-10-06.md` — current PDF/A-4 and PDF/X-6 errata, revision, and copyright-boundary receipt.
- `evidence/pdf20-examples-lab-2026-10-06.md` — dual-reader inspection of public PDF 2.0 examples and deliberate edge cases.
- `evidence/entry-diagnostic-2026-10-06.md` — five-part entry diagnostic classification and next-gate boundaries.
- `reports/pfe601-rerun-2026-10-06/` — source-level rerun receipt for the object-model and xref-repair labs.
- `evidence/pfe602-font-capability-2026-10-06.md` — installed-font metadata and shaping-toolchain boundary for PFE 602.
- `reports/css-pagination-rerun-2026-10-06/` — independent pypdf/Poppler rerun of the frozen Chrome pagination artifact.
- `evidence/pfe604-color-profile-receipt-2026-10-06.md` — ICC profile inventory and output-intent inspection with print-color boundaries.
- `reports/verapdf-runtime-capability-2026-10-06/` — fresh veraPDF launcher check showing the current Java-runtime boundary.
- `labs/` — executable exercises and saved results.
- `reports/verapdf-1.30.2/` — pinned PDF/A-4 and PDF/UA-2 validator reports, stderr captures, hashes, and interpretation limits.
- `reports/production-pdfa4-2026-10-05/` — separately authored office-export experiment with preserved initial failures and a bounded post-export PDF/A-4 repair pass; PDF/UA-2 remains failed.
- `reports/profile-test-plan-2026-10-05/` — declared next-step plan for authorized normative-text custody, profile tests, and human accessibility review.
- `reports/human-review-partial-2026-10-05/` — bounded 144/288 DPI visual review receipt; explicitly not a PDF/UA conformance review.
- `reports/preflight-capability-inventory-2026-10-05/` — fresh executable inventory showing why PDF/X-6 preflight remains unexecuted in this environment.
- `reports/repository-integrity-2026-10-05/` — independent source-ID, path, package, and release-state consistency receipt.
- `governance/completion-audit-2026-10-05.md` — current requirement-by-requirement completion audit and hard-veto decision.

## Evidence state

The repository currently contains a foundation recovery slice. It does not claim a PhD, completed coursework, qualifying-exam passage, candidacy, dissertation, or universal PDF conformance. Future work must advance through the gates in the curriculum and update the evidence state explicitly.

## Operating rule

When three failures occur on the same capability, stop repeating the unchanged approach. Return to the curriculum, identify the smallest falsifiable deficiency, complete the relevant study and exercise, test an unfamiliar case, obtain independent challenge, and only then retry the production task.

## Sources

The source register distinguishes standards, primary research, university teaching material, validator documentation, and informative guidance. The 995 target is a hard source-quality gate, not a decorative claim. A score is recorded only after source identity, authority, version, scope, access, applicability, and limitations are evidenced.
