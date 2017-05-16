import operations
import pytest
import sys

def test_multiplication():
    result = operations.multiplication(3, 6)
    assert result == 18

@pytest.mark.skipif(sys.version_info > (3,0), reason = "No reason.")
def test_subtraction():
    result = operations.subtraction(3, 6)
    assert result == -3

@pytest.mark.skip(reason="Not working.")
def test_power():
    result = operations.power(6)
    assert result == 36