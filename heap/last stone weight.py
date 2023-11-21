#last stone weight

#the time complexity is nLogn because the pop and push operation on heap is LogN
#as we are going to do this 3 times for n times
#this will be equal to 3n * LogN = 3nLogN => nLogN

import heapq
import unittest

def last_stone_weight(array):
    negative_array = [-x for x in array]
    heapq.heapify(negative_array)
    while(len(negative_array)>1):
        first_element = heapq.heappop(negative_array)
        second_element = heapq.heappop(negative_array)
        if first_element != second_element:
            new_element = first_element - second_element
            heapq.heappush(negative_array, new_element) 
    
    if len(negative_array) == 0:
        return 0
    else:
        return -negative_array[0]
    
class Test(unittest.TestCase):

    def test1(self):
        array = [2,7,4,1,8,1]
        expected = 1
        result = last_stone_weight(array)

        self.assertEquals(expected, result)

    def test2(self):
        array = [2,7,4,10]
        expected = 1
        result = last_stone_weight(array)

        self.assertEquals(expected, result)

if __name__ == '__main__':
    unittest.main()
    
