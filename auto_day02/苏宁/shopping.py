# -*- coding:utf-8 -*-
# @Time    : 2021/08/12 09:33
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : shopping.py
# @Software: PyCharm
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.suning.com/")
driver.maximize_window()
driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/ul/li[1]/a[1]').click()  # 选择手机分区
wids = driver.window_handles
driver.switch_to.window(wids[-1])
ac = ActionChains(driver)
for i in range(5):
    ac.key_up(Keys.DOWN).key_down(Keys.DOWN).perform()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[9]/div[1]/a/img').click()  # 选择小米手机分区
wids = driver.window_handles
driver.switch_to.window(wids[-1])
time.sleep(1)
for i in range(6):
    ac.key_up(Keys.DOWN).key_down(Keys.DOWN).perform()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[11]/div[3]/div/div[1]/div/div/div/div/map/area[7]').click()  # 选择手机型号
time.sleep(1)
wids = driver.window_handles
driver.switch_to.window(wids[-1])
driver.find_element_by_xpath('//*[@id="colorItemList"]/dd/ul/li[1]/a').click()  # 选择内存
time.sleep(1)
driver.find_element_by_xpath('//*[@id="versionItemList"]/dd/ul/li[5]/a').click()  # 选择颜色
time.sleep(3)
ac.key_up(Keys.DOWN).key_down(Keys.DOWN).perform()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="addCart"]').click()  # 加入购物车
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[38]/div/a').click()  # 关闭
time.sleep(3)
driver.quit()