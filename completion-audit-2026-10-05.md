# ACOS Compass PDF-engineering completion audit

**Audit date:** 2026-10-05  
**Objective:** execute the doctoral PDF-engineering curriculum and source-quality gate to the ACOS 995/1000 standard.  
**Current disposition:** `INCOMPLETE / CHANGES_REQUIRED`  
**Audit method:** each requirement is checked against the current repository, preserved reports, and public repository state. Indirect evidence is not promoted to completion.

## Requirement audit

| Requirement | Evidence inspected | Finding | State |
|---|---|---|---|
| Doctoral curriculum exists | `curriculum/doctoral-curriculum.md`, `study-plan.json` | Four-year sequence, prerequisites, laboratories, research and examination requirements are present. | **PROVEN** |
| ACOS recovery rule is encoded | `governance/three-failure-recovery.md`, `governance/source-quality-gate.md` | Three-failure diagnosis, frozen measurements, independent challenge, and honest release states are recorded. | **PROVEN** |
| Claim inventory is frozen | `sources/frozen-claim-inventory.md` | Claims C-001 through C-014 have source IDs, evidence classes, and next evidence requirements. | **PROVEN** |
| Source register is independently challenged | `sources/source-register.md`, `sources/independent-source-challenge.md` | Authority, identity, edition/status, access boundaries, and unresolved conflicts are recorded. | **PROVEN / LIMITED** |
| PDF 2.0 normative clause map | `sources/claim-evidence-matrix.md`, `sources/official-source-verification.md` | Official identity and sponsored access path are verified; complete authorized text and clause map are absent. | **MISSING** |
| PDF/UA-2 normative clause map | same source files, public preview and WTPDF companion record | Identity, scope, preview headings, and bounded companion corroboration are verified; clauses 5–8 and complete authorized text are absent. | **MISSING** |
| PDF/A-4 profile map and production preflight | `reports/production-pdfa4-2026-10-05/`, `reports/profile-test-plan-2026-10-05/README.md` | One fixture passes PDF/A-4 after a bounded repair; independent inspection and limitations are preserved. No declared production fixture or complete normative profile map exists. | **LIMITED** |
| PDF/X-6 profile map and preflight | `reports/verapdf-1.30.2/profile-inventory.md`, official-source records | ISO identity and PDF Association scope corroboration exist. veraPDF exposes no PDF/X-6 profile and no PDF/X-capable preflight result is present. | **UNTESTED** |
| Browser/CSS pagination evidence | `reports/css-pagination-2026-10-05/` | Chrome print output and Firefox divergence are recorded with versions, fixture, and independent page/text checks. | **PROVEN / LIMITED** |
| Tagged-PDF machine checks | `evidence/pfe611-accessibility-review-2026-10-05.md`, veraPDF reports | Object-level structure observations and validator failures are preserved. | **PROVEN / LIMITED** |
| Human accessibility checks | `reports/profile-test-plan-2026-10-05/README.md` | Keyboard, screen-reader, visual, and second-reviewer checks are specified but not executed in an equipped environment. | **MISSING** |
| Independent lab challenge | `evidence/independent-audit-2026-10-05.md` | Separate parser, geometry, font, hash, and raster checks are preserved; scope limits are explicit. | **PROVEN / LIMITED** |
| Public repository publication | GitHub repository; the audit artifact is visible in the rendered repository after publication | Latest test plan is visible in the public repository. | **PROVEN** |
| Markdown-only handoff package | `outputs/ACOS-Compass-MD-University-Study.zip` | 17 entries, all `.md`; SHA-256 `1b30a3455587d94ed4289019900b7272d036d9f7f502703fc831deb83cd887e5`. | **PROVEN** |
| 995/1000 source gate | `governance/source-quality-gate.md`, `sources/provisional-scorecard.md` | Conservative provisional score is 796/1000. Hard veto remains active because normative text, clause maps, PDF/X-6 preflight, and human checks are incomplete. | **NOT ACHIEVED** |

## Independent consistency checks

- The local repository is clean after the audit commit and its latest commit is checked independently with `git status` and `git log`.
- The public repository exposes the new test-plan artifact and commit independently through GitHub’s rendered page.
- The Markdown package was rebuilt from the study directory, then reopened as a ZIP and checked for exactly 17 Markdown entries and zero non-Markdown entries.
- The source gate and scorecard use the same disposition: `CHANGES_REQUIRED`; no numerical 995 claim appears in either record.

## Hard-veto decision

The objective is not complete. The decisive missing evidence is authorized access to the controlling normative standard text and clause-by-clause mapping for PDF 2.0, PDF/UA-2, PDF/A-4, and PDF/X-6. Separate unresolved production gates are PDF/X-6 preflight and equipped human accessibility review. Public identity pages, abstracts, previews, technical indexes, validator output, and local experiments cannot substitute for those requirements.

The next allowed state transition is defined in `reports/profile-test-plan-2026-10-05/README.md`: obtain authorized text and custody receipts, run the declared profile and human checks, preserve complete reports, and then rerun this audit. Until those artifacts exist, the repository must remain `INCOMPLETE / CHANGES_REQUIRED`.
