import numpy as np
import timeit 
import unittest


a = np.zeros(5)
a = a.astype("int")
b = np.array([3,4,4,6,1,4,4])

def MaxCounter(a,b) :
    max = len(a)
    for i in range(len(b)):
        if b[i] > max:
            IgualarAllCounters(a)
        else :
            a[b[i]-1] = a[b[i]-1]+ 1
    return a

def IgualarAllCounters(a):
    max_v = a.max()
    for i in range(len(a)):
        a[i] = max_v
    return a

#print(MaxCounter(a,b))
#print("*********")




#better solution start line

import numpy as np

a = np.zeros(5)
a = a.astype("int")
b = np.array([3,4,4,6,1,4,4])


def MaxCounter2(a,b) :
    start_line = 0
    max = len(a)
    for i in range(len(b)):
        if b[i] > max:
            start_line = a.max() # the problem is here because we need to iterate over the aaray to get the max value
        else :
            if start_line > a[b[i]-1]:
                a[b[i]-1] =  start_line + 1
            else :
                a[b[i]-1] =  a[b[i]-1]+ 1

    for i in range(len(a)):
        if start_line > a[i] :
            a[i] = start_line       
        #print(a)
    return a


#print(MaxCounter2(a,b))


#better solution2 start line
#keep track of the max current value to avoid the a.max problem

import numpy as np

def MaxCounter3(a,b) :
    start_line = 0
    max = len(a)
    max_current_value = 0
    for i in range(len(b)):

        if b[i] > max:
            #start_line = a.max() # the problem is here because we need to iterate over the aaray to get the max value
            start_line = max_current_value
        else :
            if start_line > a[b[i]-1]:
                a[b[i]-1] =  start_line + 1
            else :
                a[b[i]-1] =  a[b[i]-1]+ 1
            
            if a[b[i]-1] > max_current_value:
                max_current_value = a[b[i]-1]

    

    for i in range(len(a)):
        if start_line > a[i] :
            a[i] = start_line       
        #print(a)
    return a



#****delete this


#better solution start line

import numpy as np






#***to this




class TestMaxCounter(unittest.TestCase):
    
    def test1(self):
        a = np.zeros(5)
        a = a.astype("int")
        b = np.array([3,4,4,6,1,4,4])
        res = np.allclose(MaxCounter3(a,b),np.array([3,2,2,4,2]))
        self.assertEqual(res, True, "Should be true")
    
    def test2(self):
        a = np.zeros(5)
        a = a.astype("int")
        b = np.array([6,7,7,7,7,7,7])
        res = np.allclose(MaxCounter3(a,b),np.array([0,0,0,0,0]))
        self.assertEqual(res, True, "Should be true")

    def test3(self):
        a = np.zeros(6)
        a = a.astype("int")
        b = np.array([1,7])
        res = np.allclose(MaxCounter3(a,b),np.array([1,1,1,1,1,1]))
        self.assertEqual(res, True, "Should be true")

    def test4(self):
        a = np.zeros(6)
        a = a.astype("int")
        b = np.array([1,1,1,1,1])
        res = np.allclose(MaxCounter3(a,b),np.array([5,0,0,0,0,0]))
        self.assertEqual(res, True, "Should be true")
        
    def test5(self):
        a = np.zeros(6)
        a = a.astype("int")
        b = np.array([5,5,5,5,5,7])
        res = np.allclose(MaxCounter3(a,b),np.array([5,5,5,5,5,5]))
        self.assertEqual(res, True, "Should be true")

    def test6(self):
        a = np.zeros(6)
        a = a.astype("int")
        b = np.array([5,5,5,5,5,7,6])
        res = np.allclose(MaxCounter3(a,b),np.array([5,5,5,5,5,6]))
        self.assertEqual(res, True, "Should be true")

    def test7(self):
        a = np.zeros(100000)
        a = a.astype("int")
        b = np.array([5,5,5,5,5,5,100001])
        c = np.ones(100000) * 6
        res = np.allclose(MaxCounter3(a,b),c)
        self.assertEqual(res, True, "Should be true")

    def testMAx(self):
        a = np.ones(100000) * 5
        a = a.astype("int")
        a[100] = 100
        res = GetMax(a)
        self.assertEqual(res, 100, "Should be 100")

        
def my_function():
    y = 3.1415
    for x in range(100):
        y = y ** 0.7
    return y

if __name__ == "__main__":
    print("maintest")

    #unittest.main()
    #a = np.zeros(100000)
    #a = a.astype("int")
    #b = np.array([5,5,5,5,5,5,100001])
    #MaxCounter3(a,b)
    print(timeit.timeit(MaxCounter4, number = 10)) 
    print(timeit.timeit(MaxCounter5, number = 10)) 
    print(timeit.timeit(MaxCounter6, number = 10)) 


















