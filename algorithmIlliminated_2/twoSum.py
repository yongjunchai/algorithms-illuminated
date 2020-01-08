
import random


class TwoSum:
    def __init__(self):
        pass

    def find2Sum(self, numbers: list, target):
        nums = dict()
        for i in numbers:
            nums[i] = True
        twoSums = list()
        for i in numbers:
            v = nums.get(target - i)
            if v is not None:
                twoSums.append((i, target - i))
                nums.pop(i)
        return twoSums