from Calc import Calc
from unittest import TestCase

class TestMulti(TestCase):

    def testMulti1(self):
        a = 12
        b = 5
        c = 60

        calc = Calc()
        s = calc.multi(a,b)

        self.assertEqual(s,c)

    def testMulti2(self):
        a = 18
        b = 2
        c = 36

        calc = Calc()
        s = calc.multi(a, b)

        self.assertEqual(s, c)

    def testMulti3(self):
        a = 1000000000000000000000000000000000000000000000000
        b = 10
        c = 10000000000000000000000000000000000000000000000000

        calc = Calc()
        s = calc.multi(a, b)

        self.assertEqual(s, c)

