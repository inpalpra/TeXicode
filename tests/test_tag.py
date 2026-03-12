import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from test_data import TAG_TESTS

from pipeline import render_tex

def render(tex):
    return render_tex(tex, debug=False, color=False, context="raw", options={"fonts": "serif"})

@pytest.mark.parametrize("tex, expected", TAG_TESTS)
def test_tag_feature(tex, expected):
    """
    Data-driven test for Equation Tags feature
    using data extracted into test_data.py
    """
    assert render(tex) == expected
