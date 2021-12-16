from unittest import TestCase
from Calc import Calc

class TestMinus(TestCase):

    def testMinus1(self):
        a = 9
        b = 10
        c = -1
        calc = Calc()
        s = calc.minus(a,b)

        self.assertEqual(s,c)

    def testMinus2(self):
        a = 8
        b = 7
        c = 1
        calc = Calc()
        s = calc.minus(a, b)

        self.assertEqual(s, c)

    def testMinus3(self):
        a = 20
        b = 10
        c = 10
        calc = Calc()
        s = calc.minus(a, b)

        self.assertEqual(s, c)