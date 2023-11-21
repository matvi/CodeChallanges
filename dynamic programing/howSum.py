import unittest

def howSum(k,array):
    if k<0 : return -1
    if k == 0 : return []

    for i in array:
        result = howSum(k-i,array)
        if(result != -1):
            result.append(i)
            return result
        
    return -1

def howSumMemo(k,array, memo):
    # Convert the input_array to a comma-separated string
    
    # Create the key in the desired format
    key = k
    if key in memo:
        return memo[k]
    
    if k<0 : return -1
    if k == 0 : return []

    for i in array:
        result = howSumMemo(k-i,array,memo)
        memo[key] = result
        if(result != -1):
            result.append(i)
            return result
        
    return -1

class Test(unittest.TestCase):
    
    def test1 (self):
        array= [5,3,4,7]
        k = 7
        expected = [3,4]
        result = howSum(k,array)

        self.assertEqual(set(result), set(expected))

    def test1 (self):
        array= [5,9]
        k = 7
        expected = -1
        result = howSum(k,array)

        self.assertEqual(result, expected)

    def testMemo (self):
        array= [5,3,4,7]
        k = 7
        expected = [3,4]
        result = howSumMemo(k,array,{})

        self.assertEqual(set(result), set(expected))

    def testMemoNegative1 (self):
        array= [7,14]
        k = 20
        expected = -1
        result = howSumMemo(k,array,{})

        self.assertEqual(result, expected)

    def testMemoOk1 (self):
        array= [7,4]
        k = 20
        expected = [4,4,4,4,4]
        result = howSumMemo(k,array,{})

        self.assertEqual(result, expected)

    def testMemoNegative2 (self):
        array= [5,9]
        k = 7
        expected = -1
        result = howSumMemo(k,array,{})

        self.assertEqual(result, expected)

    def testMemoNegative3Intensive(self):
        array= [7,14]
        k = 300
        expected = -1
        result = howSumMemo(k,array,{})

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
