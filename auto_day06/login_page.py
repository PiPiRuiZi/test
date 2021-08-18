# -*- coding:utf-8 -*-
# @Time    : 2021/08/17 15:17
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : login_page.py
# @Software: PyCharm
"""
    逻辑功能
"""


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, account, passwd):
        self.driver.find_element_by_id("com.tencent.mobileqq:id/btn_login").click()
        self.driver.find_element_by_xpath('//android.widget.EditText[@content-desc="请输入QQ号码或手机或邮箱"]').send_keys(account)
        self.driver.find_element_by_accessibility_id("密码 安全").send_keys(passwd)
        self.driver.find_element_by_accessibility_id("登录").click()

    def get_success_data(self):
        try:
            return self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                     '/android.widget.FrameLayout/android.widget.RelativeLayout/android'
                                                     '.widget.LinearLayout/android.widget.TextView').text  # 登陆成功
        except Exception as e:
            print("抛出异常：{}".format(e))
            return "找不到元素"

    def get_error_data(self):
        try:
            return self.driver.find_element_by_accessibility_id("帐号或密码错误，请重新输入。").text  # 登陆失败
        except Exception as e:
            print("抛出异常：{}".format(e))
            return "找不到元素"
