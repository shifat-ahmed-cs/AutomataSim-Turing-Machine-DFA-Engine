"""
Deterministic Finite Automata (DFA) Engine with Hopcroft State Minimization.
"""
from typing import Set, Dict, Tuple, List

class DFA:
    def __init__(self, states: Set[str], alphabet: Set[str], transitions: Dict[Tuple[str, str], str], start_state: str, accept_states: Set[str]):
        self.states = set(states)
        self.alphabet = set(alphabet)
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = set(accept_states)

    def process(self, input_string: str) -> bool:
        curr = self.start_state
        for char in input_string:
            if char not in self.alphabet:
                return False
            curr = self.transitions.get((curr, char), None)
            if curr is None:
                return False
        return curr in self.accept_states
