# -*- coding:utf-8 -*-
class Call:
    """姓名，性别，年龄，所拥有的手机剩余话费，手机品牌，手机电池容量，手机屏幕大小，手机最大待机时长，所拥有的积分。"""

    def __init__(self, name, sex, age, money, brand, battery, scrn_size, standby_time, jifen):
        self.__name = name
        self.__sex = sex
        self.__age = age
        self.__money = money
        self.__brand = brand
        self.__battery = battery
        self.__scrn_size = scrn_size
        self.__standby_time = standby_time
        self.__jifen = jifen

    def send_message(self, str):
        print("发送短信中，内容为：{}".format(str))

    def call_up(self, phonenum, time):
        if self.__money < 1:
            print("话费不足，剩余{}，请缴费！".format(self.__money))
        else:
            tmp = 0
            tmp1 = 0
            if time <= 10:
                self.__jifen -= 15 * time
                self.__money -= 1 * time
                tmp = 1 * time
                tmp1 = 15 * time
            elif time <= 20:
                self.__jifen -= 39 * time
                self.__money -= 0.8 * time
                tmp = 0.8 * time
                tmp1 = 15 * time
            else:
                self.__jifen -= 48 * time
                self.__money -= 0.65 * time
                tmp = 0.65 * time
                tmp1 = 48 * time
            print("本次与{}通话{}分钟，消费了{}元、{}积分，剩余话费为：{}，剩余积分为：{}".format(phonenum, time, tmp, tmp1, self.__money, self.__jifen))
