# -*- coding:utf-8 -*-
# @Time    : 2021/08/11 16:27
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : detect_displacement.py
# @Software: PyCharm
import cv2

# 作者-上海悠悠 QQ交流群:717225969
# blog地址 https://www.cnblogs.com/yoyoketang/


def _tran_canny(image):
    """消除噪声"""
    image = cv2.GaussianBlur(image, (3, 3), 0)
    return cv2.Canny(image, 50, 150)


def detect_displacement(img_slider_path, image_background_path):
    """detect displacement"""
    # # 参数0是灰度模式
    image = cv2.imread(img_slider_path, 0)
    template = cv2.imread(image_background_path, 0)

    # 寻找最佳匹配
    res = cv2.matchTemplate(_tran_canny(image), _tran_canny(template), cv2.TM_CCOEFF_NORMED)
    # 最小值，最大值，并得到最小值, 最大值的索引
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    top_left = max_loc[0]  # 横坐标
    # 展示圈出来的区域
    x, y = max_loc  # 获取x,y位置坐标

    w, h = image.shape[::-1]  # 宽高
    cv2.rectangle(template, (x, y), (x + w, y + h), (7, 249, 151), 2)
    # show(template)
    return top_left


if __name__ == '__main__':
    top_left = detect_displacement("image/background.png", "image/target.png")
    print(top_left)
