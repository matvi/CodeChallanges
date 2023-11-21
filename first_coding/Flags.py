import numpy as np
import unittest
import math


def solution(A,k):
    B = getPicks(A)
    max_flags = mat.sqr(len(A)) + 2 

def getPicks(A):
    B = np.zeros(len(A))
    
    #create B who is an array representing 1 as picks
    for i in range (len(A)-1):
        if A[i] > A [i+1]:
            B[i] = 1
        #checking the last element
        if i == len(A) -2:
            if A[i+1] > A[i]:
                B[i+1] = 1
    return B

def getMaxFlags(B,k):
    count = 0
    flags = k

    #for i in range(len(B)):
    i = 0
    while(k>0):
        if i >= len(B):
            return count
        if B[i] == 1:
            k -= 1
            count +=1
            i = i + flags
        else:
            i += 1
    return count

class TestFlags(unittest.TestCase):
    #this will create an array with picks as 1 and no picks as 0
    def testCreatingArrayWithPicks(self):
        a = np.array([1,5,3,4,3,4,1,2,3,4,6,2])
        res = getPicks(a)
        expected = np.array([0,1,0,1,0,1,0,0,0,0,1,0])
        sol = np.allclose(res, expected)
        self.assertEqual(sol, True, "must be tru")

    def testSolution1(self):
        a = np.array([1,5,3,4,3,4,1,2,3,4,6,2])
        res = getMaxFlags(a,2)
        expected = 2
        sol = np.allclose(res, expected)
        self.assertEqual(sol, True, "must be {}".format(expected))

    def testSolution2(self):
        a = np.array([1,5,3,4,3,4,1,2,3,4,6,2])
        res = getMaxFlags(a,3)
        expected = 3
        sol = np.allclose(res, expected)
        self.assertEqual(sol, True, "must be {}".format(expected))

    def testSolution3(self):
        a = np.array([1,5,3,4,3,4,1,2,3,4,6,2])
        res = getMaxFlags(a,4)
        expected = 3
        sol = np.allclose(res, expected)
        self.assertEqual(sol, True, "must be {}".format(expected))

if __name__ == "__main__":
    unittest.main()
