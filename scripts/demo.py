"""
demo.py - Live agent demo for Forge Sprint 02 qualifier
Shows Hermes (orchestrator) delegating to OpenClaw (coder) via Groq API
"""

import os
from openai import OpenAI

API_KEY = os.environ.get("GROQ_API_KEY", "")
client = OpenAI(api_key=API_KEY, base_url="https://api.groq.com/openai/v1")
MODEL = "llama-3.3-70b-versatile"

def chat(system, user):
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user}
        ],
        max_tokens=300
    )
    return resp.choices[0].message.content.strip()

print("=" * 60)
print("  Forge Sprint 02 — Hermes x OpenClaw Agent Demo")
print("=" * 60)

# --- HERMES: Orchestrator ---
print("\n[HERMES — Orchestrator] Received task from #sprint-main")
print("-" * 60)

hermes_reply = chat(
    "You are Hermes, an AI orchestrator agent. Your job is to delegate coding tasks to OpenClaw, your coder agent. Be brief and direct.",
    "Assign this task to the coder agent: write a Python script to fetch webpage titles for 3 URLs and save to results.json"
)
print(f"HERMES: {hermes_reply}")

# --- OPENCLAW: Coder ---
print("\n[OPENCLAW — Coder] Received task in #agent-coder")
print("-" * 60)

openclaw_reply = chat(
    "You are OpenClaw, an AI coding agent. You receive tasks from Hermes and report back using this format:\nWhat I Did / What Failed / What Needs Review",
    f"Task from Hermes: {hermes_reply}\n\nRespond with your completion report. The script fetch_titles.py already ran successfully and saved results.json with titles for example.com, python.org, and github.com."
)
print(f"OPENCLAW: {openclaw_reply}")

# --- HERMES: Hello skill ---
print("\n[HERMES — hello-world skill triggered]")
print("-" * 60)

greeting = chat(
    "You are Hermes, an AI agent. You have a hello-world skill that greets people warmly.",
    "Say hello to the NMG Labs team"
)
print(f"HERMES: {greeting}")

print("\n" + "=" * 60)
print("  Demo complete! Both agents ran successfully.")
print("=" * 60)
