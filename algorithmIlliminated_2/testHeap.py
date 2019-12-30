import unittest
from algorithmIlliminated_2.heap import Heap


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


if __name__ == '__main__':
    unittest.main()
