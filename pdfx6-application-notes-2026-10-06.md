# PDF/X-6 application-notes study and test-plan receipt — 2026-10-06

**Status:** EXECUTED / INFORMATIVE CORROBORATION / TEST PLAN READY

## Source custody

- **Source ID:** S-024
- **Publisher:** Association for PRINT Technologies (APTech), US TAG to ISO/TC 130
- **Title:** *A Practical Guide to Implementing and Using the PDF/X-6 Standard*
- **Public source:** <https://printtechnologies.org/standards/files/Application_Notes_PDF_X6_final.pdf>
- **Retrieved/rechecked:** 2026-10-05
- **Document properties:** 22 pages; PDF 1.6; file size 1,840,683 bytes
- **Downloaded-file SHA-256:** `54319aa01fac9ccdd581f1bb5f4dbe2912be608d24530de637718e5274e47a45`
- **Class:** INDUSTRY APPLICATION NOTES / INFORMATIVE GUIDANCE

The document itself states that it supplements ISO 15930-9, is subject to revision, and is **not a substitute for the full standard**. It also states that ISO standards take precedence if a conflict exists. Those limitations are part of this receipt, not footnotes added later.

## Direct study observations

A local Poppler extraction and the public PDF text were inspected. The application notes provide a usable implementation map for the PFE 613 laboratory:

- PDF/X-6, PDF/X-6p, and PDF/X-6n are treated as the three ISO 15930-9:2020 conformance levels, all using PDF 2.0.
- PDF/X-6 is complete exchange with required print resources contained in the file; PDF/X-6p uses externally referenced gray/RGB/CMYK ICC profiles; PDF/X-6n uses externally referenced n-colorant profiles.
- The notes describe document-level and page-level output intents, DPart metadata, multiple output intents, transparency, optional-content groups, annotations with defined appearances, and interactive forms/digital signatures as PDF/X-6 implementation areas.
- The notes describe workflow stages including native-source export, preflight, RIP/rendering, proofing, customer sign-off, imposition, and press output.
- The case study records page-specific dimensions, bleed, output intents, and different printing processes as inputs to a multi-component PDF/X-6 job.

These are implementation and workflow observations, not normative clause claims. The exact ISO requirements, exceptions, and conformance tests remain unavailable without authorized ISO 15930-9 text.

## Bounded PFE 613 test plan derived from the notes

| Test unit | Frozen input or condition | Evidence to collect | Current state |
|---|---|---|---|
| Level identity | PDF/X-6, PDF/X-6p, PDF/X-6n declared before export | metadata and profile-selection receipt | **READY / no validator** |
| PDF 2.0 baseline | Header/version and PDF 2.0 features | object inspection plus independent parser | **READY** |
| Output intents | one document-level and one page-level intent where supported | catalog/page object inspection, ICC digest, renderer comparison | **READY / no X-6 validator** |
| Complete versus external profile | embedded ICC versus controlled external-profile set | file-set manifest, profile digest, path-resolution failure test | **READY / no X-6 validator** |
| DPart/page metadata | page-level DPart tree fixture | object graph and metadata extraction | **READY / no X-6 validator** |
| Appearance-bound annotations | annotation with explicit appearance stream | object inspection and raster comparison | **READY / no X-6 validator** |
| Production path | declared printer condition, proof, RIP/preflight, sign-off | vendor receipt and proof measurements | **UNAVAILABLE** |

The test plan is intentionally frozen as a plan, not reported as executed conformance. A usable X-6-capable validator and an authorized profile map are required before any row can become a conformance result.

## Independent challenge and release meaning

The source's explicit “not a substitute” language was independently checked against the APTech standards page, which describes the application notes as supplementary to ISO 15930-9 and directs implementers to the purchased standard for authoritative requirements. This source improves implementation context and test design, but it does not remove the PDF/X-6 hard veto or raise the numerical score.
