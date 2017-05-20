import unittest

def if_letter_in_string(s, l = None):
    results = []
    if l == None: 
        return False
    for word in s:
        if l not in word:
            results.append(False)
        else:
            results.append(True)
    return results

seq = "dawid daria dom domeczek".split()
seq1 = "awi aria om omeczek".split()

class TestWordList(unittest.TestCase):

    def test_letter(self):
        self.assertTrue(if_letter_in_string("lower", "l"))

    def test_letter_not_in_sequence(self):
        self.assertTrue(if_letter_in_string("door", "a")) # check again

    def test_bad_letter(self):
        self.assertRaises(TypeError, if_letter_in_string, *["dawid", 3])
    
    def test_none_letter(self):
        self.assertFalse(if_letter_in_string("dawid"))

    def test_list(self):
        result = if_letter_in_string(seq, "d")
        for element in result:
            self.assertTrue(element)

    def test_list_false(self):
        result = if_letter_in_string(seq1, "d")
        for element in result:
            self.assertFalse(element)


if __name__ == "__main__":
    unittest.main()