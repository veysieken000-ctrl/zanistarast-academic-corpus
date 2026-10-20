#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ZANABUN-01 / supplementary experiment, 2026-10-20.

Synthetic Gaussian common-error model, independent versus shared calibration.
No human observations, no metaphysical validation, no external data.
Python >= 3.9; standard library only. Run: python3 zanabun01_independent_calibration.py
"""
import math
import random

SEED = 20261020
TRIALS = 10000
SIGMA = 1.0
TAU = 2.0
SIZES = (4, 16, 64)


def rmse(values):
    return math.sqrt(sum(x * x for x in values) / len(values))


def analytic(n):
    """One group; two independent calibration groups; two groups with same bias."""
    return (
        math.sqrt(TAU ** 2 + SIGMA ** 2 / n),
        math.sqrt(TAU ** 2 / 2 + SIGMA ** 2 / (2 * n)),
        math.sqrt(TAU ** 2 + SIGMA ** 2 / (2 * n)),
    )


def simulation():
    rng = random.Random(SEED)
    for n in SIZES:
        one, independent, shared = [], [], []
        for _ in range(TRIALS):
            b1 = rng.gauss(0, TAU)
            b2 = rng.gauss(0, TAU)
            e1 = sum(rng.gauss(0, SIGMA) for _ in range(n)) / n
            e2 = sum(rng.gauss(0, SIGMA) for _ in range(n)) / n
            one.append(b1 + e1)
            independent.append((b1 + e1 + b2 + e2) / 2)
            shared.append(b1 + (e1 + e2) / 2)
        yield n, (rmse(one), rmse(independent), rmse(shared)), analytic(n)


def tests():
    # Perfect internal agreement does not imply external correctness.
    theta = 0.0
    witnesses = [5.0] * 4
    avg = sum(witnesses) / len(witnesses)
    assert sum((w - avg) ** 2 for w in witnesses) == 0
    assert abs(avg - theta) == 5.0

    # Observational non-identifiability: theta + B stays fixed.
    for shift in (-10.0, 0.0, 3.5):
        theta0, bias0 = 1.0, 4.0
        assert theta0 + bias0 == (theta0 + shift) + (bias0 - shift)

    # Exchangeable correlation and effective sample size.
    rho = TAU ** 2 / (TAU ** 2 + SIGMA ** 2)
    n_eff = 16 / (1 + 15 * rho)
    assert math.isclose(rho, 0.8)
    assert math.isclose(n_eff, 16 / 13)
    assert all(a > b and c > b for n in SIZES for a, b, c in [analytic(n)])

    # Independent calibration improves the common-error floor,
    # whereas adding witnesses under one global bias does not.
    assert math.isclose(analytic(16)[1], math.sqrt(2 + 1 / 32))
    assert math.isclose(analytic(16)[2], math.sqrt(4 + 1 / 32))


def main():
    tests()
    print("SYNTHETIC ONLY; seed=20261020; trials=10000; tau=2; sigma=1")
    print("n,one_sim,one_theory,independent_sim,independent_theory,shared_sim,shared_theory")
    for n, observed, predicted in simulation():
        for actual, expected in zip(observed, predicted):
            assert abs(actual - expected) < 0.09, (n, actual, expected)
        print(f"{n},{observed[0]:.4f},{predicted[0]:.4f},"
              f"{observed[1]:.4f},{predicted[1]:.4f},"
              f"{observed[2]:.4f},{predicted[2]:.4f}")
    print("PASS: invariants and simulation tolerances")


if __name__ == "__main__":
    main()
