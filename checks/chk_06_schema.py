"""Check 06: the response schema (appendix Section 5.1, Annex A) is valid JSON Schema and records what the pipeline needs.

1. schema/traversal.v0.schema.json is a valid draft 2020-12 schema.
2. 400 synthetic traversals (simulate.py, scenario P3, with Epinet layers), written as records by pipeline/records.py,
   all validate, across the four order conditions and the three layer versions.
3. Read back from the records, they give the same arrays, and the same measures, as the simulator produced directly.
4. Malformed records are rejected (wrong identifier pattern, 36 responses, a bin outside 1..5, an unknown order).
5. The four stand-in audits (runs/audits/), mapped to the schema's Audit object, validate.

The four stand-in traversals are not validated as Traversal records: they used instrument v0.1 (32 items), and the
v0.2 schema requires 37 responses. Requires the jsonschema package. Nothing here describes real researchers.

Run from the repository root:  python3 checks/chk_06_schema.py
"""
import copy, json, os, re, sys
import numpy as np

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, os.path.join(root, "pipeline"))
import measures as M, simulate as sim, records as REC
from jsonschema import Draft202012Validator

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}" + (f": {detail}" if detail else ""))


schema = json.load(open(os.path.join(root, "schema", "traversal.v0.schema.json")))
spec = json.load(open(os.path.join(root, "instrument", "items.json")))
ids, anchors = [it["id"] for it in spec["items"]], spec["anchors"]
codes = M.code_matrix(spec["items"])

print("1. The schema")
try:
    Draft202012Validator.check_schema(schema)
    check("valid JSON Schema, draft 2020-12", True, schema["$id"])
except Exception as e:  # noqa: BLE001
    check("valid JSON Schema, draft 2020-12", False, str(e)[:200])
V = Draft202012Validator(schema)

print("\n2. Synthetic traversals written as records")
N = 400
kw = dict(classes=["generation", "core", "tool"], class_mix=[0.4, 0.35, 0.25], theta_mu=[0.60, 0.60, 0.65],
          theta_sd=0.15, alpha=8, h=1.0)
pop = sim.population(N, codes, ids, seed=12, retest_share=0, **kw)
aidx = [ids.index(x) for x in anchors]
m2, m3, disc = sim.epinet_layers(pop["a"][:, aidx], np.zeros(len(anchors)), 0.15, -0.05, -1.0, np.log(1.5),
                                 np.random.default_rng(3))
recs = REC.to_records(pop, ids, anchors, m2, m3, disc, seed=4)
errs = [e for r in recs for e in V.iter_errors(r)]
orders = sorted({r["condition"]["order"] for r in recs})
layers = sorted({r["condition"]["layer_version"] for r in recs})
check(f"{N} records validate", not errs, f"{len(errs)} errors" + (f"; first: {errs[0].message[:120]}" if errs else ""))
check("all four order conditions and all three layer versions occur", orders == list("EFRS") and layers == list("ABC"),
      f"orders {orders}, layers {layers}")
one = recs[0]
path = os.path.join(root, "checks", "example_traversal_record.json")
json.dump(one, open(path, "w"), indent=1)
print(f"  (one record written to checks/example_traversal_record.json, {len(json.dumps(one))} bytes)")

print("\n3. Round trip: records back to arrays")
back = REC.from_records(recs, ids)
check("judgments, confidence tags and orders identical", (back["a"] == pop["a"]).all()
      and (back["arguable"] == pop["arguable"]).all() and (back["orders"] == pop["orders"]).all())
dom = M.dominance(codes)
same = (np.array_equal(M.break_point(back["a"]), M.break_point(pop["a"]))
        and np.allclose(M.dominance_violations(back["a"], dom), M.dominance_violations(pop["a"], dom)))
check("break-points and dominance violations identical", same)
isA = np.array([r["condition"]["layer_version"] == "A" for r in recs])
m2b = back["m2"][:, aidx]
check("second-order answers present for versions A and B only, third-order for A only",
      np.isfinite(m2b[isA]).all() and np.isnan(back["m3"][:, aidx][~isA]).all()
      and np.isnan(m2b[[r["condition"]["layer_version"] == "C" for r in recs]]).all())
check("binned answers read back as the simulator's midpoints", np.allclose(m2b[isA], m2[isA]))

print("\n4. Malformed records are rejected")


def rejected(mutate):
    r = copy.deepcopy(one)
    mutate(r)
    return not V.is_valid(r)


check("participant id not of the form P + 8 hex digits", rejected(lambda r: r.update(participant_id="P123")))
check("36 responses instead of 37", rejected(lambda r: r["responses"].pop()))
check("a peer-belief bin of 6", rejected(lambda r: r["responses"][1].update(peer_second=6)))
check("an order condition other than F, R, E, S", rejected(lambda r: r["condition"].update(order="X")))
check("a judgment other than OK / NOT_OK", rejected(lambda r: r["responses"][0].update(judgment="MAYBE")))

print("\n5. The stand-in audits as schema Audit objects")
AV = Draft202012Validator({"$ref": "#/$defs/Audit", "$defs": schema["$defs"]})
for s in ["S1", "S2", "S3", "S4"]:
    t = open(os.path.join(root, "runs", "audits", f"{s}_audit.md")).read()
    j = json.loads(re.search(r"```json\n(.*?)\n```", t, re.S).group(1))
    j = j.get("Audit", j)
    dirs = ["NOT_OK" if "not_ok" in d["direction"].lower() else "OK" for d in j["defeaters"]]
    k_ok, k_not = dirs.count("OK"), dirs.count("NOT_OK")
    obj = dict(auditor_model="claude-opus-5-5", n_toward_OK=k_ok, n_toward_NOT_OK=k_not,
               balance=0.0 if not dirs else (k_ok - k_not) / len(dirs), leading_questions=len(j["leading_questions"]),
               interviewer_assertions=len(j["interviewer_assertions"]), **{"pass": j["result"].lower() == "pass"})
    e = list(AV.iter_errors(obj))
    check(f"{s} audit validates", not e, json.dumps(obj) if not e else e[0].message)

print(f"\n{sum(RESULTS)} of {len(RESULTS)} assertions hold")
print("RESULT:", "PASS" if all(RESULTS) else "FAIL")
sys.exit(0 if all(RESULTS) else 1)
