"""
Demonstration of AutomataSim: DFA String Acceptance and Turing Machine Binary Incrementer.
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.dfa import DFA
from src.turing_machine import TuringMachine

def main():
    print("=" * 65)
    print("       AUTOMATASIM: FORMAL LANGUAGES & TURING MACHINES        ")
    print("=" * 65)

    # 1. DFA: Accepts binary strings ending with '01'
    states = {"q0", "q1", "q2"}
    alphabet = {"0", "1"}
    transitions = {
        ("q0", "0"): "q1", ("q0", "1"): "q0",
        ("q1", "0"): "q1", ("q1", "1"): "q2",
        ("q2", "0"): "q1", ("q2", "1"): "q0"
    }
    dfa = DFA(states, alphabet, transitions, start_state="q0", accept_states={"q2"})

    test_strings = ["101", "1001", "1110", "01", "10"]
    print("[+] DFA Simulation (Language: strings ending with '01'):")
    for s in test_strings:
        res = dfa.process(s)
        print(f"    - String '{s:<6}' -> {'ACCEPTED' if res else 'REJECTED'}")

    # 2. Turing Machine: Binary Incrementer (adds 1 to binary number)
    # Alphabet: 0, 1, _
    tm_trans = {
        ("q_scan", "0"): ("q_scan", "0", "R"),
        ("q_scan", "1"): ("q_scan", "1", "R"),
        ("q_scan", "_"): ("q_add", "_", "L"),
        ("q_add", "1"): ("q_add", "0", "L"),
        ("q_add", "0"): ("q_done", "1", "L"),
        ("q_add", "_"): ("q_done", "1", "L"),
    }
    tm = TuringMachine(
        states={"q_scan", "q_add", "q_done", "q_rej"},
        alphabet={"0", "1"},
        tape_alphabet={"0", "1", "_"},
        transitions=tm_trans,
        start_state="q_scan",
        accept_state="q_done",
        reject_state="q_rej"
    )

    in_val = "1011"  # 11 in decimal
    acc, out_val, steps = tm.run(in_val)
    print(f"\n[+] Turing Machine Execution (Binary Increment):")
    print(f"    - Input Tape  : {in_val} (dec: {int(in_val, 2)})")
    print(f"    - Output Tape : {out_val} (dec: {int(out_val, 2)})")
    print(f"    - Steps Taken : {steps} (Halted in Accept State: {acc})")
    print("=" * 65)

if __name__ == "__main__":
    main()
