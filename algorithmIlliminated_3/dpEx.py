
class Item:
    def __init__(self, index: int, value: int, size: int):
        assert (type(size) is int and size > 0)
        assert (type(value) is int and value > 0)
        assert (type(index) is int and index >= 0)
        self.value = value
        self.size = size
        self.index = index


class Knapsack:
    def __init__(self, capacity: int):
        assert (type(capacity) is int and capacity > 0)
        self.capacity = capacity
        self.items = list()


class DpEx:
    def __init__(self):
        pass

    def constructDoubleKnapsackSolution(self, c1, c2, items, subProblemSolutions):
        assert(type(c1) is int)
        assert(type(c2) is int)
        assert(type(items) is list)
        assert(type(subProblemSolutions) is list)
        ascii(len(subProblemSolutions) == len(items) + 1)
        ascii(len(subProblemSolutions[0]) == c2 + 1)
        ascii(len(subProblemSolutions[0][0]) == c1 + 1)
        solution = list()
        i = len(items)
        j = c2
        k = c1
        while i > 0:
            if subProblemSolutions[i][j][k] <= subProblemSolutions[i - 1][j][k]:
                i = i - 1
                continue
            c1Val = -1
            c2Val = -1
            if items[i - 1].size <= k:
                c1Val = subProblemSolutions[i - 1][j][k - items[i - 1].size] + items[i - 1].value
            if items[i - 1].size <= j:
                c2Val = subProblemSolutions[i - 1][j - items[i - 1].size][k] + items[i - 1].value
            if c1Val >= subProblemSolutions[i][j][k]:
                k = k - items[i - 1].size
                solution.append(("c1", items[i - 1]))
            elif c2Val >= subProblemSolutions[i][j][k]:
                j = j - items[i - 1].size
                solution.append(("c2", items[i - 1]))
            else:
                assert(False)
            i = i - 1
        return solution

    def solveDoubleKnapsack(self, c1, c2, items: list):
        assert(type(c1) is int)
        assert(type(c2) is int)
        assert(type(items) is list)
        subProblemSolutions = [[[None for i in range(c1 + 1)] for j in range(c2 + 1)] for k in range(len(items) + 1)]
        for i in range(c2 + 1):
            for j in range(c1 + 1):
                subProblemSolutions[0][i][j] = 0
        for i in range(len(items) + 1):
            subProblemSolutions[i][0][0] = 0
        for i in range(1, len(items) + 1):
            for j in range(c2 + 1):
                for k in range(c1 + 1):
                    c1Val = -1
                    c2Val = -1
                    if items[i - 1].size <= k:
                        c1Val = subProblemSolutions[i - 1][j][k - items[i - 1].size] + items[i - 1].value
                    if items[i - 1].size <= j:
                        c2Val = subProblemSolutions[i - 1][j - items[i - 1].size][k] + items[i - 1].value
                    c3Val = subProblemSolutions[i - 1][j][k]
                    if c2Val <= c1Val and c3Val <= c1Val:
                        subProblemSolutions[i][j][k] = c1Val
                    elif c3Val <= c2Val and c1Val <= c2Val:
                        subProblemSolutions[i][j][k] = c2Val
                    else:
                        subProblemSolutions[i][j][k] = c3Val
        return subProblemSolutions




