#given an array of items, select with item is the dominator.

#In order to say that there is a Leader it should be more than halfe of the array
#[eagle, wolf, wolf, deer, wolf, eagle, wolf]
#eagle -> 2
#wolf -> 4
#deer -> 1
# the wolf is the leader because 4 > 7/2


#there are multiple solution to this problem
#1.- It´s to  count the ocurrence of each element having a O(n*n) because you can end up looping the array as many elements in has in the array
#2.- We can sort the array and the most common element will be in the middle then we cound the number of times it occurs in the array
    #if we pick a good sorting alghorithm we end up with an algorithm equal to the sorting algorithm -> best case scenario O(n log n)


#my solution uses a dictionary with has a Time complexity of O(n) in the worst case

import numpy as np
import unittest

def solution(array):
    elements = {}
    for e in array:
        if e in elements:
            elements[e] = elements[e] + 1
        else :
            elements[e] = 1
    
    max_number = 0
    max_key = None
    for key in elements:
        if(max_key is None):
            max_key = key
            max_number = elements[key]
        else:
            if elements[key] > max_number:
                max_number = elements[key]
                max_key = key
    
    #we need to check if the elemente with max number of repetitions is the leader
    if max_number > (len(array)/2):
        return max_key
    else:
        return False



class TestDominator(unittest.TestCase):

    def test1(self):
        a = np.array([3,2,3,3,2,3,1])
        expected = 3
        res = solution(a)
        self.assertEqual(res, expected, "Should be 3")

    def test_False(self):
        a = np.array([3,2,3,3,2,3,1,4,4])
        expected = False
        res = solution(a)
        self.assertEqual(res, expected, "Should be False")

    def test2(self):
        a = np.array([3,2,3,3,2,3,1,5,5,5,5,5,5,5,5,5,5,5,5,5])
        expected = 5
        res = solution(a)
        self.assertEqual(res, expected, "Should be 5") 


if __name__ == "__main__":
    unittest.main()