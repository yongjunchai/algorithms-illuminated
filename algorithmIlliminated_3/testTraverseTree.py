import unittest
from algorithmIlliminated_3.treeTraverse import *


class traverseTreeTestCase(unittest.TestCase):
    def test_treeCreationAndTraversal(self):
        tree: Tree = Tree()
        totalNodes = 1234
        root1 = tree.createTreeIterative(totalNodes)
        root2 = Node(None, None, 1)
        tree.createTreeRecrusive(root2, totalNodes)
        nodes1 = tree.levelOrderTraversal_Quadaratic(root1)
        nodes2 = tree.levelOrderTraversal_n(root2)
        print(nodes1)
        print(nodes2)
        self.assertTrue(nodes1 == nodes2)

    def test_dfs(self):
        tree: Tree = Tree()
        totalNodes = 9
        root1 = tree.createTreeIterative(totalNodes)
        result1 = []
        tree.dfsRecursive(root1, result1)
        result2 = tree.dfsIterative(root1)
        print(result1)
        print(result2)
        self.assertTrue(result1 == result2)


if __name__ == '__main__':
    unittest.main()
