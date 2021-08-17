# -*- coding:utf-8 -*-
# @Time    : 2021/08/16 15:37
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : auto_douyin.py
# @Software: PyCharm
"""
    已知问题：
        抖音会有各种弹窗，比如软件更新提醒，青少年提醒弹窗等等
        一旦弹出，便无法自动化刷视频
"""
import time
from appium import webdriver


class AutoDouyin:
    def __init__(self):
        server = "http://localhost:4723/wd/hub"  # Appium Server, 端口默认为4723
        desired_capabilities = {
            "platformName": "Android",
            "platformVersion": "7.1.2",
            "appPackage": "com.ss.android.ugc.aweme",
            "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",  # 启动活动
            "deviceName": "127.0.0.1:62001",  # 设备
            "noReset": True  # 启动app时不要清除app里的原有的数据
        }
        self.driver = webdriver.Remote(server, desired_capabilities)

    def auto_douyin(self):
        time.sleep(3)
        while True:
            time.sleep(5)
            try:
                self.driver.swipe(496, 1458, 549, 650)  # 适用于大部分大于1080*1920的设备
            except Exception as e:
                print("出错了，异常是：{}".format(e))
                break
        self.driver.quit()


if __name__ == "__main__":
    auto = AutoDouyin()
    auto.auto_douyin()
