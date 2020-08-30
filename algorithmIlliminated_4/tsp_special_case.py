
from utils.utils import *
import json

"""
problem 19.8
"""


class TspSpecial:
    def __init__(self, graph: GraphUndirected):
        """
        graph is a connected an acyclic graph
        """
        self.graph = graph

    def convertToCompleteUndirectedGraph(self):
        for node in self.graph.nodes.values():
            self.graph.clearVisitedFlag()
            node.visited = True
            for item in node.connectedEdges.items():
                nodeName = item[0]
                edgeLength = item[1]
                nodeConnected: NodeUndirected = self.graph.nodes.get(nodeName)
                nodeConnected.visited = True
                for itemSndLevel in nodeConnected.connectedEdges.items():
                    nodeNameSndLevel = itemSndLevel[0]
                    edgeLengthSndLevel = itemSndLevel[1]
                    if nodeNameSndLevel == node.name:
                        continue
                    nodeSndLevel: NodeUndirected = self.graph.nodes.get(nodeNameSndLevel)
                    self.completeNode(nodeSndLevel, node, edgeLength + edgeLengthSndLevel)

    def completeNode(self, node: NodeUndirected, nodeStart: NodeUndirected, pathLength: int):
        node.visited = True
        nodeStart.addExtEdge(node.name, pathLength)
        for item in node.connectedEdges.items():
            nodeName = item[0]
            edgeLength = item[1]
            nodeConnected: NodeUndirected = self.graph.nodes.get(nodeName)
            if nodeConnected.visited is True:
                continue
            self.completeNode(nodeConnected, nodeStart, pathLength + edgeLength)

    def getMinTsp(self):
        self.convertToCompleteUndirectedGraph()
        print("done")


edge1 = Edge("A", "B", 1)
edge2 = Edge("B", "C", 2)
edge3 = Edge("B", "D", 3)
edge4 = Edge("C", "E", 1)

edges = [edge1, edge2, edge3, edge4]

graph = GraphUndirected(edges)
tspSpecial = TspSpecial(graph)
tspSpecial.getMinTsp()
