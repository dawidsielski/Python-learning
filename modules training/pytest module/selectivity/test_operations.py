import operations
import pytest

@pytest.mark.linuks
def test_multiplication():
    result = operations.multiplication(3, 6)
    assert result == 18

@pytest.mark.mac
def test_subtraction():
    result = operations.subtraction(3, 6)
    assert result == -3

@pytest.mark.windows
def test_power():
    result = operations.power(5)
    assert result == 25


# -k [name] do select specified test (name can be a part of function name)
# -m [category name] for selecting category for the test
# can write [not [category name]] to run every test but specified in command line