import sys
from utils.utils import *


class TourNode:
    def __init__(self, name: str):
        self.name = name
        self.next: TourNode = None
        self.nextLength = 0
        self.previous: TourNode = None
        self.previousLength = 0


class Tsp:
    def __init__(self, graph: Graph):
        # TourNode in the visited sequence  of the tour
        self.headTourNode: TourNode = None
        self.tourLength = 0
        self.graph = graph
        self.suc = True

    def nearest_neighbor(self, startNode: str):
        curNode: Node = self.graph.nodes.get(startNode)
        if curNode is None:
            print("Failed to find start node {}".format(startNode))
            self.suc = False
            return
        tailTourNode: TourNode = None
        while curNode is not None:
            curTourNode = TourNode(curNode.name)

            if tailTourNode is None:
                tailTourNode = curTourNode
                self.headTourNode = curTourNode

            # find nearest not-visited neighbor
            nextNode = None
            nextEdgeLength = 0
            for name, length in curNode.outflowEdges.items():
                node = self.graph.nodes.get(name)
                if node is None:
                    self.suc = False
                    print("Failed to find node {}".format(name))
                    return
                if node.visited:
                    continue
                if (nextNode is None) or (length < nextEdgeLength):
                    nextNode = node
                    nextEdgeLength = length
                    continue
            curNode = None
            if nextNode is None:
                continue
            nextNode.visited = True
            tailTourNode.nextLength = nextEdgeLength
            tailTourNode.next = TourNode(nextNode.name)
            tailTourNode.next.previous = tailTourNode
            tailTourNode.next.previousLength = nextEdgeLength
            tailTourNode = tailTourNode.next
            self.tourLength = self.tourLength + nextEdgeLength
            curNode = nextNode
        if (self.headTourNode is not None) and (tailTourNode is not None):
            edgeLen = self.getEdgeLength(tailTourNode.name, startNode)
            tailTourNode.next = self.headTourNode
            tailTourNode.nextLength = edgeLen
            self.headTourNode.previous = tailTourNode
            self.headTourNode.previousLength = edgeLen

    def getEdgeLength(self, endpoint1: str, endpoint2: str):
        node: Node = self.graph.nodes.get(endpoint1)
        if node is None:
            return sys.maxsize
        length = node.outflowEdges.get(endpoint2)
        if length is None:
            return sys.maxsize
        return length

    def two_opt(self, startNodeName: str):
        self.nearest_neighbor(startNodeName)
        if self.suc is False:
            print("failed to find nearest neighbor tour")
            return
        isLocalMinimum = False
        while not isLocalMinimum:
            optTourNode1: TourNode = None
            optTourNode2: TourNode = None
            lenDecrease = 0
            firstTourNode = self.headTourNode
            while firstTourNode.next.name != self.headTourNode.name:
                secondTourNode = firstTourNode.next
                while secondTourNode.name != self.headTourNode.name:
                    # skip if there is endpoint overlap
                    if firstTourNode.name == secondTourNode.name or firstTourNode.name == secondTourNode.next.name:
                        secondTourNode = secondTourNode.next
                        continue
                    if firstTourNode.next.name == secondTourNode.name or firstTourNode.next.name == secondTourNode.next.name:
                        secondTourNode = secondTourNode.next
                        continue
                    linkLenSum = firstTourNode.nextLength + secondTourNode.nextLength
                    swappedLinkLenSum = self.getEdgeLength(firstTourNode.name, secondTourNode.name) + \
                        self.getEdgeLength(firstTourNode.next.name + secondTourNode.next.name)
                    if linkLenSum > swappedLinkLenSum:
                        if (optTourNode1 is None) or (lenDecrease < (linkLenSum - swappedLinkLenSum)):
                            optTourNode1 = firstTourNode
                            optTourNode2 = secondTourNode
                            lenDecrease = linkLenSum - swappedLinkLenSum
            if optTourNode1 is None:
                isLocalMinimum = True
                continue
            v = optTourNode1
            w = optTourNode1.next
            x = optTourNode2
            u = x.next
            xPrevious = x.previous
            xPreviousLength = x.previousLength


            v.next = x
            v.nextLength = self.getEdgeLength(v.name, x.name)
            x.previous = v
            x.previousLength = v.nextLength
            w.next = u
            w.nextLength = self.getEdgeLength(w.name, u.name)
            u.previous = w
            u.previousLength = w.nextLength
            # flip the link direction from x, to w
            x.nextLength = xPreviousLength
            curFlipNode = x
            curFlipNodePrevious = xPrevious
            while curFlipNode.name != w.name:
                curFlipNode.next = curFlipNodePrevious
                curFlipNodePrevious = curFlipNodePrevious.previous
                curFlipNode.next.previous = curFlipNode
                curFlipNode = curFlipNode.next

