# Standards-access recheck — 2026-10-06

**Purpose:** independently recheck whether an authorized, no-cost route exists for the controlling PDF 2.0 and PDF/UA standards before treating standards access as an unresolved assumption.

## Findings

The PDF Association's sponsored-standards page now states that the current ISO 32000-2:2020 bundle is available at no cost and was updated on 2026-06-18. The listed bundle includes ISO 32000-2:2020 with Errata Collection 3, ISO/TS 32001, ISO/TS 32002, ISO/TS 32003, ISO/TS 32004, and ISO/TS 32005:

- <https://pdfa.org/sponsored-standards>
- <https://www.pdfa-inc.org/product/iso-32000-2-pdf-2-0-bundle-sponsored-access/>

The same page states that the PDF/UA bundle is available at no cost and includes ISO 14289-2:2024, ISO 14289-1:2014, and ISO/TS 32005:2023:

- <https://www.pdfa-inc.org/product/pdf-ua-bundle/>

The product pages show a `$0.00` cart flow. No cart, account, license acceptance, or download was initiated in this study cycle. The repository therefore records the authorized access path and its exact boundary without claiming custody of the files or redistributing them.

## Open-source corroboration

The PDF Association identifies the Arlington PDF Model as a specification-derived, machine-readable model of the PDF 2.0 document object model, with public source at <https://github.com/pdf-association/arlington-pdf-model>. Its own documentation explicitly says that it does not replace the official ISO specification and does not define lexical rules, content streams, or file-structure/layout rules. It is suitable for object-model exercises and parser/writer research, not for replacing the normative text or proving profile conformance.

The PDF Association's public errata index is also available at <https://pdf-issues.pdfa.org/32000-2-2020/>. It lists corrected PDF 2.0 clauses and tables, but it remains an errata and implementation-corroboration resource rather than the complete ISO standard.

## Disposition

This recheck changes the next action from “find whether a no-cost authorized path exists” to “obtain the sponsored files through the explicit cart/account/license flow, if that action is authorized, then record custody receipts and perform the clause map.” It does not change the release state. The source gate remains `CHANGES_REQUIRED` until the authorized files or permitted extracts, complete mappings, PDF/X-6 and PDF/A-4 profile evidence, and human accessibility checks are present.
