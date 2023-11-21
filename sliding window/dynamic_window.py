#dynamic sliding window
#https://www.youtube.com/watch?v=GcW4mgmgSbw

import unittest
from typing import List

def dynamic_sliding_window(arr: List[int], x:int) -> int :
    suma = arr[0]
    i=0
    j=0
    min_arr_len = len(arr)

    while(j<len(arr)-1):
        j +=1
        suma += arr[j]
        if suma >= x:
            new_len = j -i +1
            if min_arr_len > new_len:
                min_arr_len = new_len

            while(suma >x):
                i=+1
                suma -= arr[i]
                new_len = j -i +1

                if min_arr_len > new_len:
                    min_arr_len = new_len
            
            i= j
            suma = arr[i]
    
    return min_arr_len


class Test(unittest.TestCase):

    def test(self):
        arr = [1,2,3,4,5,6]
        x=7
        expected_result = 2
        actual_result = dynamic_sliding_window(arr,x)

        self.assertEquals(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()

            
                    
                    
                

                