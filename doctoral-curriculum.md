# ACOS Compass doctoral curriculum: PDF engineering

**Status:** Curriculum created before further mastery claims  
**Date:** October 5, 2026  
**Domain:** PDF production, typography, document engineering, accessibility, color management, print production, pagination, and reproducible research  
**Model:** Four-year, 60-credit doctoral-equivalent research program with qualifying examination, candidacy examination, supervised research, public dissemination, and dissertation defense

This is the curriculum to execute. It is not an academic degree, university enrollment, or institutional credit. A real PhD requires an institution, faculty supervision, formal assessment, residency rules, and an awarded dissertation. This curriculum supplies the intellectual sequence and evidence gates those claims would require; it does not pretend to confer them.

## 1. Governing standard

ACOS Compass controls the method.

**Integrity / roots:** recover the earliest traceable foundations of a PDF concept, distinguish historical origin from earliest source found, and record uncertainty.

**Authenticity / trunk:** identify enduring principles rather than treating browser behavior, a vendor feature, or a fashionable workflow as a standard.

**Responsibility / branches:** separate syntax, rendering, typography, accessibility, color, print, archival, and research claims. A result in one branch cannot silently establish competence in another.

**Enrichment / fruit:** produce a useful artifact and a reusable, teachable method. Preserve the immediate benefit and the transferable lesson.

**Learning levels:** Instinct begins the work; Intellect investigates it; Discipline applies it repeatedly; Mastery requires repeatable performance on unfamiliar cases and a defensible contribution to knowledge.

Every claim moves through `OBSERVED → PROPOSED → APPROVED → IMPLEMENTED → VERIFIED`. A successful export is only an implementation event. A validator result is one evidence class. Visual, semantic, production, and human-use evidence remain distinct.

## 2. Doctoral outcome

At completion, the learner must be able to:

1. explain PDF 2.0 syntax and object semantics from source-level evidence;
2. generate and repair PDFs without losing editability, provenance, or semantic relationships;
3. reason about text shaping, font programs, CMaps, ToUnicode, tagging, reading order, and Unicode edge cases;
4. design pagination algorithms with explicit constraints and objectives, then prove or measure their behavior;
5. produce accessible documents against the applicable PDF/UA requirements and test them with automated and human methods;
6. manage color from source capture through display, conversion, proof, and print condition;
7. engineer PDF/X and PDF/A deliverables when the production or archival requirement calls for them;
8. design reproducible experiments, analyze uncertainty, distinguish statistical significance from practical importance, and publish complete evidence;
9. critique research and production claims at doctoral depth, including confounds, invalid generalization, and missing evidence;
10. make an original, defensible contribution that survives independent replication and oral examination.

## 3. Entry diagnostic and prerequisite repair

Before credit is assigned, complete a diagnostic in five parts:

- write a parser-backed account of one PDF object graph;
- reconstruct a page from primitive content operators;
- explain a font resource from glyph selection through Unicode extraction;
- produce a tagged one-page document and describe its unverified assumptions;
- design a controlled experiment with independent and dependent variables, confounds, and a falsification condition.

Any failed part triggers a foundation module. No failure is hidden by averaging. The diagnostic is repeated on an unfamiliar document after repair.

Prerequisites include discrete mathematics, linear algebra, probability and statistics, programming, data structures, color science foundations, typography, and technical writing. Missing mathematics or programming is repaired before advanced research rather than bypassed with a library call.

## 4. Four-year sequence

### Year 1 — foundations and qualifying knowledge (15 credits)

#### PFE 601: PDF syntax, object model, and rendering pipeline — 3 credits

Study PDF 1.7 and PDF 2.0 syntax, indirect objects, cross-reference structures, streams, filters, page trees, resource inheritance, content operators, graphics state, transparency, annotations, actions, metadata, encryption, incremental updates, linearization, and extensions.

**Laboratories:** build a minimal PDF writer; parse and reserialize an object graph; repair a broken cross-reference table; compare incremental and full rewrites; render with at least three independent engines; document behavior differences.

**Exam:** closed-source explanation of a supplied file's object graph and a live repair under time constraint.

#### PFE 602: Digital typography and font technology — 3 credits

Study letterform construction, metrics, kerning, shaping, OpenType tables, variable fonts, CFF, TrueType, CID fonts, CMaps, ToUnicode, Unicode normalization, bidirectional text, complex scripts, fallback, hinting, subsetting, licensing, and font interchange.

