# PFE 611 accessibility review — 2026-10-05

## Review scope

Fixture reviewed: `outputs/acos-university-study/specimens/truetype-tagged.pdf`  
Tools: bundled Python 3.12.14 with `pypdf`; veraPDF 1.30.2 reports in `reports/verapdf-1.30.2/`  
Review type: structured artifact inspection plus declared human-review checklist

This record separates machine and artifact evidence from human assistive-technology evidence. It does not claim PDF/UA conformance.

## Completed checks

- The document has one page and extracts a coherent character sequence with headings, body text, table text, ligature examples, and numeric content.
- The catalog has `/Lang en`, `/MarkInfo /Marked true`, `/StructTreeRoot`, `/Outlines`, and `/ViewerPreferences /DisplayDocTitle true`.
- The structure tree contains `/Document`, `/H1`, `/H2`, `/P`, `/Link`, `/Figure`, `/Table`, `/TR`, `/TH`, and `/TD` elements.
- The figure has alternative text: `Lime taper meets a white architectural A on Obsidian`.
- Table header cells have `/Scope /Column`; data cells reference header IDs through `/Headers`.
- The link annotation has a URI action to the W3C PDF3 technique page and a valid rectangle.
- The saved veraPDF PDF/UA-2 report records 2,532 passed checks and 7 failed checks for this fixture. The result is non-compliant.

## Human checks not completed

- No screen-reader session was available in this environment, so spoken reading order, announcement of table headers, figure-alt-text announcement, and link naming were not observed through assistive technology.
- No keyboard-only interaction session was available, so focus order and activation behavior were not verified.
- No human visual review at multiple zoom levels or print conditions was completed in this run.

## Disposition

The fixture demonstrates useful semantic structure and provides inspectable evidence for the teaching laboratory. The artifact review supports a bounded `IMPLEMENTED STUDY` claim. The missing human checks and seven failed PDF/UA-2 checks keep the accessibility gate open. The fixture must not be described as accessible-PDF conformant or production-ready.

