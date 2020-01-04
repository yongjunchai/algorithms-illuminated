from algorithmIlliminated_2.heap import *
from algorithmIlliminated_2.redBlackTree import *


class MedianHeap:
    def __init__(self):
        """
        invariants:
        1. all keys in in maxHeap <= all keys in minHeap
        2. the size diff of the two heap is < 2
        """
        self.maxHeap = Heap(HeapType.MAX)
        self.minHeap = Heap(HeapType.MIN)
        self.size = 0

    def insert(self, key: int, value: object):
        self.size = self.size + 1
        l = None
        if self.maxHeap.size > 0:
            l = self.maxHeap.peek()
        if l is not None and key < l[0]:
            self.maxHeap.insert(key, value)
        else:
            self.minHeap.insert(key, value)
        if self.maxHeap.size > self.minHeap.size + 1:
            item = self.maxHeap.extract_max()
            self.minHeap.insert(item[0], item[1])
        if self.minHeap.size > self.maxHeap.size + 1:
            item = self.minHeap.extract_min()
            self.maxHeap.insert(item[0], item[1])

    def getMedian(self):
        """
        :return: items[], if size is event, return middle two items; if size is odd, return two middle items
        """
        if self.size == 0:
            return None

        if self.size % 2 == 0:
            item1 = self.maxHeap.peek()
            item2 = self.minHeap.peek()
            return [item1, item2]
        else:
            if self.maxHeap.size > self.minHeap.size:
                item = self.maxHeap.peek()
                return [item]
            else:
                item = self.minHeap.peek()
                return [item]


class MedianTree:
    def __init__(self):
        self.tree: RedBlackTree = RedBlackTree()

    def insert(self, key, value):
        self.tree.insert(key, value)

    def getMedian(self):
        """
        :return: items[], if size is event, return middle two items; if size is odd, return two middle items
        """
        if self.tree.root is None:
            return None

        if self.tree.root.size % 2 == 0:
            k = self.tree.root.size / 2
            node1 = self.tree.selectEx(k)
            node2 = self.tree.selectEx(k + 1)
            return [(node1.key, node1.value), (node2.key, node2.value)]
        else:
            k = (self.tree.root.size + 1) / 2
            node = self.tree.selectEx(k)
            return [(node.key, node.value)]