**Laboratories:** build a glyph inventory; compare Type3, CFF, and TrueType output; test ligatures, combining marks, right-to-left text, emoji, missing glyphs, and malformed mappings; use a shaping engine and compare it with PDF extraction.

**Exam:** diagnose why visually correct text is semantically wrong in a supplied PDF and specify the smallest repair.

#### PFE 603: Typography, layout, and information design — 3 credits

Study reading behavior, legibility, readability, line length, leading, hierarchy, Gestalt grouping, alignment, grids, visual variables, whitespace, tables, figures, captions, and decision-oriented information design. Read MIT 6.813 typography, layout, color, and accessibility materials plus graduate typography assignments.

**Laboratories:** reproduce a reference layout from separate editable elements; create a typographic system with measurable tokens; conduct a blind comparison; record visual defects independently from semantic defects.

#### PFE 604: Mathematics for pagination and document layout — 3 credits

Study dynamic programming, graph models, constraint satisfaction, optimization objectives, complexity, integer programming, line breaking, page breaking, floats, footnotes, widows, orphans, columns, spreads, and trade-offs between page count and reading cost.

**Laboratories:** implement baseline, greedy, dynamic-programming, and integer-programming paginators; compare objectives; construct adversarial fixtures; measure runtime and quality; reproduce a published pagination result.

#### PFE 605: Research methods and scientific reasoning — 3 credits

Study experimental design, qualitative artifact analysis, reproducibility, reliability, internal and external validity, sampling, measurement error, power, estimation, hypothesis testing, Bayesian reasoning, effect size, preregistration, and research ethics.

**Laboratories:** write a preregistered experiment; run a small pilot; analyze it with uncertainty intervals and effect sizes; write a negative result; reproduce a published analysis; audit a paper for p-value misuse using the ASA principles.

**Year 1 gate:** written qualifying examination, practical PDF examination, typography critique, pagination implementation, and research-methods proposal. A passing grade requires every hard-veto section to pass; a mean score cannot hide a failure in semantics, accessibility, provenance, or safety.

### Year 2 — advanced systems and qualifying research (15 credits)

#### PFE 611: Tagged PDF, PDF/UA, and assistive technology — 3 credits

Study structure trees, role maps, namespaces, marked content, logical order, artifacts, alternate descriptions, tables, formulas, annotations, language, headings, lists, links, forms, captions, page labels, and screen-reader interaction. Study PDF/UA-1 and PDF/UA-2 differences and current validator limitations.

**Laboratories:** create a tagged document from source semantics; inspect the structure tree; run veraPDF or another applicable validator; test with at least two screen readers or equivalent accessibility inspection paths; conduct keyboard-only review; test figures, tables, forms, and multilingual text.

**Gate:** no claim of accessibility conformance without a declared standard, validator version, human inspection protocol, defects, and disposition.

#### PFE 612: Color science and color-managed reproduction — 3 credits

Study radiometry, colorimetry, CIE XYZ, Lab, chromatic adaptation, metamerism, color appearance models, device profiles, transfer curves, gamut mapping, rendering intents, spectral behavior, ICC workflows, proofing, spot colors, overprint, trapping, and substrate effects.

**Laboratories:** characterize a display; build a profile-aware conversion; compare untagged and profiled assets; measure ΔE00; construct a soft proof and physical proof plan; analyze out-of-gamut colors; document viewing conditions.

#### PFE 613: PDF/X, prepress, and production engineering — 3 credits

Study PDF/X-4 and PDF/X-6, output intents, transparency, overprint, separations, trim/bleed/media boxes, effective image resolution, black generation, spot plates, imposition, trapping, proofing, RIP behavior, printer marks, and vendor acceptance specifications.

**Laboratories:** produce a press package for a declared condition; inspect separations; test overprint and transparency; generate a preflight report; compare a soft proof to a physical proof; record deviations and vendor decisions.

#### PFE 614: PDF/A, preservation, metadata, and digital forensics — 3 credits

Study PDF/A-1 through current applicable profiles, embedded files, XMP, identifiers, dates, provenance, checksums, signatures, encryption restrictions, fixity, migration, redaction, and evidentiary chain of custody.

**Laboratories:** create an archival package; validate it; perform controlled migration; recover provenance from a damaged file; test redaction by object and raster inspection; document what the archive can and cannot preserve.

