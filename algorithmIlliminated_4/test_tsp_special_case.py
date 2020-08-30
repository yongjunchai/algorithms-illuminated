import unittest
from algorithmIlliminated_4.tsp_special_case import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        edge1 = Edge("A", "B", 1)
        edge2 = Edge("B", "C", 2)
        edge3 = Edge("B", "D", 3)
        edge4 = Edge("C", "E", 1)

        edges = [edge1, edge2, edge3, edge4]

        graph = GraphUndirected(edges)
        tspSpecial = TspSpecial(graph)
        tspSpecial.getMinTsp()
        self.assertTrue(14 == tspSpecial.tourLength)


if __name__ == '__main__':
    unittest.main()
