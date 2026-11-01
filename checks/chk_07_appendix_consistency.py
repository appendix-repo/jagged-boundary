"""Check 07: the technical appendix and this repository say the same thing.

Reads docs/JAGGED_TECHNICAL_APPENDIX.md (the appendix as submitted) and compares, mechanically:

  Section 2.1   the design matrix (positions, items, regimes, codes, anchors)      with instrument/items.json
  Section 2.2   the item texts                                                     with instrument/items.json
  Section 2.4   the flagged steps, their ratings and Kendall's W                   with the outputs of Check 02
  Section 7.4   the norm-dynamics numbers                                          with the output of Check 03
  Section 8.2   the recovered quantities                                           with the output of Check 03
  Section 8.4   the power table                                                    with the outputs of Checks 03 and 08
  Annex A       the schema                                                         with schema/traversal.v0.schema.json
  Annex B       every check output                                                 with checks/*.out (the run time is ignored)
  Annex C       the instruction sets                                               with instruction-sets/JAGGED_INSTRUCTION_SETS.md
  Annex D       the transcripts and audits                                         with runs/transcripts/S*.md, runs/audits/S*_audit.md
  Annex E       the Project Lakatos tables                                         with lakatos/LAKATOS_TABLES_1-4.md

Text is compared after collapsing whitespace and heading markers, since the annexes nest the files' headings one
level deeper. Run from the repository root:  python3 checks/chk_07_appendix_consistency.py
"""
import json, os, re, sys

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
P = lambda *p: os.path.join(root, *p)
app = open(P("docs", "JAGGED_TECHNICAL_APPENDIX.md")).read()
items = json.load(open(P("instrument", "items.json")))
RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}" + (f": {detail}" if detail else ""))


def norm(t):
    return " ".join(re.sub(r"^#+\s*", "", t, flags=re.M).split())


def section(start, end=None):
    i = app.index(start)
    return app[i: app.index(end, i) if end else len(app)]


def strip_time(t):
    return re.sub(r"; \d+ s\n", "\n", t)


def out(name):
    return open(P("checks", name)).read()


# ------------------------------------------------------------------ 2.1, 2.2
print("Sections 2.1 and 2.2 against instrument/items.json")
rows = re.findall(r"^\| (\d+) \| \*?([0-9]+[ab]?)\*? \| (R\d) \| (\d) \| (\d) \| (\d) \| (\d) \| (\d) \| [^|]* \| (✓?) \|$",
                  section("**The matrix.**", "### 2.2"), re.M)
mat = [(int(p), i, r, tuple(map(int, c)), a == "✓") for p, i, r, *c, a in
       [(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]) for x in rows]]
js = [(it["position"], it["id"], it["regime"], tuple(it["codes"][d] for d in "TCGSH"), it["anchor"]) for it in items["items"]]
check("design matrix: 37 rows, identical positions, items, regimes, codes and anchors", mat == js,
      f"{len(mat)} rows parsed" + ("" if mat == js else f"; first difference {next((a, b) for a, b in zip(mat, js) if a != b)}"))
s22 = section("### 2.2", "### 2.3")
texts = dict(re.findall(r"^(\d+[ab]?)\. (?:⚓ )?(\.\.\..*?\?)", s22, re.M))
bad = [it["id"] for it in items["items"] if texts.get(it["id"]) != it["text"]]
check("item texts: all 37 identical", len(texts) == 37 and not bad, f"{len(texts)} parsed; differing {bad or 'none'}")
check("the fixed stem is identical", items["stem"] in s22)

# ------------------------------------------------------------------ 2.4
print("\nSection 2.4 against Check 02")
s24 = section("### 2.4", "## 3.")
o1, o2 = out("chk_02_v0.1.out"), out("chk_02_v0.2.out")
for tab_start, o, rnd in (("**Round 1", o1, "round 1"), ("**Round 2", o2, "round 2")):
    tab = section(tab_start, "**Revision.**" if rnd == "round 1" else "The designed steps")
    flags = re.findall(r"^\| (\S+→\S+) \| ([\d, ]+) \|", tab, re.M)
    got = {m[0].strip(): m[1].replace(" ", "") for m in re.findall(r"^\s*(\S+->\S+)\s+\[([\d, ]+)\].*FLAG$", o, re.M)}
    want = {s.replace("→", "->"): r.replace(" ", "") for s, r in flags}
    check(f"{rnd}: flagged steps and their ratings", got == want, f"{sorted(want)}")
