import unittest
from algorithmIlliminated_3.treeTraverse import *


class traverseTreeTestCase(unittest.TestCase):
    def test_treeCreationAndTraversal(self):
        tree: Tree = Tree()
        root = tree.createTreeIterative(19999999)
        root = Node(None, None, 1)
        #tree.createTreeRecrusive(root, 19999999)
        #nodes = tree.levelOrderTraversal_Quadaratic(root)
        #print(nodes)
        nodes = tree.levelOrderTraversal_n(root)
        print(nodes)


if __name__ == '__main__':
    unittest.main()
