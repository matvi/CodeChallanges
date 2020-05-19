import numpy as np

arr = np.array([5,3,4,1,2])

def solution(a, k):
    if k == len(a):
        return a
    b = np.ones(len(a))
    
    for i in range(len(a)):
        index = (i + k) % len(a)
        #print("index {} ".format(index))
        b[index] = a[i]
    

    for i in range(len(a)):
        print("i + k {}".format(i+k))
        print("% {}".format((i+k)% len(a)))

    return "0"



print(solution(arr,2))
