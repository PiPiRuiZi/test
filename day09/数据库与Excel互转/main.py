# -*- coding:utf-8 -*-
from DB_Excel_Utils import Transform

t = Transform("localhost", "root", "111111", "excel2db_test")  # 生成实例
file_path = r"G:\文档\python\day09\数据库与Excel互转\2020sales.xlsx"  # 文件路径
t.excel2db(file_path)  # excel转数据库
t.db2excel()  # 数据库转excel
