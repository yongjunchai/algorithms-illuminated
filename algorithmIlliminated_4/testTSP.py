import unittest

from algorithmIlliminated_4.tsp import *
from utils.utils import *


class MyTestCase(unittest.TestCase):
    def test_TSP_4_vertices(self):
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
        print("shortest tour: ")
        tsp.dumpTour(tsp.edges.values())

    def test_TSP_5_vertices(self):
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
        edge13 = Edge("a", "e", 5)
        edge14 = Edge("e", "a", 5)
        edge15 = Edge("b", "e", 5)
        edge16 = Edge("e", "b", 5)
        edge17 = Edge("c", "e", 5)
        edge18 = Edge("e", "c", 5)
        edge19 = Edge("d", "e", 5)
        edge20 = Edge("e", "d", 5)

        edges = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12,
                 edge13, edge14, edge15, edge16, edge17, edge18, edge19, edge20]
        graph = Graph(edges)
        tsp = TSP(graph)
        tsp.solve("a")
        self.assertTrue(tsp.tourLength == 17)
        print("shortest tour: ")
        tsp.dumpTour(tsp.edges.values())

    def test_TSP_5_vertices_quiz_20_7(self):
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
        tsp = TSP(graph)
        tsp.solve("a")
        print("shortest tour: ")
        tsp.dumpTour(tsp.edges.values())

    def extractEdges(self, graph: GraphUndirected):
        edgeDict = dict()
        edges = list()
        for node in graph.nodes.values():
            for name, length in node.connectedEdges.items():
                edge1 = Edge(node.name, name, length)
                edge2 = Edge(name, node.name, length)
                edgeDict[edge1.getEdgeKey()] = edge1
                edgeDict[edge2.getEdgeKey()] = edge2
            for name, length in node.extConnectedEdges.items():
                edge1 = Edge(node.name, name, length)
                edge2 = Edge(name, node.name, length)
                edgeDict[edge1.getEdgeKey()] = edge1
                edgeDict[edge2.getEdgeKey()] = edge2
        for edge in edgeDict.values():
            edges.append(edge)
        return edges

    def test_tsp_special_case(self):
        edge1 = Edge("A", "B", 1)
        edge2 = Edge("B", "C", 2)
        edge3 = Edge("B", "D", 3)
        edge4 = Edge("C", "E", 1)

        edges = [edge1, edge2, edge3, edge4]
        graphUndirected = GraphUndirected(edges)
        graphUndirected.convertToCompleteUndirectedGraph()
        graph = Graph(self.extractEdges(graphUndirected))
        tsp = TSP(graph)
        tsp.solve("A")
        print("shortest tour: ")
        tsp.dumpTour(tsp.edges.values())

    def test_tsp_special_case_4_vertices(self):
        edge1 = Edge("A", "B", 1)
        edge2 = Edge("B", "C", 2)
        edge3 = Edge("B", "D", 3)
        edges = [edge1, edge2, edge3]
        graphUndirected = GraphUndirected(edges)
        graphUndirected.convertToCompleteUndirectedGraph()
        graph = Graph(self.extractEdges(graphUndirected))
        tsp = TSP(graph)
        tsp.solve("A")
        print("shortest tour: ")
        tsp.dumpTour(tsp.edges.values())


if __name__ == '__main__':
    unittest.main()
