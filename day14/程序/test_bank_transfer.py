# -*- coding:utf-8 -*-
# @Time    : 2021/08/05 16:28
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : test_bank_transfer.py
# @Software: PyCharm
import unittest
from bank_system import *
from ddt import ddt
from ddt import data
from ddt import unpack

origin = [
    [10796329, 23730200, 1, True],
    [11859218, 24113989, 5, True],
    [13774475, 24140878, 10, True],
    [19343052, 25213726, 3, True],
    [20213324, 26147889, 4, True],
]


@ddt
class TestBank_transfer(unittest.TestCase):
    @data(*origin)
    @unpack
    def test_bank_transfer(self, account, payee, s, expect):
        result = bank_transfer(account, payee, s)
        self.assertEqual(result, expect)
