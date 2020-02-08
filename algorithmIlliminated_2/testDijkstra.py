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
        dists["s"] = Path(0, ["s"])
        dists["v"] = Path(1, ["s", "v"])
        dists["w"] = Path(3, ["s", "v", "w"])
        dists["t"] = Path(6, ["s", "v", "w", "t"])

        graph = Graph(edges)
        return graph, souceVertex, dists

    def getData2(self):
        edge1: Edge = Edge("s", "v", 1)
        edge2: Edge = Edge("s", "x", 100)
        edge3: Edge = Edge("s", "w", 4)
        edge4: Edge = Edge("v", "w", 2)
        edge5: Edge = Edge("v", "x", 15)
        edge6: Edge = Edge("v", "t", 6)
        edge7: Edge = Edge("w", "t", 3)
        edge8: Edge = Edge("t", "x", 2)
        edge9: Edge = Edge("x", "s", 2)

        edges = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9]
        souceVertex = "s"
        dists = dict()
        dists["s"] = Path(0, ["s"])
        dists["v"] = Path(1, ["s", "v"])
        dists["w"] = Path(3, ["s", "v", "w"])
        dists["t"] = Path(6, ["s", "v", "w", "t"])
        dists["x"] = Path(8, ["s", "v", "w", "t", "x"])

        graph = Graph(edges)
        return graph, souceVertex, dists

    def getData3(self):
        edge1: Edge = Edge("s", "v", 1)
        edge2: Edge = Edge("s", "x", 100)
        edge3: Edge = Edge("s", "w", 4)
        edge4: Edge = Edge("v", "w", 2)
        edge5: Edge = Edge("v", "x", 15)
        edge6: Edge = Edge("v", "t", 6)
        edge7: Edge = Edge("w", "t", 3)
        edge8: Edge = Edge("w", "x", 3)
        edge9: Edge = Edge("t", "x", 2)
        edge10: Edge = Edge("x", "s", 2)

        edges = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10]
        souceVertex = "s"
        dists = dict()
        dists["s"] = Path(0, ["s"])
        dists["v"] = Path(1, ["s", "v"])
        dists["w"] = Path(3, ["s", "v", "w"])
        dists["t"] = Path(6, ["s", "v", "w", "t"])
        dists["x"] = Path(6, ["s", "v", "w", "x"])

        graph = Graph(edges)
        return graph, souceVertex, dists

    def getTestData(self):
        dataSet = [self.getData1(), self.getData2(), self.getData3()]
        return dataSet

    def getMaxEdgeData1(self):
        edge1: Edge = Edge("s", "v", 2)
        edge2: Edge = Edge("s", "w", 4)
        edge3: Edge = Edge("v", "w", 3)
        edge4: Edge = Edge("v", "t", 5)
        edge5: Edge = Edge("w", "t", 3)

        edges = [edge1, edge2, edge3, edge4, edge5]
        souceVertex = "s"
        dists = dict()
        dists["s"] = Path(0, ["s"])
        dists["v"] = Path(2, ["s", "v"])
        dists["w"] = Path(3, ["s", "v", "w"])
        dists["t"] = Path(3, ["s", "v", "w", "t"])

        graph = Graph(edges)
        return graph, souceVertex, dists

    def getMaxEdgeData2(self):
        edge1: Edge = Edge("s", "v", 2)
        edge2: Edge = Edge("s", "w", 4)
        edge3: Edge = Edge("v", "w", 3)
        edge4: Edge = Edge("v", "t", 5)
        edge5: Edge = Edge("w", "t", 3)
        edge6: Edge = Edge("v", "x", 4)
        edge7: Edge = Edge("t", "x", 1)
        edge8: Edge = Edge("s", "x", 4)

        edges = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8]
        souceVertex = "s"
        dists = dict()
        dists["s"] = Path(0, ["s"])
        dists["v"] = Path(2, ["s", "v"])
        dists["w"] = Path(3, ["s", "v", "w"])
        dists["t"] = Path(3, ["s", "v", "w", "t"])
        dists["x"] = Path(3, ["s", "v", "w", "t", "x"])

        graph = Graph(edges)
        return graph, souceVertex, dists

    def getMaxEdgeData3(self):
        edge1: Edge = Edge("s", "v", 2)
        edge2: Edge = Edge("s", "w", 4)
        edge3: Edge = Edge("v", "w", 100)
        edge4: Edge = Edge("v", "t", 100)
        edge5: Edge = Edge("w", "t", 3)
        edge6: Edge = Edge("v", "x", 6)
        edge7: Edge = Edge("t", "x", 1)
        edge8: Edge = Edge("s", "x", 100)

        edges = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8]
        souceVertex = "s"
        dists = dict()
        dists["s"] = Path(0, ["s"])
        dists["v"] = Path(2, ["s", "v"])
        dists["w"] = Path(4, ["s", "w"])
        dists["t"] = Path(4, ["s", "w", "t"])
        dists["x"] = Path(4, ["s", "w", "t", "x"])

        graph = Graph(edges)
        return graph, souceVertex, dists

    def getMaxEdgeTestData(self):
        dataSet = [self.getMaxEdgeData1(), self.getMaxEdgeData2(), self.getMaxEdgeData3()]
        return dataSet

    def verifyPah(self, path: deque, node: Node):
        vertex = path.pop()
        self.assertTrue(vertex == node.name)
        if node.predecessor is None:
            self.assertTrue(len(path) == 0)
        else:
            self.verifyPah(path, node.predecessor)

    def test_shortestFastPath(self):
        dijkstra = Dijkstra()
        dataSet = self.getTestData()
        for data in dataSet:
            graph = data[0]
            sourceVertex = data[1]
            dists = data[2]
            dijkstra.search(graph, sourceVertex)
            self.assertTrue(len(dists) == len(graph.nodes))
            for item in dists.items():
                vertex = item[0]
                path = item[1]
                node: Node = graph.nodes.get(vertex)
                self.assertTrue(node.dist == path.length)
                self.verifyPah(path.path, node)

    def test_minimumMaximumEdgeOnPath(self):
        dijkstra = Dijkstra()
        dataSet = self.getMaxEdgeTestData()
        for data in dataSet:
            graph = data[0]
            sourceVertex = data[1]
            dists = data[2]
            dijkstra.searchMaxEdge(graph, sourceVertex)
            self.assertTrue(len(dists) == len(graph.nodes))
            for item in dists.items():
                vertex = item[0]
                path = item[1]
                node: Node = graph.nodes.get(vertex)
                self.assertTrue(node.dist == path.length)
                self.verifyPah(path.path, node)


if __name__ == '__main__':
    unittest.main()
