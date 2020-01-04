import unittest
from algorithmIlliminated_2.redBlackTree import *
import random


class MyTestCase(unittest.TestCase):
    def test_insert(self):
        redBlackTree = RedBlackTree()
        redBlackTree.insert(10, True)
        redBlackTree.insert(20, True)
        redBlackTree.insert(30, True)
        redBlackTree.insert(15, True)

        node: TreeNode = None
        node = redBlackTree.searchEx(20)
        self.assertTrue(node.color == Color.BLACK)
        self.assertTrue(node.parent is None)
        self.assertTrue(node.left.key == 10)
        self.assertTrue(node.right.key == 30)

        node = redBlackTree.searchEx(100)
        self.assertTrue(node is None)

        node = redBlackTree.searchEx(10)
        self.assertTrue(node.color == Color.BLACK)
        self.assertTrue(node.right.key == 15)

        node = redBlackTree.searchEx(30)
        self.assertTrue(node.color == Color.BLACK)

        node = redBlackTree.searchEx(15)
        self.assertTrue(node.color == Color.RED)

        redBlackTree.insert(9, True)
        redBlackTree.insert(8, True)
        redBlackTree.insert(7, True)
        self.verifyParentChildRelation(redBlackTree.root)

    def test_insert_rnd_10k(self):
        redBlackTree = RedBlackTree()
        keys = []
        cnt = 1024 * 10
        for i in range(cnt):
            keys.append(i)
        random.shuffle(keys)
        for key in keys:
            redBlackTree.insert(key, True)
        for key in keys:
            node: TreeNode = redBlackTree.searchEx(key)
            self.assertTrue(node is not None)
            self.assertTrue(node.key == key)
            self.assertTrue(node.value is True)
        self.verifyParentChildRelation(redBlackTree.root)
        self.verifyNodeSize(redBlackTree.root)
        self.assertTrue(cnt == redBlackTree.root.size)

    def test_insert_find(self):
        cnt = 10
        loop = 1
        while True:
            loop = loop + 1
            if loop > 1000:
                break
            print("loop [%d]" % loop)
            redBlackTree = RedBlackTree()
            keys = []
            for i in range(cnt):
                keys.append(i)
            random.shuffle(keys)
            print(keys)
            for i in keys:
                redBlackTree.insert(i, True)
            for i in keys:
                node: TreeNode = redBlackTree.searchEx(i)
                self.assertTrue(node is not None)
                self.assertTrue(node.key == i)
                self.assertTrue(node.value is True)
            self.verifyParentChildRelation(redBlackTree.root)

    def verifyParentChildRelation(self, curNode: TreeNode):
        if curNode is None:
            return
        if curNode.left is not None:
            if curNode.key != curNode.left.parent.key:
                print("error")
            self.assertTrue(curNode.key == curNode.left.parent.key)
        if curNode.right is not None:
            if curNode.key != curNode.right.parent.key:
                print("error")
            self.assertTrue(curNode.key == curNode.right.parent.key)
        self.verifyParentChildRelation(curNode.left)
        self.verifyParentChildRelation(curNode.right)

    def test_10(self):
        keys = [0, 9, 7, 1, 2, 8, 3, 6]
        redBlackTree = RedBlackTree()
        for i in keys:
            redBlackTree.insert(i, True)
            print("after insert %d" % i)
            self.verifyParentChildRelation(redBlackTree.root)

        redBlackTree.insert(4, True)
        print("after insert %d" % 4)
        self.verifyParentChildRelation(redBlackTree.root)

        redBlackTree.insert(5, True)
        for i in keys:
            node: TreeNode = redBlackTree.searchEx(i)
            self.assertTrue(node is not None)
            self.assertTrue(node.key == i)
            self.assertTrue(node.value is True)

    def getSubTreeSize(self, node: TreeNode):
        if node is None:
            return 0
        return 1 + self.getSubTreeSize(node.left) + self.getSubTreeSize(node.right)

    def verifyNodeSize(self, node: TreeNode):
        if node is None:
            return
        self.assertTrue(node.size == self.getSubTreeSize(node))
        self.verifyNodeSize(node.left)
        self.verifyNodeSize(node.right)

    def test_dup(self):
        keys = [0, 9, 7, 1, 2, 8, 3, 6, 4, 5, 5, 5, 5, 5]
        redBlackTree = RedBlackTree()
        for i in keys:
            redBlackTree.insert(i, True)
            self.verifyParentChildRelation(redBlackTree.root)

        self.verifyParentChildRelation(redBlackTree.root)
        for i in keys:
            node: TreeNode = redBlackTree.searchEx(i)
            self.assertTrue(node is not None)
            self.assertTrue(node.key == i)
            self.assertTrue(node.value is True)
        self.assertTrue(14 == redBlackTree.root.size)
        self.verifyNodeSize(redBlackTree.root)

    def test_select(self):
        keys = []
        cnt = 1024
        for i in range(1, cnt, 1):
            keys.append(i)
        redBlackTree = RedBlackTree()
        for i in keys:
            redBlackTree.insert(i, None)
            node: TreeNode = redBlackTree.selectEx(i)
            self.assertTrue(i == node.key)


if __name__ == '__main__':
    unittest.main()

