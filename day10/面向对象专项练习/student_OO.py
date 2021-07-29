# -*- coding:utf-8 -*-
class Student:
    def __init__(self, name=None, age=0):
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

    def show_self(self):
        print("大家好，我叫{}，今年{}岁了".format(self.__name, self.__age))

    def compare_age(self, age):
        if self.__age > age:
            return "我同桌比我大{}岁！".format(self.__age-age)
        elif self.__age < age:
            return "我同桌比我小{}岁！".format(age-self.__age)
        else:
            return "我和同桌一样大！"
















