# -*- coding:utf-8 -*-
import random  # 随机数
import os  # 按任意键继续

"""
    账户ID为键
"""

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

# 开户行名称
bank_name = "中国建设银行昌平支行"
# 欢迎页面模板
wellCome = """
        ------------------------------------
        |      欢迎来到中国建设银行昌平支行    |
        ------------------------------------
        |             1.开户               |
        |             2.存钱               |
        |             3.取钱               |
        |             4.转账               |
        |             5.查询               |
        |             6.退出               |
        ------------------------------------
"""


# 银行添加用户
def bank_add_user(username, password, money, country, province, street, door, account):
    # 用户库已满
    if len(names) >= 100:
        print(len(names))
        return False
    # 已存在，则重新生成，按照用户ID
    while True:
        if account in names:
            account = random.randint(10000000, 99999999)
        else:
            break

    # 录入
    names[account] = {
        "username": username,
        "password": password,
        "money": money,
        "country": country,
        "province": province,
        "street": street,
        "door": door,
        "bank_name": bank_name
    }
    return 1


# 开户
def add_user():
    username = input("请输入账户用户名：")
    password = input("请输入账户密码：")
    money = int(input("请输入账户金额："))
    country = input("请输入所属国籍：")
    province = input("请输入所属省份：")
    street = input("请输入所属街道：")
    door = input("请输入门牌号：")
    account = random.randint(10000000, 99999999)
    status = bank_add_user(username, password, money, country, province, street, door, account)
    if status:
        print("开户成功！")
        info = """
            ----------个人信息【建设银行】---------
            账户ID：{account}
            用户名：{username}
            密码：{password}
            金额：{money}
            居住地址：
                国籍：{country}
                省份：{province}
                街道：{street}
                门牌号：{door}
            ------------------------------------
        """
        print(info.format(account=account, username=username, password=password,
                          money=money, country=country, province=province,
                          street=street, door=door))
    else:
        print("用户库存已达上限！")


# 存钱 由高晓鑫完成
def bank_add_money(account, money):
    if account in names:
        names[account]["money"] += money
        return True
    else:
        return False


def add_money():
    while True:
        account = int(input("请输入您的账号："))
        money = int(input("请输入您的存款金额："))  # 将输入金额转换成int类型
        status = bank_add_money(account, money)
        if status:
            print("恭喜您存款成功！")
            print("当前余额为：", names[account]["money"])
            break
        else:
            print("未找到该用户，存款失败！请重新输入！")


# 取钱 由叶宪胤完成
def bank_take_money(account1, password1, money1):
    if account1 in names:  # 判断用户存不存在
        if password1 == names[account1]["password"]:  # 判断密码对不对
            if names[account1]["money"] < money1:  # 判断余额够不够
                print("余额不够")
                return False
            else:
                names[account1]["money"] = names[account1]["money"] - money1
                print("取款成功！当前余额为:",names[account1]["money"])
                return True
        else:
            print("输入密码错误，请重新输入！")
            return False
    else:
        print("账号输入错误，请重新输入！")


def take_money():
    while True:
        account1 = int(input("请输入您的账号：\n"))
        password1 = input("请输入密码：\n")
        money1 = int(input('请输入取款金额：\n'))
        data = bank_take_money(account1, password1, money1)
        if data:
            return


# 转账
def transfer():
    account = int(input("请输入您的账户ID："))
    if account in names:  # 判断用户是否存在
        while True:
            password = input("请输入您的密码：")
            if names[account]["password"] != password:  # 判断密码是否正确
                print("您输入的密码有误！请重新输入")
            else:
                print("登录成功！您当前余额为：", names[account]["money"])
                while True:
                    payee = int(input("请输入收款人账户ID："))
                    if payee == account:  # 收款人不能是自己
                        print("收款人不能是自己！请重新输入")
                    else:
                        if payee in names:  # 判断收款人是否存在
                            while True:
                                s = int(input("请输入转账金额："))
                                if s > names[account]["money"]:  # 判断余额是否充足
                                    print("余额不足")
                                else:
                                    names[account]["money"] -= s
                                    names[payee]["money"] += s
                                    print("转帐成功！您当前余额为：", names[account]["money"])
                                    return
                        else:
                            print("您输入的收款人不存在！请重新输入")
    else:
        print("该用户不存在！请重新输入")
        transfer()


# 查询 由张冲完成
def inquiry():
    while True:
        account = int(input("输入您的账户："))
        if account in names:
            while True:
                password = input("输入您的密码：")
                if password != names[account]["password"]:
                    print("您输入的密码错误，请重新输入！")
                else:
                    print("登陆成功，以下是您的个人信息")
                    info = """
    -----------个人信息---------
    用户ID：%s
    用户名：%s
    密码：%s
    地址信息
        国家：%s
        省份：%s
        街道：%s
        门牌号: %s
    余额：%s
    开户行地址：%s
    ---------------------------
                    """
                    print(info % (account,
                                  names[account]["username"],
                                  names[account]["password"],
                                  names[account]["country"],
                                  names[account]["province"],
                                  names[account]["street"],
                                  names[account]["door"],
                                  names[account]["money"],
                                  names[account]["bank_name"]))
                    return
        else:
            print("您输入的账户不存在，请重新输入！")


# 入口程序 由赵瑞完成整合
while True:
    print(wellCome)
    choose = input("请输入需求业务编号：")
    if choose == '1':
        add_user()  # 开户
    elif choose == '2':
        add_money()  # 存钱 由高晓鑫完成
    elif choose == '3':
        take_money()  # 取钱 由叶宪胤完成
    elif choose == '4':
        transfer()  # 转账
    elif choose == '5':
        inquiry()  # 查询 由张冲完成
    elif choose == '6':
        break  # 退出
    else:
        print("输入非法！请重新输入")
    os.system('pause')  # 按任意键继续
