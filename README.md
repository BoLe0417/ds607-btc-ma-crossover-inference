# Statistical Inference on a Rule-Based Bitcoin Trading Strategy

DS607 Statistics for Data Science, AY2026/27 August Term (Instructor: Qiu Yue).
This repository is MDSE group work.

**Members:** Zhang Enhao (group leader), Ma Tianjiao, Deng Shenbojia.

## Research question

Does a pre-specified 5-day / 20-day moving-average crossover rule applied to Bitcoin daily
prices produce a mean daily excess return over buy-and-hold that is statistically
distinguishable from zero?

## Motivation and objective

TODO (Zhang Enhao, Z2).

## Pre-registered design

All parameters live in `src/config.py` and were committed before any inference was run.
They are never tuned on the data.

| Parameter | Value |
| --- | --- |
| Instrument / frequency | BTCUSDT spot, daily candles (UTC 00:00 open) |
| Sample | 2019-01-01 to 2025-12-31 (2,557 daily returns); Dec 2018 only warms up the averages |
| Rule | SMA5 vs SMA20 on closes, signal lagged one day; zero return when out of the market |
| Block length | main result l = round(n^(1/3)) = 14; sensitivity l in {1, 5, 10, 20, 40} |
| Bootstrap | B = 9,999 resamples, seed 607 |
| Sub-periods | bull 2020-01-01 to 2021-12-31; bear 2022-01-01 to 2022-12-31 |
| Transaction cost | 0.1% per position switch |
| Test level | 5%, two-sided |

### Deviations from plan

None so far. Any change to `src/config.py` is recorded here with the date and the reason.

## Data

TODO (Deng Shenbojia, A5): source, endpoint, pull date, time zone, cleaning checks.
Raw data: `data/raw/`. Licensing: public Binance market data, no account or API key needed.

## Methods

TODO: classical baseline (Ma Tianjiao), moving block bootstrap (Deng Shenbojia),
Monte Carlo coverage check and robustness (Ma Tianjiao).

## Key results

TODO (links to `outputs/figures/` and `outputs/tables/`).

## Limitations

TODO.

## How to run

1. Python 3.12, then `pip install -r requirements.txt`.
2. Run the notebooks in `notebooks/` in order: `01` to `05`.
3. If `data/raw/` is empty, `01` pulls the data from the Binance public API first.

## Repository map

```
src/
  config.py      pre-registered parameters (do not edit without telling the group)
  data.py        pull and load Binance daily candles
  strategy.py    returns, moving averages, lagged signal, excess return d
  classical.py   t-test and CLT confidence interval for the mean
  bootstrap.py   moving block bootstrap: indices, means, CI, test
notebooks/
  01_data_rule_eda.ipynb          data checks, rule, descriptive statistics
  02_classical_baseline.ipynb     t-test baseline and its assumptions
  03_block_bootstrap.ipynb        block bootstrap, block-length sensitivity, side-by-side CIs
  04_monte_carlo_coverage.ipynb   coverage of both intervals on simulated data
  05_robustness.ipynb             sub-periods and transaction costs
data/raw/, data/processed/
outputs/figures/, outputs/tables/, outputs/presentation/
```

See `CONTRIBUTIONS.md` for who did what and `AI_USAGE.md` for the AI declaration.
