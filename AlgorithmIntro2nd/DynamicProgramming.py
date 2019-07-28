
class RodCutting:
    def __init__(self):
        self.prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        # optimal revenue
        self.r = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        # cut point
        self.s = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        # cut cost
        self.c = 1


    def cutRod(self, n):
        if n == 0:
            return 0
        q = -1
        i = 1
        while i <= n:
            q = max(q, self.prices[i - 1] + self.cutRod(n - i))
            i = i + 1
        return q

    def memoizedCutRod(self, n):
        i = 1
        while i <= n:
            self.r[i - 1] = -1
            i = i + 1
        return self.memoizedCutRodAux(n)

    def memoizedCutRodAux(self, n):
        if self.r[n - 1] >= 0:
            return self.r[n - 1]
        if n == 0:
            q = 0
        else:
            q = -1
            i = 1
            while i <= n:
                q = max(q, self.prices[i - 1] + self.memoizedCutRodAux(n - i))
                i = i + 1
            self.r[n - 1] = q
        return q

    def extendedMemoizedCutRodAux(self, n):
        if self.r[n - 1] >= 0:
            return self.r[n - 1]
        if n == 0:
            q = 0
        else:
            q = -1
            i = 1
            while i <= n:
                if q < self.prices[i - 1] + self.extendedMemoizedCutRodAux(n - i):
                    q = self.prices[i - 1] + self.extendedMemoizedCutRodAux(n - i)
                    self.s[n - 1] = i
                    self.r[n - 1] = q
                i = i + 1
        return q

    def extendedMemoizedCutRod(self, n):
        i = 1
        while i <= n:
            self.r[i - 1] = -1
            i = i + 1
        self.extendedMemoizedCutRodAux(n)
        while n > 0:
            print(self.s[n - 1])
            n = n - self.s[n - 1]

    def bottomUpCutRod(self, n):
        self.r[0] = 0
        j = 1
        while j <= n:
            q = -1
            i = 1
            while i <= j:
                q = max(q, self.prices[i - 1] + self.r[j - i])
                i = i + 1
            self.r[j] = q
            j = j + 1
        return self.r[n]

    def bottomUpCutRod_WithCutCost(self, n):
        self.r[0] = 0
        j = 1
        while j <= n:
            q = -1
            i = 1
            while i <= j:
                q = max(q, self.prices[i - 1] + self.r[j - i] - self.c)
                i = i + 1
            self.r[j] = q
            j = j + 1
        return self.r[n]

    def extendedBottomUpCutRod(self, n):
        self.r[0] = 0
        j = 1
        while j <= n:
            q = -1
            i = 1
            while i <= j:
                if q < self.prices[i - 1] + self.r[j - i]:
                    q = self.prices[i - 1] + self.r[j - i]
                    self.s[j] = i
                    self.r[j] = q
                i = i + 1
            j = j + 1
        return self.r[n]

    def printCutSolution(self, n):
        self.extendedBottomUpCutRod(n)
        while n > 0:
            print(self.s[n])
            n = n - self.s[n]

class FibonaciNum:
    @staticmethod
    def nth(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        i = 1
        cur = 1
        pre = 0
        while i < n:
            i = i + 1
            tmp = cur
            cur = cur + pre
            pre = tmp
        return cur

def fibN(n):
    fibs = []
    for i in range(0, n+1):
        fibs.append(FibonaciNum.nth(i))
    print(fibs)

class Matrix:
    def __init__(self, row, column):
        self.row = row
        self.column = column

class MaxtrixChainOrder:
    def __init__(self):
        self.dimensions = [30, 35, 15, 5, 10, 20, 25]
        self.n = len(self.dimensions) - 1
        self.m = [[0 for col in range(self.n)] for row in range(self.n)]
        self.s = [[0 for col in range(self.n - 1)] for row in range(self.n - 1)]
        self.stack = list()
        self.complexity = 0

    def matrixChainOrderRecursive(self, i, j):
        if i == j:
            return 0
        if i > j:
            print("error, wrong range i > j")
            return 0
        minVal = -1
        k = i
        while k < j:
            val = self.matrixChainOrderRecursive(i, k) + self.matrixChainOrderRecursive(k + 1, j) \
                  + self.dimensions[i - 1] * self.dimensions[k] * self.dimensions[j]
            if minVal == -1 or minVal > val:
                minVal = val
            k = k + 1
        return minVal

    def matrixChainOrder(self):
        curLen = 2
        while curLen <= self.n:
            i = 1
            while i <= self.n - curLen + 1:
                j = i + curLen - 1
                self.m[i - 1][j - 1] = -1
                k = i
                while k <= j - 1:
                    q = self.m[i - 1][k - 1] + self.m[k][j - 1] + self.dimensions[i - 1] * self.dimensions[k] \
                        * self.dimensions[j]
                    if self.m[i - 1][j - 1] == -1 or self.m[i - 1][j - 1] > q:
                        self.m[i - 1][j - 1] = q
                        self.s[i - 1][j - 2] = k
                    k = k + 1
                i = i + 1
            curLen = curLen + 1
        return self.m[0][self.n - 1]

    def printOptimalParens(self, s, i, j):
        if i == j:
            print("A" + str(i) + "  ", end="")
        else:
            print("(", end="")
            self.printOptimalParens(s, i, s[i - 1][j - 2])
            self.printOptimalParens(s, s[i - 1][j - 2] + 1, j)
            print(")", end="")

    def matrixChainMultiply(self, s, i, j):
        if i == j:
            self.stack.append(Matrix(self.dimensions[i - 1], self.dimensions[i]))
        else:
            self.matrixChainMultiply(s, i, s[i - 1][j - 2])
            self.matrixChainMultiply(s, s[i - 1][j - 2] + 1, j)
            # pop two matrix from the stack and calculate and push a new one
            matrixRight = self.stack.pop()
            matrixLeft = self.stack.pop()
            if matrixRight.row != matrixLeft.column:
                print("error matrix size")
                return
            self.complexity = self.complexity + matrixLeft.row * matrixLeft.column * matrixRight.column
            matrixNew = Matrix(matrixLeft.row, matrixRight.column)
            self.stack.append(matrixNew)

