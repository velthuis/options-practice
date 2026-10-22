# AI log

Three records in one file: how you used AI, what the critic found, and your examiner practice. Add
rows as you go; the rubric (criterion 5) looks for this file.

## 1. AI use
One row per meaningful use, as the syllabus requires. It also shows which parts you need to be able
to explain at the demo.

| Date | Who | Tool and model | What we asked | What we kept or changed | How we checked it |
|---|---|---|---|---|---|
| 2026-10-20 | (name) | GitHub Copilot, Auto | Explain pricing.py and the tests | Nothing changed | Read the code and ran pytest |

## 2. Critic review
Run the critic agent in a **new chat session**, before each milestone and before the demo. Log every
finding, including the ones you decide not to fix, and say why. Check each finding yourself: a
second agent's opinion is not proof.

| Date | Commit reviewed | Finding | Severity (high/med/low) | What we did | Test added |
|---|---|---|---|---|---|
| | | | | | |

## 3. Examiner practice
Before the demo, run the examiner agent with `RUBRIC.md` and paste its report here. Practice scores
do not determine grades.

- Date and commit reviewed:
- Team members (3-5), GitHub usernames, and own-commit links:
- Evidence inspected and evidence it could not see:

| Criterion | Level | Maximum | Awarded | Evidence and next step |
|---|---|---|---|---|
| 1. Finance | | 25 | | |
| 2. Verification | | 25 | | |
| 3. Working app | | 10 | | |
| 4. Data and privacy | | 10 | | |
| 5. Agent supervision | | 10 | | |
| 6. Group presentation and demo (practice) | | 15 | | |

| Student | GitHub username | Own-account commit link | Criterion 7 (5 or 0) |
|---|---|---|---|
| | | | |

Use the level conversion in `RUBRIC.md`. Mark evidence the examiner could not see "not assessed",
and report a complete total only when every criterion is assessed.
