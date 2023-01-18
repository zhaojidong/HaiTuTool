# -*- coding: utf-8 -*-
import openpyxl as op


def op_toExcel(data, fileName):  # openpyxl库储存数据到excel
    wb = op.Workbook()  # 创建工作簿对象
    ws = wb['All_Error']  # 创建子表
    ws.append(['序号', '酒店', '价格'])  # 添加表头
    for i in range(len(data[0])):
        d = data[i]["id"], data[i]["name"], data[i]["price"]
        ws.append(d)  # 每次写入一行
    wb.save(fileName)


# "-------------数据用例-------------"
testData = [
    {"id": 1, "name": "立智", "price": 100},
    {"id": 2, "name": "维纳", "price": 200},
    {"id": 3, "name": "如家", "price": 300},
]
fileName = '测试3.xlsx'
op_toExcel(testData, fileName)