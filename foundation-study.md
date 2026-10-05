# ACOS Compass — PDF engineering university study

October 5, 2026 · Executed self-study and coursework record · Markdown source of truth

## Governing instruction

After three failures on the same task or capability, stop repeating the approach, undertake the deepest relevant university-level education available within the agent's capabilities, work exercises, and demonstrate the learning before retrying. Jeff explicitly activated that recovery here. This record documents actual reading, worked exercises, experiments, corrections and limits. It does not award academic credit or declare the whole field mastered.

The ordered plan is retained with the evidence package. This education task superseded the earlier production-audit plan. Caliber production revision is outside this study's scope.

## ACOS Compass application

The controlling source is Jeff's October 1 author addendum, recovered from the existing local ACOS material. Integrity is the roots: investigate the problem and trace available foundations. Authenticity is the trunk: distinguish enduring principles from temporary implementation advice. Responsibility is the branches: identify the domain and limits of transfer. Enrichment is the fruit: retain both the immediate benefit and knowledge that others can reuse.

Instinct is the capability already present; Intellect is explicit investigation; Discipline is applied work; Mastery requires demonstrated useful results and repeatable transfer. These stages remain distinct. Belief + Action = Faith; Faith × Consistency = Trust; Trust over Time = Certainty remain teaching relationships rather than numerical confidence calculations.

ACOS evidence states stay separate. A completed reading is OBSERVED study activity. An implemented exercise is not automatically a VERIFIED professional capability. The retained record carries scope, provenance, uncertainty and failures. Local learning does not constitute a change to live ACOS or Asgard runtime configuration.

## Actual university study

### Graduate digital typography: measurements and working systems

Read MIT MAS.962's syllabus, calendar and assignments 1 and 10. The course emphasizes making working typographic systems and taking responsibility for their effectiveness. Assignment 1 asks about em, point and pixel and exercises text transformation; assignment 10 develops word-based communication. Worked the measurement portion using contemporary CSS/print definitions. The original Java programming assignments and unavailable assigned book chapter were not completed. Their completion is not implied by this adaptation. [MIT MAS.962 syllabus](https://ocw.mit.edu/courses/mas-962-digital-typography-fall-1997/pages/syllabus/), [assignment 1](https://ocw.mit.edu/courses/mas-962-digital-typography-fall-1997/6db7f1d975e0712069ed2b2c4a24ed45_ps1.pdf), [assignment 10](https://ocw.mit.edu/courses/mas-962-digital-typography-fall-1997/ba5df9376d4f4ec91f34b06ac2ec1a79_ps10.pdf).

### Hierarchy and information design

Studied MIT's graphic-design reading: reduce unnecessary variation while preserving distinctions the reader needs. Hierarchy must have a task: establish sequence, grouping or importance. Size, value and position communicate order differently from hue. A successful export cannot demonstrate that the intended hierarchy survived. Applied this distinction to the learning method: inspect the perceived organization separately from technical structure. [MIT graphic design](https://web.mit.edu/6.813/www/sp17/classes/13-graphic-design/).

### Layout and grouping

Studied MIT's layout reading and answered its whitespace exercise: proximity explains grouping through relative space. Alignment reduces arbitrary positions; whitespace must distinguish internal relationships from separation between groups. Page fitting must preserve relationships such as heading/body, figure/caption and label/value. A blanket scale reduction can solve overflow while breaking readability. The pagination exercise below treats keep groups as indivisible input blocks. [MIT layout](https://web.mit.edu/6.813/www/sp17/classes/14-layout/).

### Typography and reader performance

Studied MIT's typography reading and answered its exercise. Legibility concerns recognition; readability concerns the whole reading task. Pair kerning and overall tracking differ. Leading affects the darkness and rhythm of a text field. Oldstyle and lining figures have different visual roles. Long measures and tightly packed lines need actual evaluation, not approval because a font was loaded. Historical claims about particular typeface classes are context-dependent; they were not adopted as universal laws. [MIT typography](https://web.mit.edu/6.813/www/sp17/classes/16-typography/).

### Color and reproduction

Studied MIT's color reading, especially perception, redundant cues, device gamuts and calibration. A numerical RGB triplet does not independently establish matching appearance on different devices. Small chromatic details require attention to luminance contrast and viewing conditions. Print behavior depends on the substrate, inks and output condition. Retained decision: web color tokens may remain exact sRGB values; a print conversion requires an identified production condition and proof rather than a guessed universal CMYK recipe. [MIT color](https://web.mit.edu/6.813/www/sp17/classes/15-color/).

