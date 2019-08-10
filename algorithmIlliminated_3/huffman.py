import json
import heapq
from collections import deque
class Node:
    """ the root Node of a tree will have the pSum attribute"""
    def __init__(self, left, right, pSum):
        self.left = left
        self.right = right
        self.pSum = pSum


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
            symbol = Symbol(item[0], item[1])
            symbol.pSum = symbol.frequency
            trees.append(symbol)
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
            return secondQueue[0]
        if len(secondQueue) == 0:
            return firstQueue[0]
        if firstQueue[0].pSum < secondQueue[0].pSum:
            return firstQueue.popleft()
        return secondQueue.popleft()

    def sorted_buildHuffmanTree(self, inputData):
        """
       :param inputData:  list for the frequency of symbols
        :return:
        """
        queue1 = deque()
        queue2 = deque()
        sortedData = sorted(inputData)
        for item in sortedData:
            node = Node(None, None, item)
            queue1.append(node)
        while not queue1.empty() or queue2.qsize() > 1:
            minFirst = self.findMin(queue1, queue2)
            minSecond = self.findMin(queue1, queue2)
            node = Node(minFirst, minSecond, minFirst.pSum + minSecond.pSum)
            queue2.append(node)
        assert(len(queue2) == 1)
        return queue2.popleft()

    def heap_HuffmanTree(self, inputData):
        heap = []
        for item in inputData:
            node = Node(None, None, item)
            heap.append((node.pSum, node))
        heapq.heapify(heap)
        while len(heap) > 1:
            minFirst = heapq.heappop(heap)[1]
            minSecond = heapq.heappop(heap)[1]
            node = Node(minFirst, minSecond, minFirst.pSum + minSecond.pSum)
            heapq.heappush(heap, (node.pSum, node))
        return heapq.heappop(heap)[1]

    def main(self):
        #nodes = self.buildHuffmanTree(self.simpleInput())
        #print(nodes)
        node = self.quadraticTime_buildHuffmanTree(self.complexInput())
        self.dumpCode(node, "")

    def dumpCode(self, node, code):
        if node.left is None and node.right is None:
            print("{} = {}".format(node.pSum, code))
            return
        if node.right is not None:
            self.dumpCode(node.right, code + "1")
        if node.left is not None:
            self.dumpCode(node.left, code + "0")

huffmanTree = HuffmanTree()
huffmanTree.main()
