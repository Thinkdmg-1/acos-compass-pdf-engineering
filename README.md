# veraPDF validation run — 1.30.2

**Run date:** 2026-10-05  
**Validator:** veraPDF Greenfield CLI 1.30.2, built 2026-06-03  
**Profiles:** PDF/A-4 (`4`) and PDF/UA-2 + Tagged PDF (`ua2`)  
**Java runtime:** Temurin/OpenJDK 21.0.12.1, x86_64 macOS  
**Installer source:** <https://software.verapdf.org/releases/verapdf-installer.zip>  
**Installer SHA-256:** `6cc6341cb1af644044054b81f00a6590a7918abb18f762243de115258bcad838`

The installer was downloaded from the official veraPDF distribution site and installed into the ignored `work/` area. The CLI and documentation packs were selected; the GUI and sample plugins were not selected. The local machine does not have `gpg`, so the detached signature was downloaded but could not be cryptographically checked in this run. The SHA-256 digest is preserved above.

## Command form

```text
verapdf --format json --flavour 4 <file.pdf>
verapdf --format json --flavour ua2 <file.pdf>
```

The complete JSON reports and stderr captures are in this directory. `results-summary.json` is a derived index, not a substitute for the raw reports.

## Results

| Fixture | PDF/A-4 | PDF/UA-2 | Interpretation |
|---|---:|---:|---|
| `pfe601-minimal.pdf` | fail: 6 checks / 6 rules | fail: 7 checks / 7 rules | minimal syntax/rendering teaching file; not an archival or accessibility deliverable |
| `pfe601-repaired-xref.pdf` | fail: 6 checks / 6 rules | fail: 7 checks / 7 rules | xref repair preserved parser/rendering behavior but did not create profile conformance |
| `truetype-tagged.pdf` | fail: 276 checks / 6 rules | fail: 7 checks / 5 rules | useful tagged specimen with remaining PDF/UA-2 defects; no PDF/A-4 claim |
| `truetype-untagged.pdf` | fail: 276 checks / 6 rules | fail: 257 checks / 5 rules | intentionally untagged comparison specimen |
| `cff-untagged.pdf` | fail: 276 checks / 6 rules | fail: 257 checks / 5 rules | CFF/Type3 comparison specimen; not a missing-font conclusion |

The validator result is machine evidence only. veraPDF's own documentation distinguishes machine-verifiable PDF/UA checks from human checkpoints. No row above establishes full PDF/UA conformance, physical print quality, screen-reader acceptance, or archival suitability.

