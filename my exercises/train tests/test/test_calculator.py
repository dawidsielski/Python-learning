import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_fail(self):
        self.assertFalse(False)