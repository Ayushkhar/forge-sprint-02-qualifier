"""
Real two-agent demo: Hermes (orchestrator) → OpenClaw (coder)
Uses the Cerebras API — the same provider configured in hermes.config.json
Captures real token counts, timestamps, and AI-generated code as evidence.
"""

import os
import json
import time
import datetime
from openai import OpenAI

# Groq API (free tier — same model family as hermes.config.json)
# Set GROQ_API_KEY env var before running: $env:GROQ_API_KEY="your-key-here"
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise EnvironmentError("Set GROQ_API_KEY environment variable before running.")
MODEL = "llama-3.3-70b-versatile"

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=GROQ_API_KEY,
)

LOG = []

def log(role, content, tokens=None, ts=None):
    ts = ts or datetime.datetime.utcnow().isoformat() + "Z"
    entry = {"timestamp": ts, "role": role, "content": content}
    if tokens:
        entry["tokens"] = tokens
    LOG.append(entry)
    print(f"\n[{ts}] [{role}]")
    print(content)
    if tokens:
        print(f"  -> tokens: prompt={tokens.get('prompt_tokens')} completion={tokens.get('completion_tokens')} total={tokens.get('total_tokens')}")

def call_llm(system_prompt, user_message, agent_name):
    print(f"\n{'='*60}")
    print(f"  {agent_name} is thinking...")
    print(f"{'='*60}")
    ts = datetime.datetime.utcnow().isoformat() + "Z"
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_message},
        ],
        temperature=0.3,
    )
    usage = {
        "prompt_tokens":     resp.usage.prompt_tokens,
        "completion_tokens": resp.usage.completion_tokens,
        "total_tokens":      resp.usage.total_tokens,
    }
    reply = resp.choices[0].message.content
    log(agent_name, reply, tokens=usage, ts=ts)
    return reply

# ── Step 1 : Human sends task to Hermes ──────────────────────────────────────
HUMAN_TASK = (
    "Write a Python script that fetches the HTML <title> tag from these 3 URLs "
    "and saves the results to results.json:\n"
    "- https://example.com\n"
    "- https://python.org\n"
    "- https://github.com"
)

log("human", HUMAN_TASK)

# ── Step 2 : Hermes plans and delegates ──────────────────────────────────────
HERMES_SYSTEM = """You are Hermes, an AI orchestration agent. Analyse the task and write a concise delegation to your coder sub-agent OpenClaw. State what to build and the expected output format."""

hermes_reply = call_llm(
    HERMES_SYSTEM,
    f"Task from human: {HUMAN_TASK}\n\nWrite your delegation message to OpenClaw.",
    "hermes",
)

time.sleep(1)   # brief pause — visible in timestamps

# ── Step 3 : OpenClaw receives delegation and writes code ────────────────────
OPENCLAW_SYSTEM = """You are OpenClaw, an AI coder sub-agent. Respond with a single, working Python script only."""

openclaw_reply = call_llm(
    OPENCLAW_SYSTEM,
    f"Delegation from Hermes:\n{hermes_reply}\n\nWrite the complete Python script now.",
    "openclaw",
)

time.sleep(1)

# ── Step 4 : Hermes reviews and reports back ─────────────────────────────────
hermes_final = call_llm(
    HERMES_SYSTEM,
    f"OpenClaw returned this code:\n\n{openclaw_reply}\n\n"
    "Review it briefly (2-3 sentences) and confirm to the human that the task is done.",
    "hermes (review)",
)

# ── Save transcript ───────────────────────────────────────────────────────────
out_path = "evidence/agent-run-transcript.json"
os.makedirs("evidence", exist_ok=True)
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(LOG, f, indent=2, ensure_ascii=False)

print(f"\n\n{'='*60}")
print(f"  Transcript saved -> {out_path}")
print(f"  Total turns: {len(LOG)}")
total_tokens = sum(e["tokens"]["total_tokens"] for e in LOG if "tokens" in e)
print(f"  Total tokens used: {total_tokens}")
print(f"{'='*60}\n")
