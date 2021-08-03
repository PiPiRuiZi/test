# -*- coding:utf-8 -*-
# @Time    : 2021/08/03 11:43
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : testSubtra.py
# @Software: PyCharm
import unittest
from calc import Calc


class TestSubtra(unittest.TestCase):
    def test_subtra1(self):
        num1 = 0
        num2 = 0
        expect = 0

        calc = Calc()
        result = calc.subtra(num1, num2)

        # 断言
        self.assertEqual(expect, result)

    def test_subtra2(self):
        num1 = 56
        num2 = 23
        expect = 33

        calc = Calc()
        result = calc.subtra(num1, num2)

        # 断言
        self.assertEqual(expect, result)

    def test_subtra3(self):
        num1 = 23
        num2 = 30
        expect = -7

        calc = Calc()
        result = calc.subtra(num1, num2)

        # 断言
        self.assertEqual(expect, result)

    def test_subtra4(self):
        num1 = 0
        num2 = 30
        expect = -30

        calc = Calc()
        result = calc.subtra(num1, num2)

        # 断言
        self.assertEqual(expect, result)

    def test_subtra5(self):
        num1 = -60
        num2 = 30
        expect = -90

        calc = Calc()
        result = calc.subtra(num1, num2)

        # 断言
        self.assertEqual(expect, result)

    def test_subtra6(self):
        num1 = -23
        num2 = -30
        expect = 7

        calc = Calc()
        result = calc.subtra(num1, num2)

        # 断言
        self.assertEqual(expect, result)