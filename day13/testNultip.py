# -*- coding:utf-8 -*-
# @Time    : 2021/08/03 11:44
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : testNultip.py
# @Software: PyCharm
import unittest
from calc import Calc


class testNultip(unittest.TestCase):
    def test_nultip1(self):
        num1 = 0
        num2 = 30
        expect = 0

        calc = Calc()
        result = calc.multip(num1, num2)

        # 断言
        self.assertEqual(expect, result)

    def test_nultip2(self):
        num1 = 5
        num2 = 5
        expect = 25

        calc = Calc()
        result = calc.multip(num1, num2)

        # 断言
        self.assertEqual(expect, result)

    def test_nultip3(self):
        num1 = 0
        num2 = 0
        expect = 0

        calc = Calc()
        result = calc.multip(num1, num2)

        # 断言
        self.assertEqual(expect, result)

    def test_nultip4(self):
        num1 = -25
        num2 = 3
        expect = -75

        calc = Calc()
        result = calc.multip(num1, num2)

        # 断言
        self.assertEqual(expect, result)

    def test_nultip5(self):
        num1 = -6
        num2 = -8
        expect = 48

        calc = Calc()
        result = calc.multip(num1, num2)

        # 断言
        self.assertEqual(expect, result)

    def test_nultip6(self):
        num1 = -54
        num2 = 0
        expect = 0

        calc = Calc()
        result = calc.multip(num1, num2)

        # 断言
        self.assertEqual(expect, result)
