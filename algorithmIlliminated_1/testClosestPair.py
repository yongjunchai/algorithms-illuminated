import unittest
from algorithmIlliminated_1.closestPair import *


class MyTestCase(unittest.TestCase):
    def loadData1(self):
        dataList = [(-3, 2), (-1, 4), (1, 1), (2, -3), (3, 6), (3, 2), (3, -4), (5, 4), (5, -1)]
        p = []
        for data in dataList:
            point = Point(data[0], data[1])
            p.append(point)
        p1 = Point(2, -3)
        p2 = Point(3, -4)
        return (p, (p1, p2))

    def loadData2(self):
        dataList = [(-3, 2), (-1, 4), (1, 1), (3, 6), (3, 2), (3, -4), (5, 4), (5, -1)]
        p = []
        for data in dataList:
            point = Point(data[0], data[1])
            p.append(point)
        p1 = Point(1, 1)
        p2 = Point(3, 2)
        return (p, (p1, p2))

    def loadData3(self):
        dataList = [(-3, 2), (-1, 4), (1, 1), (3, 6), (5.2, 4.2), (3, 2), (3, -4), (5, 4), (5, -1)]
        p = []
        for data in dataList:
            point = Point(data[0], data[1])
            p.append(point)
        p1 = Point(5, 4)
        p2 = Point(5.2, 4.2)
        return (p, (p1, p2))

    def test_findClosestPair(self):
        dataSet = [self.loadData1(), self.loadData2(), self.loadData3()]
        for data in dataSet:
            points = data[0]
            pair = data[1]
            closestPair = ClosestPair()
            p1, p2 = closestPair.closestPair(points)
            len1 = closestPair.calcDistance(p1, p2)
            minLen = closestPair.calcDistance(pair[0], pair[1])
            self.assertTrue(len1 == minLen)


if __name__ == '__main__':
    unittest.main()
