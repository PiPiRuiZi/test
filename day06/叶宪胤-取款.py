

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


def bank_getMoney(account1, password1, money1):
    if account1 in names:
        if password1 == names[account1]["password"]:
            names[account1]["money"] = names[account1]["money"] - money1
            print("取款成功！当前余额为:",names[account1]["money"])
            return True
        else:
            print("输入密码错误，请重新输入！")
            return False






        return
    else:
        print("账号输入错误，请重新输入！")


bank_names = "中国建设银行昌平回龙观支行"
def welcome():
    print("*************************************")
    print("*      中国建设银行昌平支行           *")
    print("*************************************")
    print("*  1.开户                            *")
    print("*  2.存钱                            *")
    print("*  3.取钱                            *")
    print("*  4.转账                            *")
    print("*  5.查询                            *")
    print("*  6.Bye！                           *")
    print("**************************************")

def getMoney():
    while True:
        account1 = int(input("请输入您的账号：\n"))
        password1 = input("请输入密码：\n")
        money1 = int(input('请输入取款金额：\n'))
        data = bank_getMoney(account1, password1, money1)
        if data:
            return








while True:
    welcome()
    chose = input("请输入您的业务：")
    if chose == "3":
        getMoney()




        # 余额
        #
        # 账号
        # 密码
        #
        # 逻辑
        # 取款金额
        #
        # 取款成功
