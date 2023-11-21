import unittest

def sum_num_nat(num):
    if num == 0 : return num 

    result = num + sum_num_nat(num -1)
    return result

class Test(unittest.TestCase):
    def test(self):
        num = 10
        expected = 55
        result = sum_num_nat(num)
        self.assertEquals(expected, result)

if __name__ == '__main__':
    unittest.main()