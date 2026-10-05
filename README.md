# Controlled tagged-PDF repair experiment — 2026-10-06

Status: EXECUTED / NON-CONFORMING

This experiment copied the tagged TrueType fixture and changed only document-level metadata and namespace structures. The original fixture remains untouched. The repair script is repair.py; the repaired PDF is truetype-tagged-metadata-repaired.pdf; the fresh veraPDF report is verapdf-ua2.json.

## Changes

- added catalog /Lang and confirmed /MarkInfo /Marked true;
- confirmed /ViewerPreferences /DisplayDocTitle true;
- added an XMP metadata stream with PDF/UA identification and dc:title;
- added a PDF 2.0 structure namespace dictionary to /StructTreeRoot /Namespaces and referenced it from the /Document structure element.

## Fresh comparison

| Artifact | PDF/UA-2 rules passed/failed | Checks passed/failed | Result |
|---|---:|---:|---|
| Original truetype-tagged.pdf | 1722 / 5 | 2532 / 7 | non-compliant |
| Repaired copy | 1724 / 3 | 2540 / 5 | non-compliant |

The remaining fresh failures are:

- 8.2.2: content not considered real is not marked as an artifact;
- Table 5: the Table contains content items;
- 8.8: in-document destinations are not structure destinations.

Original digest: d82571d66f6018ce60a7f6c13cf2d842ccdcc04001a8bb1f50ccdbc949c3c3c6
Repaired digest: 1d0f61ae957c6519da7e22460179cb81cceb0236b24d1f7743e96a79525e8813

This is a controlled repair result for one fixture. It does not establish PDF/UA-2 conformance, screen-reader behavior, keyboard behavior, or a general repair recipe. Human accessibility checks remain unavailable.

## Isolated outline ablation

A separate ablation removed the catalog Outlines entry from the repaired copy, without changing page content or the structure tree. Its PDF/UA-2 result was 1,725 rules passed and 2 failed, with 2 failed checks; removing Outlines eliminated 8.8. It remains non-compliant because artifact marking and table-content structure still fail. This is diagnostic evidence only: removing navigation is a product regression and is not accepted as a production repair.
