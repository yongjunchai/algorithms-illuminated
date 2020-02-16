from enum import Enum


class Quadrant(Enum):
    BottomLeft = 0
    BottomRight = 1
    TopLeft = 2
    TopRight = 3

# problem 3.4
class FindLocalMinimum:
    def __init__(self):
        pass

    @staticmethod
    def isLocalMinimum(matrix, rows: int, cols: int, startRow: int, startColumn: int, rowOffset: int, colOffset: int):
        minRow = startRow + rowOffset
        minCol = startColumn + colOffset
        value = matrix[minRow][minCol]
        if minRow - 1 >= startRow:
            if value > matrix[minRow - 1][minCol]:
                return False
        if minRow + 1 < startRow + rows:
            if value > matrix[minRow + 1][minCol]:
                return False
        if minCol - 1 >= startColumn:
            if value > matrix[minRow][minCol - 1]:
                return False
        if minCol + 1 < startColumn + cols:
            if value > matrix[minRow][minCol + 1]:
                return False
        return True

    def findLocalMinimum(self, matrix, rows: int, columns: int):
        """
        solve the issue through divide-and-conquer
        :param matrix:
        :param rows:
        :param columns:
        :return: index of the local minimum (row, column)
        """
        return self.findLocalMinimum_internal(matrix, rows, columns, 0, 0, None)

    def findLocalMinimum_internal(self, matrix, rows: int, columns: int, startRow: int, startColumn: int, quadrant: Quadrant):
        """
        :param matrix:
        :param rows: rows inside the small rectangle
        :param columns: columns inside the small rectangle
        :param startRow: bottom left of the small rectangle inside the matrix
        :param startColumn: bottom left of the small rectangle inside the matrix
        :return: row, column of local minimum
        """
        if rows < 4 or columns < 4:
            iStart = 0
            jStart = 0
            if quadrant == Quadrant.BottomLeft:
                rows = rows - 1
                columns = columns - 1
            elif quadrant == Quadrant.BottomRight:
                iStart = 1
                jStart = 1
                rows = rows - 1
            elif quadrant == Quadrant.TopLeft:
                iStart = 1
                columns = columns - 1
            else:
                iStart = 1
                jStart = 1
            for i in range(iStart, rows):
                for j in range(jStart, columns):
                    if FindLocalMinimum.isLocalMinimum(matrix, rows, columns, startRow, startColumn, i, j):
                        return startRow + i, startColumn + j
            return None, None
        midRow = startRow + int(rows / 2)
        midCol = startColumn + int(columns / 2)
        midRowMinimum_row, midRowMinimum_column = self.findMinimum_of_row(matrix, columns, midRow, startColumn)
        midColMinimum_row, midColMinimum_column = self.findMinimum_of_column(matrix, rows, startRow, midCol)
        minRow, minCol = midRowMinimum_row, midRowMinimum_column
        if matrix[minRow][minCol] > matrix[midColMinimum_row][midColMinimum_column]:
            minRow, minCol = midColMinimum_row, midColMinimum_column
        # roll downhill to the quadrant
        if minRow - 1 >= startRow:
            if matrix[minRow - 1][minCol] < matrix[minRow][minCol]:
                if minCol <= midCol:
                    # bottom left quadrant
                    return self.findLocalMinimum_internal(matrix, midRow - startRow + 1, midCol - startColumn + 1, startRow, startColumn, Quadrant.BottomLeft)
                else:
                    # bottom right quadrant
                    return self.findLocalMinimum_internal(matrix, midRow - startRow + 1, columns - (midCol - startColumn), startRow, midCol, Quadrant.BottomRight)
        if minRow + 1 < startRow + rows:
            if matrix[minRow + 1][minCol] < matrix[minRow][minCol]:
                if minCol <= midCol:
                    # top left quadrant
                    return self.findLocalMinimum_internal(matrix, rows - (midRow - startRow), midCol - startColumn + 1, midRow, startColumn, Quadrant.TopLeft)
                else:
                    # top right quadrant
                    return self.findLocalMinimum_internal(matrix, rows - (midRow - startRow), columns - (midCol - startColumn), midRow, midCol, Quadrant.TopRight)
        if minCol - 1 >= startColumn:
            if matrix[minRow][minCol - 1] < matrix[minRow][minCol]:
                if minRow <= midRow:
                    # bottom left quadrant
                    return self.findLocalMinimum_internal(matrix, midRow - startRow + 1, midCol - startColumn + 1, startRow, startColumn, Quadrant.BottomLeft)
                else:
                    # top left quadrant
                    return self.findLocalMinimum_internal(matrix, rows - (midRow - startRow), midCol - startColumn + 1, midRow, startColumn, Quadrant.TopLeft)
        if minCol + 1 < startColumn + columns:
            if matrix[minRow][minCol + 1] < matrix[minRow][minCol]:
                if minRow <= midRow:
                    # bottom right quadrant
                    return self.findLocalMinimum_internal(matrix, midRow - startRow + 1, columns - (midCol - startColumn), startRow, midCol, Quadrant.BottomRight)
                else:
                    # top right quadrant
                    return self.findLocalMinimum_internal(matrix, rows - (midRow - startRow), columns - (midCol - startColumn), midRow, midCol,Quadrant.TopRight)
        return minRow, minCol

    def findMinimum_of_column(self, matrix, rows: int, startRow: int, startColumn: int):
        minRow, minCol = startRow, startColumn
        for i in range(1, rows):
            if matrix[minRow][minCol] > matrix[startRow + i][startColumn]:
                minRow = startRow + i
        return minRow, minCol

    def findMinimum_of_row(self, matrix, columns: int, startRow: int, startColumn: int):
        minRow, minCol = startRow, startColumn
        for i in range(1, columns):
            if matrix[minRow][minCol] > matrix[startRow][startColumn + i]:
                minCol = startColumn + i
        return minRow, minCol

