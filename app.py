"""Streamlit user interface. Replace this example with your own app.

Run locally or in a Codespace with:  streamlit run app.py
Streamlit reruns this whole script on every click or input change. See docs/streamlit.md.
"""
from math import exp

import streamlit as st

from pricing import bs_call, bs_put

st.set_page_config(page_title="MSF 8615 app", page_icon="📈")
st.title("Black-Scholes calculator (starter example)")
st.caption("Example app from the MSF 8615 template. Replace it with your team's app.")

col1, col2 = st.columns(2)
with col1:
    S = st.number_input("Underlying price S", value=42.0, min_value=0.01)
    K = st.number_input("Strike K", value=40.0, min_value=0.01)
    T = st.number_input("Time to expiry T (years)", value=0.5, min_value=0.001)
with col2:
    r = st.number_input("Risk-free rate r (%)", value=10.0) / 100
    sigma = st.number_input("Volatility sigma (%)", value=20.0, min_value=0.1) / 100

call, put = bs_call(S, K, r, sigma, T), bs_put(S, K, r, sigma, T)
c1, c2 = st.columns(2)
c1.metric("Call price", f"{call:,.2f}")
c2.metric("Put price", f"{put:,.2f}")

st.write(
    f"Put-call parity check: c − p = {call - put:,.4f} and S − K·e^(−rT) = {S - K * exp(-r * T):,.4f}"
)
st.info("Model assumptions: European options, no dividends, constant volatility and rates.")
