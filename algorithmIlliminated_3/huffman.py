import json
import heapq
class Node:
    """ the root Node of a tree will have the pSum attribute"""
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.pSum = None


class Symbol(Node):
    def __init__(self, symbol, frequency):
        Node.__init__(self, None, None)
        self.symbol = symbol
        self.frequency = frequency


class HuffmanTree:
    def simpleInput(self):
        return [("A", 0.60), ("B", 0.25), ("C", 0.10), ("D", 0.05)]

    def complexInput(self):
        return [("A", 3), ("B", 2), ("C", 6), ("D", 8), ("E", 2), ("F", 6)]

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
            node = Node(smallest, secondSmallest)
            node.pSum = smallest.pSum + secondSmallest.pSum
            trees.append(node)
        return trees[0]

    def heap_HuffmanTree(self):
        pass

    def main(self):
        #nodes = self.buildHuffmanTree(self.simpleInput())
        #print(nodes)
        node = self.quadraticTime_buildHuffmanTree(self.complexInput())
        self.dumpCode(node, "")

    def dumpCode(self, node, code):
        if getattr(node, "symbol", None) is not None:
            print("{} = {}".format(node.symbol, code))
            return
        if node.right is not None:
            self.dumpCode(node.right, code + "1")
        if node.left is not None:
            self.dumpCode(node.left, code + "0")

huffmanTree = HuffmanTree()
huffmanTree.main()
