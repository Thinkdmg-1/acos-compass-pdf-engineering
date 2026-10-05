# Provisional source-quality scorecard

**Audit date:** 2026-10-05  
**Status:** `PROVISIONAL / NOT A RELEASE SCORE`  
**Target:** 995/1000  
**Hard-veto status:** FAIL — authorized full normative text and clause-by-clause mappings are not complete.

This score follows the frozen rubric in `governance/source-quality-gate.md`. Points are awarded only for evidence currently preserved in the repository. The score is deliberately conservative and cannot authorize a 995 release while a hard veto remains.

| Factor | Available | Provisional points | Evidence basis | Lost points / repair |
|---|---:|---:|---|---|
| Authority and provenance | 180 | 160 | Official ISO, W3C, university, primary research, and official veraPDF sources are identified with URLs, editions, dates, and institutions. | Some supporting guidance is not yet version-locked; complete source provenance package still required. |
| Directness to the claim | 170 | 130 | Official records directly establish identity, edition, status, and scope; PDF/UA-2 public preview exposes relevant section headings; public PDF Association resources provide bounded companion corroboration for PDF/UA-2, PDF/A-4, and PDF/X-6. | Full normative requirements are not available for every claim; identity and companion evidence cannot support clause-level assertions. |
| Technical completeness | 150 | 48 | Labs, validator reports, public preview headings, and research adaptations expose parts of the technical method. | Full ISO clauses, exceptions, tables, and conformance conditions are not mapped. |
| Currency and version control | 120 | 115 | ISO current/confirmed dates, W3C publication statuses, veraPDF 1.30.2 build, hashes, and report dates are recorded. | A small number of university and research sources require explicit archival/version metadata. |
| Reproducibility | 120 | 105 | Local labs, commands, fixtures, raw validator reports, hashes, independent challenge, and a separately authored office-export production experiment, a preserved PDF/A-4-passing repair, and an independent parser/font/geometry/raster inspection are preserved. | Standards-based reproduction still requires authorized text, independent repair review, and a production-condition fixture. |
| Independent corroboration | 100 | 85 | Separate source challenge, independent lab audit, multiple parsers/renderers, veraPDF evidence, and bounded PDF Association companion/index corroboration are recorded. | No independent clause-by-clause standards review or human screen-reader review is complete. |
| Scope and transfer limits | 80 | 78 | Draft-versus-standard, PDF-versus-web, machine-versus-human, parser-versus-print, and teaching-versus-production boundaries are explicit; the office-export failure makes transfer risk concrete. | PDF/X, repaired PDF/A/PDF-UA, color, and vendor acceptance remain untested. |
| Accessibility and recoverability | 40 | 35 | Public source links, local Markdown records, Git history, GitHub mirror, raw reports, and archive hashes are available. | Authorized standards text cannot be redistributed in this record; one installer signature check was unavailable because `gpg` is absent. |
| Evidence integrity | 40 | 40 | Failures, corrections, missing evidence, and non-degree status are preserved; no numerical release claim is made. | No deduction. |
| **Provisional total** | **1,000** | **796** | Evidence-supported working score only. | Hard veto still blocks release. |

## Required path to 995

1. Obtain authorized access to the current ISO normative texts or approved extracts.
2. Map every C-001 through C-016 standards-based claim to exact clauses, definitions, exceptions, and applicability conditions.
3. Have an independent reviewer repeat the mappings and challenge edition/supersession decisions.
4. Complete the human accessibility review and a declared production-condition PDF/X/PDF/A fixture.
5. Re-score each factor, preserve dissent, and apply the hard-veto test before any release decision.

The controlled repair and the independent inspection add evidence for one fixture only; it does not establish a universal repair recipe or production conformance. The provisional total is an audit instrument. It is not a claim that the curriculum is 780/1000 complete, and it is not a substitute for resolving the hard veto.
