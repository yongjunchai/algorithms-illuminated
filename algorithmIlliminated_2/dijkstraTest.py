import unittest
from utils.utils import *
from algorithmIlliminated_2.dijkstra import *


class DijkstraTest(unittest.TestCase):
    def getData1(self):
        edge1: Edge = Edge("s", "v", 1)
        edge2: Edge = Edge("s", "w", 4)
        edge3: Edge = Edge("v", "w", 2)
        edge4: Edge = Edge("v", "t", 6)
        edge5: Edge = Edge("w", "t", 3)

        edges = [edge1, edge2, edge3, edge4, edge5]
        souceVertex = "s"
        dists = dict()
        dists["s"] = 0
        dists["v"] = 1
        dists["w"] = 3
        dists["t"] = 6

        graph = Graph(edges)
        return graph, souceVertex, dists

    def getTestData(self):
        dataSet = [self.getData1()]
        return dataSet

    def test_shortestFastPath(self):
        dijkstra = Dijkstra()
        dataSet = self.getTestData()
        for data in dataSet:
            graph = data[0]
            sourceVertex = data[1]
            dists = data[2]
            dijkstra.search(graph, sourceVertex)
            for item in dists.items():
                vertex = item[0]
                length = item[1]
                node: Node = graph.nodes.get(vertex)
                self.assertTrue(node.dist == length)


if __name__ == '__main__':
    unittest.main()
