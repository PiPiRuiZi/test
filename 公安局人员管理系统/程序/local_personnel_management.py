# -*- coding:utf-8 -*-
# @Time    : 2021/08/04 16:31
# @Author  : ZhaoRui
# @Email   : rui.999@foxmail.com
# @File    : local_personnel_management.py
# @Software: PyCharm
from DBUtils import DBUtils
from student import Student
import datetime


# 地方人员管理
class Local_personnel_management:

    def immi(self, iden):  # 移民，传入用户iden
        tool = DBUtils()
        sql = "select count(*) from local where id='{}'".format(iden)
        data = tool.select(sql, mode="one")
        if data[0] == 0:
            print("您是未成年人还不能移民")
        else:
            stu = Student(iden)  # 获取学生对象
            if stu.credit >= 3:
                print("有犯罪历史，无法移民")
            elif stu.culture < 4:
                if stu.immi_date is not None:
                    stu = Student(iden)
                    now = datetime.datetime.now().strftime("%Y-%m-%d")  # 获取当前时间，为str类型
                    now = datetime.datetime.strptime(now, "%Y-%m-%d")  # str转换为datetime.datetime
                    immi_date = str(stu.immi_date)  # datetime.date转换为str
                    form = datetime.datetime.strptime(immi_date, "%Y-%m-%d")  # str转换为datetime.datetime
                    t = (now - form).days  # 同为datetime.datetime进行运算
                    if t >= 365:
                        sql = "delete from local where id='{}'".format(iden)
                        tool.delete(sql)
                        sql = "delete from state where id='{}'".format(iden)
                        tool.delete(sql)
                        print("移民成功")
                    else:
                        print("申请时间截止现在未满一年，无法移民")
                else:
                    tool = DBUtils()
                    now = datetime.datetime.now().strftime("%Y-%m-%d")
                    sql = "update local set immi=%s where id=%s"
                    param = [now, iden]
                    tool.update(sql, param)
                    sql = "update state set immi=%s where id=%s"
                    tool.update(sql, param)
                    print("需要再等待1年审核时间")
            else:  # 永久删除公民
                sql = "delete from local where id='{}'".format(iden)
                tool.delete(sql)
                sql = "delete from state where id='{}'".format(iden)
                tool.delete(sql)
                print("移民成功")


if __name__ == "__main__":
    t = Local_personnel_management()
    t.immi("7iyg5qes8t5ckvhe61ow4kgm2vwpjrcy")
    # stu = Student("tgmi9t43ygt4nvq7zmqlkiosee39caws")
    # now = datetime.datetime.now().strftime("%Y-%m-%d")  # 获取当前时间，为str类型
    # now = datetime.datetime.strptime(now, "%Y-%m-%d")  # str转换为datetime.datetime
    # immi_date = str(stu.immi_date)  # datetime.date转换为str
    # form = datetime.datetime.strptime(immi_date, "%Y-%m-%d")  # str转换为datetime.datetime
    # t = (now - form).days  # 同为datetime.datetime进行运算
