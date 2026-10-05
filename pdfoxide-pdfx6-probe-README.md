# PDF Oxide PDF/X-6 capability probe — 2026-10-06

**Status:** `IMPLEMENTATION DIAGNOSTIC REACHED / PDF/X-6 CONFORMANCE UNVERIFIED`

A current open-source candidate, PDF Oxide `0.3.78`, was installed into a temporary target directory and exercised against both declared fixtures. Its public documentation states that PDF/X-6 is supported, but the installed Python API rejected the requested level before validation:

```text
ValueError: Unknown PDF/X level: '6'. Use 1a_2001, 3_2002, 4
```

The exact exception, package version, fixture hashes, and PDF/X-4 control-call representations are preserved in [`results.json`](results.json). The control call demonstrates that the package can enter its PDF/X validation API; it does not turn the PDF/X-4 control into a PDF/X-6 result.

This is an independent capability boundary, not a PDF/X-6 conformance result. The tool cannot be used to claim PDF/X-6 conformance or release-grade preflight from this environment. The public capability claim and the installed API behavior are recorded as a conflict for future investigation. A materially different Rust binding attempt is preserved in [`rust-binding-attempt.md`](rust-binding-attempt.md) and [`rust-x6-probe-2026-10-06.md`](rust-x6-probe-2026-10-06.md). A disposable Rust 1.99.0 toolchain reached `PdfXLevel::X6` after a copied-crate compile patch was required for the published 0.3.78 source; the heldout specimen was rejected with three implementation errors and one warning. The patch is preserved and is not treated as upstream or production-ready. A disposable release-binary check is preserved in [`cli-release-attempt.md`](cli-release-attempt.md); the CLI runs but exposes no validation command.

Sources inspected:

- [PDF Oxide PDF/X documentation](https://pdf.oxide.fyi/r/docs/compliance/pdf-x)
- [PDF Oxide PDF/X Rust source](https://docs.rs/pdf_oxide/latest/src/pdf_oxide/compliance/pdf_x/mod.rs.html)
- [PDF Association PDF/X index](https://pdfa.org/resource/iso-15930-pdfx/)
