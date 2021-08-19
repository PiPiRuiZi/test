# -*- coding:utf-8 -*-
# @Time    : 2021/08/19 10:19
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : weather2excel.py
# @Software: PyCharm
import requests
import xlwt
import json


# 获取请求和响应，返回列表
def weather(dis):
    url = "http://flash.weather.com.cn/wmaps/xml/{}.xml".format(dis)
    r = requests.get(url)
    request_header = dict(r.request.headers)  # 请求头
    response_header = dict(r.headers)  # 响应头
    data = r.content.decode("utf8")  # 网页源码
    return [request_header, response_header, data.split("\n")]  # 返回列表


# 清洗数据获取所有省份，返回字典
def get_province(data):
    province = {}  # 省份
    for i in range(1, len(data) - 1):
        t = data[i].split("\"")
        t1 = t[1]
        province[t1] = t[3]
    return province  # 返回字典


# 写入excel
def to_excel(wb, sheet_name, request, response, data):
    sheet = wb.add_sheet(sheet_name)  # 创建sheet
    # 请求头
    sheet.write(0, 0, "请求")
    i = 1
    for k in request:
        sheet.write(i, 0, k + ":" + request[k])
        i += 1
    # 响应头
    sheet.write(0, 1, "响应")
    i = 1
    for k in response:
        sheet.write(i, 1, k + ":" + response[k])
        i += 1
    # 响应体
    for val in data:
        sheet.write(i, 1, val)
        i += 1


if __name__ == "__main__":
    data = weather("china")
    province = get_province(data[2])
    province["中国"] = "china"
    wb = xlwt.Workbook(encoding='utf-8')  # 创建工作簿
    for key in province:
        data = weather(province[key])
        to_excel(wb, key, request=data[0], response=data[1], data=data[2])
        wb.save("request&response.xls")
