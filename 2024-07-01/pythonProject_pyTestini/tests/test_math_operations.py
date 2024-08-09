import pytest
from src.math_operations import MathOperations

# Create a MathOperations instance

math_ops = MathOperations()


@pytest.mark.parametrize("number, expected", [
    (0, 1),
    (1, 1),
    (3, 6),
    (5, 120)
])
def test_factorial(number, expected):
    assert math_ops.factorial(number) == expected


def test_factorial_negative():
    with pytest.raises(ValueError, match="Negetive numbers do not have a factorial."):
        math_ops.factorial(-1)
