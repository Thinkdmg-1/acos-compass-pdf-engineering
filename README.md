# Fresh veraPDF runtime and validator rerun — 2026-10-06

**Status:** `EXECUTED / PROFILE-SCOPED`

A portable Temurin JRE 21 runtime was downloaded into `/tmp` for this run only; no system Java installation or repository dependency was changed. The pinned veraPDF 1.30.2 launcher then executed successfully.

## Runtime and custody

- veraPDF: `1.30.2`, built 2026-06-03; complete version output is in [`version.txt`](version.txt).
- Runtime: Temurin OpenJDK JRE `21.0.12.1+1`, x86_64 macOS.
- Download endpoint: `https://api.adoptium.net/v3/binary/latest/21/ga/mac/x64/jre/hotspot/normal/eclipse`.
- Downloaded archive SHA-256: `6717ec641fd9ce0bb209ca083ee23b42202ac68cb6fcc5753496e0e4a0f41989`.
- The built-in profile inventory is preserved in [`profile-list.txt`](profile-list.txt). It lists PDF/A-4, PDF/UA-2, and WTPDF profiles; it does not list PDF/X-6.

## Fresh runs

| Fixture | Profile | Result | Rules passed/failed | Checks passed/failed |
|---|---|---:|---:|---:|
| `fixture-repaired2.pdf` | PDF/A-4 | compliant | 109 / 0 | 375 / 0 |
| `fixture-repaired2.pdf` | PDF/UA-2 + Tagged PDF | non-compliant | 1721 / 6 | 310 / 8 |
| `truetype-tagged.pdf` | PDF/A-4 | non-compliant | 103 / 6 | 1362 / 276 |
| `truetype-tagged.pdf` | PDF/UA-2 + Tagged PDF | non-compliant | 1722 / 5 | 2532 / 7 |

The complete JSON reports and stderr captures are preserved beside this receipt. The repaired production fixture digest is `c027477c49ffbb7f055a3c7ed37a804ef3423c3d6c1a0ad4faaa5f1a916f8c73`; the tagged TrueType fixture digest is `d82571d66f6018ce60a7f6c13cf2d842ccdcc04001a8bb1f50ccdbc949c3c3c6`.

## Interpretation

This removes the previous Java-runtime capability boundary and supplies fresh PDF/A-4 and PDF/UA-2 machine evidence for the two declared fixtures. It does not establish PDF/X-6 support or conformance: veraPDF's current built-in inventory has no PDF/X-6 profile. It also does not replace keyboard, screen-reader, high-contrast, or second-reviewer checks. The PDF/UA failures remain open and are recorded from the fresh run rather than inherited from historical reports.
