# -*- coding:utf-8 -*-
import random
import os  # 按任意键继续
import pymysql


class Bank:
    # 开户行名称
    def __init__(self, bank_name="中国建设银行昌平支行", host="localhost", user="root", passwd="111111", db="bank"):
        self.__bank_name = bank_name
        self.__host = host
        self.__user = user
        self.__passwd = passwd
        self.__db = db
        self.__wellCome = """
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

    # update方法
    def update(self, sql, param):
        conn = pymysql.connect(host=self.__host, user=self.__user, passwd=self.__passwd, db=self.__db)
        cur = conn.cursor()
        cur.execute(sql, param)
        conn.commit()
        cur.close()
        conn.close()

    # select方法
    def select(self, sql, param=None, mode="all", size=1):
        conn = pymysql.connect(host=self.__host, user=self.__user, passwd=self.__passwd, db=self.__db)
        cur = conn.cursor()
        cur.execute(sql, param)
        data = None
        if mode == "all":
            data = cur.fetchall()
        elif mode == "one":
            data = cur.fetchone()
        elif mode == "many":
            data = cur.fetchmany(size)
        conn.commit()
        cur.close()
        conn.close()
        return data

    # 自动生成账户id,不能和已有的重复
    def create_account(self, data, len):
        account = random.randint(10000000, 99999999)
        for i in range(len):
            if account == data[i][0]:
                account = self.create_account(data, len)  # 如果已存在,则递归
        return account

    # 银行添加用户
    def bank_add_user(self, username, password, money, country, province, street, door):
        sql = "select id from user"
        data = self.select(sql)
        length = len(data)
        # 用户库已满
        if length >= 100:
            return False
        account = self.create_account(data, length)
        # 录入
        sql = "insert into user values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        param = [account, username, password, money, country, province, street, door, self.__bank_name]
        self.update(sql, param)
        return account

    # 开户
    def add_user(self):
        username = input("请输入账户用户名：")
        password = input("请输入账户密码：")
        money = input("请输入账户金额：")
        if money.isdigit():
            money = int(money)
            country = input("请输入所属国籍：")
            province = input("请输入所属省份：")
            street = input("请输入所属街道：")
            door = input("请输入门牌号：")
            account: int
            status = self.bank_add_user(username, password, money, country, province, street, door)
            if status is False:
                print("用户库存已达上限！")
            else:
                account = status
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
                    开户行地址：{bank_name_tmp}
                    ------------------------------------
                """
                print(info.format(account=account, username=username, password=password,
                                  money=money, country=country, province=province,
                                  street=street, door=door, bank_name_tmp=self.__bank_name))
        else:
            print("输入不合法！请重新输入")

    # 存钱
    def bank_add_money(self, account, add_money):
        sql = "select id from user"
        data = self.select(sql)
        length = len(data)
        tmp = False
        for i in range(length):
            if account == data[i][0]:
                tmp = True
                break
        if tmp:
            sql = "update user set money = money + %s where id = %s"
            param = [add_money, account]
            self.update(sql, param)
            return True
        else:
            return False

    def add_money(self):
        while True:
            account = input("请输入您的账号：")
            if account.isdigit():
                account = int(account)
                while True:
                    money = input("请输入您的存款金额：")  # 将输入金额转换成int类型
                    if money.isdigit():
                        money = int(money)
                        status = self.bank_add_money(account, money)
                        if status:
                            sql = "select money from user where id = %s"
                            param = [account]
                            data = self.select(sql, param, "one")
                            print("恭喜您存款成功！")
                            print("当前余额为：", data[0])
                            return
                        else:
                            print("未找到该用户，存款失败！请重新输入！")
                            self.add_money()
                            return
                    else:
                        print("输入不合法！请重新输入")
            else:
                print("输入不合法！请重新输入")

    # 取钱
    def bank_take_money(self, account1, password1, money1):
        sql = "select id,password,money from user where id = %s"
        param = [account1]
        data = self.select(sql, param, "one")
        if data != None and account1 == data[0]:
            if password1 == data[1]:
                if money1 > data[2]:
                    return 2  # 余额不够
                else:
                    sql = "update user set money = money - %s where id = %s"
                    param = [money1, account1]
                    self.update(sql, param)
                    return 3  # 成功取钱
            else:
                return 1  # 密码不正确
        else:
            return 0  # 账号不存在

    def take_money(self):
        while True:
            account1 = input("请输入您的账号：\n")
            if account1.isdigit():
                account1 = int(account1)
                password1 = input("请输入密码：\n")
                while True:
                    money1 = input('请输入取款金额：\n')
                    if money1.isdigit():
                        money1 = int(money1)
                        data = self.bank_take_money(account1, password1, money1)
                        if data == 3:
                            print("恭喜您取款成功！")
                            sql = "select money from user where id = %s"
                            param = [account1]
                            data = self.select(sql, param, "one")
                            print("当前余额为：", data[0])
                            return
                        elif data == 2:
                            print("您的余额不足！")
                        elif data == 1:
                            print("您输入的密码不正确！")
                        else:
                            print("您输入的账号有误，请重新输入！")
                    else:
                        print("输入不合法！请重新输入")
            else:
                print("输入不合法！请重新输入")

    # 转账
    def transfer(self):
        while True:
            account = input("请输入您的账户ID：")
            if account.isdigit():
                account = int(account)
                sql = "select id, password, money from user where id = %s"
                param = [account]
                data = self.select(sql, param, "one")
                if account == data[0]:
                    while True:
                        password = input("请输入您的密码：")
                        if password == data[1]:
                            print("登录成功！您当前余额为：", data[2])
                            while True:
                                payee = input("请输入收款人账户ID：")
                                if payee.isdigit():
                                    payee = int(payee)
                                    if payee == account:  # 收款人不能是自己
                                        print("收款人不能是自己！请重新输入")
                                    else:
                                        sql = "select id, password, money from user where id = %s"
                                        param = [payee]
                                        data1 = self.select(sql, param, "one")
                                        if data1 != None and payee == data1[0]:  # 判断收款人是否存在
                                            while True:
                                                s = input("请输入转账金额：")
                                                if s.isdigit():
                                                    s = int(s)
                                                    if s > data[2]:  # 判断余额是否充足
                                                        print("余额不足")
                                                    else:
                                                        sql = "update user set money = money - %s where id = %s"
                                                        param = [s, account]
                                                        self.update(sql, param)
                                                        sql = "select money from user where id = %s"
                                                        param = [account]
                                                        tmp = self.select(sql, param, "one")
                                                        print("转帐成功！您当前余额为：", tmp[0])
                                                        sql = "update user set money = money + %s where id = %s"
                                                        param = [s, payee]
                                                        self.update(sql, param)
                                                        return
                                                else:
                                                    print("输入不合法！请重新输入")
                                        else:
                                            print("您输入的收款人不存在！请重新输入")
                                else:
                                    print("输入不合法！请重新输入")
                        else:
                            print("您输入的密码有误！请重新输入！")
                else:
                    print("您输入的账户不存在，请重新输入！")
                    self.transfer()
            else:
                print("输入不合法！请重新输入")

    # 查询
    def inquiry(self):
        while True:
            account = input("输入您的账户：")
            if account.isdigit():
                account = int(account)
                sql = "select * from user where id = %s"
                param = [account]
                data = self.select(sql, param, "one")
                if data != None and account == data[0]:
                    while True:
                        password = input("输入您的密码：")
                        if password != data[2]:  # 判断密码是否正确
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
                            print(info % (
                                data[0], data[1], data[2], data[4], data[5], data[6], data[7], data[3], data[8]))
                            return
                else:
                    print("您输入的账户不存在，请重新输入！")
            else:
                print("输入不合法！请重新输入")

    def run(self):
        # 入口程序
        while True:
            print(self.__wellCome)
            choose = input("请输入需求业务编号：")
            if choose == '1':
                self.add_user()  # 开户
            elif choose == '2':
                self.add_money()  # 存钱
            elif choose == '3':
                self.take_money()  # 取钱
            elif choose == '4':
                self.transfer()  # 转账
            elif choose == '5':
                self.inquiry()  # 查询
            elif choose == '6':
                break  # 退出
            else:
                print("输入非法！请重新输入")
            os.system('pause')  # 按任意键继续
