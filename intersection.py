import numpy as np
import unittest



def solution(array):
    tuple_list = []
    #first create a list of tuples, each tuple represents the begin and the end of the new array
    for i in range(len(array)):
        figure = (i-array[i], i+array[i])
        tuple_list.append(figure)
    #order the tuple (#depending on the algorithm this sorting can have a O(nlogn)) time complexity
    tuple_list.sort()
    intersections = 0

    #this algorithm to find th eintersections will have an O(n log n) time complexity
    for i in range(len(tuple_list)-1):
        for j in range(i+1,len(tuple_list)):
            intersections += checkIntersection(tuple_list[i], tuple_list[j])
    return intersections

    #this algorithm to find the intersections will have an O(nlogn) Time complexity (it is a binary search)


#check intersection between tuple1 and t2
def checkIntersection(t, t2):
    if ( t2[0] >= t[0] and t2[0] <= t[1] ):
        return 1
    return 0
    
class TestIntersections(unittest.TestCase):

    def Test1(self):
        a = np.array([1,5,2,1,4,0])
        res = solution(a)
        self.assertEqual(res,11,"must be 11")

if __name__ == "__main__":
    unittest.main()
    #a = np.array([1,5,2,1,4,0])
    #res = solution(a)
    #print(res)
    