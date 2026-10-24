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
