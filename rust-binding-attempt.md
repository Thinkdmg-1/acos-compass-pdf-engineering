# PDF Oxide Rust X-6 binding attempt — 2026-10-06

**Status:** VERIFIED API REACHED THROUGH DISPOSABLE RUST TOOLCHAIN; SPECIMEN REJECTED BY IMPLEMENTATION CHECKS

## Frozen question

Can the current PDF Oxide Rust API, which publicly declares `PdfXLevel::X6`, accept a PDF/X-6 validation request against the preserved combined specimen?

## Inputs and method

- Input specimen: `reports/pfe611-tagged-repair-2026-10-06/pdfa4-ua2-experiment/combined-pdfa4-ua2.pdf`.
- Candidate version: `pdf_oxide = "0.3.78"`.
- Intended source-level call:

```rust
use pdf_oxide::api::Pdf;
use pdf_oxide::compliance::{validate_pdf_x, PdfXLevel};
let mut pdf = Pdf::open(path)?;
let result = validate_pdf_x(&mut pdf.document()?, PdfXLevel::X6)?;
```

- A clean temporary Cargo project was created outside the repository. No dependency or system installation was changed.
- The build/run attempt stopped before dependency resolution because this host has no `cargo`, `rustc`, or `rustup` executable on the command path, and the bounded search of the local runtime/tool directories found none.

Observed terminal result:

```text
command not found: cargo
```

## Interpretation

The first clean build attempt exposed a dependency compile defect in the published 0.3.78 source (`DocumentIR` construction omitted the newly required `defined_names` field). To test the API boundary without changing the published source claim, a disposable copy was patched only with `defined_names: Vec::new()` and used under Cargo `[patch.crates-io]`; the patch is preserved as an experiment and is not a production dependency. With Rust 1.99.0 in `/tmp`, the probe compiled and reached `validate_pdf_x(..., PdfXLevel::X6)`. The heldout shaped-semantic specimen was rejected with three errors and one warning: missing OutputIntents (6.2.2), missing Info `GTS_PDFXVersion` (6.7.5), missing TrimBox/ArtBox (6.1.1), and missing XMP pdfxid identification (6.7.2). This demonstrates executable X-6-shaped checks, not ISO conformance: the published implementation’s coverage and the authorized ISO 15930-9 requirement map still require independent verification.

## Fallback and stop condition

The Python control path, original unpatched compile failure, disposable toolchain provenance, source inspection, veraPDF profile inventory, and PDF/X-4 control result remain preserved. The X-6 result is a bounded implementation diagnostic and does not remove the PDF/X-6 hard veto. Future work still requires an authorized ISO 15930-9 requirement map, independent PDF/X validator agreement or documented scope, and production-profile verification.
