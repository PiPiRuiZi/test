# -*- coding:utf-8 -*-
import xlwt
from tqdm import *
from DBUtils import *

wb = xlwt.Workbook()  # 创建一个新的工作簿
sql = "show tables"
data = show(sql)  # 获取所有sheet名

for val in tqdm(data, desc="导入到Excel中"):
    sheet_name = val[0]
    sheet = wb.add_sheet(sheet_name)  # 创建sheet
    sql = "desc {0}".format(sheet_name)
    lookup = select(sql)  # 获取sheet的顶部字段
    # 录入列名
    cols = len(lookup)  # 获取列数
    for i in range(0, cols):
        sheet.write(0, i, lookup[i][0])
    # 录入数据
    sql = "select count(*) from {0}".format(sheet_name)
    sheet_day = select(sql, mode="one")  # 获取行数（不算字段列）
    rows = sheet_day[0]  # 获取行数
    sql = "select * from {0}".format(sheet_name)
    tmp_data = select(sql)  # 获取所有数据
    for i in range(1, rows+1):
        for j in range(0, cols):
            sheet.write(i, j, tmp_data[i-1][j])

wb.save("test.xls")
