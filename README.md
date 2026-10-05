# PFE 605 exploratory pilot and analysis protocol — 2026-10-06

**Protocol ID:** `PFE605-2026-10-06-v1`  
**Status:** analysis protocol frozen before the follow-up measurement; the earlier three-case result is labeled exploratory because it preceded this protocol. The follow-up measurement is executed and retained in `followup-results.json`.

## Question

Within the existing one-page PDF specimen set, does changing the font/export treatment or requesting tagging alter page geometry, normalized extracted text, structure metadata, or raster output?

## Cases

- `cff-untagged`
- `truetype-untagged`
- `truetype-tagged`

Content, page size, and nominal layout are intended to remain constant. The treatment is font format and tagging request.

## Measurements fixed before the follow-up run

For every case, record:

1. SHA-256 and byte length;
2. page count and MediaBox dimensions;
3. PDF version, structure-tree presence, MarkInfo, language, and outline count;
4. normalized extracted text using NFKC plus whitespace collapse;
5. Poppler raster dimensions and SHA-256 at 1400-pixel target width;
6. exact tool versions and any warnings.

## Falsification conditions

The protocol is falsified for a “geometry preserved” claim if any page count or page-box dimension differs. It is falsified for a “semantic extraction preserved” claim if normalized critical text differs. It is falsified for a “visual output preserved” claim if raster dimensions differ or pixel hashes differ; pixel equality is sufficient for this fixture but pixel inequality alone does not explain the cause.

No inferential statistical test is planned for three deterministic specimens. The analysis reports exact observations and avoids p-values, generalization, and causal claims beyond this fixture.

## Boundaries

This protocol cannot assess complex-script shaping, screen-reader reading order, PDF/UA conformance, licensing, printer color, or universal renderer behavior. The first pilot result was collected before this protocol and is retained as exploratory rather than retroactively called preregistered.

## Follow-up result

The follow-up found identical page count, MediaBox, normalized-text hash, and critical-text presence across all three cases. The TrueType untagged and tagged cases also produced identical 1400-pixel Poppler raster hashes; the CFF raster hash differed. Tagging changed structure metadata (structure tree, MarkInfo, language, and outlines) without changing the normalized text or the tested TrueType raster. These are exact observations on three specimens, not universal font or accessibility conclusions.