#### PFE 615: Reproducible software and artifact engineering — 3 credits

Study deterministic builds, dependency pinning, source maps, test fixtures, property-based testing, fuzzing, differential rendering, CI, artifact manifests, version control, licensing, and secure handling of untrusted PDFs.

**Laboratories:** build a reproducible document pipeline; run a corpus through multiple renderers; fuzz parser boundaries safely; create a regression suite; publish source, environment, inputs, outputs, and known limitations.

**Year 2 gate:** qualifying examination. The candidate must defend a research question, complete a second-year research project, submit a publishable paper, and pass an oral defense of the experiment design, implementation, evidence, and limits.

### Year 3 — specialization, independent research, and candidacy (15 credits)

Select two specializations and one supporting field:

- accessible document systems;
- typography and font engineering;
- pagination and layout algorithms;
- color-managed print and imaging;
- digital preservation and forensics;
- browser and native export pipelines;
- document security, signatures, and privacy;
- multilingual and multiscript typesetting;
- computational design and visual quality measurement.

#### PFE 701: Specialization seminar I — 3 credits

Read ten primary papers or standards documents. For each, record the research question, method, evidence, assumptions, replication status, and transfer boundary. Lead two hostile seminars in which the strongest claim is challenged.

#### PFE 702: Specialization seminar II — 3 credits

Build and test a substantial system in the chosen branch. The system must expose its editable source, intermediate representations, receipts, and failure modes. A black-box result is insufficient.

#### PFE 703: Advanced statistics and measurement — 3 credits

Study mixed models, repeated measures, nonparametric methods, measurement theory, inter-rater reliability, psychophysics, multiple comparisons, missing data, causal inference, and Bayesian decision analysis.

#### PFE 704: Research practicum and teaching — 3 credits

Teach a complete module to another learner or simulated cohort. Prepare exercises, grading rubrics, examples, counterexamples, and a correction log. Teaching exposes whether the claimed knowledge is transferable.

#### PFE 705: Dissertation proposal and candidacy — 3 credits

Produce a literature review, gap statement, hypotheses or design questions, methods, preregistration, risk register, data-management plan, ethics review, anticipated contributions, and a staged schedule.

**Candidacy gate:** committee-style written proposal, oral defense, independent reviewer report, and a held-out practical task. The proposal must identify what would falsify the thesis.

### Year 4 — dissertation and defense (15 credits)

#### PFE 801: Dissertation research I — 6 credits

Collect evidence under the preregistered method. Preserve null results, deviations, source lineage, environmental details, and versioned artifacts. Any material method change triggers a documented amendment and re-review.

#### PFE 802: Dissertation research II — 6 credits

Complete analysis, replication, ablation studies, held-out tests, cross-renderer tests, and external critique. At least one result must be independently reproduced by a person or process not responsible for the original implementation.

#### PFE 803: Dissertation defense and public artifact — 3 credits

Submit a dissertation, source archive, data or fixtures, reproducibility instructions, visual appendix, accessibility statement, limitations, and public talk. Defend the work orally under hostile questioning about validity, evidence, contribution, and transfer.

**Doctoral completion gate:** the dissertation must make an original contribution, survive independent replication, be defensible in oral examination, and leave a reusable artifact or method. Completion of readings or production of a polished PDF is not enough.

## 5. Core source spine

The curriculum uses primary or authoritative sources wherever the claim matters:

- ISO 32000-2:2020 and its current approved errata, via the PDF Association standards register;
- ISO 14289-1 and ISO 14289-2 for PDF/UA;
- ISO 15930 series for PDF/X;
- ISO 19005 series for PDF/A;
- W3C CSS Paged Media and CSS Fragmentation specifications;
- W3C WCAG 2.2 and relevant techniques;
- MIT 6.813/6.831 User Interface Design and Implementation, including typography, layout, color, accessibility, and doctoral research-method readings;
- MIT MAS.962 Digital Typography graduate materials and all available problem sets;
- Donald Knuth and the TeX line-breaking and typesetting literature;
- Plass and later pagination research, including *Pagination Reconsidered*;
- RIT Color Science PhD core topics: color science, computational vision, color physics, visual-perception modeling, historical research, and research-publication methods;
- University of Reading Typography and Graphic Communication doctoral research and practice-informed research methods;
- PDF Association technical guidance, with every informative article checked against the controlling ISO edition;
- veraPDF and other validators as tools whose scope and version are recorded, never as a substitute for the standard or human review.

