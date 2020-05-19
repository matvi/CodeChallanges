import numpy as np
import unittest


#This coding challange tries to find the max sum that a sub array can have
#In other words try to find the consecutive indexes that will sum the max value in a given array
#for example given the next array -> [5,-4,8,-10,-2,4,-3,2,7,-8,3,-5,3]
#find the sub array that sumed the max number
#in this case will be index 5 -> 8 that is [4,-3,2,7] this sub array has the max value -> 10 than any other.

#one solution is to use brute force by forming subarrays 
#the best solution is using the kadanes alghorithm
#this algorithm will loop the array just once
#the idea is that if the array[i] > local_max + array[i] we start a new sub array
#and only when the local_max > global_max we know that there is a max value between those indexes.


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

def solution_kadanes_algh(array):
    global_max = 0
    local_max = 0
    initial_index = 0
    maxPoint = Point(0,0)
    for i in range(len(array)):
        if i == 0:
            global_max = array[i]
            local_max = array[i]
        else:


            local_max = local_max + array[i]

            if array[i] > local_max:
                initial_index = i
                local_max = array[i]
            #order on the if it is imortant due to the first one can update local_max

            if local_max > global_max:
                global_max = local_max
                maxPoint.x = initial_index
                maxPoint.y = i

            

    return maxPoint

def codility_kadanes(A):
    global_max_sum = 0
    local_max_sum = 0
    for i in range(1, len(A)):
        d = A[i] - A[i-1]
        local_max_sum = max(d, local_max_sum + d)
        global_max_sum = max(local_max_sum, global_max_sum)
    return global_max_sum

def comparePoints(point_a, point_b):
    if point_a.x == point_b.x and point_a.y == point_b.y:
        return True
    return False

class TestMaxProfit(unittest.TestCase):

    # def test1(self):
    #     a = np.array([5,-4,8,-10,-2,4,-3,2,7,-8,3,-5,3])
    #     expected = Point(5,8)
    #     res = solution_kadanes_algh(a)
    #     self.assertEqual(True, comparePoints(res,expected), "must be True")
    
    def test2(self):
        a = np.array([-4,1,-3,5,-8,1])
        expected = Point(2,2)
        res = solution_kadanes_algh(a)
        self.assertEqual(True, comparePoints(res,expected), "must be True")



if __name__ == "__main__":
    unittest.main()
    #a = np.array([5,-4,8,-10,-2,4,-3,2,7,-8,3,-5,3])
    #solution_kadanes_algh(a)
    #b = np.array([512,517,513,521,511,503,513,511,513,521,524,519])
    #print(codility_kadanes(b))




