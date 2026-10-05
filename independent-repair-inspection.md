# Independent inspection of the repaired production fixture

**Inspection date:** 2026-10-05  
**Artifact:** `fixture-repaired2.pdf`  
**Independent paths:** pypdf 6.10.0, Poppler `pdftotext`, Poppler `pdffonts`, Poppler `pdftoppm`, and veraPDF 1.30.2.

## Observations

| Measurement | Observed result |
|---|---|
| SHA-256 | `c027477c49ffbb7f055a3c7ed37a804ef3423c3d6c1a0ad4faaa5f1a916f8c73` |
| PDF header | `%PDF-2.0` |
| Page count | 1 |
| Media box | 612 × 792 pt (US Letter) |
| Extracted text | 86 characters, including the fixture heading and three-line proof phrase |
| Fonts | Embedded Liberation Sans Bold and Liberation Serif; both subsetted and Unicode-mapped in Poppler output |
| Raster render | 612 × 792 px PNG at 72 dpi; rendered without an error |
| Structure tree | absent |
| Marked content metadata | absent |
| pypdf metadata dictionary | empty after the controlled repair |

The rendered page was inspected as a raster image and remains visually legible with the heading and proof phrase in the expected upper-left region. The geometry and text checks are independent of veraPDF’s PDF/A-4 result.

## Interpretation boundary

The independent checks establish byte identity, basic parse/extraction, font embedding, page geometry, and raster rendering for this fixture. They do not establish PDF/UA-2, PDF/X-6, screen-reader behavior, keyboard operation, reading order, or production-wide reliability. The absent structure tree and marked-content metadata are direct evidence for why the same file cannot be treated as an accessible tagged-PDF result even though veraPDF reports PDF/A-4 compliance.

Raw machine output is preserved in `independent-repair-inspection.json` and the adjacent veraPDF reports. The visual inspection is a human check of this one rendered page, not a substitute for a full accessibility review.
