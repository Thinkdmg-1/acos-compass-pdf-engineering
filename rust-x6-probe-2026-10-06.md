# Disposable Rust PDF/X-6 probe — 2026-10-06

## Question

Can the published `pdf_oxide = 0.3.78` Rust API accept `PdfXLevel::X6` and execute its validator against the shaped semantic held-out PDF?

## Reproducible inputs

- Crate requested: `pdf_oxide = 0.3.78` from crates.io.
- Rust toolchain: stable `rustc 1.99.0` for `x86_64-apple-darwin`, installed under `/tmp/acos-rustup-20261006` with Cargo under `/tmp/acos-cargo-20261006`.
- Original clean build: failed in published source because `src/converters/pdf_to_ir.rs:194` initializes `DocumentIR` without the required `defined_names` field.
- Disposable patch: copied the crate to `/tmp/pdf_oxide-0.3.78-patched-20261006` and added `defined_names: Vec::new()` only so the API boundary could be exercised. This patch is not asserted as upstream or production-ready.
- Probe source: `/tmp/pdfoxide-probe-20261006-v2/src/main.rs`.
- Input specimen: `reports/pfe602-pdf-fixture-lab-2026-10-06/shaping-fixture-heldout-shaped-semantic-tagged.pdf`.

## Executed result

The patched probe compiled and executed the public call:

```rust
let mut doc = PdfDocument::open(path)?;
let result = validate_pdf_x(&mut doc, PdfXLevel::X6)?;
```

Observed output:

```text
level=X6
is_compliant=false
detected_level=None
errors=3
ERROR XMETA-001 OutputIntents array is required for PDF/X clause=Some("6.2.2")
ERROR XMETA-007 GTS_PDFXVersion key is required in Info dictionary clause=Some("6.7.5")
ERROR XBOX-001 Either TrimBox or ArtBox is required for PDF/X clause=Some("6.1.1")
warnings=1
WARN XMETA-006 XMP metadata missing pdfxid:GTS_PDFXVersion identification clause=Some("6.7.2")
stats pages=1 fonts=0 embedded_fonts=0 images=0 annotations=0
```

## Interpretation

This is executable implementation evidence that the Rust API exposes an `X6` level and runs a validator. It is not evidence that `pdf_oxide` implements every ISO 15930-9:2020 requirement, nor that the specimen is PDF/X-6 compliant. The specimen is correctly recorded as rejected by the implementation’s checks. The compile patch and the validator’s own clause labels are implementation evidence; they do not replace an authorized normative text and clause map.

## Provenance

The unpatched source compile failure and the patched experiment are both preserved. The dependency was never installed into the host environment; all Rust state is disposable under `/tmp`. The source package’s exact contents are available in Cargo’s registry cache for this run; the public dependency is pinned by `Cargo.lock` in the temporary probe.
