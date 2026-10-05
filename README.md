# Production export path experiment — 2026-10-05

## Input and method

- Source: a minimal, separately authored ODT fixture containing a heading and three paragraphs.
- Exporter: bundled LibreOffice `soffice` through `writer_pdf_Export` with `SelectPdfVersion=4`.
- Export command:

  ```text
  soffice --headless --convert-to 'pdf:writer_pdf_Export:SelectPdfVersion=4' --outdir <out> fixture.odt
  ```

- Fixture PDF SHA-256: `77bf5f4ca0807d6028c3121531293f10319e6ca2539b3a54fd041879ae9dceff`
- Validator: veraPDF Greenfield CLI 1.30.2.

## Results

| Profile | Result | Passed checks | Failed checks | Failed rules |
|---|---:|---:|---:|---:|
| PDF/A-4 | non-compliant | 388 | 10 | 5 |
| PDF/UA-2 | non-compliant | 467 | 5 | 5 |

## PDF/A-4 failures

- ISO 19005-4:2020 6.1.3-4: Info key present without a permitted PieceInfo condition.
- ISO 19005-4:2020 6.7.3-1: missing or invalid PDF/A identification extension schema.
- ISO 19005-4:2020 6.2.4.3-2: DeviceRGB used without the required device-independent or output-intent condition (6 checks).
- ISO 19005-4:2020 6.1.2-1: header is not `%PDF-2.n` as required for PDF/A-4.
- ISO 19005-4:2020 6.1.3-5: document information dictionary contains entries beyond the permitted ModDate condition.

## PDF/UA-2 failures

- ISO 14289-2:2024 8.11.2-1: missing required `DisplayDocTitle=true` viewer preference.
- ISO 14289-2:2024 8.8-1: internal destinations are not structure destinations.
- ISO 14289-2:2024 5-1: missing PDF/UA identification metadata.
- ISO 14289-2:2024 8.11.1-1: missing `dc:title` metadata.
- ISO 14289-2:2024 8.2.5.2-1: structure tree root does not satisfy the PDF 2.0 namespace/Document-child requirement.

## Disposition

This experiment proves that selecting a PDF/A-4 export option in a general office exporter is not evidence of PDF/A-4 or PDF/UA-2 conformance. The failure report is retained as production-path evidence and a repair target. No production-ready or conformance claim is made.

