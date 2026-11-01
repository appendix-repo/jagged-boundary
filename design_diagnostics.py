"""Design diagnostics behind appendix Sections 8.3, 8.4, 10.2 and 10.3 that run_demo.py does not print.

  8.3 (2)  the first rejection is a noisy break-point: power of the hysteresis tests on the break-point against the
           tests on the acceptance count, on the same synthetic populations
  8.3 (4)  a plain latent-class model over-counts heuristics where the mixture Rasch model does not
  8.4      the 95% interval on the H3 power estimate (27 of 30 replications at N = 1,000)
  10.2     the number of invitations implied by the target N and the response rate
  10.3     the power of 65 interviews per arm for a placement-change difference of 0.40 against 0.65

Items 8.3 (1), (3) and (5), and the power table of 8.4, are printed by run_demo.py (checks/chk_03_synthetic_demo.out).
Every number printed here is about synthetic data or is arithmetic on the design; none describes real researchers.

Run from the repository root:  python3 pipeline/design_diagnostics.py [--quick]
"""
import json, os, sys, time
import numpy as np
from scipy.stats import mannwhitneyu, norm, wilcoxon

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import measures as M, simulate as sim

QUICK = "--quick" in sys.argv
spec = json.load(open(os.path.join(here, "..", "instrument", "items.json")))
ids = [it["id"] for it in spec["items"]]
codes = M.code_matrix(spec["items"])
P3 = dict(classes=["generation", "core", "tool"], class_mix=[0.4, 0.35, 0.25], theta_mu=[0.60, 0.60, 0.65],
          theta_sd=0.15, alpha=8, h=1.0)
P2 = {**P3, "alpha": 100, "h": 0.0}
t0 = time.time()


def latent_class(a, kmax=8, restarts=3, iters=500, seed=0):
    """Plain (unrestricted) latent-class model for binary items, fit by EM; K selected by BIC. Each class has its own
    acceptance probability for every item, with no person parameter within a class."""
    rng = np.random.default_rng(seed)
    keep = (a.mean(0) > 0) & (a.mean(0) < 1)
    a = a[:, keep].astype(float)
    n, m = a.shape
    bic = {}
    for k in range(1, kmax + 1):
        best = -np.inf
        for _ in range(restarts):
            p = rng.uniform(0.2, 0.8, (k, m))
            pi = np.full(k, 1 / k)
            old = -np.inf
            for _ in range(iters):
                lp = a @ np.log(p).T + (1 - a) @ np.log(1 - p).T + np.log(pi)
                mx = lp.max(1, keepdims=True)
                ll = float((mx[:, 0] + np.log(np.exp(lp - mx).sum(1))).sum())
                r = np.exp(lp - mx)
                r /= r.sum(1, keepdims=True)
                pi = np.clip(r.mean(0), 1e-6, None)
                p = np.clip((r.T @ a) / r.sum(0)[:, None], 1e-4, 1 - 1e-4)
                if ll - old < 1e-6:
                    break
                old = ll
            best = max(best, ll)
        bic[k] = -2 * best + (k * m + k - 1) * np.log(n)
    return min(bic, key=bic.get), bic


print("Section 8.3 (4): number of heuristics selected, plain latent-class model against mixture Rasch model "
      "(N = 1,000, planted three)")
for name, kw, seed in (("P2 (sharp lines)", P2, 11), ("P3 (fuzzy lines, hysteresis)", P3, 12)):
    pop = sim.population(1000, codes, ids, seed=seed, **kw)
    k_lc, _ = latent_class(pop["a"], kmax=8, restarts=2 if QUICK else 3)
    k_mr, _ = M.mixture_rasch(pop["a"], kmax=5, restarts=2 if QUICK else 3)
    lc = f"{k_lc} or more (the largest K fitted)" if k_lc == 8 else str(k_lc)
    print(f"  {name:<30} latent-class model selects {lc}; mixture Rasch model selects {k_mr}")

print("\nSection 8.3 (2): hysteresis tests on the break-point against the acceptance count "
      "(scenario P3, h = 1.0, retest of 0.2N drawn from F and R)")
reps = 40 if QUICK else 200
print(f"  share of {reps} replications rejecting at alpha = 0.05")
for n in (600, 1000):
    hits = dict(bp_between=0, count_between=0, bp_retest=0, count_retest=0)
    for r in range(reps):
        pop = sim.population(n, codes, ids, seed=5000 + r, **P3, retest_share=0.4)
        a, o = pop["a"], pop["orders"]
        bp, c = M.break_point(a), a.sum(1)
        hits["bp_between"] += mannwhitneyu(bp[o == "F"], bp[o == "R"]).pvalue < 0.05
        hits["count_between"] += mannwhitneyu(c[o == "F"], c[o == "R"]).pvalue < 0.05
        # within person, oriented as (forward) - (reverse); retest_shift = BP(retest) - BP(original)
        sh = pop["retest_shift"]
        fr_bp = np.where(o == "F", -sh, np.where(o == "R", sh, np.nan))
        fr_bp = fr_bp[~np.isnan(fr_bp)]
        fr_c = pop["retest_fr"][~np.isnan(pop["retest_fr"])]
        hits["bp_retest"] += np.any(fr_bp != 0) and wilcoxon(fr_bp).pvalue < 0.05
        hits["count_retest"] += np.any(fr_c != 0) and wilcoxon(fr_c).pvalue < 0.05
    print(f"  N = {n:>4}: between orders  break-point {hits['bp_between'] / reps:.2f}  count {hits['count_between'] / reps:.2f}"
          f"   |   within-person retest  break-point {hits['bp_retest'] / reps:.2f}  count {hits['count_retest'] / reps:.2f}")

print("\nSection 8.4: precision of the H3 power estimate")
k, n = 27, 30
z = norm.ppf(0.975)
ph = k / n
c = (ph + z * z / (2 * n)) / (1 + z * z / n)
hw = z * np.sqrt(ph * (1 - ph) / n + z * z / (4 * n * n)) / (1 + z * z / n)
print(f"  {k} of {n} replications = {ph:.2f}; 95% Wilson interval [{c - hw:.2f}, {c + hw:.2f}]")

print("\nSection 10.2: invitations for N = 1,000 completed traversals")
for rr in (0.10, 0.125, 0.15):
    print(f"  response rate {rr:.3f}: {1000 / rr:,.0f} invitations")

print("\nSection 10.3: power of 65 interviews per arm (placement change 0.40 against 0.65, two-sided alpha = 0.05)")
p1, p2, m = 0.40, 0.65, 65
pbar = (p1 + p2) / 2
se0, se1 = np.sqrt(2 * pbar * (1 - pbar) / m), np.sqrt(p1 * (1 - p1) / m + p2 * (1 - p2) / m)
power = norm.cdf((abs(p2 - p1) - z * se0) / se1)
n80 = ((z * np.sqrt(2 * pbar * (1 - pbar)) + norm.ppf(0.8) * np.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) / (p2 - p1)) ** 2
print(f"  power at 65 per arm {power:.2f}; per-arm size for power 0.80: {int(np.ceil(n80))}")
print(f"\n{time.time() - t0:.0f} s", file=sys.stderr)
