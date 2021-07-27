# -*- coding:utf-8 -*-
import xlrd
import pymysql
from tqdm import *

wb = xlrd.open_workbook("2020sales.xlsx", encoding_override=True)
st_names = wb.sheet_names()  # 获取所有选项卡名称
st_name_len = len(st_names)  # 选项卡数量
sheet = wb.sheet_by_name(st_names[0])  # 每个月字段是相同的，所以只需要拿一月表的获取字段名即可
li = sheet.row_values(0)  # 获取首行字段名称

# 创建表
conn = pymysql.connect(host="localhost", user="root", passwd="111111", db="excel2db_test")
cur = conn.cursor()
for val in tqdm(st_names, desc="创建表中"):
    sql = "create table if not exists {0}(`{1}` varchar(5), `{2}` varchar(10), `{3}` double(11, 2), `{4}` int, " \
          "`{5}` int)".format(val, li[0], li[1], li[2], li[3], li[4])
    cur.execute(sql)
    conn.commit()
# 插入值
for val in tqdm(st_names, desc="导入数据中"):
    sheet = wb.sheet_by_name(val)
    rows = sheet.nrows
    for i in range(1, rows):
        tmp_li = sheet.row_values(i)
        sql = "insert into {0} values('{1}', '{2}', '{3}', '{4}', '{5}')".format(val, tmp_li[0], tmp_li[1], tmp_li[2],
                                                                                 tmp_li[3], tmp_li[4])
        cur.execute(sql)
        conn.commit()
cur.close()
conn.close()
