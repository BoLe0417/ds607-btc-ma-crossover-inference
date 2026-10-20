"""Returns, moving averages, lagged signal and excess return. Owner: Deng Shenbojia (A1)."""
from src import config


def build_series(df):
    """Return the N_SAMPLE rows of the analysis window with columns:
    r, sma5, sma20, s (signal from day t-1, i.e. shift(1)), r_rule, d, switch, d_cost.
    Checks: no missing s in the window; d == 0 whenever s == 1."""
    raise NotImplementedError
