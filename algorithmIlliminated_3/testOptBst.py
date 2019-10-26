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
        optBst = OptBst()
        frequencies = [0.8, 0.1, 0.1]
        nodes = list()
        for i in range(len(frequencies)):
            node = Node(i + 1, frequencies[i])
            nodes.append(node)
        subProblems = optBst.solveOptBst_n2(nodes)
        print(subProblems)

if __name__ == '__main__':
    unittest.main()
