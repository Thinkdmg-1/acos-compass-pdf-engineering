# Independent source challenge — 2026-10-05

## Method

The source register was challenged against a second inspection path: official ISO record pages, W3C technical-report status pages, official veraPDF documentation/release material, and the local validator receipts. The challenge checked identity, edition, current status, scope, supersession, and whether the curriculum had silently upgraded a summary into a normative requirement.

## Findings

| Check | Result | Evidence |
|---|---|---|
| PDF 2.0 edition and status | Pass, bounded | ISO 32000-2:2020 is Edition 2, published 2020-12, confirmed current in 2026; Amendment 1.2 is tracked as future work. |
| PDF/UA-1 edition and supersession | Pass, bounded | ISO 14289-1:2014 is current Edition 2, confirmed in 2025; ISO 14289-1:2012 is withdrawn and excluded. |
| PDF/UA-2 edition and foundation | Pass, bounded | ISO 14289-2:2024 is Edition 1 and uses PDF 2.0; it does not replace PDF/UA-1. |
| PDF/X-6 and PDF/A-4 status | Pass, bounded | Official ISO records identify the published 2020 editions and separately identify revisions under development. |
| Browser specification status | Pass, bounded | CSS Paged Media is a Working Draft; CSS Fragmentation is a Candidate Recommendation explicitly described as draft work. Neither is represented as a Recommendation or ISO requirement. |
| Validator scope | Pass, bounded | veraPDF documentation distinguishes formalized machine checks from human PDF/UA checkpoints; local 1.30.2 reports are preserved. |
| Claim inventory completeness | Pass for frozen slice | C-001 through C-015 are explicit; unresolved authorized-text mappings remain visible. |
| Hidden conflict or silent substitution | No conflict found; open limitations remain | PDF/UA-1 vs PDF/UA-2, published vs draft revisions, browser vs PDF conformance, and validator vs human review are separated. |

## Outcome

The source register passes this independent identity/status challenge for the inspected public evidence. It does **not** pass the 995 release gate. The hard veto remains the missing authorized full normative text and clause-by-clause mapping for the standards-based claims. This report therefore supports `CHANGES_REQUIRED`, not a numerical score.

