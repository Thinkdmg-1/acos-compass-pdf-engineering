"""PFE 604 bounded pagination lab.

Model: contiguous, indivisible positive-height blocks; fixed page capacity; final-page
slack is free. This is a teaching model, not a production layout engine.
"""
from __future__ import annotations
from itertools import product
from time import perf_counter
import hashlib, json, platform, sys


def validate(heights, capacity):
    if not heights or capacity <= 0 or any(type(x) is not int or x <= 0 for x in heights):
        raise ValueError("positive integer heights and positive capacity are required")
    if any(x > capacity for x in heights):
        raise ValueError("an indivisible block exceeds capacity")


def cuts_to_loads(heights, cuts):
    starts = [0] + list(cuts[:-1])
    return [sum(heights[a:b]) for a, b in zip(starts, cuts)]


def objective(heights, capacity, cuts):
    loads = cuts_to_loads(heights, cuts)
    if any(load > capacity for load in loads):
        return None
    return sum((capacity - load) ** 2 for load in loads[:-1])


def greedy(heights, capacity):
    validate(heights, capacity)
    cuts, used = [], 0
    for index, height in enumerate(heights):
        if used and used + height > capacity:
            cuts.append(index)
            used = 0
        used += height
    cuts.append(len(heights))
    return tuple(cuts)


def dynamic_programming(heights, capacity):
    validate(heights, capacity)
    n = len(heights)
    best = [None] * (n + 1)
    paths = [None] * (n + 1)
    best[n], paths[n] = 0, ()
    for start in range(n - 1, -1, -1):
        used = 0
        for end in range(start, n):
            used += heights[end]
            if used > capacity:
                break
            candidate = (0 if end + 1 == n else (capacity - used) ** 2) + best[end + 1]
            if best[start] is None or candidate < best[start]:
                best[start] = candidate
                paths[start] = (end + 1,) + paths[end + 1]
    return best[0], paths[0]


def exact_enumerator(heights, capacity):
    """Independent oracle: enumerate every possible cut mask."""
    validate(heights, capacity)
    best_cost, best_cuts = None, None
    for mask in product((False, True), repeat=len(heights) - 1):
        cuts = tuple(i + 1 for i, selected in enumerate(mask) if selected) + (len(heights),)
        value = objective(heights, capacity, cuts)
        if value is not None and (best_cost is None or value < best_cost):
            best_cost, best_cuts = value, cuts
    return best_cost, best_cuts


def run():
    capacity = 10
    adversarial = [(3, 6, 2, 9), (7, 2, 6, 3, 2), (4, 5, 1, 6, 2, 3)]
    exhaustive = []
    for length in range(1, 8):
        for heights in product((2, 5, 8), repeat=length):
            dp_cost, dp_cuts = dynamic_programming(heights, capacity)
            exact_cost, exact_cuts = exact_enumerator(heights, capacity)
            assert dp_cost == exact_cost
            assert objective(heights, capacity, dp_cuts) == exact_cost
            exhaustive.append(heights)
    cases = []
    for heights in adversarial:
        gcuts = greedy(heights, capacity)
        dpcost, dpcuts = dynamic_programming(heights, capacity)
        ecost, ecuts = exact_enumerator(heights, capacity)
        cases.append({
            "heights": heights,
            "greedy": {"cuts": gcuts, "loads": cuts_to_loads(heights, gcuts), "cost": objective(heights, capacity, gcuts)},
            "dynamic_programming": {"cuts": dpcuts, "loads": cuts_to_loads(heights, dpcuts), "cost": dpcost},
            "independent_exact": {"cuts": ecuts, "cost": ecost},
        })
    start = perf_counter()
    for heights in exhaustive:
        dynamic_programming(heights, capacity)
    elapsed = perf_counter() - start
    payload = {
        "protocol": "PFE604-2026-10-06-v1",
        "model": "contiguous indivisible positive integer blocks; fixed capacity; final-page slack unpenalized",
        "objective": "sum of squared unused capacity on non-final pages",
        "algorithms": ["first-fit greedy", "dynamic programming", "independent exhaustive cut-mask oracle"],
        "capacity": capacity,
        "exhaustive_fixture_count": len(exhaustive),
        "exhaustive_domain": "length 1..7; each height in {2,5,8}",
        "dp_matches_exact_oracle": True,
        "adversarial_cases": cases,
        "runtime_seconds_dynamic_programming_on_exhaustive_domain": elapsed,
        "runtime_environment": {"python": sys.version.split()[0], "platform": platform.platform()},
        "source_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
        "limits": [
            "No floats, footnotes, columns, spreads, widows/orphans, elastic whitespace, line breaking, or renderer behavior.",
            "The exhaustive oracle is an independent implementation of the partition search, not an independent published benchmark.",
            "No integer-programming solver was available; this receipt does not claim an ILP implementation.",
            "Squared slack is a teaching objective and is not a perceptual quality metric or a page-count optimum.",
        ],
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    run()
