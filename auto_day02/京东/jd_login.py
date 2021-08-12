# -*- coding:utf-8 -*-
# @Time    : 2021/08/11 14:06
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : jd_login.py
# @Software: PyCharm
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from detect_displacement import *
import track
import time
import random

driver = webdriver.Chrome()
driver.get("https://www.jd.com")

driver.maximize_window()
driver.find_element_by_xpath('//*[@id="ttbar-login"]/a[1]').click()
driver.find_element_by_link_text('账户登录').click()
driver.find_element_by_id('loginname').send_keys("zhaorui")
driver.find_element_by_id('nloginpwd').send_keys("123456")
driver.find_element_by_id('loginsubmit').click()

# 获取背景图和滑块图保存到image下
# 全屏图
driver.save_screenshot("image\\full_snap.png")
full_snap = Image.open("image\\full_snap.png")

# 滑块图
img1 = driver.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[1]/div[2]/div[2]/img')
location1 = img1.location
size1 = img1.size
left1 = location1['x']
top1 = location1['y']
right1 = left1 + size1['width']
bottom1 = top1 + size1['height']
image_obj = full_snap.crop((left1, top1, right1, bottom1))
image_obj.save("image\\target_snap.png")

# 背景图
img = driver.find_element_by_class_name('JDJRV-bigimg')
location = img.location
size = img.size
left = location['x']
top = location['y']
right = left + size['width']
bottom = top + size['height']
left += size1['width']
image_obj = full_snap.crop((left, top, right, bottom))
image_obj.save("image\\background_snap.png")

# 调用方法返回移动距离
x = detect_displacement("image/background_snap.png", "image/target_snap.png")
x += size1['width']

# 移动
ac = ActionChains(driver)  # 事件链对象
ele = driver.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[3]')
track_list = track.get_track(x)

ac.click_and_hold(ele)  # 按下鼠标
for i in track_list:
    ac.move_by_offset(i, 0)  # 鼠标移动
    # time.sleep(0.001)

t = x - sum(track_list)
ac.move_by_offset(t+1, 0)  # 补充误差位移

time.sleep(0.5)
ac.release(ele).perform()  # 释放鼠标

time.sleep(10)
driver.quit()
