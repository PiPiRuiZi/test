# -*- coding:utf-8 -*-
# @Time    : 2021/08/04 14:52
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : student.py
# @Software: PyCharm
from person import Person
from DBUtils import DBUtils


# 学生类继承人类
class Student(Person):
    def __init__(self, iden):
        tool = DBUtils()
        sql = "select * from local where id='{}'".format(iden)
        data = tool.select(sql, mode="one")
        name = data[1]
        sex = data[2]
        age = data[3]
        passwd = data[4]
        status = data[5]
        country = data[6]
        province = data[7]
        street = data[8]
        door = data[9]
        date = data[10]
        immi_date = data[11]
        credit = data[12]
        culture = data[13]
        learn_num = data[14]
        # print(data)
        # print("name={}, sex={}, age={}, passwd={}, status={}, date={}, country={}, province={}, street={}, door={},"
        #       "immi_date={}, credit={}, culture={}, learn_num={}".format(name, sex, age, passwd, status, date,
        #                                                                  country, province, street, door, immi_date,
        #                                                                  credit, culture, learn_num))
        super().__init__(iden, name, sex, age, passwd, status, date, country, province, street, door)
        self.immi_date = immi_date  # 申请移民日期
        self.credit = credit  # 信誉程度
        self.culture = culture  # 文化程度
        self.learn_num = learn_num  # 学习次数

    def learn(self, num):  # 传入学习的级别
        if num - self.culture == 1:  # 学习的上一级内容是否已经达到
            tool = DBUtils()  # 学历增加
            sql = "update local set culture=culture+1 where id='{}'".format(self.iden)  # 更改地方数据库
            tool.update(sql)
            sql = "update state set culture=culture+1 where id='{}'".format(self.iden)  # 更改国家数据库
            tool.update(sql)
            self.culture += 1
            return 1
        elif num - self.culture > 1:  # 不能跨级学习
            return 2
        else:  # 已经学习过了
            return 3


if __name__ == "__main__":
    t = Student("tgmi9t43ygt4nvq7zmqlkiosee39caws")