### Universal access and semantics

Studied MIT's accessibility reading and answered its situational-impairment exercise. Design should accommodate variations in vision, motor ability, cognition and environment from the beginning. Keyboard operation, meaningful link names and programmatic relationships need explicit support. The older course is not a current conformance checklist. Cross-checked text spacing with WCAG 2.2: the requirement concerns avoiding loss when specified spacing is applied; it does not require every author to set those values as the default. [MIT accessibility](https://web.mit.edu/6.813/www/sp17/classes/19-accessibility/), [WCAG 2.2](https://www.w3.org/TR/WCAG22/#text-spacing).

### Doctoral research methods: causal diagnosis

Studied MIT's doctoral experiment-design reading through controlled experiments and validity. An independent variable is manipulated; dependent variables are measured. Confounding can prevent attribution. Internal validity, external validity and reliability answer different questions. Answered the reading exercise and applied the framework to a PDF font/tagging experiment: keep content and geometry fixed, vary a single treatment, inspect output objects, then restrict conclusions to the tested implementation. No reader study or human usability finding was fabricated. [MIT doctoral experiment design](https://web.mit.edu/6.813/www/sp17/classes/phd-experiment-design/).

### Doctoral research methods: critical interpretation

Studied MIT's experiment-analysis reading through significance, t tests, pairing and ANOVA. Its pedagogical shorthand sometimes overstates what a p-value means. Cross-checked against the American Statistical Association: a p-value is not the probability the hypothesis is true or the probability that chance alone produced the data. Significance does not establish effect size or practical importance. Deterministic PDF structure and geometry checks in this study do not need decorative significance testing. [MIT doctoral experiment analysis](https://web.mit.edu/6.813/www/sp17/classes/phd-experiment-analysis/), [ASA statement](https://www.amstat.org/asa/files/pdfs/P-ValueStatement.pdf).

### University research: pagination as a constrained problem

