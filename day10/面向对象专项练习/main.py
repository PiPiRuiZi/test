# -*- coding:utf-8 -*-
from air_condition_OO import *
from student_OO import *
from call_OO import *
# 空调类
ac = Air_condition()  # 生成实例
ac.set_brand("海尔")  # 设置品牌
ac.set_price("2000")  # 设置价格
brand = ac.get_brand()  # 获取品牌
price = ac.get_price()  # 获取价格
print("{}空调的价格为：{}".format(brand, price))
ac.start()  # 空调开机
ac.timed_shutdown(5)  # 定时关机

# 学生类
self = Student("赵瑞", 21)   # 自己实例
deskmate = Student("张三", 23)  # 同桌实例
self.show_self()  # 自我介绍
deskmate_age = deskmate.get_age()  # 获取同桌年龄
str = self.compare_age(deskmate_age)  # 年龄比较
print(str)

# 打电话类
# (姓名，性别，年龄，所拥有的手机剩余话费，手机品牌，手机电池容量，手机屏幕大小，手机最大待机时长，所拥有的积分)全部是必选参数
phone = Call("赵瑞", "男", 21, 100, "Mi", 5000, 6.5, 24, 220)
phone.send_message("hello")  # 发送信息
phone.call_up("15698563214", 10)  # 打电话并完成扣费
