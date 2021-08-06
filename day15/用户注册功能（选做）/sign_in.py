# -*- coding:utf-8 -*-
# @Time    : 2021/08/06 16:32
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : sign_in.py
# @Software: PyCharm
"""
    编程实现：有names.txt文件，实现用户的注册，登陆，修改密码，上传头像并记录头像路径的功能。（选做）
"""
li = list()
print("------注册用户------")
li.append(input("请输入姓名："))
li.append(input("请输入密码："))
li.append(input("请输入性别："))
li.append(input("请输入年龄："))
li.append(input("请输入地址："))
li.append(input("请输入头像路径："))

f = open(file="Names.txt", mode="a+", encoding="utf-8")
lenght = len(li)
for i in range(lenght):
    if lenght - i != 1:
        f.write(li[i] + ",")
    else:
        f.write(li[i])
f.write("\n")
