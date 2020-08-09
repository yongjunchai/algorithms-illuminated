import sys
from utils.utils import *
import copy


class TSP:
    def __init__(self, graph: Graph):
        # list of tour edges with minimum length
        self.edges = list()
        self.tourLength = sys.maxsize
        self.graph = graph

    def solve(self, start: Node):
        edges: dict = start.outflowEdges
        for edge in edges:
            nodesVisited = set()
            edgesVisited = list()
            target = self.graph.nodes.get(edge.targetNodeName)
            nodesVisited.add(start.name)
            nodesVisited.add(target.name)
            edgesVisited.append(edge)
            self.travel(start, target, copy.deepcopy(nodesVisited), copy.deepcopy(edgesVisited))

    def calculateEdgesLength(self, edges: list):
        totalLength = 0
        for edge in edges:
            totalLength += edge.edgeLength
        return totalLength

    def travel(self, startNode: Node, curNode: Node, nodesVisited: set, edgesVisited: list):
        # if all nodes visited, then the tour is done
        # check whether the current tour is the shortest tour
        if len(nodesVisited) == len(self.graph.nodes):
            for name, length in curNode.outflowEdges.items():
                if name == startNode.name:
                    edge = Edge(curNode.name, startNode.name, length)
                    edgesVisited.append(edge)
                    totalLength = self.calculateEdgesLength(edgesVisited)
                    if totalLength < self.tourLength:
                        self.tourLength = totalLength
                        self.edges = copy.deepcopy(edgesVisited)
                    return
            assert False
            return
        edges: dict = curNode.outflowEdges
        for edge in edges:
            if edge.targetNodeName in nodesVisited:
                continue
            targetNode = self.graph.nodes.get(edge.targetNodeName)
            self.travel(startNode, targetNode, copy.deepcopy(nodesVisited).add(edge.targetNodeName),
                        copy.deepcopy(edgesVisited).append(edge))


    # TODO: don't copy the collection

