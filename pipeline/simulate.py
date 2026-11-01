"""Synthetic respondents with known structure (appendix Section 8). Nothing here describes real researchers.

Each respondent belongs to a heuristic class k, which scores item i as s_k(i) = w_k . c(i), where c(i) is the item's
five codes scaled to [0, 1]. Classes with different weights order the items differently: these are the planted
"incommensurable stopping heuristics". Respondent p has a threshold theta_p and accepts item i with probability
logistic(alpha * (theta_p - s_k(i)) + h * (2 * previous answer - 1)). alpha sets how sharp individual lines are;
h is a carry-over from the previous answer shown, which produces hysteresis in a forced march.
"""
import numpy as np

SCALE = np.array([2, 7, 4, 5, 1])
CLASS_WEIGHTS = {  # T, C, G, S, H
    "generation": np.array([0.05, 0.20, 0.60, 0.10, 0.05]),
    "core": np.array([0.05, 0.70, 0.10, 0.10, 0.05]),
    "tool": np.array([0.55, 0.15, 0.10, 0.10, 0.10]),
}
ENTRIES = ["10", "17", "24"]


def presentation(order, m, ids, rng):
    if order == "F":
        return np.arange(m)
    if order == "R":
        return np.arange(m)[::-1]
    if order == "E":
        e = ids.index(rng.choice(ENTRIES))
        seq, k = [e], 1
        while len(seq) < m:
            for x in (e + k, e - k):
                if 0 <= x < m:
                    seq.append(x)
            k += 1
        return np.array(seq)
    while True:  # S: scrambled, no designed neighbours shown consecutively
        perm = rng.permutation(m)
        if not (np.abs(np.diff(perm)) == 1).any():
            return perm


def opposite(order):
    return {"F": "R", "R": "F"}.get(order, "F")


def traverse(theta, cls, orders, S, alpha, h, ids, rng):
    """Returns responses a (n x m, designed order), latent logits, and presentation sequences."""
    n, m = len(theta), S.shape[1]
    pres = np.stack([presentation(o, m, ids, rng) for o in orders])
    a = np.zeros((n, m), int)
    logit = np.zeros((n, m))
    prev = np.zeros(n)
    rows = np.arange(n)
    for t in range(m):
        i = pres[:, t]
        z = alpha * (theta - S[cls, i]) + (h * (2 * prev - 1) if t > 0 else 0)
        y = (rng.random(n) < 1 / (1 + np.exp(-z))).astype(int)
        a[rows, i], logit[rows, i], prev = y, z, y
    return a, logit, pres


def population(n, codes, ids, classes, class_mix, theta_mu, theta_sd, alpha, h, retest_share=0.2, seed=1):
    rng = np.random.default_rng(seed)
    c = codes / SCALE
    W = np.stack([CLASS_WEIGHTS[k] for k in classes])
    S = W @ c.T  # classes x items
    cls = rng.choice(len(classes), n, p=class_mix)
    theta = rng.normal(np.array(theta_mu)[cls], theta_sd)
    orders = rng.choice(list("FRES"), n)
    a, logit, pres = traverse(theta, cls, orders, S, alpha, h, ids, rng)
    arguable = np.abs(logit) < 1.0
    # retest in the opposite direction
    rt = rng.random(n) < retest_share
    shift = np.full(n, np.nan)
    fr = np.full(n, np.nan)  # within-person (items accepted under F) - (items accepted under R), F/R originals only
    if rt.any():
        a2, _, _ = traverse(theta[rt], cls[rt], [opposite(o) for o in orders[rt]], S, alpha, h, ids, rng)
        from measures import break_point
        shift[rt] = break_point(a2) - break_point(a[rt])
        c1, c2 = a[rt].sum(1), a2.sum(1)
        o = orders[rt]
        fr[rt] = np.where(o == "F", c1 - c2, np.where(o == "R", c2 - c1, np.nan))
    return dict(a=a, arguable=arguable, cls=cls, theta=theta, orders=orders, pres=pres, retest_shift=shift,
                retest_fr=fr, S=S)


def epinet_layers(a_anchor, pi_bias, projection, group_bias, disc_b0, disc_b1_per_bin, rng):
    """Second- and third-order beliefs, binned to midpoints, and disclosure among those who accept.
    pi_bias: planted pluralistic ignorance per anchor; projection: weight of own view in the estimate of others
    (false consensus); disc_b1_per_bin: log-odds of not disclosing per one-bin (0.2) rise in concealment pressure."""
    n, k = a_anchor.shape
    A = a_anchor.mean(0)
    mids = np.array([0.1, 0.3, 0.5, 0.7, 0.9])
    to_bin = lambda x: mids[np.clip((np.clip(x, 0, 0.999) * 5).astype(int), 0, 4)]
    raw2 = A + pi_bias + projection * (a_anchor - A) + rng.normal(0, 0.12, (n, k))
    m2 = to_bin(raw2)
    m3 = to_bin(raw2 + group_bias + rng.normal(0, 0.10, (n, k)))
    g = a_anchor - m3
    p_not = 1 / (1 + np.exp(-(disc_b0 + disc_b1_per_bin / 0.2 * g)))
    would_not = (rng.random((n, k)) < p_not) & (a_anchor == 1)
    disclosure = np.where(a_anchor == 1, np.where(would_not, "would_not_disclose", "would_disclose"), "would_not_do_it")
    return m2, m3, disclosure
