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
        huffmanTree = HuffmanTree()
        for data in self.dataSet:
            res1 = huffmanTree.sorted_buildHuffmanTree(data)
            list1 = []
            huffmanTree.dumpCode(res1, "", list1)
            list1 = sorted(list1)
            res2 = huffmanTree.heap_HuffmanTree(data)
            list2 = []
            huffmanTree.dumpCode(res2, "", list2)
            list2 = sorted(list2)
            res3 = huffmanTree.quadraticTime_buildHuffmanTree(data)
            list3 = []
            huffmanTree.dumpCode(res3, "", list3)
            list3 = sorted(list3)
            self.assertTrue(len(list1) == len(list2))
            self.assertTrue(len(list2) == len(list3))
            for i in range(0, len(list1)):
                self.assertTrue(list1[i][0] == list2[i][0])
                self.assertTrue(list2[i][0] == list3[i][0])
                self.assertTrue(len(list1[i][1]) == len(list2[i][1]))
                self.assertTrue(len(list2[i][1]) == len(list3[i][1]))


if __name__ == '__main__':
    unittest.main()
