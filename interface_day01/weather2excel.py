# -*- coding:utf-8 -*-
# @Time    : 2021/08/18 15:17
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : weather2excel.py
# @Software: PyCharm
import time
import xlwt
import pandas as pd  # 读取剪贴板
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def weather(dis):
    driver = webdriver.Chrome()
    driver.get("http://flash.weather.com.cn/wmaps/xml/{}.xml".format(dis))
    driver.maximize_window()
    time.sleep(2)
    # 预防省略号
    pd.set_option('display.max_columns', 1000)
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_colwidth', 1000)
    ac = ActionChains(driver)
    ac.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()  # ctrl+a
    ac.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()  # ctrl+c
    driver.quit()
    df = pd.read_clipboard(sep=',')  # 读取剪切板中的数据，分隔符这里是“ , ”，加个参数sep=','即可
    df = str(df)
    list_data = df.split("\n")  # 按转行分割为list
    return list_data


if __name__ == "__main__":
    province = {}  # 省份
    data = weather("china")  # 剪贴板数据
    for i in range(2, len(data) - 1):
        t = data[i].split("\"")
        t1 = t[1]
        province[t1] = t[3]

    wb = xlwt.Workbook(encoding='utf-8')  # 创建工作簿
    sheet = wb.add_sheet("中国")  # 创建sheet
    sheet.write(0, 0, "响应")
    rows = len(data)
    for i in range(1, rows):
        if i > 1:
            t = data[i-1].split(" ", 1)[1]
            sheet.write(i, 0, t)
        else:
            sheet.write(i, 0, data[i - 1])
    for pro in province:
        sheet = wb.add_sheet(pro)  # 创建sheet
        sheet.write(0, 0, "响应")
        data = weather(province[pro])  # 剪贴板数据
        rows = len(data)
        for i in range(1, rows):
            if i > 1:
                t = data[i-1].split(" ", 1)[1]
                sheet.write(i, 0, t)
            else:
                sheet.write(i, 0, data[i-1])
            wb.save("weather.xls")
