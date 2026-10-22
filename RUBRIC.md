# MSF 8615 app project rubric

**100 points: 95 team points + 5 points for each student's own GitHub account and commit.**
Teams have **3-5 students**. This is a group project: criteria 1-6 give one shared team score.
Every member presents part of the group presentation and demo, where the team shows that it
understands its app.

Build a small app that answers a finance question. Scope, sound reasoning, and verifiable results matter more than feature count or visual polish. AI assistance is allowed and must be disclosed. Students may use AI to learn GitHub, write code and tests, and diagnose errors; the team remains responsible for the work.

### Scoring

**Criteria 1-6 (team, 95 points).** For each criterion, select the best-supported level. Award the criterion's maximum points multiplied by: **4 = 100%, 3 = 85%, 2 = 65%, 1 = 40%, 0 = 0%**. Level 0 means no assessable evidence. Levels 4-1 are described below. Add the unrounded criterion scores and round the final total to one decimal place. Example: level 3 on a 25-point criterion earns 21.25 points.

**Criterion 7 (each student, 5 points).** All or nothing: 5 points with a commit under the student's own account, 0 without.

The instructor determines grades. Examiner scores are practice feedback only. If the examiner cannot inspect evidence, it must mark it **not assessed**, not invent a score or treat missing access as missing work. Report subtotals and available points; do not report a complete grade while criteria remain unassessed.

### Evidence to submit

- Repository and runnable app, deployed on Streamlit Community Cloud with data permitted for publication. Include a short recording or screenshots as a backup.
- README: question, method, inputs and outputs, data source and date, assumptions, limitations, run instructions, and team members.
- Tests and independently established expected results, including their sources or calculations. Teams choose and justify checks suited to their project.
- AI_LOG.md: AI use, the critic review, and examiner practice, identifying the version or commit reviewed.
- For each member: GitHub username and a link to at least one commit made under their own account.
- The group presentation and demo, in which every member presents.

An approved local demonstration can substitute where data restrictions prevent public deployment. A temporary hosting outage is not itself evidence of an incorrect app; use the runnable version and backup. Apply course academic-integrity and privacy policies separately; this rubric does not create automatic misconduct penalties.

## 1. Financial question, method, and correctness (25 points; team)

What we look for: A useful, bounded financial question and an appropriate calculation whose assumptions, conventions, and interpretation are clear. Evaluate the submitted results, not how much code the team wrote.

- 4: The method fits the question; core results are correct for the stated scope. Units, signs, timing, and contract conventions are consistent. The team distinguishes observed inputs, assumptions, and scenarios, and explains important limitations without overstating conclusions.
- 3: The central method and results are sound. Minor omissions in assumptions, conventions, or interpretation do not materially change the answer.
- 2: The question is identifiable, but a material error or unjustified assumption affects some results, or the interpretation extends beyond what the method supports.
- 1: The method is poorly matched or insufficiently specified, or central numerical results or conclusions are unreliable.

## 2. Independent verification and tests (25 points; team)

What we look for: Evidence that important calculations were checked against results established independently of the implementation, plus relevant boundary or failure cases. pytest is a way to repeat these checks, not the learning objective.

- 4: Important displayed calculations have traceable independent benchmarks or financial consistency checks. Tests cover relevant units, boundaries, and invalid inputs. The team explains tolerances and what the tests cannot establish, and provides reproducible test results.
- 3: Main calculations have appropriate independent checks and repeatable tests. Coverage or explanation has minor gaps, but the central results are supported.
- 2: Some useful checks exist, but important outputs remain unchecked, expected results are weakly sourced, or important edge cases are missing.
- 1: Verification consists mainly of visual plausibility, asking AI whether it is correct, or comparing the implementation with itself. Passing tests provide little independent support.

## 3. Working app and reproducibility (10 points; team)

What we look for: A usable app with clear inputs and outputs that another person can run or inspect. A small, complete app can earn full credit.

