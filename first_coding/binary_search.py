# O(log n): is the case when a set of data is repeatedly divided into half and the middle element is processed. For example: binary search algorithm.
# Explanation: I am using binary search to explain O(log n) scenario.
# List of items is sorted. All we do is:
# Recursively divide the list into three parts: Left sublist, Middle element and right sublist
# Check for the element by matching with the middle element.
# So, in this case repeatedly dividing the set of elements brings the O(log n).


import numpy as np
import unittest


def binary_search(array, num, indexes):  
    if len(array) == 1 and array[0] != num:
        return -1 
    index = int(len(array) / 2)
    if(array[index] == num):
        return indexes[index]
    if array[index] > num:
        array = array[0:index]
        indexes = indexes[0:index]
    else :
        array = array[index:]
        indexes = indexes[index:]
    return binary_search(array,num, indexes)



class TestBinarySearch(unittest.TestCase):

    def test_findNumber(self):
        a = np.array([3,11,21,29,41,54,61,78,110,127])
        indexes = np.arange(0, len(a))
        res = binary_search(a, 3, indexes)
        self.assertEqual(res,0, "should be in position 0")

    def test_findNumber2(self):
        a = np.array([3,11,21,29,41,54,61,78,110,127])
        indexes = np.arange(0, len(a))
        res = binary_search(a, 127,indexes)
        self.assertEqual(res,9, "should be in position 9")

    def test_notFindNumber(self):
        a = np.array([3,11,21,29,41,54,61,78,110,127])
        indexes = np.arange(0, len(a))
        res = binary_search(a, 13, indexes)
        self.assertEqual(res,-1, "should be in position -1")



if __name__ == "__main__":
    unittest.main()
    a = np.array([3,11,21,29,41,54,61,78,110,127])
    indexes = np.arange(0, len(a))
    res = binary_search(a, 3, indexes)
    print(res)