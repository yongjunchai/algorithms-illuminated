import unittest
from .DynamicProgramming import RodCutting


class TestCutRod(unittest.TestCase):
    def cutRodTest(self):
        rodCutting = RodCutting()
        val = rodCutting.cutRod(3)
        self.assertTrue(val == 8)

        val = rodCutting.cutRod(4)
        self.assertTrue(val == 10)

        val = rodCutting.cutRod(5)
        self.assertTrue(val == 13)

        val = rodCutting.cutRod(7)
        self.assertTrue(val == 18)

        val = rodCutting.cutRod(10)
        self.assertTrue(val == 30)

    def memoizedCutRodTest(self):
        rodCutting = RodCutting()
        val = rodCutting.memoizedCutRod(3)
        self.assertTrue(val == 8)

        val = rodCutting.memoizedCutRod(4)
        self.assertTrue(val == 10)

        val = rodCutting.memoizedCutRod(5)
        self.assertTrue(val == 13)

        val = rodCutting.memoizedCutRod(7)
        self.assertTrue(val == 18)

        val = rodCutting.memoizedCutRod(10)
        self.assertTrue(val == 30)

    def bottomUpCutRodTest(self):
        rodCutting = RodCutting()
        val = rodCutting.bottomUpCutRod(3)
        self.assertTrue(val == 8)

        val = rodCutting.bottomUpCutRod(4)
        self.assertTrue(val == 10)

        val = rodCutting.bottomUpCutRod(5)
        self.assertTrue(val == 13)

        val = rodCutting.bottomUpCutRod(7)
        self.assertTrue(val == 18)

        val = rodCutting.bottomUpCutRod(10)
        self.assertTrue(val == 30)


    def extendedBottomUpCutRodTest(self):
        rodCutting = RodCutting()
        val = rodCutting.extendedBottomUpCutRod(3)
        self.assertTrue(val == 8)

        val = rodCutting.extendedBottomUpCutRod(4)
        self.assertTrue(val == 10)

        val = rodCutting.extendedBottomUpCutRod(5)
        self.assertTrue(val == 13)

        val = rodCutting.extendedBottomUpCutRod(7)
        self.assertTrue(val == 18)

        val = rodCutting.extendedBottomUpCutRod(10)
        self.assertTrue(val == 30)

    def printCutSolutionTest(self):
        rodCutting = RodCutting()
        # rodCutting.printCutSolution(7)

        rodCutting.printCutSolution(10)

    def extendedMemoizedCutRodPrintTest(self):
        rodCutting = RodCutting()
        rodCutting.extendedMemoizedCutRod(8)


if __name__ == '__main__':
    unittest.main()

testSuit = unittest.TestSuite()
testSuit.addTest(TestCutRod("cutRodTest"))
testSuit.addTest(TestCutRod("memoizedCutRodTest"))
testSuit.addTest(TestCutRod("extendedBottomUpCutRodTest"))
testSuit.addTest(TestCutRod("printCutSolutionTest"))
testSuit.addTest(TestCutRod("extendedMemoizedCutRodPrintTest"))

testSuit.debug()