# -*- coding:utf-8 -*-
# @Time    : 2021/08/10 14:13
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : 跳转页面.py
# @Software: PyCharm
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(r"D:\软件\软件生产过程与数据库\python\python自动化\day01\练习的html\练习的html\跳转页面\pop.html")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='goo']").click()
data = driver.window_handles  # 获取所有窗口
driver.switch_to.window(data[-1])  # 切换到新窗口，第一个用下标[0]表示，最后一个用下标-1表示，倒数第二个用下标-2表示，以此类推

driver.find_element_by_name("wd").send_keys("Java")
driver.find_element_by_id("su").click()
time.sleep(3)
driver.quit()
