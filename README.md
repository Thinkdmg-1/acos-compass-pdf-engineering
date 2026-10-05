# Experimental combined PDF/A-4 and PDF/UA-2 machine pass — 2026-10-06

**Status:** EXECUTED / PROFILE-SCOPED MACHINE PASS

This experiment starts from the bounded PDF/UA-2 repair copy and adds the minimum document-level metadata required for a PDF/A-4 validator run. It is a separate experimental artifact; the original tagged fixture and the earlier repair variants remain preserved.

## Controlled changes

- set the PDF header and catalog version to PDF 2.0;
- omitted the document information dictionary, which PDF/A-4 disallows here;
- added a deterministic trailer identifier;
- copied the embedded sRGB output intent and ICC profile semantics from the separately repaired PDF/A-4 fixture;
- added XMP identification for PDF/A-4 (`pdfaid:part=4`, `pdfaid:rev=2020`) and PDF/UA-2 (`pdfuaid:part=2`, `pdfuaid:rev=2024`).

The repair source is [`repair.py`](repair.py), and the resulting bytes are [`combined-pdfa4-ua2.pdf`](combined-pdfa4-ua2.pdf), SHA-256 `68b9fb2e89c450284c1a8294faa96ac0e1e03020a552ad3b94ab6cdfdfb8000a`.

## Fresh veraPDF 1.30.2 results

| Profile | Rules passed/failed | Checks passed/failed | Result |
|---|---:|---:|---|
| PDF/A-4 | 109 / 0 | 1,635 / 0 | **Compliant** |
| PDF/UA-2 + Tagged PDF | 1,727 / 0 | 2,539 / 0 | **Compliant** |

The JSON receipts and stderr captures are [`4.json`](4.json), [`4.stderr`](4.stderr), [`ua2.json`](ua2.json), and [`ua2.stderr`](ua2.stderr). The run used the pinned repository veraPDF 1.30.2 launcher and the recorded portable Temurin JRE from the parent runtime receipt.

## Independent preservation check

[`independent-check.json`](independent-check.json) uses a separate pypdf and Poppler path. Relative to the bounded PDF/UA-2 repair copy, it found equal page count, MediaBox, extracted-text digest, and 144 DPI raster digest. The experimental copy adds `/OutputIntents` and `/Version` as expected for PDF/A-4 metadata; it does not establish unchanged navigation, because the earlier bounded repair had already removed `/Outlines`.

## Limits and release meaning

This is one deliberately repaired specimen and two profile-scoped machine-validator passes. It does not prove that the source export is compliant, that the outline removal is an acceptable product decision, that a production exporter will reproduce the result, or that screen-reader, keyboard, visual, color-management, or second-reviewer checks pass. PDF/X-6 remains untested because the available validators do not expose a usable PDF/X-6 profile and the installed PDF Oxide API rejected level `6`. The repository therefore remains `INCOMPLETE / CHANGES_REQUIRED` under the 995 source gate.
