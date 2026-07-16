# Forge Sprint 02 Qualifier Build

This repository contains the required setup for the Forge Sprint 02 Edition 1 Qualifier. 

## Models Used
- **Orchestrator (Hermes Agent):** GPT-OSS 120B via Groq API. Chosen for its high-dimensional reasoning and planning capabilities.
- **Coder (OpenClaw):** Qwen2.5-Coder 7B via Ollama. Chosen for local, fast, and cost-efficient execution.

## Agent Capabilities
- **Hermes Agent:** Acts as the orchestrator. Plans tasks, decomposes goals, and routes instructions to OpenClaw. Configured with a `hello-world` skill and local persistence for memory.
- **OpenClaw:** Acts as the coder. Receives tasks via Slack, executes the python script, and reports back using the "What I Did / What Failed / What Needs Review" format.

## Configuration Details
- **Memory:** `persistence` is set to local. The agent is able to recall facts across sessions.
- **Skills:** Found under `skills/hello-world`. Fired automatically when a greeting is requested.
- **Slack Communication:** Full logs available in `agent-log.md`.

## Mini-Challenge
The `fetch_titles.py` script was written by OpenClaw to fetch webpage titles for 3 URLs and save them to `results.json`.

## How to Run
1. Ensure `node` and `git` are installed.
2. Ensure you have the `GROQ_API_KEY` set.
3. Start Hermes: `npx hermes-agent@latest`
4. Start OpenClaw: `npx openclaw@latest`
