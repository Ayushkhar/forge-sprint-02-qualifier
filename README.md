# Forge Sprint 02 Qualifier — Hermes × OpenClaw Edition

A two-agent AI system built for **NMG Labs Forge Sprint 02**. This repository demonstrates autonomous multi-agent collaboration using **Hermes** (orchestrator) and **OpenClaw** (coder) communicating over Slack.

## Stack
| Component | Tool | Model |
|---|---|---|
| Orchestrator | Hermes Agent | `llama-3.3-70b-versatile` via Groq |
| Coder | OpenClaw | `llama-3.3-70b-versatile` via Groq |
| Communication | Slack (Socket Mode) | — |

## Agent Capabilities
- **Hermes Agent:** Plans tasks, routes instructions to OpenClaw via Slack, and fires custom skills (e.g., `hello-world`) from the `skills/` directory. Configured with local memory persistence so it can recall facts across sessions.
- **OpenClaw:** Receives tasks from Hermes, writes Python scripts, runs them, and reports back in a structured `What I Did / What Failed / What Needs Review` format.

## Project Structure
```
forge-sprint-02/
├── hermes.config.json        # Hermes model + memory + skills config
├── skills/
│   └── hello-world/
│       └── SKILL.md          # Custom skill: greet the NMG Labs team
├── openclaw/
│   └── IDENTITY.md           # OpenClaw persona and communication protocol
├── scripts/
│   └── fetch_titles.py       # Mini-challenge: fetch webpage titles
│   └── results.json          # Output from fetch_titles.py
├── tests/
│   └── test_fetch.py         # Unit tests for fetch_titles.py
├── agent-log.md              # Simulated Slack chat log
└── .github/workflows/ci.yml  # GitHub Actions CI quality gate
```

## Mini-Challenge Result
The `fetch_titles.py` script fetches webpage titles for 3 URLs and saves them to `results.json`. Run it yourself:
```bash
python scripts/fetch_titles.py
```

## Running Locally
1. Make sure `node` (v20+) and `python` (3.11+) are installed.
2. Set your Groq API key:
   ```powershell
   $env:GROQ_API_KEY="your_key_here"
   ```
3. Start Hermes:
   ```bash
   npx hermes-agent@latest chat
   ```
4. Start OpenClaw (in a separate terminal):
   ```bash
   npx openclaw@latest onboard
   ```

## CI/CD Quality Gate
GitHub Actions automatically runs `tests/test_fetch.py` on every push and pull request to ensure the fetching logic works correctly and handles invalid URLs gracefully.
