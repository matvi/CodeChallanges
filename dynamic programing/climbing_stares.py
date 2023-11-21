

import unittest

def climbing_stares(n):
    if n==0 : return 1
    if n<0 : return 0
    
    combination = climbing_stares(n-1) + climbing_stares(n-2)

    return combination


class Test(unittest.TestCase):
    def test1(self):
        n = 3
        expected = 3
        result = climbing_stares(n)
        self.assertEqual(expected, result)

    def test2(self):
        n = 2
        expected = 2
        result = climbing_stares(n)
        self.assertEqual(expected, result)

    

if __name__ == '__main__':
    unittest.main()