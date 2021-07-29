# -*- coding:utf-8 -*-
from cup_OO import *
from computer_OO import *
from bank_OO import *

# 杯子
cub = Cup(20, 600, "透明", "玻璃")  # 杯子实例，（高度，容积，颜色，材质）必选参数
cub.store(600)  # 存放液体，输入存放液体的体积，可选参数默认为0

# 笔记本电脑
computer = Computer(15.5, 7000, "i5-8600H", 16, 90)  # 笔记本电脑实例，（屏幕大小，价格，cpu型号，内存大小，待机时长）必选参数
computer.show_param()  # 显示参数
computer.game()  # 打游戏
computer.video()  # 看视频
computer.type_writ()  # 打字

# 银行系统
bank = Bank()
bank.run()
