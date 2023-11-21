# Write a function:

# def solution(A, B, K)

# that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

# { i : A ≤ i ≤ B, i mod K = 0 }

# For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

# Write an efficient algorithm for the following assumptions:

# A and B are integers within the range [0..2,000,000,000];
# K is an integer within the range [1..2,000,000,000];
# A ≤ B.


import numpy as np
import unittest

def solution(a,b,k):
    i = range(a,b+1,k)
    return(len(i))

from math import ceil, floor
def codelity_solution(a,b,k):
    n_start = ceil(a/k)
    n_end = floor(b/k)
    return n_end - n_start + 1


class TestDivider(unittest.TestCase):
    def test1(self):
        a = 5
        b = 16
        k = 3
        res = solution(a,b,k)
        self.assertEqual(res, 4, "should be 4")

    def test2(self):
        a = 6
        b = 11
        k = 2
        res = solution(a,b,k)
        self.assertEqual(res, 3, "should be 3")

if __name__ == "__main__":
    unittest.main()