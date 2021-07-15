# -*- coding:utf-8 -*-
import random

num = random.randint(1, 200)  # 包括1和50
count = 0   # 计数器
print("猜数字游戏，数字范围1到200")

gold = 2000  # 金币

while True:
    if gold == 0:  # 金币不足退出游戏
        print("金币不足，强制退出游戏")
        break

    gold -= 200  # 运行一次游戏减200金币
    count += 1  # 计数器累加
    tmp = int(input("输入猜测的数据："))

    if tmp > num:
        print("大了，剩余金币", gold)
    elif tmp < num:
        print("小了，剩余金币", gold)
    else:
        print("恭喜，猜对了，获得金币5000，猜了", count, "次，正确答案为：", num)
        gold += 5000
        print("剩余金币：", gold)
        st = input("是否继续游戏（y/n）：")
        if st == "n":
            print("ByeBye!")
            break
        num = random.randint(1, 200)  # 重新获取随机数
