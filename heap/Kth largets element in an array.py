#Kth largets element in an array

import unittest

def k_largest_element_array(array, k):
    #find max number
    max_number = max(array) + 1
    new_array = [0] * max_number

    for i in array:
        new_array[i] +=1

    #find k largest element
    total = 0
    for i in range(0,len(new_array)):
        total += new_array[i]
        if(total >= k):
            return i


class Test(unittest.TestCase):

    def test1(self):
        array = [0,1,2,3,4,5]
        k = 3
        expected = 2
        result = k_largest_element_array(array, k)

        self.assertEquals(expected, result)

    def test2(self):
        array = [0,1,2,3,4,5]
        k = 6
        expected = 5
        result = k_largest_element_array(array, k)

        self.assertEquals(expected, result)

    def test3(self):
        array = [5,1,4,3,2,0]
        k = 6
        expected = 5
        result = k_largest_element_array(array, k)

        self.assertEquals(expected, result)

    def test4(self):
        array = [10,15,16,20,31]
        k = 5
        expected = 31
        result = k_largest_element_array(array, k)

        self.assertEquals(expected, result)

if __name__ == '__main__':
    unittest.main()