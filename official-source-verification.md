# Official source verification — 2026-10-05

This file records the official source checks performed for the 995 gate. It does not reproduce copyrighted standards. It records identity, status, scope, and what remains to be read from the authorized standard text.

## Normative PDF foundations

### ISO 32000-2:2020 — PDF 2.0

Official ISO record: <https://www.iso.org/cms/%20render/live/en/sites/isoorg/contents/data/standard/07/58/75839.html>

- Edition 2, published December 2020.
- ISO currently shows the 2020 edition as published and confirmed in 2026.
- The record identifies 986 pages and ISO/TC 171/SC 2.
- The abstract explicitly covers software that creates, reads, renders, interacts with, and processes PDF.
- The abstract explicitly excludes validation methods, implementation details, rendering operations, hardware, and operating systems.
- ISO lists Draft Amendment 1.2 as under development. It must not be treated as current normative text.

**Curriculum use:** PFE 601 is governed by the 2020 edition. Amendment material is tracked as proposed/future and cannot silently change current requirements.

### ISO 14289-2:2024 — PDF/UA-2

Official ISO record: <https://www.iso.org/cms/%20render/live/en/sites/isoorg/contents/data/standard/08/22/82278.html>

Official Online Browsing Platform sample: <https://www.iso.org/obp/ui?_escaped_fragment_=iso%3Astd%3Aiso%3A14289%3A-2%3Aed-1%3Av1%3Aen>

- Edition 1, published March 2024.
- The scope is construction of accessible digital documents using PDF 2.0 as specified by ISO 32000-2.
- The sample exposes the conformance section and requirements for logical structure, artifacts, text representation, annotations, forms, metadata, navigation, and actions.
- The official scope explicitly excludes conversion processes, implementation or presentation design, storage methods, and hardware/operating systems.
- ISO states that PDF/UA-2 is a companion to ISO 32000-2 and does not replace PDF/UA-1, which is based on ISO 32000-1.

**Curriculum use:** PFE 611 must test the applicable version explicitly. Presence of a structure tree or a validator result cannot be promoted to PDF/UA-2 conformance without the complete requirement set and human review.

### ISO 15930-9:2020 — PDF/X-6

Official ISO record: <https://www.iso.org/standard/77103.html>

- Edition 1, published November 2020.
- The standard specifies complete and partial exchange of print data using PDF 2.0.
- ISO currently marks it for revision and identifies ISO/CD 15930-9.3 as the under-development replacement.
- The draft replacement is not a current published standard and cannot be used as if it were an approved production requirement.

**Curriculum use:** PFE 613 declares the exact PDF/X profile and production condition before preflight. It records the published profile and tracks the draft replacement separately.

### ISO 19005-4:2020 — PDF/A-4

Official ISO record: <https://www.iso.org/standard/71832.html?eu=true>

- Edition 1, published November 2020.
- The standard specifies use of PDF 2.0 to preserve static visual representations of page-based electronic documents over time, with embedded content permitted.
- ISO marks the 2020 edition for revision and identifies ISO/DIS 19005-4.2 as the under-development replacement.
- The draft replacement is not the current published standard.

**Curriculum use:** PFE 614 tests the declared PDF/A profile and records whether the current or future draft is being discussed. It never labels a draft as a conformance target.

## Browser pagination sources

### W3C CSS Paged Media Level 3

Official technical report: <https://www.w3.org/TR/css-page-3/>

- The published page is a Working Draft dated 14 September 2023, not a W3C Recommendation.
- The module describes page context, page boxes, page size, orientation, margins, and fragmentation for paged output.
- It explicitly states that content can fall outside the page box and that handling of such overflow is outside the specification.

**Curriculum use:** PFE 615 treats this as browser-printing specification evidence. It does not convert CSS behavior into PDF, PDF/UA, PDF/X, or PDF/A conformance.

### W3C CSS Fragmentation Module Level 3

Official technical report: <https://www.w3.org/TR/css-break-3/>

- The published page identifies itself as a Candidate Recommendation dated 4 December 2018.
- The status section calls it a draft/work in progress that may be updated, replaced, or obsoleted.
- The abstract and model define fragmentation across pages, columns, and regions, including break controls, widows, and orphans.

**Curriculum use:** PFE 615 records the exact browser and print pathway used for every fixture and keeps unsupported or divergent implementation behavior visible.

## University and research sources

- MIT OCW identifies MAS.962 Digital Typography as graduate material and supplies a syllabus, calendar, assignments, and downloadable course package: <https://ocw.mit.edu/courses/mas-962-digital-typography-fall-1997/>.
- MIT 6.813/6.831 provides the typography, layout, color, accessibility, and doctoral experiment-design/analysis readings used in the foundation study: <https://web.mit.edu/6.813/www/sp17/>.
- RIT's official Color Science PhD page specifies core coursework, a qualifying examination, second-year research project, candidacy examination, and dissertation: <https://www.rit.edu/science/study/color-science-phd>.
- The University of Reading lists active and completed doctoral topics in typography, information design, communication design, materiality, and practice-informed research: <https://www.reading.ac.uk/typography/phd/phd-research-topics>.
- Brüggemann-Klein, Klein, and Wohlfeil's *Pagination Reconsidered* is the primary pagination research source used for the teaching adaptation: <https://d-nb.info/1149749830/34>.

These sources support curriculum shape and research context. They do not certify the learner, replace the standards, or prove completion of a course or degree.

## Validator source

### veraPDF validation model and release evidence

Official validation documentation: <https://docs.verapdf.org/validation/>

CLI profile documentation: <https://docs.verapdf.org/cli/validation/>

Official test corpus: <https://github.com/veraPDF/veraPDF-corpus>

Release page inspected: <https://github.com/veraPDF/veraPDF-library/releases>

- The documentation says the engine formalizes PDF/A and PDF/UA `shall` requirements as runtime validation profiles.
- The docs explicitly distinguish machine-verifiable PDF/UA checks from human checkpoints and point to the Matterhorn protocol for that boundary.
- The CLI documentation lists distinct profiles including PDF/A-4, PDF/UA-1, and PDF/UA-2, and explains that profile selection can come from metadata or an explicit command option.
- The corpus repository describes atomic, self-documented tests for PDF/A, PDF/UA, ISO 32000-1, and ISO 32000-2.
- The release page currently identifies veraPDF v1.26.2; this version is recorded as source evidence, not as a completed local validation run.

**Curriculum use:** PFE 611/PFE 614 must record the exact veraPDF version, profile, command, report, test fixture, and human inspection protocol. A validator pass is machine evidence only and cannot establish full PDF/UA conformance alone.

## Gate disposition after verification

The source inventory now has direct official ISO records for the governing PDF 2.0, PDF/UA-2, PDF/X-6, and PDF/A-4 identities and current status. The remaining hard-veto work is access to the complete authorized normative texts, a claim-by-claim mapping of the curriculum to those texts, and a local veraPDF run. Until that is completed, the source gate remains `CHANGES_REQUIRED`; a 995 score is not claimed.
