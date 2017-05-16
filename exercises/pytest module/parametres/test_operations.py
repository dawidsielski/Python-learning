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
                            (3, 9)
                         ]
                        )
def test_power(test_input, expected_output):
    result = operations.power(test_input)
    assert result == expected_output

@pytest.mark.parametrize("test_input, expected_output",
                        [
                            ([1,2,3,4],4),
                            ([4,3,2,1],1)
                        ]
                        )
def test_last_list_element(test_input, expected_output):
    try:
        result = operations.last_list_element(test_input)
    except IndexError:
        assert True
    assert result == expected_output


def test_no_element_in_list():
    with pytest.raises(IndexError):
        operations.last_list_element([])

@pytest.mark.xfail(raises = IndexError)
def test_no_element_in_list2():
    operations.last_list_element([])

def test_no_element_in_list3():
    pytest.raises(IndexError, "operations.last_list_element([])")