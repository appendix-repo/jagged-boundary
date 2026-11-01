"""Check 01: the single-increase rule for adjacent pairs.

For every adjacent pair (i, i+1) in the administered sequence, count the dimensions on which i+1 is coded higher
than i. The design rule is that at most one dimension increases. Steps where the one increase exceeds one level
are listed, as are parallel steps (no increase). Also reports dominance relations used by the dominance-violation
measure (Section 5.2): j dominates i if j >= i on every dimension and > on at least one.
"""
import json, sys

items = json.load(open(sys.argv[1]))["items"]
dims = ["T", "C", "G", "S", "H"]
n_single, n_multi, n_parallel, violations = 0, [], [], []
for a, b in zip(items, items[1:]):
    ups = {d: b["codes"][d] - a["codes"][d] for d in dims if b["codes"][d] > a["codes"][d]}
    pair = f'{a["id"]}->{b["id"]}'
    if len(ups) > 1:
        violations.append((pair, ups))
    elif len(ups) == 0:
        n_parallel.append(pair)
    elif max(ups.values()) > 1:
        n_multi.append((pair, ups))
    else:
        n_single += 1
print(f"adjacent pairs: {len(items) - 1}")
print(f"  one dimension up by one level: {n_single}")
print(f"  one dimension up by more than one level: {len(n_multi)} {n_multi}")
print(f"  no dimension up (parallel or descending): {len(n_parallel)} {n_parallel}")
print(f"  more than one dimension up (rule violated): {len(violations)} {violations}")

dom = 0
for i in items:
    for j in items:
        ci, cj = i["codes"], j["codes"]
        if all(cj[d] >= ci[d] for d in dims) and any(cj[d] > ci[d] for d in dims):
            dom += 1
pairs = len(items) * (len(items) - 1) // 2
print(f"ordered dominance pairs: {dom} of {pairs} unordered pairs are comparable")
print("RESULT:", "PASS" if not violations else "FAIL")
