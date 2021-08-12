# -*- coding:utf-8 -*-
# @Time    : 2021/08/12 11:15
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : initpage.py
# @Software: PyCharm
"""
    数据
"""
class Initpage:
    login_success_data = [
        {"username": "张三", "passwd": "123456", "expect": "Student Loginhahaha"},
        # {"username": "fuzhenyu", "passwd": "123456", "expect": "Student Login"},
        # {"username": "zhangyan", "passwd": "zhangyan", "expect": "Student Login"},
        # {"username": "何登勇", "passwd": "123456", "expect": "Student Login"},
        # {"username": "xiao", "passwd": "123456", "expect": "Student Login"}
    ]

    login_error_data = [
        {"username": "张三", "passwd": "654321", "expect": "账户名错误或密码错误!别瞎弄!"},
        # {"username": "fuzhenyu", "passwd": "654321", "expect": "账户名错误或密码错误!别瞎弄!"},
        # {"username": "zhangyan", "passwd": "654321", "expect": "账户名错误或密码错误!别瞎弄!"},
        # {"username": "何登勇", "passwd": "654321", "expect": "账户名错误或密码错误!别瞎弄!"},
        # {"username": "xiao", "passwd": "654321", "expect": "账户名错误或密码错误!别瞎弄!"}
    ]
