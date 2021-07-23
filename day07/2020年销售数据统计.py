# -*- coding:utf-8 -*-
"""
    每月的销售总金额
    全年的销售总金额
    每种衣服的销售总金额
    每个季度销售总金额占比
    全年每种销售总数量占比
"""
import xlrd  # xlrd 1.2.0版本


# 每月的销售金额
def sheet_sum(workbook):
    s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 声明每月总销售量
    st_names = workbook.sheet_names()  # 获取所有选项卡名称
    st_len = len(st_names)  # 获取sheet数量
    for k in range(st_len):  # 通过角标遍历所有选项卡
        st = workbook.sheet_by_index(k)  # 获取当前选项卡
        rows = st.nrows  # 获取行数
        for j in range(1, rows):  # 遍历当前选项卡
            price = float(st.cell_value(j, 2))  # 获取单价
            num = int(st.cell_value(j, 4))  # 获取数量
            s[k] += price * num  # 累加销售额
    return s


# 每种衣服的销售总额
def alone_sum(workbook):
    all_st = workbook.sheet_names()  # 获取所有选项卡名称
    dt = {}  # 声明服装名称与销售额的对应关系，字典数据关系：dt = {"服装名称": [销售金额, 销售数量]}
    for k in all_st:  # 遍历所有选项卡
        st = workbook.sheet_by_name(k)  # 获取当前选项卡
        rows = st.nrows  # 获取行数
        for j in range(1, rows):  # 遍历当前选项卡
            name = st.cell_value(j, 1)  # 获取服装名称
            price = float(st.cell_value(j, 2))  # 获取单价
            num = int(st.cell_value(j, 4))  # 获取数量
            if name in dt:  # 判断该服装名称在li字典中是否已经存在
                dt[name][0] += price * num  # 已经存在则累加销售金额
                dt[name][1] += num  # 累加销售数量
            else:
                dt[name] = [price * num, num]
    return dt


wb = xlrd.open_workbook(filename="2020年每个月的销售情况.xlsx", encoding_override=True)  # 打开工作簿

# 1.每月的销售总金额
li = sheet_sum(wb)  # 调用sheet_sum()方法
li_len = len(li)  # 获取列表长度
for key, value in enumerate(li, 1):
    print(key, "月的销售总额为：￥%.2f" % value)
print("-" * 40)

# 2.全年的销售总金额
sale_sum = 0
for i in li:
    sale_sum += i
print("全年的销售总金额为：￥%.2f" % sale_sum)
print("-" * 40)

# 3.每种衣服的销售总金额
last_dt = alone_sum(wb)  # 调用alone_sum()方法
dt_len = len(last_dt)
for key in last_dt:
    print(key, "的销售总金额为：￥%.2f" % last_dt[key][0])  # 全年销售金额
print("-" * 40)

# 4.每个季度销售总金额占比
qua_sum = [0, 0, 0, 0]  # 声明季度总和
for i in range(li_len):
    t = i // 3
    qua_sum[t] += li[i]

for key, value in enumerate(qua_sum, 1):
    print("第", key, "季度的销售金额占比为：￥%.2f" % (value/sale_sum*100), "%")
print("-" * 40)

# 5.全年每种销售总数量占比
sale_num = 0  # 声明销售总数量
for key in last_dt:
    sale_num += last_dt[key][1]  # 累加销售数量

for key in last_dt:
    ratio = last_dt[key][1] / sale_num  # 销售数量占比，销售数量/总数量
    print(key, "占总销售数量的：%.2f" % (ratio * 100), "%")  # 以百分比格式输出,保留两位小数
