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
- The public preview exposes the table of contents and section headings for 1 Scope, 2 Normative references, 5 Version identification, 6 Conformity requirements, 7 Accessible PDF, and 8 File format requirements. Section 8 lists logical structure, artifacts, text representation, real content without textual semantics, text string objects, optional content, intra-document destinations, annotations, forms, metadata, navigation, and actions.
- The official scope explicitly excludes conversion processes, implementation or presentation design, storage methods, and hardware/operating systems.
- ISO states that PDF/UA-2 is a companion to ISO 32000-2 and does not replace PDF/UA-1, which is based on ISO 32000-1.

**Curriculum use:** PFE 611 must test the applicable version explicitly. Presence of a structure tree or a validator result cannot be promoted to PDF/UA-2 conformance without the complete requirement set and human review.

#### Public-preview inspection record (2026-10-05)

The official ISO Online Browsing Platform preview was inspected directly at the URL above. The accessible preview exposed the following material before the paywall boundary:

- Introduction: PDF/UA is concerned with machine-readable text in a declared language, semantic structures, logical reading order, and descriptive metadata such as image alternatives.
- Scope clauses 1 and 2: PDF/UA-2 specifies use of PDF 2.0 to construct accessible digital documents; it excludes conversion processes, presentation implementation details, physical storage, hardware/operating systems, and content-specific requirements beyond programmatic access and textual representation.
- Normative references: ISO 14289-1, ISO 32000-2:2020, ISO/TS 32005:2023, DPUB-ARIA 1.0, and PDF Declarations are named.
- Terms 3.1–3.7: assistive technology, PDF 1.7 namespace, PDF 2.0 namespace, real content, structure attribute, unique PDF 1.7 element, and artifact marked content sequence are exposed.

The preview then states that only informative sections are publicly available and that the full content requires purchase. This is stronger direct evidence for identity, scope, normative references, and terminology than an abstract, but it is still insufficient for a complete clause-by-clause conformance map. Clauses 5–8 remain uninspected from the authorized full text.

### ISO 14289-1:2014 — PDF/UA-1

Official ISO record: <https://www.iso.org/cms/%20render/live/en/sites/isoorg/contents/data/standard/06/45/64599.html>

- Edition 2, published December 2014.
- The official record says the edition was last reviewed and confirmed in 2025 and remains current.
- The abstract identifies ISO 32000-1:2008 as the PDF foundation and lists the same broad exclusions for conversion processes, rendering implementation details, storage, and hardware/operating systems.
- ISO 14289-1:2012 is separately listed as withdrawn; it must not be used as the current PDF/UA-1 edition.

**Curriculum use:** PFE 611 keeps PDF/UA-1 and PDF/UA-2 separate. The official records establish the edition distinction and PDF foundation; complete requirement-by-requirement comparison still requires authorized standard text.

### ISO 15930-9:2020 — PDF/X-6

Official ISO record: <https://www.iso.org/standard/77103.html>

- Edition 1, published November 2020.
- The standard specifies complete and partial exchange of print data using PDF 2.0.
- ISO currently marks it for revision and identifies ISO/CD 15930-9.3 as the under-development replacement.
- The draft replacement is not a current published standard and cannot be used as if it were an approved production requirement.

**Curriculum use:** PFE 613 declares the exact PDF/X profile and production condition before preflight. It records the published profile and tracks the draft replacement separately.

#### Current public record recheck (2026-10-05)

The current ISO record was rechecked directly. It identifies ISO 15930-9:2020 as Edition 1, published 2020-11, 26 pages, published and under revision, covering complete and partial print-data exchange using PDF 2.0 and identifying ISO/CD 15930-9.3 as the replacement under development. This confirms profile identity and revision status only; it does not provide the PDF/X-6 requirement clauses or a preflight result.

### ISO 19005-4:2020 — PDF/A-4

Official ISO record: <https://www.iso.org/standard/71832.html?eu=true>

- Edition 1, published November 2020.
- The standard specifies use of PDF 2.0 to preserve static visual representations of page-based electronic documents over time, with embedded content permitted.
- ISO marks the 2020 edition for revision and identifies ISO/DIS 19005-4.2 as the under-development replacement.
- The draft replacement is not the current published standard.

**Curriculum use:** PFE 614 tests the declared PDF/A profile and records whether the current or future draft is being discussed. It never labels a draft as a conformance target.

#### Current public record recheck (2026-10-05)

The current ISO record was rechecked directly. It identifies ISO 19005-4:2020 as Edition 1, published 2020-11, 27 pages, published but under revision, with ISO/DIS 19005-4.2 identified as the forthcoming replacement. The public abstract repeats the PDF 2.0 preservation purpose and the exclusions for conversion processes, rendering implementation, storage conditions, and hardware/operating systems. The draft replacement remains non-current and is not used as a normative source.

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
- The official release/distribution inspected for this run is veraPDF v1.30.2, built 2026-06-03; the exact installer digest and local reports are preserved in `reports/verapdf-1.30.2/`.

**Curriculum use:** PFE 611/PFE 614 records the exact veraPDF version, profile, command, report, test fixture, and human inspection boundary. The 2026-10-05 run found no compliant PDF/A-4 or PDF/UA-2 fixture in the teaching set; a validator result remains machine evidence only and cannot establish full PDF/UA conformance alone.

## Gate disposition after verification

The source inventory now has direct official ISO records for the governing PDF 2.0, PDF/UA-2, PDF/X-6, and PDF/A-4 identities and current status, plus a pinned local veraPDF run. The remaining hard-veto work is access to the complete authorized normative texts and a claim-by-claim mapping of the curriculum to those texts. Until that is completed, the source gate remains `CHANGES_REQUIRED`; a 995 score is not claimed.
