from collections import deque
from enum import Enum


class HeapType(Enum):
    MIN = 1
    MAX = 2


class Heap:
    """
    this is an array based min/max heap
    left child index: 2i + 1
    right child index: 2i + 2
    """

    def __init__(self, heapType: HeapType):
        self.items = deque()
        self.size = 0
        self.heapType = heapType

    # TODO: problem 10.6

    def buildHeap(self, items: list):
        """
        heapify a list of items
        :param items: each item is a tuple. item[0] is a number, item[1] is an object
        :return:
        """
        self.items.extend(items)
        self.size = len(items)
        for i in range(int(self.size / 2) - 1, -1, -1):
            self.bubbleDown(i)

    def swapItems(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def bubbleDown(self, i):
        if self.heapType == HeapType.MIN:
            minimum = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < self.size and self.items[minimum][0] > self.items[l][0]:
                minimum = l
            if r < self.size and self.items[minimum][0] > self.items[r][0]:
                minimum = r
            if minimum != i:
                self.swapItems(i, minimum)
                self.bubbleDown(minimum)
        else:
            maximum = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < self.size and self.items[maximum][0] < self.items[l][0]:
                maximum = l
            if r < self.size and self.items[maximum][0] < self.items[r][0]:
                maximum = r
            if maximum != i:
                self.swapItems(i, maximum)
                self.bubbleDown(maximum)

    def bubbleUp(self, i):
        if i == 0:
            return
        p = int((i - 1) / 2)
        if self.heapType == HeapType.MIN:
            if self.items[p][0] > self.items[i][0]:
                self.swapItems(p, i)
                self.bubbleUp(p)
        else:
            if self.items[p][0] < self.items[i][0]:
                self.swapItems(p, i)
                self.bubbleUp(p)

    def insert(self, key: int, value):
        self.items.append((key, value))
        self.size = len(self.items)
        self.bubbleUp(self.size - 1)

    def extract_min(self):
        """
        :return: item, item[0] is int, item[1] is an object
        """
        if self.heapType != HeapType.MIN:
            raise Exception("not supported method")
        item = self.items[0]
        self.items[0] = self.items[self.size - 1]
        self.size = self.size - 1
        self.items.pop()
        self.bubbleDown(0)
        return item

    def extract_max(self):
        """
        :return: item, item[0] is int, item[1] is an object
        """
        if self.heapType != HeapType.MAX:
            raise Exception("not supported method")
        item = self.items[0]
        self.items[0] = self.items[self.size - 1]
        self.size = self.size - 1
        self.items.pop()
        self.bubbleDown(0)
        return item
