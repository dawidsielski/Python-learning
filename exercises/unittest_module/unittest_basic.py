import my_operations
import unittest

class TestMyOperations(unittest.TestCase):
    def test_multiplication(self):
        self.assertEqual(my_operations.multiplication(1,4),4)
    
    def test_exists(self):
        self.assertTrue(my_operations.exists([1,2,3,4], 5), True)

    def test_last(self):
        self.assertRaises(IndexError, my_operations.last, [])

if __name__ == "__main__":
    unittest.main(exit=False)