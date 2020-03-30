import unittest
from algorithmIlliminated_1.quicksort import *
import random

class MyTestCase(unittest.TestCase):
    def test_quickSort(self):
        arr = []
        n = 1024
        for j in range(0, n):
            arr.append(j)
        for i in range(100):
            random.shuffle(arr)
            quickSort = Quicksort()
            quickSort.sort(arr, 0, n - 1)
            for j in range(0, n):
                self.assertTrue(arr[j] == j)



if __name__ == '__main__':
    unittest.main()
