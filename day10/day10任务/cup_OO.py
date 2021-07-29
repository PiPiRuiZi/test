# -*- coding:utf-8 -*-
class Cup:
    """高度，容量，颜色，材料"""
    def __init__(self, height, cubage, color, material):
        self.__height = height
        self.__cubage = cubage
        self.__color = color
        self.__material = material

    def get_height(self):
        return self.__height

    def get_cubage(self):
        return self.__cubage

    def get_color(self):
        return self.__color

    def get_material(self):
        return self.__material

    def set_height(self, height):
        self.__height = height

    def set_cubage(self, cubage):
        self.__cubage = cubage

    def set_color(self, color):
        self.__color = color

    def set_material(self, material):
        self.__material = material

    def store(self, cubage=0):
        if cubage <= self.__cubage:
            print("{}厘米高、{}色的{}杯存放了{}毫升的液体".format(self.__height, self.__color, self.__material, cubage))
        else:
            print("杯子装不下")
