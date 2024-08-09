# test_math_operations
# math_operations_test

import pytest
from src.math_operations import add, sub


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (-1, -1, -2),
    (0, 0, 0)
])
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, -1),
    (-1, 1, -2),
    (-1, -1, 0),
    (0, 0, 0)
])
def test_sub(a, b, expected):
    assert sub(a, b) == expected
