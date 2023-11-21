
import unittest

def valid_word_count(k, array_words):
    if k == '' : return 1
    count = 0

    for word in array_words:
        is_starts = k.startswith(word)
        if(is_starts):
            result = valid_word_count(k[len(word):], array_words)
            count += result
    
    return count


        

class Test(unittest.TestCase):
    def test1 (self):
        array = ['ab', 'xcd', 'cdf']
        k = 'abcdf'
        expected = 1

        response = valid_word_count(k, array)

        self.assertEqual(response, expected)

    def test2 (self):
        array = ['ab', 'xcd', 'xcdf']
        k = 'abcdf'
        expected = 0

        response = valid_word_count(k, array)

        self.assertEqual(response, expected)

    def test3 (self):
        array = ['ab', 'abc', 'cd', 'def', 'abcd']
        k = 'abcdef'
        expected = 1

        response = valid_word_count(k, array)

        self.assertEqual(response, expected)

    # def test2 (self):
    #     array = ['xab', 'xcd', 'xcdf']
    #     k = 'abcdf'
    #     expected = False

    #     response = valid_word_count(k, array)

    #     self.assertEqual(response, expected)

    # def test_3 (self):
    #     array = ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']
    #     k = 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef'
    #     expected = False

    #     response = valid_word_count(k, array)

    #     self.assertEqual(response, expected)





if __name__ == '__main__':
    unittest.main()