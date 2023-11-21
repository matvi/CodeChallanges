import numpy as np
import unittest

#complexity for O(n)
#complexity for A[i] in slice_queue is O(n)
#complexity for while is O(n)
#Result 70% in codility tests
# def solution(A):
#     slices_queue = []
#     count = 0
#     pointA = 0
#     for i in range(len(A)):
#         while A[i] in slices_queue:
#             slices_queue.pop(0) #remove item as a queue
#             pointA += 1
#         slices_queue.append(A[i])
#         count += (i+1-pointA)
#         if count > 1000000000: return count
#     return count


def better_solution(M,A):
    slices_queue = [None] * (M+1)
    count = 0
    tail = 0
    head=0

    while head < len(A):
        if slices_queue[A[head]] == 1:
            slices_queue[A[tail]] = 0
            tail +=1
        else:
            slices_queue[A[head]] = 1
            count += (head+1-tail)
            head += 1
            if count > 1000000000: return 1000000000
    
    return count




class TestSlice(unittest.TestCase):
    
    # def test1(self):
    #     a = np.array([2,7,4,6])
    #     expectd = 10
    #     res = solution(a)
    #     self.assertEqual(res,expectd,"Should be {}".format(expectd))

    # def test2(self):
    #     a = np.array([2,7,4,6,3])
    #     expectd = 15
    #     res = solution(a)
    #     self.assertEqual(res,expectd,"Should be {}".format(expectd))
    
    # def test3(self):
    #     a = np.array([2,4,1,7,4,9,7,3])
    #     expectd = 24
    #     res = solution(a)
    #     self.assertEqual(res,expectd,"Should be {}".format(expectd))

    def test1(self):
        a = np.array([2,4,1,7,4,8,7,3,2])
        M= 9
        expectd = 29
        res = better_solution(M,a)
        self.assertEqual(res,expectd,"Should be {}".format(expectd))

if __name__ == "__main__":
    print("test")
    unittest.main()
    print("test fnishing")