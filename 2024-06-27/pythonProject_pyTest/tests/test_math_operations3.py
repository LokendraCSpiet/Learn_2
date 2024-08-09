# test_math_operations
# math_operations_test

import pytest
from src.math_operations import add, sub


@pytest.fixture(scope="class")
def math_fixture():  # math obj
    print("Setup Math Fixture")
    # You can put any setup code here
    yield
    # Any code after the yield statement is considered teardown code
    print("Teardown Math Fixture")


class TestMathOperations:
    def test_add(self, math_fixture):
        assert add(1, 2) == 3
        assert add(-1, 1) == 0
        assert add(-1, -1) == -2

    def test_subtract(self, math_fixture):
        assert sub(2, 1) == 1
        assert sub(-1, 1) == -2
        assert sub(-1, -1) == 0
