import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from test_data import MATRIX_TESTS

from pipeline import render_tex

def render(tex):
    return render_tex(tex, debug=False, color=False, context="raw", options={"fonts": "serif"})

@pytest.mark.parametrize("tex, expected", MATRIX_TESTS)
def test_matrix_environments(tex, expected):
    """
    Data-driven test that renders complex matrix alignments and sub/super scripts
    using data extracted into test_data.py
    """
    assert render(tex) == expected
