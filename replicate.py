"""Regenerate every result in the repository and compare it with the stored output.

    python3 replicate.py          # everything, about 3 minutes
    python3 replicate.py --fast   # skips the two slow steps (Check 03 and Check 08), about 10 seconds

Each step is run from the repository root. Its output is compared with the stored file named in the table below,
ignoring only the reported run time. Generated files (instrument/items.json, runs/configs/standins.json,
checks/example_traversal_record.json) are compared byte for byte with the committed versions. The script prints one
line per step and exits with status 0 only if every step reproduces. No step calls an AI model.
"""
import os, re, subprocess, sys, time

ROOT = os.path.dirname(os.path.abspath(__file__))
FAST = "--fast" in sys.argv
PY = sys.executable

# (label, command, stored stdout or None, generated files compared byte for byte, slow)
STEPS = [
    ("Item sequence v0.2 (2.1, 2.2)", ["instrument/build_items.py"], None, ["instrument/items.json"], False),
    ("Stand-in configurations (4.1)", ["runs/configs/make_standins.py"], None, ["runs/configs/standins.json"], False),
    ("Check 01 v0.2, single-increase rule (2.1)", ["checks/chk_01_adjacency.py", "instrument/items.json"], "checks/chk_01_v0.2.out", [], False),
    ("Check 01 v0.1 (2.1)", ["checks/chk_01_adjacency.py", "instrument/items_v0.1.json"], "checks/chk_01_v0.1.out", [], False),
    ("Check 02 round 1, increment ratings (2.4)", ["checks/chk_02_increments.py", "v0.1"], "checks/chk_02_v0.1.out", [], False),
    ("Check 02 round 2 (2.4)", ["checks/chk_02_increments.py", "v0.2"], "checks/chk_02_v0.2.out", [], False),
    ("Check 03, synthetic demonstration and power (7.4, 8)", ["pipeline/run_demo.py"], "checks/chk_03_synthetic_demo.out", [], True),
    ("Check 04, design counts (0, 1, 2, 5.2)", ["checks/chk_04_design_counts.py"], "checks/chk_04_design_counts.out", [], False),
    ("Check 05, stand-in runs (4.2, 4.4, 4.5)", ["checks/chk_05_standin_runs.py"], "checks/chk_05_standin_runs.out", [], False),
    ("Check 06, response schema (5.1, Annex A)", ["checks/chk_06_schema.py"], "checks/chk_06_schema.out", ["checks/example_traversal_record.json"], False),
    ("Check 07, appendix against repository", ["checks/chk_07_appendix_consistency.py"], "checks/chk_07_appendix_consistency.out", [], False),
    ("Check 08, design diagnostics (8.3, 8.4, 10.2, 10.3)", ["pipeline/design_diagnostics.py"], "checks/chk_08_design_diagnostics.out", [], True),
]


def clean(text):
    text = re.sub(r"; \d+ s\n", "\n", text)          # run time printed by run_demo.py
    text = re.sub(r"^EXIT 0\n?", "", text, flags=re.M)  # exit status appended to the stored Check 03 output
    return text.strip()


def main():
    ok_all, t_all = True, time.time()
    for label, cmd, stored, generated, slow in STEPS:
        if slow and FAST:
            print(f"  [SKIP] {label}")
            continue
        before = {f: open(os.path.join(ROOT, f), "rb").read() for f in generated}
        t0 = time.time()
        r = subprocess.run([PY, *cmd], cwd=ROOT, capture_output=True, text=True)
        notes = []
        ok = r.returncode == 0
        if not ok:
            notes.append(f"exit status {r.returncode}: {r.stderr.strip()[-300:]}")
        if stored:
            want = clean(open(os.path.join(ROOT, stored)).read())
            if clean(r.stdout) != want:
                ok = False
                got = clean(r.stdout).splitlines()
                exp = want.splitlines()
                k = next((i for i, (a, b) in enumerate(zip(got, exp)) if a != b), min(len(got), len(exp)))
                notes.append(f"output differs from {stored} at line {k + 1}:\n      got:      "
                             f"{got[k] if k < len(got) else '<end>'}\n      expected: {exp[k] if k < len(exp) else '<end>'}")
        for f in generated:
            if open(os.path.join(ROOT, f), "rb").read() != before[f]:
                ok = False
                notes.append(f"{f} regenerated differently from the committed version")
        ok_all &= ok
        print(f"  [{'OK  ' if ok else 'FAIL'}] {label}  ({time.time() - t0:.0f} s)")
        for n in notes:
            print("      " + n)
    print(f"\n{'All steps reproduce' if ok_all else 'Some steps did not reproduce'} ({time.time() - t_all:.0f} s)"
          + (" [--fast: slow steps skipped]" if FAST else ""))
    print("RESULT:", "PASS" if ok_all else "FAIL")
    sys.exit(0 if ok_all else 1)


if __name__ == "__main__":
    main()
