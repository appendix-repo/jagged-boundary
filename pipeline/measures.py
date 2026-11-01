"""Measures of appendix Section 5.2, computed from traversal arrays.

Arrays are indexed by participant (rows) and designed position (columns, 0-based), so position order is the order
of instrument/items.json whatever order the items were shown in.
"""
import numpy as np

DIMS = ["T", "C", "G", "S", "H"]


def code_matrix(items):
    return np.array([[it["codes"][d] for d in DIMS] for it in items])


def dominance(codes):
    """dom[j, i] is True if item j dominates item i (>= on every dimension, > on at least one)."""
    ge = (codes[:, None, :] >= codes[None, :, :]).all(-1)
    gt = (codes[:, None, :] > codes[None, :, :]).any(-1)
    return ge & gt


def break_point(a):
    """First rejected position (1-based); n + 1 if the participant accepts everything."""
    rej = a == 0
    return np.where(rej.any(1), rej.argmax(1) + 1, a.shape[1] + 1)


def dominance_violations(a, dom):
    """Share of the participant's opportunities for a violation that are violations (Section 5.2)."""
    acc = a.astype(bool)
    # pairs (j, i), j dominates i, j accepted
    opp = np.einsum("pj,ji->p", acc, dom.astype(int))
    viol = np.einsum("pj,ji,pi->p", acc, dom.astype(int), ~acc)
    return np.divide(viol, opp, out=np.zeros(len(a)), where=opp > 0)


def parallel_inconsistency(a, codes):
    same = [(i, j) for i in range(len(codes)) for j in range(i + 1, len(codes)) if (codes[i] == codes[j]).all()]
    return np.mean([a[:, i] != a[:, j] for i, j in same], axis=0), same


def dominance_steps(codes):
    """Adjacent steps on which something increases and nothing decreases."""
    d = codes[1:] - codes[:-1]
    return np.where((d >= 0).all(1) & (d > 0).any(1))[0]


def jaggedness(A, codes):
    """J: total rise of field acceptance across steps that, by design, should not raise it."""
    s = dominance_steps(codes)
    return float(np.clip(A[s + 1] - A[s], 0, None).sum())


