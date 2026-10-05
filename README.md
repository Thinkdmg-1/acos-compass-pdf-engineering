# CSS pagination independent rerun — 2026-10-06

**Purpose:** rerun the independent extraction and geometry checks for the frozen Chrome 154 pagination fixture without regenerating the browser PDF.

## Receipt

```json
{
  "html_sha256": "5bb34cd179e16791c838b8994088615da00d35dad2b9a163355e6ef319059e47",
  "pdf_sha256": "2bccbb6f923c72bd34c884e4df137c6bb65f52cc08a8a43396de66ed94efff9f",
  "pypdf_pages": 4,
  "pypdf_boxes": [[594.95996, 841.91998], [594.95996, 841.91998], [594.95996, 841.91998], [594.95996, 841.91998]],
  "forced_page_occurrences": 1,
  "overflow_occurrences": 1,
  "text_len": 1383,
  "poppler_creator": "HeadlessChrome/154.0.0.0"
}
```

The rerun agrees with the original four-page A4 geometry and confirms that the forced section and overflow probe remain present in extracted text. It is a reproducibility check over the frozen artifact, not a second browser print engine and not a CSS, PDF/UA, PDF/X, or PDF/A conformance claim.
