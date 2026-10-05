# Firefox print-path capability recheck — 2026-10-06

## Purpose

The CSS pagination study requires an actual second print engine before it can claim cross-engine print behavior. This receipt records a direct capability probe of the installed Firefox application rather than treating its existing headless screenshot as a print-to-PDF result.

## Environment

- Executable: /Applications/Firefox.app/Contents/MacOS/firefox
- Reported version: Mozilla Firefox 111.0
- Input: reports/css-pagination-2026-10-05/fixture.html
- Attempted command shape: firefox --headless --no-remote --profile <profile> --print-to-pdf <output.pdf> file://<fixture.html>
- Observation bound: 30 seconds

## Observed result

The process emitted only normal headless/GFX diagnostics, created no out.pdf, and did not terminate within the 30-second observation bound. It was terminated after the bound.

Firefox's earlier --screenshot artifact remains a screen-media divergence observation, not a print-to-PDF result. This probe therefore does not establish a second print engine, PDF output, CSS cross-engine equivalence, or any PDF conformance profile.

## Gate effect

C-008 and C-009 remain IMPLEMENTED STUDY / LIMITED. The remaining valid routes are a supported Firefox print workflow, another independently controlled print engine, or an explicitly authorized environment change that supplies one. No claim is promoted from this failed capability probe.
