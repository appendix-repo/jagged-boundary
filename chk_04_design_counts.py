"""Check 04: the counts and design relations that the appendix states about the item sequence.

Every assertion below is a sentence of the appendix (section given in each label), recomputed from
instrument/items.json and instrument/items_v0.1.json. It complements Check 01, which covers the single-increase rule.

Run from the repository root:  python3 checks/chk_04_design_counts.py
"""
import json, os, sys

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
v2 = json.load(open(os.path.join(root, "instrument", "items.json")))
v1 = json.load(open(os.path.join(root, "instrument", "items_v0.1.json")))
DIMS = ["T", "C", "G", "S", "H"]
items = v2["items"]
ids = [it["id"] for it in items]
code = {it["id"]: tuple(it["codes"][d] for d in DIMS) for it in items}
RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}" + (f": {detail}" if detail else ""))


def dominates(j, i):
    return all(a >= b for a, b in zip(code[j], code[i])) and any(a > b for a, b in zip(code[j], code[i]))


print("Instrument size and anchors (Section 0, 2.2)")
check("v0.2 has 37 positions", len(items) == 37, str(len(items)))
check("v0.1 has 32 positions", len(v1["items"]) == 32, str(len(v1["items"])))
proposal_ids = [str(k) for k in range(1, 27)] + ["27a", "27b"] + [str(k) for k in range(28, 32)]
interp = [x for x in ids if x not in proposal_ids]
check("v0.2 = the proposal's items 1-31 (27 split as 27a/27b) plus five interpolations",
      set(proposal_ids) <= set(ids) and interp == ["15b", "17b", "19b", "21b", "28b"], f"interpolations {interp}")
check("v0.1 = the proposal's items only", [it["id"] for it in v1["items"]] == proposal_ids)
check("positions run 1..37 in file order", [it["position"] for it in items] == list(range(1, 38)))
anchors = v2["anchors"]
check("11 anchor items: 2, 7, 10, 14, 17, 19, 22, 24, 27a, 27b, 31",
      anchors == ["2", "7", "10", "14", "17", "19", "22", "24", "27a", "27b", "31"]
      and [it["id"] for it in items if it["anchor"]] == anchors, str(anchors))

print("\nRegimes (Section 1)")
reg = {r: [it["id"] for it in items if it["regime"] == r] for r in ("R1", "R2", "R3", "R4")}
check("R1 = items 1 to 7", reg["R1"] == [str(k) for k in range(1, 8)], str(reg["R1"]))
check("R2 = items 8 to 17b", reg["R2"] == ["8", "9", "10", "11", "12", "13", "14", "15", "15b", "16", "17", "17b"], str(reg["R2"]))
check("R3 = items 18 to 23", reg["R3"] == ["18", "19", "19b", "20", "21", "21b", "22", "23"], str(reg["R3"]))
check("R4 = items 24 to 31", reg["R4"] == ["24", "25", "26", "27a", "27b", "28", "28b", "29", "30", "31"], str(reg["R4"]))

print("\nWhy the sequence is not monotone (Section 2.1)")
incr = sum(b - a for a, b in zip(code[ids[0]], code[ids[-1]]))
check("18 level-increments from the first item to the last, against 36 steps", incr == 18 and len(ids) - 1 == 36,
      f"{incr} increments, {len(ids) - 1} steps")
pairs = [(ids[x], ids[y]) for x in range(37) for y in range(x + 1, 37)]
ordered = sum(dominates(j, i) or dominates(i, j) for i, j in pairs)
check("558 of the 666 item pairs are ordered by dominance", ordered == 558 and len(pairs) == 666, f"{ordered} of {len(pairs)}")

print("\nParallel inconsistency (Section 5.2)")
same = [(i, j) for i, j in pairs if code[i] == code[j]]
groups = {}
for i in ids:
    groups.setdefault(code[i], []).append(i)
groups = sorted([g for g in groups.values() if len(g) > 1], key=lambda g: ids.index(g[0]))
expected = [["3", "4", "5"], ["6", "7"], ["15", "15b"], ["17", "17b"], ["21", "21b"], ["24", "28", "28b"], ["25", "26", "27b"]]
check("identically coded groups {3,4,5} {6,7} {15,15b} {17,17b} {21,21b} {24,28,28b} {25,26,27b}", groups == expected, str(groups))
check("13 identically coded pairs", len(same) == 13, str(len(same)))

print("\nNon-adjacent probes (Section 2.3)")


def differ(i, j):
    return [d for d, a, b in zip(DIMS, code[i], code[j]) if a != b]


check("P1 2 vs 10 differ on T only", differ("2", "10") == ["T"], str(differ("2", "10")))
check("P2 17 vs 21 differ on C only", differ("17", "21") == ["C"], str(differ("17", "21")))
check("P3 22 vs 29 differ on T only", differ("22", "29") == ["T"], str(differ("22", "29")))
check("P4 26 vs 27b coded identically", differ("26", "27b") == [], str(differ("26", "27b")))
d5 = {d: b - a for d, a, b in zip(DIMS, code["19"], code["25"]) if a != b}
check("P5 19 vs 25 incomparable: C and T up, G down", not dominates("25", "19") and not dominates("19", "25")
      and d5.get("T", 0) > 0 and d5.get("C", 0) > 0 and d5.get("G", 0) < 0, str(d5))
check("P6 18 dominates 13", dominates("18", "13"))

print("\nDominance steps used by the jaggedness measure J (Section 5.2)")
steps = [(a, b) for a, b in zip(ids, ids[1:])
         if all(y >= x for x, y in zip(code[a], code[b])) and any(y > x for x, y in zip(code[a], code[b]))]
print(f"  (reported, not asserted) {len(steps)} of 36 steps raise a dimension and lower none: "
      + ", ".join(f"{a}->{b}" for a, b in steps))

print("\nChanges from v0.1 to v0.2 (Sections 2.4, 4.5)")
t1 = {it["id"]: it["text"] for it in v1["items"]}
t2 = {it["id"]: it["text"] for it in items}
reworded = [i for i in t1 if t1[i] != t2[i]]
check("only item 18 was reworded", reworded == ["18"], str(reworded))
c1 = {it["id"]: it["codes"] for it in v1["items"]}
recoded = [i for i in c1 if c1[i] != items[ids.index(i)]["codes"]]
check("no item of v0.1 was recoded", recoded == [], str(recoded))

print("\nRespondent burden (Section 2.2)")
secs = 37 * 12 + 11 * 25 + 6 * 10 + 120
check("about 15 minutes: 37 items x 12 s + 11 anchors x 25 s + 6 probes x 10 s + 2 min", 13 * 60 <= secs <= 17 * 60,
      f"{secs} s = {secs / 60:.1f} min")

print(f"\n{sum(RESULTS)} of {len(RESULTS)} assertions hold")
print("RESULT:", "PASS" if all(RESULTS) else "FAIL")
sys.exit(0 if all(RESULTS) else 1)
