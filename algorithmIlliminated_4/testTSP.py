import unittest

from algorithmIlliminated_4.tsp import *
from utils.utils import *


class MyTestCase(unittest.TestCase):
    def test_TSP(self):
        edge1 = Edge("a", "b", 1)
        edge2 = Edge("b", "a", 1)
        edge3 = Edge("b", "d", 2)
        edge4 = Edge("d", "b", 2)
        edge5 = Edge("d", "c", 6)
        edge6 = Edge("c", "d", 6)
        edge7 = Edge("c", "a", 4)
        edge8 = Edge("a", "c", 4)
        edge9 = Edge("a", "d", 3)
        edge10 = Edge("d", "a", 3)
        edge11 = Edge("b", "c", 5)
        edge12 = Edge("c", "b", 5)
        edges = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12]
        graph = Graph(edges)
        tsp = TSP(graph)
        tsp.solve("a")
        self.assertTrue(tsp.tourLength == 13)
        for edge in tsp.edges.values():
            print(edge.srcNodeName + " --> " + edge.targetNodeName + "  :  " + str(edge.edgeLength))


if __name__ == '__main__':
    unittest.main()
