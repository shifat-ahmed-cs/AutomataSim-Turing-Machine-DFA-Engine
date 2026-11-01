"""
Entry point for CSE331_Automata_and_Computability.
Executes the comprehensive demonstration suite.
"""
import sys
import os

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from examples.demo import main

if __name__ == "__main__":
    main()
