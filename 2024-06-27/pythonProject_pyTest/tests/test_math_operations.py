# test_math_operations
# math_operations_test

import pytest
from src.math_operations import add, sub, mul, div


# Standalone test functions
def test_add_simple():
    assert add(1, 2) == 3


def test_subtract_simple():
    assert sub(2, 1) == 1


def test_multiply_simple():
    assert mul(2, 1) == 2


def test_divide_simple():
    assert div(2, 1) == 2


# Test Class
class TestMathOperations:
    def test_add(self):
        assert add(-1, 1) == 0
        assert add(-1, -1) == -2

    def test_subtract(self):
        assert sub(-1, 1) == -2
        assert sub(-1, -1) == 0

    def test_multiply(self):
        assert mul(-1, 1) == -1
        assert mul(-1, -1) == 1

    def test_divide(self):
        assert div(-1, 1) == -1
        assert div(-1, -1) == 1
