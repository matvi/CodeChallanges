#This code challange:
#Equilibrium
#A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

# Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].
# 
# The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|
# 
# In other words, it is the absolute difference between the sum of the first part and the sum of the second part.
# 
# For example, consider array A such that:
# 
#   A[0] = 3
#   A[1] = 1
#   A[2] = 2
#   A[3] = 4
#   A[4] = 3
# We can split this tape in four places:
# 
# P = 1, difference = |3 − 10| = 7
# P = 2, difference = |4 − 9| = 5
# P = 3, difference = |6 − 7| = 1
# P = 4, difference = |10 − 3| = 7
# Write a function:
# 
# def solution(A)
# 
# that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.
# 
# For example, given:
# 
#   A[0] = 3
#   A[1] = 1
#   A[2] = 2
#   A[3] = 4
#   A[4] = 3
# the function should return 1, as explained above.
# 
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [2..100,000];
# each element of array A is an integer within the range [−1,000..1,000].


#simplest solution
import numpy as np

#arr = np.array([3,1,2,4,3])
arr = np.array([13,1,2,4,3])
res = 1000


def getMinAbs(a,res):
    for i in range(1,len(a)):
        x = sumArr(a[0:i])
        y = sumArr(a[i:])
        tmp = abs(x-y)
        #print("x: {}, ... y: {}, ... tmp{}".format(x,y,tmp))
        if( tmp < res ):
            res = tmp
    return res
        

def sumArr(a):
    return a.sum()


print(getMinAbs(arr, res))

#this algorith will take the first element and the last element and will compare them
#then it will move the pivote where the value is less

def Equilibrium(arr):
    sum_left = 0
    j = len(arr) - 1 #we get the las position
    sum_right = arr[j]
    j = j-1
    for i in range(0, j):
        if(i-1==j):
            break;
        sum_left +=  arr[i]
        while(sum_left>sum_right and i<j):
            sum_right += + arr[j]
            j = j-1
    return abs(sum_left-sum_right)

print(Equilibrium(arr))


#this algorithm will take the first value and then 
def solution(A):
    sum_left = A[0]
    sum_right = A.sum() - A[0]
    diff = abs(sum_left - sum_right)
    for i in range(1, len(A)-1):
        sum_left += A[i]
        sum_right -= A[i]
        currend_dif = abs(sum_left - sum_right)
        if diff > currend_dif:
            diff = currend_dif
    return diff

print(solution(arr))

