# -*- coding:utf-8 -*-
# @Time    : 2021/08/06 15:11
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : copy_picture.py
# @Software: PyCharm
"""
    使用python复制一张图片到D盘的python文件夹里
"""
f = open(file="picture.jpg", mode="rb")
pic = f.read()
f = open(file="d:\\python\\tag.jpg", mode="wb")  # 这个目录要存在
f.write(pic)
f.flush()
f.close()
