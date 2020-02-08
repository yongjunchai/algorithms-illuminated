import copy
import math
import sys
from algorithmIlliminated_1.mergeSort import *


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.index = None


class ClosestPair:
    def __init__(self):
        pass

    def calcDistance(self, p1: Point, p2: Point):
        return math.sqrt(math.pow(p1.x - p2.x, 2) + math.pow(p1.y - p2.y, 2))

    def closestPair(self, points: list):
        if len(points) < 2:
            return None, None
        if len(points) == 2:
            return points[0], points[1]
        if len(points) == 3:
            len1 = self.calcDistance(points[0], points[1])
            len2 = self.calcDistance(points[0], points[2])
            len3 = self.calcDistance(points[1], points[2])
            minLen = len1
            pair = points[0], points[1]
            if len2 < minLen:
                minLen = len2
                pair = (points[0], points[2])
            if len3 < minLen:
                minLen = len3
                pair = (points[1], points[2])
            return pair
        mergeSort = MergeSort()
        px = mergeSort.mergeSort(points, lambda p1, p2: p1.x < p2.x)
        for i in range(0, len(points)):
            px[i].index = i
        py = px
        py = mergeSort.mergeSort(py, lambda p1, p2: p1.y < p2.y)
        self.closestPair_internal(px, py)

    def closestSplitPair(self, px, py, minLenPair):
        mid = int(len(px) / 2)
        midX = px[mid - 1].x
        lx = midX - minLenPair
        rx = midX + minLenPair
        sy = []
        for i in range(len(py)):
            if lx <= py[i] <= rx:
                sy.append(py[i])
        best = minLenPair
        bestPair = (None, None)
        for i in range(len(sy) - 1):
            maxStep = min(7, len(sy) - 1 - i)
            for j in range(1, maxStep + 1):
                curLen = self.calcDistance(sy[i], sy[i + j])
                if curLen < best:
                    best = curLen
                    bestPair = (sy[i], sy[i + j])
        return bestPair

    def closestPair_internal(self, px: list, py: list):
        assert(len(px) == len(py))
        if len(px) < 2:
            return None, None
        if len(px) == 2:
            return px[0], px[1]
        if len(px) == 3:
            len1 = self.calcDistance(px[0], px[1])
            len2 = self.calcDistance(px[0], px[2])
            len3 = self.calcDistance(px[1], px[2])
            minLenPair = len1
            pair = px[0], px[1]
            if len2 < minLenPair:
                minLenPair = len2
                pair = (px[0], px[2])
            if len3 < minLenPair:
                minLenPair = len3
                pair = (px[1], px[2])
            return pair
        mid = int(len(px) / 2)
        midIndex = px[mid - 1].index
        lx = []
        rx = []
        for i in range(0, mid):
            lx.append(px[i])
        for i in range(mid, len(px)):
            rx.append(px[i])
        ly = []
        ry = []
        for i in range(0, len(py)):
            if py[i].index <= midIndex:
                ly.append(py[i])
            else:
                ry.append(py[i])
        l1, l2 = self.closestPair_internal(lx, ly)
        r1, r2 = self.closestPair_internal(rx, ry)
        lLen = self.calcDistance(l1, l2)
        rLen = self.calcDistance(r1, r2)
        minLenPair = lLen
        minPair = (l1, l2)
        if minLenPair < rLen:
            minLenPair = rLen
            minPair = (r1, r2)
        s1, s2 = self.closestSplitPair(px, py, minLenPair)
        if s1 is not None and s2 is not None:
            minPair = (s1, s2)
        return minPair


p1 = Point(122, 11)
p2 = Point(111, 112)
p3 = Point(1, 2)
p4 = Point(10000, 1)

ps = [p1, p2, p3, p4]

c = ClosestPair()
c.closestPair(ps)