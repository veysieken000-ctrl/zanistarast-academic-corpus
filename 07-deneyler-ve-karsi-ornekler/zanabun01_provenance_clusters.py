#!/usr/bin/env python3
"""ZANABUN-01: synthetic witness-dependence sensitivity analysis.
No human observations. Standard-library-only deterministic simulation.
"""
from __future__ import annotations
import math
import random

SEED = 20261021
REPS = 20000
SIGMA = 1.0
TAU = 2.0
N = 16


def analytical_rmse(groups: int, n: int = N, tau: float = TAU, sigma: float = SIGMA) -> float:
    assert n % groups == 0 and 1 <= groups <= n
    return math.sqrt(tau * tau / groups + sigma * sigma / n)


def simulate(groups: int, reps: int = REPS, seed: int = SEED) -> tuple[float, float]:
    """Each of groups provenance clusters shares its own independent Gaussian B_g.
    Witness-level private errors are independent. n witnesses evenly split.
    """
    assert N % groups == 0
    rng = random.Random(seed + groups)
    squared = 0.0
    for _ in range(reps):
        shared_mean = sum(rng.gauss(0.0, TAU) for _ in range(groups)) / groups
        private_mean = sum(rng.gauss(0.0, SIGMA) for _ in range(N)) / N
        squared += (shared_mean + private_mean) ** 2
    return math.sqrt(squared / reps), analytical_rmse(groups)


def test() -> None:
    reports = [5.0] * 4
    mean = sum(reports) / len(reports)
    spread = sum((x - mean) ** 2 for x in reports) / len(reports)
    assert mean == 5.0 and spread == 0.0 and abs(mean - 0.0) == 5.0
    assert math.isclose(analytical_rmse(1) ** 2, 4.0 + 1 / 16)
    assert math.isclose(analytical_rmse(16) ** 2, 4 / 16 + 1 / 16)
    # Identifiability: theta + B is invariant under opposing shifts.
    theta, bias, shift = 3.0, 2.0, 7.0
    assert theta + bias == (theta + shift) + (bias - shift)


def main() -> None:
    test()
    print('SYNTHETIC ONLY; seed=20261021; reps=20000; n=16; tau=2; sigma=1')
    print('groups,cluster_size,simulated_rmse,analytic_rmse')
    for groups in (1, 2, 4, 8, 16):
        simulated, analytic = simulate(groups)
        assert abs(simulated - analytic) < 0.05, (groups, simulated, analytic)
        print(f'{groups},{N // groups},{simulated:.4f},{analytic:.4f}')
    print('PASS')


if __name__ == '__main__':
    main()
