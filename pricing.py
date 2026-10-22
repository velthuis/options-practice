"""Pricing formulas for the app.

Keep this file free of Streamlit code so every function can be tested with pytest.
Units: S and K in index points or dollars, r and sigma as decimals per year
(0.05, not 5), T in years.
"""
from math import erf, exp, log, sqrt


def norm_cdf(x: float) -> float:
    """Standard normal cumulative distribution function N(x)."""
    return 0.5 * (1.0 + erf(x / sqrt(2.0)))


def bs_d1_d2(S: float, K: float, r: float, sigma: float, T: float) -> tuple[float, float]:
    """Black-Scholes-Merton d1 and d2 (no dividends)."""
    if S <= 0 or K <= 0 or sigma <= 0 or T <= 0:
        raise ValueError("S, K, sigma and T must be positive")
    d1 = (log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * sqrt(T))
    return d1, d1 - sigma * sqrt(T)


def bs_call(S: float, K: float, r: float, sigma: float, T: float) -> float:
    """European call price under Black-Scholes-Merton (no dividends)."""
    d1, d2 = bs_d1_d2(S, K, r, sigma, T)
    return S * norm_cdf(d1) - K * exp(-r * T) * norm_cdf(d2)


def bs_put(S: float, K: float, r: float, sigma: float, T: float) -> float:
    """European put price under Black-Scholes-Merton (no dividends)."""
    d1, d2 = bs_d1_d2(S, K, r, sigma, T)
    return K * exp(-r * T) * norm_cdf(-d2) - S * norm_cdf(-d1)
