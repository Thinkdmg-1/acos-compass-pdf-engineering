# Partial human-review receipt

**Date:** 2026-10-05  
**Fixture:** `reports/production-pdfa4-2026-10-05/fixture-repaired2.pdf`  
**Disposition:** `PARTIAL / NOT A PDF/UA CONFORMANCE REVIEW`

## Executed visual check

The one-page fixture was rendered independently with Poppler `pdftoppm` at 144 DPI to a 1224 × 1584 PNG and at 288 DPI (a 200% inspection render) to a 2448 × 3168 PNG. Both full-page images were inspected. The page visibly contains the heading `PFE Production Fixture`, the subtitle `PDF/A-4 production-path experiment.`, and the line `Precision. Progress. Proof.` on a white page with no clipping, raster corruption, or unexpected overflow visible at this scale.

Because `pdfinfo` reports one page, this covers the complete page set at the two recorded render resolutions. The check does not establish high-contrast behavior, assistive-technology behavior, or PDF/UA conformance.

## Checks not executed

- Keyboard traversal through a viewer was not treated as complete because no controlled viewer test script and focus-order receipt were captured.
- Screen-reader reading order and announcements were unavailable in this environment.
- A second human reviewer and held-out export were not available.

These missing checks remain `UNAVAILABLE`/`MISSING` in the source-quality gate. The partial visual observation is retained to prevent the stronger but unsupported claim that no human review occurred.
