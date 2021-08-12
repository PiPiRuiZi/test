# -*- coding:utf-8 -*-
# @Time    : 2021/08/12 11:27
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : login_page.py
# @Software: PyCharm
"""
    逻辑
"""
import time


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def login(self, username, passwd):
        self.driver.find_element_by_link_text('教师登录').click()
        self.driver.find_element_by_xpath('//*[@id="loginname"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(passwd)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        # 文件命名不能有冒号
        self.driver.save_screenshot("images\\{}.png".format(time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())))

    def get_success_data(self):
        return self.driver.title

    def get_error_data(self):
        return self.driver.find_element_by_xpath('//*[@id="msg_uname"]').text
