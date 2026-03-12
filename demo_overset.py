import sys
import os

# Ensure the src directory is in the path
sys.path.insert(0, os.path.abspath("src"))

from pipeline import render_tex

def demo():
    test_cases = [
        (r"\overset{\text{def}}{=}", "Test 1: overset"),
        (r"\underset{x \to 0}{\lim}", "Test 2: underset"),
        (r"\underbrace{a + b + c}_{3 \text{ terms}}", "Test 3: underbrace"),
        (r"\overbrace{x + y}^{2}", "Test 4: overbrace"),
        (r"\stackrel{*}{\longrightarrow}", "Test 5: stackrel (alias for overset)"),
        (r"\xrightarrow{\text{yields}}", "Test 6: xrightarrow"),
        (r"\xleftarrow{\text{back}}", "Test 7: xleftarrow"),
    ]
    
    options = {"fonts": "normal"}
    
    for tex, description in test_cases:
        print(f"=================== {description} ===================")
        print(f"Expression: {tex}")
        try:
            result = render_tex(tex, False, False, "raw", options)
            print("Output:")
            print(result)
        except Exception as e:
            print(f"Error rendering {tex}: {e}")
        print("\n")

if __name__ == "__main__":
    demo()
