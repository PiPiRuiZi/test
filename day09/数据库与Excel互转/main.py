# -*- coding:utf-8 -*-
from DB_Excel_Utils import Transform
"""
    待优化
        Excel转数据库
        1.文件中有合并单元格的情况,数据是储存在左上角的单元格,其他位置为empty(空)
        2.未指定生成文件名和路径,默认为test.xls,储存在当前目录,不够灵活
        3.数字类型为decimal(13, 2),布尔类型为tinyint(1),日期类型为date,其他类型全部为varchar(50)
        4.表中有数据之外的提示性文字时建议在转换时手动对改文字进行删除
        数据库转Excel
        1.字段类型全部重置为文本格式,后续对该Excel进行运算操作时可能会出错
        2.只能转换成xls后缀的文件
    已优化
    1.有表头为空会报错
      为空时将表头自动设置为NULL（字段名不能重复,多个空字段NULL1，NULL2...）
    2.当sheet为空会报错,由于sheet对象没有内容获取表头时提示超出列表索引范围
      加入判断语句,当sheet.nrows小于表头所在行时return
    3.创建的表已存在是时报错
      进行异常捕获,弹出友好提示信息
    
"""
# 生成实例
t = Transform("localhost", "root", "111111", "excel2db_test")
# 文件路径
file_path = r"G:\下载\Tim下载\表2 2019-2020学年 软件1803班总评成绩.xlsx"
# excel转数据库
t.excel2db(file_path, 3)  # 文件路径和表头所在行,所在行是可选参数,默认等于1
# 数据库转excel
# t.db2excel()
