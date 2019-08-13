from algorithmIlliminated_3.huffman import Node
from collections import deque

class Tree:
    def createTreeRecrusive(self, cur: Node, max: int):
        if cur.pSum >= max:
            return
        if cur.pSum * 2 <= max:
            cur.left = Node(None, None, cur.pSum * 2)
        if cur.pSum * 2 + 1 <= max:
            cur.right = Node(None, None, cur.pSum * 2 + 1)
        if cur.left is not None:
            self.createTreeRecrusive(cur.left, max)
        if cur.right is not None:
            self.createTreeRecrusive(cur.right, max)

    def createTreeIterative(self, max: int):
        queue = deque()
        root = Node(None, None, 1)
        queue.append(root)
        curId = 1
        while len(queue) > 0:
            cur = queue.popleft()
            if curId < max:
                curId += 1
                cur.left = Node(None,  None, curId)
                queue.append(cur.left)
            if curId < max:
                curId += 1
                cur.right = Node(None, None, curId)
                queue.append(cur.right)
        return root

    def dfsRecursive(self, cur: Node, result: list):
        if cur is None:
            return
        result.append(cur.pSum)
        self.dfsRecursive(cur.left, result)
        self.dfsRecursive(cur.right, result)

    def dfsIterative(self, root: Node):
        if root is None:
            return
        result = []
        stack = [root]
        while len(stack) > 0:
            cur = stack.pop()
            result.append(cur.pSum)
            if cur.right is not None:
                stack.append(cur.right)
            if cur.left is not None:
                stack.append(cur.left)
        return result

    def printLevel(self, cur: Node, level: int, result: list):
        if cur is None or level < 1:
            return False
        if level == 1:
            result.append(cur.pSum)
            # only return true if one node appear in given level
            return True
        left: bool = self.printLevel(cur.left, level - 1, result)
        right: bool = self.printLevel(cur.right, level - 1, result)
        return left or right

    def levelOrderTraversal_Quadaratic(self, cur: Node):
        level = 1
        result = []
        while self.printLevel(cur, level, result):
            level += 1
        return result

    def levelOrderTraversal_n(self, cur: Node):
        """
        put the current level nodes in the queue and add children of processed nodes
        :param cur:
        :return:
        """
        result = []
        # invariants of the queue
        #   start: nodes of the first level
        #   each iteration: process nodes from the front of the queue, and add nodes in the level sequence to the queue
        queue = deque()
        queue.append(cur)
        while len(queue) > 0:
            cur = queue.popleft()
            result.append(cur.pSum)
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)
        return result

    def getTreeHeight(self, cur: Node, curHeight: int):
        if cur is None:
            return curHeight
        ++ curHeight
        if cur.left is not None:
            return self.getTreeHeight(cur.left, curHeight)
        elif cur.right is not None:
            return self.getTreeHeight(cur.right, curHeight)
        else:
            return curHeight

    def drawTree(self, cur: Node):
        totalHeight = self.getTreeHeight(cur, 0)
