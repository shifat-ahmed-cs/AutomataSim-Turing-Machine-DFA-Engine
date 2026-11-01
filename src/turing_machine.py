"""
Deterministic Turing Machine (TM) with Infinite Tape and Transition Step Tracing.
"""
from typing import Dict, Tuple, Optional

class TuringMachine:
    def __init__(self, states: set, alphabet: set, tape_alphabet: set, transitions: Dict[Tuple[str, str], Tuple[str, str, str]], start_state: str, accept_state: str, reject_state: str, blank_symbol: str = '_'):
        self.states = states
        self.alphabet = alphabet
        self.tape_alphabet = tape_alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.blank = blank_symbol

    def run(self, input_string: str, max_steps: int = 1000) -> Tuple[bool, str, int]:
        """Runs TM returning (accepted, final_tape_str, steps_taken)."""
        tape = list(input_string) if input_string else [self.blank]
        head = 0
        state = self.start_state
        steps = 0

        while steps < max_steps:
            if state == self.accept_state:
                return True, "".join(tape).strip(self.blank), steps
            if state == self.reject_state:
                return False, "".join(tape).strip(self.blank), steps

            sym = tape[head] if 0 <= head < len(tape) else self.blank
            trans_key = (state, sym)

            if trans_key not in self.transitions:
                return False, "".join(tape).strip(self.blank), steps

            next_state, write_sym, direction = self.transitions[trans_key]
            tape[head] = write_sym
            state = next_state

            if direction == 'R':
                head += 1
                if head == len(tape):
                    tape.append(self.blank)
            elif direction == 'L':
                head -= 1
                if head < 0:
                    tape.insert(0, self.blank)
                    head = 0

            steps += 1

        return False, "".join(tape).strip(self.blank), steps
