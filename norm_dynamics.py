"""Threshold model of the disclosure norm (appendix Section 7).

At an anchor item, researcher p privately accepts the practice (a_p = 1) or not, believes a fraction x_p of the field
would judge it acceptable for researchers like them (the third-order answer m3, the belief that gates disclosure), and
openly does and discloses it if a_p = 1 and x_p >= tau_p, a personal threshold. Researchers
infer acceptance from what is visible: the mean belief moves toward the visible share V by
    xbar(t+1) = xbar(t) + lam * (V(t) - xbar(t)),   x_p = xbar + e_p (individual offsets kept).
V(xbar) = mean_p a_p * F((xbar + e_p - mu) / s), with F logistic and (mu, s) estimated from the disclosure question
(Section 5.2, H5). A stable fixed point V* is the item's equilibrium visible share. The tipping quantity Delta is the
smallest common shift of these third-order beliefs that carries V* across one half: the size of the change in what
researchers believe about each other that would move the collective line at that item (Granovetter 1978; Centola,
Willer & Macy 2005).
"""
import numpy as np


def visible(xbar, a, e, mu, s):
    return float(np.mean(a / (1 + np.exp(-(xbar + e - mu) / s))))


def equilibrium(x0, a, e, mu, s, lam=0.5, iters=2000):
    x = x0
    for _ in range(iters):
        v = visible(x, a, e, mu, s)
        nx = x + lam * (v - x)
        if abs(nx - x) < 1e-9:
            break
        x = nx
    return visible(x, a, e, mu, s)


def tipping(x0, a, e, mu, s, grid=np.linspace(0, 1, 201)):
    """Smallest |delta| that moves the equilibrium visible share across 0.5 (np.inf if none in [-1, 1])."""
    v0 = equilibrium(x0, a, e, mu, s)
    sign = 1 if v0 < 0.5 else -1
    for d in grid:
        if (equilibrium(x0 + sign * d, a, e, mu, s) >= 0.5) != (v0 >= 0.5):
            return v0, sign * d
    return v0, np.inf


def fixed_points(a, e, mu, s, grid=np.linspace(0, 1, 401)):
    f = np.array([visible(x, a, e, mu, s) - x for x in grid])
    return grid[np.where(np.diff(np.sign(f)) != 0)[0]]
