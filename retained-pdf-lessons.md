# PDF recovery: scoped retained learning

Study evidence: October 5, 2026, Caliber-related university recovery. The full record is at `/Users/quickwhitt/Documents/Codex/2026-10-05/referenced-chatgpt-conversation-this-is-an/outputs/acos-university-study/University-Study-Record.md`. Treat the absolute path as historical provenance; recover it if available, and use primary sources for current decisions.

## Useful foundations

- MIT graduate MAS.962 Digital Typography, syllabus and assignments 1/10: https://ocw.mit.edu/courses/mas-962-digital-typography-fall-1997/ . Assignment measurements were adapted; the Java coursework and assigned book were not completed.
- MIT 6.813/6.831 typography, layout, color, accessibility, doctoral experiment design/analysis: https://web.mit.edu/6.813/www/sp17/ . Actual reading and worked conceptual answers; older pedagogical shortcuts were critically checked rather than universally adopted.
- University pagination research: https://d-nb.info/1149749830/34 . Studied introduction, constraints, objective and algorithm. Local optimizer was a smaller contiguous-block teaching adaptation.
- Normative foundation and conformance sources: https://pdfa.org/resource/iso-32000-2/ ; https://pdfa.org/iso-14289-2-pdfua-2/ ; https://www.w3.org/TR/WCAG22/ ; https://www.w3.org/TR/css-page-3/ ; https://www.w3.org/TR/css-break-3/ . Verify applicable version and requirements when using.

## Demonstrated lessons

1. A loaded source font does not prove the PDF font representation. Inspect exported resources recursively, including Type3 glyph procedures, descendant font descriptors and Unicode mapping. Type3 alone does not mean unembedded.
2. One local tagged/untagged TrueType specimen had identical rasters but different semantics. Visual inspection and semantic inspection are separate requirements. Tags alone do not prove PDF/UA conformance.
3. Print CSS units predicted page geometry and two parsers plus Poppler agreed with the exported page box. This is file-geometry evidence, not a physical print measurement.
4. NFKC and whitespace normalization can check a semantic character sequence while masking actual spacing, ligature code points and reading order. Retain separate tests for those concerns.
5. A small positive-integer block pagination optimizer matched exhaustive enumeration on 1,092 fixtures and an independent challenge on 150 additional cases. This is evidence for the stated model and objective, not production pagination or aesthetic quality.
6. Color intent, color conversion and physical reproduction differ. Effective image ppi depends on placed size. Screen review does not establish press suitability.
7. The relevant reference governs visual fidelity. Do not crop composite references into production assets. Recreate separate editable elements and inspect the smallest specimen before expansion.

## Return criterion

Identify the actual repeated failure. Apply the corresponding principle to a minimal reference-matched specimen and a fresh case. Demonstrate the specific repair before scaling. Full course completion, degrees, broad PDF mastery, PDF/X or PDF/UA conformance, physical print proof, and corrected Caliber release were not established by this study.
