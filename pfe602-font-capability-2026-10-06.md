# PFE 602 font and shaping capability receipt — 2026-10-06

**Purpose:** advance the font-engineering diagnostic while distinguishing font coverage and Unicode analysis from actual OpenType shaping and PDF extraction.

## Host capability check

The configured Python runtime has no `fontTools`, `uharfbuzz`, or FreeType Python module. The host has `fc-query`, which can report installed-font family, style, and language metadata, but no `hb-shape`, `hb-view`, `otfinfo`, or `pango-view` executable was available. Therefore no shaping claim is made.

## Font metadata observations

Independent `fc-query` checks reported:

| Font resource | Reported language coverage |
|---|---|
| `/System/Library/Fonts/NotoSerifMyanmar.ttc` | `my`, `mnw`, `shn` |
| `/System/Library/Fonts/NotoSansOriya.ttc` | `or` |
| `/System/Library/Fonts/AppleSDGothicNeo.ttc` | broad Latin, Cyrillic, Greek, Korean, CJK, and related language metadata |

These are installed-font metadata observations, not proof that every glyph, shaping rule, or PDF export path works.

## Unicode-only diagnostic

A fresh Python process inspected representative strings containing a combining mark (`e\u0301`), right-to-left Hebrew, Myanmar, Oriya, and an emoji sequence. It recorded code-point sequences before and after NFC/NFKC normalization. Normalization changes code-point representation where canonical composition is available, but it does not perform script shaping, bidi reordering, glyph selection, variation-selector handling, or PDF ToUnicode validation.

The executed receipt included these representative results:

| Sample | Source code points | NFC/NFKC observation |
|---|---|---|
| `é` | `U+0065 U+0301` | composes to `U+00E9` |
| Hebrew `שלום` | `U+05E9 U+05DC U+05D5 U+05DD` | unchanged by NFC/NFKC |
| Myanmar `မြန်မာ` | `U+1019 U+103C U+1014 U+103A U+1019 U+102C` | unchanged by NFC/NFKC |
| Oriya `ଓଡ଼ିଆ` | `U+0B13 U+0B21 U+0B3C U+0B3F U+0B06` | unchanged by NFC/NFKC |
| `👩🏽‍💻` | `U+1F469 U+1F3FD U+200D U+1F4BB` | unchanged by NFC/NFKC |

## Disposition

PFE 602 remains **DEMONSTRATED / LIMITED**. The repository has controlled CFF/Type3, TrueType/CIDFont, ToUnicode, and extraction evidence from the existing specimens. Complex-script shaping and malformed-mapping tests remain unexecuted until a shaping-capable toolchain is available. The absence of those tools is recorded as a capability boundary, not a pass or failure of any font.
