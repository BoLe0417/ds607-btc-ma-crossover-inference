"""Moving block bootstrap for the mean of d. Owner: Deng Shenbojia (A3)."""
import numpy as np  # arrays, random numbers, quantiles
from scipy import stats
from src import config


def mbb_indices(n, L, rng):
    """Draw k = ceil(n / L) block starts uniformly from {0, ..., n - L}, take L consecutive
    days from each, concatenate and cut to n. No wrap-around."""
    k = int(np.ceil(n / L))  # number of blocks needed to cover n days
    starts = rng.integers(0, n - L + 1, size=k)  # block starts, uniform on {0, ..., n - L}
    idx = starts[:, None] + np.arange(L)  # k x L matrix: row j = start_j, start_j + 1, ..., start_j + L - 1
    return idx.ravel()[:n]  # glue the blocks together, keep the first n days


def mbb_means(d, L, B=config.B, rng=None):
    """B bootstrap means, computed in batches of 1,000 to save memory."""
    d = np.asarray(d, dtype=float)  # accept a list, pandas Series or array
    if rng is None:
        rng = np.random.default_rng(config.SEED)  # reproducible default, seed 607
    n = d.size  # number of days
    k = int(np.ceil(n / L))  # blocks per resample
    means = np.empty(B)  # one bootstrap mean per resample
    for first in range(0, B, 1000):  # batches of at most 1,000 resamples
        size = min(1000, B - first)  # last batch is smaller (9,999 = 9 x 1,000 + 999)
        starts = rng.integers(0, n - L + 1, size=(size, k))  # block starts, one row per resample
        idx = starts[:, :, None] + np.arange(L)  # size x k x L array of day indices
        idx = idx.reshape(size, k * L)[:, :n]  # glue the blocks in each row, keep n days
        means[first:first + size] = d[idx].mean(axis=1)  # bootstrap means of this batch
    return means


def mbb_ci(d, L, B=config.B, level=0.95, rng=None):
    """Percentile CI, bootstrap SE, and mean +/- 1.96 * SE."""
    d = np.asarray(d, dtype=float)  # accept a list, pandas Series or array
    means = mbb_means(d, L, B, rng)  # B bootstrap means (step 2)
    alpha = 1 - level  # 0.05 for a 95% interval
    d_bar = d.mean()  # observed mean of d
    se = means.std(ddof=1)  # bootstrap SE = sd of the bootstrap means
    pct_lo, pct_hi = np.quantile(means, [alpha / 2, 1 - alpha / 2])  # percentile CI (2.5% and 97.5%)
    z = stats.norm.ppf(1 - alpha / 2)  # normal critical value, 1.96 at 95%
    return {
        "n": d.size,
        "mean": d_bar,
        "se": se,
        "pct_lo": pct_lo,  # percentile interval: main result
        "pct_hi": pct_hi,
        "norm_lo": d_bar - z * se,  # d_bar +/- 1.96 x SE
        "norm_hi": d_bar + z * se,
        "L": L,
        "B": B,
        "level": level,
    }


def mbb_test(d, L, B=config.B, rng=None):
    """Test H0: mean = 0. p = (1 + #{|mean* - mean| >= |mean|}) / (B + 1)."""
    d = np.asarray(d, dtype=float)  # accept a list, pandas Series or array
    means = mbb_means(d, L, B, rng)  # B bootstrap means (step 2)
    d_bar = d.mean()  # observed mean of d
    centred = means - d_bar  # shift the bootstrap distribution so it is centred at 0 (H0)
    count = np.sum(np.abs(centred) >= abs(d_bar))  # resamples at least as far from 0 as d_bar
    p = (count + 1) / (B + 1)  # add-one p-value, as in Weeks 4-5
    return {
        "n": d.size,
        "mean": d_bar,
        "p": p,
        "count": int(count),  # how many of the B resamples were as extreme
        "L": L,
        "B": B,
    }
