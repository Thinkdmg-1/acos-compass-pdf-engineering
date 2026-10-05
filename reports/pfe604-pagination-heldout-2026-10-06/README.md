# PFE 604 held-out pagination transfer benchmark — 2026-10-06

**Protocol:** PFE604-2026-10-06-heldout-v1  
**Status:** EXECUTED / BOUNDED

The original PFE 604 lab proved dynamic programming against an exhaustive cut-mask oracle on a small enumerated domain. This follow-up tests transfer to a frozen, independently generated fixture set outside that domain.

## Method

- Seed: 60420261006
- Capacity: 17
- Fixtures: 240
- Length range: 8..12
- Block-height range: 1..17
- Solver: labs/pfe604_pagination.py::dynamic_programming
- Independent oracle: fresh cut-mask enumeration in run-heldout.py
- Independent checker: check.py

## Result

All 240 held-out fixtures matched the independent exhaustive oracle, and every dynamic-programming partition independently re-scored to the oracle objective. Greedy packing was strictly worse on 55 of 240 fixtures. Frozen fixture-set digest: da71a1bee69e60e3bfa3cd7a4650691deadfc4a1b78ec350dec5ac586f552d0d.

## Limits

This advances C-011 only for the bounded contiguous-block model. It is not a published pagination benchmark and does not reproduce Knuth–Plass or an integer-programming solver. It excludes line breaking, floats, footnotes, columns, spreads, widows/orphans, renderer behavior, and perceptual reading quality. No production or universal pagination claim follows.
