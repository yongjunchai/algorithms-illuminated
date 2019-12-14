import unittest
from utils.utils import *
from algorithmIlliminated_2.graphSearch import *
class GraphTestCase(unittest.TestCase):
    def getTestData_2(self):
        edges = list()
        edges.append(Edge("1", "3", 1))
        edges.append(Edge("3", "5", 1))
        edges.append(Edge("5", "1", 1))
        edges.append(Edge("5", "7", 1))
        edges.append(Edge("5", "9", 1))
        edges.append(Edge("7", "9", 1))
        edges.append(Edge("9", "2", 1))
        edges.append(Edge("9", "4", 1))
        edges.append(Edge("4", "7", 1))
        edges.append(Edge("9", "8", 1))
        edges.append(Edge("8", "6", 1))
        edges.append(Edge("6", "10", 1))
        edges.append(Edge("10", "8", 1))
        edges.append(Edge("11", "8", 1))
        edges.append(Edge("11", "6", 1))
        edges.append(Edge("3", "11", 1))
        edges.append(Edge("2", "10", 1))
        edges.append(Edge("2", "4", 1))
        graph = Graph(edges)
        data = [graph, {"1": ["6", "8", "10"], "2": ["11"], "3": ["2", "4", "7", "9"], "4": ["1", "3", "5"]}]
        return data

    def test_sccKosaraju(self):
        graphSearch = GraphSearch()

        testData = self.getTestData_2()
        sccResult = graphSearch.detectSCC_kosaraju(testData[0])
        sccs = testData[1]
        self.assertTrue(len(sccResult) == len(sccs))
        for scc in sccs.items():
            sccR = sccResult.get(scc[0])
            self.assertTrue(sorted(sccR) == sorted(scc[1]))

    def test_sccKosaraju_iterative(self):
        graphSearch = GraphSearch()

        testData = self.getTestData_2()
        sccResult = graphSearch.detectSCC_kosaraju_iterative(testData[0])
        sccs = testData[1]
        self.assertTrue(len(sccResult) == len(sccs))
        for scc in sccs.items():
            sccR = sccResult.get(scc[0])
            self.assertTrue(sorted(sccR) == sorted(scc[1]))


if __name__ == '__main__':
    unittest.main()
