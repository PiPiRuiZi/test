# -*- coding:utf-8 -*-
import xlrd
import xlwt
import pymysql
from tqdm import *


class DBUtils:
    def __init__(self, host, user, passwd, db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db

    def select(self, sql, param=None, mode="all", size=1):
        conn = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db)
        cur = conn.cursor()
        cur.execute(sql, param)
        data = None
        if mode == "all":
            data = cur.fetchall()
        elif mode == "one":
            data = cur.fetchone()
        elif mode == "many":
            data = cur.fetchmany(size)
        conn.commit()
        cur.close()
        conn.close()
        return data

    def show(self, sql):
        conn = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db)
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return data


class Transform:
    def __init__(self, host, user, passwd, db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db

    # 公用insert sql语句拼接方法
    def concat_insert_sql(self, sql, names):
        for i in range(len(names)):
            if i == len(names) - 1:
                sql = sql + "%s)"
            else:
                sql = sql + "%s, "
        return sql

    # 公用create sql语句拼接方法
    def concat_create_sql(self, sql, names):
        # 数据类型
        tag = 0
        for val in names:
            if val[1] == 0:  # empty 空
                val[1] = "varchar(50)"
            elif val[1] == 1:  # string
                val[1] = "varchar(50)"
            elif val[1] == 2:  # number
                val[1] = "decimal(13, 2)"
            elif val[1] == 3:  # date
                val[1] = "date"
            elif val[1] == 4:  # boolean
                val[1] = "tinyint(1)"
            else:  # Error
                val[1] = "varchar(50)"
            if val[0] == '':
                val[0] = 'NULL' + str(tag)
                tag += 1

        for i in range(len(names)):
            if i == len(names) - 1:
                sql = sql + "`" + names[i][0] + "`" + " " + names[i][1] + ")"
            else:
                sql = sql + "`" + names[i][0] + "`" + " " + names[i][1] + ", "

        return sql

    # excel转数据库，自动创建表，生成表头，数据类型自动生成，前提是手动传入数据库，文件地址和表头所在行
    def excel2db(self, file_path, top_row = 1):
        wb = xlrd.open_workbook(file_path, encoding_override=True)
        st_names = wb.sheet_names()  # 获取所有选项卡名称
        conn = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db)
        cur = conn.cursor()
        # 导入到数据库
        for val in st_names:
            # 录入表头
            sheet = wb.sheet_by_name(val)
            if sheet.nrows < top_row:
                return
            tmp_name = sheet.row_values(top_row-1)  # 获取表头字段名称
            top_li = []
            for i in range(len(tmp_name)):
                top_li.append([tmp_name[i], sheet.cell(top_row, i).ctype])  # 获取字段名和字段类型
            sql = "create table if not exists {}(".format(val)
            sql = self.concat_create_sql(sql, top_li)
            # print(sql)
            try:
                cur.execute(sql)
            except Exception as e:
                print("create执行失败！错误是：", e)
                return
            conn.commit()
            # 录入数据
            rows = sheet.nrows
            for i in tqdm(range(top_row, rows), desc="导入到数据库中"):
                tmp_li = sheet.row_values(i)
                sql = "insert into {} values(".format(val)
                sql = self.concat_insert_sql(sql, tmp_li)
                try:
                    cur.execute(sql, tmp_li)
                except Exception as e:
                    print("insert into执行失败！错误是：", e)
                    if str(e) == """(1136, "Column count doesn't match value count at row 1")""":
                        print("数据库有冲突的表，请先删除表或者对sheet重命名")
                    return
                conn.commit()
        cur.close()
        conn.close()

    # 数据库转excel
    def db2excel(self):
        wb = xlwt.Workbook()  # 创建一个新的工作簿
        sql = "show tables"
        tool = DBUtils(self.host, self.user, self.passwd, self.db)
        data = tool.show(sql)  # 获取所有sheet名
        for val in tqdm(data, desc="导入到Excel中"):
            sheet_name = val[0]
            sheet = wb.add_sheet(sheet_name)  # 创建sheet
            sql = "desc {}".format(sheet_name)
            top_li = tool.select(sql)  # 获取sheet的顶部字段
            # 录入列名
            cols = len(top_li)  # 获取列数
            for i in range(0, cols):
                sheet.write(0, i, top_li[i][0])
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
