import dwarf
import pytest

def test_dwarf():
    result = dwarf.solution(3)
    assert result == [1, 0, 0]
