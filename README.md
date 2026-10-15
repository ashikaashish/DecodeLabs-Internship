# Project 1: Rule-Based AI Chatbot 🤖
**DecodeLabs · Artificial Intelligence · Industrial Training Kit (Batch 2026)**

A deterministic ("white box") chatbot built with pure control flow and logic.
No machine learning, no external libraries, just Python 3.

## Spec checklist (from the project brief)
| Requirement | How it's met |
|---|---|
| INPUT LOOP: continuous `while` cycle | `while True:` in `run_chatbot()` |
| SANITIZATION: case & whitespace | `sanitize()` → `.lower().strip()` + punctuation removal |
| KNOWLEDGE BASE: dictionary with 5+ intents | `INTENTS` in `knowledge_base.py` (11 intents) |
| FALLBACK: default response for unknowns | `RESPONSES.get(clean_input, FALLBACK_RESPONSE)` |
| EXIT STRATEGY: clean break command | `exit / quit / bye / goodbye` → `break` |
| Handle greetings & exit commands | `greeting` intent + `EXIT_COMMANDS` |

## Project structure
```
rule_based_chatbot/
├── chatbot.py            # IPO model + main loop
├── knowledge_base.py     # intents, exit commands, fallback text
├── tests/test_chatbot.py # unit tests
└── README.md
```

## Run
```bash
python chatbot.py
```
## Test
```bash
python -m unittest discover tests -v
```

## Sample session
```
You:   HELLO!!
DecodeBot: Hi there! I'm DecodeBot. How can I help you today?
You: what is ipo
DecodeBot: IPO = Input -> Process -> Output. ...
You: pizza
DecodeBot: I do not understand that yet. Try 'help' to see what I can talk about.
You: bye
DecodeBot: Goodbye! Thanks for chatting. Keep building! 🚀
```

## Design notes
- **IPO model:** Input (sanitize) → Process (intent match) → Output (reply).
- **Why a dictionary, not an if-elif ladder?** `dict.get()` is O(1); a ladder is O(n) and becomes technical debt as rules grow.
- **Extend it:** add a new entry to `INTENTS` with `patterns` and `response`. No other code changes needed. Duplicate patterns are caught at start-up.

## Ideas to go further (from the brief's conclusion)
- Expand the vocabulary and add a personality.
- Add nested conditions or state (e.g. remember the user's name).
- Hybrid architecture: rule match → instant reply, otherwise pass to an LLM (Project 2 bridge: exact keys → semantic vectors).
