"""Moving block bootstrap for the mean of d. Owner: Deng Shenbojia (A3)."""
from src import config


def mbb_indices(n, L, rng):
    """Draw k = ceil(n / L) block starts uniformly from {0, ..., n - L}, take L consecutive
    days from each, concatenate and cut to n. No wrap-around."""
    raise NotImplementedError


def mbb_means(d, L, B=config.B, rng=None):
    """B bootstrap means, computed in batches of 1,000 to save memory."""
    raise NotImplementedError


def mbb_ci(d, L, B=config.B, level=0.95, rng=None):
    """Percentile CI, bootstrap SE, and mean +/- 1.96 * SE."""
    raise NotImplementedError


def mbb_test(d, L, B=config.B, rng=None):
    """Test H0: mean = 0. p = (1 + #{|mean* - mean| >= |mean|}) / (B + 1)."""
    raise NotImplementedError
