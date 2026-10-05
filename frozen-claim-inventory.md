# Frozen curriculum claim inventory

**Freeze date:** 2026-10-05  
**Purpose:** establish the claim set that the 995/1000 source gate must review.  
**Rule:** a claim marked `LIMITED` is usable only for the stated teaching scope. It cannot support a conformance, production-readiness, or mastery statement.

| ID | Claim | Curriculum use | Evidence class | Source ID(s) | Current state | Release condition |
|---|---|---|---|---|---|---|
| C-001 | ISO 32000-2:2020 is the published PDF 2.0 edition identified by the official ISO record. | PFE 601 orientation | NORMATIVE | S-001 | OBSERVED | Authorized text/extract and clause map |
| C-002 | PDF 2.0 defines the document syntax and interchange model used by the object-model labs. | PFE 601 | NORMATIVE | S-001 | PROPOSED STUDY | Authorized syntax clauses, exceptions, and independent challenge |
| C-003 | A PDF page depends on an object graph, resources, content streams, and cross-reference data. | PFE 601 labs | NORMATIVE + LOCAL EXPERIMENT | S-001 | LIMITED IMPLEMENTED STUDY | Authorized clause mapping; retain lab as illustration only |
| C-004 | PDF/UA-2 is the accessibility companion for PDF 2.0 and covers logical structure, artifacts, text, annotations, forms, metadata, navigation, and actions. | PFE 611 | NORMATIVE | S-003 | OBSERVED / LIMITED | Complete authorized standard and conformance map |
| C-005 | PDF/UA-1 and PDF/UA-2 are distinct profiles with different PDF foundations. | PFE 611 | NORMATIVE | S-002/S-003 | OBSERVED / LIMITED | Inspect authorized texts and map requirement differences; retain edition distinction |
| C-006 | PDF/X-6 is a PDF 2.0 print-exchange profile. | PFE 613 | NORMATIVE | S-004 | OBSERVED / LIMITED | Authorized profile requirements and preflight evidence |
| C-007 | PDF/A-4 is a PDF 2.0 preservation profile. | PFE 614 | NORMATIVE | S-005 | OBSERVED / LIMITED | Authorized profile requirements and preservation test |
| C-008 | CSS Paged Media Level 3 describes page boxes, margins, size, orientation, and page-context behavior. | PFE 615 | NORMATIVE WEB SPEC | S-006 | OBSERVED / WORKING DRAFT | Browser/version fixture and divergence record |
| C-009 | CSS Fragmentation Level 3 describes fragmentation containers and controls including breaks, widows, and orphans. | PFE 615 | NORMATIVE WEB SPEC | S-007 | OBSERVED / CANDIDATE REC | Browser/version fixture and divergence record |
| C-010 | WCAG 2.2 text-spacing requirements govern applicable web output, not PDF/UA conformance. | PFE 611/PFE 615 | NORMATIVE WEB ACCESSIBILITY | S-008 | OBSERVED / LIMITED | Requirement-level mapping and PDF/web boundary review |
| C-011 | Dynamic programming can optimize a declared pagination objective under declared constraints. | PFE 604 | PRIMARY RESEARCH + LOCAL EXPERIMENT | S-013/S-014 | IMPLEMENTED STUDY / LIMITED | Full source reproduction and held-out benchmark |
| C-012 | veraPDF profiles provide machine-checkable evidence for selected PDF/A and PDF/UA requirements. | PFE 611/PFE 614 | VALIDATOR SCOPE | S-016 | IMPLEMENTED STUDY / LIMITED | Human accessibility review and declared production fixture |
| C-013 | A successful parser read or raster render does not establish archival, accessibility, or print conformance. | All modules | LOCAL EXPERIMENT + VALIDATOR SCOPE | S-016 | VERIFIED LIMITED PRINCIPLE | Preserve failures and independent challenge |
| C-014 | Reproducible PDF research requires pinned inputs, environment, commands, outputs, hashes, and limitation records. | PFE 605/PFE 615 | UNIVERSITY TEACHING + PROPOSED RULE | S-009/S-011/S-015 | IMPLEMENTED STUDY / LIMITED | Independent committee-style methods challenge |
| C-015 | A doctoral-equivalent curriculum is not an awarded PhD, institutional enrollment, or dissertation defense. | Governance | PROPOSED RULE | ACOS Compass governance | VERIFIED GOVERNANCE BOUNDARY | Never remove the boundary without institutional evidence |

## Gate interpretation

The frozen inventory separates what has been observed from what remains to be proved. C-005 and C-002 are explicit hard-veto items. C-004, C-006, C-007, C-008, C-009, C-010, C-011, C-012, C-013, and C-014 are bounded teaching claims until their stated release conditions are met. No aggregate score is assigned while any hard-veto item remains unresolved.
