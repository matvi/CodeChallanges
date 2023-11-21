import unittest

def soluction(array):
    if(len(array) == 0):
        return 0
    if(len(array) == 1):
        return 1
    l=0
    r=1
    sub_array = set()
    max_lenght = 0
    sub_array.add(array[l])

    while(r<len(array)):
        if(array[r] in sub_array):
            l =l+1
            r = l+1
            max_lenght = max(max_lenght, len(sub_array))
            sub_array = set()
            sub_array.add(array[l])
        else :
            sub_array.add(array[r])
            max_lenght = max(max_lenght, len(sub_array))
            r = r+1
    
    return max_lenght

class Test(unittest.TestCase):



    def test2(self):
        array = ['d','v','d','f']
        expected = 3
        result = soluction(array)
        self.assertEquals(expected, result)




if __name__ == '__main__':
    unittest.main()