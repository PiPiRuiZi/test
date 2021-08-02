# -*- coding:utf-8 -*-
# @Time    : 2021/08/02 14:41
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : 多线程卖面包.py
# @Software: PyCharm
import threading
import time


class Cook(threading.Thread):  # 厨师
    name = ""
    count = 0  # 计数器

    def run(self) -> None:
        global store  # 使用全局变量
        while True:
            if store < 600:
                time.sleep(0.5)
                store += 1  # 库存加一
                self.count += 1  # 计数器加一
                print("{}\033[1;32m生产\033[0m了一个面包，共生产了{}个，当前库存为：{}个".format(self.name, self.count, store))
            else:
                time.sleep(0.5)


class Client(threading.Thread):  # 顾客
    name = ""
    money = 3000

    def run(self) -> None:
        global store
        while True:
            if self.money - 2 >= 0:  # 判断金钱是否够用
                if store > 0:  # 有库存才能购买
                    store -= 1  # 库存减1
                    self.money -= 2  # 金钱减2
                    print("{}\033[1;31m购买\033[0m了一个面包，还剩{}元，当前库存为：{}个".format(self.name, self.money, store))
                else:  # 库存为0，等待1秒
                    time.sleep(1)
            else:
                print("{}没钱了".format(self.name))
                return


# 默认库存量
store = 0

# 三个厨师
cok1 = Cook()
cok2 = Cook()
cok3 = Cook()
cok1.name = "张师傅"
cok2.name = "赵师傅"
cok2.name = "李师傅"

# 五位顾客
cet1 = Client()
cet2 = Client()
cet3 = Client()
cet4 = Client()
cet5 = Client()
cet1.name = "赵先生"
cet2.name = "李先生"
cet3.name = "刘先生"
cet4.name = "王先生"
cet5.name = "孙先生"

# 启动线程
cok1.start()
cok2.start()
cok3.start()
cet1.start()
cet2.start()
cet3.start()
cet4.start()
cet5.start()
