# Claim-to-source evidence matrix

This matrix prevents a curriculum topic from masquerading as a verified standard requirement. The current matrix is a live audit record; `MISSING` items block the 995 release gate.

| Claim family | Curriculum location | Source | Evidence currently inspected | State | Missing evidence / next action |
|---|---|---|---|---|---|
| PDF 2.0 identity, purpose, scope | PFE 601 | S-001 / official ISO record | Edition, date, 986 pages, committee, purpose, explicit exclusions, 2026 confirmation | OBSERVED | Authorized full text or approved extract; clause-by-clause map |
| PDF 2.0 syntax and object model | PFE 601 | S-001 | No complete normative clause inspection yet | PROPOSED STUDY TOPIC | Read authorized clauses; map syntax claims and exceptions |
| PDF/UA-2 identity and scope | PFE 611 | S-003 / ISO record and OBP sample | Edition/date, PDF 2.0 dependency, conformance section, logical structure, artifacts, text, annotations, forms, metadata, navigation | OBSERVED | Complete authorized standard; map every conformance assertion |
| PDF/UA-1 distinction | PFE 611 | S-002 | Source identity not yet independently inspected | MISSING | Verify edition/corrigenda and compare scope with PDF/UA-2 |
| PDF/X-6 identity and revision status | PFE 613 | S-004 / official ISO record | Edition/date, PDF 2.0 basis, published status, revision and future draft | OBSERVED | Authorized standard text and exact profile requirement map |
| PDF/A-4 identity and revision status | PFE 614 | S-005 / official ISO record | Edition/date, PDF 2.0 basis, preservation scope, revision and future draft | OBSERVED | Authorized standard text and profile requirement map |
| CSS page size and fragmentation behavior | PFE 601/PFE 615 | S-006/S-007 | W3C Paged Media Level 3 page identifies itself as a Working Draft dated 2023-09-14, describes page boxes/margins/size/orientation and fragmentation, and explicitly leaves content outside the page box to user-agent handling; CSS Fragmentation is recorded as a separate Working Draft source | OBSERVED / LIMITED | Build browser-vs-spec fixtures for page size, `break-*`, `widows`, `orphans`, and overflow; record browser/version, print settings, raster/PDF evidence, and divergences. Do not present the WD as Recommendation-level conformance. |
| WCAG text spacing and web accessibility | PFE 611 | S-008 | WCAG 2.2 Recommendation and text-spacing scope inspected | OBSERVED | Map only web claims; maintain PDF/UA separation |
| Typography and layout principles | PFE 603 | S-009/S-010 | MIT readings and assignments actually read; adaptations recorded | IMPLEMENTED STUDY | Independent pedagogical challenge and current research corroboration |
| Doctoral research-methods sequence | PFE 605 | S-009/S-011/S-012/S-015 | MIT doctoral readings, RIT program structure, Reading research scope, ASA statement inspected | IMPLEMENTED STUDY | Independent committee-style examination |
| Pagination objective and dynamic programming | PFE 604 | S-013/S-014 | Pagination paper inspected through algorithm and constraints; local model independently tested | IMPLEMENTED STUDY | Full Knuth–Plass source and reproduction of published benchmark |
| Validator scope | PFE 611/PFE 614 | S-016 | Documentation identified; tool version and test run not yet captured in this repository | MISSING | Pin validator version, run, archive report, and human-review boundary |
| Vendor implementation behavior | PFE 601/PFE 613 | S-017 | Not used as normative authority | PROPOSED SUPPORT | Capture versioned vendor source only where needed and corroborate with ISO |
| Independent challenge of completed labs | PFE 601/PFE 602/PFE 604/PFE 611 | evidence/independent-audit-2026-10-05.md | Separate reviewer reproduced bounded computational, geometry, tagging, font, hash, and raster checks and recorded six scope limits | IMPLEMENTED STUDY / LIMITED | Extend challenge to authorized normative clauses, validator version/run, screen-reader review, and held-out production files |

## Admission rule

Only `OBSERVED` or `IMPLEMENTED STUDY` rows can support a current claim, and only within the stated scope. `PROPOSED`, `MISSING`, and `PROPOSED STUDY TOPIC` rows cannot support a conformance or mastery statement. The current matrix therefore keeps the overall source gate `CHANGES_REQUIRED`.
