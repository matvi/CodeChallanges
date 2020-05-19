import numpy as np
import unittest

#using dictionary
def firstNotRepeatingCharacter(s):
    rep = {}
    for c in s:
        if (c in rep):
            rep[c] += 1
        else:
            rep[c] = 0
    #the elements in the dictionary are not sorted so we can just loop through the entire dictionary
    for c in s:
        if rep[c] == 0:
            return c
    return '_'


class TestFirstNotR(unittest.TestCase):

    def test1(self):
        a = "abacabad"
        res = firstNotRepeatingCharacter(a)
        self.assertEqual(res, 'c' , 'Must be c')
    
    def test2(self):
        a = "abgaabadc"
        res = firstNotRepeatingCharacter(a)
        self.assertEqual(res, 'g' , 'Must be g')

    def test3(self):
        a = "abggaabacddc"
        res = firstNotRepeatingCharacter(a)
        self.assertEqual(res, '_' , 'Must be _')

if __name__ == "__main__":
    unittest.main()
