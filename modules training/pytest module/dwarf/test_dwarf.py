import dwarf
import pytest

def test_dwarf():
    result = dwarf.solution(3)
    assert result == [1, 0, 0]

@pytest.mark.parametrize('input, expected',
                        [
                            (1, [1]),
                            (2, [1,0]),
                            (3, [1,0,0])
                        ]
                        )
def test_dwarf_2(input, expected):
    result = dwarf.solution(input)
    assert result == expected