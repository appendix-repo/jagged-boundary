"""Synthetic-data demonstration of the analysis pipeline (appendix Section 8).

Generates synthetic respondents under three planted structures, runs the measures of Section 5.2 and the decision
rules of Section 6.1 on them, and checks that the planted structure is recovered. Then estimates power for the main
tests. Every number this script prints is about synthetic data; none describes real researchers.

Run:  python3 run_demo.py [--quick]
"""
import json, os, sys, time
import numpy as np
from scipy.stats import mannwhitneyu, ttest_1samp, wilcoxon
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import measures as M, simulate as sim, norm_dynamics as nd

QUICK = "--quick" in sys.argv
here = os.path.dirname(os.path.abspath(__file__))
spec = json.load(open(os.path.join(here, "..", "instrument", "items.json")))
items, ids = spec["items"], [it["id"] for it in spec["items"]]
codes = M.code_matrix(items)
dom = M.dominance(codes)
anchors = [ids.index(x) for x in spec["anchors"]]
CHECKS = []


def check(name, ok, detail):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")


SCENARIOS = {
    "P1 shared sharp line": dict(classes=["generation"], class_mix=[1.0], theta_mu=[0.60], theta_sd=0.02, alpha=100, h=0.0),
    "P2 private sharp lines, three heuristics": dict(classes=["generation", "core", "tool"], class_mix=[0.4, 0.35, 0.25],
                                                    theta_mu=[0.60, 0.60, 0.65], theta_sd=0.15, alpha=100, h=0.0),
    "P3 no sharp lines, three heuristics, hysteresis": dict(classes=["generation", "core", "tool"], class_mix=[0.4, 0.35, 0.25],
                                                          theta_mu=[0.60, 0.60, 0.65], theta_sd=0.15, alpha=8, h=1.0),
}
PLANTED = {"P1 shared sharp line": ("P1", 1, False),
           "P2 private sharp lines, three heuristics": ("P2", 3, False),
           "P3 no sharp lines, three heuristics, hysteresis": ("P3", 3, True)}
N = 1000

