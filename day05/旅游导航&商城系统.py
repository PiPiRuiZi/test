# -*- coding:utf-8 -*-
"""
    任务1：
        将导航系统与商城系统结合一起。
"""
import random


def start_store():
    while True:
        dec = input("请问是否要购物（y/n）？")
        if dec == "y":
            store()  # 商城系统
            return
        elif dec == "n":
            print("继续旅行，祝您旅行愉快！")
            return
        else:
            print("输入非法，请重新输入")


# 商城系统方法体
def store():
    # 存入商品
    shop = [
        ["杯子", 50],
        ["小米 11", 5000],
        ["魅族 18 pro", 4000],
        ["Macbook Air", 8000],
        ["iPhone 12 pro max", 10000],
        ["冰箱", 2700],
        ["洗衣机", 2700],
        ["空调", 4700],
        ["电视", 7000]
    ]
    # 展示商品
    print("-" * 20, "ZhaoRui商城系统", "-" * 20)
    for index, value in enumerate(shop, 1):
        print(index, " ", value)
    print("-" * 56)

    # 初始化资金
    salary = int(input("请输入您的资金："))  # 输入非int时崩溃，有待优化

    # 发放两张优惠券
    discount1 = round(random.uniform(0.7, 0.9), 2)  # 第一张优惠券，随机折扣幅度，0.7~0.9
    appoint1 = random.randint(0, 8)  # 第一张优惠券指定商品
    discount2 = round(random.uniform(0.7, 0.9), 2)  # 第二张优惠券，随机折扣幅度，0.7~0.9
    appoint2: int  # 声明第二张优惠券
    # 两张优惠券不能为同一商品的
    while True:
        appoint2 = random.randint(0, 8)
        if appoint2 != appoint1:  # 判断两张优惠券是否为同一商品的
            break
    sta = False  # 表示用户是否抽取了优惠券，True表示抽取了，False表示没抽取
    state1 = False  # 第一张优惠券状态标志，True表示可用，False表示不可用
    state2 = False  # 第二张优惠券状态标志，True表示可用，False表示不可用

    # 询问是否要优惠券
    while True:
        dec = input("是否要抽取优惠券？（y/n）：")
        if dec == "y":
            print("恭喜您，获得两张优惠券，购买时将自动抵扣")
            print(shop[appoint1][0], "的", int(discount1*100), "折优惠券")
            print(shop[appoint2][0], "的", int(discount2*100), "折优惠券")
            print("-" * 56)
            sta = True
            state1 = True
            state2 = True
            break
        elif dec == "n":
            print("土豪，里面请~")
            break
        else:
            print("输入非法，请重新输入！")

    # 购物车
    my_cart = []

    # 购物
    count = 1
    while count:
        # 每4次循环展示一次商品
        if count % 5 == 0:
            print("-" * 20, end="")
            print("ZhaoRui商城系统", end="")
            print("-" * 20)
            for index, value in enumerate(shop, 1):
                print(index, " ", value)
            print("-" * 56)
            count = 1  # 重置循环次数
        count += 1

        # 选择商品（资金够将放入购物车）
        num = input("请输入您要购买的商品编号：")

        if num.isdigit():  # 判断输入类型
            num = int(num) - 1
            if num >= len(shop) or num < 0:  # 判断商品编号是否存在
                print("对不起！您输入的商品不存在")
            else:
                price = shop[num][1]
                if num == appoint1:  # 判断是否是优惠券指定商品，打折操作
                    if state1:
                        price = shop[num][1] * discount1
                        state1 = False  # 变更使用状态
                elif num == appoint2:
                    if state2:
                        price = shop[num][1] * discount2
                        state2 = False  # 变更状态为不可用

                if price <= salary:  # 判断资金够不够
                    my_cart.append(shop[num])  # 加入购物车
                    salary -= price  # 购买成功，扣钱
                    print("购买成功，已加入购物车，您当前余额为：￥", salary)
                else:
                    print("对不起！余额不足")
        elif num == "q" or num == "Q":
            print("ByeBye!")
            break
        else:
            print("输入非法！请重新输入")

    # 打印发票
    sum = 0
    print("-" * 24, "消费票据", "-" * 23)
    for index, value in enumerate(my_cart, 1):
        print(index, " ", value)
    for index, value in my_cart:
        sum = sum + value

    if sta:
        if not state1:
            print("已使用一张", shop[appoint1][0], "的", int(discount1*100), "折优惠券")
        if not state2:
            print("已使用一张", shop[appoint2][0], "的", int(discount2 * 100), "折优惠券")
    print("消费金额：￥", sum)
    print("剩余余额：￥", salary)
    print("-" * 56)
    print("欢迎下次光临！")


def naviga():
    while True:
        city1 = input("请输入您要去的城市：")
        if city1 in data:
            start_store()  # 商城系统
            print_place(data[city1])
            while True:
                city2 = input("请输入二级城市：")
                if city2 in data[city1]:
                    start_store()  # 商城系统
                    print_place(data[city1][city2])
                    while True:
                        city3 = input("请输入三级地区：")
                        if city3 in data[city1][city2]:
                            start_store()  # 商城系统
                            print_place(data[city1][city2][city3])
                            while True:
                                city4 = input("请输入最终旅游景点：")
                                if city4 in data[city1][city2][city3]:
                                    print("欢迎来到", city4, "祝您旅途愉快！")
                                    start_store()  # 商城系统
                                    return
                                elif city4 == 'q' or city4 == "Q":
                                    print("------------------欢迎下次光临旅行社！------------------")
                                    return
                                else:
                                    print("当前三级城市不存在，请重新输入！")
                        elif city3 == 'q' or city3 == "Q":
                            print("------------------欢迎下次光临旅行社！------------------")
                            return
                        else:
                            print("当前三级城市不存在，请重新输入！")
                elif city2 == 'q' or city2 == "Q":
                    print("------------------欢迎下次光临旅行社！------------------")
                    return
                else:
                    print("当前二级城市不存在，请重新输入！")
        elif city1 == 'q' or city1 == "Q":
            print("------------------欢迎下次光临旅行社！------------------")
            return
        else:
            print("当前城市不存在，请重新输入！")


data = {
    "北京": {
        "昌平": {
            "十三陵": ["十三陵水库", "沙河水库"],
            "高校": ["北京邮电大学", "中央戏剧学院", "北京师范大学", "华北电力大学", "北京航空航天大学"],
            "天通苑": ["海底捞", "呷哺呷哺"]
        },
        "海淀": {
            "公主坟": ["军事博物馆", "中华世纪园"],
            "科普场馆": ["中国科技馆", "北京天文馆"],
            "高校": ["北京大学", "清华大学"],
            "景区": ["北京植物园", "香山公园", "玉渊潭公园"]
        },
        "朝阳": {
            "龙城": ["鸟化石国家地质公园", "朝阳南北塔"],
            "双塔": ["朝阳凌河公园", "朝阳凤凰山"]
        },
        "延庆": {
            "龙庆峡": ["龙庆峡景区"]
        }
    }
}


# 打印城市
def print_place(choice):
    for value in choice:
        print(value)


# 攻略
for val in data:
    print(val)

naviga()
