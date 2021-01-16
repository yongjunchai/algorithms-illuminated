
from utils.utils import *
import math
import itertools
import sys
import random


class Solution:
    def __init__(self):
        self.previousVertexIndex: int = None
        self.length = 0
        self.edgeLength = 0


class PanchromaticPath:
    def __init__(self, graph: Graph):
        self.graph = graph

    def run(self, k: int):
        n = len(self.graph.nodes)
        if k > len(self.graph.nodes):
            return None

        nameIndexDict = dict()
        indexNameDict = dict()
        cnt = 0
        for item in self.graph.nodes.values():
            node: Node = item
            nameIndexDict[node.name] = cnt
            indexNameDict[str(cnt)] = node.name
            cnt += 1

        rows = int(math.pow(2, k) - 1)
        columns = n
        subProblems = [[None for j in range(0, columns)] for i in range(0, rows)]

        # base case
        for i in range(0, k):
            s = 1 << i
            for item in self.graph.nodes.values():
                node: Node = item
                if node.color == i:
                    solution = Solution()
                    solution.length = 0
                    subProblems[s - 1][nameIndexDict[node.name]] = solution
        colorsArray = [i for i in range(0, k)]
        for size in range(2, k + 1):
            for colors in itertools.combinations(colorsArray, size):
                s = 0
                for color in colors:
                    s |= 1 << color
                for item in self.graph.nodes.values():
                    node: Node = item
                    if (1 << node.color) & s == 0:
                        continue
                    minLength = sys.maxsize
                    lastEdgeLength = None
                    lastVertex = None
                    for target, edgeLength in node.outflowEdges.items():
                        targetNode = self.graph.nodes[target]
                        if (1 << targetNode.color) & s == 0:
                            continue
                        subProblemColorSet = s & (~(1 << node.color))
                        subProblemSolutioin: Solution = subProblems[subProblemColorSet - 1][nameIndexDict[targetNode.name]]
                        if subProblemSolutioin is None:
                            continue
                        length = subProblemSolutioin.length + edgeLength
                        if length < minLength:
                            minLength = length
                            lastEdgeLength = edgeLength
                            lastVertex = nameIndexDict[target]
                    if minLength != sys.maxsize:
                        solution: Solution = Solution()
                        solution.previousVertexIndex = lastVertex
                        solution.length = minLength
                        solution.edgeLength = lastEdgeLength
                        subProblems[s - 1][nameIndexDict[node.name]] = solution
        kPathLength = sys.maxsize
        vertexIndex = None
        # find k-path solution
        for i in range(0, n):
            solution = subProblems[rows - 1][i]
            if solution is None:
                continue
            if solution.length < kPathLength:
                kPathLength = solution.length
                vertexIndex = i
        if vertexIndex is None:
            return None
        # reconstruct path
        size = k
        curVertexIndex = vertexIndex
        curSet = rows
        edgeTemplate = "{} --> {} "" {}"
        while size > 1:
            curSolution: Solution = subProblems[curSet - 1][curVertexIndex]
            print(edgeTemplate.format(indexNameDict[str(curSolution.previousVertexIndex)], indexNameDict[str(curVertexIndex)], curSolution.edgeLength))
            size -= 1
            curNode = self.graph.nodes[indexNameDict[str(curVertexIndex)]]
            curSet &= ~(1 << curNode.color)
            curVertexIndex = curSolution.previousVertexIndex
        return kPathLength


class ColorCoding:
    def __init__(self, graph: Graph):
        self.graph = graph

    def run(self, k: int, p: float):
        if k < 2 or k > len(self.graph.nodes) or p >= 1 or p <= 0:
            return None

        minKpath = sys.maxsize
        t = int(math.pow(math.e, k) / math.sqrt(2 * math.pi * k) * math.log(1 / p, math.e))
        for i in range(0, t):
            for item in self.graph.nodes.values():
                node: Node = item
                node.color = random.randint(0, k - 1)
            panchromaticPath = PanchromaticPath(self.graph)
            length = panchromaticPath.run(k)
            if length is not None and length < minKpath:
                minKpath = length
        return minKpath


