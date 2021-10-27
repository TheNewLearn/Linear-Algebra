import unittest
from matrixcal import MatrixCalculator as mc

class TestMatrixCala(unittest.TestCase):
    def test_plus(self):

        matrix1 = [[1,2],[3,4]]
        matrix2 = [[5,6],[7,8]]
        self.assertEqual(mc.plus(matrix1,matrix2),[[6,8],[10,12]])

    def test_minus(self):
        matrix1 = [[1,2],[3,4]]
        matrix2 = [[5,6],[7,8]]
        self.assertEqual(mc.minus(matrix1,matrix2),[[-4,-4],[-4,-4]])

    def test_matrixtran(self):
        matrix = [[2,3,4],[5,6,7]]
        self.assertEqual(mc.matrixtran(matrix),[[2,5],[3,6],[4,7]])

    def test_multiplymatrix(self):
        matrix1 = [[1,2],[3,4]]
        matrix2 = [[2,3,4],[5,6,7]]
        self.assertEqual(mc.matrixmultiply(matrix1,matrix2),[[12,15,18],[26,33,40]])
    def test_multiply(self):
        matrix = [[1,2],[3,4]]
        num = 3
        self.assertEqual(mc.multiply(3,matrix),[[3,6],[9,12]])

    def test_dev(self):
        matrix = [[2,-1],[3,5]]
        self.assertEqual(mc.dev(matrix),13)

    def test_inv(self):
        a = [[2,-1],[3,5]]
        self.assertEqual(mc.inv(a),[[0.386,0.0769],[-0.20308,0.1538]])

    
if __name__ == '__main__':
    unittest.main()