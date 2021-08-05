# -*- coding:utf-8 -*-
# @Time    : 2021/08/04 17:05
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : state_personnel_management.py
# @Software: PyCharm
from DBUtils import *
from student import Student
import time
import random


# 国家人员管理
class State_personnel_management:
    # 查询
    def inquire(self, iden):
        stu = Student(iden)
        info = """
        -------------------------------------
                      个人信息
        -------------------------------------
        身份证号={}
            姓名={}
            性别={}
            年龄={}
            密码={}
            生存状态={}（1代表生存，0代表死亡）
            注册日期={}
            国家={}
            省份={}
            街道={}
            门牌号={}
            申请移民时间={}（如果为None代表未申请）
            信誉程度={}
            文化程度={}
            学习次数={}
        -------------------------------------
        """
        print(info.format(iden, stu.name, stu.sex, stu.age, stu.passwd,
                          stu.status, stu.date, stu.country,
                          stu.province, stu.street, stu.door,
                          stu.immi_date, stu.credit, stu.culture,
                          stu.learn_num))

    # 录入
    def input(self, iden, name, sex, age, passwd, date, country, province, street, door,
              immi_date=None, credit=2, culture=0, learn_num=0, status=1):
        tool = DBUtils()
        sql = "select count(*) from state where id='{}'".format(iden)
        data = tool.select(sql, mode="one")
        if data[0] != 0:  # 判断人员是否存在
            print("------->该公民已存在")
        else:
            sql = "insert into local values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            param = [iden, name, sex, age, passwd, status, country, province, street, door, date,
                     immi_date, credit, culture, learn_num]
            tool.update(sql, param)
            sql = "insert into state values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            tool.update(sql, param)
            print("------->录入公民成功")
            print("您的身份证号为：{}".format(iden))

    # 删除
    def delete(self, iden):
        tool = DBUtils()
        sql = "select count(*) from state where id='{}'".format(iden)
        data = tool.select(sql, mode="one")
        if data[0] == 0:
            print("------->人员身份未备案")
        else:  # 永久删除公民，国家和地方同时删除
            sql = "delete from local where id='{}'".format(iden)
            tool.delete(sql)
            sql = "delete from state where id='{}'".format(iden)
            tool.delete(sql)
            print("------->删除成功")


if __name__ == "__main__":
    t = time.strftime("%Y-%m-%d")
    print(type(t))
    state = State_personnel_management()
    state.inquire("7iyg5qes8t5ckvhe61ow4kgm2vwpjrcy")
    # iden = str()
    # for i in range(32):
    #     iden += random.choice("qwertyuiopasdfghjklzxcvbnm123456789")
    # state.input(iden, "赵瑞", "男", 21, "123456", str(time.strftime("%Y-%m-%d")), "中国", "北京", "中关村", "s001")
    # state.delete("y79it49w1x57di2r1cru48s7r2c2hchb")
