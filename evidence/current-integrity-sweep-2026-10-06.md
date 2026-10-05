# Current repository integrity sweep — 2026-10-06

Fresh checks after the latest ACOS Compass PDF-engineering additions:

- 26 source IDs in the register; 25 referenced by the claim matrix.
- 16 frozen claim IDs; zero missing source IDs and zero missing referenced paths.
- Pagination checker passes on 240 fixtures.
- The bounded binary ILP objective matches dynamic programming on all 240 fixtures using SciPy 1.10.1.
- Working tree is clean at local commit 708fe3f.
- Release state remains CHANGES_REQUIRED.

This verifies repository linkage and machine-receipt integrity only. It does not establish normative clause completeness, accepted PDF/X-6 preflight, human accessibility, production equivalence, or a 995/1000 release.
