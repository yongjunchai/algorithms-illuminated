import sys
from algorithmIlliminated_3.utils import *

class Node:
    def __init__(self, key, frequency):
        self.key = key
        self.frequency = frequency


class OptBst:
    def __init__(self):
        pass

    def solveOptBst(self, nodes: list):
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