def field_band(A, w=3):
    """Distance in positions from where the smoothed acceptance curve first falls below 0.8 to where it first falls
    below 0.2 (Section 5.2). A sharp shared line gives a small band."""
    sm = np.convolve(np.pad(A, (w // 2, w // 2), mode="edge"), np.ones(w) / w, mode="valid")
    hi = np.where(sm < 0.8)[0]
    lo = np.where(sm < 0.2)[0]
    if len(hi) == 0 or len(lo) == 0:
        return np.nan
    return float(lo[0] - hi[0])


def iqr(x):
    q75, q25 = np.percentile(x, [75, 25])
    return float(q75 - q25)


def loevinger_H(a):
    """Loevinger's H for the whole set of binary items (Mokken scale analysis, Sijtsma & Molenaar 2002)."""
    p = a.mean(0)
    keep = (p > 0) & (p < 1)
    a, p = a[:, keep], p[keep]
    order = np.argsort(-p)  # easiest (most accepted) first
    a, p = a[:, order], p[order]
    n = len(a)
    obs = exp = 0.0
    for i in range(a.shape[1]):
        for j in range(i + 1, a.shape[1]):
            # Guttman error: the harder item j accepted while the easier item i rejected
            obs += np.sum((a[:, j] == 1) & (a[:, i] == 0))
            exp += n * p[j] * (1 - p[i])
    return float(1 - obs / exp)


def mixture_rasch(a, kmax=5, restarts=3, iters=400, nodes=61, span=30, seed=0):
    """Mixture Rasch model (Rost 1990) fit by EM with each class's person distribution N(0, sigma_k) on a fixed grid of
    nodes; class-specific item difficulties b_k (centred), mixing weights pi_k. K = 1..kmax, selected by BIC.
    Items that everyone accepts or everyone rejects carry no information and are dropped before fitting."""
    rng = np.random.default_rng(seed)
    keep = (a.mean(0) > 0) & (a.mean(0) < 1)
    a = a[:, keep].astype(float)
    n, m = a.shape
    grid = np.linspace(-span, span, nodes)
    p0 = np.clip(a.mean(0), 0.01, 0.99)
    out = {}
    for k in range(1, kmax + 1):
        best = None
        for _ in range(restarts):
            b = np.log((1 - p0) / p0)[None] + rng.normal(0, 1.0, (k, m))
            b -= b.mean(1, keepdims=True)
            sig = np.full(k, 2.0)
            pi = np.full(k, 1 / k)
            ll_old = -np.inf
            for _ in range(iters):
                L = grid[None, :, None] - b[:, None, :]                       # k x Q x m
                lp1, lp0 = -np.logaddexp(0, -L), -np.logaddexp(0, L)
                w = np.exp(-0.5 * (grid[None] / sig[:, None]) ** 2)
                w /= w.sum(1, keepdims=True)                                   # k x Q
                lj = (np.einsum("pi,kqi->pkq", a, lp1) + np.einsum("pi,kqi->pkq", 1 - a, lp0)
                      + np.log(w + 1e-300)[None] + np.log(pi + 1e-300)[:, None][None])
                mx = lj.max((1, 2), keepdims=True)
                tot = np.exp(lj - mx).sum((1, 2), keepdims=True)
                ll = float((mx + np.log(tot)).sum())
                r = np.exp(lj - mx) / tot                                      # p x k x Q
                Nkq = r.sum(0)                                                 # k x Q
                Skqi = np.einsum("pkq,pi->kqi", r, a)                          # expected acceptances
                P = 1 / (1 + np.exp(-L))
                grad = (Skqi - Nkq[:, :, None] * P).sum(1)                     # d ll / d(-b)
                hess = (Nkq[:, :, None] * P * (1 - P)).sum(1) + 1e-6
                b = b - grad / hess
                b -= b.mean(1, keepdims=True)
                pi = np.clip(Nkq.sum(1) / n, 1e-6, None)
                sig = np.sqrt(np.clip((Nkq * grid[None] ** 2).sum(1) / Nkq.sum(1), 0.05, (span / 2.5) ** 2))
                if ll - ll_old < 1e-5:
                    break
                ll_old = ll
            if best is None or ll > best[0]:
                best = (ll, pi, b, sig)
        ll, pi, b, sig = best
        npar = k * (m - 1) + k + (k - 1)
        out[k] = dict(ll=ll, bic=-2 * ll + npar * np.log(n), pi=pi, theta=-b, sigma=sig)
    kbest = min(out, key=lambda k: out[k]["bic"])
    return kbest, out


latent_classes = mixture_rasch


def orderings_cross(theta, min_share=0.05, pi=None, tau_cut=0.8):
    """True if at least two classes order the items differently (Kendall's tau between the classes' item easiness
    below tau_cut), counting only classes with at least min_share of respondents."""
    from scipy.stats import kendalltau
    idx = [k for k in range(len(theta)) if pi is None or pi[k] >= min_share]
    taus = [kendalltau(theta[i], theta[j])[0] for x, i in enumerate(idx) for j in idx[x + 1:]]
    return (len(taus) > 0 and min(taus) < tau_cut), taus


def sharp_individuals(a, conf_arguable, dom, bp_retest_shift=None):
    """Section 6.1: no dominance violations, firm on both items flanking the break, and (if retested) a break that
    moves by at most one position."""
    n, m = a.shape
    dv = dominance_violations(a, dom)
    bp = break_point(a)
    firm = np.ones(n, bool)
    for p in range(n):
        b = bp[p] - 1
        flank = [x for x in (b - 1, b) if 0 <= x < m]
        firm[p] = not conf_arguable[p, flank].any()
    ok = (dv == 0) & firm
    if bp_retest_shift is not None:
        tested = ~np.isnan(bp_retest_shift)
        ok = ok & (~tested | (np.abs(np.nan_to_num(bp_retest_shift)) <= 1))
    return ok


def picture(a, conf_arguable, dom, kbest, crossing, H, A, bp_retest_shift=None):
    """Decision rules of Section 6.1."""
    bp = break_point(a)
    # H is not part of the P1 rule: when everyone's line is in the same place respondents barely differ, and H,
    # which measures how well one ordering explains differences between respondents, is low or undefined (Section 8.3)
    p1 = iqr(bp) <= 2 and (field_band(A) <= 3) and kbest == 1
    if p1:
        return "P1"
    share_sharp = sharp_individuals(a, conf_arguable, dom, bp_retest_shift).mean()
    return "P2" if share_sharp > 0.5 else "P3"


def epinet(a_anchor, m2, m3, w=None):
    """Pluralistic ignorance, false consensus, truly false consensus, concealment pressure (Section 5.2)."""
    w = np.ones(len(a_anchor)) if w is None else w
    A = (w[:, None] * a_anchor).sum(0) / w.sum()
    PI = (w[:, None] * m2).sum(0) / w.sum() - A
    FC = np.array([m2[a_anchor[:, i] == 1, i].mean() - m2[a_anchor[:, i] == 0, i].mean() for i in range(a_anchor.shape[1])])
    e2 = m2 - A
    TFC = np.array([np.corrcoef(a_anchor[:, i], e2[:, i])[0, 1] for i in range(a_anchor.shape[1])])
    g = a_anchor - m3
    return dict(A=A, PI=PI, FC=FC, TFC=TFC, g=g)


def logit_fit(X, y, iters=50, cluster=None):
    """Logistic regression by Newton-Raphson; returns coefficients and standard errors (cluster-robust if cluster ids
    are given, so that several answers from one participant are not treated as independent)."""
    X = np.column_stack([np.ones(len(X)), X])
    b = np.zeros(X.shape[1])
    for _ in range(iters):
        p = 1 / (1 + np.exp(-X @ b))
        W = p * (1 - p)
        Hm = X.T @ (X * W[:, None])
        step = np.linalg.solve(Hm, X.T @ (y - p))
        b += step
        if np.abs(step).max() < 1e-8:
            break
    Hi = np.linalg.inv(Hm)
    if cluster is None:
        return b, np.sqrt(np.diag(Hi))
    p = 1 / (1 + np.exp(-X @ b))
    sc = X * (y - p)[:, None]
    G = np.zeros((len(np.unique(cluster)), X.shape[1]))
    np.add.at(G, np.unique(cluster, return_inverse=True)[1], sc)
    return b, np.sqrt(np.diag(Hi @ (G.T @ G) @ Hi))
