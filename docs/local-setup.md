# Working on your own laptop (VS Code)

On the Villanova network, GitHub Codespaces don't open: the network blocks the tunnels they use.
VS Code on your own laptop works anywhere, with the same repository and the same agent
(GitHub Copilot). At home you can still use a Codespace; it does steps 1-4 for you. Commit and
sync before you switch between them.

## 1. Install Git, Python 3.12 and VS Code

**Windows**
- Git: https://git-scm.com/download/win (keep every default).
- Python 3.12: https://www.python.org/downloads/windows/ (64-bit installer). On the first screen,
  tick **Add python.exe to PATH**.
- VS Code: https://code.visualstudio.com/ (leave **Add to PATH** ticked).
- Or all three in PowerShell:
  ```
  winget install -e --id Git.Git; winget install -e --id Python.Python.3.12; winget install -e --id Microsoft.VisualStudioCode
  ```

**Mac**
- Git: in Terminal, run `git --version`; if offered, install the command line developer tools.
- Python 3.12: https://www.python.org/downloads/macos/ then run
  **Applications → Python 3.12 → Install Certificates.command**.
- VS Code: https://code.visualstudio.com/ (drag it into Applications).

Check in a new terminal: `git --version` and `py -3.12 --version` (Windows) or
`python3.12 --version` (Mac).

## 2. Set up VS Code (once)
- Install the **Python** extension (by Microsoft).
- Accounts icon (bottom left) → **Sign in with GitHub**. Copilot appears in the chat panel.
- Copilot Free trains on your chats and code by default: turn it off at
  https://github.com/settings/copilot/features → Privacy.
- Tell Git who you are (Terminal → New Terminal), with the email you verified on GitHub so your
  commits count under your account:
  ```
  git config --global user.name "Your Name"
  git config --global user.email "your.name@villanova.edu"
  git config --global pull.rebase false
  ```

## 3. Clone the repository
Source Control view → **Clone Repository** → **Clone from GitHub** → pick the repository (or the
Command Palette → **Git: Clone**). Choose a folder that OneDrive or iCloud does **not** sync, such as
`C:\Users\you\code` or `~/code`. Open it and trust the authors.

## 4. Make the Python environment (once per repository)
**Windows (PowerShell)**
```
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```
**Mac**
```
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```
Let VS Code use the new environment (or Command Palette → **Python: Select Interpreter** → `.venv`).
New terminals then start with `(.venv)`. Git ignores the `.venv` folder.

## 5. Check
- `pytest`: runs the tests in `tests/`.
- `streamlit run app.py`: the app opens at http://localhost:8501 (press Enter if it asks for an
  email; Ctrl+C stops it).

## 6. The agent
Copilot Chat (chat icon at the top): **Ask**, **Plan**, **Agent**, and the team's **critic**. On
your laptop the agent runs commands on your own computer: read each command, allow it once, and
don't choose "Always allow" or auto-approve.

## 7. Every session
Sync Changes (pull) → work → `pytest` → Commit → Sync Changes (push).

## If something goes wrong
- *"python" or "py" is not recognized* (Windows): rerun the Python installer → Modify → tick
  **Add Python to environment variables**; reopen VS Code.
- *"running scripts is disabled"* when activating (Windows): run
  `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, answer Y.
- *SSL certificate error* (Mac): run **Install Certificates.command** (Applications → Python 3.12).
- *"streamlit" or "pytest" not found*: activate `.venv`, or use `python -m pytest` and
  `python -m streamlit run app.py`.
- *Push rejected*: Sync Changes first, run `pytest`, sync again (see `docs/git-and-teamwork.md`).
- *Commits don't show your name on GitHub*: set `user.email` to an email verified on your account.
