import sys
from algorithmIlliminated_3.utils import *


class Node:
    def __init__(self, key, frequency):
        self.key = key
        self.frequency = frequency


class RootNode:
    def __init__(self, key, totalSum):
        self.key = key
        self.sum = totalSum


class OptBst:
    def __init__(self):
        pass

    def solveOptBst_n3(self, nodes: list):
        for i in range(1, len(nodes) + 1):
            assert(i == nodes[i - 1].key)
            assert (nodes[i - 1].frequency > 0)
        # subproblems (i indexed from 1, j indexed from 0)
        subProblems = Utils.createArray([len(nodes) + 2, len(nodes) + 1])
        # base case
        for i in range(1, len(nodes) + 2):
            subProblems[i][i - 1] = 0
        for size in range(1, len(nodes) + 1):
            for i in range(1, len(nodes) + 1 - size + 1):
                sumFrequency = 0
                for k in range(i, i + size):
                    sumFrequency = sumFrequency + nodes[k - 1].frequency
                minSubs = sys.maxsize
                for r in range(i, i + size):
                    value = subProblems[i][r - 1] + subProblems[r + 1][i + size - 1]
                    if value < minSubs:
                        minSubs = value
                subProblems[i][i + size - 1] = sumFrequency + minSubs
        return subProblems


    def solveOptBst_n2(self, nodes: list):
        for i in range(1, len(nodes) + 1):
            assert(i == nodes[i - 1].key)
            assert(nodes[i - 1].frequency > 0)

        # prepare frequency sum cache
        frequencySums = Utils.createArray([len(nodes), len(nodes)])
        # base case, size == 1
        for i in range(len(nodes)):
            frequencySums[i][0] = nodes[i].frequency
        for i in range(len(nodes)):
            for size in range(2, len(nodes) + 1):
                frequencySums[i][i + size - 1] = frequencySums[i][i + size - 2] + nodes[i + size - 1]

        # prepare for subProblemsSum
        subProblemsSum = Utils.createArray([len(nodes), len(nodes)])
        # base case, size == 1
        for i in range(len(nodes)):
            subProblemsSum[i][0] = RootNode(nodes[i].key, nodes[i].frequency)
        for i in range(len(nodes)):
            for size in range(2, len(nodes) + 1):
                minRoot = subProblemsSum[i][i + size - 1 - 1]
                maxRoot = subProblemsSum[i + 1][i + size - 1]
                minSubRoot = RootNode(0, sys.maxsize)
                for j in range(minRoot.key - 1, maxRoot.key):
                    value = subProblemsSum[i][j - 1].totalSum + subProblemsSum[i + 1][j].totalSum
                    if value < minSubRoot.sum:
                        minSubRoot.key = j + 1
                        minSubRoot.totalSum = value
                subProblemsSum[i][i + size - 1] = minSubRoot

        # subproblems (i indexed from 1 to n + 1, j indexed from 0 to n - 1)
        subProblems = Utils.createArray([len(nodes) + 2, len(nodes) + 1])
        # base case
        for i in range(1, len(nodes) + 2):
            subProblems[i][i - 1] = 0
        for size in range(1, len(nodes) + 1):
            for i in range(1, len(nodes) + 1 - size + 1):
                subProblems[i][i + size - 1] = frequencySums[i - 1][i - 1 + size - 1] + subProblemsSum[i - 1][i - 1 + size - 1]
        return subProblems


