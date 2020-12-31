import sys
from utils.utils import *


class TourNode:
    def __init__(self, name: str):
        self.name = name
        self.next: TourNode = None
        self.nextLength = 0
        self.previous: TourNode = None
        self.previousLength = 0


class TspLocalSearch:
    def __init__(self, graph: Graph):
        # TourNode in the visited sequence  of the tour
        self.headTourNode: TourNode = None
        self.tourLength = 0
        self.graph = graph
        self.suc = True

    def dumpTour(self):
        print("tour length: {}".format(self.tourLength))
        curTourNode = self.headTourNode
        print("{} --> {}  : {}".format(curTourNode.name, curTourNode.next.name, curTourNode.nextLength))
        curTourNode = curTourNode.next
        while(curTourNode.name != self.headTourNode.name):
            print("{} --> {}  : {}".format(curTourNode.name, curTourNode.next.name, curTourNode.nextLength))
            curTourNode = curTourNode.next

    def nearest_neighbor(self, startNode: str):
        self.headTourNode = Node
        self.tourLength = 0
        self.suc = True
        curNode: Node = self.graph.nodes.get(startNode)
        if curNode is None:
            print("Failed to find start node {}".format(startNode))
            self.suc = False
            return
        tailTourNode: TourNode = None
        curNode.visited = True
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
            curNode = None
            if nextNode is None:
                continue
            nextNode.visited = True
            tailTourNode.next = TourNode(nextNode.name)
            tailTourNode.nextLength = nextEdgeLength
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
            self.tourLength = self.tourLength + edgeLen

    def getEdgeLength(self, endpoint1: str, endpoint2: str):
        if endpoint1 == endpoint2:
            return 0
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
                        self.getEdgeLength(firstTourNode.next.name,  secondTourNode.next.name)
                    if linkLenSum > swappedLinkLenSum:
                        if (optTourNode1 is None) or (lenDecrease < (linkLenSum - swappedLinkLenSum)):
                            optTourNode1 = firstTourNode
                            optTourNode2 = secondTourNode
                            lenDecrease = linkLenSum - swappedLinkLenSum
                    secondTourNode = secondTourNode.next
                firstTourNode = firstTourNode.next
            if optTourNode1 is None:
                isLocalMinimum = True
                continue
            print("current tour length: {}".format(self.tourLength))
            print("swap link {}->{}, {}->{}".format(optTourNode1.name, optTourNode1.next.name, optTourNode2.name, optTourNode2.next.name))
            print("tour length decrease: {}".format(lenDecrease))
            v = optTourNode1
            w = optTourNode1.next
            x = optTourNode2
            u = optTourNode2.next
            xPrevious = x.previous

            # do the 2OPT swap
            v.next = x
            v.nextLength = self.getEdgeLength(v.name, x.name)
            x.previous = v
            x.previousLength = v.nextLength
            w.next = u
            w.nextLength = self.getEdgeLength(w.name, u.name)
            u.previous = w
            u.previousLength = w.nextLength
            # flip the link direction from x, to w
            curFlipNode = x
            curFlipNodePrevious = xPrevious
            while curFlipNode.name != w.name:
                curFlipNode.next = curFlipNodePrevious
                curFlipNode.nextLength = curFlipNodePrevious.nextLength
                curFlipNodePrevious = curFlipNodePrevious.previous
                curFlipNode.next.previous = curFlipNode
                curFlipNode.next.previousLength = curFlipNode.nextLength
                curFlipNode = curFlipNode.next
            self.tourLength = self.tourLength - lenDecrease
            self.dumpTour()

