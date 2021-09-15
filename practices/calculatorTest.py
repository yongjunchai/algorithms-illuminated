import unittest
from practices.calculator import *


class MyTestCase(unittest.TestCase):
    def test_add(self):
        calculator: Calculator = Calculator()
        # self.assertEqual(11, calculator.calculate("5+6"))
        # self.assertEqual(110, calculator.calculate("50+60"))
        # self.assertEqual(1350, calculator.calculate("570+780"))
        # self.assertEqual(7, calculator.calculate("1+2*3"))
        # self.assertEqual(-12, calculator.calculate("1-13"))
        #self.assertEqual(1, calculator.calculate("1+2*3-6"))
        #self.assertEqual(21, calculator.calculate("1+2*3-6+20*3"))
        #self.assertEqual(95, calculator.calculate("1+2*3-6+20*5-6"))


if __name__ == '__main__':
    unittest.main()
