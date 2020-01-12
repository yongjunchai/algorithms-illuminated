import unittest
import random
from algorithmIlliminated_1.mergeSort import *


class MyTestCase(unittest.TestCase):
    def test_mergeSort(self):
        for loop in range(1, 100):
            rndNums = []
            cnt = 1024
            for i in range(cnt):
                rndNums.append(i)
            random.shuffle(rndNums)
            mergeSort = MergeSort()
            s = mergeSort.mergeSort(rndNums)
            for i in range(cnt):
                self.assertTrue(i == s[i])

    def test_mergeSort_withDups(self):
        for loop in range(1, 100):
            rndNums = []
            cnt = 1024
            for i in range(cnt):
                rndNums.append(random.randint(0, 500))
            random.shuffle(rndNums)
            mergeSort = MergeSort()
            s = mergeSort.mergeSort(rndNums)
            minVal = s[0]
            for i in range(cnt):
                self.assertTrue(minVal <= s[i])
                minVal = s[i]

if __name__ == '__main__':
    unittest.main()
