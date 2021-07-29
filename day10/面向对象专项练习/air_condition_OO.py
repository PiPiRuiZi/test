# -*- coding:utf-8 -*-
class Air_condition:
    def __init__(self, brand="", price=""):
        self.__brand = brand
        self.__price = price

    def set_brand(self, brand):
        self.__brand = brand

    def set_price(self, price):
        self.__price = price

    def get_brand(self):
        return self.__brand

    def get_price(self):
        return self.__price

    def start(self):
        print("空调开机了")

    def timed_shutdown(self, time):
        print("空调将在{}分钟后自动关闭...".format(time))
