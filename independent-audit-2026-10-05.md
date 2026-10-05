# Independent challenge report — 2026-10-05

## Scope

This is an independent, bounded challenge of the saved PFE 601 pagination, font, tagged-PDF, and specimen exercises. It is not a degree examination, a PDF/UA certification, or a general claim of PDF engineering mastery.

## Reproduced evidence

- The pagination dynamic program agrees with a separate partition enumerator on 150 fresh positive-height cases.
- The reported 1,092 exhaustive fixtures is correct: `3^1 + … + 3^6 = 1,092`.
- All three specimen hashes match the saved exercise results.
- Normalized character tests succeed in all three specimens.
- Independent Poppler inspection confirms 792 × 612 pt landscape Letter geometry; tagging is reported only for the tagged specimen.
- The tagged specimen contains heading, paragraph, link, figure, and table structure. The figure has alternative text; table headers have `/Scope /Column` attributes.
- TTF specimens contain embedded `FontFile2` programs and `ToUnicode`. The CFF/WOFF specimen uses Type3 glyph procedures and `ToUnicode`; this is not evidence of a missing-font failure.
- Saved tagged and untagged TTF rasters are identical at the tested rendering settings. The independently reproduced CFF/TTF mean channel difference is real for that specimen.

## Required boundary corrections

1. The pagination early-break logic assumes nonnegative block heights. The exercise tests strictly positive heights but does not validate that input contract. Its objective is squared unused capacity with the final page exempt; it does not optimize page count, widows, floats, columns, or visual quality.
2. NFKC and whitespace normalization verify a normalized character sequence only. They erase distinctions in ligatures and whitespace and cannot verify exact code points, word spacing, line arrangement, or reading order.
3. Agreement between `pypdf` and `pdfplumber` is two parser interpretations of the same stored page box. It is not an independent physical measurement. Poppler supplies a third interpretation, not a print proof.
4. Useful tagging does not establish PDF/UA conformance. No complete PDF/UA validation, screen-reader examination, or reading-order acceptance occurred.
5. Raster equality is scoped to the tested TTF specimen and resolution. A mean channel delta does not establish equivalent contours, layout, or perceived appearance.
6. Course-reading statements require source locations and worked-answer provenance before they are presented as independently verified coursework.

## Defensible learning statement

> Completed and independently challenged a scoped set of university-study exercises in pagination, print units, font export, Unicode extraction, and tagged-PDF structure.

An earned degree, full-course completion, accessible-PDF certification, broad mastery, or live ACOS/Asgard implementation would exceed the evidence currently preserved.

