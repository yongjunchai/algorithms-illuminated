import unittest
from algorithmIlliminated_3.bellmanFord import *

class BellmanFordTest(unittest.TestCase):

    def getTestData_1(self):
        edges = list()
        edges.append(Edge("s", "s", 0))
        edges.append(Edge("s", "v", 4))
        edges.append(Edge("s", "u", 2))
        edges.append(Edge("u", "v", -1))
        edges.append(Edge("u", "w", 2))
        edges.append(Edge("w", "t", 2))
        edges.append(Edge("v", "t", 4))
        graph = Graph(edges)
        data = ("s", graph, [["v", 1, ["s", "u", "v"]],
                        ["u", 2, ["s", "u"]],
                        ["w", 4, ["s", "u", "w"]],
                        ["t", 5, ["s", "u", "v", "t"]]
                        ]
        )
        return data

    def getTestData_2(self):
        edges = list()
        edges.append(Edge("s", "s", 0))
        edges.append(Edge("s", "v", 4))
        edges.append(Edge("s", "u", 2))
        edges.append(Edge("u", "v", 1))
        edges.append(Edge("u", "w", 2))
        edges.append(Edge("w", "t", 2))
        edges.append(Edge("v", "t", 4))
        graph = Graph(edges)
        data = ("s", graph, [["v", 3, ["s", "u", "v"]],
                        ["u", 2, ["s", "u"]],
                        ["w", 4, ["s", "u", "w"]],
                        ["t", 6, ["s", "u", "w", "t"]]
                        ]
        )
        return data

    def getTestData_negative_cycle(self):
        edges = list()
        edges.append(Edge("s", "s", 0))
        edges.append(Edge("s", "v", 4))
        edges.append(Edge("s", "u", 2))
        edges.append(Edge("u", "v", 1))
        edges.append(Edge("u", "w", 2))
        edges.append(Edge("w", "t", 2))
        edges.append(Edge("v", "t", 4))
        edges.append(Edge("v", "w", -10))
        edges.append(Edge("w", "u", -4))
        graph = Graph(edges)
        data = ("s", graph, []
        )
        return data

    def test_findShortestPath(self):

        dataSet = [self.getTestData_1(), self.getTestData_2(), self.getTestData_negative_cycle()]
        bellmanFord = BellmanFord()
        for data in dataSet:
            print("start data set....................")
            s = data[0]
            g = data[1]
            expectedPaths = data[2]
            subProblemsSolution, stableStep = bellmanFord.findShortestPath(s, g)
            if len(expectedPaths) == 0:
                self.assertTrue(subProblemsSolution is None)
                self.assertTrue(stableStep is None)
                print("negative cycle detected")
                continue
            self.assertTrue(subProblemsSolution is not None)
            self.assertTrue(stableStep is not None)
            paths = bellmanFord.constructSolution(s, g, subProblemsSolution, stableStep)
            self.assertTrue(len(expectedPaths) == len(paths))
            for curPath in expectedPaths:
                target = curPath[0]
                targetPath = paths.get(target)
                self.assertTrue(targetPath is not None)
                self.assertTrue(targetPath.length == curPath[1])
                self.assertTrue(targetPath.path == deque(curPath[2]))
            for item in paths.items():
                print("%s --> %s : %s, %s" % (s,  item[0], str(item[1].length), str(item[1].path)))
            print("end data set....................")

if __name__ == '__main__':
    unittest.main()
