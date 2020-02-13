import unittest
from algorithmIlliminated_1.findNum import *


class MyTestCase(unittest.TestCase):
    def createData_1(self):
        return True, [-100, -1, 2, 10, 11, 12, 13]

    def createData_2(self):
        return True, [-100, -9, -6, -2, 3, 5, 100]

    def createData_3(self):
        return False, [-100, -9, -6, -2, 3, 90, 100]

    def createData_padding(self):
        status, nums = self.createData_1()
        start = nums[len(nums) - 1]
        for i in range(1, 1024):
            nums.append(start + i * 2)
        return status, nums

    def createData_padding_false(self):
        status, nums = self.createData_1()
        start = nums[len(nums) - 1]
        for i in range(1, 1024):
            nums.append(start + i * 2)
        nums[2] = 3
        return False, nums

    def test_findNum(self):
        dataSet = [self.createData_1(), self.createData_2(), self.createData_3(), self.createData_padding(), self.createData_padding_false()]

        for data in dataSet:
            status = data[0]
            nums = data[1]
            findNum = FindNum()
            result = findNum.findNum(nums)
            self.assertTrue(result == status)


if __name__ == '__main__':
    unittest.main()
