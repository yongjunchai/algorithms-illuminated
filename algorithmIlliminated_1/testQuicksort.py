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

    def test_quickSort_duplicate_values(self):
        arr = []
        n = 20
        for i in range(0, n):
            arr.append(random.randint(0, n / 2))
        quickSort = Quicksort()
        for k in range(0, 10):
            print("loop [{}]".format(k))
            random.shuffle(arr)
            print(arr)
            quickSort.sort(arr, 0, n - 1)
            for i in range(0, n - 1):
                self.assertTrue(arr[i] <= arr[i + 1])
            print(arr)

if __name__ == '__main__':
    unittest.main()
