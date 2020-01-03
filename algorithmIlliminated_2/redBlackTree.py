
from enum import Enum


class Color(Enum):
    RED = 1
    BLACK = 2


class Direction(Enum):
    LEFT = 1
    RIGHT = 2


class TreeNode:
    def __init__(self):
        self.parent: TreeNode = None
        self.left: TreeNode = None
        self.right: TreeNode = None
        self.color: Color = Color.RED
        self.key: int = None
        self.value: object = None


class RedBlackTree:
    def __init__(self):
        self.root: TreeNode = None

    def insert(self, key: int, value: object):
        """
        insert <key, value> into the tree. The key is already in the tree, the value will be updated.
        :param key:
        :param value:
        :return:
        """
        if self.root is None:
            node = TreeNode()
            node.key = key
            node.value = value
            node.color = Color.BLACK
            self.root = node
        else:
            self.insert_internal(self.root, key, value)

    def getDirection(self, curNode: TreeNode):
        p = curNode.parent
        if curNode.key > p.key:
            return Direction.RIGHT
        else:
            return Direction.LEFT

    def getUncle(self, curNode: TreeNode):
        p = curNode.parent
        g = p.parent
        if p.key < g.key:
            return g.right
        else:
            return g.left

    def leftRotate(self, node: TreeNode):
        rightChild = node.right
        if node.parent is None:
            self.root = rightChild
        else:
            self.fix_parent(node, rightChild)
        rightChild.parent = node.parent
        node.right = rightChild.left
        if rightChild.left is not None:
            rightChild.left.parent = node
        rightChild.left = node
        node.parent = rightChild

    def fix_parent(self, node: TreeNode, child: TreeNode):
        p = node.parent
        if p.key > node.key:
            p.left = child
        else:
            p.right = child


    def rightRotate(self, node: TreeNode):
        leftChild = node.left
        if node.parent is None:
            self.root = leftChild
        else:
            self.fix_parent(node, leftChild)
        leftChild.parent = node.parent
        node.left = leftChild.right
        if leftChild.right is not None:
            leftChild.right.parent = node
        leftChild.right = node
        node.parent = leftChild

    def balanceNode(self, curNode: TreeNode):
        """
        ref: https://www.geeksforgeeks.org/red-black-tree-set-2-insert/
        :param curNode:
        :param gpDirection: grandparent to parent direction
        :param pDirection: parent to current node direction
        :return:
        """
        if curNode.parent is None:
            curNode.color = Color.BLACK
            return
        assert curNode.parent is not None
        p = curNode.parent
        if p.color is Color.BLACK:
            return
        assert p.parent is not None
        g = p.parent
        uncle: TreeNode = self.getUncle(curNode)
        if uncle is not None and uncle.color is Color.RED:
            p.color = Color.BLACK
            uncle.color = Color.BLACK
            g.color = Color.RED
            self.balanceNode(g)
        else:
            # null node is treated as black
            # If x’s uncle is BLACK, then there can be four configurations for x, x’s parent (p) and x’s grandparent (g)
            # (This is similar to AVL Tree)
            pDir = self.getDirection(curNode.parent)
            curDir = self.getDirection(curNode)

            if pDir == Direction.LEFT and curDir == Direction.LEFT:
                self.rightRotate(g)
                p.color = Color.BLACK
                g.color = Color.RED
            elif pDir == Direction.LEFT and curDir == Direction.RIGHT:
                self.leftRotate(p)
                self.rightRotate(g)
                curNode.color = Color.BLACK
                g.color = Color.RED
            elif pDir == Direction.RIGHT and curDir == Direction.RIGHT:
                self.leftRotate(g)
                p.color = Color.BLACK
                g.color = Color.RED
            else:
                # right left case
                self.rightRotate(p)
                self.leftRotate(g)
                curNode.color = Color.BLACK
                g.color = Color.RED

    def insert_internal(self, curNode: TreeNode, key: int, value: object):
        if curNode.key == key:
            curNode.value = value
        elif curNode.key < key:
            if curNode.right is None:
                # insert new node here
                right = TreeNode()
                right.key = key
                right.value = value
                right.parent = curNode
                right.color = Color.RED
                curNode.right = right
                self.balanceNode(right)
            else:
                self.insert_internal(curNode.right, key, value)
        else:
            if curNode.left is None:
                # insert new node here
                left = TreeNode()
                left.key = key
                left.value = value
                left.parent = curNode
                left.color = Color.RED
                curNode.left = left
                self.balanceNode(left)
            else:
                self.insert_internal(curNode.left, key, value)

    def search(self, key: int):
        """
        :param key:
        :return: value if found, else None
        """
        return self.search_internal(self.root, key)

    def search_internal(self, curNode: TreeNode, key: int):
        if curNode is None:
            return None
        if curNode.key == key:
            return curNode.value
        if curNode.key < key:
            return self.search_internal(curNode.right, key)
        else:
            return self.search_internal(curNode.left, key)

    def searchEx(self, key: int):
        """
        :param key:
        :return: TreeNode if found, else None
        """
        return self.searchEx_internal(self.root, key)

    def searchEx_internal(self, curNode: TreeNode, key: int):
        if curNode is None:
            return None
        if curNode.key == key:
            return curNode
        if curNode.key < key:
            return self.searchEx_internal(curNode.right, key)
        else:
            return self.searchEx_internal(curNode.left, key)
