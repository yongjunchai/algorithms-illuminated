import unittest
from algorithmIlliminated_1.countInv import *


class MyTestCase(unittest.TestCase):
    def test_inv(self):
        dataSet = [([1, 3, 5, 2, 4, 6], 3),
                   ([1, 5, 3, 2, 4, 6], 4),
                   ([5, 3, 1, 2, 4, 6], 6),
                   ([5, 3, 1, 6, 4, 2], 9)]
        for data in dataSet:
            nums = data[0]
            expectedInv = data[1]
            countInv = CountInv()
            inv = countInv.countInv(nums)
            self.assertTrue(inv == expectedInv)


if __name__ == '__main__':
    unittest.main()
