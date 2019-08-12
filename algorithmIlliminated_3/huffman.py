import heapq
from collections import deque


class Node:
    """ the root Node of a tree will have the pSum attribute"""
    def __init__(self, left, right, pSum):
        self.left: Node = left
        self.right: Node = right
        self.pSum: int = pSum


class Symbol(Node):
    def __init__(self, symbol, frequency):
        Node.__init__(self, None, None, frequency)
        self.symbol = symbol
        self.frequency = frequency


class HuffmanTree:
    def simpleInput(self):
        return [("A", 0.60), ("B", 0.25), ("C", 0.10), ("D", 0.05)]

    def complexInput(self):
        return [("A", 1), ("B", 2), ("C", 3), ("D", 4), ("E", 5), ("F", 6), ("G", 7)]

    def init(self, inputList):
        trees = list()
        for item in inputList:
            node = Node(None, None, item)
            trees.append(node)
        return trees

    def argmins(self, trees):
        """ return two trees tuple with the smallest pSum
        """
        assert(len(trees) >= 2)
        smallest = trees[0]
        secondSmallest = trees[1]
        if secondSmallest.pSum < smallest.pSum:
            smallest, secondSmallest = secondSmallest, smallest
        for x in trees[2:]:
            if x.pSum < smallest.pSum:
                smallest, secondSmallest = x, smallest
            elif x.pSum < secondSmallest.pSum:
                secondSmallest = x
        return smallest, secondSmallest

    def quadraticTime_buildHuffmanTree(self, inputList):
        if inputList is None or len(inputList) == 0:
            return None
        trees = self.init(inputList)
        while len(trees) > 1:
            smallest, secondSmallest = self.argmins(trees)
            trees.remove(smallest)
            trees.remove(secondSmallest)
            node = Node(smallest, secondSmallest, smallest.pSum + secondSmallest.pSum)
            trees.append(node)
        return trees[0]

    def findMin(self, firstQueue, secondQueue):
        if len(firstQueue) == 0:
            return secondQueue.popleft()
        if len(secondQueue) == 0:
            return firstQueue.popleft()
        if firstQueue[0].pSum < secondQueue[0].pSum:
            return firstQueue.popleft()
        return secondQueue.popleft()

    def sorted_buildHuffmanTree(self, inputData):
        """
       :param inputData:  list for the frequency of symbols
        :return:
        """
        if inputData is None or len(inputData) == 0:
            return None
        queue1 = deque()
        queue2 = deque()
        sortedData = sorted(inputData)
        for item in sortedData:
            node = Node(None, None, item)
            queue1.append(node)
        while len(queue1) > 0 or len(queue2) > 1:
            minFirst = self.findMin(queue1, queue2)
            minSecond = self.findMin(queue1, queue2)
            node = Node(minFirst, minSecond, minFirst.pSum + minSecond.pSum)
            queue2.append(node)
        assert(len(queue2) == 1)
        return queue2.popleft()

    def heap_HuffmanTree(self, inputData):
        if inputData is None or len(inputData) == 0:
            return None
        q = []
        for item in inputData:
            node = Node(None, None, item)
            q.append((node.pSum, node))
        heapq.heapify(q)
        while len(q) > 1:
            minFirst = heapq.heappop(q)[1]
            minSecond = heapq.heappop(q)[1]
            node = Node(minFirst, minSecond, minFirst.pSum + minSecond.pSum)
            heapq.heappush(q, (node.pSum, node))
        return heapq.heappop(q)[1]

    def main(self):
        #nodes = self.buildHuffmanTree(self.simpleInput())
        #print(nodes)
        node = self.quadraticTime_buildHuffmanTree(self.complexInput())
        self.dumpCode(node, "")

    def dumpCode(self, node, code, result):
        if node.left is None and node.right is None:
            result.append((node.pSum, code))
            return
        if node.right is not None:
            self.dumpCode(node.right, code + "1", result)
        if node.left is not None:
            self.dumpCode(node.left, code + "0", result)

    def dumpCodeIterate(self, node, code, result):
        if node is None:
            return
        stack = deque()
        while(len(stack) > 0):
            stack.p

