import pytest
from pipeline import render_tex

def t(tex):
    return render_tex(tex, False, False, "raw", {"fonts": "serif"})

def test_binary_op_spacing():
    # Binary operators should have spaces around them
    assert t("a + b") == "𝑎 + 𝑏"
    assert t("x - y") == "𝑥 - 𝑦"
    assert t(r"\alpha \pm \beta") == "α ± β"
    assert t(r"x \times y") == "𝑥 × 𝑦"

def test_relation_spacing():
    # Relations should have spaces around them
    assert t("E = mc^2") == "𝐸 = 𝑚𝑐²"
    assert t(r"a \approx b") == "𝑎 ≈ 𝑏"
    assert t(r"x \neq y") == "𝑥 ≠ 𝑦"
    assert t(r"x \leq y") == "𝑥 ≤ 𝑦"
    assert t(r"x \in X") == "𝑥 ∈ 𝑋"

def test_unary_op_spacing():
    # Unary operators should NOT have spaces after them (or before if at start)
    # Standard LaTeX: +x remains +x (no space)
    assert t("+x") == "+𝑥"
    assert t("-y") == "-𝑦"
    # f(x) = -y should have space around = but not after -
    assert t("f(x) = -y") == "𝑓(𝑥) = -𝑦"

def test_multiple_ops():
    assert t(r"a + b = c") == "𝑎 + 𝑏 = 𝑐"
    assert t(r"x \pm y \mp z") == "𝑥 ± 𝑦 ∓ 𝑧"

def test_accents_and_ops():
    assert t(r"\hat{x} + \bar{y}") == "𝑥̂ + 𝑦̄"
