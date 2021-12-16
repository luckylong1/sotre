from Calc import Calc
from unittest import TestCase

class TestDevision(TestCase):

    def testDevision1(self):

        a = 5
        b = 1
        c = 5

        calc = Calc()
        s = calc.devision(a,b)

        self.assertEqual(s,c)

    def testDevision2(self):
        a = 10
        b = 2
        c = 5

        calc = Calc()
        s = calc.devision(a, b)

        self.assertEqual(s, c)

    def testDevision3(self):
        a = 30
        b = 5
        c = 5

        calc = Calc()
        s = calc.devision(a, b)

        self.assertEqual(s, c)
