import sys
from algorithmIlliminated_3.utils import *

class Node:
    def __init__(self, nodeName: str):
        self.name = nodeName
        self.inflowEdges = dict()

    def addInflowEdge(self, inflowNodeName: str, edgeLength: int):
        """
        only keep the shorted edge from the same node
        :param inflowNodeName:
        :param edgeLength:
        :return:
        """
        existingEdgeLen = self.inflowEdges.get(inflowNodeName)
        if existingEdgeLen is not None:
            if existingEdgeLen < edgeLength:
                return
        self.inflowEdges[inflowNodeName] = edgeLength


class Edge:
    def __init__(self, srcNodeName: str, targetNodeName: str, edgeLength: int):
        self.srcNodeName = srcNodeName
        self.targetNodeName = targetNodeName
        self.edgeLength = edgeLength


class Graph:
    def __init__(self, edges: list):
        self.nodes = dict()
        for edge in edges:
            node = self.nodes.get(edge.targetNodeName)
            if node is None:
                node = Node(edge.targetNodeName)
                self.nodes[edge.targetNodeName] = node
            node.addInflowEdge(edge.srcNodeName, edge.edgeLength)



class BellmanFord:
    def __init__(self):
        pass

    def findShortestPath(self, sourceNodeName: str, graph: Graph):
        steps = len(graph.nodes) + 1
        vertexes = len(graph.nodes)
        keys = graph.nodes.keys()
        nodes = list()
        nameIndexMap = dict()
        for key in keys:
            nodes.append(key)
        indexOfSourceNode = -1
        for i in range(0, len(nodes)):
            nameIndexMap[nodes[i]] = i
            if nodes[i] == sourceNodeName:
                indexOfSourceNode = i
                break
        assert(indexOfSourceNode > 0)
        subProblemsSolution = Utils.createArray([steps, vertexes])

        # base case
        subProblemsSolution[0][indexOfSourceNode] = 0
        for i in range(0, len(nodes)):
            if i == indexOfSourceNode:
                continue
            subProblemsSolution[0][i] = sys.maxsize

        for i in range(1, steps):
            stable = True
            for j in range(0, len(nodes)):
                if j == indexOfSourceNode:
                    continue
                minLen = subProblemsSolution[i - 1][j]
                for edge in graph.nodes[nodes[j]].inflowEdges.items():
                    inflowNodeName = edge[0]
                    edgeLength = edge[1]
                    inflowNodeIndex = nameIndexMap[inflowNodeName]
                    length = subProblemsSolution[i - 1][inflowNodeIndex] + edgeLength
                    if length < minLen:
                        minLen = length
                subProblemsSolution[i][j] = minLen
                if subProblemsSolution[i][j] != subProblemsSolution[i - 1][j]:
                    stable = False
            if stable:
                return subProblemsSolution
        return None



