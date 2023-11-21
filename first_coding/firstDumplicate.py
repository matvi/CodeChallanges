import numpy as np
import unittest

#this solution is a good solution but it uses space
#this solution is an O(n)
def solution(arrayA):
    l = len(arrayA)
    if(l == 0): return -1
    b = set()

    for n in arrayA:
        if(n>l or n<0): return -1

    for n in arrayA:
        if(n in b):
            return n
        else:
            b.add(n)
    return -1

def secondSolution(arrayA):
    for i in range(len(arrayA)):
        num = arrayA[i] -1
        if arrayA[num] < 0:
            return arrayA[i]
        else :
            arrayA[num] = arrayA[num] * -1
    return -1


class TestFirstDumplicate(unittest.TestCase):

    def test_ArrayMustNotHaveNegativeNumbers(self):
        a = np.array([1,-1,1,2,3,0])
        res = solution(a)
        self.assertEqual(res, -1, "Must be -1")

    def test_ArrayMustNotHaveNumberGreaterThanTheArryaLenght(self):
        a = np.array([1,10,1,2,3,0])
        res = solution(a)
        self.assertEqual(res, -1, "Must be -1")

    def test_ArrayMustHaveDuplicates(self):
        a = np.array([1,2,3,4,5,6])
        res = solution(a)
        self.assertEqual(res, -1, "Must be -1")

    def test_return1(self):
        a = np.array([1,2,3,1,5,2])
        res = solution(a)
        self.assertEqual(res, 1, "Must be 1")

    def test_return2(self):
        a = np.array([1,2,3,0,5,2])
        res = solution(a)
        self.assertEqual(res, 2, "Must be 2")

    def test_return5(self):
        a = np.array([1,2,3,4,5,5])
        res = solution(a)
        self.assertEqual(res, 5, "Must be 5")


 # Test second solution.
    def test_ArrayMustHaveDuplicates2(self):
        a = np.array([1,2,3,4,5,6])
        res = secondSolution(a)
        self.assertEqual(res, -1, "Must be -1")

    def test_return1_2(self):
        a = np.array([1,2,3,1,5,2])
        res = secondSolution(a)
        self.assertEqual(res, 1, "Must be 1")

    def test_return2_2(self):
        a = np.array([1,2,3,4,5,2])
        res = secondSolution(a)
        self.assertEqual(res, 2, "Must be 2")

    def test_return5_2(self):
        a = np.array([1,2,3,4,5,5])
        res = secondSolution(a)
        self.assertEqual(res, 5, "Must be 5")

if __name__ == "__main__":
    unittest.main()

    