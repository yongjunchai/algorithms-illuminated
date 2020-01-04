import unittest
from algorithmIlliminated_2.medianMaintenance import *
from utils.utils import *
import random

"""
problem 11.3

Test result:
    with smaller data set like less than 100k, heap is faster
    with big data set like more than 100K, tree is faster
    
    possible reason: heap use array, too much data cause more memory reallocation and copy
"""


class MyTestCase(unittest.TestCase):
    def test_heapMedian(self):
        cnt = 1024
        heap = MedianHeap()
        for i in range(1, cnt, 1):
            heap.insert(i, True)
            if i % 2 == 0:
                k = i / 2
                items = heap.getMedian()
                self.assertTrue(len(items) == 2)
                self.assertTrue(items[0][0] == k)
                self.assertTrue(items[1][0] == k + 1)
            else:
                k = (i + 1) / 2
                items = heap.getMedian()
                self.assertTrue(len(items) == 1)
                self.assertTrue(items[0][0] == k)

    def test_TreeMedian(self):
        cnt = 1024
        tree = MedianTree()
        for i in range(1, cnt, 1):
            tree.insert(i, True)
            if i % 2 == 0:
                k = i / 2
                items = tree.getMedian()
                self.assertTrue(len(items) == 2)
                self.assertTrue(items[0][0] == k)
                self.assertTrue(items[1][0] == k + 1)
            else:
                k = (i + 1) / 2
                items = tree.getMedian()
                self.assertTrue(len(items) == 1)
                self.assertTrue(items[0][0] == k)

    def test_perf_compete_median_heap_tree(self):
        cnt = 1024 * 100
        tree = MedianTree()
        timerTree = Timer()
        timerTree.start()
        for i in range(1, cnt, 1):
            tree.insert(i, True)
            if i % 2 == 0:
                k = i / 2
                items = tree.getMedian()
                self.assertTrue(len(items) == 2)
                self.assertTrue(items[0][0] == k)
                self.assertTrue(items[1][0] == k + 1)
            else:
                k = (i + 1) / 2
                items = tree.getMedian()
                self.assertTrue(len(items) == 1)
                self.assertTrue(items[0][0] == k)
        timerTree.stop()
        heap = MedianHeap()
        timerHeap = Timer()
        timerHeap.start()
        for i in range(1, cnt, 1):
            heap.insert(i, True)
            if i % 2 == 0:
                k = i / 2
                items = heap.getMedian()
                self.assertTrue(len(items) == 2)
                self.assertTrue(items[0][0] == k)
                self.assertTrue(items[1][0] == k + 1)
            else:
                k = (i + 1) / 2
                items = heap.getMedian()
                self.assertTrue(len(items) == 1)
                self.assertTrue(items[0][0] == k)
        timerHeap.stop()
        print("tree use [%d]ms, heap use [%s]ms to process [%d] items" % (timerTree.timeElapsedMs(), timerHeap.timeElapsedMs(), cnt))
        if timerTree.timeElapsedMs() < timerHeap.timeElapsedMs():
            print("tree is faster")
        else:
            print("heap is faster")

    def test_perf_compete_median_heap_tree_rnd(self):
        cnt = 1024 * 300
        keys = []
        for i in range(1, cnt, 1):
            keys.append(i)
        random.shuffle(keys)

        tree = MedianTree()
        timerTree = Timer()
        timerTree.start()
        for i in keys:
            tree.insert(i, True)
            items = tree.getMedian()
        timerTree.stop()
        heap = MedianHeap()
        timerHeap = Timer()
        timerHeap.start()
        for i in keys:
            heap.insert(i, True)
            items = heap.getMedian()
        timerHeap.stop()
        print("tree use [%d]ms, heap use [%s]ms to process [%d] items" % (timerTree.timeElapsedMs(), timerHeap.timeElapsedMs(), cnt))
        if timerTree.timeElapsedMs() < timerHeap.timeElapsedMs():
            print("tree is faster")
        else:
            print("heap is faster")


if __name__ == '__main__':
    unittest.main()
