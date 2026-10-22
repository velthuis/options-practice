# <App name>

MSF 8615 Derivatives, Fall 2026 · Team: <names>

**Live app:** <Streamlit link, once deployed>

## Project objective: explain and verify
The team can explain what the app computes, why the method fits the question, and how each
displayed number was verified, and every member presents part of the group demo. You are responsible for the output, whoever or whatever wrote the code.

Deliverables that show it: tests against independent numbers (`tests/`) and `AI_LOG.md` (AI use,
the critic's review, examiner practice), scored against `RUBRIC.md`.

## Files in this repo
| File | Who uses it | What it is for |
|---|---|---|
| `README.md` | You | This page: the question, data, method, checks, limitations and team |
| `AI_LOG.md` | You | How you used AI, the critic's findings and your fixes, and examiner practice |
| `RUBRIC.md` | You read it | How the app is graded |
| `AGENTS.md` | The agent | Standing rules it reads every session. Add a rule when it repeats a mistake |
| `PLAN.md` | The agent | Notes on the current task, so a new session can pick up where the last one stopped |
| `app.py`, `pricing.py`, `tests/`, `data/` | Code | The page, the formulas, the checks, the dated data files |
| `docs/` | You, when needed | Guides: your laptop setup, setting up your agent, how Streamlit works, git as a team |

To read a `.md` file with its formatting: on github.com, click it. In a Codespace, right-click it
and choose **Open Preview** (Ctrl+Shift+V).

## The question
<One or two sentences: what decision, calculation, or risk does the app help a user understand?>

## Inputs and outputs
- Inputs: <what the user enters or uploads>
- Outputs: <numbers, charts, and what they mean>

## Data
<Where each file in `data/` comes from, when it was saved, and what is observed versus assumed.>

| File in `data/` | Source | Date and time saved | Terms of use: can it be public? |
|---|---|---|---|
| | | | |

- Save market data as dated files, for example `cboe_spx-options_2026-10-20.csv`, and show the date
  on screen.
- Licensed data (Bloomberg, FactSet, Risk.net, WRDS, ...) does not go into a public repo or into AI
  tools. Keep it in `data/licensed/` (ignored by git) and run your code on it yourself.
- Hypothetical inputs and stress scenarios are fine. Label them as such.

## Method
<Formulas and model assumptions, in plain English. Cite the textbook section.>

## Tests
Run `pytest`. Each test compares our code with a number we checked independently:
- `tests/test_pricing.py`: Black-Scholes prices match Hull's Chapter 15 example; put-call parity holds.

The agent skill in `.agents/skills/check-the-numbers/` tells coding agents how to add checks like these.

## How to run
First make your own repository: on the template's page, **Use this template → Create a new
repository** (one per team). Don't open a Codespace on the template itself: when you commit there,
GitHub quietly turns your work into a public fork of the template, and "Open in a codespace" from
the template button keeps your work only inside that codespace until you publish it.

In a GitHub Codespace (at home), or in VS Code on your laptop (works on campus too; first follow
`docs/local-setup.md`):
```
pip install -r requirements.txt
pytest
streamlit run app.py
```
New to Streamlit? `docs/streamlit.md` explains how an app works (the script reruns from top to
bottom on every click), with caching, layout and deployment.

## Limitations
<What the app cannot tell you. Which inputs are scenarios rather than observed prices?>

## AI use
<Short summary. Details in `AI_LOG.md`.>

## Working with agents
Set up the agent you want with `docs/agent-setup.md`: GitHub Copilot (free for students), Antigravity
CLI, Codex or Claude Code. All of them read `AGENTS.md`. Use each tool's built-in plan mode to plan
a step. Two review helpers live in `.github/agents/`:
- `critic`: adversarial review in a new session; cannot edit files; findings go in `AI_LOG.md`
- `examiner`: asks practice questions for the group demo and scores them against `RUBRIC.md`

In Copilot, pick them from the agent menu. In other tools, start a new session and ask the agent
to read the file and follow it (`docs/agent-setup.md` has the prompt).

## Working as a team
See `docs/git-and-teamwork.md`: pull before you start, one owner per file, push daily, and what to do when git
reports a merge conflict.

## Team contributions
| Name | Main contributions |
|---|---|
| | |

## Team size and your own commit
Teams have **3-5 students**. One member creates the repository and invites the other **2-4**.
Every member makes **at least one commit under their own GitHub account** that adds something the
project needs: a formula, a test, a data file and its notes, part of the README, or rows in
`AI_LOG.md`. You decide what; an empty or placeholder file does not count. That commit is worth
**5 points per student** (all or nothing). Check the history together, and never share accounts.
The other **95 points are shared** by the team, and every member presents part of the group
presentation and demo.

