import unittest

def decima_to_binary(num):
    if num == 1:
        return 1
    
    rem = num % 2
    return str(decima_to_binary(num//2)) +  str(rem)

def decima_to_binary_stack(num):
    if num == 1:
        return [num]
    
    
    rem = num % 2
    result = (decima_to_binary_stack(num//2))
    result.append(rem)
    return result
    

class Test(unittest.TestCase):
    def test(self):
        num = 233
        expected = '11101001' 
        resut = decima_to_binary(num)
        self.assertEqual(expected,resut)

    def test_stack(self):
        num = 233
        expected = [1,1,1,0,1,0,0,1]
        resut = decima_to_binary_stack(num)
        self.assertEqual(expected,resut)
if __name__ == '__main__':
    unittest.main()