w1 = re.search(r"Kendall's W \(tie-corrected\): ([\d.]+)", o1).group(1)
w2 = re.search(r"Kendall's W \(tie-corrected\): ([\d.]+)", o2).group(1)
check("Kendall's W 0.96 (v0.1) and 0.95 (v0.2)", f"*W* = {w1} for v0.1 and {w2} for v0.2" in s24, f"{w1}, {w2}")
sh = re.search(r"share of ratings <=2: ([\d.]+)", o1).group(1)
check("round 1: half of all ratings (52%) were 1 or 2", float(sh) == 0.52 and "(52%)" in s24, sh)
d1 = re.search(r"27a->27b \[[\d, ]+\] mean ([\d.]+)", o2).group(1)
d2 = re.search(r"30->31\s+\[[\d, ]+\] mean ([\d.]+)", o2).group(1)
check("designed steps rated 3.67 (27a->27b) and 4.33 (30->31)", f"rated {d1} (27a→27b) and {d2} (30→31)" in s24, f"{d1}, {d2}")

# ------------------------------------------------------------------ 7.4, 8.2
print("\nSections 7.4 and 8.2 against Check 03")
o3 = out("chk_03_synthetic_demo.out")
s74, s82 = section("### 7.4", "## 8."), section("### 8.2", "### 8.3")
strong = o3[o3.index("strong link"):]
mov = re.search(r"most movable anchor (\S+) \(\|Delta\| = ([\d.]+)\)", strong)
row14 = re.search(r"^\s+14\s+([\d.]+)\s+([\d.]+)", strong, re.M)
check("7.4: most movable anchor is item 10, |Delta| 0.31", mov.groups() == ("10", "0.31") and "about 0.31" in s74, str(mov.groups()))
check("7.4: item 14, 78% accept, 7% openly practise", row14.groups() == ("0.78", "0.07") and "78% accept, 7% openly practise" in s74,
      str(row14.groups()))
three = re.findall(r"^\s+(\S+)\s+[\d.]+\s+[\d.]+\s+-[\d.]+\s+3$", strong, re.M)
check("7.4: anchors 2, 7 and 10 have three fixed points under the strong link", three == ["2", "7", "10"], str(three))
weak = o3[o3.index("weak link"):o3.index("strong link")]
check("7.4: weak link, private line 27a, no visible line", "private line (last anchor, in sequence order, accepted by half): 27a; "
      "visible line (last anchor openly practised and disclosed by half): none" in weak)
p1 = o3[o3.index("P1 shared"):o3.index("P2 private")]
p2 = o3[o3.index("P2 private"):o3.index("P3 no sharp")]
p3 = o3[o3.index("P3 no sharp"):o3.index("Epinet layers")]
check("8.2 P1: IQR 0, field band 2", "break-point IQR 0.0; field band 2;" in p1 and "break-point IQR 0; field band 2" in s82)
check("8.2 P2: H 0.78, 61% sharp", "Loevinger H 0.78" in p2 and "sharp individuals 0.61" in p2 and "*H* = 0.78; 61%" in s82)
check("8.2 P3: 2% sharp, forward accepts 1.1 more items, Wilcoxon p = 0.002",
      "sharp individuals 0.02" in p3 and "mean F - R +1.10 items, Wilcoxon p = 0.00188" in p3 and "1.1 more items than reverse (Wilcoxon *p* = 0.002)" in s82)
check("8.2 Epinet: mean PI -0.14, OR 1.51 [1.45, 1.57]", "mean PI -0.141" in o3 and "OR 1.51 [1.45, 1.57]" in o3
      and "Mean PI −0.14" in s82 and "OR 1.51 [1.45, 1.57]" in s82)
check("8.2: all 14 recovery checks pass", "14 of 14 recovery checks passed" in o3 and "All 14 recovery checks pass" in s82)
s83 = section("### 8.3", "### 8.4")
check("8.3 (1): H 0.39 in P1 against 0.78 in P2", "Loevinger H 0.39" in p1 and "(0.39 in the P1 scenario, against 0.78 in P2)" in s83)
pi_hi = re.search(r"^  PI\s+(-?[\d.]+)", o3, re.M).group(1)
check("8.3 (5): PI -0.09 at anchors nearly everyone accepts, where none was planted", pi_hi == "-0.09" and "as −0.09 where none" in s83, pi_hi)

