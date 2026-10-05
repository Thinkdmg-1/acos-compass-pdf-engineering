# PDF preflight capability inventory

**Date:** 2026-10-05  
**Purpose:** independently determine whether the current host can execute the required PDF/X-6 preflight step.

## Method

A fresh shell checked the executable search path for `verapdf`, `veraPDF`, Ghostscript (`gs`), `qpdf`, MuPDF (`mutool`), `pdfcpu`, `cpdf`, callas, and pdfToolbox. It also searched installed Adobe InDesign resource trees for a standalone preflight executable. Paths and search results were recorded rather than inferred from application names.

## Result

All checked command-line tools were unavailable. Adobe InDesign resource directories were present, but the bounded resource search found no standalone PDF/X preflight executable or callable profile runner. The installed application presence is therefore not treated as a PDF/X-6 validation capability.

## Release interpretation

No PDF/X-6 preflight was executed. This receipt confirms the capability boundary only; it is not evidence that the fixture passes or fails PDF/X-6. The claim remains `UNTESTED` until an engine that explicitly supports ISO 15930-9:2020 PDF/X-6 is authorized and available, with its profile selection and complete report preserved.
