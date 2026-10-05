# PDF-2.0 header-only boundary variant

This controlled variant starts from `dual-pdfa4-ua2-pdfx6-variant.pdf` and changes only the first header from `%PDF-1.3` to `%PDF-2.0`. It tests the narrowest repair for the PDF/A-4 header failure while preserving the clone, tagging, metadata, and output intents.

Results:

- PDF/UA-2, veraPDF 1.30.2: pass, 0 failed rules/checks.
- PDF/A-4, veraPDF 1.30.2: still fails 2 rules/checks. The remaining failures are the Info/PieceInfo relationship and PDF/A-4's restriction that the Info dictionary contain only ModDate. The header failure is removed.
- Rust PDF/X-6 implementation probe: still fails two unembedded-font errors for F4 and F5 and reports the Trapped-key and annotation-appearance warnings.

The header-only repair is therefore a valid isolated improvement, but it does not establish dual conformance. The original dual-profile artifact and this boundary variant are both retained for comparison.
