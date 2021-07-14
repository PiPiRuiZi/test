# -*- coding:utf-8 -*-

import xlrd

# 打开工作簿
workbook = xlrd.open_workbook(filename="12月份衣服销售数据.xlsx", encoding_override=True)

# 选择选项卡
sheet = workbook.sheet_by_name("12月份各种服饰销售情况")

sum = 0  # 声明销售总额
rows = sheet.nrows  # 获取行数

for i in range(1, rows):  # 跳过首行遍历
    sum += float(sheet.cell_value(i, 2)) * int(sheet.cell_value(i, 4))  # 单价*数量，累加

# 12月份销售总额
print("12月份销售总额为：", round(sum, 2))  # 保留两位小数
print("-"*70)  # 分隔符

# 储存服装名称与销售量、销售额的对应关系
data = {
    "羽绒服": [0, 0],
    "牛仔裤": [0, 0],
    "风衣": [0, 0],
    "皮草": [0, 0],
    "T血": [0, 0],
    "衬衫": [0, 0],
}

sale_sum = 0  # 声明销售总量
sales = 0  # 声明销售总额

for i in range(1, rows):  # 跳过首行遍历
    sale_sum += int(sheet.cell_value(i, 4))  # 计算销售总量
    sales += float(sheet.cell_value(i, 2)) * int(sheet.cell_value(i, 4))  # 计算销售总额
    tmp = sheet.cell_value(i, 1)  # 获取服装名称
    data[tmp][0] += int(sheet.cell_value(i, 4))  # 服装销售量累加
    data[tmp][1] += float(sheet.cell_value(i, 2)) * int(sheet.cell_value(i, 4))  # 服装销售额累加

for k in data:
    ratio = data[k][0] / sale_sum  # 得出销售量占比
    print(k, "的销售量占比为：", round(ratio*100, 2), "%")  # 保留两位小数

print("-"*70)  # 分隔符

for k in data:
    ratio = data[k][1] / sales  # 得出销售额占比
    print(k, "的销售额占比为：", round(ratio*100, 2), "%")  # 保留两位小数
