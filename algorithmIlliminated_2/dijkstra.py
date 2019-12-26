from utils.utils import *
from utils.heap import *
import sys


class Dijkstra:
    def __init__(self):
        self.cnt = 0

    def updateHeap(self, graph: Graph, predecessor: Node, heap: Heap):
        for edgeItem in predecessor.outflowEdges.items():
            name = edgeItem[0]
            length = edgeItem[1]
            targetNode = graph.nodes.get(name)
            if targetNode is None:
                print("error %d" % get_linenumber())
                continue
            if targetNode.visited:
                continue
            self.cnt = self.cnt + 1
            heap.insert(predecessor.dist + length, (targetNode.name + str(self.cnt), targetNode, predecessor))

    def updateHeapMaxEdge(self, graph: Graph, predecessor: Node, heap: Heap):
        for edgeItem in predecessor.outflowEdges.items():
            name = edgeItem[0]
            length = edgeItem[1]
            targetNode = graph.nodes.get(name)
            if targetNode is None:
                print("error %d" % get_linenumber())
                continue
            if targetNode.visited:
                continue
            self.cnt = self.cnt + 1
            maxEdge = predecessor.dist
            if maxEdge < length:
                maxEdge = length
            heap.insert(maxEdge, (targetNode.name + str(self.cnt), targetNode, predecessor))

    def search(self, graph: Graph, vertexName: str):
        """
        use dijkstra algorithm to find shortest path to source node
        :param graph:
        :param vertexName: the source vertex name
        :return: updated Graph with info annotate on the nodes
        """
        sourceNode: Node = graph.nodes.get(vertexName)
        if sourceNode is None:
            print("there is no source vertex %d" % get_linenumber())
            return None
        # initialization
        for node in graph.nodes.values():
            node.dist = sys.maxsize
            node.visited = False

        sourceNode.dist = 0
        sourceNode.visited = True

        heap = Heap()
        self.updateHeap(graph, sourceNode, heap)
        while heap.size() > 0:
            key, value = heap.extractMin()
            node: Node = value[1]
            predecessor = value[2]
            if node.visited:
                continue
            node.visited = True
            node.dist = key
            node.predecessor = predecessor
            self.updateHeap(graph, node, heap)
        return graph

    def searchMaxEdge(self, graph: Graph, vertexName: str):
        """
        Problem 9.7
        use dijkstra algorithm to find path that include the minimum maximum-edge
        :param graph:
        :param vertexName: the source vertex name
        :return: updated Graph with info annotate on the nodes
        """
        sourceNode: Node = graph.nodes.get(vertexName)
        if sourceNode is None:
            print("there is no source vertex %d" % get_linenumber())
            return None
        # initialization
        for node in graph.nodes.values():
            node.dist = sys.maxsize
            node.visited = False

        sourceNode.dist = 0
        sourceNode.visited = True

        heap = Heap()
        self.updateHeapMaxEdge(graph, sourceNode, heap)
        while heap.size() > 0:
            key, value = heap.extractMin()
            node: Node = value[1]
            predecessor = value[2]
            if node.visited:
                continue
            node.visited = True
            node.dist = key
            node.predecessor = predecessor
            self.updateHeapMaxEdge(graph, node, heap)
        return graph
