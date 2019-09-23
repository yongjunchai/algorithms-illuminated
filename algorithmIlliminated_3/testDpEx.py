import unittest
from algorithmIlliminated_3.dpEx import *


class DpExTestCase(unittest.TestCase):
    def test_solveDoubleKnapsack(self):
        dataSet = [(([Item(1, 2, 3), Item(2, 3, 4), Item(3, 4, 2), Item(4, 4, 3)], 5, 6), ({"c1": [3, 4], "c2": [2]})),
                   (([Item(1, 2, 3), Item(2, 3, 4), Item(3, 4, 4), Item(4, 4, 3)], 2, 100), ({"c1": [], "c2": [1, 2, 3, 4]})),
                   (([Item(1, 2, 7), Item(2, 3, 18), Item(3, 4, 100), Item(4, 4, 101)], 25, 201), ({"c1": [1, 2], "c2": [3, 4]})),
                    (([Item(1, 2, 7), Item(2, 3, 18), Item(3, 4, 100), Item(4, 4, 101), Item(5, 4, 30)], 201, 55), ({"c1": [3, 4], "c2": [1, 2, 5]})),
                   (([Item(1, 2, 7), Item(2, 3, 18), Item(3, 4, 100)], 106, 30), ({"c1": [3], "c2": [1, 2]})),

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

if __name__ == '__main__':
    unittest.main()

