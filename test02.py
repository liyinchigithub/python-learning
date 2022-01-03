#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test02.py
# 读写csv

import csv

def readCsv():
    with open("./test.csv") as f:
        r = csv.reader(f) # 创建阅读器对象
        rows=[row for row in r]
        print(rows[0]) # ['姓名', '年龄', '老家']
        print(rows[1]) # ['张三', '33', '泉州']
        print(rows[2]) # ['王五', '22', '漳州']
        print(rows[3]) # ['赵四', '34', '厦门']

readCsv()

def writeCsv():
    with open("./test.csv",'a') as f:
        row=['曹操','23','学生','黑龙江','5000']
        write=csv.writer(f)
        write.writerow(row)
        print("写入完毕！")

readCsv()
writeCsv()