# -*- coding:utf-8 -*-
# @Time    : 2021/08/06 15:21
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : upload_photo.py
# @Software: PyCharm
"""
    编写程序模拟证件上传的功能，让用户输入证件的路径，并拷贝到一个统一的图片路径下
"""
name = 0  # 避免命名重复被覆盖
while True:
    path = input("请输入证件路径（请使用“\\\”隔开）：")
    if path == "q" or path == "Q":
        print("已退出")
        break
    f = open(file=path, mode="rb")
    pic = f.read()
    f = open(file="d:\\tmp\\证件照片{}.jpg".format(name), mode="wb")  # 这个路径必须存在
    f.write(pic)
    f.flush()
    f.close()
    print("上传成功！")
    name += 1
