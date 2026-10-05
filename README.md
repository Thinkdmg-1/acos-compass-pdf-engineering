# Profile and human-review test plan

**Date frozen:** 2026-10-05  
**Status:** `PLANNED / NOT EXECUTED`  
**Purpose:** define the smallest reproducible next study cycle for the unresolved PDF/X-6, PDF/A-4, and human PDF/UA checks without treating public summaries or a single validator run as conformance evidence.

## Inputs and custody

The test requires three declared inputs before execution:

1. An authorized copy or permitted extract of ISO 15930-9:2020 (PDF/X-6), with edition, license boundary, file digest, and clause locations recorded.
2. An authorized copy or permitted extract of ISO 19005-4:2020 (PDF/A-4), with edition, license boundary, file digest, and clause locations recorded.
3. A declared production fixture set: source file, export application/version, fonts and font licenses, linked assets, color profiles, and export settings, each hashed or otherwise recoverable.

The existing local teaching fixture and its reports remain useful for method rehearsal. They cannot stand in for the declared production set.

## Execution order

### A. Normative extraction

Freeze the claim inventory before reading the clauses. For every claim, record the exact clause, requirement verb, exceptions, applicability condition, profile part, and an independent reviewer’s interpretation. A public profile index may corroborate identity and scope; it cannot fill a missing requirement clause.

**Stop condition:** stop and mark the row unresolved if the authorized text, clause context, or profile applicability cannot be inspected.

### B. PDF/A-4 preflight

Run the declared production fixture through a pinned validator and one independent parser. Record command, validator version, profile identifier, exit status, complete machine report, and parser observations. Repeat after any repair from the original source, preserving both bytes and hashes.

Required measurements:

- PDF/A profile and revision selected;
- metadata and output-intent presence and values;
- embedded-font and embedded-file status;
- object-level parser warnings;
- byte hash before and after repair;
- page count, media boxes, and rendered pixel dimensions.

**Stop condition:** a pass from one validator alone is insufficient; any disagreement between validator and parser remains open until explained.

### C. PDF/X-6 preflight

Use a preflight engine that explicitly supports ISO 15930-9:2020 PDF/X-6. Record the selected profile, profile version, color-management settings, output intent, page geometry, font/resource embedding, transparency/overprint findings, and all errors and warnings. Preserve the complete report and a screenshot or export of the profile-selection screen when the interface is graphical.

**Stop condition:** the local veraPDF profile inventory does not list PDF/X-6, so a veraPDF result must never be labeled a PDF/X-6 result. Without a PDF/X-capable engine and authorized requirement map, the profile remains `UNTESTED`.

### D. Human PDF/UA review

Run the tagged fixture through three independent human checks: keyboard traversal, screen-reader reading order/announcements, and visual inspection at 200% and in a high-contrast setting. Record operating system, assistive technology/version, browser or viewer/version, test script, reviewer, date, and each observed defect with page/object location.

A second reviewer repeats the script on a held-out page or a separately exported copy. Disagreements are preserved and adjudicated against the authorized PDF/UA text.

**Stop condition:** machine validation and human checks must agree on the disposition. If the environment cannot run the assistive-technology check, report `UNAVAILABLE`; do not convert that absence into a pass.

## Independent verification

The measurements are checked by a different method where practical:

- validator output versus parser/object inspection;
- reported page count versus Poppler or viewer count;
- file hash from two independent reads;
- profile selection versus the report’s profile identifier;
- human reading order versus structure-tree inspection.

A repeated run of the same command is a reproducibility check, not independent corroboration.

## Release rule

This plan does not authorize a conformance statement. A profile claim can be promoted only when the authorized normative mapping, a complete machine report, independent parser evidence, and the required human checks are all present and mutually consistent. Until then the matrix status remains `CHANGES_REQUIRED`, and the source-quality gate remains below the 995 target.
