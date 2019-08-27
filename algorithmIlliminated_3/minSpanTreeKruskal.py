from collections import defaultdict
from algorithmIlliminated_3.unionfind import *


# A class to represent a graph. A graph
# is the list of the adjacency lists.
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.mst = defaultdict(list)
        self.edges = []

    def add_mstEdge(self, s, v, cost):
        self.mst[s].append((v, cost))
        self.mst[v].append((s, cost))

    def add_edge(self, s, v, cost):
        self.graph[s].append((v, cost))
        self.graph[v].append((s, cost))
        self.edges.append((cost, s, v))

    def buildKruskalMst(self):
        if len(self.edges) < 2 or len(self.graph) < 2:
            return None
        self.edges = sorted(self.edges)
        vertices = []
        for key in self.graph.keys():
            vertices.append(key)
        unionFind = UnionFind(vertices)
        for edge in self.edges:
            i = unionFind.find(edge[1])
            j = unionFind.find(edge[2])
            if i is None or j is None:
                print("Error: failed to find component for (%s, %s)", edge[1], edge[2])
                continue
            if i == j:
                continue
            self.add_mstEdge(edge[1], edge[2], edge[0])
            unionFind.union(edge[1], edge[2])
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

    mst = graph.buildKruskalMst()
    print(mst)
