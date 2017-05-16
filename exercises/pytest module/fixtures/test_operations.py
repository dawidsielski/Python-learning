import operations
import pytest

def test_multiplication():
    result = operations.multiplication(3, 6)
    assert result == 18

def test_subtraction():
    result = operations.subtraction(3, 6)
    assert result == -3

@pytest.mark.parametrize("test_input, expected_output",
                         [   
                            (2, 4),
                            (3, 10)
                         ]
                        )
def test_power(test_input, expected_output):
    result = operations.power(test_input)
    assert result == expected_output