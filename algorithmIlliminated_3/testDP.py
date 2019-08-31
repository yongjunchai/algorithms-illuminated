import unittest
from algorithmIlliminated_3.dp import *

class TestDP(unittest.TestCase):
    def test_wis_divide_and_conquer(self):
        dp = DP()
        testData = [([1, 4, 5, 4], [4, 4]),
                    ([8, 10, 11, 9, 8], [8, 11, 8]),
                    ([8, 10, 16, 9, 8, 1999, 19, 10], [8, 16, 1999, 10])
                    ]
        for item in testData:
            values = item[0]
            wisNodes = dp.wis_divide_and_conquer(values)
            wisNodes = sorted(wisNodes, key=lambda x: x.index)
            exp = item[1]
            self.assertTrue(len(exp) == len(wisNodes))
            for i in range(0, len(exp)):
                self.assertTrue(exp[i] == wisNodes[i].value)


if __name__ == '__main__':
    unittest.main()
