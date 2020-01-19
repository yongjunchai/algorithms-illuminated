import unittest
from algorithmIlliminated_1.karatsuba import *
import random
import math


class MyTestCase(unittest.TestCase):
    def test_something(self):
        karatsuba = Karatsuba()
        x = 1009
        y = 1001
        m = karatsuba.multiply(str(x), str(y))
        self.assertTrue(m == (x * y))
        for i in range(1024):
            a = int(math.pow(10, 15) + 1)
            b = int(math.pow(10, 15) * 9)
            self.assertTrue(len(str(a)) == len(str(b)))
            x = random.randint(a, b)
            y = random.randint(a, b)
            print(x)
            print(y)
            m = karatsuba.multiply(str(x), str(y))
            self.assertTrue(m == (x * y))



if __name__ == '__main__':
    unittest.main()
