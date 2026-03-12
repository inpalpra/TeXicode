import sys
import os
import pytest

# Add src to path so we can import modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from pipeline import render_tex

def render(tex):
    # Use the same default options as main.py (serif font, raw context, no color)
    return render_tex(tex, debug=False, color=False, context="raw", options={"fonts": "serif"})

def test_bmatrix_2x2():
    tex = r'\begin{bmatrix} a & b \\ c & d \end{bmatrix}'
    expected = "\n".join([
        " ⎡ 𝑎 𝑏 ⎤",
        " ⎣ 𝑐 𝑑 ⎦"
    ])
    assert render(tex) == expected

def test_pmatrix_2x2():
    tex = r'\begin{pmatrix} a & b \\ c & d \end{pmatrix}'
    expected = "\n".join([
        " ⎛ 𝑎 𝑏 ⎞",
        " ⎝ 𝑐 𝑑 ⎠"
    ])
    assert render(tex) == expected

def test_bmatrix_3x3():
    tex = r'\begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix}'
    expected = "\n".join([
        " ⎡ 𝑎 𝑏 𝑐 ⎤",
        " ⎢ 𝑑 𝑒 𝑓 ⎥",
        " ⎣ 𝑔 ℎ 𝑖 ⎦"
    ])
    assert render(tex) == expected

def test_matrix_fractions():
    tex = r'\begin{pmatrix} \frac{1}{2} & 0 \\ 0 & 1 \end{pmatrix}'
    expected = "\n".join([
        " ⎛  1    ⎞",
        " ⎜ ╶─╴ 0 ⎟",
        " ⎜  2    ⎟",
        " ⎝  0  1 ⎠"
    ])
    assert render(tex) == expected

def test_bare_matrix():
    tex = r'\begin{matrix} a & b \\ c & d \end{matrix}'
    expected = "\n".join([
        " 𝑎 𝑏",
        " 𝑐 𝑑"
    ])
    assert render(tex) == expected


def test_vmatrix():
    tex = r'\begin{vmatrix} a & b \\ c & d \end{vmatrix}'
    expected = "\n".join([
        " │ 𝑎 𝑏 │",
        " │ 𝑐 𝑑 │"
    ])
    assert render(tex) == expected

def test_column_vector():
    tex = r'\begin{bmatrix} x \\ y \\ z \end{bmatrix}'
    expected = "\n".join([
        " ⎡ 𝑥 ⎤",
        " ⎢ 𝑦 ⎥",
        " ⎣ 𝑧 ⎦"
    ])
    assert render(tex) == expected

def test_sparam_matrix():
    tex = r'\begin{bmatrix} b_1 \\ b_2 \end{bmatrix} = \begin{bmatrix} S_{11} & S_{12} \\ S_{21} & S_{22} \end{bmatrix} \begin{bmatrix} a_1 \\ a_2 \end{bmatrix}'
    expected = "\n".join([
        "⎡ 𝑏₁ ⎤ ⎡ 𝑆₁₁ 𝑆₁₂ ⎤⎡ 𝑎₁ ⎤",
        "⎣ 𝑏₂ ⎦=⎣ 𝑆₂₁ 𝑆₂₂ ⎦⎣ 𝑎₂ ⎦"
    ])
    assert render(tex) == expected
