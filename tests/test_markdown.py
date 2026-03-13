import subprocess
import os
import tempfile
import pytest

def run_txc_markdown(content):
    """Helper to run txc (main.py) on a temporary markdown file and return the output."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as tmp:
        tmp.write(content)
        tmp_path = tmp.name
    
    try:
        # Using sys.executable to ensure we use the same python interpreter
        import sys
        cmd = [sys.executable, "src/main.py", "-f", tmp_path]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

def test_markdown_inline_math():
    content = "The value of $x$ is 5."
    # x in serif font is 𝑥
    expected = "The value of 𝑥 is 5."
    assert run_txc_markdown(content) == expected

def test_markdown_display_math_indent():
    content = "Matrix:\n$$\nM = \\begin{bmatrix} a & b \\\\ c & d \\end{bmatrix}\n$$"
    # Should have 0 space indent as per recent update
    # The matrix render_any_root aligns by horizon.
    # For a 2x2 matrix, horizon is 1.
    # M = (horizon 0) aligns with row 1 of matrix.
    # Output should look like:
    #     ⎡ 𝑎 𝑏 ⎤
    # 𝑀 = ⎣ 𝑐 𝑑 ⎦
    output = run_txc_markdown(content)
    assert "    ⎡ 𝑎 𝑏 ⎤" in output
    assert "𝑀 = ⎣ 𝑐 𝑑 ⎦" in output
    # Verify no leading spaces on the line starting with M =
    for line in output.splitlines():
        if line.startswith("𝑀 ="):
            assert not line.startswith("  𝑀 =")

def test_markdown_code_protection():
    content = "In code: `let x = $5;` but in math: $x = 5$."
    expected = "In code: `let x = $5;` but in math: 𝑥 = 5."
    assert run_txc_markdown(content) == expected

def test_markdown_fenced_block_protection():
    content = """
```latex
\\begin{align}
  a &= b
\\end{align}
```
Outside: $\\alpha$
"""
    output = run_txc_markdown(content)
    assert "\\begin{align}" in output
    assert "Outside: α" in output

def test_markdown_escaped_dollars():
    content = "The cost is \\$10 and $x=5$."
    expected = "The cost is \\$10 and 𝑥 = 5."
    assert run_txc_markdown(content) == expected

def test_markdown_multiline_math():
    content = "Sum:\n$$\n\\sum_{i=0}^n i\n$$"
    output = run_txc_markdown(content)
    assert "┰─╴" in output  # part of the sum symbol
    assert "𝑖 = 0" in output

def test_markdown_error_fallback():
    # Syntax error in TeX should fallback to raw string
    content = "Broken: $\\frac{a}{b$."
    expected = "Broken: $\\frac{a}{b$."
    assert run_txc_markdown(content) == expected
