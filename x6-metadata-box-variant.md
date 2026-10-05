# Controlled PDF/X-6 metadata and page-box variant — 2026-10-06

## Purpose

The Rust probe first showed that the shaped-semantic specimen failed the implementation's PDF/X-6 checks for OutputIntents, `GTS_PDFXVersion`, TrimBox/ArtBox, and XMP identification. This experiment injected those fields with a disposable pypdf script and reran the implementation and independent validators.

## Construction

- Source: `shaping-fixture-heldout-shaped-semantic-tagged.pdf`.
- Added page `/TrimBox` and `/ArtBox` equal to the source MediaBox.
- Added Info `/GTS_PDFXVersion` and `/GTS_PDFXConformance` as `PDF/X-6`.
- Added an XMP packet with `pdfxid:GTS_PDFXVersion` and `pdfxid:GTS_PDFXConformance`.
- Added an embedded system sRGB profile under a `/GTS_PDFX` OutputIntent.
- Construction script: `/tmp/make-x6-metadata-variant.py`; it remains a disposable experiment and is not a production generator.

## Results

The patched Rust `pdf_oxide 0.3.78` probe reports:

```text
level=X6
is_compliant=true
detected_level=Some(X6)
errors=0
warnings=0
```

This proves only that the implementation's current checks accept this metadata/page-box shape. It does not prove ISO 15930-9 conformance.

Independent pypdf inspection preserved page count and extracted-text hash and confirmed the injected X6-facing keys. It also found that the pypdf rewrite dropped the source `/StructTreeRoot`. That is a material semantic regression. veraPDF consequently reports:

- PDF/UA-2: 1,720 passed / 7 failed rules and 548 passed / 11 failed checks.
- PDF/A-4: 102 passed / 7 failed rules and 423 passed / 450 failed checks.

The negative control is retained because it demonstrates why metadata-only PDF/X acceptance cannot be promoted to an accessible production artifact.

## Release state

`OBSERVED` implementation acceptance; `FAILED` semantic preservation and independent profile checks; `UNRELEASED`. The hard PDF/X-6 and 995/1000 source gates remain active.
