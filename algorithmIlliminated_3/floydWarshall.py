from algorithmIlliminated_3.utils import *
import sys


class FloydWarshall:
    def __init__(self):
        pass

    def solveAllPairsShortestPath(self, graph: Graph):
        vertexesCnt = len(graph.nodes)
        keys = graph.nodes.keys()
        nodes = list()
        nameIndexMap = dict()
        i = 0
        for key in keys:
            nodes.append(key)
            nameIndexMap[key] = i
            i = i + 1
        subProblemSize = vertexesCnt + 1
        subProblemsSolutions = Utils.createArray([subProblemSize, vertexesCnt, vertexesCnt])

        # base case (problem size = 1, there is no internal vertex in path)
        for i in range(0, vertexesCnt):
            for j in range(0, vertexesCnt):
                iIndex = nameIndexMap[nodes[i]]
                jIndex = nameIndexMap[nodes[j]]
                if iIndex == jIndex:
                    subProblemsSolutions[0][iIndex][jIndex] = 0
                edgeLen = graph.nodes[nodes[j]].inflowEdges.get(nodes[i])
                if edgeLen is not None:
                    subProblemsSolutions[0][iIndex][jIndex] = edgeLen
                else:
                    subProblemsSolutions[0][iIndex][jIndex] = sys.maxsize

        # systematically solve subproblems
        for i in range(1, subProblemSize):
            for j in range(0, vertexesCnt):
                for k in range(0, vertexesCnt):
                    iIndex = nameIndexMap[nodes[i - 1]]
                    jIndex = nameIndexMap[nodes[j]]
                    kIndex = nameIndexMap[nodes[k]]
                    minLen = subProblemsSolutions[i - 1][jIndex][iIndex] + subProblemsSolutions[i - 1][iIndex][kIndex]
                    if minLen > subProblemsSolutions[i - 1][jIndex][kIndex]:
                        minLen = subProblemsSolutions[i - 1][jIndex][kIndex]
                    subProblemsSolutions[i][jIndex][kIndex] = minLen

        # check for negative cycle
        for i in vertexesCnt:
            index = nameIndexMap[nodes[i]]
            if subProblemsSolutions[subProblemSize - 1][index][index] < 0:
                return None
        return subProblemsSolutions


