# -*- coding:utf-8 -*-
# @Time    : 2021/08/06 15:03
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : 统计资产.py
# @Software: PyCharm
"""
    以下文件是用户的一些数据（姓名、年龄、净资产），要求使用数据库工具将文件中的数据写入到数据库中。并统计所有人的资产总和！
"""
import DBUtils
tool = DBUtils.DBUtils("localhost", "root", "111111", "excel2db_test")
data = tool.select("select sum(salary) from 用户数据", mode="one")
print("总资产为：{}".format(data[0]))
