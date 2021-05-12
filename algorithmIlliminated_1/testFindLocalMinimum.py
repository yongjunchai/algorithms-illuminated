import unittest
import random
from algorithmIlliminated_1.findLocalMinimum import *
from utils.utils import *


class MyTestCase(unittest.TestCase):
    def createOrderedData(self, rows: int, columns: int):
        assert(rows == columns)
        assert(rows >= 2)
        nums = Utils.createArray([rows, columns])
        for i in range(rows):
            for j in range(columns):
                nums[i][j] = i * columns + j
        return nums

    def createRandomData(self, rows: int, columns: int):
        nums = []
        for i in range(rows * columns):
            nums.append(i)
        random.shuffle(nums)
        rndNums = Utils.createArray([rows, columns])
        for i in range(rows):
            for j in range(columns):
                rndNums[i][j] = nums[i * columns + j]
        return rndNums

    def test_9_many_times_with_rnd(self):
        for j in range(3, 50):
            i = 9
            rndData = self.createRandomData(i, i)
            findLocalMinimum = FindLocalMinimum()
            row, col = findLocalMinimum.findLocalMinimum(rndData, i, i)
            isLocalMin = FindLocalMinimum.isLocalMinimum(rndData, i, i, 0, 0, row, col)
            self.assertTrue(isLocalMin)

    def test_increasing_rows(self):
        for i in range(3, 50):
            print(i)
            rndData = self.createRandomData(i, i)
            findLocalMinimum = FindLocalMinimum()
            row, col = findLocalMinimum.findLocalMinimum(rndData, i, i)
            isLocalMin = FindLocalMinimum.isLocalMinimum(rndData, i, i, 0, 0, row, col)
            self.assertTrue(isLocalMin)

    def test_increasing_rows_ordered(self):
        for i in range(3, 50):
            rndData = self.createOrderedData(i, i)
            findLocalMinimum = FindLocalMinimum()
            row, col = findLocalMinimum.findLocalMinimum(rndData, i, i)
            isLocalMin = FindLocalMinimum.isLocalMinimum(rndData, i, i, 0, 0, row, col)
            self.assertTrue(isLocalMin)


if __name__ == '__main__':
    unittest.main()
