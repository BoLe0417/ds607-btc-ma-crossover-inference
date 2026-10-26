# AI usage

Course rule (DS607 guidelines): GenAI is allowed if we remain able to justify every modelling
choice, and every use is documented here.

Add one row every time you use an AI tool, before your deadline. The last column is required:
say how you checked the output (re-ran it, compared with a hand calculation, read the docs, etc.).

| Date | Member | Tool | File | What it was used for | How the output was checked |
| --- | --- | --- | --- | --- | --- |
| 2026-10-21 | Zhang Enhao | Claude | proposal PDF | Drafting the one-page proposal from the group's design | Read and approved by all members |
| 2026-10-21 | Zhang Enhao | Claude Code | repository skeleton | Folders, module stubs, notebook headers, README and templates | Reviewed every file before pushing |
| 2026-10-22 | Ma Tianjiao | Claude | src/classical.py | Drafting t_test_mean() and the variance-factor helpers | Compared t, p and CI with scipy.stats.ttest_1samp; ar1_t_coverage() reproduces the 97% / 89% values in the task pack |
| 2026-10-23 | Zhang Enhao | Claude Code | review of A1, A2, B1 | Independent re-run of src/data.py, src/strategy.py, src/classical.py and notebook 01; look-ahead test (perturbing a day's close leaves that day's signal unchanged) | Numbers match the 10/21 trial run exactly; notebook 01 runs clean from a fresh kernel |
| 2026-10-23 | Ma Tianjiao | Claude | notebooks/02_classical_baseline.ipynb | Drafting code, figures and first-draft interpretations (marked DRAFT; I am rewriting them in my own words) | Restart & Run All on the team's data.py and strategy.py; n, d_bar, t, p, rho_1 and Ljung-Box match the trial run and notebook 01 |
| 2026-10-24 | Ma Tianjiao | Claude | notebooks/04_monte_carlo_coverage.ipynb, notebooks/05_robustness.ipynb | Drafting simulation code, figures and first-draft interpretations (marked DRAFT) | Restart & Run All; t-interval coverage within 3 Monte Carlo SEs of theory (97% / 89% for AR(1)); bootstrap parts use a temporary local mbb_ci until A3 lands |
| 2026-10-22 | Deng Shenbojia | Claude | src/data.py, src/strategy.py (A1) | Drafting fetch_klines(), load_daily() and build_series() | Offline test with a mocked Binance API (paging, fallback URL, missing-day assert); SMA lag recomputed by hand for one day; checked d = -(1 - s) r and the cost total; I pulled the real data in Codespaces and the numbers match the trial run (55.4% in BTC, 143 switches, mean d -0.000208) |
| 2026-10-22 | Deng Shenbojia | Claude | notebooks/01_data_rule_eda.ipynb (A2) | Drafting code, figures and first-draft interpretations; Chinese translation and line-by-line explanation of each interpretation (I am rewriting them in my own words for A5) | Restart & Run All in Codespaces; skewness, kurtosis, ACF(1) and Ljung-Box match the trial run; leader's independent re-run on 10/23 matches |
| 2026-10-23 | Deng Shenbojia | Claude | src/bootstrap.py (A3) | Step-by-step explanation of the moving block bootstrap; I typed the four functions myself following it | Toy case (n = 10, L = 3) checked by hand; L = 1 self-check: SE 0.000476 vs t-test 0.000475, p 0.661 vs 0.662; full block-length table (L = 1 to 40) identical to Claude's reference run |
