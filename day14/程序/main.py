# -*- coding:utf-8 -*-
# @Time    : 2021/08/05 15:23
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : main.py
# @Software: PyCharm
import unittest
import smtplib
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def run_htmlTest():
    tests = unittest.defaultTestLoader.discover(r"G:\文档\python\day14", pattern="test*.py")
    runner = HTMLTestRunner.HTMLTestRunner(
        title="银行的测试报告",
        description="测试",
        verbosity=1,
        stream=open(r"银行的测试报告.html", mode="w+", encoding="utf-8")
    )
    runner.run(tests)


def send_email():
    mail_host = "smtp.163.com"
    mail_passwd = "PKTPHZVBGTTBTYXU"
    sender = "18391513986@163.com"  # 发件人
    receivers = ["2431320433@qq.com", "rui.999@foxmail.com", "rui.888@foxmail.com"]  # 收件人，可群发

    # 封装msg
    title = "计算机测试报告by赵瑞"
    msg = MIMEMultipart()  # 创建附件对象，先不填，后续可以不断附加到里面
    msg["subject"] = title
    msg["from"] = sender

    # 读出文件
    with open("银行的测试报告.html", encoding="utf-8") as file:
        content = file.read()

    # part = MIMEText(content, "html", "utf-8")# 以文本形式发送
    # 以附件形式发送
    part = MIMEText(content, "base64", 'utf-8')
    part["Content-Type"] = 'application/octet-stream'
    part.add_header('Content-Disposition', 'attachment', filename='银行测试报告.html')

    part1 = MIMEText("by赵瑞", "plain", "utf-8")  # 正文

    msg.attach(part)  # 附加
    msg.attach(part1)  # 附加
    # 发送邮件
    try:
        s = smtplib.SMTP_SSL(mail_host, 465)  # 连接服务器，SMTP_SSL服务器地址：465,587支持SSL（TSL），SMTP默认25
        s.login(sender, mail_passwd)  # 登陆邮箱
        s.sendmail(sender, receivers, msg.as_string())  # 发送邮件
        s.quit()  # 退出邮件
        print("发送成功")
    except Exception as e:
        print("发送失败，错误是{}".format(e))


if __name__ == "__main__":
    run_htmlTest()
    send_email()
