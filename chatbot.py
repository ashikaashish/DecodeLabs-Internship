"""
chatbot.py
----------
Project 1: Rule-Based AI Chatbot  |  DecodeLabs AI Industrial Training Kit

Architecture follows the IPO model:
    INPUT   -> sanitize()      (case + whitespace + punctuation normalization)
    PROCESS -> get_response()  (O(1) dictionary lookup with .get() fallback)
    OUTPUT  -> print reply     (inside a continuous while-loop)

Run:  python chatbot.py
"""

import string

from knowledge_base import (
    BOT_NAME,
    EXIT_COMMANDS,
    EXIT_MESSAGE,
    FALLBACK_RESPONSE,
    build_lookup,
)

# Build the flat {phrase: response} dictionary ONCE at start-up.
RESPONSES = build_lookup()

# Translation table that removes punctuation, but keeps apostrophes
# so phrases like "what's up" still match.
_PUNCT_TABLE = str.maketrans(
    "", "", "".join(c for c in string.punctuation if c != "'")
)


# --------------------------------------------------------------------------
# PHASE 1: INPUT & SANITIZATION
# --------------------------------------------------------------------------
def sanitize(raw_input: str) -> str:
    """Normalize raw user text: lowercase, strip, remove punctuation,
    collapse repeated spaces.   '  HeLLo!!  ' -> 'hello'
    """
    cleaned = raw_input.lower().strip()
    cleaned = cleaned.translate(_PUNCT_TABLE)
    return " ".join(cleaned.split())


# --------------------------------------------------------------------------
# PHASE 2: PROCESS (intent matching)
# --------------------------------------------------------------------------
def is_exit_command(clean_input: str) -> bool:
    return clean_input in EXIT_COMMANDS


def get_response(clean_input: str) -> str:
    """Atomic lookup + fallback in one call (dict.get)."""
    if not clean_input:
        return "Please type something so I can help you."
    return RESPONSES.get(clean_input, FALLBACK_RESPONSE)


# --------------------------------------------------------------------------
# PHASE 3: OUTPUT + THE HEARTBEAT (infinite loop)
# --------------------------------------------------------------------------
def run_chatbot() -> None:
    print("=" * 60)
    print(f"  {BOT_NAME} - Rule-Based AI Chatbot (DecodeLabs Project 1)")
    print("  Type 'help' for options, or 'exit' / 'bye' to quit.")
    print("=" * 60)

    while True:                                   # continuous loop
        try:
            raw_input_text = input("You: ")       # INPUT
        except (EOFError, KeyboardInterrupt):     # Ctrl+D / Ctrl+C = clean exit
            print(f"\n{BOT_NAME}: {EXIT_MESSAGE}")
            break

        clean_input = sanitize(raw_input_text)    # SANITIZE

        if is_exit_command(clean_input):          # KILL COMMAND
            print(f"{BOT_NAME}: {EXIT_MESSAGE}")
            break

        print(f"{BOT_NAME}: {get_response(clean_input)}")   # PROCESS + OUTPUT


if __name__ == "__main__":
    run_chatbot()
