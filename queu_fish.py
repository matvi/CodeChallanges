
from collections import deque
import numpy as np
import unittest

def getFish(array):
    if len(array) == 1 or checkIfhasToCompute(array) is False:
        return array
    l = []
    for i in range(len(array)):
        if (len(l) == 0):
            l.append(array[i])
        else:
            item = l.pop()
            # if item is positive and nextItem is negative
            if(item > 0 and array[i] <0):
                left = abs(item)
                right = abs(array[i])
                if (left > right):
                    l.append(item)
                else:
                    l.append(array[i])
            else:
                l.append(item)
                l.append(array[i])
    res = getFish(l)
    return res

#it will check if there are some + and - fishes that means that it should process the array
def checkIfhasToCompute(a):
    for i in range(len(a)-1):

        if a[i] > 0 and a[i+1] < 0 :
            return True
    return False


class TestGetFish(unittest.TestCase):

    def test_checkIfhasToCompute(self):
        a = np.array([8,8,5,3,5])
        res = checkIfhasToCompute(a)
        self.assertEqual(res, False, "should be false")
    
    def test_checkIfhasToCompute2(self):
        a = np.array([8,8,-5,3,5])
        res = checkIfhasToCompute(a)
        self.assertEqual(res, True, "should be false")

    def test_getFish_1(self):
        a = np.array([8,5,-2,-1,-6])
        r = getFish(a)
        res = np.allclose(r, np.array([8]))
        self.assertEqual(res, True, "must be True")

    def test_getFish_2(self):
        a = np.array([8,8,-5,3,5])
        res = np.allclose(getFish(a), np.array([8,8,3,5]))
        self.assertEqual(res, True, "must be True")
    

if __name__ == "__main__":
    array = np.array([8,5,-2,-1,-6])
    getFish(array)

    unittest.main()