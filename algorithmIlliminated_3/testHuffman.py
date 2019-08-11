import unittest
import time
from algorithmIlliminated_3.huffman import HuffmanTree


def current_milli_time():
    return time.time_ns() / 1000


class TestHuffman(unittest.TestCase):
    def loadTestData(self, fileName):
        f = open(fileName, "r")
        lines = f.readlines()
        isFirstLine = True
        vals = []
        for line in lines:
            if isFirstLine:
                isFirstLine = False
                continue
            val = int(line)
            vals.append(val)
        f.close()
        return vals

    def setUp(self):
        self.dataSet = []
        self.dataSet.append(self.loadTestData("huffmanTestData/problem14.6.txt"))
        self.dataSet.append(self.loadTestData("huffmanTestData/problem14.6test1.txt"))
        self.dataSet.append(self.loadTestData("huffmanTestData/problem14.6test2.txt"))

    def test_perf_quadratic(self):
        print("start test_perf_quadratic")
        start = current_milli_time()
        huffmanTree = HuffmanTree()
        for data in self.dataSet:
            huffmanTree.quadraticTime_buildHuffmanTree(data)
        end = current_milli_time()
        print("\n time used: %s ms \n" % str(end - start))
        print("done test_perf_quadratic")

    def test_perf_heap(self):
        print("start test_perf_heap")
        start = current_milli_time()
        huffmanTree = HuffmanTree()
        for data in self.dataSet:
            huffmanTree.heap_HuffmanTree(data)
        end = current_milli_time()
        print("\n time used: %s ms \n" % str(end - start))
        print("done test_perf_heap")

    def test_perf_sort_with_additionalLinearEffort(self):
        print("start test_perf_sort_with_additionalLinearEffort")
        start = current_milli_time()
        huffmanTree = HuffmanTree()
        for data in self.dataSet:
            huffmanTree.sorted_buildHuffmanTree(data)
        end = current_milli_time()
        print("\n time used: %s ms \n" % str(end - start))
        print("done test_perf_sort_with_additionalLinearEffort")

    def test_correctness(self):
        pass


if __name__ == '__main__':
    unittest.main()
