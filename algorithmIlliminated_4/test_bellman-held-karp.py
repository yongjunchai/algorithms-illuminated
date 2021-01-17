import unittest
from algorithmIlliminated_4.bellman_held_karp import *


class MyTestCase(unittest.TestCase):
    def get_graph_quiz_20_7(self):
        edge1 = Edge("a", "b", 1)
        edge2 = Edge("b", "a", 1)
        edge3 = Edge("b", "c", 2)
        edge4 = Edge("c", "b", 2)
        edge5 = Edge("d", "c", 7)
        edge6 = Edge("c", "d", 7)
        edge7 = Edge("e", "d", 9)
        edge8 = Edge("d", "e", 9)
        edge9 = Edge("a", "e", 10)
        edge10 = Edge("e", "a", 10)
        edge11 = Edge("a", "c", 4)
        edge12 = Edge("c", "a", 4)
        edge13 = Edge("c", "e", 8)
        edge14 = Edge("e", "c", 8)
        edge15 = Edge("b", "e", 3)
        edge16 = Edge("e", "b", 3)
        edge17 = Edge("b", "d", 6)
        edge18 = Edge("d", "b", 6)
        edge19 = Edge("a", "d", 5)
        edge20 = Edge("d", "a", 5)
        edges = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12,
                 edge13, edge14, edge15, edge16, edge17, edge18, edge19, edge20]
        graph = Graph(edges)
        return graph

    def test_something(self):
        graph = self.get_graph_quiz_20_7()
        bellManHeldKarp = BellmanHeldKarp(graph)
        tourLength = bellManHeldKarp.run()
        self.assertTrue(23 == tourLength)


if __name__ == '__main__':
    unittest.main()
