# -*- coding:utf-8 -*-
# @Time    : 2021/08/10 14:19
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : 表单提交.py
# @Software: PyCharm
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(r"D:\软件\软件生产过程与数据库\python\python自动化\day01\练习的html\练习的html\上传文件和下拉列表\autotest.html")
driver.maximize_window()
driver.find_element_by_xpath("//*[@name='account' and @id='accountID']").send_keys("赵瑞")
driver.find_element_by_xpath("//*[@name='password' and @id='passwordID']").send_keys("123456")
driver.find_element_by_xpath("//*[@id='areaID']").send_keys("陕西省")  # 必须是下拉列表中存在的
driver.find_element_by_xpath("//*[@id='sexID2']").click()
driver.find_element_by_xpath("//*[@name='u3' and @type='checkbox' and @value='spring']").click()
driver.find_element_by_xpath("//*[@name='u3' and @type='checkbox' and @value='summer']").click()
driver.find_element_by_xpath("//*[@name='u3' and @type='checkbox' and @value='Auterm']").click()
driver.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys(r"G:\图片\头像\微信图片_20201224153428.jpg")
driver.find_element_by_xpath("//*[@class='u16' and @id='buttonID']").click()
driver.switch_to.alert.accept()  # 点击弹出对话框的确定按钮，点击之后回到原来的页面
time.sleep(3)
driver.quit()



