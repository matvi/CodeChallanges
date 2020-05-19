import unittest
import numpy as np


def solution(arrA, arrB, v):
    for a in arrA:
        for b in arrB:
            if(a+b == v):
                return True
    return False

#this solution doesnt contemplate that the arrayA and arrayB have different size
def betterSolution(arrA, arrB, v):
    #we are going to use set() that is a HashSet with time complexity of O(1)
    complement_set = set()
    for a in arrA:
        complement_set.add(v-a)
    for b in arrB:
        if b in complement_set:
            return True
    
    return False
    

class TestSolution(unittest.TestCase):

    def test1(self):
        a = np.array([5,3,8,9])
        b = np.array([2,1,0,5])
        v = 10
        res = betterSolution(a,b,v)
        self.assertEqual(res, True, 'must be True')

    def test2(self):
        a = np.array([5,3,8,9])
        b = np.array([2,1,0,5])
        v = 100
        res = betterSolution(a,b,v)
        self.assertEqual(res, False, 'must be False')

    def test3(self):
        a = np.array([5,3,8,50])
        b = np.array([2,1,0,50])
        v = 100
        res = betterSolution(a,b,v)
        self.assertEqual(res, True, 'must be True')

    def test4(self):
        a = np.array([5,3,8,-5])
        b = np.array([2,1,0,5])
        v = 10
        res = betterSolution(a,b,v)
        self.assertEqual(res, True, 'must be True')

if __name__ == "__main__":
    unittest.main()