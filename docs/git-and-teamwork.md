# Working as a team on one repository

Each teammate opens their **own** Codespace. Each Codespace is a separate copy of the repository:
your work reaches your teammates only when you **commit and push**, and theirs reaches you only
when you **pull**. We all work on the `main` branch.

## Team size and your own commit
Teams have **3-5 students**. One member creates the repository and invites the other **2-4**.
Every member makes **at least one commit under their own GitHub account** that adds something the
project needs: a formula, a test, a data file and its notes, part of the README, or rows in
`AI_LOG.md`. You decide what; an empty or placeholder file does not count. That commit is worth
**5 points per student** (all or nothing). Check the history together, and never share accounts.
The other **95 points are shared** by the team, and every member presents part of the group
presentation and demo.

## Every session
1. `git pull`: get your teammates' latest work before you change anything.
2. Work on your own part (agree who owns which file, and list it in the README's Team contributions table).
3. `pytest`: the tests must pass.
4. Commit small steps: `git add -A` then `git commit -m "Add delta to the Greeks table"`.
5. `git pull` again, then `git push`.
6. Stop your Codespace (github.com/codespaces → ⋯ → Stop codespace). Push first.

The Source Control panel (the branch icon on the left) does the same with buttons: write a message,
**Commit**, then **Sync Changes** (pull and push).

## Rules that prevent most conflicts
- **One owner per file.** Split the app into modules (for example `greeks.py`, `hedging.py`) and
  pages, and agree who edits which. `app.py` stays short and calls the modules.
- **One person edits `requirements.txt`**, or say so in the team chat before you do.
- **One agent per Codespace at a time.** Two agents changing the same files will collide.
- **No drive-by reformatting.** Reformatting a whole file changes every line and conflicts with
  everyone. `AGENTS.md` tells agents not to.
- **Push at least once a day.** Small, frequent pushes conflict less than one big push.
- **A red ✗ next to a commit on GitHub** means the tests failed after that push. Whoever pushed it
  fixes it first, before anyone builds on it.

## "Updates were rejected" when you push
A teammate pushed first. Run `git pull`, check `pytest`, then `git push` again.

## When git says CONFLICT
Two people changed the same lines. Git stops and marks the file:
```
<<<<<<< HEAD
x = 100        <- your version
=======
x = 10         <- your teammate's version
>>>>>>> 18e5406...
```
Nothing is lost. To fix it:
1. Open the file. VS Code shows **Accept Current Change**, **Accept Incoming Change** and
   **Accept Both Changes** above each conflict, or **Resolve in Merge Editor** for a side-by-side
   view. Or ask your agent:
   > Resolve the merge conflict in app.py. Show me both versions and explain each choice before
   > you change anything, then run pytest.
2. Delete any leftover `<<<<<<<`, `=======` and `>>>>>>>` lines.
3. `pytest`, then `git add -A`, `git commit -m "Merge teammate's changes"`, and `git push`.

Changed your mind halfway? `git merge --abort` puts everything back as it was before the pull
(this works because you committed before pulling).
Talk to the teammate whose change you are overwriting.

**Never** run `git push --force` (it deletes your teammates' work on GitHub), and never delete a
Codespace that has work you have not pushed.

## If `git pull` says "Need to specify how to reconcile divergent branches"
The template's Codespace sets this up for you. If you see it anyway, run once:
`git config --global pull.rebase false`, then `git pull` again.

## If a text editor opens after `git pull`
Git is asking for a message for the merge commit. The template's Codespace turns this off. If
it happens anyway: in a VS Code tab, close the tab; in the terminal editor `nano`, press Ctrl+X;
in `vi`, type `:wq` and press Enter. Next time use `git pull --no-edit`.

## Later: branches and pull requests (optional)
Once you are comfortable, work on a branch for each feature (`git switch -c greeks-table`), push
it, and open a pull request on GitHub. Your teammates review it, the tests run on it, and you
merge when they pass. This keeps `main` working at all times. On GitHub Free, rules that *require*
this are available for public repositories; for private ones the owner needs GitHub Pro (free
with the Student Pack).

Links: GitHub flow https://docs.github.com/en/get-started/using-github/github-flow ·
merge conflicts in VS Code https://code.visualstudio.com/docs/sourcecontrol/merge-conflicts ·
Codespaces lifecycle https://docs.github.com/en/codespaces/about-codespaces/understanding-the-codespace-lifecycle
