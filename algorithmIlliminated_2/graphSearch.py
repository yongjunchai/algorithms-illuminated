from collections import deque
from utils.utils import *


class GraphSearch:
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
        sccs = dict()
        for node in nodesOrdered:
            if node.numScc is None:
                print("no scc for [%s] node" % node.name)
                continue
            scc = sccs.get(str(node.numScc))
            if scc is None:
                scc = list()
                sccs[str(node.numScc)] = scc
            scc. append(node.name)
        return sccs

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
            for name in edges.keys():
                curNode = graph.nodes.get(name)
                if curNode is None:
                    print("Error: node not in the graph: %s" % name)
                    continue
                if curNode.visited:
                    continue
                curLabel = self.dfsTopo(curNode, curLabel, graph, reverse, nodesOrdered)
        node.topoOrderVal = curLabel
        nodesOrdered.appendleft(node)
        curLabel = curLabel - 1
        return curLabel

    def detectSCC_kosaraju_iterative(self, graph: Graph):
        for node in graph.nodes.values():
            node.visited = False
        nodesOrdered = deque()
        self.topoSort_iterative(graph, True, nodesOrdered)
        for node in graph.nodes.values():
            node.visited = False
        numSCC = 0
        for node in nodesOrdered:
            if node.visited:
                continue
            numSCC = numSCC + 1
            self.dfsSccIterative(node, numSCC, graph)
        sccs = dict()
        for node in nodesOrdered:
            if node.numScc is None:
                print("no scc for [%s] node" % node.name)
                continue
            scc = sccs.get(str(node.numScc))
            if scc is None:
                scc = list()
                sccs[str(node.numScc)] = scc
            scc. append(node.name)
        return sccs


    def dfsSccIterative(self, node: Node, numScc: int, graph: Graph):
        stack = deque()
        stack.append(node)
        while len(stack) > 0:
            curNode: Node = stack.pop()
            if curNode.visited:
                continue
            curNode.visited = True
            curNode.numScc = numScc
            for name in curNode.outflowEdges.keys():
                tempNode = graph.nodes.get(name)
                if tempNode is None:
                    print("Error %d: node not in the graph: %s" % (get_linenumber(), name))
                    continue
                if tempNode.visited:
                    continue
                stack.append(tempNode)



    def topoSort_iterative(self, graph: Graph, reverse: bool, nodesOrdered: deque):
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
            curLabel = self.dfsTopo_iterative(node, curLabel, graph, reverse, nodesOrdered)

    def dfsTopo_iterative(self, node: Node, curLabel: int, graph: Graph, reverse: bool, nodesOrdered: deque):
        stack = deque()
        stack.append(node)
        while len(stack) > 0:
            curNode: Node = stack.pop()
            if curNode.visited:
                if curNode.topoOrderVal is not None:
                    # in cyclical graph, same node may be pushed to stack multiple times
                    continue
                curNode.topoOrderVal = curLabel
                nodesOrdered.appendleft(curNode)
                curLabel = curLabel - 1
            else:
                curNode.visited = True
                stack.append(curNode)
                edges = None
                if reverse:
                    edges = curNode.inflowEdges
                else:
                    edges = curNode.outflowEdges
                if edges is not None:
                    for name in edges.keys():
                        tempNode = graph.nodes.get(name)
                        if tempNode is None:
                            print("Error: node not in the graph: %s" % name)
                            continue
                        if tempNode.visited:
                            continue
                        stack.append(tempNode)
        return curLabel