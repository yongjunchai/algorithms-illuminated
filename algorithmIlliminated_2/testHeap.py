import unittest
import random
from algorithmIlliminated_2.heap import Heap
from utils.utils import *


class MyTestCase(unittest.TestCase):
    def buildItems(self, keys):
        items = []
        for key in keys:
            items.append((key, None))
        return items

    def test_buildMinHeap(self):
        heap = Heap()
        keys = [5, 4, 1, 2, 6, 3, 8, 7, 9, 0]
        heap.buildHeap(self.buildItems(keys))
        heap.insert(13, None)
        heap.insert(11, None)
        heap.insert(12, None)
        heap.insert(10, None)
        for i in range(0, 14, 1):
            item = heap.extract_min()
            self.assertTrue(i == item[0])

    def test_shuffle_heap_ops(self):
        startMillSnds = current_milli_time()
        keys = []
        cnt = 1024 * 10
        for i in range(4, cnt, 1):
            keys.append(i)
        random.shuffle(keys)

        heap = Heap()
        heap.buildHeap(self.buildItems(keys))
        item = heap.extract_min()
        self.assertTrue(4 == item[0])
        heap.insert(2, None)
        item = heap.extract_min()
        self.assertTrue(2 == item[0])
        heap.insert(1, None)
        heap.insert(3, None)
        item = heap.extract_min()
        self.assertTrue(1 == item[0])
        item = heap.extract_min()
        self.assertTrue(3 == item[0])
        for i in range(5, cnt, 1):
            item = heap.extract_min()
            self.assertTrue(i == item[0])
        endMilliSnds = current_milli_time()
        print("time used to process 10K heaps [%d] ms" % (endMilliSnds - startMillSnds))


if __name__ == '__main__':
    unittest.main()
