# PFE 602 complex-script shaping lab — 2026-10-06

**Status:** EXECUTED / DEMONSTRATED SHAPING / PDF EXPORT STILL UNVERIFIED

## Frozen question

Can a disposable OpenType shaping path expose the difference between Unicode normalization, script direction, glyph substitution/positioning, and font coverage for representative PFE 602 cases?

## Inputs and tools

- Runtime: temporary Python target directory `/tmp/acos-font-lab-20261006`.
- `fontTools` 4.60.2 for font-table/cmap inspection.
- `uharfbuzz` 0.51.7 for HarfBuzz shaping.
- Independent host checks: `fc-query` font metadata and SHA-256 of each system font resource.
- Fonts were referenced in place and were not copied into the repository:
  - `/System/Library/Fonts/NotoSerifMyanmar.ttc`
  - `/System/Library/Fonts/NotoSansOriya.ttc`
  - `/Library/Fonts/Arial Unicode.ttf`
- The executable source is [`run.py`](run.py); the machine-readable receipt is [`results.json`](results.json), SHA-256 `fd814b205eac4752fb9203dd909877399bc5891f91c8c2d9edc65d20614ccce8`.

## Observed results

| Sample | Shaping observation | Interpretation |
|---|---|---|
| `e` + combining acute | 2 input code points normalize to 1 NFC code point and shape to 1 glyph | normalization and shaping can change representation; they are not PDF extraction evidence |
| Hebrew `שלום` | HarfBuzz detects Hebrew/RTL and returns clusters in descending logical order | direction and cluster order must be retained by layout/export paths |
| Myanmar `မြန်မာ` | HarfBuzz detects Myanmar and returns nontrivial clusters with GSUB/GPOS-capable font tables | script shaping is not equivalent to code-point iteration |
| Oriya `ଓଡ଼ିଆ` | HarfBuzz detects Oriya and returns 4 glyphs for 5 input code points with grouped clusters | glyph count is not a character count; clusters carry mapping information |
| `👩🏽‍💻` with Arial Unicode | the selected font returns missing glyph IDs for the unsupported emoji sequence | fallback and color-font handling remain separate unresolved requirements |

The full glyph IDs, clusters, advances, font hashes, table lists, and `fc-query` metadata are retained in `results.json`.

## Independent challenge

[`independent-check.py`](independent-check.py) is a separate parser/assertion path. It verifies the result hash, tool-version fields, font digests, script/direction detections, cluster properties, and the explicit emoji missing-glyph boundary. Its receipt is [`independent-check.json`](independent-check.json).

## Scope and limits

This lab demonstrates a shaping-capable text path and advances the PFE 602 shaping prerequisite. It does not prove CoreText, DirectWrite, browser, LaTeX, or PDF-export equivalence; it does not prove ToUnicode correctness, tagging, visual raster fidelity, font licensing, or screen-reader behavior. A PDF fixture containing these strings and an independent PDF parser/render comparison remain required before making a PDF semantic or production claim.
