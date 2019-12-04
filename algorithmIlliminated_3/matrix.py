
def createMatrix(rows, columns):
    m = [[None for i in range(columns)] for j in range(rows)]
    cnt = 0
    for row in range(0, rows):
        for column in range(0, columns):
            cnt = cnt + 1
            m[row][column] = cnt
    return m


def dumpMatrix(m, rows, columns, fn=lambda a: a):
    for i in range(0, rows):
        for j in range(0, columns):
            print("%5d" % fn(m[i][j]), end="")
        print("")


def testMatrix():
    rows = 5
    columns = 8
    m = createMatrix(rows, columns)
    myfn = lambda a: a * 2
    dumpMatrix(m, rows, columns, lambda a : a *  a)


testMatrix()

