import unittest

def valid_word_all(k,words):
    if k=='' : return [[]]

    array_result = []
    for w in words:
        if(k.startswith(w)):
            result = valid_word_all(k[len(w):], words)
            for sub_array in result:
                sub_array.append(w)
                array_result.append(sub_array)
    
    return array_result

class Test(unittest.TestCase):
    def test1(self):
        words = ['ab', 'c']
        k = 'abc'
        result = valid_word_all(k, words)   
        expected = [['c', 'ab']] 
        self.assertEqual(result, expected)

    def test2(self):
        words = ['ab','a','bc', 'c']
        k = 'abc'
        result = valid_word_all(k, words)   
        expected = [['c', 'ab'],['bc','a']] 
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
