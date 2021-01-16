import unittest
from algorithmIlliminated_4.color_coding import *
from utils.utils import *


class MyTestCase(unittest.TestCase):

    def createGraph_21_5(self):
        edge1 = Edge("a", "c", 1)
        edge2 = Edge("c", "e", 7)
        edge3 = Edge("e", "g", 9)
        edge4 = Edge("b", "d", 4)
        edge5 = Edge("d", "f", 3)
        edge6 = Edge("f", "h", 10)
        edge7 = Edge("a", "f", 2)
        edge8 = Edge("c", "h", 8)
        edge9 = Edge("b", "e", 6)
        edge10 = Edge("d", "g", 5)
        edges = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10]
        edges = completeEdge(edges)
        return edges

    def test_problem_21_5(self):
        edges = self.createGraph_21_5()
        graph = Graph(edges)
        for item in graph.nodes.values():
            node: Node = item
            if node.name == "a" or node.name == "b":
                node.color = 0
            elif node.name == "c" or node.name == "d":
                node.color = 1
            elif node.name == "e" or node.name == "f":
                node.color = 2
            else:
                node.color = 3
        panchromaticPath = PanchromaticPath(graph)
        length = panchromaticPath.run(4)
        self.assertTrue(length == 10)

    def test_color_coding(self):
        edges = self.createGraph_21_5()
        graph = Graph(edges)
        colorCoding = ColorCoding(graph)
        length = colorCoding.run(4, 0.0001)
        self.assertTrue(length == 6)
        length = colorCoding.run(5, 0.0001)
        self.assertTrue(length == 10)


if __name__ == '__main__':
    unittest.main()
