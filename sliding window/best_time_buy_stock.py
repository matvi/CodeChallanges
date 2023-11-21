import unittest

def best_time_stock(array):
    l=0
    r=1
    max_amount = 0

    while(r< len(array)):
        if(array[l] > array[r]):
            l =r
            r = l + 1
        else :
            amount = array[r] - array[l]
            max_amount = max(amount, max_amount)
            r = r+1
    
    return max_amount

class Test(unittest.TestCase):
    def test1(self):
        array = [7,1,5,3,6,4]
        expected = 5
        result = best_time_stock(array)
        self.assertEquals(expected, result)
    
if __name__ == '__main__':
    unittest.main()