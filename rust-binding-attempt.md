# PDF Oxide Rust X-6 binding attempt — 2026-10-06

**Status:** VERIFIED UNAVAILABLE ON THIS HOST / FALLBACK PRESERVED

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

This is a verified host-capability boundary for the alternate Rust path. It is not a Rust API failure and not a PDF/X-6 conformance result. The Python wheel rejection remains the only executed PDF Oxide binding result. The public Rust source still supplies source-level corroboration that an X6 enum exists, while the language-binding conflict and missing Rust toolchain prevent an accepted X-6 validation request in this environment.

## Fallback and stop condition

The Python control path, current Rust-source inspection, veraPDF profile inventory, and PDF/X-4 control result remain preserved. Installing a compiler or changing the host toolchain would be an external environment change; no silent installation was performed. A future run needs a pinned Rust toolchain or a released executable that accepts `PdfXLevel::X6`, followed by independent challenge against the authorized ISO 15930-9 requirement map.
