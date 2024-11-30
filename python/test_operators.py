import operators
import pytest

"""
Tests for operators.

To run all tests, type pytest at top level like:
    pytest

To run only the tests in this file, do this:
    pytest -q python/test_operators.py
"""

@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]


class TestSwitch:

    def test_switch_false(self):
        res = operators.switch(False, 0.35)
        assert res == 0

    def test_switch_true(self):
        res = operators.switch(True, 0.35)
        assert res == 0.35


class TestPeek:
    """
    """

    def test_peek_something(self):
        res = 0
        assert res == 1


# class TestHistory:
#     """
#     """

#     def test_history_something(self):
#         res = 0
#         assert res == 1

