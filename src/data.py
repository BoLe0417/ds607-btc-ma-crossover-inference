"""Pull and load Binance daily candles. Owner: Deng Shenbojia (A1)."""
from src import config

KLINES_URL = "https://api.binance.com/api/v3/klines"
KLINES_URL_FALLBACK = "https://data-api.binance.vision/api/v3/klines"


def fetch_klines(start=config.PULL_START, end=config.SAMPLE_END):
    """Page through the klines endpoint (limit=1000), save all 12 columns to data/raw/ and
    write data/raw/PULL_LOG.md (pull time UTC, URL, parameters, row count)."""
    raise NotImplementedError


def load_daily():
    """Read the raw CSV (pull it first if missing). Asserts: N_PULL rows, no duplicate or
    missing days, close > 0. Column `date` is the UTC date of the candle open."""
    raise NotImplementedError
