import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from test_data import CORE_TESTS, ALIGNMENT_TESTS

from pipeline import render_tex

def render(tex):
    return render_tex(tex, debug=False, color=False, context="raw", options={"fonts": "serif"})

@pytest.mark.parametrize("tex, expected", CORE_TESTS)
def test_core_regressions(tex, expected):
    """
    Data-driven test that covers fundamental syntax: fractions, integrals, sums, 
    limits, binomials, squareroots, and greek symbols.
    """
    assert render(tex) == expected

@pytest.mark.parametrize("tex, expected", ALIGNMENT_TESTS)
def test_alignment_environments(tex, expected):
    """
    Data-driven test focusing on aligned block structures: arrays, branches, gather, cases.
    """
    assert render(tex) == expected
