import unittest
from algorithmIlliminated_1.unimodalMax import *


class MyTestCase(unittest.TestCase):
    def createUnimodalArray(self, cnt: int):
        assert(cnt >= 1)
        if cnt == 1:
            return (1, [1])
        mid = int(cnt / 2)
        nums = []
        maxNum = mid - 1
        for i in range(0, mid):
            nums.append(i)
        for i in range(mid, cnt):
            nums.append(maxNum - i)
        return (maxNum, nums)


    def test_unimodal(self):
        for i in range(1, 1024):
            maxNum, nums = self.createUnimodalArray(i)
            unimodalMax = UnimodalMax()
            found = unimodalMax.findMax(nums)
            self.assertTrue(found == maxNum)

if __name__ == '__main__':
    unittest.main()
