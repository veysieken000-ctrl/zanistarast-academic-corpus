#!/usr/bin/env python3
"""Synthetic hierarchical witness-error experiment; Python standard library."""
import math
import random

SEED = 20261020
REPS = 10000

def mse(g, m, tau0=1.0, taug=2.0, sigma=1.0):
    return tau0*tau0 + taug*taug/g + sigma*sigma/(g*m)

def run(g, m, rng):
    total = 0.0
    for _ in range(REPS):
        error = rng.gauss(0.0, 1.0)
        for _ in range(g):
            error += (rng.gauss(0.0, 2.0) +
                      sum(rng.gauss(0.0, 1.0) for j in range(m))/m)/g
        total += error*error
    return math.sqrt(total/REPS)

if __name__ == "__main__":
    rng = random.Random(SEED)
    print("SYNTHETIC ONLY: seed", SEED, "reps", REPS)
    for g in (1, 2, 4, 8, 24):
        m = 24//g
        simulated, analytic = run(g, m, rng), math.sqrt(mse(g, m))
        assert abs(simulated-analytic) < 0.12
        print(g, m, round(simulated, 4), round(analytic, 4))
    assert mse(24, 1) < mse(1, 24)
    assert 3 + (-1) == (3+7) + (-1-7)
    print("PASS")
