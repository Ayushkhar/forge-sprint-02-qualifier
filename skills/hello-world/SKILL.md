---
name: hello-world
description: Greets a person or team by name. Fires when the user asks Hermes to say hello to someone.
---

# Hello World Skill

## Trigger
When the user asks to greet someone or says something like "say hello to the NMG Labs team".

## Context
This skill demonstrates Hermes's ability to fire pre-defined skills from its skills directory based on natural language triggers.

## Steps
1. Parse the name or team from the user's input.
2. Compose a warm, enthusiastic greeting addressed to that person or team.
3. Post the greeting as a reply in Slack.
4. Append the greeting to `greetings.md` in the project root for a persistent log.

## Output Format
Reply with:
> "👋 Hello, [Name/Team]! Greetings from the Forge Sprint 02 multi-agent system. Hermes + OpenClaw are live and ready to build!"
