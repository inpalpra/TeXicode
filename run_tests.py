#!/usr/bin/env python3

import subprocess
import sys

# Add tests directory to path so we can import test_data
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'tests')))

from test_data import CORE_TESTS, ALIGNMENT_TESTS, MATRIX_TESTS, OVERSET_TESTS, MATRIX_BRACE_TESTS

# ==========================================
# TeXicode Regression Test Suite
# ==========================================
# Now reading seamlessly from tests/test_data.py

def run_suite(name, tests):
    print(f"\033[0;36m{'=' * 42}\033[0m")
    print(f"\033[0;36mRunning {name} tests...\033[0m")
    print(f"\033[0;36m{'=' * 42}\033[0m")
    for test, _ in tests:
        print(f"\033[0;36m=== TEST: [ {test} ] ===\033[0m")
        subprocess.run([sys.executable, "src/main.py", test])
        print("")

if __name__ == "__main__":
    run_suite("CORE", CORE_TESTS)
    run_suite("ALIGNMENT", ALIGNMENT_TESTS)
    run_suite("MATRIX", MATRIX_TESTS)
    run_suite("OVERSET", OVERSET_TESTS)
    run_suite("MATRIX_BRACE", MATRIX_BRACE_TESTS)
