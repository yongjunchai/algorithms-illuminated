import unittest
from algorithmIlliminated_3.optBst import *

class OptBstTestCase(unittest.TestCase):
    def test_solveOptBst_n3(self):
        optBst = OptBst()
        frequencies = [0.8, 0.1, 0.1]
        nodes = list()
        for i in range(len(frequencies)):
            node = Node(i + 1, frequencies[i])
            nodes.append(node)
        subProblems = optBst.solveOptBst_n3(nodes)
        print(subProblems)

    def test_solveOptBst_n2(self):
        dataSet = [([0.8, 0.1, 0.1], (1, 1.3, None, 2))]
        optBst = OptBst()
        for data in dataSet:
            frequencies = data[0]
            rootKey = data[1][0]
            totalSum = data[1][1]
            leftChildKey = data[1][2]
            rightChildKey = data[1][3]
            nodes = list()
            for i in range(len(frequencies)):
                node = Node(i + 1, frequencies[i])
                nodes.append(node)
            subProblems = optBst.solveOptBst_n2(nodes)
            self.assertTrue(subProblems[1][len(nodes)].key == rootKey)
            self.assertTrue(subProblems[1][len(nodes)].totalSum == totalSum)

            root = optBst.constructOptBST(subProblems, nodes, 1, len(nodes))
            self.assertTrue(root.key == rootKey)
            print(root)
            if root.left is None:
                self.assertTrue(leftChildKey is None)
            else:
                self.assertTrue(root.left.key == leftChildKey)
            if root.right is None:
                self.assertTrue(rightChildKey is None)
            else:
                self.assertTrue(root.right.key == rightChildKey)


if __name__ == '__main__':
    unittest.main()
