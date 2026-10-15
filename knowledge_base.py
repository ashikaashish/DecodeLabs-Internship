"""
knowledge_base.py
-----------------
The chatbot's "brain": a dictionary of intents.

Each intent has:
  - patterns : phrases the user might type (already lowercase, no punctuation)
  - response : what the bot says back

At start-up, build_lookup() flattens this into a single
{phrase: response} dictionary so every lookup is O(1) via dict.get(),
instead of a slow O(n) if-elif ladder.
"""

BOT_NAME = "DecodeBot"

# Words/phrases that terminate the program (the "Kill Command").
EXIT_COMMANDS = {"exit", "quit", "bye", "goodbye", "see you", "stop"}

EXIT_MESSAGE = "Goodbye! Thanks for chatting. Keep building! 🚀"

FALLBACK_RESPONSE = (
    "I do not understand that yet. Try 'help' to see what I can talk about."
)

INTENTS = {
    "greeting": {
        "patterns": ["hello", "hi", "hey", "hii", "good morning",
                     "good afternoon", "good evening", "namaste"],
        "response": f"Hi there! I'm {BOT_NAME}. How can I help you today?",
    },
    "how_are_you": {
        "patterns": ["how are you", "how are you doing", "how r u",
                     "whats up", "what's up", "sup"],
        "response": "I'm running at 100% logic efficiency. Thanks for asking!",
    },
    "name": {
        "patterns": ["what is your name", "whats your name",
                     "who are you", "your name"],
        "response": f"I'm {BOT_NAME}, a rule-based chatbot built at DecodeLabs.",
    },
    "purpose": {
        "patterns": ["what can you do", "what do you do", "why do you exist"],
        "response": ("I match your message against predefined rules and reply "
                     "with a hard-coded answer. No guessing, no hallucinations."),
    },
    "rule_based_ai": {
        "patterns": ["what is a rule based chatbot", "what is rule based ai",
                     "rule based ai"],
        "response": ("A rule-based chatbot follows explicit if-else / lookup "
                     "rules written by a developer. Same input, same output, "
                     "every time."),
    },
    "ai": {
        "patterns": ["what is ai", "what is artificial intelligence"],
        "response": ("Artificial Intelligence is the field of building machines "
                     "that perform tasks that normally need human intelligence, "
                     "like understanding language or making decisions."),
    },
    "ipo": {
        "patterns": ["what is ipo", "what is the ipo model", "ipo model"],
        "response": ("IPO = Input -> Process -> Output. Sanitize the input, "
                     "match the intent, then generate the response."),
    },
    "dictionary": {
        "patterns": ["why dictionary", "why use a dictionary",
                     "dictionary vs if else"],
        "response": ("A dictionary gives O(1) constant-time lookup, while a long "
                     "if-elif ladder is O(n) and becomes hard to maintain."),
    },
    "help": {
        "patterns": ["help", "menu", "commands", "options"],
        "response": ("Try: 'hello', 'how are you', 'what is your name', "
                     "'what can you do', 'what is ai', 'what is ipo', "
                     "'thanks', or 'bye' to quit."),
    },
    "thanks": {
        "patterns": ["thanks", "thank you", "thx", "ty"],
        "response": "You're welcome! Happy to help.",
    },
    "joke": {
        "patterns": ["tell me a joke", "joke", "make me laugh"],
        "response": ("Why do programmers prefer dark mode? "
                     "Because light attracts bugs. 🐛"),
    },
}


def build_lookup(intents=INTENTS):
    """Flatten INTENTS into a single {phrase: response} dictionary."""
    lookup = {}
    for intent_name, data in intents.items():
        for phrase in data["patterns"]:
            if phrase in lookup:
                raise ValueError(
                    f"Duplicate pattern '{phrase}' found in intent '{intent_name}'"
                )
            lookup[phrase] = data["response"]
    return lookup
