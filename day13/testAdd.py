# -*- coding:utf-8 -*-
# @Time    : 2021/08/03 11:31
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : testAdd.py
# @Software: PyCharm
import unittest
from calc import Calc


class TestAdd(unittest.TestCase):
    def test_add1(self):
        num1 = 13
        num2 = 21
        expect = 34

        calc = Calc()
        result = calc.add(num1, num2)

        # 断言
        self.assertEqual(expect, result)

    def test_add2(self):
        num1 = 0
        num2 = 45
        expect = 45

        calc = Calc()
        result = calc.add(num1, num2)

        # 断言
        self.assertEqual(expect, result)

    def test_add3(self):
        num1 = 0
        num2 = 0
        expect = 0

        calc = Calc()
        result = calc.add(num1, num2)

        # 断言
        self.assertEqual(expect, result)

    def test_add4(self):
        num1 = -54
        num2 = 0
        expect = -54

        calc = Calc()
        result = calc.add(num1, num2)

        # 断言
        self.assertEqual(expect, result)

    def test_add5(self):
        num1 = -35
        num2 = 25
        expect = -10

        calc = Calc()
        result = calc.add(num1, num2)

        # 断言
        self.assertEqual(expect, result)

    def test_add6(self):
        num1 = -22
        num2 = -10
        expect = -32

        calc = Calc()
        result = calc.add(num1, num2)

        # 断言
        self.assertEqual(expect, result)