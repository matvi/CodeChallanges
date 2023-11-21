# return the shortest combination of numbers that add up to exactly the target number
# 7, [5,3,4,7] -> [7]
#8, [2,3,5] -> [3,5]

import unittest

def bestSum (k, array): #k is target and array is the list numbers
    if k == 0: return []
    if k < 0 : return -1

    shortestArray = []

    for i in array:
        result = bestSum(k-i, array)

        if(result != -1):
            result.append(i)
            if len(shortestArray) > len(result) or shortestArray == [] :
                shortestArray.clear
                shortestArray = result.copy()
    
    if (shortestArray == []):
        return -1
    
    return shortestArray


class Test(unittest.TestCase):

    def test0(self):
        array = [1,2,5]
        k = 11
        expected = [5,5,1]
        result = bestSum(k, array)
        print(result)

        self.assertEqual(expected, result)

    # def test1(self):
    #     array = [3,6]
    #     k = 6
    #     expected = [6]
    #     result = bestSum(k, array)

    #     self.assertEqual(expected, result)


    # def test2(self):
    #     array = [5,3,4,7]
    #     k = 7
    #     expected = [7]
    #     result = bestSum(k, array)

    #     self.assertEqual(expected, result)

    # def test3(self):
    #     array = [2,3,5]
    #     k = 8
    #     expected = [5,3]
    #     result = bestSum(k, array)

    #     self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()