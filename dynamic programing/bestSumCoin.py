# return the shortest combination of numbers that add up to exactly the target number
# 7, [5,3,4,7] -> [7]
#8, [2,3,5] -> [3,5]

import unittest

def coinChange (amount, coins, memo):
    result = cont(amount,coins, memo)
    return -1 if result is None else len(result)
    

def cont(k,array, memo):
    if k in memo:
        return memo[k]
    if k == 0: return []
    if k < 0 : return None

    shortestArray = None

    for coin in array:
        result = cont(k-coin, array,memo)
            
        if(result != None):
            combination = result + [coin]
            if shortestArray is None or len(combination) < len(shortestArray) :
                shortestArray = combination[:]
            

    memo[k] = shortestArray;
    return shortestArray

                


class Test(unittest.TestCase):

    def test1(self):
        array = [1,2,5]
        k = 11
        expected = 3
        result = coinChange(k, array,{})

        self.assertEqual(expected, result)


    def test2(self):
        array = [2]
        k = 3
        expected = -1
        result = coinChange(k, array,{})

        self.assertEqual(expected, result)

    def test3(self):
        array = [1,2,3]
        k = 5
        expected = 2
        result = coinChange(k, array,{})

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()