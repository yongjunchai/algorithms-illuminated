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
        self.row = None
        self.column = None


class Config:
    def __init__(self):
        self.level = Level.EASY


class SudokoGame:
    def __init__(self):
        self.config = Config()

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
        starRow = int(row / 3) * 3
        startCol = int(column / 3) * 3
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
                curItem.row = i
                curItem.column = j
                curItem.connectedItems = self.getConnectedItems(board, i, j)
        return board

    def pickRndValue(self, item: Item):
        assert(len(item.possibleValues) > 0)
        item.name = item.possibleValues[int(len(item.possibleValues) * random.random())]
        item.possibleValues.clear()
        item.possibleValues.append(item.name)

    def updateGraph_DFS_Recursive(self, item: Item):
        for connectedItem in item.connectedItems:
            assert(len(connectedItem.possibleValues) > 0)
            if connectedItem.possibleValues.count(item.name) > 0:
                connectedItem.possibleValues.remove(item.name)
                if len(connectedItem.possibleValues) == 1:
                    connectedItem.name = connectedItem.possibleValues[0]
                    self.updateGraph_DFS_Recursive(connectedItem)

    def verifyBoard(self, board):
        for i in range(0, 9):
            for j in range(0, 9):
                item: Item = board[i][j]
                assert(len(item.possibleValues) == 1)
                assert(item.possibleValues[0] == item.name)
                for connectedItem in item.connectedItems:
                    assert(connectedItem.name != item.name)

    def isBoardAllFilled(self, board):
        for i in range(0, 9):
            for j in range(0, 9):
                item: Item = board[i][j]
                if item.name is None:
                    return False
        return True


    def startNewGame(self):
        board = self.createEmptyBorad()
        Utils.dumpMatrix(board, 9, 9, lambda item: item.name)

        # based on level set init filled values on board
        itemsToFill = 0
        if self.config.level == Level.EASY:
            itemsToFill = 50
        elif self.config.level == Level.NORMAL:
            itemsToFill = 40
        else:
            itemsToFill = 20

        isBoardAllFilled = False
        step = 0
        while isBoardAllFilled is False:
            row = int(9 * random.random())
            col = int(9 * random.random())
            curItem : Item = board[row][col]
            if curItem.name is not None:
                continue
            step = step + 1
            self.pickRndValue(curItem)
            self.updateGraph_DFS_Recursive(curItem)
            print("[%d] step: pick up new item (%d, %d) =  %s " % (step, row + 1, col + 1, curItem.name))
            Utils.dumpMatrix(board, 9, 9, lambda item: item.name)
            isBoardAllFilled = self.isBoardAllFilled(board)

        self.verifyBoard(board)


sudokoGame = SudokoGame()
for i in range(100):
    print("start new game [%d]" % i)
    sudokoGame.startNewGame()
    print("end new game [%d]" % i)
