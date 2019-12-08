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

class Parameter:
    def __init__(self, startI: int, startJ: int, i: int, j: int, index: int):
        self.startI = startI
        self.startJ = startJ
        self.i = i
        self.j = j
        self.index = index

class SudokoGame:
    def __init__(self):
        pass

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

    def updateGraph_DFS_Recursive(self, item: Item):
        for connectedItem in item.connectedItems:
            if connectedItem.possibleValues.count(item.name) > 0:
                connectedItem.possibleValues.remove(item.name)
                if len(connectedItem.possibleValues) == 1:
                    connectedItem.name = connectedItem.possibleValues[0]
                    self.updateGraph_DFS_Recursive(connectedItem)

    def updateGraph_DFS_Iterative(self, item: Item):
        stack = deque()
        for connectedItem in item.connectedItems:
            stack.append((connectedItem, item.name))
        while len(stack) > 0:
            t = stack.pop()
            curItem: Item = t[0]
            valueToRemove = t[1]
            if curItem.possibleValues.count(valueToRemove) > 0:
                curItem.possibleValues.remove(valueToRemove)
                if len(curItem.possibleValues) == 1:
                    curItem.name = curItem.possibleValues[0]
                    for connectedItem in curItem.connectedItems:
                        stack.append((connectedItem, curItem.name))

    def updateGraph_BFS_Iterative(self, item: Item):
        queue = deque()
        for connectedItem in item.connectedItems:
            queue.append((connectedItem, item.name))
        while len(queue) > 0:
            t = queue.popleft()
            curItem: Item = t[0]
            valueToRemove = t[1]
            if curItem.possibleValues.count(valueToRemove) > 0:
                curItem.possibleValues.remove(valueToRemove)
                if len(curItem.possibleValues) == 1:
                    curItem.name = curItem.possibleValues[0]
                    for connectedItem in curItem.connectedItems:
                        queue.append((connectedItem, curItem.name))


    def verifyBoard(self, board):
        for i in range(0, 9):
            for j in range(0, 9):
                item: Item = board[i][j]
                if len(item.possibleValues) == 0:
                    return False
                if item.name is not None:
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

    def fillRemaining(self, startI: int, startJ: int, i: int, j: int, board):
        if j > 2:
            i = i + 1
            j = 0
        if i > 2:
            startJ = startJ + 1
            i = 0
        if startI == startJ:
            startJ = startJ + 1
        if startJ > 2:
            startI = startI + 1
            startJ = 0
        if startI > 2:
            return True
        item: Item = board[startI * 3 + i][startJ * 3 + j]
        for value in item.possibleValues:
            isGoodToFit = True
            for connectedItem in item.connectedItems:
                if value == connectedItem.name:
                    isGoodToFit = False
                    break
            if not isGoodToFit:
                continue
            item.name = value
            if self.fillRemaining(startI, startJ, i, j + 1, board):
                item.possibleValues.clear()
                item.possibleValues.append(value)
                break
            item.name = None
        return item.name is not None

    def fillRemaining_iterative(self, board):
        stack = deque()
        stack.append(Parameter(0, 0, 0, 0, 0))
        while len(stack) > 0:
            parameter = stack.pop()
            startI = parameter.startI
            startJ = parameter.startJ
            i = parameter.i
            j = parameter.j
            index = parameter.index
            if j > 2:
                i = i + 1
                j = 0
            if i > 2:
                startJ = startJ + 1
                i = 0
            if startI == startJ:
                startJ = startJ + 1
            if startJ > 2:
                startI = startI + 1
                startJ = 0
            if startI > 2:
                return

            item: Item = board[startI * 3 + i][startJ * 3 + j]
            if index > len(item.possibleValues) - 1:
                item.name = None
                continue
            stack.append(Parameter(startI, startJ, i, j, index + 1))
            value = item.possibleValues[index]
            isGoodToFit = True
            for connectedItem in item.connectedItems:
                if value == connectedItem.name:
                    isGoodToFit = False
                    break
            if not isGoodToFit:
                continue
            item.name = value
            stack.append(Parameter(startI, startJ, i, j + 1, 0))

    def startNewGame(self):
        board = self.createEmptyBorad()

        # fill 3 diagonal 3 * 3 box first
        for c in range(0, 3):
            start = c * 3
            nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            random.shuffle(nums)
            ii = 0
            for i in range(start, start + 3):
                for j in range(start, start + 3):
                    item: Item = board[i][j]
                    item.name = nums[ii]
                    ii = ii + 1
                    item.possibleValues.clear()
                    item.possibleValues.append(item.name)
                    self.updateGraph_BFS_Iterative(item)
        self.fillRemaining(0, 0, 0, 0, board)
        print("final board")
        Utils.dumpMatrix(board, 9, 9, lambda item: item.name)
        assert(self.isBoardAllFilled(board))
        assert(self.verifyBoard(board))

sudokoGame = SudokoGame()
startMilli = current_milli_time()
for i in range(100):
    print("start new game [%d]" % i)
    sudokoGame.startNewGame()
    print("end new game [%d]" % i)
endMilli = current_milli_time()
print("time used [%d] milliseconds" % (endMilli - startMilli))