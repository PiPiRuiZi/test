# -*- coding:utf-8 -*-
import random

# 银行的库
names = {
    10000001: {
        "username": "test1",
        "password": "123456",
        "money": 10000,
        "country": "中国",
        "province": "北京",
        "street": "沙河镇街道",
        "door": "狼腾测试员",
        "bank_name": "中国建设银行昌平支行"
    },
    10000002: {
        "username": "test2",
        "password": "654321",
        "money": 20000,
        "country": "中国",
        "province": "上海",
        "street": "东方明珠",
        "door": "001",
        "bank_name": "中国建设银行东方支行"
    }
}

bank_name = "中国工商银行昌平回龙观支行"  # 银行名称写死的


def welcome():
    print("*************************************")
    print("*      中国工商银行昌平支行           *")
    print("*************************************")
    print("*  1.开户                            *")
    print("*  2.存钱                            *")
    print("*  3.取钱                            *")
    print("*  4.转账                            *")
    print("*  5.查询                            *")
    print("*  6.Bye！                           *")
    print("**************************************")


def bank_add_money(account,money):

    if account in names:
        names[account]["money"]+=money
        return True
    else:
        return False


def add_money():
    while True:
        account = int(input("请输入您的账号："))
        money = int(input("请输入您的存款余额："))  # 将输入金额转换成int类型
        status = bank_add_money(account,money)
        if status :
            print("恭喜您存款成功！")
            print("当前余额为：", names[account]["money"])
            break
        else:
            print("未找到该用户，存款失败！请重新输入！")


while True:
    # 打印欢迎程序
    welcome()
    chose = input("请输入您的业务：")
    if chose == "1":
        pass
    elif chose == "2":
        add_money()
    elif chose == "3":
        pass
    elif chose == "4":
        pass
    elif chose == "5":
        pass
    elif chose == "6":
        print("欢迎下次光临！")
        break
    else:
        print("输入错误！请重新输入！")