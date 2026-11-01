"""Builds the stand-in personas' traversals and focal items for the worked interviews (appendix Section 4).
Writes runs/configs/standins.json. The traversals were written by the demonstration operator (Claude) as
plausible patterns, chosen to cover the cases the appendix needs: a halt at the critical pair 27a/27b, an early
halt with low confidence, a dominance violation, and a reflection-only control. They are not data."""
import json, os

here = os.path.dirname(os.path.abspath(__file__))
seq = json.load(open(os.path.join(here, "..", "..", "instrument", "items_v0.1.json")))["items"]  # the demonstration interviews used v0.1
ids = [it["id"] for it in seq]
codes = {it["id"]: it["codes"] for it in seq}

def traversal(accept, arguable):
    return {i: ("OK" if i in accept else "NOT_OK", "arguable" if i in arguable else "firm") for i in ids}

def upto(last):  # all ids up to and including `last`
    return set(ids[: ids.index(last) + 1])

PERSONAS = {
 "S1": dict(arm="defeater",
   persona="Post-tenure professor of strategy at a research university; works mainly in formal modeling (game theory, "
           "industrial organization). Has used LLMs for editing and for literature searches. Believes ideas are cheap and "
           "that the proof, or the derivation, is where a theorist's contribution and accountability lie.",
   strata=dict(subfield="strategy", career_stage="post_tenure", tradition="formal_modeling"),
   accept=upto("27a"), arguable={"22", "23"}),
 "S2": dict(arm="defeater",
   persona="Pre-tenure assistant professor of organizational behavior; qualitative researcher (ethnography, interviews). "
           "Writes carefully and regards the writing as part of the interpretive work. Uses a grammar checker; has tried an "
           "LLM for redrafting and felt uneasy about it.",
   strata=dict(subfield="ob", career_stage="pre_tenure", tradition="qualitative"),
   accept=upto("15") | {"27a"}, arguable={"15", "16"}),
 "S3": dict(arm="defeater",
   persona="Fourth-year doctoral student in operations management; quantitative-empirical (panel data, causal inference). "
           "Uses coding assistants daily for analysis code. Expects to be judged on whether the empirical results are right.",
   strata=dict(subfield="operations", career_stage="doctoral", tradition="quantitative_empirical"),
   accept=upto("19") | {"26", "27a"}, arguable={"19", "26"}),
 "S4": dict(arm="reflection_only",
   persona="Post-tenure professor of entrepreneurship; mixed methods; serves on the editorial board of a major journal. "
           "Has reviewed submissions that appeared to be LLM-written and has views about what reviewers can detect.",
   strata=dict(subfield="entrepreneurship", career_stage="post_tenure", tradition="mixed"),
   accept=upto("18") | {"27a"}, arguable={"18", "19"}),
}

def dominates(j, i):
    cj, ci = codes[j], codes[i]
    return all(cj[d] >= ci[d] for d in cj) and any(cj[d] > ci[d] for d in cj)

out = {}
for pid, p in PERSONAS.items():
    t = traversal(p["accept"], p["arguable"])
    first_rej = next(i for i in ids if t[i][0] == "NOT_OK")
    last_acc_before = ids[ids.index(first_rej) - 1]
    dv = [(j, i) for j in ids for i in ids if t[j][0] == "OK" and t[i][0] == "NOT_OK" and dominates(j, i)]
    same = [(a, b) for a in ids for b in ids if ids.index(a) < ids.index(b) and codes[a] == codes[b] and t[a][0] != t[b][0]]
    focal = [last_acc_before, first_rej] + [i for i in ids if t[i][1] == "arguable" and i not in (last_acc_before, first_rej)][:2]
    out[pid] = dict(arm=p["arm"], persona=p["persona"], strata=p["strata"],
                    traversal=[{"item": i, "judgment": t[i][0], "confidence": t[i][1]} for i in ids],
                    break_point=first_rej, focal=focal, dominance_violations=dv, parallel_inconsistencies=same)
    print(pid, p["arm"], "break at", first_rej, "focal", focal, "DV", dv, "parallel", same)
json.dump(out, open(os.path.join(here, "standins.json"), "w"), indent=1)
