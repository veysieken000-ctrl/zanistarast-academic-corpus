#!/usr/bin/env python3
"""ZANABUN-01 v1: synthetic clustered-error experiment.

Purpose: test a mathematical implication of an operational witness model.
NOT a study of human testimony; NOT proof of Zanabûn ontology/theology.
Python standard library only; deterministic fixed seeds.
"""
from __future__ import annotations

import math
import random

TOTAL_OBSERVERS = 16
COMMON_SD = 2.0
PRIVATE_SD = 1.0
REPETITIONS = 20_000
CLUSTERS = (1, 2, 4, 8, 16)
SEED_BASE = 20261021


def analytic_rmse(groups: int) -> float:
    """Independent group-specific errors; equal cluster sizes."""
    assert TOTAL_OBSERVERS % groups == 0
    return math.sqrt(COMMON_SD**2 / groups
                     + PRIVATE_SD**2 / TOTAL_OBSERVERS)


def simulate(groups: int) -> float:
    assert TOTAL_OBSERVERS % groups == 0
    rng = random.Random(SEED_BASE + groups)
    cluster_size = TOTAL_OBSERVERS // groups
    squared_error = 0.0
    for _ in range(REPETITIONS):
        group_errors = [rng.gauss(0.0, COMMON_SD)
                        for _ in range(groups)]
        mean_error = sum(
            group_errors[i // cluster_size] + rng.gauss(0.0, PRIVATE_SD)
            for i in range(TOTAL_OBSERVERS)
        ) / TOTAL_OBSERVERS
        squared_error += mean_error**2
    return math.sqrt(squared_error / REPETITIONS)


def test_exact_counterexample() -> None:
    theta = 0.0
    reports = [5.0] * 4
    consensus = sum(reports) / len(reports)
    spread = sum((x - consensus)**2 for x in reports) / len(reports)
    assert spread == 0.0
    assert abs(consensus - theta) == 5.0


def test_formula() -> None:
    assert math.isclose(analytic_rmse(1), math.sqrt(4.0625))
    assert math.isclose(analytic_rmse(16), math.sqrt(0.3125))
    assert analytic_rmse(16) < analytic_rmse(8) < analytic_rmse(4)
    assert analytic_rmse(4) < analytic_rmse(2) < analytic_rmse(1)


def main() -> None:
    test_exact_counterexample()
    test_formula()
    print("SYNTHETIC ONLY; N=16, tau=2, sigma=1, trials=20000")
    print("groups,observed_rmse,analytic_rmse,abs_difference")
    for groups in CLUSTERS:
        observed = simulate(groups)
        predicted = analytic_rmse(groups)
        difference = abs(observed - predicted)
        assert difference < 0.06, (groups, observed, predicted)
        print(f"{groups},{observed:.4f},{predicted:.4f},{difference:.4f}")
    print("PASS")


if __name__ == "__main__":
    main()
