# Forge Sprint 02 — Multi-Agent Slack Orchestration System

This repository implements a fully automated two-agent coordination loop utilizing **Hermes** (the brain) and **OpenClaw** (the hands) wired directly into Slack to solve coding tasks under human-in-the-loop validation.

## 🛠️ Architecture Overview

The division of labor, communication pipelines, and configurations are detailed in [ARCHITECTURE.md](file:///c:/Users/khare/Desktop/Resume_PLC/nmg/forge-sprint-02/ARCHITECTURE.md).

- **Hermes (Brain):** Meta Llama 3.3 70B via OpenRouter. Handles planning, task decomposition, and code reviews.
- **OpenClaw (Hands):** Llama 3.3 70B via Groq. Handles actual coding execution, writes files, runs local shell tasks.
- **Slack (Comms):** Wired using Slack Socket Mode + Event Subscriptions for direct DM or channel communication.

---

## 📂 Project Structure

```
├── ARCHITECTURE.md          # Division of labor, model routing, Slack scheme
├── agent-log.md             # Unedited transcript of the Slack agent run
├── openclaw.json            # OpenClaw agent and Slack config (secrets removed)
├── hermes.config.yaml       # Hermes model and orchestrator config (secrets removed)
├── .env.example             # Template for required environment secrets
├── fetch_titles.py          # Solution Python scraper script
├── results.json             # Generated output JSON file
├── scripts/
│   └── demo.py              # CLI-based local simulation of the agent loop
├── tests/
│   └── test_fetch.py        # Automated test suite verifying the solution
└── evidence/
    ├── agent-run-transcript.json # Clean runtime token log and timestamp transcript
    └── Windows PowerShell - 16 July 2026.mp4 # Session walkthrough video
```

---

## 🚀 Setup & Execution Guide

### 1. Set Up Environment Variables
Create a local `.env` file (copied from `.env.example`) or export these keys in your shell:
```powershell
$env:GROQ_API_KEY="your-groq-key"
$env:OPENROUTER_API_KEY="your-openrouter-key"
$env:SLACK_BOT_TOKEN="xoxb-your-bot-token"
$env:SLACK_APP_TOKEN="xapp-your-app-token"
```

### 2. Configure Slack Bot Gateway
1. Set up a custom Slack app at [api.slack.com/apps](https://api.slack.com/apps).
2. Configure **OAuth Scopes** for Bot: `chat:write`, `users:read`, `channels:read`, `groups:read`, `mpim:read`, `im:read`, `im:history`, `channels:history`, `app_mentions:read`.
3. Enable **Socket Mode** and add Event Subscriptions for: `app_mention`, `message.channels`, `message.im`.
4. Install to workspace.

### 3. Run the Gateway
Start the Hermes gateway in your PowerShell terminal to listen to Slack Socket Mode events:
```powershell
hermes gateway
```

Start the OpenClaw gateway in another terminal window:
```powershell
openclaw gateway
```

---

## 🎯 Verification & Testing

### Test Suite Execution
Verify the scraper functionality using the automated test suite:
```powershell
python tests/test_fetch.py -v
```

### Local CLI Verification
To simulate the planning -> execution -> review loop locally without hitting Slack Socket Mode endpoints:
```powershell
python scripts/demo.py
```
This script calls Groq/OpenRouter endpoints directly, outputs timestamps, log tracks, and token counts, saving the transcript to `evidence/agent-run-transcript.json`.
