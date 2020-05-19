import numpy as np
import unittest

#problem
#you are going to receive a sorted algorithm
#you need to square the algorith and you need to return a sorted algorithm
#example input [-5,3,9]
#output [9,25,81]


#this solution has a O(NlogN) because it has to sort the array
def solution(array):
    array = abs(array)
    array = array * array
    array.sort()
    return array

#best solution
#this solution do not uses any sort algorith
#instead it uses the logic that the array is already sorted
#and only iterates over the array once
def  best_solution(array):
    new_arr = np.zeros(len(array))
    #index = len(array) -1
    piv_right = 0
    piv_lefth = len(array) - 1
    #this will give index the value of size of array -1 to 0
    #ex. array_size =[-4,1,2,3] -> index = [3,2,1,0]
    for index in range(len(array) -1, -1, -1): 
        if (abs(array[piv_right]) > abs(array[piv_lefth])):
            new_arr[index] = array[piv_right] * array[piv_right]
            piv_right += 1
        else:
            new_arr[index] = array[piv_lefth] * array[piv_lefth]
            piv_lefth -= 1
        #index -= 1
    return new_arr

#Note for Python 3 users: There are no separate range and xrange functions in Python 3, there is just range, which follows the design of Python 2's xrange




class TestSortedSquaredSorted(unittest.TestCase):

    def test1(self):
        a = np.array([-4,1,2,3])
        expected = np.array([1,4,9,16])
        res = best_solution(a)
        test = np.allclose(res, expected)
        self.assertEqual(test, True, "Should be true")

    def test2(self):
        a = np.array([-5,-4,1,2,3])
        expected = np.array([1,4,9,16,25])
        res = best_solution(a)
        test = np.allclose(res, expected)
        self.assertEqual(test, True, "Should be true")

    def test3(self):
        a = np.array([-5,-4,1,2,3,6])
        expected = np.array([1,4,9,16,25,36])
        res = best_solution(a)
        test = np.allclose(res, expected)
        self.assertEqual(test, True, "Should be true")

    def test_unsortedArray(self):
        a = np.array([-5,-4,1,8,2,3,6])
        expected = np.array([1,4,9,16,25,36,64])
        res = best_solution(a)
        test = np.allclose(res, expected)
        self.assertEqual(test, False, "Should be false")

    

if __name__ == "__main__":
    unittest.main()
    # a = np.array([-4,1,2,3])
    # res = best_solution(a)
    # print(res)