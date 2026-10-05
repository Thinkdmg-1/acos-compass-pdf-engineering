# PDF Oxide PDF/X-6 current-source recheck — 2026-10-06

**Status:** EXECUTED / TOOL-CONFLICT PRESERVED

## Public source inspection

- **Source:** PDF Oxide `pdf_x/types.rs` on docs.rs
- **URL:** <https://docs.rs/pdf_oxide/latest/src/pdf_oxide/compliance/pdf_x/types.rs.html>
- **Retrieved/rechecked:** 2026-10-05
- **Published crate shown by docs.rs:** `pdf_oxide 0.3.78`

The current public Rust source directly declares `PdfXLevel::X6` and maps it to:

- `ISO 15930-9:2020` (source lines 38–53);
- required PDF version `2.0` (lines 56–63);
- transparency and layers allowed for X6 (lines 66–82);
- `GTS_PDFXVersion` value `PDF/X-6` (lines 94–107);
- parsing of the string `PDF/X-6` to `PdfXLevel::X6` (lines 115–129).

The public module-level source also describes PDF/X-6 as based on PDF 2.0 and lists the PDF/X validation module, but its summary table does not yet enumerate X6. That documentation inconsistency is retained rather than silently reconciled.

## Local implementation challenge

The separately preserved local probe installed the published Python wheel `pdf_oxide 0.3.78` and attempted the claimed X-6 path. The Python API rejected level `'6'` with:

```text
ValueError: Unknown PDF/X level: '6'. Use 1a_2001, 3_2002, 4
```

The same probe successfully reached the X-4 control path and captured its scoped validation errors. The exact environment, source documentation, exception, and control result remain in the parent [`README.md`](README.md), `run.py`, and `result.json`.

## Interpretation

The current public Rust source demonstrates that the codebase contains an X6 enum, but it does not prove that the Python wheel exposes or implements the same path, nor that either implementation correctly enforces ISO 15930-9:2020. The observed language-binding conflict means this repository must continue to mark PDF/X-6 preflight as **UNTESTED / TOOL-CONFLICT RECORDED** until a validated release accepts an X-6 request and its output is independently challenged against authorized profile requirements.
