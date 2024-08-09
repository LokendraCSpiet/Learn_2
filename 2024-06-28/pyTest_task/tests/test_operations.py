# # test_math_operations
# # math_operations_test
#
# import pytest
# import os
# from src.operations import add, sub
#
#
# @pytest.fixture(scope="class")
# def math_fixture():  # math obj
#     print("Setup Math Fixture")
#     # You can put any setup code here
#     os.mkdir("Test Directory")
#     yield
#     # Any code after the yield statement is considered teardown code
#     os.rmdir("Test Directory")
#     print("Teardown Math Fixture")
#
#
# class TestMathOperations:
#     def test_add(self, math_fixture):
#         assert add(1, 2) == 3
#         assert add(-1, 1) == 0
#         assert add(-1, -1) == -2
#
#     def test_subtract(self, math_fixture):
#         assert sub(2, 1) == 1
#         assert sub(-1, 1) == -2
#         assert sub(-1, -1) == 0


import pytest
import os
import tempfile
import shutil


@pytest.fixture(scope="function")
def temp_dir():
    """
    Pytest fixture to create and destroy a temporary directory for each test.
    """
    temp_dir_path = tempfile.mkdtemp()
    yield temp_dir_path
    # shutil.rmtree(temp_dir_path)


class TestWithTempDirectory:

    def test_example(self, temp_dir):
        """
        Example test method that uses the temp_dir fixture.
        """
        # The test can use temp_dir to perform operations within the temporary directory.
        temp_file = os.path.join(temp_dir, 'temp_file.txt')
        with open(temp_file, 'w') as f:
            f.write("Hello, World!")

        # Check if the file was created
        assert os.path.isfile(temp_file)
        print(f"Test: Verified creation of {temp_file}")
