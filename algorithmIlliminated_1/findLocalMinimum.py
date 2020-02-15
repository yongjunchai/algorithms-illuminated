

# problem 3.4
class FindLocalMinimum:
    def __init__(self):
        pass

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
        assert(rows == columns)
        assert(startRow == startColumn)
        assert(rows >= 2)
        if rows == 2:
            i00 = matrix[startRow][startColumn]
            i01 = matrix[startRow][startColumn + 1]
            i10 = matrix[startRow + 1][startColumn]
            i11 = matrix[startRow + 1][startColumn + 1]
            if i00 < i01 and i00 < i10:
                return startRow, startColumn
            if i01 < i00 and i01 < i11:
                return startRow, startColumn + 1
            if i10 < i00 and i10 < i11:
                return startRow + 1, startColumn
            return startRow + 1, startColumn + 1
        midRow = startRow + int(rows / 2)
        midCol = startColumn + int(columns / 2)
        midPlusRow = midRow + 1
        midPlusCol = midCol + 1
        





