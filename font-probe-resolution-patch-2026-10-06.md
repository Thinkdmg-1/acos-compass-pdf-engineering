# PDF/X-6 font-probe resolution patch — 2026-10-06

## Purpose

Resolve the previously observed conflict between the PDF Oxide PDF/X-6 probe (which reported F4/F5 as unembedded) and independent object inspection (which found descendant /FontFile2 streams) without changing the specimen PDF.

## Method

The published PDF Oxide 0.3.78 source was copied to the disposable workspace /tmp/pdf_oxide-0.3.78-patched-20261006. A minimal source patch was applied only to the PDF/X font check in src/compliance/pdf_x/validator.rs: when a page-resource font has subtype /Type0, the checker now resolves its first /DescendantFonts CIDFont and checks that descendant's /FontDescriptor for /FontFile, /FontFile2, or /FontFile3. The patch does not alter the PDF, the PDF/X rules, metadata, or any other validator rule.

The probe was rebuilt in the disposable Rust workspace /tmp/pdfoxide-probe-20261006-v2 with the patched crate pinned through Cargo's local [patch.crates-io] override.

## Inputs and hashes

- Specimen: dual-pdfa4-ua2-pdfx6-xmp-only-v5-patched.pdf
- Specimen SHA-256: a43bda6ac77a68c4070079fd8c7b34245a849644ae8904e62fe720a47d8c9e24
- Patched validator source SHA-256: baa83261a85ea92aa73abb66f89cc53493fa69135055c5faa3c2bdb9830b335a
- Patched probe binary SHA-256: 3d5a3ad4e9d4d7f769c612893ba6837c38a8e30f709085b3fa23577a66f48e21

## Result

The unmodified probe receipt reported three errors: missing /GTS_PDFXVersion, F4 unembedded, and F5 unembedded. The patched probe reports:

```text
level=X6
is_compliant=false
detected_level=Some(X6)
errors=1
ERROR XMETA-007 GTS_PDFXVersion key is required in Info dictionary clause=Some("6.7.5")
warnings=2
WARN XMETA-004 Trapped key should be present in Info dictionary clause=Some("6.7.5")
WARN XANNOT-001 Link annotation should have appearance stream clause=None
stats pages=1 fonts=2 embedded_fonts=2 images=0 annotations=1
```

The independent pypdf object inspection remains consistent: F4 and F5 are Type0 fonts whose descendant font descriptors contain decoded /FontFile2 streams of 19,208 and 26,564 bytes. The PDF bytes and specimen hash did not change.

## Interpretation and limit

This resolves the specific implementation-resolution conflict: the two font errors were caused by the unmodified probe not following the Type0-to-descendant font graph. The patched run is a source-level diagnostic and independent implementation check. It is not an ISO PDF/X-6 certification, does not cure the remaining /GTS_PDFXVersion/Trapped/annotation findings, and does not replace an authorized normative clause review or production preflight.
