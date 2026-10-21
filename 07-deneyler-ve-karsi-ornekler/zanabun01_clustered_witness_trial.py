#!/usr/bin/env python3
"""ZANABUN-01: reproducible *synthetic* clustered-witness uncertainty study.

This is a mathematical toy model, not a human-participant experiment,
not an empirical test of Zanabun or metaphysical/ontological claims.
Python standard library only. Run: python3 zanabun01_clustered_witness_trial.py
"""
from __future__ import annotations

import math
import random

SEED = 20261021
TRIALS = 30000
N = 8
PRIVATE_SD = 1.0
CLUSTER_SD = 2.0
GLOBAL_SD = 0.5


def groups(n: int, group_count: int) -> list[int]:
    """Allocate n observers as evenly as possible across group_count sources."""
    if not 1 <= group_count <= n:
        raise ValueError("group_count must be between 1 and n")
    q, r = divmod(n, group_count)
    return [q + (i < r) for i in range(group_count)]


def predicted_mse(group_sizes: list[int], bias: float = 0.0,
                  global_sd: float = GLOBAL_SD,
                  cluster_sd: float = CLUSTER_SD,
                  private_sd: float = PRIVATE_SD) -> float:
    """E[(mean report - theta)^2] for the specified random-effects model."""
    n = sum(group_sizes)
    if n < 1:
        raise ValueError("at least one observer required")
    return (bias ** 2 + global_sd ** 2
            + cluster_sd ** 2 * sum((m / n) ** 2 for m in group_sizes)
            + private_sd ** 2 / n)


def simulate(group_sizes: list[int], seed: int, bias: float = 0.0,
             trials: int = TRIALS, global_sd: float = GLOBAL_SD,
             cluster_sd: float = CLUSTER_SD,
             private_sd: float = PRIVATE_SD) -> tuple[float, float]:
    """Return simulated RMSE and analytic RMSE, for theta=0 without loss of generality."""
    rng = random.Random(seed)
    n = sum(group_sizes)
    squared_errors = 0.0
    for _ in range(trials):
        global_effect = rng.gauss(0.0, global_sd)
        reports_total = 0.0
        for m in group_sizes:
            cluster_effect = rng.gauss(0.0, cluster_sd)
            for _ in range(m):
                reports_total += (bias + global_effect + cluster_effect
                                  + rng.gauss(0.0, private_sd))
        squared_errors += (reports_total / n) ** 2
    observed = math.sqrt(squared_errors / trials)
    expected = math.sqrt(predicted_mse(
        group_sizes, bias, global_sd, cluster_sd, private_sd))
    return observed, expected


def test_invariants() -> None:
    """Deterministic counterexamples and algebraic assertions."""
    theta = 0.0
    reports = [5.0] * 8
    mean = sum(reports) / len(reports)
    within_variance = sum((x - mean) ** 2 for x in reports) / len(reports)
    assert within_variance == 0.0 and abs(mean - theta) == 5.0

    # Fixed total observer count: diversifying *independent* calibrations
    # reduces cluster uncertainty, but cannot remove global uncertainty.
    one = predicted_mse(groups(8, 1))
    four = predicted_mse(groups(8, 4))
    eight = predicted_mse(groups(8, 8))
    assert math.isclose(one, 4.375)
    assert math.isclose(four, 1.375)
    assert math.isclose(eight, 0.875)
    assert one > four > eight > GLOBAL_SD ** 2

    # No shared effects: n independent measurements -> sigma^2/n.
    assert math.isclose(predicted_mse(groups(8, 1),
                                     global_sd=0.0, cluster_sd=0.0), 0.125)
    # Fixed systematic bias is squared in MSE, not absorbed in variance.
    assert math.isclose(predicted_mse(groups(8, 4), bias=1.0), 2.375)


def main() -> None:
    test_invariants()
    print("SYNTHETIC ONLY; no human observations; seed=", SEED)
    print("condition,groups,n,bias,simulated_rmse,analytic_rmse")
    scenarios = [
        ("one_calibration", 1, 0.0),
        ("two_calibrations", 2, 0.0),
        ("four_calibrations", 4, 0.0),
        ("eight_calibrations", 8, 0.0),
        ("four_calibrations_fixed_bias", 4, 1.0),
    ]
    for idx, (name, g, bias) in enumerate(scenarios):
        simulated, analytic = simulate(groups(N, g), SEED + idx, bias=bias)
        assert abs(simulated - analytic) < 0.065, (name, simulated, analytic)
        print(f"{name},{g},{N},{bias:g},{simulated:.4f},{analytic:.4f}")
    observed, analytic = simulate(groups(N, 1), SEED + 99,
                                  global_sd=0.0, cluster_sd=0.0)
    assert abs(observed - analytic) < 0.025
    print(f"independent_noise_only,1,{N},0,{observed:.4f},{analytic:.4f}")
    print("PASS: deterministic identities and seeded Monte Carlo tolerances")


if __name__ == "__main__":
    main()
