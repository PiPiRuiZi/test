# -*- coding:utf-8 -*-
# @Time    : 2021/08/03 11:44
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : testDevision.py
# @Software: PyCharm
import unittest
from calc import Calc


class testDevision(unittest.TestCase):
    def test_devision1(self):
        num1 = 0
        num2 = 21
        expect = 0

        calc = Calc()
        result = calc.devision(num1, num2)

        # 断言
        self.assertEqual(expect, result)

    def test_devision2(self):
        num1 = 80
        num2 = 20
        expect = 4

        calc = Calc()
        result = calc.devision(num1, num2)

        # 断言
        self.assertEqual(expect, result)

    def test_devision3(self):
        num1 = 40
        num2 = -20
        expect = -2

        calc = Calc()
        result = calc.devision(num1, num2)

        # 断言
        self.assertEqual(expect, result)

    def test_devision4(self):
        num1 = -30
        num2 = 3
        expect = -10

        calc = Calc()
        result = calc.devision(num1, num2)

        # 断言
        self.assertEqual(expect, result)

    def test_devision5(self):
        num1 = -60
        num2 = -3
        expect = 20

        calc = Calc()
        result = calc.devision(num1, num2)

        # 断言
        self.assertEqual(expect, result)

    def test_devision6(self):
        num1 = -50
        num2 = -50
        expect = 1

        calc = Calc()
        result = calc.devision(num1, num2)

        # 断言
        self.assertEqual(expect, result)
