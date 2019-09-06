
from collections import deque

class Node:
    def __init__(self, value: int, index: int):
        self.value = value
        self.index = index


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
            if self.calSum(leftMerged) + self.calSum(rightMerged2nd) < self.calSum(leftMerged2nd) + self.calSum(rightMerged):
                for node in  leftMerged2nd:
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

    def wis_dp_recursive_cache_internal(self, wisCache, values):
        if len(values) <= 1:
            return values
        if wisCache[len(values) - 1] is not None:
            return wisCache[len(values) - 1]
        s1 = self.wis_dp_recursive_cache_internal(wisCache, values[0:len(values) - 1])
        s2 = self.wis_dp_recursive_cache_internal(wisCache, values[0:len(values) - 2])
        s1Sum = self.calSumForNumArray(s1)
        s2Sum = self.calSumForNumArray(s2) + values[len(values) - 1]
        if  s1Sum > s2Sum:
            wisCache[len(values) - 1] = s1Sum
            return s1
        else:
            wisCache[len(values) - 1] = s2Sum
            s2.append(values[len(values) - 1])
            return s2

    def wis_dp_recursive_cache(self, values):
        if len(values) <= 1:
            return values
        wisCache = [None] * len(values)
        wisCache[0] = values[0]
        return self.wis_dp_recursive_cache_internal(wisCache, values)

    def wis_dp_iterative(self, values):
        subProblemResult = [None] * (len(values) + 1)
        subProblemResult[0] = 0
        subProblemResult[1] = values[0]
        for i in range(2, len(values)):
            if subProblemResult[i - 1] > subProblemResult[i - 2] + values[i]:
                subProblemResult[i] = subProblemResult[i - 1]
            else:
                subProblemResult[i] = subProblemResult[i - 2] + values[i]
        return subProblemResult[len(values - 1)]

    def wis_dp_construct_solution(self, subProblemResult, values):
        queue = deque()
        i = len(values)
        while i > 0:
            if subProblemResult[i] > subProblemResult[i - 2] + values[i - 1]:
                continue
            queue.appendleft(values[i - 1])
        return queue

