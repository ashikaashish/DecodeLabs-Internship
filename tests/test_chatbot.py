import os
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import chatbot
from knowledge_base import INTENTS, FALLBACK_RESPONSE, EXIT_MESSAGE


class TestSanitize(unittest.TestCase):
    def test_case_and_whitespace(self):
        self.assertEqual(chatbot.sanitize("  HeLLo  "), "hello")

    def test_punctuation(self):
        self.assertEqual(chatbot.sanitize('Hello "'), "hello")
        self.assertEqual(chatbot.sanitize("Hi!!!"), "hi")

    def test_inner_spaces(self):
        self.assertEqual(chatbot.sanitize("how   are    you"), "how are you")

    def test_apostrophe_kept(self):
        self.assertEqual(chatbot.sanitize("What's up?"), "what's up")


class TestResponses(unittest.TestCase):
    def test_at_least_five_intents(self):
        self.assertGreaterEqual(len(INTENTS), 5)

    def test_greeting(self):
        self.assertIn("Hi there", chatbot.get_response("hello"))

    def test_fallback(self):
        self.assertEqual(chatbot.get_response("asdfgh"), FALLBACK_RESPONSE)

    def test_empty(self):
        self.assertIn("type something", chatbot.get_response(""))

    def test_exit_commands(self):
        for word in ("exit", "quit", "bye", "goodbye"):
            self.assertTrue(chatbot.is_exit_command(word))
        self.assertFalse(chatbot.is_exit_command("hello"))


class TestLoop(unittest.TestCase):
    def test_loop_runs_then_exits(self):
        with patch("builtins.input", side_effect=["  HELLO ", "blah", "BYE"]), \
             patch("builtins.print") as mock_print:
            chatbot.run_chatbot()
        printed = " ".join(str(c.args[0]) for c in mock_print.call_args_list)
        self.assertIn("Hi there", printed)
        self.assertIn(FALLBACK_RESPONSE, printed)
        self.assertIn(EXIT_MESSAGE, printed)

    def test_ctrl_c_exits_cleanly(self):
        with patch("builtins.input", side_effect=KeyboardInterrupt), \
             patch("builtins.print"):
            chatbot.run_chatbot()   # must not raise


if __name__ == "__main__":
    unittest.main()
