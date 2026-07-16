# forge sprint 02 — hermes + openclaw setup

two agent system for nmg labs forge sprint 02. hermes is the orchestrator, openclaw does the coding. they talk over slack.

## what's running

- hermes agent — llama-3.3-70b via groq, handles planning and routing
- openclaw — llama-3.3-70b via groq, does the actual coding tasks
- slack for communication between the two

## folder structure

```
scripts/fetch_titles.py   — mini challenge script
scripts/results.json      — output from the script
tests/test_fetch.py       — basic tests
skills/hello-world/       — custom skill for hermes
openclaw/IDENTITY.md      — openclaw persona config
hermes.config.json        — hermes model + memory settings
agent-log.md              — slack chat log
```

## how to run

set your groq key first:
```
$env:GROQ_API_KEY="your_key"
```

start hermes:
```
npx hermes-agent@latest chat
```

start openclaw in another terminal:
```
npx openclaw@latest onboard
```

## mini challenge

`fetch_titles.py` grabs the html title from 3 urls and saves to `results.json`. run it with:
```
python scripts/fetch_titles.py
```