# ------------------------------------------------------------------ 8.4
print("\nSection 8.4 against Checks 03 and 08")
s84 = section("### 8.4", "## 9.")


def nums(line):
    return re.findall(r"N=\d+: ([\d.]+)", line)


def demo(label):
    return nums(next(l for l in o3.splitlines() if l.strip().startswith(label)))


def table(label):
    row = next(l for l in s84.splitlines() if l.startswith("| " + label))
    return [c.strip() for c in row.split("|")[3:6]]


pairs = [("H2, between orders", "hysteresis h = 1.0, between orders"),
         ("H2, retest as first designed", "hysteresis h = 1.0, retest 20% (as designed)"),
         ("H2, retest from F and R only (0.2", "hysteresis h = 1.0, retest 40%"),
         ("H2, retest from F and R only |", "hysteresis h = 0.5, retest 40%"),
         ("H4, one anchor | PI = −0.05", "pluralistic ignorance, PI = -0.05"),
         ("H4, one anchor | PI = −0.10", "pluralistic ignorance, PI = -0.10"),
         ("H5, 11 anchors", "H5, OR 1.2 per bin"),
         ("H3, three heuristics", "three classes selected by BIC (P3)")]
for tl, dl in pairs:
    t, d = table(tl), demo(dl)
    check(f"power row '{tl.rstrip(' |')}'", t == d, f"appendix {t}, Check 03 {d}")
o8 = out("chk_08_design_diagnostics.out")
check("H3 interval 'roughly 0.74 to 0.97' (Check 08)", "[0.74, 0.97]" in o8 and "roughly 0.74 to 0.97" in s84)
s103 = section("### 10.3", "### 10.4")
check("10.3: 65 per arm gives power 0.8 for 0.40 against 0.65 (Check 08)",
      re.search(r"power at 65 per arm 0\.8\d", o8) is not None and "65 per arm detects a difference in placement change of 0.40 against 0.65 with power 0.8" in s103)

# ------------------------------------------------------------------ Annexes
print("\nAnnexes A to E against the repository files")
annexA = json.loads(re.search(r"```json\n(.*?)\n```", section("## Annex A.", "## Annex B."), re.S).group(1))
check("Annex A is schema/traversal.v0.schema.json", annexA == json.load(open(P("schema", "traversal.v0.schema.json"))))
blocks = re.findall(r"```\n(.*?)```", section("## Annex B.", "## Annex C."), re.S)
files = ["chk_01_v0.2.out", "chk_01_v0.1.out", "chk_02_v0.1.out", "chk_02_v0.2.out", "chk_03_synthetic_demo.out"]
for b, f in zip(blocks, files):
    check(f"Annex B block = checks/{f}", strip_time(b).strip() == strip_time(out(f)).strip())
check("Annex B has exactly these five blocks", len(blocks) == 5, str(len(blocks)))
C, D, E = (norm(section(a, b)) for a, b in (("## Annex C.", "## Annex D."), ("## Annex D.", "## Annex E."), ("## Annex E.", None)))
check("Annex C contains instruction-sets/JAGGED_INSTRUCTION_SETS.md (body after its title)",
      norm(open(P("instruction-sets", "JAGGED_INSTRUCTION_SETS.md")).read().split("\n", 1)[1]) in C)
for s in ["S1", "S2", "S3", "S4"]:
    t = norm(open(P("runs", "transcripts", f"{s}.md")).read().split("\n", 1)[1])
    a = norm(open(P("runs", "audits", f"{s}_audit.md")).read().replace("AUDIT", "", 1))
    check(f"Annex D contains runs/transcripts/{s}.md and runs/audits/{s}_audit.md", t in D and a in D)
check("Annex E contains lakatos/LAKATOS_TABLES_1-4.md", norm(open(P("lakatos", "LAKATOS_TABLES_1-4.md")).read().split("\n", 1)[1]) in E)

print(f"\n{sum(RESULTS)} of {len(RESULTS)} assertions hold")
print("RESULT:", "PASS" if all(RESULTS) else "FAIL")
sys.exit(0 if all(RESULTS) else 1)
