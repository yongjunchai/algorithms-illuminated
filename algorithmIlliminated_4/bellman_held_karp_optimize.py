
from utils.utils import *
import itertools
import sys


class Solution:
    def __init__(self):
        self.length = None
        self.penultimateVertexIndex = None


# problem 21.8
class BellmanHeldKarpOptimize:
    def __init__(self, graph: Graph):
        # the input graph is a complete graph
        self.graph = graph

    def createKeyFromList(self, items: list, itemToSkip: int):
        sItems = sorted(items)
        key = ""
        for i in sItems:
            if i == itemToSkip:
                continue
            key += "_" + str(i)
        return key

    def run(self):
        n = len(self.graph.nodes)
        # create index to vertax name map
        # create vertax name to index map
        indexNameDict = dict()
        nameIndexDict = dict()
        i = - 1
        for nodeName in self.graph.nodes.keys():
            i += 1
            indexNameDict[str(i)] = nodeName
            nameIndexDict[nodeName] = i
        #create matrix graph
        matrixGraph = [[0 for i in range(n)] for j in range(n)]
        for i in range(0, n):
            matrixGraph[i][i] = 0
        for value in self.graph.nodes.values():
            node: Node = value
            srcIndex = nameIndexDict[node.name]
            for name, length in node.outflowEdges.items():
                targetIndex = nameIndexDict[name]
                matrixGraph[srcIndex][targetIndex] = length
                matrixGraph[targetIndex][srcIndex] = length
        # assume vertex with index as 0 as the start vertex
        # <key, list of size n - 1>
        subProblems = dict()
        # base case, set size as 1
        for i in range(0, n - 1):
            solution = Solution()
            solution.length = matrixGraph[0][i + 1]
            solution.penultimateVertexIndex = indexNameDict[str(i + 1)]
            subProblems["_" + str(i)] = [None for i in range(0, n - 1)]
            subProblems["_" + (str(i))][i] = solution

        vertexIndicesArray = [i for i in range(0, n - 1)]
        # set size 2 and beyond case
        for size in range(2, n):
            curProblems = dict()
            for indices in itertools.combinations(vertexIndicesArray, size):
                curKey = self.createKeyFromList(indices, None)
                curProblems[curKey] = [None for i in range(0, n - 1)]
                for j in indices:
                    solution = Solution()
                    solution.length = sys.maxsize
                    s = self.createKeyFromList(indices, j)
                    for k in indices:
                        if k == j:
                            continue
                        subProblemSolution: Solution = subProblems[s][k]
                        curLength = subProblemSolution.length + matrixGraph[k + 1][j + 1]
                        if curLength < solution.length:
                            solution.length = curLength
                            solution.penultimateVertexIndex = k
                    curProblems[curKey][j] = solution
            subProblems = curProblems
        minTourLength = sys.maxsize
        key = self.createKeyFromList(vertexIndicesArray, None)
        for j in range(0, n - 1):
            subProblemSolution: Solution = subProblems[key][j]
            length = subProblemSolution.length + matrixGraph[0][j + 1]
            if length < minTourLength:
                minTourLength = length
        return minTourLength

