#sliding window

#problem: find the total sum of K subarray in original array
#this problem has On time complexity because we are passing through the array once

#https://www.youtube.com/watch?v=GcW4mgmgSbw

import unittest
from typing import List

def fixed_sliding_window(arr: List[int], k:int) -> List[int]:
    current_subarray = sum(arr[:k])
    total = current_subarray

    for i in range(0,len(arr)-k):
        current_subarray += arr[k +i] - arr[i]
        total += current_subarray

    return total

class Test(unittest.TestCase):

    def test1(self):
        array = [1,2,3,4,5,6]
        k =3
        expected_result = 42
        result = fixed_sliding_window(array, k)

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
        unittest.main()