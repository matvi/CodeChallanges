#reverse string using recursion
import unittest
def reverse_words(array_words):
    if len(array_words) == 1 : return array_words[0]
    
    return array_words[len(array_words)-1] + reverse_words(array_words[0:len(array_words)-1])

class Test(unittest.TestCase):
    def test(self):
        array = ["three", "two ","one "]
        expected = "one two three"
        result = reverse_words(array)
        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()
