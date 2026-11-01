# AutomataSim: Finite Automata, Formal Grammars & Turing Machine Simulator

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![CI: Passing](https://img.shields.io/badge/build-passing-brightgreen.svg)](.github/workflows/ci.yml)
[![Domain: Theoretical CS](https://img.shields.io/badge/domain-Theory%20of%20Computation-red.svg)]()
[![Academic: BRACU CSE331](https://img.shields.io/badge/course-CSE%20331-orange.svg)]()

## 📌 Course Context: CSE 331 (Automata and Computability)
*Department of Computer Science and Engineering, BRAC University*  
**Core Principles:** Deterministic Finite Automata (DFA), Nondeterministic Finite Automata (NFA), Regular Expressions, Context-Free Grammars, Turing Machines, and Decidability.

---

## 🎯 Formal Computational Models

1. **Deterministic Finite Automaton (DFA):**
   - 5-tuple specification: $M = (Q, \Sigma, \delta, q_0, F)$
   - String verification over transition function $\delta : Q \times \Sigma \to Q$.
2. **Deterministic Turing Machine (TM):**
   - 7-tuple model: $M = (Q, \Sigma, \Gamma, \delta, q_0, q_{accept}, q_{reject})$
   - Infinite linear tape simulation with bidirectional read/write head movement ($L, R$).
   - Executable binary arithmetic demonstration (unary/binary incrementer).

---

## 🚀 Quickstart & Testing
```bash
# Run demonstration
python main.py

# Run unit tests
python -m unittest discover -s tests
```
