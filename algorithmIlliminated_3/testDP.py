import unittest
from algorithmIlliminated_3.dp import *


class TestDP(unittest.TestCase):
    def test_wis(self):
        dp = DP()
        testData = [([1, 4, 5, 4], [4, 4]),
                    ([8, 10, 11, 9, 8], [8, 11, 8]),
                    ([8, 10, 16, 9, 8, 1999, 19, 10], [8, 16, 1999, 10])
                    ]
        for item in testData:
            values = item[0]
            dqWisNodes = dp.wis_divide_and_conquer(values)
            dqWisNodes = sorted(dqWisNodes, key=lambda x: x.index)

            dpRecWisNodes = dp.wis_dp_recursive(values)
            dpRecWisNodes = sorted(dpRecWisNodes, key=lambda x: x.index)

            dpRecCacheSubProblemSolutions = dp.wis_dp_recursive_cache(values)
            dpRecCacheNodes = dp.wis_dp_construct_solution(dpRecCacheSubProblemSolutions, values)
            dpRecCacheNodes = sorted(dpRecCacheNodes, key=lambda x: x.index)

            dpRecIterativeSubProblemSolutions = dp.wis_dp_iterative(values)
            dpIterativeCacheNodes = dp.wis_dp_construct_solution(dpRecIterativeSubProblemSolutions, values)
            dpIterativeCacheNodes = sorted(dpIterativeCacheNodes, key=lambda x: x.index)

            exp = item[1]
            self.assertTrue(len(exp) == len(dqWisNodes))
            self.assertTrue(len(exp) == len(dpRecWisNodes))
            self.assertTrue(len(exp) == len(dpRecCacheNodes))
            self.assertTrue(len(exp) == len(dpIterativeCacheNodes))
            for i in range(0, len(exp)):
                self.assertTrue(exp[i] == dqWisNodes[i].value)
                self.assertTrue(exp[i] == dpRecWisNodes[i].value)
                self.assertTrue(exp[i] == dpRecCacheNodes[i].value)
                self.assertTrue(exp[i] == dpIterativeCacheNodes[i].value)

    def test_knapsack(self):
        testData = [((6, [Item(1, 3, 4), Item(2, 2, 3), Item(3, 4, 2), Item(4, 4, 3)]), [Item(3, 4, 2), Item(4, 4, 3)]),
                    ((1, [Item(1, 3, 4), Item(2, 2, 3), Item(3, 4, 2), Item(4, 4, 3)]), []),
                    ((100, [Item(1, 3, 4), Item(2, 2, 3), Item(3, 4, 2), Item(4, 4, 3)]), [Item(1, 3, 4), Item(2, 2, 3), Item(3, 4, 2), Item(4, 4, 3)])
                    ]

        for data in testData:
            knapsack = Knapsack(data[0][0], data[0][1])
            expected = data[1]
            dp = DP()
            subProblemSolutions = dp.solveKnapsackProblem(knapsack)
            solution = dp.constructKnapsackSolution(subProblemSolutions, knapsack)
            self.assertTrue(len(expected) == len(solution))
            for i in range(0, len(expected)):
                self.assertTrue(expected[i].index == solution[i].index)
                self.assertTrue(expected[i].size == solution[i].size)
                self.assertTrue(expected[i].value == solution[i].value)

    def test_dumpSolution(self):
        knapsack = Knapsack(9, [Item(1, 1, 1), Item(2, 2, 3), Item(3, 3, 2), Item(4, 4, 5), Item(5, 5, 4)])
        dp = DP()
        subProblemSolutions = dp.solveKnapsackProblem(knapsack)
        print(subProblemSolutions)

if __name__ == '__main__':
   unittest.main()
