
class Node:
    def __init__(self, val, parentIndex):
        self.val = val
        self.parentIndex = parentIndex
        self.size = 1


class UnionFind:
    def __init__(self, vals: list):
        assert(vals is not None)
        assert(len(vals) > 0)
        self.vertices = []
        self.verticesDict = dict()
        for i in range(0, len(vals)):
            node = Node(vals[i], i)
            self.vertices.append(node)
            self.verticesDict[vals[i]] = i

    def find(self, val):
        index = self.verticesDict.get(val)
        if index is None:
            return None
        cur = self.vertices[index]
        while index != cur.parentIndex:
            index = cur.parentIndex
            cur = self.vertices[cur.parentIndex]
        return index

    def union(self, val1, val2):
        i = self.find(val1)
        j = self.find(val2)
        if i is None or j is None:
            print("failed to find vertex %s, %s" % (val1, val2))
            return
        if i == j:
            return
        iNode = self.vertices[i]
        jNode = self.vertices[j]
        if iNode.size < jNode.size:
            iNode.parentIndex = j
            jNode.size = iNode.size + jNode.size
        else:
            jNode.parentIndex = i
            iNode.size = iNode.size + jNode.size
        return
