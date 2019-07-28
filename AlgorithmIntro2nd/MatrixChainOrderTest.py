from AlgorithmIntro2nd.DynamicProgramming import MaxtrixChainOrder
import unittest


class MatrixChainOrderTest(unittest.TestCase):
    def matrixChainOrder(self):
        matrixChainOrder = MaxtrixChainOrder()
        valRec = matrixChainOrder.matrixChainOrderRecursive(1, 6)
        val = matrixChainOrder.matrixChainOrder()
        self.assertTrue(val == valRec)
        matrixChainOrder.printOptimalParens(matrixChainOrder.s, 1, 6)
        matrixChainOrder.matrixChainMultiply(matrixChainOrder.s, 1, 6)
        self.assertTrue(15125 == matrixChainOrder.complexity)


if __name__ == '__main__':
    unittest.main()


testSuit = unittest.TestSuite()
testSuit.addTest(MatrixChainOrderTest("matrixChainOrder"))

testSuit.debug()