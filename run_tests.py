#!/usr/bin/env python3

import subprocess
import sys
import os

# Add tests directory to path so we can import test_data
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'tests')))

import test_data

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
    # Get all available suites from test_data automatically
    # We look for any variable that ends in _TESTS (excluding the combined ALL_TESTS)
    found_suites = []
    for attr_name in dir(test_data):
        if attr_name.endswith("_TESTS") and attr_name != "ALL_TESTS":
            suite_name = attr_name[:-6] # Remove "_TESTS"
            suite_data = getattr(test_data, attr_name)
            if isinstance(suite_data, list):
                found_suites.append((suite_name, suite_data))
    
    # Run them all (sorted alphabetically for consistency)
    for name, tests in sorted(found_suites):
        run_suite(name, tests)
