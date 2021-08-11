# -*- coding:utf-8 -*-
# @Time    : 2021/08/10 15:22
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : HKRAuto_test.py
# @Software: PyCharm
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://localhost:8080/HKR")
driver.maximize_window()
# 登陆
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("张三")
driver.find_element_by_xpath("//*[@id='password']").send_keys("123456")
driver.find_element_by_xpath("//*[@id='submit']").click()

# 首页

time.sleep(1)
driver.refresh()
driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[2]/a[2]").click()
driver.find_element_by_xpath("//*[@name='time' and @class='show_tea']").send_keys("9（上晚自习）")
driver.find_element_by_xpath("//*[@name='teaName' and @class='show_tea']").send_keys("贾生")
driver.find_element_by_xpath('//*[@id="form_table"]/tbody/tr[5]/td[3]/div/label[2]/div').click()
driver.find_element_by_xpath('//*[@id="form_table"]/tbody/tr[6]/td[2]/div/label[3]/div').click()
driver.find_element_by_xpath('//*[@id="form_table"]/tbody/tr[7]/td[3]/div/label[3]/div').click()
driver.find_element_by_xpath('//*[@id="form_table"]/tbody/tr[8]/td[2]/div/label[4]/div').click()
driver.find_element_by_xpath('//*[@id="form_table"]/tbody/tr[9]/td[2]/div/label[2]/div').click()
driver.find_element_by_xpath('//*[@id="form_table"]/tbody/tr[10]/td[3]/div/label[3]/div').click()
driver.find_element_by_xpath('//*[@id="form_table"]/tbody/tr[11]/td[2]/div/label[3]/div').click()
driver.find_element_by_xpath('//*[@id="form_table"]/tbody/tr[12]/td[2]/div/label[2]/div').click()
driver.find_element_by_xpath('//*[@id="textarea"]').clear()
driver.find_element_by_xpath('//*[@id="textarea"]').send_keys("继续努力，再接再厉！")
driver.find_element_by_xpath('//*[@id="subtn"]').click()
time.sleep(3)
try:
    driver.find_element_by_xpath('/html/body/div[7]/div[3]/a').click()
except Exception:
    driver.find_element_by_xpath('/html/body/div[8]/div[3]/a/span/span').click()
driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[2]/a").click()

# 修改个人信息
driver.refresh()
driver.find_element_by_xpath('//*[@id="_easyui_tree_7"]/span[1]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="_easyui_tree_7"]/span[1]').click()
driver.find_element_by_xpath('//*[@id="_easyui_tree_8"]/span[4]/a').click()
driver.find_element_by_xpath('//*[@id="info"]/table/tbody/tr[1]/td[2]/input').clear()
driver.find_element_by_xpath('//*[@id="info"]/table/tbody/tr[1]/td[2]/input').send_keys("张三")
driver.find_element_by_xpath('//*[@id="info"]/table/tbody/tr[3]/td[2]/input').clear()
driver.find_element_by_xpath('//*[@id="info"]/table/tbody/tr[3]/td[2]/input').send_keys("123456")
driver.find_element_by_xpath('//*[@id="_easyui_textbox_input1"]').clear()
driver.find_element_by_xpath('//*[@id="_easyui_textbox_input1"]').send_keys("22")
driver.find_element_by_xpath('//*[@id="info"]/table/tbody/tr[5]/td[2]/select').send_keys("女")
driver.find_element_by_xpath('//*[@id="info"]/table/tbody/tr[6]/td[2]/input').clear()
driver.find_element_by_xpath('//*[@id="info"]/table/tbody/tr[6]/td[2]/input').send_keys("北京市海淀区")
driver.find_element_by_xpath('//*[@id="info"]/table/tbody/tr[8]/td[2]/input').clear()
driver.find_element_by_xpath('//*[@id="info"]/table/tbody/tr[8]/td[2]/input').send_keys("123987@qq.com")
driver.find_element_by_xpath('//*[@id="info"]/table/tbody/tr[9]/td[2]/textarea').clear()
driver.find_element_by_xpath('//*[@id="info"]/table/tbody/tr[9]/td[2]/textarea').send_keys("你好，我是人dfddd")
driver.find_element_by_xpath('//*[@id="btn_modify"]').click()

# 查看所有好友
driver.find_element_by_xpath('//*[@id="_easyui_tree_10"]/span[4]/a').click()

# 修改头像
driver.find_element_by_xpath('//*[@id="img"]').click()
driver.find_element_by_xpath('//*[@id="file1"]').send_keys(r"G:\图片\头像\16086046778073790.jpg")
driver.find_element_by_xpath('//*[@id="pic_btn"]').click()

# 退出登录
driver.find_element_by_xpath('//*[@id="pic_btn"]').click()
# 关闭浏览器
time.sleep(3)
driver.quit()