print(f"Synthetic demonstration, instrument v{spec['version']}, {len(ids)} items, N = {N} per scenario\n")
t0 = time.time()
for si, (name, kw) in enumerate(SCENARIOS.items()):
    pic_true, k_true, hyst_true = PLANTED[name]
    pop = sim.population(N, codes, ids, seed=10 + si, **kw)
    a, arg, orders = pop["a"], pop["arguable"], pop["orders"]
    A = a.mean(0)
    bp = M.break_point(a)
    dv = M.dominance_violations(a, dom)
    H = M.loevinger_H(a)
    kbest, fits = M.mixture_rasch(a, kmax=4 if QUICK else 5, restarts=2 if QUICK else 3)
    cross, taus = M.orderings_cross(fits[kbest]["theta"], pi=fits[kbest]["pi"])
    pic = M.picture(a, arg, dom, kbest, cross, H, A, pop["retest_shift"])
    bpF, bpR = bp[orders == "F"], bp[orders == "R"]
    hdiff = float(np.median(bpF) - np.median(bpR))
    # hysteresis is tested on the acceptance count, which is less noisy than the first rejection (Section 5.2)
    cF, cR = a[orders == "F"].sum(1), a[orders == "R"].sum(1)
    cdiff = float(cF.mean() - cR.mean())
    p_h = mannwhitneyu(cF, cR).pvalue
    fr = pop["retest_fr"][~np.isnan(pop["retest_fr"])]
    p_w = wilcoxon(fr).pvalue if np.any(fr != 0) else 1.0
    print(f"{name}")
    print(f"  break-point IQR {M.iqr(bp):.1f}; field band {M.field_band(A):.0f}; J {M.jaggedness(A, codes):.2f}; "
          f"mean DV {dv.mean():.3f}; Loevinger H {H:.2f}; BIC classes {kbest}; orderings cross {cross}; "
          f"sharp individuals {M.sharp_individuals(a, arg, dom, pop['retest_shift']).mean():.2f}")
    print(f"  median BP forward {np.median(bpF):.0f}, reverse {np.median(bpR):.0f} (diff {hdiff:+.1f}); "
          f"mean items accepted forward {cF.mean():.1f}, reverse {cR.mean():.1f} (diff {cdiff:+.2f}, Mann-Whitney p = {p_h:.3g}); "
          f"within-person retest (n = {len(fr)}): mean F - R {fr.mean():+.2f} items, Wilcoxon p = {p_w:.3g}")
    check(f"{pic_true}: picture recovered", pic == pic_true, f"classified {pic}")
    check(f"{pic_true}: number of heuristics recovered", kbest == k_true and (cross == (k_true > 1)), f"BIC selects {kbest}, crossing {cross}")
    if hyst_true:
        check(f"{pic_true}: hysteresis detected (within-person retest)", p_w < 0.05 and fr.mean() > 0, f"F - R {fr.mean():+.2f} items, p = {p_w:.3g}")
    else:
        check(f"{pic_true}: no hysteresis found", abs(hdiff) <= 1 and abs(cdiff) <= 1, f"BP difference {hdiff:+.1f} positions, count difference {cdiff:+.2f}")

    if si == 2:  # Epinet layers and the norm-dynamics model on the P3 population
        rng = np.random.default_rng(99)
        aA = a[:, anchors]
        pid = np.repeat(np.arange(N)[:, None], len(anchors), 1)
        bias = np.array([-0.15 if spec["anchors"][j] in ("14", "17", "19", "22") else 0.0 for j in range(len(anchors))])
        m2, m3, disc = sim.epinet_layers(aA, pi_bias=bias, projection=0.15, group_bias=-0.05, disc_b0=-1.0,
                                         disc_b1_per_bin=np.log(1.5), rng=rng)
        ep = M.epinet(aA, m2, m3)
        print("\nEpinet layers (planted: PI = -0.15 at anchors 14, 17, 19, 22 before binning, 0 elsewhere; projection 0.15)")
        print("  anchor  " + " ".join(f"{x:>6}" for x in spec["anchors"]))
        for key in ("A", "PI", "FC", "TFC"):
            print(f"  {key:<6}  " + " ".join(f"{v:6.2f}" for v in ep[key]))
        gen = [j for j, x in enumerate(spec["anchors"]) if x in ("14", "17", "19", "22")]
        check("PI recovered at the generative anchors", ep["PI"][gen].mean() < -0.10, f"mean PI {ep['PI'][gen].mean():+.3f}")
        check("false consensus recovered", (ep["FC"] > 0).mean() >= 0.8, f"FC > 0 at {(ep['FC'] > 0).sum()} of {len(anchors)} anchors")
        acc = aA == 1
        y = (disc[acc] == "would_not_disclose").astype(float)
        b, se = M.logit_fit(ep["g"][acc], y, cluster=pid[acc])
        orb, lo, hi = (np.exp(x * 0.2) for x in (b[1], b[1] - 1.96 * se[1], b[1] + 1.96 * se[1]))
        check("H5 effect recovered (OR per bin of concealment pressure, planted 1.50)", lo <= 1.5 <= hi and lo > 1,
              f"OR {orb:.2f} [{lo:.2f}, {hi:.2f}], cluster-robust")

        print("\nNorm-dynamics model (Section 7) at each anchor; threshold distribution estimated from the disclosure data")
        for label, b1 in (("weak link (planted OR 1.5 per bin)", np.log(1.5)), ("strong link (planted OR 4 per bin)", np.log(4.0))):
            b0 = -0.5 * b1 / 0.2 if b1 > 1 else -1.0
            _, m3s, discs = sim.epinet_layers(aA, pi_bias=bias, projection=0.15, group_bias=-0.05, disc_b0=b0,
                                              disc_b1_per_bin=b1, rng=np.random.default_rng(5))
            yd = (discs[acc] == "would_disclose").astype(float)
            b2, _ = M.logit_fit(m3s[acc], yd)
            s_hat, mu_hat = 1 / b2[1], -b2[0] / b2[1]
            print(f"  {label}: estimated threshold location {mu_hat:.2f}, scale {s_hat:.2f}")
            print("    anchor   A    V*   Delta  equilibria")
            rows = []
            for j, x in enumerate(spec["anchors"]):
                e = m3s[:, j] - m3s[:, j].mean()
                v, d = nd.tipping(m3s[:, j].mean(), aA[:, j], e, mu_hat, s_hat)
                fp = nd.fixed_points(aA[:, j], e, mu_hat, s_hat)
                rows.append((x, ep["A"][j], v, d))
                print(f"    {x:>6}  {ep['A'][j]:.2f}  {v:.2f}  " + (f"{d:+.2f}" if np.isfinite(d) else " none") + f"  {len(fp)}")
            priv = [x for x, A_, v, d in rows if A_ >= 0.5]
            vis = [x for x, A_, v, d in rows if v >= 0.5]
            fin = sorted((abs(d), x) for x, A_, v, d in rows if np.isfinite(d))
            print(f"    private line (last anchor, in sequence order, accepted by half): {priv[-1] if priv else 'none'}; "
                  f"visible line (last anchor openly practised and disclosed by half): {vis[-1] if vis else 'none'}; "
                  + (f"most movable anchor {fin[0][1]} (|Delta| = {fin[0][0]:.2f})" if fin else "no anchor movable"))
            check(f"{label}: visible line never later than private line",
                  (not vis) or (bool(priv) and ids.index(vis[-1]) <= ids.index(priv[-1])), "equilibrium disclosure cannot exceed private acceptance")
    print()

