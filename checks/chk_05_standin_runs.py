"""Check 05: the tables and counts of appendix Section 4 (and proposal Section 4), recomputed from the run records.

The stand-in interviews cannot be rerun to the same text (a language model answers differently each time). What can be
checked is that every number the appendix reports about them follows from the stored records:

  runs/configs/standins.json      traversals, break-points, focal items, dominance violations   (Section 4.2)
  runs/transcripts/S*.md          participant turns, counted from the transcript itself         (Section 4.2)
  runs/audits/S*_audit.md         the Auditor's JSON: defeaters, directions, leading questions,
                                  assertions, second pushes, pass/fail                          (Section 4.4)
  runs/records/S*_record.json     the interviewer's own record: defeaters, outcomes, recognition (Sections 4.4, 4.5)

The balance and the pass/fail result are recomputed from the Auditor's lists by the rule of Section 3.4, not read from
the Auditor's summary fields. The Auditors wrote their JSON with slightly different key names; the loader normalizes them.

Run from the repository root:  python3 checks/chk_05_standin_runs.py
"""
import json, os, re, sys

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
R = lambda *p: os.path.join(root, "runs", *p)
RUNS = ["S1", "S2", "S3", "S4"]
RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}" + (f": {detail}" if detail else ""))


def audit(s):
    text = open(R("audits", f"{s}_audit.md")).read()
    j = json.loads(re.search(r"```json\n(.*?)\n```", text, re.S).group(1))
    return j.get("Audit", j)


def direction(d):
    d = d.lower().replace("-", "_").replace(" ", "_")
    return "NOT_OK" if "not_ok" in d else "OK"


def balance(n_ok, n_not):
    tot = n_ok + n_not
    return 0.0 if tot == 0 else (n_ok - n_not) / tot


standins = json.load(open(R("configs", "standins.json")))
records = {s: json.load(open(R("records", f"{s}_interviewer_record.json"))) for s in RUNS}
audits = {s: audit(s) for s in RUNS}

# ---------------------------------------------------------------- Section 4.2
print("Section 4.2, the four runs")
TABLE_42 = {  # run: (arm, break, focal, dominance violation, participant turns)
    "S1": ("defeater", "27b", ["27a", "27b", "22", "23"], [["24", "27b"]], 10),
    "S2": ("defeater", "16", ["15", "16"], [], 11),
    "S3": ("defeater", "20", ["19", "20", "26"], [["26", "20"]], 11),
    "S4": ("reflection_only", "19", ["18", "19"], [], 9),
}
for s, (arm, bp, focal, dv, turns) in TABLE_42.items():
    c = standins[s]
    n_part = len(re.findall(r"^\*\*Participant\*\*", open(R("transcripts", f"{s}.md")).read(), re.M))
    n_raw = len(re.findall(r"^\*\*Participant\*\*", open(R("transcripts", f"{s}_raw.md")).read(), re.M))
    check(f"{s}: arm {arm}, break {bp}, focal {focal}, dominance violation {dv or 'none'}",
          c["arm"] == arm and c["break_point"] == bp and c["focal"] == focal and c["dominance_violations"] == dv)
    check(f"{s}: {turns} participant turns in the transcript (cleaned and raw agree)", n_part == turns == n_raw,
          f"cleaned {n_part}, raw {n_raw}; the interviewer's record self-reports {records[s]['participant_turns']}")

