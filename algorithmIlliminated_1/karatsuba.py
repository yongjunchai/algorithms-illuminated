import math


class Karatsuba:
    def __init__(self):
        pass

    def fixLen(self, x: str, y: str):
        if len(x) < len(y):
            diff = len(y) - len(x)
            leadingZeros = ""
            for i in range(diff):
                leadingZeros = leadingZeros + "0"
            x = leadingZeros + x
        else:
            diff = len(x) - len(y)
            leadingZeros = ""
            for i in range(diff):
                leadingZeros = leadingZeros + "0"
            y = leadingZeros + y
        if len(x) % 2 != 0:
            x = "0" + x
            y = "0" + y
        return x, y

    def multiply(self, x: str, y: str):
        if len(x) == 1 and len(y) == 1:
            return int(x) * int(y)
        x, y = self.fixLen(x, y)
        n = len(x)
        halfLen = int(n / 2)
        a = x[0:halfLen]
        b = x[halfLen:]
        c = y[0:halfLen]
        d = y[halfLen:]
        p = int(a) + int(b)
        q = int(c) + int(d)
        ac = self.multiply(a, c)
        bd = self.multiply(b, d)
        pq = self.multiply(str(p), str(q))
        abcd = pq - ac - bd
        return int(math.pow(10, n)) * ac + int(math.pow(10, n / 2)) * abcd + bd





