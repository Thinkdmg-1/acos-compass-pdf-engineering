# Dual PDF/A-4 + PDF/UA-2 + PDF/X-6 implementation experiment

**Date:** 2026-10-06  
**Purpose:** Controlled boundary experiment using the existing machine-passing PDF/A-4 + PDF/UA-2 specimen as the source.

## Inputs and method

Source: `reports/pfe611-tagged-repair-2026-10-06/pdfa4-ua2-experiment/combined-pdfa4-ua2.pdf`.

The generator `make-dual-pdfa4-ua2-pdfx6-variant.py` cloned the source page tree, retained its tagging and PDF/UA metadata, added TrimBox and ArtBox, retained the existing PDF/A output intent, appended a PDF/X output intent using the same embedded sRGB profile, replaced XMP with PDF/A-4, PDF/UA-2, and PDF/X-6 identifiers, and added PDF/X Info keys. This was a controlled implementation probe; it is not an ISO conformance claim.

## Results

| Check | Result | Evidence |
|---|---|---|
| Structure-preserving clone | Pass | `dual-pdfa4-ua2-pdfx6-variant-independent-check.json` |
| Page count preserved | Pass | independent pypdf check |
| Extracted text preserved | Pass; SHA-256 `141d3b01923d9daa3b78ff0985fe683048ada2af9e3040d801fe01455593711e` for source and variant | independent pypdf check |
| StructTreeRoot retained | Pass | independent pypdf check |
| Two output intents present | Pass; `/GTS_PDFA1` and `/GTS_PDFX` | independent pypdf check |
| PDF/UA-2, veraPDF 1.30.2 | Pass; 0 failed rules, 0 failed checks | `dual-pdfa4-ua2-pdfx6-variant-ua2.json` |
| PDF/UA-2, veraPDF 1.28.2 | Pass; 0 failed rules, 0 failed checks | `dual-pdfa4-ua2-pdfx6-variant-verapdf1282-ua2.json` |
| PDF/A-4, veraPDF 1.30.2 | Fail; 3 failed rules, 3 failed checks | `dual-pdfa4-ua2-pdfx6-variant-pdfa4.json` |
| Rust PDF/X-6 implementation probe | Fail; 2 errors and 2 warnings | recorded terminal output in completion audit |

## Failure interpretation

veraPDF identifies three PDF/A-4 failures: PDF/A-4 does not permit the added Info keys without a PieceInfo entry; if an Info dictionary is present it may contain only ModDate; and the file header remains `%PDF-1.3` rather than the PDF-2.n form required by the PDF/A-4 profile. The Rust PDF/X-6 implementation rejects the two existing unembedded fonts (`F4`, `F5`) under clause 6.3.5 and reports a missing Trapped key plus a link annotation without an appearance stream.

This experiment demonstrates that carrying markers and output intents across profiles does not establish simultaneous conformance. The PDF/UA-2 machine pass and structure preservation are useful evidence, but the artifact remains a failed dual-profile candidate. No PDF/A-4, PDF/X-6, or combined conformance claim is released from this result.
