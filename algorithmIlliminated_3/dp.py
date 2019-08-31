
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


dp = DP()
values = [1, 4, 5, 4]
wisNodes = dp.wis_divide_and_conquer(values)
wisNodes = sorted(wisNodes, key=lambda x: x.index)
for node in wisNodes:
    print("index: %d, value: %d  " % (node.index, node.value))
