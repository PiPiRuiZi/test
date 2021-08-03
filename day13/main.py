# -*- coding:utf-8 -*-
# @Time    : 2021/08/03 11:20
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : main.py
# @Software: PyCharm
"""
    报告：
        1.加载器：加载所有测试用例并得到所有用例
        2.使用运行器运行这些测试用例并生成报告
    任务2：
        减乘除：进行测试（）
        实现报告的邮件发送
"""
import unittest
import smtplib
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def run():
    tests = unittest.defaultTestLoader.discover(r"G:\文档\python\day13", pattern="test*.py")
    runner = HTMLTestRunner.HTMLTestRunner(
        title="计算机的测试报告",
        description="包括加减乘除所有的测试用例----by赵瑞",
        verbosity=1,
        stream=open(r"计算机测试报告.html", mode="w+", encoding="utf-8")
    )
    runner.run(tests)


def send_email():
    mail_host = "smtp.163.com"
    mail_passwd = "YBGYVSTIDFFRBSSA"
    sender = "18391513986@163.com"  # 发件人
    receivers = ["rui.999@foxmail.com", "rui.888@foxmail.com"]  # 收件人，可群发

    # 封装msg
    title = "计算机测试报告"
    msg = MIMEMultipart()  # 创建附件对象，先不填，后续可以不断附加到里面
    msg["subject"] = title
    msg["from"] = sender

    # 读出文件
    with open("计算机测试报告.html", "r", encoding="utf-8") as file:
        content = file.read()

    part = MIMEText(content, "html", "utf-8")

    msg.attach(part)  # 附加
    try:
        s = smtplib.SMTP_SSL(mail_host, 465)  # 连接服务器，SMTP_SSL服务器地址：465,587支持SSL（TSL），SMTP默认25
        s.login(sender, mail_passwd)  # 登陆邮箱
        s.sendmail(sender, receivers, msg.as_string())  # 发送邮件
        s.quit()  # 退出邮件
        print("发送成功")
    except Exception as e:
        print("发送失败，错误是{}".format(e))


if __name__ == "__main__":
    run()
    send_email()
