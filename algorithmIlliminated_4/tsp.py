import sys
from utils.utils import *


class TSP:
    def __init__(self, graph: Graph):
        # edges of the shortest tour
        self.edges = dict()
        self.tourLength = sys.maxsize
        self.graph = graph

    def getEdgeKey(self, edge: Edge):
        return edge.srcNodeName + "_to_" + edge.targetNodeName

    def solve(self, start: str):
        startNode: Node = self.graph.nodes.get(start)
        edges: dict = startNode.outflowEdges
        nodesVisited = set()
        edgesVisited = dict()
        nodesVisited.add(start)
        for name, length in edges.items():
            target = self.graph.nodes.get(name)
            nodesVisited.add(target.name)
            edge = Edge(start, name, length)
            edgesVisited[self.getEdgeKey(edge)] = edge
            self.travel(start, target, nodesVisited, edgesVisited)
            nodesVisited.remove(target.name)
            edgesVisited.pop(self.getEdgeKey(edge))
        assert len(edgesVisited) == 0
        assert len(nodesVisited) == 1

    def calculateEdgesLength(self, edges: dict):
        totalLength = 0
        for edge in edges.values():
            totalLength += edge.edgeLength
        return totalLength

    def travel(self, start: str, curNode: Node, nodesVisited: set, edgesVisited: dict):
        # if all nodes visited, then the tour is done
        # check whether the current tour is the shortest tour
        if len(nodesVisited) == len(self.graph.nodes):
            for name, length in curNode.outflowEdges.items():
                if name == start:
                    edge = Edge(curNode.name, start, length)
                    edgesVisited[self.getEdgeKey(edge)] = edge
                    totalLength = self.calculateEdgesLength(edgesVisited)
                    if totalLength < self.tourLength:
                        self.tourLength = totalLength
                        self.edges = copy.deepcopy(edgesVisited)
                    edgesVisited.pop(self.getEdgeKey(edge))
                    return
            assert False
            return

        edges: dict = curNode.outflowEdges
        for name, length in edges.items():
            if name in nodesVisited:
                continue
            targetNode = self.graph.nodes.get(name)
            nodesVisited.add(name)
            edge = Edge(curNode.name, name, length)
            edgesVisited[self.getEdgeKey(edge)] = edge
            self.travel(start, targetNode, nodesVisited, edgesVisited)
            nodesVisited.remove(targetNode.name)
            edgesVisited.pop(self.getEdgeKey(edge))


