import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from test_data import STYLING_TESTS, COLOR_TESTS
from pipeline import render_tex

def render(tex, color=False):
    return render_tex(tex, debug=False, color=color, context="raw", options={"fonts": "serif"})

@pytest.mark.parametrize("tex, expected", STYLING_TESTS)
def test_styling_commands(tex, expected):
    """
    Test styling commands: boxed, color, cancel, etc.
    Tests verify that styling is applied (boxed/cancel) or ignored (color) in non-color mode.
    """
    assert render(tex) == expected

@pytest.mark.parametrize("tex, expected", COLOR_TESTS)
def test_styling_colors(tex, expected):
    """
    Test styling commands with color enabled.
    """
    assert render(tex, color=True) == expected

def test_color_enabled_manual():
    """Verify that color mode actually adds ANSI codes."""
    tex = r'\color{red}{x}'
    rendered = render_tex(tex, debug=False, color=True, context="raw", options={"fonts": "serif"})
    assert "\x1b[31m" in rendered
    assert "𝑥" in rendered
    assert "\x1b[39m" in rendered
