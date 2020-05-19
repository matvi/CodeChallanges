import numpy as np
import unittest


#this solution will take each row and convert it to a column
def solution(matrix):
    m = np.copy(matrix)
    n = matrix.shape[1]
    for i in range(matrix.shape[0]):
        n = n - 1
        for j in range(matrix.shape[1]):
            matrix[j,n] = m[i,j]
    return matrix

#this solution first transport the matrix and then flips it
#this solution is better because we don´t need to create extra space in memory to save a new image.
def solution_transport(matrix):
    #matrix = matrix.transpose()
    #return np.flip(matrix, axis=1)
    matrix = transponse(matrix)
    return flip(matrix)

#this is just the algorith for transpose
def transponse(m):
    for i in range(m.shape[0]):
        for j in range(i+1,m.shape[0]):
            tmp = m[i,j]
            m[i,j] = m[j,i]
            m[j,i] = tmp
    return m

def flip(m):
    mid = int(m.shape[0] / 2)
    for i in range(m.shape[0]):
        for j in range(mid):
            n = m.shape[0] - j -1 
            tmp = m[i,j]
            m[i,j] = m[i,n]
            m[i,n] = tmp
    return m


class TestRotation90(unittest.TestCase):
    
    def test1(self):
        a = np.array([[1,2,3],[4,5,6],[7,8,9]])
        m = solution(a)
        res = np.allclose(m, np.array([[7,4,1],[8,5,2],[9,6,3]]) )
        self.assertEqual(res, True, "Must be true")

    def test2(self):
        a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
        m = solution(a)
        res = np.allclose(m, np.array([[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]]) )
        self.assertEqual(res, True, "Must be true")

    #testing solution 2

    def test3(self):
        a = np.array([[1,2,3],[4,5,6],[7,8,9]])
        m = solution_transport(a)
        res = np.allclose(m, np.array([[7,4,1],[8,5,2],[9,6,3]]) )
        self.assertEqual(res, True, "Must be true")

    def test4(self):
        a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
        m = solution_transport(a)
        res = np.allclose(m, np.array([[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]]) )
        self.assertEqual(res, True, "Must be true")


    #test transponse
    def test_transponse(self):
        a =np.array([[1,2,3],[4,5,6],[7,8,9]])
        res = np.allclose(transponse(a), np.array([[1,4,7],[2,5,8],[3,6,9]]))
        self.assertEqual(res, True, "must be true")

    #test flip
    def test_flip3x3(self):
        a =np.array([[1,2,3],[4,5,6],[7,8,9]])
        res = np.allclose(flip(a), np.array([[3,2,1],[6,5,4],[9,8,7]]))
        self.assertEqual(res, True, "must be true")

    def test_flip4x4(self):
        a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
        m = flip(a)
        res = np.allclose(m, np.array([[4,3,2,1],[8,7,6,5],[12,11,10,9],[16,15,14,13]]) )
        self.assertEqual(res, True, "Must be true")

if __name__ == "__main__":
    unittest.main()

