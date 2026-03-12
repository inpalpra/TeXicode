import sys
import os
import pytest

# Ensure the src directory is in the path
sys.path.insert(0, os.path.abspath("src"))

from pipeline import render_tex

def test_overset():
    tex = r"\overset{\text{def}}{=}"
    output = render_tex(tex, False, False, "raw", {"fonts": "normal"})
    # Expected: 
    #  def
    #   =
    lines = output.strip().split("\n")
    assert len(lines) == 2
    assert "def" in lines[0]
    assert "=" in lines[1]

def test_underset():
    tex = r"\underset{x \to 0}{\lim}"
    output = render_tex(tex, False, False, "raw", {"fonts": "normal"})
    # Expected:
    #  lim
    #  x→0
    lines = output.strip().split("\n")
    assert len(lines) == 2
    assert "lim" in lines[0]
    assert "x→0" in lines[1]

def test_stackrel():
    tex = r"\stackrel{*}{\longrightarrow}"
    output = render_tex(tex, False, False, "raw", {"fonts": "normal"})
    # Expected:
    #  *
    #  ⟶
    lines = output.strip().split("\n")
    assert len(lines) == 2
    assert "*" in lines[0]
    assert "⟶" in lines[1]

def test_underbrace():
    tex = r"\underbrace{a + b + c}_{3 \text{ terms}}"
    output = render_tex(tex, False, False, "raw", {"fonts": "normal"})
    # Expected at least 3 rows: content, brace, label
    lines = output.strip().split("\n")
    assert len(lines) >= 3
    assert "a + b + c" in lines[0] or "a+b+c" in lines[0]
    assert "┬" in lines[1] # middle of underbrace pointing down
    assert "3 terms" in lines[2]

def test_overbrace():
    tex = r"\overbrace{x + y}^{2}"
    output = render_tex(tex, False, False, "raw", {"fonts": "normal"})
    # Expected at least 3 rows: label, brace, content
    lines = output.strip().split("\n")
    assert len(lines) >= 3
    assert "²" in lines[0]
    assert "┴" in lines[1] # middle of overbrace pointing up
    assert "x + y" in lines[2] or "x+y" in lines[2]

def test_xarrow():
    # Mandatory argument only
    tex = r"\xrightarrow{\text{yields}}"
    output = render_tex(tex, False, False, "raw", {"fonts": "normal"})
    lines = output.strip().split("\n")
    assert len(lines) == 2
    assert "yields" in lines[0]
    assert ">" in lines[1]
    
    # Mandatory + optional argument
    tex = r"\xrightarrow[below]{above}"
    output = render_tex(tex, False, False, "raw", {"fonts": "normal"})
    lines = output.strip().split("\n")
    assert len(lines) == 3
    assert "above" in lines[0]
    assert ">" in lines[1]
    assert "below" in lines[2]

    # xleftarrow
    tex = r"\xleftarrow{\text{back}}"
    output = render_tex(tex, False, False, "raw", {"fonts": "normal"})
    lines = output.strip().split("\n")
    assert len(lines) == 2
    assert "back" in lines[0]
    assert "<" in lines[1]
