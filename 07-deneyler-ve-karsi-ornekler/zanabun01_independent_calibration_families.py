#!/usr/bin/env python3
"""Synthetic nested-error demonstration for ZANABUN-01 v0.2.

No human participants; no empirical claim about Zanabun or theology.
Run with Python 3: python3 zanabun01_independent_calibration_families.py
"""
import math
import random

SEED = 20261021
REPETITIONS = 12000
N = 16
LOCAL_SD = 2.0
PRIVATE_SD = 1.0
CASES = [
    (1, 0.0, 0.0),
    (4, 0.0, 0.0),
    (16, 0.0, 0.0),
    (1, 1.0, 0.0),
    (4, 1.0, 0.0),
    (16, 1.0, 0.0),
    (4, 1.0, 1.0),
]


def theoretical_rmse(groups, global_sd, fixed_bias):
    return math.sqrt(
        fixed_bias ** 2
        + global_sd ** 2
        + LOCAL_SD ** 2 / groups
        + PRIVATE_SD ** 2 / N
    )


def simulate(groups, global_sd, fixed_bias, rng):
    assert N % groups == 0
    size = N // groups
    squared_error = 0.0
    for _ in range(REPETITIONS):
        global_error = rng.gauss(0.0, global_sd)
        total = 0.0
        for _ in range(groups):
            family_error = rng.gauss(0.0, LOCAL_SD)
            for _ in range(size):
                total += (
                    fixed_bias + global_error + family_error
                    + rng.gauss(0.0, PRIVATE_SD)
                )
        squared_error += (total / N) ** 2
    return math.sqrt(squared_error / REPETITIONS)


def main():
    assert sum((x - 5.0) ** 2 for x in [5.0] * 4) == 0.0
    assert abs(5.0 - 0.0) == 5.0
    assert math.isclose(theoretical_rmse(4, 1.0, 1.0), 1.75)
    rng = random.Random(SEED)
    print("SYNTHETIC ONLY seed=%d repetitions=%d N=%d" % (SEED, REPETITIONS, N))
    print("G,tau0,fixed_bias,simulated_RMSE,analytic_RMSE")
    for groups, global_sd, fixed_bias in CASES:
        empirical = simulate(groups, global_sd, fixed_bias, rng)
        expected = theoretical_rmse(groups, global_sd, fixed_bias)
        assert abs(empirical - expected) < 0.08
        print(f"{groups},{global_sd:g},{fixed_bias:g},{empirical:.4f},{expected:.4f}")
    print("PASS: deterministic counterexample and analytic Monte Carlo checks")


if __name__ == "__main__":
    main()
