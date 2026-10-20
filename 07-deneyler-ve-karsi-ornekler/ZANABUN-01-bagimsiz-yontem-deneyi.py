#!/usr/bin/env python3
"""ZANABUN-01: analytic and synthetic tests of source dependence.
Standard library only; synthetic Gaussian observations, not human-subject data.
"""
from __future__ import annotations
import math
import random

SEED = 20261021
REPS = 20000
TOTAL_OBSERVERS = 16
PRIVATE_SD = 1.0
METHOD_SD = 2.0

# (label, number of independent methods, global shared SD, method shared SD)
DESIGNS = (
    ("single-method", 1, 0.0, METHOD_SD),
    ("four-methods", 4, 0.0, METHOD_SD),
    ("sixteen-methods", 16, 0.0, METHOD_SD),
    ("sixteen-with-global-error", 16, 1.0, METHOD_SD),
    ("no-shared-error", 1, 0.0, 0.0),
)

def theoretical_mse(methods: int, global_sd: float, method_sd: float) -> float:
    """Equal-sized methods, independent centered Gaussian error components."""
    assert TOTAL_OBSERVERS % methods == 0
    return global_sd**2 + method_sd**2 / methods + PRIVATE_SD**2 / TOTAL_OBSERVERS

def run() -> list[tuple[str, int, float, float]]:
    rng = random.Random(SEED)
    rows = []
    for name, methods, global_sd, method_sd in DESIGNS:
        per_method = TOTAL_OBSERVERS // methods
        sum_sq_error = 0.0
        for _ in range(REPS):
            global_error = rng.gauss(0, global_sd)
            reports = []
            for _method in range(methods):
                method_error = rng.gauss(0, method_sd)
                for _observer in range(per_method):
                    reports.append(global_error + method_error + rng.gauss(0, PRIVATE_SD))
            group_mean = sum(reports) / TOTAL_OBSERVERS
            sum_sq_error += group_mean**2  # true theta = 0
        observed = math.sqrt(sum_sq_error / REPS)
        predicted = math.sqrt(theoretical_mse(methods, global_sd, method_sd))
        rows.append((name, methods, observed, predicted))
    return rows

def checks() -> None:
    theta = 0.0
    unanimous = [5.0] * 4
    assert sum((x - 5.0)**2 for x in unanimous) / 4 == 0.0
    assert abs(sum(unanimous) / 4 - theta) == 5.0
    divided = [-10.0, 10.0]
    assert sum(divided) / 2 == theta
    assert sum(x*x for x in divided) / 2 == 100.0
    # Observational nonidentifiability: (theta, B) and (theta+c, B-c).
    for c in (-4.0, 0.0, 3.0):
        theta, common_bias = 7.0, 2.0
        assert theta + common_bias == (theta + c) + (common_bias - c)
    assert theoretical_mse(1, 0, METHOD_SD) > theoretical_mse(4, 0, METHOD_SD)
    assert theoretical_mse(4, 0, METHOD_SD) > theoretical_mse(16, 0, METHOD_SD)

def main() -> None:
    checks()
    print(f"seed={SEED}; repetitions={REPS}; observers={TOTAL_OBSERVERS}; synthetic only")
    print("design,independent_methods,simulated_RMSE,analytic_RMSE")
    for name, methods, observed, predicted in run():
        assert abs(observed - predicted) < 0.06, (name, observed, predicted)
        print(f"{name},{methods},{observed:.4f},{predicted:.4f}")
    print("PASS: invariants, identifiability counterexample, simulation tolerances")

if __name__ == "__main__":
    main()
