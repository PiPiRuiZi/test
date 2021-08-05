# -*- coding:utf-8 -*-
# @Time    : 2021/08/04 14:51
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : DBUtils.py
# @Software: PyCharm
import pymysql


class DBUtils:
    def __init__(self, host="localhost", user="root", passwd="111111", db="公安局人员管理系统"):
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

    def delete(self, sql, param=None):
        conn = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db)
        cur = conn.cursor()
        cur.execute(sql, param)
        conn.commit()
        cur.close()
        conn.close()

    def update(self, sql, param=None):
        conn = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db)
        cur = conn.cursor()
        cur.execute(sql, param)
        conn.commit()
        cur.close()
        conn.close()
