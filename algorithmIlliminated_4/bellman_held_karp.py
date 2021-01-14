from utils.utils import *
import math
import itertools
import sys


class Solution:
    def __init__(self):
        self.length = None
        self.penultimateVertaxIndex = None


class BellManHeldKarp:
    def __init__(self, graph: Graph):
        # the input graph is a complete graph
        self.graph = graph

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
        rows = int(math.pow(2, n - 1) - 1)
        columns = n - 1
        subProblems = [[0 for i in range(columns)] for j in range(rows)]

        # base case, set size as 1
        for i in range(0, n - 1):
            solution = Solution()
            solution.length = matrixGraph[0][i + 1]
            solution.penultimateVertaxIndex = indexNameDict[str(i + 1)]
            subProblems[(1 << i) - 1][i] = solution

        vertexIndicesArray = [i for i in range(0, n - 1)]
        # set size 2 and beyond case
        for size in range(2, n):
            for indices in itertools.combinations(vertexIndicesArray, size):
                index = 0
                for i in indices:
                    index |= (1 << i)
                for j in indices:
                    solution = Solution()
                    solution.length = sys.maxsize
                    s = index & (~(1 << j))
                    for k in indices:
                        if k == j:
                            continue
                        subProblemSolution: Solution = subProblems[s - 1][k]
                        curLength = subProblemSolution.length + matrixGraph[k + 1][j + 1]
                        if curLength < solution.length:
                            solution.length = curLength
                            solution.penultimateVertaxIndex = k
                    subProblems[index - 1][j] = solution
        lastStop = None
        minTourLength = sys.maxsize
        for j in range(0, n - 1):
            subProblemSolution: Solution = subProblems[rows - 1][j]
            length = subProblemSolution.length + matrixGraph[0][j + 1]
            if length < minTourLength:
                lastStop = j
                minTourLength = length
        # reconstruct tour
        edgeTemplate = "{} --> {}  :: {}"
        print(edgeTemplate.format(indexNameDict[str(lastStop + 1)], indexNameDict["0"], matrixGraph[0][lastStop + 1]))
        curProblemSize = n - 1
        curProblemSet = rows
        curVertaxIndex = lastStop
        while curProblemSize > 1:
            solution: Solution = subProblems[curProblemSet - 1][curVertaxIndex]
            print(edgeTemplate.format(indexNameDict[str(solution.penultimateVertaxIndex + 1)], indexNameDict[str(curVertaxIndex + 1)], matrixGraph[solution.penultimateVertaxIndex + 1][curVertaxIndex + 1]))
            curProblemSize -= 1
            curProblemSet &= ~(1 << curVertaxIndex)
            curVertaxIndex = solution.penultimateVertaxIndex
        print(edgeTemplate.format(indexNameDict["0"], indexNameDict[str(curVertaxIndex + 1)], matrixGraph[0][curVertaxIndex + 1]))
        return minTourLength

