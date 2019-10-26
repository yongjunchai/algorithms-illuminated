import sys
from algorithmIlliminated_3.utils import *


class Node:
    def __init__(self, key, frequency):
        self.key = key
        self.frequency = frequency
        self.left = None
        self.right = None


class RootNode:
    def __init__(self, key, totalSum):
        self.key = key
        self.totalSum = totalSum


class OptBst:
    def __init__(self):
        pass

    def solveOptBst_n3(self, nodes: list):
        for i in range(1, len(nodes) + 1):
            assert(i == nodes[i - 1].key)
            assert (nodes[i - 1].frequency > 0)
        # subproblems (i indexed from 1, j indexed from 0)
        subProblemsSolution = Utils.createArray([len(nodes) + 2, len(nodes) + 1])
        # base case
        for i in range(1, len(nodes) + 2):
            subProblemsSolution[i][i - 1] = 0
        for size in range(1, len(nodes) + 1):
            for i in range(1, len(nodes) + 1 - size + 1):
                sumFrequency = 0
                for k in range(i, i + size):
                    sumFrequency = sumFrequency + nodes[k - 1].frequency
                minSubs = sys.maxsize
                for r in range(i, i + size):
                    value = subProblemsSolution[i][r - 1] + subProblemsSolution[r + 1][i + size - 1]
                    if value < minSubs:
                        minSubs = value
                subProblemsSolution[i][i + size - 1] = sumFrequency + minSubs
        return subProblemsSolution

    def solveOptBst_n2(self, nodes: list):
        for i in range(1, len(nodes) + 1):
            assert(i == nodes[i - 1].key)
            assert(nodes[i - 1].frequency > 0)

        # prepare frequency sum cache
        frequencySums = Utils.createArray([len(nodes), len(nodes)])
        # base case, size == 1
        for i in range(len(nodes)):
            frequencySums[i][i] = nodes[i].frequency
        for i in range(len(nodes)):
            for size in range(2, len(nodes) - i + 1):
                frequencySums[i][i + size - 1] = frequencySums[i][i + size - 2] + nodes[i + size - 1].frequency

        # prepare for subProblemsSolution
        subProblemsSolution = Utils.createArray([len(nodes) + 2, len(nodes) + 1])
        # base case, size == 1
        for i in range(1, len(nodes) + 1):
            subProblemsSolution[i][i] = RootNode(nodes[i - 1].key, nodes[i - 1].frequency)
        for i in range(1, len(nodes) + 2):
            subProblemsSolution[i][i - 1] = RootNode(0, 0)
        for size in range(2, len(nodes) + 1):
            for i in range(1, len(nodes) - size + 1 + 1):
                minRoot = subProblemsSolution[i][i + size - 1 - 1]
                maxRoot = subProblemsSolution[i + 1][i + size - 1]
                minSubRoot = RootNode(0, sys.maxsize)
                for j in range(minRoot.key, maxRoot.key + 1):
                    value = subProblemsSolution[i][j - 1].totalSum + subProblemsSolution[j + 1][i + size - 1].totalSum
                    if value < minSubRoot.totalSum:
                        minSubRoot.key = j
                        minSubRoot.totalSum = value
                minSubRoot.totalSum = minSubRoot.totalSum + frequencySums[i - 1][i + size - 1 - 1]
                subProblemsSolution[i][i + size - 1] = minSubRoot
        return subProblemsSolution

    def constructOptBST(self, subProblemsSolution, nodes: list, left: int, right: int):
        """
        :param subProblemsSolution: subproblems (i indexed from 1 to n + 1, j indexed from 0 to n - 1)
        :param nodes:
        :param left: index of nodes
        :param right: index of nodes
        :return: root node of the OptBST tree
        """
        assert(0 <= left <= len(nodes))
        if left > right:
            return None
        if left == right:
            return nodes[left - 1]
        rootNode = subProblemsSolution[left][right]
        node = Node(rootNode.key, nodes[rootNode.key - 1].frequency)
        node.left = self.constructOptBST(subProblemsSolution, nodes, left, rootNode.key - 1)
        node.right = self.constructOptBST(subProblemsSolution, nodes, rootNode.key + 1, right)
        return node



