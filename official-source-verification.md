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

## University and research sources

- MIT OCW identifies MAS.962 Digital Typography as graduate material and supplies a syllabus, calendar, assignments, and downloadable course package: <https://ocw.mit.edu/courses/mas-962-digital-typography-fall-1997/>.
- MIT 6.813/6.831 provides the typography, layout, color, accessibility, and doctoral experiment-design/analysis readings used in the foundation study: <https://web.mit.edu/6.813/www/sp17/>.
- RIT's official Color Science PhD page specifies core coursework, a qualifying examination, second-year research project, candidacy examination, and dissertation: <https://www.rit.edu/science/study/color-science-phd>.
- The University of Reading lists active and completed doctoral topics in typography, information design, communication design, materiality, and practice-informed research: <https://www.reading.ac.uk/typography/phd/phd-research-topics>.
- Brüggemann-Klein, Klein, and Wohlfeil's *Pagination Reconsidered* is the primary pagination research source used for the teaching adaptation: <https://d-nb.info/1149749830/34>.

These sources support curriculum shape and research context. They do not certify the learner, replace the standards, or prove completion of a course or degree.

## Gate disposition after verification

The source inventory now has direct official ISO records for the governing PDF 2.0, PDF/UA-2, PDF/X-6, and PDF/A-4 identities and current status. The remaining hard-veto work is access to the complete authorized normative texts and a claim-by-claim mapping of the curriculum to those texts. Until that is completed, the source gate remains `CHANGES_REQUIRED`; a 995 score is not claimed.
