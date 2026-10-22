---
name: check-the-numbers
description: Use when adding or changing a formula, a data transformation, or any number the app displays, or when the user asks whether results are right. Writes a check against an independent reference before a number is trusted.
---

# Check the numbers

Goal: every number the app shows comes from code, and a test confirms it against a reference
that does not reuse that code.

1. Restate the calculation and its conventions:
   - units: percent, decimal or basis points;
   - time: days or years, the day count (ACT/360, ACT/365), annualized or per period;
   - sign: who pays whom, long or short;
   - size: per share, per contract, multiplier, notional;
   - prices: bid, ask, mid, settlement or close, and their timestamp.
2. Choose at least one independent reference, of one of these four kinds:
   - **A worked example:** a number the user gives you from the textbook, a lecture, DerivaGem,
     a hand or spreadsheet calculation, or a published figure (an exchange settlement or tool,
     a fund's reported return, an agency's published series, a company filing). Ask for the
     inputs, the answer and the source.
   - **The data itself:** one row of the raw file checked against the source, and plain facts
     about it: dates in order, no duplicates, values in a plausible range, totals that match.
   - **Another method:** the same number computed a different way: a closed form against a loop
     or a simulation, a library function against your own code, a small case done step by step.
   - **An identity or a limit:** no-arbitrage relations (put-call parity, covered interest
     parity, forward = spot plus carry); accounting (the parts add up to the total; daily
     margin flows add up to the total gain or loss); probabilities between 0 and 1 that add up
     to 1; payoffs at expiry; long plus short = 0; limiting cases (zero volatility, zero rates,
     expiry today, a series hedged against itself); the direction a result must move when an
     input rises.
   You cannot see the textbooks, DerivaGem, lecture slides or paid data, and course materials
   may not be uploaded to AI tools. Never supply a reference value yourself, not even one you
   think you remember: ask. Name the source in a comment above each test.
3. Write a pytest test in `tests/` that compares the code with the reference, with a stated
   tolerance. Use a small fixed input or a dated snapshot from `data/`, never a live download,
   so the test gives the same answer tomorrow.
4. Add edge cases that fit the topic: a missing or stale value, a weekend or holiday, zero or
   negative input, expiry today, deep in or out of the money, an empty file.
5. Run `pytest`. If a test fails, report which number disagrees and by how much. Never change an
   expected value to make a test pass unless the user confirms the reference was wrong.
6. Report what was checked, against which source, and what is still unchecked. Say which
   displayed numbers are observed data, which are model estimates, and which are assumptions or
   scenarios.
