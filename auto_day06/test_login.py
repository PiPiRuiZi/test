# -*- coding:utf-8 -*-
# @Time    : 2021/08/17 15:17
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : test_login.py
# @Software: PyCharm
from appium import webdriver  # app
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
        server = "http://localhost:4723/wd/hub"  # Appium Server, 端口默认为4723
        desired_capabilities = {
            "platformName": "Android",
            "platformVersion": "7.1.2",
            "appPackage": "com.tencent.mobileqq",
            "appActivity": "com.tencent.mobileqq.activity.LoginActivity",
            "deviceName": "127.0.0.1:62001"
        }
        self.driver = webdriver.Remote(server, desired_capabilities)
        time.sleep(10)

    # 用例执行后执行
    def tearDown(self) -> None:
        time.sleep(10)
        self.driver.quit()

    @data(*Initpage.login_success_data)
    def test_success_login(self, testdata):
        # 获取数据
        username = testdata["account"]
        passwd = testdata["passwd"]
        expect = testdata["expect"]
        # 执行逻辑
        login = LoginPage(self.driver)
        login.login(username, passwd)
        time.sleep(10)
        # 断言
        result = login.get_success_data()
        self.assertEqual(result, expect)

    @data(*Initpage.login_error_data)
    def test_error_login(self, testdata):
        # 获取数据
        username = testdata["account"]
        passwd = testdata["passwd"]
        expect = testdata["expect"]
        # 执行逻辑
        login = LoginPage(self.driver)
        login.login(username, passwd)
        time.sleep(10)
        # 断言
        result = login.get_error_data()
        self.assertEqual(result, expect)
