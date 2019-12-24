from utils.utils import *
from utils.heap import *
import sys


class Dijkstra:
    def __init__(self):
        pass

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
            targetNode.predecessor = predecessor
            targetNode.dist = predecessor.dist + length
            heap.insert(targetNode.dist, (targetNode.name + str(targetNode.dist), targetNode))

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
            if node.visited:
                continue
            node.visited = True
            self.updateHeap(graph, node, heap)
        return graph
