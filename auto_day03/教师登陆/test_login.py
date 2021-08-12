# -*- coding:utf-8 -*-
# @Time    : 2021/08/12 11:13
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : test_login.py
# @Software: PyCharm
from selenium import webdriver  # 浏览器
from unittest import TestCase  # 测试
import time
from ddt import ddt
from ddt import data
from init_page import Initpage  # 数据
from login_page import LoginPage  # 逻辑

@ddt
class TestLogin(TestCase):
    # 用例执行前执行
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:8080/HKR/')
        time.sleep(2)

    # 用例执行后执行
    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()

    @data(*Initpage.login_success_data)
    def test_success_login(self, testdata):
        # 获取数据
        username = testdata["username"]
        passwd = testdata["passwd"]
        expect = testdata["expect"]
        # 执行逻辑
        login = LoginPage(self.driver)
        login.login(username, passwd)
        # 断言
        result = login.get_success_data()
        self.assertEqual(result, expect)

    @data(*Initpage.login_error_data)
    def test_error_login(self, testdata):
        # 获取数据
        username = testdata["username"]
        passwd = testdata["passwd"]
        expect = testdata["expect"]
        # 执行逻辑
        login = LoginPage(self.driver)
        login.login(username, passwd)
        # 断言
        result = login.get_error_data()
        self.assertEqual(result, expect)

