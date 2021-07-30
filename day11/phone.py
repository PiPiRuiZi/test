# -*- coding:utf-8 -*-
class Old_phone:
    def __init__(self, brand):
        self.__brand = brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_brand(self):
        return self.__brand

    def call(self, phonenum):
        print("正在给{}打电话...".format(phonenum))


class New_phone(Old_phone):
    def call(self, phonenum):
        print("语音拨号中...")
        super().call(phonenum)

    def show(self):
        print("品牌为：{}的手机很好用...".format(super().get_brand()))


class Test:
    phone = New_phone("Apple")
    phone.set_brand("华为")
    phone.show()
    phone.call("18899996666")
