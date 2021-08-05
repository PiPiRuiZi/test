# -*- coding:utf-8 -*-
# @Time    : 2021/08/05 16:17
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : test_bank_take_money.py
# @Software: PyCharm
import unittest
from bank_system import *
from ddt import ddt
from ddt import data
from ddt import unpack

origin = [
    [10000002, "654321", 10, 3],
    [10000001, "123456", 9401, 2],
    [10000003, "111111", 100, 1],
    [10000004, "111111", 100, 0],
    [10288083, "123456", 1, 3]
]

@ddt
class TestBank_take_money(unittest.TestCase):
    @data(*origin)
    @unpack
    def test_take_money(self, account, password, money, expect):
        result = bank_take_money(account, password, money)
        self.assertEqual(result, expect)