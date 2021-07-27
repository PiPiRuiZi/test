# -*- coding:utf-8 -*-
import pymysql

host = "localhost"
user = "root"
passwd = "111111"
db = "excel2db_test"


def select(sql, param=None, mode="all", size=1):
    conn = pymysql.connect(host=host, user=user, passwd=passwd, db=db)
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


def show(sql):
    conn = pymysql.connect(host=host, user=user, passwd=passwd, db=db)
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return data
