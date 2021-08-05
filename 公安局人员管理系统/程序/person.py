# -*- coding:utf-8 -*-
# @Time    : 2021/08/04 17:16
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : person.py
# @Software: PyCharm
from address import Address


# 人类继承地址类
class Person(Address):
    def __init__(self, iden, name, sex, age, passwd, status, date, country, province, street, door):
        self.iden = iden
        self.name = name
        self.sex = sex
        self.age = age
        self.passwd = passwd
        self.status = status
        self.date = date  # 注册日期
        super().__init__(country, province, street, door)
