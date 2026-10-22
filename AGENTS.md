# AGENTS.md

Instructions for AI coding agents (GitHub Copilot, Antigravity, Codex, Claude Code, and others)
working in this repository. All of them read this file at the start of a session. Keep it short
and current. When an agent makes the same mistake twice, add a rule here.

## Project
- Teams have 3-5 students. Each member needs at least one own-account commit visible on GitHub.
- Read RUBRIC.md for assessment criteria. Do not alter it to improve a score.
- MSF 8615 Derivatives (Villanova) student team project, built with Streamlit.
- App: <one sentence: what question does the app help a user answer?>
- Users: classmates and recruiters. Explain every result in plain English on screen.

## Structure
- `pricing.py` and any other modules: formulas only, no Streamlit code.
- `app.py`: Streamlit user interface only. It calls functions from the modules.
- Dollar amounts in `st.markdown`, `st.write`, `st.caption` or a widget label: write `\$`. Streamlit
  shows text between two `$` signs as LaTeX math.
- `tests/`: pytest. Every formula gets at least one test against an independent reference: a
  worked example we give you, the data itself, another method, or an identity (see the
  check-the-numbers skill). You can't see our textbooks, DerivaGem or paid data, so we give you
  those numbers. If we haven't, ask; never use one from memory.
- `data/`: dated snapshots named `<source>_<YYYY-MM-DD>.csv`. Record each one in the README's Data section.

## When you plan (plan mode, or when we say "plan first")
Do not edit files. A plan lists:
1. The files you will change, and why.
2. Each test you will add and the independent reference it compares with: a number we give you
   (textbook example, DerivaGem, a hand calculation, a published figure), the data itself,
   another method, or an identity such as put-call parity. List the numbers you still need from us.
3. What the app will show, with units and labels for assumptions and scenarios.
4. What could make the numbers wrong (units, sign conventions, bid vs. ask, stale data).
Keep each step small enough for us to review in one sitting.

## Sessions and context
- One task per session. When we switch to an unrelated task, we start a new session (`/clear`).
- Keep the current goal, decisions and next steps in `PLAN.md`. Update it before a session ends
  or is compacted, so a fresh session can pick up from the file instead of the chat.
- Read files when you need them; do not paste whole data files or long logs into the chat.
  Summarize test output to the failures that matter.
- If we have corrected you twice on the same point, say so and suggest a fresh session with a
  better prompt.

## Team agents, skills and logs
- `.github/agents/` holds two team agents: `critic` and `examiner`. In Copilot
  chat, pick them from the agent menu; in Copilot CLI, run `copilot --agent critic`. In other
  tools, we start a new session and ask you to read the agent's file and follow it. The critic
  always runs in a fresh session.
- `.agents/skills/check-the-numbers/SKILL.md`: follow it whenever you add or change a calculation.

## The .md files and what to do with them
- `README.md`: the team's description of the app. When you add a data file, change a formula or
  add a test, update its Data, Method or Tests section in the same step and point out the edit.
  Do not rewrite the team's wording elsewhere.
- `PLAN.md`: yours to keep current (see Sessions and context).
- `AI_LOG.md`: the team's record of AI use, graded under rubric criterion 5. At the end of each
  task, draft a row for section 1 in the chat (date, tool and model, what we asked, what we kept
  or changed, how it was checked). We check it and add it, or ask you to; leave "Who" for us.
  Never edit or delete existing rows. Sections 2 and 3 hold the critic's findings and the
  examiner's report, which the team pastes in.
- `RUBRIC.md`: read it; never change it.
- `docs/`: guides for the team. Read `docs/streamlit.md` before changing `app.py` and follow
  `docs/git-and-teamwork.md` for git.
- `AGENTS.md` (this file): the team adds rules here. When you repeat a mistake, suggest a rule.

## Working with teammates (we all push to `main`)
- Run `git pull` before you start a task.
- Change only the files the task needs. Do not reformat, rename or reorder code you were not
  asked to change; that causes merge conflicts for teammates.
- Ask before editing `requirements.txt`, and say so when you do.
- Commit only when asked, with a one-line message. Never run `git push --force`,
  `git reset --hard`, or anything that rewrites history.
- If git reports a merge conflict, stop. Show us both versions and explain each before you
  resolve it, then run `pytest`.

## Rules
- Do not invent market data. Load it from `data/` or ask us for it.
- Label every hypothetical scenario and model assumption on screen.
- Units: time in years, rates and volatility as annual decimals (0.05, not 5).
  State units in every docstring.
- Never put API keys or passwords in code. Use Streamlit secrets or Codespaces secrets.
- One feature or fix per step. Keep changes small enough for us to review.

## Before you say a task is done
1. Run `pytest` and report the result.
2. Summarize what you changed and why, in plain English.
3. List any assumption you made and anything we should check by hand.
4. Draft the `AI_LOG.md` row for this task.

## Helping beginners
Explain unfamiliar GitHub and pytest steps in plain language. Identify what a command changes before running it. Do not fabricate test results, commit attribution, or individual understanding. The critic and examiner are review helpers; their feedback is not an official grade.
