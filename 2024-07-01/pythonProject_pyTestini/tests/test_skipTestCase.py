import pytest
import sys


@pytest.mark.skipif(sys.platform == "win32", reason="Does not run on windows")
def test_not_on_windows():
    assert True


@pytest.mark.skip(reason="Skipping this test")
def test_skip():
    assert True