Books and papers are read in full where they underpin the dissertation, not represented by a link, abstract, or bibliography entry. Copyrighted works are used for study and cited, not reproduced wholesale.

## 6. Research infrastructure

Every experiment retains:

- a frozen research question and falsification condition;
- source register with version, date, scope, and checksum where practical;
- exact input corpus and licensing/provenance;
- source code and dependency lock;
- environment and renderer versions;
- units, tolerances, sampling plan, and uncertainty;
- raw output, derived output, and analysis script;
- visual renders and semantic extraction;
- independent review and dissent;
- defects, repairs, regressions, and superseded interpretations;
- a final claim ledger mapping every conclusion to evidence.

The minimum independent methods for a material PDF claim are: object-level inspection, rendered inspection, semantic extraction, and a second implementation or tool. Physical print claims add proof and production-condition evidence. Human usability claims add an ethical user study or a defensible alternative method.

## 7. Examination standards

The qualifying and candidacy examinations are cumulative and closed to unsupported confidence.

**Written examination:** explain, derive, compare, and critique. Questions include malformed PDFs, font mapping failures, page-tree inheritance, tagging defects, color-management failures, pagination objectives, experimental confounds, and standard-version conflicts.

**Practical examination:** repair an unfamiliar PDF, produce a tagged version, generate a declared print profile, run a reproducible experiment, and submit complete receipts within a fixed environment.

**Oral examination:** defend each conclusion, identify what would change the conclusion, distinguish standard requirement from local rule, and explain why a plausible alternative interpretation fails.

**Teaching examination:** teach a difficult concept, answer adversarial questions, and correct a student artifact without hiding uncertainty.

## 8. Dissertation requirements

The dissertation must investigate a real unresolved problem in PDF engineering. Suitable examples include:

- a reproducible, cross-renderer method for detecting semantic reading-order defects;
- a pagination objective that better captures reader navigation cost while preserving constraints;
- a font and shaping pipeline that preserves multilingual semantics through PDF export;
- a color-managed PDF-to-print workflow with measured uncertainty across devices and substrates;
- a practice-informed accessible document system tested with assistive technology;
- a preservation and forensic method for identifying meaningful changes across incremental PDF revisions.

The dissertation must state its contribution, compare against prior work, publish negative results, include an independent replication, and separate empirical findings from design recommendations.

## 9. Current execution state

The prior work satisfies only a foundation recovery slice: selected graduate readings, a small pagination model, local font/tag experiments, extraction correction, and bounded independent challenge. It is **not** Year 1 completion, not a qualifying pass, not candidacy, and not doctoral completion.

The next execution order is fixed:

1. complete the entry diagnostic and repair prerequisites;
2. complete PFE 601 through PFE 605 with full lab receipts;
3. sit the Year 1 written and practical qualifying examination;
4. continue into Year 2 only after the gate is passed;
5. select and begin a dissertation question only after the research-methods foundation is demonstrated.

No future response may call this curriculum “finished” merely because the file exists. A completed curriculum is a proposal. A doctoral result requires the gates above and evidence for each one.

## 10. Primary links

- [MIT graduate Digital Typography](https://ocw.mit.edu/courses/mas-962-digital-typography-fall-1997/)
- [MIT 6.813/6.831 course spine](https://web.mit.edu/6.813/www/sp17/)
- [MIT doctoral experiment design](https://web.mit.edu/6.813/www/sp17/classes/phd-experiment-design/)
- [MIT doctoral experiment analysis](https://web.mit.edu/6.813/www/sp17/classes/phd-experiment-analysis/)
- [RIT Color Science PhD](https://www.rit.edu/science/study/color-science-phd)
- [University of Reading doctoral research topics](https://www.reading.ac.uk/typography/phd/phd-research-topics)
- [University of Reading PhD proposal guidance](https://www.reading.ac.uk/typography/phd/develop-your-phd-proposal)
- [PDF Association standards](https://pdfa.org/pdf-standards/)
- [ISO 32000-2 errata](https://pdf-issues.pdfa.org/32000-2-2020/)
- [W3C CSS Paged Media](https://www.w3.org/TR/css-page-3/)
- [W3C CSS Fragmentation](https://www.w3.org/TR/css-break-3/)
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [veraPDF validation documentation](https://docs.verapdf.org/validation/)
