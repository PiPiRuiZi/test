# -*- coding:utf-8 -*-
class Person:
    def __init__(self, name, sex, age):
        self.__name = name
        self.__sex = sex
        self.__age = age

    def get_name(self):
        return self.__name

    def get_sex(self):
        return self.__sex

    def get_age(self):
        return self.__age


class Worker(Person):
    def work(self):
        print("我是工人，我叫{}，性别{}，今年{}岁，正在工作中...".format(super().get_name(), super().get_sex(), super().get_age()))


class Student(Person):
    def __init__(self, name, sex, age, id):
        super().__init__(name, sex, age)
        self.__id = id

    def study(self):
        print("我是学生中，我叫{}，性别{}，今年{}岁，学号是{}, 正在学习中...".format(super().get_name(), super().get_sex(),
                                                             super().get_age(), self.__id))


class Test:
    worker = Worker("张三", "男", 30)
    worker.work()
    stu = Student("赵瑞", "男", 21, "0405180346")
    stu.study()
