# ZANABUN-01 — Synthetic experiment and analytic checks

The linked Python experiment fixes total observer count N=16, shared-error standard deviation tau=2, private-error standard deviation sigma=1, and 20,000 synthetic tasks per condition. The number of independent calibration groups G is 1, 2, 4, 8, or 16. Each group receives an independent normal shared error; each observer receives independent normal private noise. Seeds are 20261021+G. The outcome is the root mean squared error of the grand mean relative to a stipulated zero target.

| G | Synthetic RMSE | Analytic sqrt(4/G + 1/16) |
|---:|---:|---:|
| 1 | 2.0052 | 2.0156 |
| 2 | 1.4373 | 1.4361 |
| 4 | 1.0158 | 1.0308 |
| 8 | 0.7516 | 0.7500 |
| 16 | 0.5552 | 0.5590 |

The numbers were independently calculated locally on 21 October 2026 using the documented algorithm. The program checks its exact counterexample and analytical monotonicity and requires each simulated RMSE to differ from the analytic benchmark by less than 0.06. This tolerance is a numerical sanity check, not a statistical test of real-world witness behavior.

Run: python3 07-deneyler-ve-karsi-ornekler/zanabun01_cluster_independence.py. Only synthetic values are used; there are no human subjects, real measurements, field findings, or evidence of ontological claims. This is a methodological extension within the same ZANABUN-01 article family, not a new unique paper.
