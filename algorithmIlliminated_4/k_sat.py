
from utils.utils import *


class TwoColorability():
    def __init__(self, graph: Graph):
        self.graph = graph

    def getNeighborNodesColors(self, node: Node):
        colors = 0
        for key in node.outflowEdges:
            targetNode: Node = key
            colors |= targetNode.color
        return colors

    def isTwoColorable(self, node: Node):
        if node.visited:
            return True
        colors = self.getNeighborNodesColors(node)
        if colors == 3:
            return False
        node.color = 3 & ~colors
        node.visited = True
        for key in node.outflowEdges:
            targetNode: Node = self.graph.nodes[key]
            if targetNode.visited:
                continue
            if not self.isTwoColorable(targetNode):
                return False
        return True

    def isTwoColorable(self):
        # clear color of all nodes
        for node in self.graph.nodes.values():
            node.color = 0

        for node in self.graph.nodes.values():
            if node.visited:
                continue
            if not self.isTwoColorable(node):
                print("graph is not two colorable")
                return False
        print("graph is two colorable")
        return True