Read the introduction, page model, objectives and algorithm sections of Brüggemann-Klein, Klein and Wohlfeil's 1996 *Pagination Reconsidered*. The optimization objective changes both the result and computational problem. The paper considers ordered text/figure streams, citations, page heights, elastic space and legal endings. Its page-turn objective is different from minimizing squared figure distances. The exercise below is a deliberately smaller contiguous-block model; it is not a reproduction of their algorithm. The paper's descriptions of 1990s software are historical evidence, not current product evaluations. [University research paper](https://d-nb.info/1149749830/34).

## Worked exercises and evidence

### 1. Units: predict, then independently measure

At the CSS print mapping, 96 reference pixels equal one inch; 72 PDF points equal one inch when UserUnit is 1. Therefore 1056 × 816 CSS pixels predict an 11 × 8.5 inch page, or 792 × 612 points. A 24px font predicts 18pt; an em in font sizing follows the relevant font size, not the measured width of an M glyph. A CSS reference pixel is not necessarily one hardware pixel. [CSS absolute units](https://www.w3.org/TR/css-values-3/#absolute-lengths).

Measured three exported specimens with two PDF libraries: pypdf's page box and pdfplumber's page geometry both returned 792 × 612pt. UserUnit was 1. Predetermined tolerance: 0.01pt. This verifies the page mapping for these files; the shared PDF specification means two parsers are complementary inspection rather than wholly independent physics. Text size predictions still require inspecting actual exported text transforms when typography measurements matter.

### 2. Constrained pagination: implement and challenge

Implemented a dynamic program for indivisible contiguous blocks and a separately written exhaustive cut enumerator. Preconditions are positive integer heights and positive capacity; the teaching functions do not validate unsupported inputs. The objective was fixed in advance: sum squared spare capacity on non-final pages; final-page spare capacity is free. Tested every length-one-through-six sequence drawn from synthetic heights 2, 5 and 8 at capacity 10: **1,092 fixtures**. Both methods returned equal optimal costs for every fixture. Also tested an oversized block: infeasible, rather than silently scaled or clipped. A separate reviewer challenged the solver with an independently written partition recursion on **150 additional positive-height cases**, capacities 4–20 and lengths 1–8; all costs agreed.

The result verifies that implementation against enumeration within that small model. It does not establish aesthetic quality, the paper's O(mn) algorithm, float placement, multicolumn balancing, citation order or production suitability. The height units are synthetic teaching data, not project metrics. The model demonstrates why constraints and objectives must be stated before claiming an optimum.

### 3. PDF fonts and semantic structure: controlled local experiment

Three purpose-built one-page specimens kept content and geometry constant. Tested CFF WOFF with untagged export, TrueType with untagged export, and TrueType with tagged export. Inspected PDF objects and rendered through Poppler. In this local Chromium export, the CFF case used embedded Type3 glyph descriptions with ToUnicode; TrueType cases used embedded CIDFontType2 programs with ToUnicode. Type3 is not synonymous with missing embedding.

The tagged specimen contained a structure tree, Marked=true, document language and two outline entries. Tagged and untagged TrueType renders were pixel-identical at the tested resolution. The CFF and TrueType renders differed slightly. This demonstrates that visible equality cannot prove equivalent semantics and a font format change cannot be presumed visually identical. It does not establish PDF/UA conformance, a correct complete reading order, or behavior in every viewer.

### 4. Preserve and correct the failed check

The first character-preservation assertion failed. Inspection showed the exporter inserted a line break before the digits, and a ligature could be represented as a Unicode ligature character. The repaired semantic check applies NFKC normalization and whitespace normalization. It passed for all three specimens. That normalization deliberately cannot verify original spacing or reading sequence; separate checks must do that. The original failure and repair are preserved in the receipt.

## Advanced PDF knowledge retained

PDF is a page-description format whose rendered appearance, object structure, text meaning and production conditions must be evaluated separately. A parser accepting a file establishes much less than a professional handoff. The normative spine is ISO 32000-2; specifications and errata control over informal summaries. [PDF 2.0 specification access](https://pdfa.org/resource/iso-32000-2/).

For accessibility, Unicode mapping, semantic tagging, logical order, language, alternatives, navigation and relationships all matter. Having tags is an implementation observation. A conformance decision requires the applicable PDF/UA rules, automated checks and human checks that machinery cannot resolve. PDF/UA-2 is ISO 14289-2:2024; a Chromium tagging option does not confer that standard. [PDF/UA-2](https://pdfa.org/iso-14289-2-pdfua-2/), [veraPDF validation scope](https://docs.verapdf.org/validation/).

For print, page boxes, bleed, effective image resolution, font licensing/embedding, color spaces, output conditions, transparency and overprint require explicit production requirements. PDF/X is a family of constraints, not a generic quality adjective. PDF/X-6 is based on PDF 2.0. A browser PDF suitable for screen review must not be silently renamed a press master. [PDF/X and related subset standards](https://pdfa.org/the-new-pdf-2-0-and-subset-standards/).

Effective image resolution is source pixels divided by placed inches; the file's nominal DPI metadata is insufficient. Enlarging pixels does not recover lost photographic detail. Vector artwork should remain purpose-built and editable where possible. Brand fidelity still requires inspection against the approved source rather than a successful preflight.

Output intents describe an intended reproduction condition; adding an intent does not itself convert the document's colors. Source profiles, rendering intent, output profile and actual printer conditions must be handled coherently. Spot colors and specialty finishes require vendor-specific separation and proof. These topics were studied from primary technical references; no physical press proof or broad color-science experiment was performed. [Adobe output intents](https://helpx.adobe.com/acrobat/using/output-intents-pdfs-acrobat-pro.html).

Pagination and print CSS must address explicit page size, break rules, overflow, keeps, widows/orphans, font readiness and background output. A page-break declaration cannot guarantee that all content fits. Render the actual exported pages and inspect dense material, not only the cover. Freeze the export settings and artifact digest before claiming verification. [CSS paged media](https://www.w3.org/TR/css-page-3/), [CSS fragmentation](https://www.w3.org/TR/css-break-3/).

## Return-to-work evidence boundary

Demonstrated here: a unit conversion checked in actual PDFs, a small pagination optimizer checked against enumeration, a controlled export comparison, critical reading, and a corrected semantic-character check. The standing recovery procedure and these scoped lessons are retained for reuse.

Not demonstrated here: comprehensive mastery of PDF engineering, completion of a university degree or entire course, reader-performance improvements, universal renderer compatibility, PDF/UA or PDF/X conformance, professional print proofing, or a corrected Caliber production release. Those claims remain withheld. A future retry must first demonstrate repair of its relevant failure on a minimal reference-matched specimen and an unfamiliar case. The relevant deficiency—not the volume of reading—determines readiness.

The durable result is a changed method with inspectable evidence: diagnose before retrying; trace sources; work the exercise; measure actual output; challenge the result; retain only the conclusion demonstrated.
