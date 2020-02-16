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

    def test_something(self):
        for i in range(3, 1000):
            #i = 9
            print(i)
            timerData = Timer()
            timerData.start()
            #orderedData = self.createOrderedData(i, i)
            # Utils.dumpMatrix(orderedData, i, i)
            timerData.stop()
            #print("creation data time %d ms" % timerData.timeElapsedMs())
            rndData = self.createRandomData(i, i)
            timer = Timer()
            timer.start()
            findLocalMinimum = FindLocalMinimum()
            #row, col = findLocalMinimum.findLocalMinimum(orderedData, i, i)
            #self.assertTrue(FindLocalMinimum.isLocalMinimum(orderedData, i, i, 0, 0, row, col))
            timer.stop()
            #print("time elapsed %d ms" % timer.timeElapsedMs())
            #Utils.dumpMatrix(rndData, i, i)
            row, col = findLocalMinimum.findLocalMinimum(rndData, i, i)
            isLocalMin = FindLocalMinimum.isLocalMinimum(rndData, i, i, 0, 0, row, col)
            #if not isLocalMin:
            #    print("fail")
            if not isLocalMin:
                print("(%d, %d)" % (row, col))
                row, col = findLocalMinimum.findLocalMinimum(rndData, i, i)
                isLocalMin = FindLocalMinimum.isLocalMinimum(rndData, i, i, 0, 0, row, col)

            self.assertTrue(isLocalMin)

if __name__ == '__main__':
    unittest.main()
