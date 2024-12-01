import operators
import pytest
import numpy as np

"""
Tests for operators.

To run all tests, type pytest at top level like:
    pytest

To run only the tests in this file, do this:
    pytest -q python/test_operators.py
"""


class TestSwitch:

    def test_switch_false(self):
        res = operators.switch(False, 0.35)
        assert res == 0.35

    def test_switch_true(self):
        res = operators.switch(True, 0.35)
        assert res == 0


class TestPhaseWrap:

    def test_phasewrap_within(self):
        res1 = operators.phasewrap(2.516)
        res2 = operators.phasewrap(-2.516)
        assert res1 == 2.516
        assert res2 == -2.516

    def test_phasewrap_above(self):
        res = operators.phasewrap(5.519)
        assert res == -0.7641853071795861

    def test_phasewrap_below(self):
        res = operators.phasewrap(-4.289)
        assert res == 1.9941853071795865


class TestHistory:

    def test_history_get_last_value(self, new_history):
        res = new_history.get_last_value(4)
        next_res = new_history.get_last_value(5)
        assert res == 3
        assert next_res == 4


class TestPeek:

    def test_peek_get_second_sample_in_first_channel(self, new_buffer):
        res = new_buffer.get_sample(0, 1)
        assert res == 0.02

    def test_peek_get_third_sample_in_second_channel(self, new_buffer):
        res = new_buffer.get_sample(1, 1)
        assert res == 0.05

