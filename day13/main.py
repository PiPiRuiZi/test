# -*- coding:utf-8 -*-
# @Time    : 2021/08/03 11:20
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : main.py
# @Software: PyCharm
"""
    报告：
        1.加载器：加载所有测试用例并得到所有用例
        2.使用运行器运行这些测试用例并生成报告
    任务2：
        减乘除：进行测试（）
        实现报告的邮件发送
"""
from HTMLTestRunner import HTMLTestRunner
import unittest

tests = unittest.defaultTestLoader.discover(r"G:\文档\python\day13", pattern="test*.py")

runner = HTMLTestRunner.HTMLTestRunner(
    title="计算机的测试报告",
    description="包括加减乘除所有的测试用例",
    verbosity=1,
    stream=open(r"计算机测试报告.html", mode="w+", encoding="utf-8")
)

runner.run(tests)
