from collections import deque
from utils.utils import *


class Graph:
    def __init__(self):
        pass

    def isConnected(self, graph: Graph, sourceVertex: str):
        """
        check all nodes can be reached from sourceVertex
        use DFS(depth first search) to go through the graph
        this can be applied on acyclic graph only
        :param graph:
        :param sourceVertex
        :return:
        """
        stack = deque()
        node = graph.nodes.get(sourceVertex)
        if node is None:
            return False
        stack.append(node)
        cnt = 0
        while len(stack) > 0:
            curNode = stack.pop(len(stack) - 1)
            curNode.visited = True
            cnt = cnt + 1
            if curNode.outflowEdges is None:
                continue
            for name in curNode.outflowEdges.keys():
                node = graph.nodes.get(name)
                if node is None:
                    print("Error %d: node not in the graph: %s" % (get_linenumber(), name))
                    continue
                stack.append(node)
        return cnt == len(graph.nodes)

    def isCyclic(self, graph: Graph, sourceVertex: str):
        """
        check whether there is cycle in the graph
        use DFS(depth first search) to go through the graph
        :param graph:
        :param sourceVertex:
        :return:
        """
        totalNodes = len(graph.nodes)
        stack = deque()
        node = graph.nodes.get(sourceVertex)
        if node is None:
            return False
        stack.append(node)
        cnt = 0
        while len(stack) > 0:
            curNode = stack.pop(len(stack) - 1)
            curNode.visited = True
            cnt = cnt + 1
            if cnt > totalNodes:
                return True
            if curNode.outflowEdges is None:
                continue
            for name in curNode.outflowEdges.keys():
                node = graph.nodes.get(name)
                if node is None:
                    print("Error %d: node not in the graph: %s" % (get_linenumber(), name))
                    continue
                stack.append(node)
        return False

    def detectSCC_kosaraju(self, graph: Graph):
        for node in graph.nodes.values():
            node.visited = False
        nodesOrdered = deque()
        self.topoSort(graph, True, nodesOrdered)
        for node in graph.nodes.values():
            node.visited = False
        numSCC = 0
        for node in nodesOrdered:
            if node.visited:
                continue
            numSCC = numSCC + 1
            self.dfsScc(node, numSCC, graph)

    def dfsScc(self, node: Node, numScc: int, graph: Graph):
        node.visited = True
        node.numScc = numScc
        for name in node.outflowEdges.keys():
            curNode = graph.nodes.get(name)
            if curNode is None:
                print("Error %d: node not in the graph: %s" % (get_linenumber(), name))
                continue
            if curNode.visited:
                continue
            self.dfsScc(curNode, numScc, graph)

    def topoSort(self, graph: Graph, reverse: bool, nodesOrdered: deque):
        """
        the f-value of vertices constitute a topological ordering of G
        :param graph:
        :return:
        """
        for node in graph.nodes.values():
            node.visited = False
        curLabel: int = len(graph.nodes)
        for node in graph.nodes.values():
            if node.visited:
                continue
            curLabel = self.dfsTopo(node, curLabel, graph, reverse, nodesOrdered)

    def dfsTopo(self, node: Node, curLabel: int, graph: Graph, reverse: bool, nodesOrdered: deque):
        node.visited = True
        edges = None
        if reverse:
            edges = node.inflowEdges
        else:
            edges = node.outflowEdges
        if edges is not None:
            for name in edges.values():
                curNode = graph.nodes.get(name)
                if curNode is None:
                    print("Error: node not in the graph: %s" % name)
                    continue
                curLabel = self.dfsTopo(curNode, curLabel, graph)
        node.topoOrderVal = curLabel
        nodesOrdered.appendleft(node)
        curLabel = curLabel - 1
        return curLabel