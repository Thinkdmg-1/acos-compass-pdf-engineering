# Source register

This register is the starting inventory for the 995 gate. Each row must be inspected directly before the source set is released. URLs are entry points, not proof of content.

| ID | Source | Class | Use | Version/status | Required inspection |
|---|---|---|---|---|---|
| S-001 | ISO 32000-2:2020, PDF 2.0, with approved errata | NORMATIVE | syntax, graphics, text, rendering, interaction, document interchange | Edition 2, published 2020-12; ISO record says confirmed 2026; Draft Amendment 1.2 is future work | use official ISO identity/status record; obtain authorized text or approved extract; map every PFE 601 claim |
| S-002 | ISO 14289-1, PDF/UA-1 | NORMATIVE | accessible PDF requirements | edition and corrigenda to verify | map structure, tagging, metadata, alternatives, reading order; do not substitute PDF/UA-2 |
| S-003 | ISO 14289-2:2024, PDF/UA-2 | NORMATIVE | PDF 2.0 accessibility | Edition 1, published 2024-03; official ISO/OBP sample inspected | record differences from PDF/UA-1 and applicable conformance tests |
| S-004 | ISO 15930-9:2020, PDF/X-6 | NORMATIVE | PDF 2.0 print exchange and prepress | Edition 1, published 2020-11; ISO marks for revision; CD 15930-9.3 is future work | choose exact published profile before production exercises; track draft separately |
| S-005 | ISO 19005-4:2020, PDF/A-4 | NORMATIVE | PDF 2.0 long-term preservation | Edition 1, published 2020-11; ISO marks for revision; DIS 19005-4.2 is future work | map embedded resources, metadata, identifiers, prohibited features, and profile status |
| S-006 | W3C CSS Paged Media Level 3 | NORMATIVE WEB SPEC | page size, margins, page context | Working Draft, 2023-09-14; not a W3C Recommendation | separate CSS behavior from PDF conformance; inspect page boxes, fragmentation, overflow limits |
| S-007 | W3C CSS Fragmentation Level 3 | NORMATIVE WEB SPEC | breaks, widows, orphans, fragmentation | Candidate Recommendation dated 2018-12-04; page states it is draft/work in progress and may be replaced or obsoleted | test browser implementation against the specification and record unsupported/ambiguous cases |
| S-008 | WCAG 2.2 | NORMATIVE WEB ACCESSIBILITY | web accessibility and text spacing | Recommendation 2024 | map only applicable web claims; do not substitute for PDF/UA |
| S-009 | MIT 6.813/6.831 | UNIVERSITY TEACHING | typography, layout, color, accessibility, research methods | Spring 2017 materials | record reading scope and pedagogical limitations |
| S-010 | MIT MAS.962 Digital Typography | UNIVERSITY GRADUATE TEACHING | typography systems and assignments | Fall 1997 materials | complete and document assignments; distinguish adapted work |
| S-011 | RIT Color Science PhD curriculum | UNIVERSITY DOCTORAL PROGRAM | color science, vision, physics, research methods | current program page/catalog | use as curriculum model; do not represent as completed enrollment |
| S-012 | University of Reading Typography PhD research | UNIVERSITY DOCTORAL RESEARCH | practice-informed typography research and dissertation scope | current research page | use as research-domain map, not technical norm |
| S-013 | Brüggemann-Klein, Klein, Wohlfeil, *Pagination Reconsidered* | PRIMARY RESEARCH | page-turn objective and dynamic programming | 1996 technical report | read full paper before claiming algorithm reproduction |
| S-014 | Knuth–Plass line-breaking research and TeX sources | PRIMARY RESEARCH / SOFTWARE | line breaking and typesetting algorithms | original papers and implementation versions | reproduce algorithmic assumptions and compare implementations |
| S-015 | American Statistical Association p-value statement | PROFESSIONAL GUIDANCE | interpretation and reporting of quantitative evidence | 2016 statement | use with current statistical methods, not as a full statistics text |
| S-016 | veraPDF validation documentation and test suite | VALIDATOR SCOPE | machine-checkable PDF/A and PDF/UA evidence | tool version must be recorded | state exactly what the validator checks and omits |
| S-017 | Adobe PDF and color-management technical documentation | VENDOR GUIDANCE | implementation behavior and output intents | version/date to verify | never upgrade vendor advice into ISO requirement without corroboration |
| S-018 | PDF Association standards and technical guidance | INDUSTRY GUIDANCE | standards access and implementation commentary | current page/edition to verify | use as navigation and interpretation; trace normative claims to ISO |

## Source-use rules

- S-001 through S-008 control only the requirements within their scopes.
- S-009 through S-012 establish university-level teaching and research shape; they do not certify the learner.
- S-013 through S-015 provide research evidence and methodological guidance; their dates and assumptions remain visible.
- S-016 through S-018 describe tools or industry practice; they cannot silently replace the controlling standard.
- Every claim must name the source ID and state whether it is a fact, interpretation, local experiment, or proposed curriculum rule.
- W3C Working Draft language is treated as specification evidence for the browser-printing module, never as an ISO or W3C Recommendation-level conformance requirement.
- The score remains `CHANGES_REQUIRED` until the register is filled with actual inspected locations, version data, checksums where possible, and an independent challenge.
