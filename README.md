# PFE 604 pagination lab receipt — 2026-10-06

**Protocol:** `PFE604-2026-10-06-v1`  
**Status:** `EXECUTED / BOUNDED`

This is a reproducible teaching experiment for one narrow pagination model: contiguous indivisible positive integer blocks, a fixed page capacity, and a cost equal to squared unused capacity on non-final pages. It compares first-fit greedy packing with a dynamic-programming solver and an independently written exhaustive cut-mask oracle.

## Execution

- Source: [`labs/pfe604_pagination.py`](../../labs/pfe604_pagination.py)
- Exact command: `python3 labs/pfe604_pagination.py`
- Exhaustive domain: lengths 1 through 7; each block height in `{2, 5, 8}`; capacity `10`.
- Exhaustive fixtures: `3,279`.
- Result: dynamic-programming cost matched the independent oracle on all fixtures; the selected dynamic-programming cuts were re-scored independently.
- Adversarial fixtures include `(3, 6, 2, 9)`, where greedy cost is `65` and dynamic-programming/exact cost is `53`, and `(4, 5, 1, 6, 2, 3)`, where greedy cost is `4` and dynamic-programming/exact cost is `2`.
- The complete machine-readable receipt is [`results.json`](results.json), including runtime, environment, fixture outputs, and source digest.

## Independent checks and limits

The exhaustive oracle uses a separate cut-mask enumeration rather than the dynamic-programming recurrence. Equal-cost partitions can have different cut locations; verification therefore compares objective values and independently re-scores the dynamic-programming partition instead of requiring identical tie-breaking.

This does not reproduce Knuth–Plass, an integer-programming solver, or a published pagination benchmark. No solver library was available in the declared environment, so no ILP implementation is claimed. The model excludes line breaking, elastic whitespace, floats, footnotes, columns, spreads, widows/orphans, renderer behavior, and subjective reading quality. The result supports only the bounded algorithmic claim stated above.
