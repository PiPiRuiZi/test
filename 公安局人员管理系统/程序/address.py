# -*- coding:utf-8 -*-
# @Time    : 2021/08/04 17:16
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : address.py
# @Software: PyCharm
# 地址类
class Address:
    def __init__(self, country, province, street, door):
        self.country = country  # 国家
        self.province = province  # 省
        self.street = street  # 街道
        self.door = door  # 门牌号
