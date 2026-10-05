# Structure-preserving PDF/X-6 implementation variant — 2026-10-06

## Purpose

The first metadata variant reached the Rust implementation's X-6 acceptance path but lost `/StructTreeRoot` during a pypdf page rebuild. This experiment uses `PdfWriter(clone_from=reader)` so the original page tree and semantic structure remain intact while adding the implementation-facing PDF/X-6 fields.

## Construction

- Source: `shaping-fixture-heldout-shaped-semantic-tagged.pdf`.
- Writer path: pypdf clone of the complete source document; pages are modified in place.
- Added `/TrimBox` and `/ArtBox` equal to the MediaBox.
- Added Info `/GTS_PDFXVersion` and `/GTS_PDFXConformance`.
- Added XMP PDF/X identification, PDF/UA-2 identification (`pdfuaid:part=2`, `pdfuaid:rev=2024`), and `dc:title`.
- Added an embedded sRGB profile under `/GTS_PDFX` OutputIntent.
- Generator: `make-x6-metadata-preserving-variant.py`.

## Results

Rust `pdf_oxide 0.3.78` implementation diagnostic:

```text
level=X6
is_compliant=true
detected_level=Some(X6)
errors=0
warnings=0
```

veraPDF PDF/UA-2:

- 1.30.2: compliant, 1,727 passed rules / 0 failed, 805 passed checks / 0 failed.
- 1.28.2: compliant, 1,723 passed rules / 0 failed, 815 passed checks / 0 failed.

Independent pypdf inspection confirms:

- one page preserved;
- extracted-text SHA-256 preserved;
- `/StructTreeRoot` preserved;
- TrimBox, ArtBox, Metadata, and OutputIntents present.

Independent Poppler raster comparison at 144 DPI produced the same digest for source and variant:

```text
c1e23f0524249d02b4b0e71c237bf9a425377ba72a59da1dec139013bb6e3779
```

The same file fails the separate PDF/A-4 profile with 6 failed rules and 449 failed checks. That result is retained as a profile-interaction boundary; it does not negate the PDF/UA-2 or implementation-specific X-6 observations.

## Interpretation and release state

This is the strongest executable implementation result in the current lab: two veraPDF PDF/UA-2 releases, the Rust X-6 implementation diagnostic, independent semantic inspection, and independent raster comparison agree on the bounded specimen. It remains `OBSERVED / IMPLEMENTATION-VERIFIED / UNRELEASED` because the Rust validator is not an authorized ISO 15930-9 conformance authority, the complete normative clause map is still unavailable, PDF/A-4 is not satisfied, and human accessibility review and production preflight remain open.
