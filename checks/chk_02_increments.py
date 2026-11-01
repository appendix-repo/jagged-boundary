"""Summarises the increment-negligibility ratings (appendix Section 2.4) from runs/raters/<version>/R*.txt.
Flags a step when its mean rating exceeds 3.5 or any rater gives 5, unless it is a designed step (the 27a/27b
critical pair, or the terminal step 30->31)."""
import glob, json, os, re, statistics, sys
VER = sys.argv[1] if len(sys.argv) > 1 else "v0.2"
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.join(here, "..")
items = json.load(open(os.path.join(root, "instrument", "items.json" if VER == "v0.2" else "items_v0.1.json")))["items"]
DESIGNED = {("27a", "27b"), ("30", "31")}
files = sorted(glob.glob(os.path.join(root, "runs", "raters", VER, "R*.txt")))
ratings = {}
for f in files:
    for line in open(f):
        m = re.match(r"PAIR (\S+)→(\S+) \| (\d) \|", line)
        if m: ratings.setdefault((m[1], m[2]), []).append(int(m[3]))
codes = {i["id"]: i["codes"] for i in items}
print(f"{len(files)} raters, {len(ratings)} pairs")
rows = []
for a, b in zip(items, items[1:]):
    k = (a["id"], b["id"]); r = ratings[k]; mu = statistics.mean(r)
    up = [d for d in codes[b["id"]] if codes[b["id"]][d] > codes[a["id"]][d]]
    flag = "designed" if k in DESIGNED else ("FLAG" if mu > 3.5 or max(r) == 5 else "")
    rows.append((k, r, mu, up, flag))
    print(f"{a['id']:>3}->{b['id']:<3} {r} mean {mu:.2f} rises {','.join(up) or '-':<5} {flag}")
all_r = [x for _, r, *_ in rows for x in r]
print("share of ratings <=2:", round(sum(x <= 2 for x in all_r) / len(all_r), 2))
# agreement: Kendall's W over pairs, ranks within rater (average ranks for ties, tie-corrected)
def ranks(v):
    order = sorted(range(len(v)), key=lambda i: v[i]); r = [0.0] * len(v); i = 0
    while i < len(v):
        j = i
        while j + 1 < len(v) and v[order[j + 1]] == v[order[i]]: j += 1
        for k in range(i, j + 1): r[order[k]] = (i + j) / 2 + 1
        i = j + 1
    return r
m, n = len(files), len(rows)
by_rater = [[r[k] for _, r, *_ in rows] for k in range(m)]
R = [sum(col) for col in zip(*[ranks(v) for v in by_rater])]
S = sum((x - sum(R) / n) ** 2 for x in R)
T = sum(t ** 3 - t for v in by_rater for t in [v.count(x) for x in set(v)])
print("Kendall's W (tie-corrected):", round(12 * S / (m ** 2 * (n ** 3 - n) - m * T), 2))
print("flagged:", [f"{a}->{b}" for (a, b), r, mu, up, fl in rows if fl == "FLAG"])
