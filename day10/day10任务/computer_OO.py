# -*- coding:utf-8 -*-
class Computer:
    """屏幕大小，价格，cpu型号，内存大小，待机时长"""

    def __init__(self, scrn_size, money, cpu, rom_size, standby_time):
        self.__scrn_size = scrn_size
        self.__money = money
        self.__cpu = cpu
        self.__rom_size = rom_size
        self.__standby_time = standby_time

    """打字，打游戏，看视频"""

    def type_writ(self):
        print("打字中...")

    def game(self):
        print("打游戏中...")

    def video(self):
        print("看视频中...")

    def show_param(self):
        print("屏幕大小：{}寸，价格{}元，cpu型号'{}'，内存大小{}G，待机时长{}分钟".format(self.__scrn_size, self.__money, self.__cpu,
                                                          self.__rom_size, self.__standby_time))
