# CSS pagination browser fixture — 2026-10-05

## Frozen method

- Source: `fixture.html`, authored as a separate minimal fixture.
- Browser: Google Chrome `154.0.8037.93`, headless print path.
- Command: `Chrome --headless=new --disable-gpu --no-sandbox --user-data-dir=<pinned temporary profile> --print-to-pdf=chrome-print.pdf file://<fixture.html>`
- CSS variables: `@page { size: A4 portrait; margin: 18mm 16mm 20mm; }`, `break-before: page`, `break-inside: avoid`, `break-after: avoid`, `widows: 3`, `orphans: 3`.
- Independent checks: Poppler `pdfinfo`, Poppler `pdftotext`, SHA-256, and human raster inspection of all four pages.

## Observed output

| Measurement | Result |
|---|---|
| PDF pages | 4 |
| Page box | 594.96 × 841.92 pt (A4) |
| Text form feeds | 4 |
| Forced-page section | Present at the start of page 2 |
| Overflow probe | Begins on page 3 and continues onto page 4 |
| HTML SHA-256 | `5bb34cd179e16791c838b8994088615da00d35dad2b9a163355e6ef319059e47` |
| PDF SHA-256 | `2bccbb6f923c72bd34c884e4df137c6bb65f52cc08a8a43396de66ed94efff9f` |

The visual inspection found a clean A4 page geometry, a coherent forced break, and a deliberately split oversized element. Chrome preserved the forced break and fragmented the oversized box across two pages. This is a browser-behavior observation, not a claim that CSS declarations guarantee a particular PDF structure or that the output is PDF/UA, PDF/X, or PDF/A compliant.

## Interpretation

The fixture supplies the previously missing browser/version evidence for the curriculum's CSS page-size and fragmentation claims. It also demonstrates the transfer boundary described by CSS Paged Media: an element can exceed the page box and the user agent determines the resulting fragmentation. The fixture does not establish cross-browser equivalence; another engine, print dialog, margin setting, or header/footer policy may produce different bytes or page counts.

## Firefox comparison and divergence

Firefox `111.0` was run with its headless `--screenshot` path at 794 × 1123 px. The screenshot is a **screen-media** observation, not a print-to-PDF result. In that path, the explicit page break does not create a separate screenshot page and the overflow probe remains in the continuous viewport. This is a useful divergence record, but it does not count as a second print-engine conformance result.

Firefox screenshot SHA-256: `c8235a702d369d5e5c9d1b4bef81d3b103648ce5a5c7258c35b71a9e43937da4`

The remaining browser-study action is a second engine's actual print path or a declared reason that it cannot be obtained in the current environment. The Chrome print result remains scoped to Chrome 154 and its frozen print settings.
