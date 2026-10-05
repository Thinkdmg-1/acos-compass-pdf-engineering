# PFE 604 color and output-intent receipt — 2026-10-06

**Purpose:** inspect the available ICC profile inventory and the repaired PDF/A-4 fixture's output intent without confusing metadata presence with color-managed conversion or print proof.

## Host profile inventory

The host exposes `sips` and system ICC profiles. Independent file inspection reported:

| Profile | File type / declared identity | SHA-256 |
|---|---|---|
| `/System/Library/ColorSync/Profiles/sRGB Profile.icc` | Microsoft Color Profile 2.1, RGB/XYZ monitor, `sRGB IEC61966-2.1` | `2b3aa1645779a9e634744faf9b01e9102b0c9b88fd6deced7934df86b949af7e` |
| `/System/Library/ColorSync/Profiles/Generic CMYK Profile.icc` | ColorSync Profile 2.2, CMYK/Lab printer | `0c8a584b288a306eac9e1d3f1e68bc1b64331c717ceb051420e6257f17b3509a` |

## Fixture inspection

The repaired fixture `reports/production-pdfa4-2026-10-05/fixture-repaired2.pdf` has SHA-256 `c027477c49ffbb7f055a3c7ed37a804ef3423c3d6c1a0ad4faaa5f1a916f8c73`. A fresh pypdf inspection found one catalog output intent:

```json
{
  "/S": "/GTS_PDFA1",
  "/OutputConditionIdentifier": "sRGB IEC61966-2.1",
  "/DestOutputProfile": "embedded ICC profile, N=3"
}
```

The output intent is consistent with an sRGB-oriented PDF/A fixture. It does not prove that source colors were converted correctly, that a CMYK press condition is represented, that a printer will reproduce the appearance, or that any ΔE measurement or physical proof exists.

## Disposition

PFE 604 remains **DEMONSTRATED / LIMITED**. Profile identification and output-intent inspection are demonstrated. Device characterization, rendering-intent comparison, gamut mapping, ΔE00 measurement, viewing-condition control, and physical proofing remain unexecuted.
