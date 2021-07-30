# -*- coding:utf-8 -*-
class Chef:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def steam_rice(self):
        print("正在蒸饭...")


class Son(Chef):
    def cook(self):
        print("正在炒菜...")


class Grandson(Son):
    def steam_rice(self):
        print("蒸饭")

    def cook(self):
        print("炒菜")

class Test:
    t = Grandson("赵瑞", 21)
    name = t.get_name()
    age = t.get_age()
    print("我叫{}， 今年{}岁".format(name, age))
    t.cook()
    t.steam_rice()
