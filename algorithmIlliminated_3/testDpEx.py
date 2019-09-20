import unittest
from algorithmIlliminated_3.dpEx import *


class DpExTestCase(unittest.TestCase):
    def test_solveDoubleKnapsack(self):
        items = [Item(1, 3, 4), Item(2, 2, 3), Item(3, 4, 2), Item(4, 4, 3)]
        c1 = 2
        c2 = 3
        dpEx = DpEx()
        dpEx.solveDoubleKnapsack(c1, c2, items)


if __name__ == '__main__':
    unittest.main()

