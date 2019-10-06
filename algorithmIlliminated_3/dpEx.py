from algorithmIlliminated_3.utils import *


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

    def constructDoubleKnapsackSolution(self, c1: int, c2: int, items: list, subProblemSolutions: list):
        assert(type(c1) is int)
        assert(type(c2) is int)
        assert(type(items) is list)
        assert(type(subProblemSolutions) is list)
        assert (len(subProblemSolutions) == len(items) + 1)
        assert (len(subProblemSolutions[0]) == c1 + 1)
        assert (len(subProblemSolutions[0][0]) == c2 + 1)
        solution = list()
        i = len(items)
        j = c1
        k = c2
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
                solution.append(("c2", items[i - 1]))
            elif c2Val >= subProblemSolutions[i][j][k]:
                j = j - items[i - 1].size
                solution.append(("c1", items[i - 1]))
            else:
                assert(False)
            i = i - 1
        return solution

    def solveDoubleKnapsack(self, c1, c2, items: list):
        assert(type(c1) is int)
        assert(type(c2) is int)
        assert(type(items) is list)
        subProblemSolutions = Utils.createArray([len(items) + 1, c1 + 1, c2 + 1])
        for i in range(c1 + 1):
            for j in range(c2 + 1):
                subProblemSolutions[0][i][j] = 0
        for i in range(len(items) + 1):
            subProblemSolutions[i][0][0] = 0
        for i in range(1, len(items) + 1):
            for j in range(c1 + 1):
                for k in range(c2 + 1):
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

    def pickKnapsack(self, subProblemSolutions, indices: list, items: list, dimensions: int):
        result = [-1 for i in range(dimensions)]
        for i in range(1, dimensions):
            if indices[i] < items[indices[0] - 1].size:
                continue
            copiedIndices = indices.copy()
            copiedIndices[i] = copiedIndices[i] - items[indices[0] - 1].size
            copiedIndices[0] = copiedIndices[0] - 1
            value = Utils.getValue(subProblemSolutions, copiedIndices) + items[indices[0] - 1].value
            result[i] = value
        pickedValue = -1
        pickedIndex = -1
        for i in range(len(result)):
            if result[i] > pickedValue:
                pickedValue = result[i]
                pickedIndex = i
        return pickedIndex

    def solveKnapsacks_internal(self, subProblemSolutions, indices: list, items: list, dimensions: int):
        if len(indices) < dimensions:
            slot = Utils.getValue(subProblemSolutions, indices)
            for i in range(len(slot)):
                indicesCopied = indices.copy()
                indicesCopied.append(i)
                self.solveKnapsacks_internal(subProblemSolutions, indicesCopied, items, dimensions)
        else:
            i = self.pickKnapsack(subProblemSolutions, indices, items, dimensions)
            if i < 1:
                # items[indices[0]] was not picked up in any knapsack
                copiedIndices = indices.copy()
                copiedIndices[0] = copiedIndices[0] - 1
                Utils.updateValue(subProblemSolutions, indices, Utils.getValue(subProblemSolutions, copiedIndices))
            else:
                copiedIndices = indices.copy()
                copiedIndices[0] = copiedIndices[0] - 1
                preVal = Utils.getValue(subProblemSolutions, copiedIndices)

                copiedIndices = indices.copy()
                copiedIndices[i] = copiedIndices[i] - items[indices[0] - 1].size
                copiedIndices[0] = copiedIndices[0] - 1
                value = Utils.getValue(subProblemSolutions, copiedIndices) + items[indices[0] - 1].value
                if preVal > value:
                    Utils.updateValue(subProblemSolutions, indices, preVal)
                else:
                    Utils.updateValue(subProblemSolutions, indices, value)

    def solveKnapsacks(self, knapsacks: list, items: list):
        """
        :param knapsacks: a list of knapsacks. The value of each knapsack is the capacity of the knapsack.
        :param items: the items to be distributed into the knapsacks. each item has fields: index, value, size
        :return: the solution to sub problems
        """
        for i in range(len(knapsacks)):
            knapsacks[i] = knapsacks[i] + 1
        dimensions = [len(items) + 1]
        dimensions.extend(knapsacks)
        subProblemSolutions = Utils.createArray(dimensions)
        Utils.updateValue(subProblemSolutions, [0], 0)
        for i in range(1, len(items) + 1):
            self.solveKnapsacks_internal(subProblemSolutions, [i], items, len(knapsacks) + 1)
        return subProblemSolutions

    def constructKnapsacksSolution(self, subProblemSolutions, knapsacks: list, items: list):
        indices = [len(items)]
        indices.extend(knapsacks)
        i = len(items)
        solution = list()
        while i > 0:
            indices[0] = i
            copiedIndices = indices.copy()
            copiedIndices[0] = copiedIndices[0] - 1
            if Utils.getValue(subProblemSolutions, indices) <= Utils.getValue(subProblemSolutions, copiedIndices):
                # item[indices[0]] was not picked up in any knapsack
                i = i - 1
                continue
            j = self.pickKnapsack(subProblemSolutions, indices, items, len(indices))
            assert(j > 0)
            solution.append((str(j), items[i - 1]))
            indices[j] = indices[j] - items[i - 1].size
            i = i - 1
        return solution

    def solveKnapsacksBudget(self, capacity: int, budget: int, items: list):
        """
        :param capacity:  the capacity of the knapsack
        :param budget: the number of items to pick up
        :param items:
        :return: the solution to sub problems
        """
        assert(budget <= len(items))
        subProblemSolutions = Utils.createArray([budget + 1, len(items) + 1, capacity + 1])
        Utils.updateValue(subProblemSolutions, [0], 0)
        for i in range(1, budget + 1):
            Utils.updateValue(subProblemSolutions, [i, 0], 0)
            for j in range(1, len(items) + 1):
                subProblemSolutions[i][j][0] = 0
        for i in range(1, budget + 1):
            for j in range(1, len(items) + 1):
                for k in range(1, capacity + 1):
                    subProblemSolutions[i][j][k] = subProblemSolutions[i][j - 1][k]
                    if items[j - 1].size < k:
                        value = subProblemSolutions[i - 1][j - 1][k - items[j - 1].size] + items[j - 1].value
                        if value > subProblemSolutions[i][j - 1][k]:
                            subProblemSolutions[i][j][k] = value

    def constructKnapsackBudgetSolution(self, capacity: int, budget: int, items: list, subProblemSolutions: list):
        i = budget
        j = len(items)
        k = capacity
        solution = []
        while i > 0:
            if  subProblemSolutions[i][j][k] <= subProblemSolutions[i][j - 1][k]:
                j = j - 1
                continue
            solution.append((items[j - 1].index, items[j - 1]))
            k = k - items[j - 1].size
            i = i - 1
            j = j - 1
        return solution

