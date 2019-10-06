import unittest
from algorithmIlliminated_3.dpEx import *


class DpExTestCase(unittest.TestCase):
    def test_solveDoubleKnapsack(self):
        dataSet = [(([Item(1, 2, 3), Item(2, 3, 4), Item(3, 4, 2), Item(4, 4, 3)], 5, 4), ({"c1": [3, 4], "c2": [2]})),
                  (([Item(1, 2, 3), Item(2, 3, 4), Item(3, 4, 4), Item(4, 4, 3)], 2, 100), ({"c1": [], "c2": [1, 2, 3, 4]})),
                   (([Item(1, 2, 7), Item(2, 3, 18), Item(3, 4, 100), Item(4, 4, 101)], 25, 201), ({"c1": [1, 2], "c2": [3, 4]})),
                    (([Item(1, 2, 7), Item(2, 3, 18), Item(3, 4, 100), Item(4, 4, 101), Item(5, 4, 30)], 201, 55), ({"c1": [3, 4], "c2": [1, 2, 5]})),
                   (([Item(1, 2, 7), Item(2, 3, 18), Item(3, 4, 100)], 106, 30), ({"c1": [3], "c2": [1, 2]})),
                   (([Item(1, 20, 7), Item(2, 3, 3), Item(3, 4, 8), Item(4, 1, 3), Item(5, 2, 2)], 9, 12), ({"c1": [3], "c2": [1, 2, 5]}))
                   ]
        for data in dataSet:
            expected = data[1]
            items = data[0][0]
            c1 = data[0][1]
            c2 = data[0][2]
            dpEx = DpEx()
            subProblemSolutions = dpEx.solveDoubleKnapsack(c1, c2, items)
            solution = dpEx.constructDoubleKnapsackSolution(c1, c2, items, subProblemSolutions)
            results = dict()
            for i in solution:
                bagName = i[0]
                item = i[1]
                if results.get(bagName) is None:
                    results[bagName] = list()
                results[bagName].append(item.index)
            for bagName in results:
                results[bagName] = sorted(results[bagName])
            print(results)
            for bagName in results:
                assert(expected[bagName] == results[bagName])

    def test_solveMultiplesKnapsacks_2Knapsacks(self):
        dataSet = [
            (([Item(1, 2, 3), Item(2, 3, 4), Item(3, 4, 2), Item(4, 4, 3)], 5, 4), ({"1": [3, 4], "2": [2]})),
                   (([Item(1, 2, 3), Item(2, 3, 4), Item(3, 4, 4), Item(4, 4, 3)], 2, 100),
                    ({"1": [], "2": [1, 2, 3, 4]})),
                   (([Item(1, 2, 7), Item(2, 3, 18), Item(3, 4, 100), Item(4, 4, 101)], 25, 201),
                    ({"1": [1, 2], "2": [3, 4]})),
                   (([Item(1, 2, 7), Item(2, 3, 18), Item(3, 4, 100), Item(4, 4, 101), Item(5, 4, 30)], 201, 55),
                    ({"1": [3, 4], "2": [1, 2, 5]})),
                   (([Item(1, 2, 7), Item(2, 3, 18), Item(3, 4, 100)], 106, 30), ({"1": [3], "2": [1, 2]})),
                   (([Item(1, 20, 7), Item(2, 3, 3), Item(3, 4, 8), Item(4, 1, 3), Item(5, 2, 2)], 8, 12),
                    ({"1": [3], "2": [1, 2, 5]}))
        ]
        for data in dataSet:
            expected = data[1]
            items = data[0][0]
            c1 = data[0][1]
            c2 = data[0][2]
            dpEx = DpEx()
            subProblemSolutions = dpEx.solveKnapsacks([c1, c2], items)
            solution = dpEx.constructKnapsacksSolution(subProblemSolutions, [c1, c2], items)
            results = dict()
            for i in solution:
                bagName = i[0]
                item = i[1]
                if results.get(bagName) is None:
                    results[bagName] = list()
                results[bagName].append(item.index)
            for bagName in results:
                results[bagName] = sorted(results[bagName])
            print(results)
            for bagName in results:
                assert(expected[bagName] == results[bagName])

    def test_solveMultiplesKnapsacks_3Knapsacks(self):
        dataSet = [
                   (([Item(1, 4, 3), Item(2, 4, 4), Item(3, 5, 6), Item(4, 1, 9), Item(5, 12, 7), Item(6, 2, 5) ], 8, 9, 4),
                    ({"1": [5], "2": [1, 3], "3": [2]}))
        ]
        for data in dataSet:
            expected = data[1]
            items = data[0][0]
            c1 = data[0][1]
            c2 = data[0][2]
            c3 = data[0][3]
            dpEx = DpEx()
            subProblemSolutions = dpEx.solveKnapsacks([c1, c2, c3], items)
            solution = dpEx.constructKnapsacksSolution(subProblemSolutions, [c1, c2, c3], items)
            results = dict()
            for i in solution:
                bagName = i[0]
                item = i[1]
                if results.get(bagName) is None:
                    results[bagName] = list()
                results[bagName].append(item.index)
            for bagName in results:
                results[bagName] = sorted(results[bagName])
            print(results)
            for bagName in results:
                assert(expected[bagName] == results[bagName])

    def test_solveBudgetKnapsack(self):
        dataSet = [
                   (([Item(1, 10, 3), Item(2, 4, 4), Item(3, 5, 6), Item(4, 1, 9), Item(5, 12, 7), Item(6, 2, 5) ], 2, 9),
                    [1, 3]),
            (([Item(1, 10, 3), Item(2, 4, 4), Item(3, 5, 6), Item(4, 1, 9), Item(5, 12, 7), Item(6, 2, 5)], 1, 9),
             [5]),
            (([Item(1, 10, 3), Item(2, 4, 4), Item(3, 5, 6), Item(4, 1, 9), Item(5, 12, 7), Item(6, 2, 5)], 3, 90),
             [1, 3, 5]),

        ]
        for data in dataSet:
            expected = data[1]
            items = data[0][0]
            budget = data[0][1]
            c1 = data[0][2]
            dpEx = DpEx()
            subProblemSolutions = dpEx.solveKnapsacksBudget(c1, budget, items)
            solution = dpEx.constructKnapsackBudgetSolution(c1, budget, items, subProblemSolutions)
            results = sorted(solution)
            self.assertTrue(expected == results)

if __name__ == '__main__':
    unittest.main()

