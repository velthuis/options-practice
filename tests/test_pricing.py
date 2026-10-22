"""Tests check our numbers against values we verified independently.

Replace or extend these with checks for your own formulas: a worked example (textbook,
DerivaGem, a hand calculation, a published figure), the data itself, another method, or an
identity. Name the source in a comment, as below.
"""
from math import exp

import pytest

from pricing import bs_call, bs_put

# Hull, Options, Futures, and Other Derivatives (11th ed.), Ch. 15 worked example:
# S0 = 42, K = 40, r = 10%, sigma = 20%, T = 0.5 years -> c = 4.76, p = 0.81
S, K, R, SIGMA, T = 42.0, 40.0, 0.10, 0.20, 0.5


def test_call_matches_hull_example():
    assert bs_call(S, K, R, SIGMA, T) == pytest.approx(4.76, abs=0.005)


def test_put_matches_hull_example():
    assert bs_put(S, K, R, SIGMA, T) == pytest.approx(0.81, abs=0.005)


def test_put_call_parity():
    # c - p = S - K e^(-rT) must hold for European options on a non-dividend stock
    lhs = bs_call(S, K, R, SIGMA, T) - bs_put(S, K, R, SIGMA, T)
    rhs = S - K * exp(-R * T)
    assert lhs == pytest.approx(rhs, abs=1e-9)


def test_rejects_bad_inputs():
    with pytest.raises(ValueError):
        bs_call(S, K, R, -0.2, T)
