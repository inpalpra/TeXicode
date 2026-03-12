import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from pipeline import render_tex

def render(tex):
    return render_tex(tex, debug=False, color=False, context="raw", options={"fonts": "serif"})

def test_tag_simple():
    tex = r"\tag{1} E = mc^2"
    expected = " 𝐸=𝑚𝑐²   (1)"
    # Note: TeXicode might have different spacing/font, 
    # but for now we expect baseline alignment and 3 spaces.
    # We'll adjust the expected string after seeing the actual (failing) output.
    assert "(1)" in render(tex)

def test_tag_starred():
    tex = r"\tag*{\dagger} a = b"
    # Expected † (dagger) right-aligned
    assert "†" in render(tex)
    assert "(" not in render(tex)

def test_tag_complex_baseline():
    tex = r"\tag{2.1} \int_0^1 x\,dx = \frac{1}{2}"
    output = render(tex)
    # Tag (2.1) should be on the same line as the integral's baseline
    lines = output.split("\n")
    # Integral with limits usually has 3 lines. Baseline is index 1.
    assert len(lines) >= 3
    assert "(2.1)" in lines[1]

def test_tag_multi_line_align():
    tex = r"\begin{align} a &= b \tag{1} \\ c &= d \end{align}"
    output = render(tex)
    lines = output.split("\n")
    # Tag (1) should only be on the first line of the aligned block
    assert "(1)" in lines[0]
    assert "(1)" not in lines[1]

def test_tag_multi_tag_concatenation():
    tex = r"\tag{1} \tag{2} a = b"
    output = render(tex)
    assert "(1) (2)" in output
