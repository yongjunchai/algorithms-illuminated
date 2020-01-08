import unittest
import random
import math
from algorithmIlliminated_2.twoSum import *


class MyTestCase(unittest.TestCase):
    def test_2sum(self):
        numbers = [3, 4, 1, 6, 5]
        twoSum = TwoSum()
        target = 7
        twoSums = twoSum.find2Sum(numbers, target)
        print("target [%d] " % target)
        print(twoSums)

    def test_2sum_rnd_bigRng(self):
        numbers = []
        for i in range(1, 1000000):
            r = random.randint(-math.pow(10, 11), math.pow(10, 11))
            numbers.append(r)
        target = numbers[10]
        twoSum = TwoSum()
        twoSums = twoSum.find2Sum(numbers, target)
        print("target [%d] " % target)
        print(twoSums)


if __name__ == '__main__':
    unittest.main()
