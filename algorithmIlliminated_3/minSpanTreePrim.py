"""
A Python program to demonstrate the adjacency
list representation of the graph
"""
# A class to represent the adjacency list of the node
from collections import defaultdict
import sys
from algorithmIlliminated_3.heap import *


class Node:
    def __init__(self, vertex):
        self.vertex = vertex
        self.winner = (None, sys.maxsize)
        self.edges = None


# A class to represent a graph. A graph
# is the list of the adjacency lists.
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.mst = defaultdict(list)

    def add_mstEdge(self, s, v, cost):
        self.mst[s].append((v, cost))
        self.mst[v].append((s, cost))

    def add_edge(self, s, v, cost):
        self.graph[s].append((v, cost))
        self.graph[v].append((s, cost))

    def buildPrimMST(self):
        if len(self.graph) <= 1:
            return
        processedVertexs = set()
        heap = Heap()
        start = self.graph.popitem()
        processedVertexs.add(start[0])
        # initialize the heap with cost to the start node
        for vertex, edges in self.graph.items():
            node = None
            for edge in edges:
                if edge[0] == start[0]:
                    node = Node(vertex)
                    node.winner = edge
                    assert(node.winner[0] == start[0])
            if node is None:
                node = Node(vertex)
            node.edges = edges
            heap.insert(node.winner[1], (node.vertex, node))

        while heap.size() > 0:
            key, value = heap.extractMin()
            cost, node = key, value[1]
            self.add_mstEdge(node.vertex, node.winner[0], node.winner[1])
            processedVertexs.add(node.vertex)
            for edge in node.edges:
                if edge[0] not in processedVertexs:
                    if edge[1] < heap.getKey(edge[0]):
                        value = heap.getValue(edge[0])
                        value[1].winner = (node.vertex, edge[1])
                        heap.update(value, edge[1])
        return self.mst


# Driver program to the above graph class
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge("a", "b", 1)
    graph.add_edge("a", "d", 3)
    graph.add_edge("a", "c", 4)
    graph.add_edge("b", "d", 2)
    graph.add_edge("d", "c", 5)
    graph.add_edge("c", "e", 4)
    graph.add_edge("e", "d", 7)

    mst = graph.buildPrimMST()
    print(mst)

