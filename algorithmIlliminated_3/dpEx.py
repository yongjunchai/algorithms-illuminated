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
        for i in range(len(items) + 1):
            for j in range(c2 + 1):
                for k in range(c1 + 1):
                    c1Val = 0


