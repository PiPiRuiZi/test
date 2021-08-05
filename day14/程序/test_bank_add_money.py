# -*- coding:utf-8 -*-
# @Time    : 2021/08/05 15:51
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : test_bank_add_money.py
# @Software: PyCharm
import unittest
from HTMLTestRunner import HTMLTestRunner
from bank_system import *
from ddt import ddt
from ddt import data
from ddt import unpack

origin = [
    [34257471, 100, 1],
    [40293083, 0.01, 1],
    [43302505, 0, 1],
    [48787682, -0.01, 1],
    [10000001, -100, 1],
    [10000002, 99999999999999, 1]
]


@ddt
class TextBank_add_money(unittest.TestCase):
    @data(*origin)
    @unpack
    def test_add_money(self, account, money, expect):
        result = bank_add_money(account, money)
        self.assertEqual(result, expect)


if __name__ == "__main__":
    tests = unittest.defaultTestLoader.discover(r"G:\文档\python\day14", pattern="test_bank_add_money.py")
    runner = HTMLTestRunner.HTMLTestRunner(
        title="银行的测试报告",
        description="测试",
        verbosity=1,
        stream=open(r"银行的测试报告.html", mode="w+", encoding="utf-8")
    )
    runner.run(tests)
