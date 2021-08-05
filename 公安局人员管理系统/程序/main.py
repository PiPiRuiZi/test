# -*- coding:utf-8 -*-
# @Time    : 2021/08/04 17:50
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : main.py
# @Software: PyCharm
from local_personnel_management import *
from state_personnel_management import *
from student import *
import random
import datetime

main_welcome = """
    -------------------------
            选择您的身份
    -------------------------
            1.学生
            2.地区公安局
            3.国家安全总局
            4.退出
    -------------------------
"""
student_welcome = """
    -------------------------
            选择操作
    -------------------------
            1.学习
            2.退出
    -------------------------
"""
student_textbook = """
    ----------------------------
              选择课本
    ----------------------------
            1：小学课本
            2：初中课本
            3：高中课本
            4：大学课本
            5：研究生课本
            6：博士生课本
            7：教授课本
    ----------------------------
"""
local_welcome = """
    -------------------------
            选择操作
    -------------------------
            1.移民
            2.退出
    -------------------------
"""
state_welcome = """
    -------------------------
            选择操作
    -------------------------
            1.查询
            2.录入
            3.删除
            4.退出
    -------------------------
"""


# 学生
def choose_student():
    print("------->登陆系统")
    while True:
        iden = input("输入身份证号：")
        passwd = input("输入密码：")
        tool = DBUtils()
        sql = "select count(*) from local where id='{}'".format(iden)
        data = tool.select(sql, mode="one")
        if data[0] == 0:
            print("该公民不存在")
        else:
            sql = "select passwd from local where id='{}'".format(iden)
            data = tool.select(sql, mode="one")
            if data[0] != passwd:
                print("密码不正确")
            else:
                print("------->登陆成功")
                while True:
                    print(student_welcome)
                    choose = input("请输入业务编号：")
                    if choose == '1':
                        stu = Student(iden)
                        while True:
                            print(student_textbook)
                            num = input("请输入学习的级别：")
                            if num.isdigit():
                                num = int(num)
                                if 1 <= num <= 7:
                                    tmp = stu.learn(num)
                                    if tmp == 1:
                                        print("学习成功")
                                        break
                                    elif tmp == 2:
                                        print("不能跨级学习")
                                    else:
                                        print("该阶段已经学习过了")
                                else:
                                    print("输入不合法")
                            else:
                                print("输入不合法")
                    elif choose == '2':
                        print("------>已退出")
                        return
                    else:
                        print("输入非法！请重新输入")


# 地区公安局
def choose_local():
    print("------->登陆系统")
    while True:
        passwd = input("输入管理员密码：")
        tool = DBUtils()
        sql = "select passwd from local where id='admin'"
        data = tool.select(sql, mode="one")
        if data[0] != passwd:
            print("密码不正确")
        else:
            print("------->登陆成功")
            while True:
                print(local_welcome)
                choose = input("请输入业务编号：")
                if choose == '1':
                    while True:
                        iden = input("请输入要移民的公民身份证号：")
                        local = Local_personnel_management()
                        local.immi(iden)
                        break
                elif choose == '2':
                    print("------>已退出")
                    return
                else:
                    print("输入非法！请重新输入")


# 国家安全总局
def choose_state():
    print("------->登陆系统")
    while True:
        password = input("输入管理员密码：")
        tool = DBUtils()
        sql = "select passwd from state where id='admin'"
        data = tool.select(sql, mode="one")
        if data[0] != password:
            print("密码不正确")
        else:
            print("------->登陆成功")
            while True:
                print(state_welcome)
                choose = input("请输入业务编号：")
                if choose == '1':  # 查询
                    iden = input("请输入要查询的公民身份证号")
                    tool = DBUtils()
                    sql = "select count(*) from state where id='{}'".format(iden)
                    data = tool.select(sql, mode="one")
                    if data[0] == 0:
                        print("------->该公民不存在")
                    else:
                        state = State_personnel_management()
                        state.inquire(iden)
                elif choose == '2':  # 录入
                    state = State_personnel_management()
                    iden = str()
                    for i in range(32):
                        iden += random.choice("qwertyuiopasdfghjklzxcvbnm123456789")
                    name = input("请输入姓名")
                    sex = input("请输入性别")
                    age = input("请输入年龄")
                    passwd = input("请输入密码")
                    date = datetime.datetime.now().strftime("%Y-%m-%d")
                    country = input("请输入国家")
                    province = input("请输入省份")
                    street = input("请输入街道")
                    door = input("请输入门牌号")
                    state.input(iden, name, sex, age, passwd, date, country, province, street, door)
                elif choose == '3':  # 删除
                    state = State_personnel_management()
                    iden = input("请输入要删除的公民身份证号")
                    state.delete(iden)
                elif choose == '4':
                    print("------>已退出")
                    return
                else:
                    print("输入非法！请重新输入")


if __name__ == "__main__":
    while True:
        print(main_welcome)
        choose = input("请输入需求业务编号：")
        if choose == '1':
            choose_student()  # 学生
        elif choose == '2':
            choose_local()  # 地区公安局
        elif choose == '3':
            choose_state()  # 国家安全总局
        elif choose == '4':
            break
        else:
            print("输入非法！请重新输入")
