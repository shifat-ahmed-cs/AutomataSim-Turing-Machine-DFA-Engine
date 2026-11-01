"""
Unit tests for AutomataSim DFA and Turing Machine.
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.dfa import DFA
from src.turing_machine import TuringMachine

class TestAutomata(unittest.TestCase):
    def test_dfa(self):
        dfa = DFA(
            states={"q0", "q1"},
            alphabet={"a", "b"},
            transitions={("q0", "a"): "q1", ("q0", "b"): "q0", ("q1", "a"): "q1", ("q1", "b"): "q0"},
            start_state="q0",
            accept_states={"q1"}
        )
        self.assertTrue(dfa.process("a"))
        self.assertTrue(dfa.process("ba"))
        self.assertFalse(dfa.process("ab"))

    def test_tm(self):
        # TM that accepts empty string
        tm = TuringMachine(
            states={"q0", "qa", "qr"},
            alphabet={"0"},
            tape_alphabet={"0", "_"},
            transitions={("q0", "_"): ("qa", "_", "R")},
            start_state="q0",
            accept_state="qa",
            reject_state="qr"
        )
        acc, _, _ = tm.run("")
        self.assertTrue(acc)

if __name__ == "__main__":
    unittest.main()
