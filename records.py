"""Conversion between Traversal records (schema/traversal.v0.schema.json, appendix Section 5.1 and Annex A) and the
arrays that measures.py works on.

to_records() writes synthetic respondents from simulate.py as schema records, so that the pipeline can be run on data
in the form the study will collect. from_records() reads records back into arrays indexed by designed position.
Used by checks/chk_06_schema.py. Nothing here describes real researchers.
"""
import numpy as np

MIDS = np.array([0.1, 0.3, 0.5, 0.7, 0.9])
PROBES = [("P1", "2", "10"), ("P2", "17", "21"), ("P3", "22", "29"), ("P4", "26", "27b"), ("P5", "19", "25"), ("P6", "13", "18")]
SUBFIELDS = ["strategy", "ob", "operations", "entrepreneurship"]
STAGES = ["doctoral", "pre_tenure", "post_tenure"]
TRADITIONS = ["formal_modeling", "quantitative_empirical", "qualitative", "mixed", "conceptual"]


def to_bin(m):
    """Bin midpoint (0.1, ..., 0.9) to the schema's bin code 1..5."""
    return int(np.argmin(np.abs(MIDS - m))) + 1


def to_records(pop, ids, anchors, m2=None, m3=None, disclosure=None, version="0.2", seed=0):
    """pop: output of simulate.population. anchors: anchor item ids. m2, m3, disclosure: n x len(anchors) arrays from
    simulate.epinet_layers (optional). Layer versions are allocated A 50%, B 25%, C 25% (Section 9.3)."""
    rng = np.random.default_rng(seed)
    a, arg, orders, pres = pop["a"], pop["arguable"], pop["orders"], pop["pres"]
    n = len(a)
    acol = {x: k for k, x in enumerate(anchors)}
    out = []
    for p in range(n):
        layer = rng.choice(["A", "B", "C"], p=[0.5, 0.25, 0.25])
        shown = {int(i): t + 1 for t, i in enumerate(pres[p])}
        resp = []
        for i, x in enumerate(ids):
            r = dict(item_id=x, shown_at=shown[i], judgment="OK" if a[p, i] else "NOT_OK",
                     confidence="arguable" if arg[p, i] else "firm", latency_ms=int(rng.integers(4000, 20000)))
            if x in acol:
                k = acol[x]
                r["peer_second"] = to_bin(m2[p, k]) if (m2 is not None and layer in "AB") else None
                r["peer_third"] = to_bin(m3[p, k]) if (m3 is not None and layer == "A") else None
                r["disclosure"] = str(disclosure[p, k]) if disclosure is not None else None
            resp.append(r)
        probes = []
        for pid, l, rr in PROBES:
            if rng.random() < 0.5:
                l, rr = rr, l
            li, ri = a[p, ids.index(l)], a[p, ids.index(rr)]
            ans = "equally_acceptable" if li == ri else ("left_more_acceptable" if li > ri else "right_more_acceptable")
            probes.append(dict(probe_id=pid, left=l, right=rr, answer=ans))
        order = str(orders[p])
        out.append(dict(
            participant_id="P%08X" % int(rng.integers(0, 2 ** 32)),
            instrument_version=version,
            condition=dict(order=order, entry_item=ids[int(pres[p][0])] if order == "E" else None,
                           presentation_sequence=[ids[int(i)] for i in pres[p]], layer_version=str(layer),
                           target_stratum=(f"{rng.choice(STAGES)} {rng.choice(SUBFIELDS)}" if layer == "B" else None),
                           interview_arm="none"),
            strata=dict(subfield=str(rng.choice(SUBFIELDS)), career_stage=str(rng.choice(STAGES)),
                        tradition=str(rng.choice(TRADITIONS)), editorial_role=bool(rng.random() < 0.15)),
            responses=resp, probes=probes,
            timing=dict(started="2026-11-01T10:00:00Z", completed="2026-11-01T10:15:00Z"),
            interview_id=None))
    return out


def from_records(records, ids):
    """Arrays indexed by participant and designed position: a (judgments), arguable, orders, and a dict of anchor
    answers (peer_second and peer_third as bin midpoints, NaN where not asked)."""
    pos = {x: i for i, x in enumerate(ids)}
    n, m = len(records), len(ids)
    a = np.zeros((n, m), int)
    arg = np.zeros((n, m), bool)
    m2 = np.full((n, m), np.nan)
    m3 = np.full((n, m), np.nan)
    for p, rec in enumerate(records):
        for r in rec["responses"]:
            i = pos[r["item_id"]]
            a[p, i] = r["judgment"] == "OK"
            arg[p, i] = r["confidence"] == "arguable"
            if r.get("peer_second"):
                m2[p, i] = MIDS[r["peer_second"] - 1]
            if r.get("peer_third"):
                m3[p, i] = MIDS[r["peer_third"] - 1]
    orders = np.array([rec["condition"]["order"] for rec in records])
    return dict(a=a, arguable=arg, orders=orders, m2=m2, m3=m3)
