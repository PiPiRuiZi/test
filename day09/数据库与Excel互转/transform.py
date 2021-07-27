# -*- coding:utf-8 -*-
import xlrd
import xlwt
import pymysql
from tqdm import *
from DBUtils import *


class Transform:
    def __init__(self, host, user, passwd, db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db

    def excel2db(self, file_path):
        wb = xlrd.open_workbook(file_path, encoding_override=True)
        st_names = wb.sheet_names()  # 获取所有选项卡名称
        conn = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db)
        cur = conn.cursor()
        # 导入到数据库
        for val in tqdm(st_names, desc="导入到数据库中"):
            # 录入表头
            sheet = wb.sheet_by_name(val)
            li = sheet.row_values(0)  # 获取首行字段名称
            sql = "create table if not exists {0}(`{1}` varchar(5), `{2}` varchar(10), `{3}` double(11, 2), " \
                  "`{4}` int, `{5}` int)".format(val, li[0], li[1], li[2], li[3], li[4])
            cur.execute(sql)
            conn.commit()
            # 录入数据
            rows = sheet.nrows
            for i in range(1, rows):
                tmp_li = sheet.row_values(i)
                sql = "insert into {0} values('{1}', '{2}', '{3}', '{4}', '{5}')".format(val, tmp_li[0], tmp_li[1],
                                                                                         tmp_li[2], tmp_li[3],
                                                                                         tmp_li[4])
                cur.execute(sql)
                conn.commit()
        cur.close()
        conn.close()

    def db2excel(self):
        wb = xlwt.Workbook()  # 创建一个新的工作簿
        sql = "show tables"
        tool = DBUtils(self.host, self.user, self.passwd, self.db)
        data = tool.show(sql)  # 获取所有sheet名

        for val in tqdm(data, desc="导入到Excel中"):
            sheet_name = val[0]
            sheet = wb.add_sheet(sheet_name)  # 创建sheet
            sql = "desc {0}".format(sheet_name)
            lookup = tool.select(sql)  # 获取sheet的顶部字段
            # 录入列名
            cols = len(lookup)  # 获取列数
            for i in range(0, cols):
                sheet.write(0, i, lookup[i][0])
            # 录入数据
            sql = "select count(*) from {0}".format(sheet_name)
            sheet_day = tool.select(sql, mode="one")  # 获取行数（不算字段列）
            rows = sheet_day[0]  # 获取行数
            sql = "select * from {0}".format(sheet_name)
            tmp_data = tool.select(sql)  # 获取所有数据
            for i in range(1, rows + 1):
                for j in range(0, cols):
                    sheet.write(i, j, tmp_data[i - 1][j])

        wb.save("test.xls")
