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
        {"username": "qiaoyueyang", "passwd": "admin", "expect": "Teacher manager"},
        # {"username": "zhangdianlu", "passwd": "root", "expect": "Teacher manager"},
        # {"username": "caoshiming", "passwd": "admin", "expect": "Teacher manager"},
        # {"username": "jason", "passwd": "admin", "expect": "Teacher manager"},
        # {"username": "liyan", "passwd": "admin", "expect": "Teacher manager"}
    ]

    login_error_data = [
        {"username": "qiaoyueyang", "passwd": "admin1", "expect": "账户名错误或密码错误!别瞎弄!"},
        # {"username": "zhangdianlu", "passwd": "root1", "expect": "账户名错误或密码错误!别瞎弄!"},
        # {"username": "caoshiming", "passwd": "admin1", "expect": "账户名错误或密码错误!别瞎弄!"},
        # {"username": "jason", "passwd": "admin1", "expect": "账户名错误或密码错误!别瞎弄!"},
        # {"username": "liyan", "passwd": "admin1", "expect": "账户名错误或密码错误!别瞎弄!"}
    ]