# ---------------------------------------------------------------- Section 4.4
print("\nSection 4.4, the audits (balance and result recomputed from the Auditor's lists by the rule of Section 3.4)")
TABLE_44 = {  # run: (interviewer's defeaters, Auditor's defeaters, toward OK, toward NOT_OK, balance, leading, result)
    "S1": (2, 3, 2, 1, +0.33, 0, "pass"),
    "S2": (2, 3, 2, 1, +0.33, 0, "pass"),
    "S3": (2, 4, 2, 2, 0.00, 1, "pass"),
    "S4": (0, 0, 0, 0, 0.00, 0, "pass"),
}
n_pass = 0
for s, (n_int, n_aud, n_ok, n_not, bal, lead, res) in TABLE_44.items():
    a = audits[s]
    dirs = [direction(d["direction"]) for d in a["defeaters"]]
    k_ok, k_not = dirs.count("OK"), dirs.count("NOT_OK")
    b = balance(k_ok, k_not)
    n_lead, n_ass, n_sp = len(a["leading_questions"]), len(a["interviewer_assertions"]), len(a["second_pushes"])
    passed = abs(b) <= 0.34 and n_lead <= 1 and n_ass == 0 and n_sp == 0
    n_pass += passed
    check(f"{s}: interviewer recorded {n_int} defeaters, Auditor {n_aud} ({n_ok} toward OK / {n_not} toward Not OK)",
          len(records[s]["defeaters"]) == n_int and len(dirs) == n_aud and (k_ok, k_not) == (n_ok, n_not),
          f"record {len(records[s]['defeaters'])}, audit {len(dirs)} ({k_ok}/{k_not})")
    check(f"{s}: balance {bal:+.2f}, {lead} leading question(s), 0 assertions, 0 second pushes, {res}",
          round(b, 2) == bal and n_lead == lead and n_ass == 0 and n_sp == 0 and passed == (res == "pass")
          and a["result"].lower() == res,
          f"balance {b:+.3f}, leading {n_lead}, assertions {n_ass}, second pushes {n_sp}, recomputed "
          f"{'pass' if passed else 'fail'}, Auditor wrote {a['result']}")
check("all four interviews pass the audit (proposal Section 4)", n_pass == 4, f"{n_pass} of 4")

# ---------------------------------------------------------------- Section 4.5
print("\nSection 4.5, what the runs exposed")
extra = {s: len(audits[s]["defeaters"]) - len(records[s]["defeaters"]) for s in RUNS[:3]}
check("row 1: in every defeater-arm run the Auditor counted more defeaters than the interviewer recorded",
      all(v > 0 for v in extra.values()), str(extra))
defs = [d for s in RUNS for d in records[s]["defeaters"]]
rec = [d.get("recognized_as_genuine") for d in defs]
check("row 7 and proposal Section 4: four of six defeaters recognized as genuine challenges",
      len(defs) == 6 and sum(bool(x) for x in rec) == 4, f"{sum(bool(x) for x in rec)} of {len(defs)}")
missed = [(s, d["direction"]) for s in RUNS for d in records[s]["defeaters"] if not d.get("recognized_as_genuine")]
check("the two that missed are S1's (toward Not OK on 27a) and S3's (toward Not OK on 19)",
      [m[0] for m in missed] == ["S1", "S3"], str(missed))
outcomes = [d.get("outcome") for d in defs]
check("defeater outcomes: S1 rebutted, revised; S2 abandoned, revised; S3 rebutted, revised (Section 4.3)",
      outcomes == ["rebutted", "revised", "abandoned", "revised", "rebutted", "revised"], str(outcomes))
check("S4 (reflection-only arm): no defeater presented, by the interviewer's record and the Auditor's",
      len(records["S4"]["defeaters"]) == 0 and len(audits["S4"]["defeaters"]) == 0)


def verdict(x):
    """OK / NOT_OK at the start of a free-text or structured judgment, None if neither (e.g. 'split')."""
    if isinstance(x, dict):
        x = x.get("judgment", "")
    m = re.match(r"\s*(NOT_OK|NOT OK|OK)\b", str(x), re.I)
    return None if not m else ("NOT_OK" if "NOT" in m.group(1).upper() else "OK")


changed = []
for s in RUNS[:3]:
    for pc in records[s].get("placement_changes") or []:
        b, a = verdict(pc["before"]), verdict(pc["after"])
        if b and a and a != b:
            changed.append((s, pc["item"]))
check("row 2: no verdict (OK / Not OK) changed in any defeater-arm run; changes were to confidence, conditions or splits",
      changed == [], f"{sum(len(records[s].get('placement_changes') or []) for s in RUNS[:3])} recorded placement changes, "
      f"verdict changes {changed or 'none'}")
s4 = records["S4"]
check("row 2 and Section 4.3: S4 changed no judgment", not s4.get("judgment_changes"), str(s4.get("judgment_changes")))
check("row 8: S4 closed at 9 participant turns, below the v0.1 target of 10 to 14",
      len(re.findall(r"^\*\*Participant\*\*", open(R("transcripts", "S4.md")).read(), re.M)) == 9)

print(f"\n{sum(RESULTS)} of {len(RESULTS)} assertions hold")
print("RESULT:", "PASS" if all(RESULTS) else "FAIL")
sys.exit(0 if all(RESULTS) else 1)