- 4: The app works within its stated scope, labels inputs and outputs clearly, handles relevant invalid inputs, and avoids presenting invalid results as valid. Run instructions, dependencies, and permitted sample data support reproduction. The demonstration is accessible or has an approved alternative.
- 3: The core workflow works and is reproducible. Minor usability, error-handling, or setup problems do not obscure the financial result.
- 2: The app works only for a narrow example or needs substantial help to run. Missing labels or input handling make some results hard to interpret.
- 1: The main workflow cannot be demonstrated reliably or another person cannot reproduce the result from the supplied materials.

## 4. Data, assumptions, and privacy (10 points; team)

What we look for: Traceable data and responsible handling of what is sent to AI services, stored in cloud workspaces, and published. Synthetic data and modeled scenarios are acceptable when appropriate and clearly labeled.

- 4: Sources, dates, units, and transformations are documented. Observed data and scenarios are distinct. The team documents permitted uses, keeps restricted information and credentials out of unauthorized destinations, and checks public outputs and downloads.
- 3: Data provenance, scenario labels, and handling are appropriate, with minor documentation gaps.
- 2: Important provenance, transformation, permission, or scenario-labeling information is missing, leaving the evidence or sharing arrangements difficult to assess.
- 1: Data provenance is largely absent, invented observations are presented as real, or the handling of restricted information or credentials is demonstrably inappropriate.

## 5. Agent supervision, critic review, and disclosure (10 points; team)

What we look for: Deliberate delegation, inspection of outputs, a separate critic review, and an honest account of AI assistance. A second agent's opinion is not independent numerical proof.

- 4: The team sets bounded tasks and acceptance checks, documents significant AI assistance, runs a fresh critic review, verifies findings, and records fixes or justified disagreements. The rubric examiner is used for practice and gaps lead to follow-up work. Logs identify the version reviewed.
- 3: AI use is disclosed and the critic and examiner are used meaningfully. The team responds to findings, with minor gaps in records or follow-up.
- 2: The agents are used, but review is superficial, the team accepts findings without checking, or important assistance and responses are poorly documented.
- 1: The team largely accepts AI output without review, provides little usable disclosure, or supplies no meaningful critic/examiner evidence.

## 6. Group presentation and demo (15 points; team)

What we look for: The team presents and demonstrates its app, and every member presents part of it (excused absences excepted). The team shows that it understands the app's financial purpose, a central calculation, and the evidence that supports it, and answers questions. One team score. Students need not memorize syntax, commands, or every line of code.

- 4: The team explains the method, input units, and meaning of a selected output; traces it to a relevant check; reasons through a changed input or failure case; and explains a limitation and its own decisions.
- 3: Explains the main calculation and checks accurately with occasional prompting, and recognizes the main limitations.
- 2: Explains the broad purpose but needs substantial prompting to connect inputs, outputs, checks, and assumptions, or makes a material conceptual error.
- 1: Cannot explain a central result or its verification, or relies on "the AI did it" instead of financial reasoning.

## 7. Own GitHub account and commit (5 points; each student)

What we look for: Each student has their own GitHub account and has made at least one commit under it that adds something the project needs (code, a test, data and its notes, documentation, or rows in the AI log), visible in the team repository's history. Students choose what to commit; an empty or placeholder file does not count.

- 5 points: At least one such commit made under the student's own account is visible in the team repository by the deadline on Brightspace.
- 0 points: No such commit, for example only an empty or placeholder file, a teammate committed the student's work, or the team shared one account.

### Examiner and instructor recording sheet

Criteria 1-6: record one row per criterion with level (0-4 or not assessed), maximum points, awarded points, evidence or commit reference, and improvement needed, and a team subtotal out of 95. Criterion 7: one row per student with GitHub username, commit link, and 5 or 0 (or not assessed). Do not change the weights or rubric to improve a practice score. This rubric applies to the app project, not to the separate presentation assignment.