# ---------------- power ----------------
print("Power (share of synthetic replications in which the test rejects at alpha = 0.05)")
reps = 40 if QUICK else 200
Ns = [300, 600, 1000]
rng = np.random.default_rng(7)
kw = SCENARIOS["P3 no sharp lines, three heuristics, hysteresis"]
for h in (0.5, 1.0):
    btw, w20, w40 = [], [], []
    for n in Ns:
        hb = h20 = h40 = 0
        for r in range(reps):
            pop = sim.population(n, codes, ids, seed=1000 + r, **{**kw, "h": h})
            c, o = pop["a"].sum(1), pop["orders"]
            hb += mannwhitneyu(c[o == "F"], c[o == "R"]).pvalue < 0.05
            fr = pop["retest_fr"][~np.isnan(pop["retest_fr"])]
            h20 += np.any(fr != 0) and wilcoxon(fr).pvalue < 0.05
            pop = sim.population(n, codes, ids, seed=5000 + r, **{**kw, "h": h}, retest_share=0.4)
            fr = pop["retest_fr"][~np.isnan(pop["retest_fr"])]
            h40 += np.any(fr != 0) and wilcoxon(fr).pvalue < 0.05
        btw.append(hb / reps); w20.append(h20 / reps); w40.append(h40 / reps)
    for lab, v in (("between orders", btw), ("retest 20% (as designed)", w20), ("retest 40%", w40)):
        print(f"  {'hysteresis h = ' + str(h) + ', ' + lab:<44} " + "  ".join(f"N={n}: {p:.2f}" for n, p in zip(Ns, v)))
for label, pi in (("pluralistic ignorance, PI = -0.05", -0.05), ("pluralistic ignorance, PI = -0.10", -0.10)):
    out = []
    for n in Ns:
        hits = 0
        for r in range(reps):
            a = (rng.random((n, 1)) < 0.5).astype(int)
            m2, _, _ = sim.epinet_layers(a, np.array([pi]), 0.15, -0.05, -1.0, np.log(1.5), rng)
            hits += ttest_1samp(m2[:, 0] - a[:, 0], 0).pvalue < 0.05  # mean(m2) - A, with A's sampling error
        out.append(hits / reps)
    print(f"  {label:<44} " + "  ".join(f"N={n}: {p:.2f}" for n, p in zip(Ns, out)))
for label, orr in (("H5, OR 1.2 per bin (11 anchors)", 1.2), ("H5, OR 1.5 per bin (11 anchors)", 1.5)):
    out = []
    for n in Ns:
        hits = 0
        for r in range(reps):
            a = (rng.random((n, 11)) < 0.5).astype(int)
            m2, m3, disc = sim.epinet_layers(a, np.zeros(11), 0.15, -0.05, -1.0, np.log(orr), rng)
            acc = a == 1
            pid = np.repeat(np.arange(n)[:, None], 11, 1)
            b, se = M.logit_fit((a - m3)[acc], (disc[acc] == "would_not_disclose").astype(float), cluster=pid[acc])
            hits += abs(b[1] / se[1]) > 1.96
        out.append(hits / reps)
    print(f"  {label:<44} " + "  ".join(f"N={n}: {p:.2f}" for n, p in zip(Ns, out)))
out = []
creps = 10 if QUICK else 30
for n in Ns:
    hits = 0
    for r in range(creps):
        pop = sim.population(n, codes, ids, seed=2000 + r, **kw, retest_share=0)
        k, _ = M.mixture_rasch(pop["a"], kmax=4, restarts=1)
        hits += k == 3
    out.append(hits / creps)
print(f"  {'three classes selected by BIC (P3)':<44} " + "  ".join(f"N={n}: {p:.2f}" for n, p in zip(Ns, out))
      + f"   ({creps} replications)")

print(f"\n{sum(ok for _, ok in CHECKS)} of {len(CHECKS)} recovery checks passed; {time.time() - t0:.0f} s")
print("RESULT:", "PASS" if all(ok for _, ok in CHECKS) else "FAIL")
