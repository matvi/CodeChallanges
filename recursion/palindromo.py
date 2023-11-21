import unittest

def palindromo(word):
    if len(word) % 2 != 0:
        return False
    
    if(len(word)== 0): return True

    if(word[0] != word[len(word)-1]):
        return False
    
    return palindromo(word[1:len(word)-1])

class Test(unittest.TestCase):

    def test1(self):
        word = "abccba"
        expected = True
        response = palindromo(word)
        self.assertEqual(expected,response)

    def test_false(self):
        word = "abccbaaa"
        expected = False
        response = palindromo(word)
        self.assertEqual(expected,response)

    def test_return_false_on_if(self):
        word = "abccbaaa"
        expected = False
        response = palindromo(word)
        self.assertEqual(expected,response)

if __name__ == '__main__':
    unittest.main()