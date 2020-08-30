
from utils.utils import *
import sys

"""
problem 19.8
"""


class TspSpecial:
    def __init__(self, graph: GraphUndirected):
        """
        graph is a connected an acyclic graph
        """
        self.graph = graph
        # edges of the shortest tour
        self.edges = dict()
        self.tourLength = sys.maxsize


    def getStartNode(self):
        for node in self.graph.nodes.values():
            return node
        return None

    def getMinTsp(self):
        self.graph.convertToCompleteUndirectedGraph()
        # set any node as the tour starting node
        startNode: NodeUndirected = self.getStartNode()
        edges: dict = startNode.connectedEdges
        nodesVisited = set()
        edgesVisited = dict()
        nodesVisited.add(startNode.name)
        targetNode, length = self.getNextNode(edges, nodesVisited)
        nodesVisited.add(targetNode.name)
        edge = Edge(startNode.name, targetNode.name, length)
        edgesVisited[edge.getEdgeKey()] = edge
        self.travel(startNode.name, targetNode, nodesVisited, edgesVisited)

    def getNextNode(self, edges: dict, nodesVisited: dict):
        for name, length in edges.items():
            if name in nodesVisited:
                continue
            return self.graph.nodes.get(name), length
        return None, None

    def travel(self, startNodeName: str, curNode: NodeUndirected, nodesVisited: set, edgesVisited: dict):
        # if all nodes visited, then the tour is done
        if len(nodesVisited) == len(self.graph.nodes):
            for name, length in curNode.connectedEdges.items():
                if name == startNodeName:
                    edge = Edge(curNode.name, startNodeName, length)
                    edgesVisited[edge.getEdgeKey()] = edge
                    totalLength = self.calculateEdgesLength(edgesVisited.values())
                    self.tourLength = totalLength
                    self.edges = edgesVisited
                    self.dumpTour(edgesVisited.values())
                    return
            for name, length in curNode.extConnectedEdges.items():
                if name == startNodeName:
                    edge = Edge(curNode.name, startNodeName, length)
                    edgesVisited[edge.getEdgeKey()] = edge
                    totalLength = self.calculateEdgesLength(edgesVisited.values())
                    self.tourLength = totalLength
                    self.edges = edgesVisited
                    self.dumpTour(edgesVisited.values())
                    return
            assert False
            return
        targetNode, length = self.getNextNode(curNode.connectedEdges, nodesVisited)
        if targetNode is None:
            targetNode, length = self.getNextNode(curNode.extConnectedEdges, nodesVisited)

        nodesVisited.add(targetNode.name)
        edge = Edge(curNode.name, targetNode.name, length)
        edgesVisited[edge.getEdgeKey()] = edge
        self.travel(startNodeName, targetNode, nodesVisited, edgesVisited)

    def dumpTour(self, edges: list):
        print("tour length: %d" % (self.calculateEdgesLength(edges)))
        for edge in edges:
            print(edge.srcNodeName + " --> " + edge.targetNodeName + "  :  " + str(edge.edgeLength))

    def calculateEdgesLength(self, edges: list):
        totalLength = 0
        for edge in edges:
            totalLength += edge.edgeLength
        return totalLength
