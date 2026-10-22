# Set up your coding agent

Each teammate can use a different agent. All of them run inside your Codespace and read
`AGENTS.md`, so the project rules apply whichever one you pick. If you have no subscription,
use GitHub Copilot: it is free for verified students.

| Agent | Cost for you | Command |
|---|---|---|
| GitHub Copilot, chat panel | Free with Copilot Student (GitHub Education) or Copilot Free | none: click the chat icon |
| GitHub Copilot CLI | Same plan as above | `copilot` |
| Antigravity CLI (Google) | Free weekly quota with a Google account; more with Google AI Pro | `agy` |
| Codex CLI (OpenAI) | Included with every ChatGPT plan; Free and Go have low limits | `codex` |
| Claude Code (Anthropic) | Claude Pro or Max; not the free plan | `claude` |

Gemini CLI no longer serves free or Google AI Pro accounts (since June 18, 2026). Google's
replacement is Antigravity CLI. Checked October 19, 2026: these tools change often, so if a step
below fails, check the tool's own instructions (links at the end).

## 1. Install and sign in (once per Codespace)
Open a terminal: menu ☰ → Terminal → New Terminal. A Codespace is a remote computer, so signing in
means opening a link in your browser and, for some tools, copying a code back into the terminal.

**Copilot chat panel.** Nothing to install. Click the Copilot icon at the top of the window and
sign in with GitHub if asked.

**Copilot CLI**
```
curl -fsSL https://gh.io/copilot-install | bash
copilot
```
In a Codespace it signs in with a device code: open the link it shows and enter the code. If it
reports a token or permission error, run `copilot login`.

**Antigravity CLI**
```
curl -fsSL https://antigravity.google/cli/install.sh | bash
agy
```
Maximize the terminal panel first: the sign-in link is long and wraps over several lines.
Choose **Google OAuth**, open the link (Ctrl+click; if the page shows an error, copy the whole
link instead), sign in, copy the code the page shows and paste it into the terminal. If it says
"secret keyring is locked", use Copilot for now and see Antigravity's troubleshooting page
(link below).

**Codex CLI**
First, in ChatGPT: Settings → Security → turn on **device code authorization** (in a school or
work workspace, an admin may have to allow it). Then:
```
sudo apt-get update && sudo apt-get install -y bubblewrap
curl -fsSL https://chatgpt.com/codex/install.sh | sh
codex login --device-auth
codex
```
(Codex uses `bubblewrap` to keep its commands inside your project on Linux.)

**Claude Code**
```
curl -fsSL https://claude.ai/install.sh | bash
claude
```
Choose your Claude subscription. Press `c` to copy the sign-in link, open it, and paste the code
back at "Paste code here if prompted".

"Command not found" after an install? Run `export PATH="$HOME/.local/bin:$PATH"` or open a new
terminal.

## 2. The same moves in every tool

| | Copilot chat | Copilot CLI | Antigravity CLI | Codex CLI | Claude Code |
|---|---|---|---|---|---|
| **Plan first** (reads, changes nothing) | Type `/plan`, or pick **Plan** in the agent menu | Shift+Tab to plan mode | Shift+Tab to plan, or `agy --mode plan` | `/plan` | Shift+Tab to plan mode, or `/plan` |
| **Approve each command** | Asks before terminal commands by default | Default; change with `/permissions` | Default mode | Starts in Auto (works inside the repo without asking); `/permissions` → Read Only to approve edits and commands | Starts in **auto** mode: press Shift+Tab until it shows Manual |
| **How full is the context?** | Hover the context indicator in the chat box | `/context` | `/context` | `/status` | `/context` |
| **Compact a long session** (keeps a summary) | `/compact` | `/compact` | No command: update `PLAN.md`, then `/clear` | `/compact` | `/compact` |
| **New task** (empty context) | `/clear` | `/clear` | `/clear` | `/new` | `/clear` |
| **Undo the last step** | **Restore Checkpoint** on a chat message | `/rewind` | `/rewind` | Esc Esc, then edit an earlier message | `/rewind`, or Esc Esc |
| **Pick up an earlier session** | Chat sessions list | `/resume` | `/resume`, or `agy -c` | `/resume` | `/resume`, or `claude -c` |
| **Run a team agent** | Pick `critic` or `examiner` in the agent menu | `copilot --agent critic` | New session + the prompt below | New session + the prompt below | New session + the prompt below |

**Context window.** Everything the agent sees in a session (AGENTS.md, the files it read, the
whole chat, command output) shares one context window. It is large, but accuracy drops as it fills
("context rot"), and when it is full the tool compacts it into a summary that can lose details.
So: one task per session, write decisions in `PLAN.md`, point the agent to files instead of
pasting them, and after two failed corrections start fresh (`/clear`) with a better prompt.
`/clear` empties the chat; the agent still reads `AGENTS.md`, and `PLAN.md` when you ask it to.

Prompt to run a team agent in any tool (always in a **new** session for the critic):
> Read .github/agents/critic.agent.md and follow it as your instructions for this session.
> Then review the app and its tests.

Replace `critic` with `examiner` as needed. Plan mode is built into every tool,
so there is no planner agent: `AGENTS.md` says what every plan must include.

## 3. Keys, data and your free hours
- **API keys** never go in code, chat or the repo. If a tool asks for one, store it as a
  Codespaces secret: GitHub → Settings → Codespaces → New secret, pick this repository, then stop
  and restart the Codespace. It appears as an environment variable.
- **Licensed data** (Bloomberg, WRDS, other paid sources) stays on your own computer. Do not
  upload it to the Codespace, the repo or any agent. Build with public or synthetic data.
- **Free hours:** about 60 hours a month on the default machine (90 with the GitHub Student
  Pack). Stop your Codespace when you finish: github.com/codespaces → ⋯ → Stop codespace.
- **Push before you stop.** A Codespace that stays stopped for 30 days is deleted, with any
  work you did not push.

## Links
- Copilot CLI: https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli
- Copilot in VS Code (Plan agent, custom agents): https://code.visualstudio.com/docs/agent-customization/custom-agents
- Antigravity CLI: https://antigravity.google/docs/install?tab=cli · troubleshooting: https://antigravity.google/docs/cli/troubleshooting/
- Codex CLI: https://learn.chatgpt.com/docs/codex/cli · sign-in: https://learn.chatgpt.com/docs/auth
- Claude Code: https://code.claude.com/docs/en/setup · sign-in: https://code.claude.com/docs/en/authentication
- Gemini CLI change: https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli
- Codespaces secrets: https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces
- Managing context: GitHub https://docs.github.com/en/copilot/concepts/prompting-and-context/context-management · Claude Code https://code.claude.com/docs/en/best-practices · Codex https://learn.chatgpt.com/guides/best-practices · VS Code https://code.visualstudio.com/docs/agents/best-practices
- Why long sessions degrade ("context rot"): https://research.trychroma.com/context-rot
