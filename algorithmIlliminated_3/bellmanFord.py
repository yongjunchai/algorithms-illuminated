import sys
from collections import deque
from algorithmIlliminated_3.utils import *



class BellmanFord:
    def __init__(self):
        pass

    def findShortestPath(self, sourceNodeName: str, graph: Graph):
        maxSteps = len(graph.nodes)
        vertexesCnt = len(graph.nodes)
        keys = graph.nodes.keys()
        nodes = list()
        nameIndexMap = dict()
        i = 0
        indexOfSourceNode = -1
        for key in keys:
            nodes.append(key)
            nameIndexMap[key] = i
            if key == sourceNodeName:
                indexOfSourceNode = i
            i = i + 1

        assert(indexOfSourceNode >= 0)
        subProblemsSolution = Utils.createArray([maxSteps + 1, vertexesCnt])

        # base case
        subProblemsSolution[0][indexOfSourceNode] = Solution(0, None)
        for i in range(0, len(nodes)):
            if i == indexOfSourceNode:
                continue
            subProblemsSolution[0][i] = Solution(sys.maxsize, None)

        for i in range(1, maxSteps + 1):
            stable = True
            for j in range(0, len(nodes)):
                if j == indexOfSourceNode:
                    subProblemsSolution[i][indexOfSourceNode] = Solution(0, None)
                    continue
                minLen = subProblemsSolution[i - 1][j].length
                minInflowNodeName = subProblemsSolution[i - 1][j].inflowNodeName
                for edge in graph.nodes[nodes[j]].inflowEdges.items():
                    inflowNodeName = edge[0]
                    edgeLength = edge[1]
                    inflowNodeIndex = nameIndexMap[inflowNodeName]
                    length = subProblemsSolution[i - 1][inflowNodeIndex].length + edgeLength
                    if length < minLen:
                        minLen = length
                        minInflowNodeName = inflowNodeName
                subProblemsSolution[i][j] = Solution(minLen,  minInflowNodeName)
                if subProblemsSolution[i][j].length != subProblemsSolution[i - 1][j].length:
                    stable = False
            if stable:
                return subProblemsSolution, i
        return None, None

    def constructSolution(self, sourceNodeName: str, graph: Graph, subProblemsSolution, stableStep: int):
        maxSteps = len(graph.nodes)
        vertexesCnt = len(graph.nodes)
        keys = graph.nodes.keys()
        nodes = list()
        nameIndexMap = dict()
        i = 0
        indexOfSourceNode = -1
        for key in keys:
            nodes.append(key)
            nameIndexMap[key] = i
            if key == sourceNodeName:
                indexOfSourceNode = i
            i = i + 1

        assert(indexOfSourceNode >= 0)
        assert(maxSteps == len(subProblemsSolution) - 1)
        assert(vertexesCnt == len(subProblemsSolution[0]))
        paths = dict()
        for item in nameIndexMap.items():
            key = item[0]
            index = item[1]
            if key == sourceNodeName:
                continue
            path = Path()
            paths[key] = path
            curStep = stableStep
            path.length = subProblemsSolution[curStep][index].length
            path.path.appendleft(key)
            while curStep > 0:
                # skip un-needed steps
                if subProblemsSolution[curStep][index].length == subProblemsSolution[curStep - 1][index].length:
                    curStep = curStep - 1
                    continue
                key = subProblemsSolution[curStep][index].inflowNodeName
                index = nameIndexMap[key]
                path.path.appendleft(key)
                curStep = curStep - 1
        return paths






