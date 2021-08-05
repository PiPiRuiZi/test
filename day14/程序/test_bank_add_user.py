# -*- coding:utf-8 -*-
# @Time    : 2021/08/05 15:07
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : test_bank_add_user.py
# @Software: PyCharm
import unittest
from HTMLTestRunner import HTMLTestRunner
from bank_system import *
from ddt import ddt
from ddt import data
from ddt import unpack

origin = [
    ["张三", "123456", "100", "中国", "上海", "太白路", "d001"],
    ["张三1", "123456", "1001", "中国1", "上海1", "太白路1", "d0011"],
    ["张三2", "123456", "1002", "中国2", "上海2", "太白路2", "d0012"],
    ["张三3", "123456", "1003", "中国3", "上海3", "太白路3", "d0013"],
]


@ddt  # 注解，注释这个类是参数化类
class TestBank_add_user(unittest.TestCase):
    @data(*origin)  # 引入数据源
    @unpack  # 拆分数据源
    def test_add_user(self, username, password, money, country, province, street, door):
        # 调用被测方法
        result = bank_add_user(username, password, money, country, province, street, door)
        # 断言
        self.assertNotEqual(result, 0)


if __name__ == "__main__":
    tests = unittest.defaultTestLoader.discover(r"G:\文档\python\day14", pattern="test_bank_add_user.py")
    runner = HTMLTestRunner.HTMLTestRunner(
        title="银行开户的测试报告",
        description="开户测试",
        verbosity=1,
        stream=open(r"银行开户的测试报告.html", mode="w+", encoding="utf-8")
    )
    runner.run(tests)
