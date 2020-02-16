

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
        return self.findLocalMinimum_internal(matrix, rows, columns, 0, 0)

    def findLocalMinimum_internal(self, matrix, rows: int, columns: int, startRow: int, startColumn: int):
        """

        :param matrix:
        :param rows: rows inside the small rectangle
        :param columns: columns inside the small rectangle
        :param startRow: bottom left of the small rectangle inside the matrix
        :param startColumn: bottom left of the small rectangle inside the matrix
        :return: row, column of local minimum
        """
        if rows < 4 or columns < 4:
            for i in range(rows):
                for j in range(columns):
                    if FindLocalMinimum.isLocalMinimum(matrix, rows, columns, startRow, startColumn, i, j):
                        return startRow + i, startColumn + j
            return None, None
        midRow = startRow + int(rows / 2)
        midCol = startColumn + int(columns / 2)
        midPlusRow = midRow + 1
        midPlusCol = midCol + 1
        midRowMinimum_row, midRowMinimum_column = self.findMinimum_of_row(matrix, columns, midRow, startColumn)
        midColMinimum_row, midColMinimum_column = self.findMinimum_of_column(matrix, rows, startRow, midCol)
        midPlusRowMinimum_row, midPlusRowMinimum_column = self.findMinimum_of_row(matrix, columns, midPlusRow, startColumn)
        midPlusColMinimum_row, midPlusColMinimum_column = self.findMinimum_of_column(matrix, rows, startRow, midPlusCol)
        points = [(midRowMinimum_row, midRowMinimum_column),
                  (midColMinimum_row, midColMinimum_column),
                  (midPlusRowMinimum_row, midPlusRowMinimum_column),
                  (midPlusColMinimum_row, midPlusColMinimum_column)
                  ]
        minRow, minCol = self.findMinimum(matrix, points)
        if minRow <= midRow and minCol <= midCol:
            # bottom left quadrant
            return self.findLocalMinimum_internal(matrix, midRow - startRow + 1, midCol - startColumn + 1, startRow, startColumn)
        elif minRow <= midRow and minCol >= midPlusCol:
            # bottom right quadrant
            return self.findLocalMinimum_internal(matrix, midRow - startRow + 1, columns - (midPlusCol - startColumn), startRow, midPlusCol)
        elif minRow >= midPlusRow and minCol <= midCol:
            # top left quadrant
            return self.findLocalMinimum_internal(matrix, rows - (midPlusRow - startRow), midCol - startColumn + 1, midPlusRow, startColumn)
        else:
            # top right quadrant
            return self.findLocalMinimum_internal(matrix, rows - (midPlusRow - startRow), columns - (midPlusCol - startColumn), midPlusRow, midPlusCol)

    def findMinimum(self, maxtrix, points: list):
        minRow, minCol = points[0][0], points[0][1]
        for i in range(1, len(points)):
            if maxtrix[minRow][minCol] > maxtrix[points[i][0]][points[i][1]]:
                minRow = points[i][0]
                minCol = points[i][1]
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

