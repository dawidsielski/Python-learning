import unittest

def if_letter_in_string(s, l = None):
    if l is None:
        return False
    if l in s:
        return True
    return False


class TestWord(unittest.TestCase):

    def test_letter(self):
        self.assertTrue(if_letter_in_string("lower", "l"))

    def test_letter_not_in_sequence(self):
        self.assertFalse(if_letter_in_string("door", "a"))

    def test_bad_letter(self):
        self.assertRaises(TypeError, if_letter_in_string, *["dawid", 3])
    
    def test_none_letter(self):
        self.assertFalse(if_letter_in_string("dawid"))
def main():    
    # if_letter_in_string("dawid")
    pass

if __name__ == "__main__":
    main()
    unittest.main()

    