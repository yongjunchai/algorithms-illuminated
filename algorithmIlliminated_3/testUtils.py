import unittest
from utils.utils import *


class UtilsTestCase(unittest.TestCase):
    def test_multiDimensionArray(self):
        array = Utils.createArray([3, 4, 5])
        self.assertTrue(len(array) == 3)
        self.assertTrue(len(array[0]) == 4)
        self.assertTrue(len(array[0][0]) == 5)

    def test_valueUpate(self):
        array = Utils.createArray([2, 2, 2, 2, 2])
        Utils.updateValue(array, [1], 2)
        print(array)
        print(Utils.getValue(array, [1, 1, 1, 1, 1]))



if __name__ == '__main__':
    unittest.main()
