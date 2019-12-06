from utils.utils import *
from enum import Enum
import random
from collections import deque


class Item:
    def __init__(self):
        self.name = None
        self.possibleValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.connectedItems = list()
        self.row = None
        self.column = None


class SudokoGame:

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
        board = Utils.createArray([9, 9])
        for i in range(0, 9):
            for j in range(0, 9):
                curItem = Item()
                curItem.row = i
                curItem.column = j
                board[i][j] = curItem

        for i in range(0, 9):
            for j in range(0, 9):
                curItem : Item = board[i][j]
                curItem.connectedItems = self.getConnectedItems(board, i, j)
        return board

    def updateGraph_DFS_Recursive(self, item: Item, board):
        for connectedItem in item.connectedItems:
            if connectedItem.possibleValues.count(item.name) > 0:
                connectedItem.possibleValues.remove(item.name)
                if len(connectedItem.possibleValues) == 1:
                    connectedItem.name = connectedItem.possibleValues[0]
                    self.updateGraph_DFS_Recursive(connectedItem, board)

    def verifyBoard(self, board):
        for i in range(0, 9):
            for j in range(0, 9):
                item: Item = board[i][j]
                if len(item.possibleValues) == 0:
                    return False
                if item.name is not None:
                    if len(item.possibleValues) != 1:
                        return False
                    if item.possibleValues[0] != item.name:
                        return False
                    for connectedItem in item.connectedItems:
                        if connectedItem.name == item.name:
                            return False
        return True

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

        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(nums)

        # fill 3 diagonal 3 * 3 box first
        for c in range(0, 3):
            start = c * 3
            ii = 0
            for i in range(start, start + 3):
                for j in range(start, start + 3):
                    item: Item = board[i][j]
                    ii = ii + 1
                    item.name = nums[ii - 1]
                    item.possibleValues.clear()
                    item.possibleValues.append(item.name)
                    self.updateGraph_DFS_Recursive(item, board)

        # fill rest of matrices
        for iStart in range(0, 3):
            for jStart in range(0, 3):
                checkItem: Item = board[iStart * 3][jStart * 3]
                if checkItem.name is not None:
                    continue
                for i in range(iStart * 3, iStart * 3 + 3):
                    for j in range(jStart * 3, jStart * 3 + 3):
                        # create a temporary board to find out the good value to fill the board
                        tempBoard = copy.deepcopy(board)
                        item: Item = tempBoard[i][j]
                        for value in item.possibleValues:
                            item.name = value
                            item.possibleValues.clear()
                            item.possibleValues.append(item.name)
                            self.updateGraph_DFS_Recursive(item, tempBoard)
                            if self.verifyBoard(tempBoard):
                                board = tempBoard
                                break

        print("final board")
        Utils.dumpMatrix(board, 9, 9, lambda item: item.name)
        assert(self.verifyBoard(board))

        # assert(self.isBoardAllFilled(board))

sudokoGame = SudokoGame()
for i in range(100):
    print("start new game [%d]" % i)
    sudokoGame.startNewGame()
    print("end new game [%d]" % i)
