from collections import deque


class Node:
    def __init__(self, value: int, index: int):
        self.value = value
        self.index = index


class Item:
    def __init__(self, size: int, value: int):
        assert (size is int and size > 0)
        assert (value is int and value > 0)
        self.value = value
        self.size = size


class Knapsack:
    def __init__(self, capacity: int, items: list):
        assert (capacity is int and capacity > 0)
        assert (len(items) > 0)
        for item in items:
            assert (item.size is int and item.size > 0)
            assert (item.value is int and item.value > 0)
        self.capacity = capacity
        self.items = items


class DP:
    def __init__(self):
        pass

    def calSum(self, nodes):
        res = 0
        for node in nodes:
            res = res + node.value
        return res

    def wis_divide_and_conquer_internal(self, values: list):
        if len(values) <= 1:
            return values
        mid = int(len(values) / 2)
        left = values[0:mid]
        right = values[mid:]
        leftMerged = self.wis_divide_and_conquer_internal(left)
        rightMerged = self.wis_divide_and_conquer_internal(right)
        if leftMerged[len(leftMerged) - 1].index + 1 == rightMerged[0].index:
            # conflict found, we need recalculate
            leftMerged2nd = self.wis_divide_and_conquer_internal(left[0: mid - 1])
            rightMerged2nd = self.wis_divide_and_conquer_internal(right[1:])
            if self.calSum(leftMerged) + self.calSum(rightMerged2nd) < self.calSum(leftMerged2nd) + self.calSum(
                    rightMerged):
                for node in leftMerged2nd:
                    rightMerged.append(node)
                return rightMerged
            else:
                for node in rightMerged2nd:
                    leftMerged.append(node)
                return leftMerged
        else:
            for node in rightMerged:
                leftMerged.append(node)
            return leftMerged

    def wis_divide_and_conquer(self, values):
        nodes = []
        for i in range(0, len(values)):
            node = Node(values[i], i)
            nodes.append(node)
        res = self.wis_divide_and_conquer_internal(nodes)
        return res

    def calSumForNumArray(self, values):
        total = 0
        for i in values:
            total = total + i
        return total

    def wis_dp_recursive(self, values):
        if len(values) <= 1:
            return values
        s1 = self.wis_dp_recursive(values[0:len(values) - 1])
        s2 = self.wis_dp_recursive(values[0:len(values) - 2])
        if self.calSumForNumArray(s1) > (self.calSumForNumArray(s2) + values[len(values) - 1]):
            return s1
        else:
            s2.append(values[len(values) - 1])
            return s2

    def wis_dp_recursive_cache_internal(self, subProblemSolutions, indexSolution, values):
        if subProblemSolutions[indexSolution] is not None:
            return
        self.wis_dp_recursive_cache_internal(subProblemSolutions, indexSolution - 1, values)
        self.wis_dp_recursive_cache_internal(subProblemSolutions, indexSolution - 2, values)
        s1Sum = subProblemSolutions[indexSolution - 1]
        s2Sum = subProblemSolutions[indexSolution - 2] + values[indexSolution - 1]
        if s1Sum > s2Sum:
            subProblemSolutions[indexSolution] = s1Sum
        else:
            subProblemSolutions[indexSolution] = s2Sum

    def wis_dp_recursive_cache(self, values):
        if values is None or len(values) <= 1:
            assert(False)
            return
        subProblemSolutions = [None for i in (len(values) + 1)]
        subProblemSolutions[0] = 0
        subProblemSolutions[1] = values[0]
        self.wis_dp_recursive_cache_internal(subProblemSolutions, len(values), values)
        return subProblemSolutions

    def wis_dp_iterative(self, values):
        subProblemSolutions = [None for i in range(len(values) + 1)]
        subProblemSolutions[0] = 0
        subProblemSolutions[1] = values[0]
        for i in range(2, len(values) + 1):
            if subProblemSolutions[i - 1] > subProblemSolutions[i - 2] + values[i - 1]:
                subProblemSolutions[i] = subProblemSolutions[i - 1]
            else:
                subProblemSolutions[i] = subProblemSolutions[i - 2] + values[i - 1]
        return subProblemSolutions

    def wis_dp_construct_solution(self, subProblemSolutions, values):
        assert (len(subProblemSolutions) == (len(values) + 1))
        queue = deque()
        i = len(values)
        while i > 1:
            if subProblemSolutions[i] > subProblemSolutions[i - 2] + values[i - 1]:
                i = i - 1
                continue
            queue.appendleft(values[i - 1])
            i = i - 2
        if i == 1:
            queue.appendleft(values[0])
        return queue

    def solveKnapsackProblem(self, knapsack: Knapsack):
        assert (knapsack is Knapsack)
        subProblemSolutions = [[None for i in range(len(knapsack.items) + 1)] for j in range(len(knapsack.capacity) + 1)]
        for i in range(0, len(knapsack.items) + 1):
            subProblemSolutions[i][0] = 0
        for c in range(0, knapsack.capacity + 1):
            subProblemSolutions[0][c] = 0
        for i in range(1, len(knapsack.items) + 1):
            for c in range(1, knapsack.capacity + 1):
                if knapsack.items[i - 1] > c:
                    subProblemSolutions[i][c] = subProblemSolutions[i - 1][c]
                else:
                    if subProblemSolutions[i - 1][c] > subProblemSolutions[i - 1][c - knapsack.items[i - 1].size] + \
                            knapsack.items[i - 1].value:
                        subProblemSolutions[i][c] = subProblemSolutions[i - 1][c]
                    else:
                        subProblemSolutions[i][c] = subProblemSolutions[i - 1][c - knapsack.items[i - 1].size] + \
                                                    knapsack.items[i - 1].value
        return subProblemSolutions

    def constructKnapsackSolution(self, subProblemSolutions, knapsack: Knapsack):
        solution = deque()
        c = knapsack.capacity
        i = len(knapsack.items)
        while i > 0:
            if knapsack.items[i - 1].size < c and subProblemSolutions[i - 1][c - knapsack.items[i - 1].size] + \
                    knapsack.items[i - 1].value > subProblemSolutions[i - 1][c]:
                solution.appendleft(knapsack.items[i - 1])
                c = c - knapsack.items[i - 1].size
            i = i - 1
        return solution
