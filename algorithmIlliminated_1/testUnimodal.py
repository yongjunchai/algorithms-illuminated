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

    def createUnimodalArray_leftPadding(self, cnt: int):
        maxNum, nums = self.createUnimodalArray(cnt)
        numsLeftPadding = []
        startVal = nums[0]
        for i in range(1024, 0, -1):
            numsLeftPadding.append(startVal - i)
        numsLeftPadding.extend(nums)
        return (maxNum, numsLeftPadding)

    def createUnimodalArray_rightPadding(self, cnt: int):
        maxNum, nums = self.createUnimodalArray(cnt)
        numsRightPadding = []

        startVal = nums[len(nums) - 1]
        for i in range(1, 1024):
            numsRightPadding.append(startVal - i)
        nums.extend(numsRightPadding)
        return (maxNum, nums)

    def test_unimodal(self):
        for i in range(1, 1024):
            maxNum, nums = self.createUnimodalArray(i)
            unimodalMax = UnimodalMax()
            found = unimodalMax.findMax(nums)
            self.assertTrue(found == maxNum)

    def test_unimodal_left_padding(self):
        for i in range(1, 1024):
            maxNum, nums = self.createUnimodalArray_leftPadding(i)
            unimodalMax = UnimodalMax()
            found = unimodalMax.findMax(nums)
            self.assertTrue(found == maxNum)

    def test_unimodal_right_padding(self):
        for i in range(1, 1024):
            maxNum, nums = self.createUnimodalArray_rightPadding(i)
            unimodalMax = UnimodalMax()
            found = unimodalMax.findMax(nums)
            self.assertTrue(found == maxNum)


if __name__ == '__main__':
    unittest.main()
