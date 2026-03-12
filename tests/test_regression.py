import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from pipeline import render_tex

def render(tex):
    return render_tex(tex, debug=False, color=False, context="raw", options={"fonts": "serif"})

def test_fraction():
    tex = r'\frac{1}{2}'
    expected = "\n".join([
        "  1 ",
        " ╶─╴",
        "  2 "
    ])
    assert render(tex) == expected

def test_integral():
    tex = r'\int_0^1 x\,dx = \frac{1}{2}'
    expected = "\n".join([
        " ⌠¹      1 ",
        " │ 𝑥 𝑑𝑥=╶─╴",
        " ⌡₀      2 "
    ])
    assert render(tex) == expected

def test_summation():
    tex = r'\sum_{i=0}^{n} x_i'
    expected = "\n".join([
        "  ₙ   ",
        " ┰─╴  ",
        " ▐╸ 𝑥ᵢ",
        " ┸─╴  ",
        " ⁱ⁼⁰  "
    ])
    assert render(tex) == expected

def test_left_right():
    tex = r'\left( \frac{a}{b} \right)'
    expected = "\n".join([
        " ⎛ 𝑎 ⎞",
        " ⎜╶─╴⎟",
        " ⎝ 𝑏 ⎠"
    ])
    assert render(tex) == expected

def test_accents():
    tex = r'\hat{x} + \bar{y} + \vec{z}'
    expected = " 𝑥̂+𝑦̄+𝑧⃗"
    assert render(tex) == expected

def test_greek_letters():
    tex = r'\alpha + \beta = \gamma'
    expected = " α+β=γ"
    assert render(tex) == expected

def test_inline_equation():
    tex = r'E = mc^2'
    expected = " 𝐸=𝑚𝑐²"
    assert render(tex) == expected

def test_binomial():
    tex = r'\binom{n}{k}'
    expected = "\n".join([
        " ⎛𝑛⎞",
        " ⎜ ⎟",
        " ⎝𝑘⎠"
    ])
    assert render(tex) == expected

def test_square_root():
    tex = r'\sqrt{\frac{a^2+b^2}{c^2}}'
    expected = "\n".join([
        "  ┌───────╴",
        "  │ 𝑎²+𝑏²  ",
        "  │╶─────╴ ",
        " ╰┘  𝑐²    "
    ])
    assert render(tex) == expected

def test_limit():
    tex = r'\lim_{x \to \infty} f(x)'
    expected = "\n".join([
        " lim𝑓(𝑥)",
        " 𝑥→∞    "
    ])
    assert render(tex) == expected

def test_align_environment():
    tex = r'\begin{align} a &= b + c \\ d &= e + f \end{align}'
    expected = "\n".join([
        "𝑎=𝑏+𝑐",
        "     ",
        "𝑑=𝑒+𝑓"
    ])
    assert render(tex) == expected
