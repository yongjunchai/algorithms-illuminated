from utils.utils import *
from enum import Enum
import random
from collections import deque


class Level(Enum):
    EASY = 1
    NORMAL = 2
    HARD = 3


class Item:
    def __init__(self):
        self.name = None
        self.possibleValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.connectedItems = list()
        self.visited = False


class Config:
    def __init__(self):
        self.level = Level.EASY


class SudokoGame:
    def __init__(self):
        self.config = Config()

    def clearVisitedFlag(self, board):
        for i in range(0, 9):
            for j in range(0, 9):
                curItem : Item = board[i][j]
                curItem.visited = False

    def getConnectedItems(self, board, row, column):
        # connect items of same row
        items = []
        for j in range(0, 9):
            if j == column:
                continue
            items.append(board[row][j])
        # connect items of same column
        for i in range(0, 9):
            if i == row:
                continue
            items.append(board[i][column])
        # connect items of same small board
        starRow = int(row / 3)
        startCol = int(column / 3)
        for i in range(starRow, starRow + 3):
            for j in range(startCol, startCol + 3):
                if i == row or j == column:
                    continue
                items.append(board[i][j])
        return items

    def createEmptyBorad(self):
        """
        create a new 9 * 9 sudoko board/graph with board item relationship set up
        """
        board = Utils.createArray([9, 9], Item())
        for i in range(0, 9):
            for j in range(0, 9):
                curItem : Item = board[i][j]
                curItem.connectedItems = self.getConnectedItems(board, i, j)
        return board

    def pickRndValue(self, item: Item):
        item.name = item.possibleValues[int(len(item.possibleValues) * random.random())]
        item.possibleValues.clear()
        item.possibleValues.append(item.name)

    def updateGraph(self, board, item: Item):
        assert(item.name is not None)
        self.clearVisitedFlag(board)
        queue = deque()
        item.visited = True
        for connectedItem in item.connectedItems:
            queue.append((connectedItem, item.name))
        while len(queue) > 0:
            t = queue.popleft()
            curItem : Item = t[0]
            valueToRemove = t[1]
            if curItem.visited:
                continue
            curItem.visited = True
            assert (curItem.name != valueToRemove)
            if curItem.possibleValues.count(valueToRemove) > 0:
                curItem.possibleValues.remove(valueToRemove)
                assert(len(curItem.possibleValues) > 0)
                if len(curItem.possibleValues) == 1:
                    for connectedItem in curItem.connectedItems:
                        if connectedItem.visited:
                            continue
                        queue.append((connectedItem, curItem.possibleValues[0]))

    def startNewGame(self):
        board = self.createEmptyBorad()

        # based on level set init filled values on board
        itemsToFill = 0
        if self.config.level == Level.EASY:
            itemsToFill = 50
        elif self.config.level == Level.NORMAL:
            itemsToFill = 40
        else:
            itemsToFill = 20

        for i in range(0, itemsToFill):
            row = int(9 * random.random())
            col = int(9 * random.random())
            curItem : Item = board[row][col]
            if curItem.name is not None:
                continue
            self.pickRndValue(curItem)
            self.updateGraph(board, curItem)

        # start to move forward step by step
        Utils.dumpMatrix(board, 9, 9, lambda item: item.name)


sudokoGame = SudokoGame()
sudokoGame.startNewGame()