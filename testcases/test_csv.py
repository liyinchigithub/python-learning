#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test02.py
# 读写csv

import csv
'''
读取csv文件
'''

def readCsv():
    with open("./test.csv") as f:
        r = csv.reader(f) # 创建阅读器对象
        rows=[row for row in r]
        print(rows[0]) # ['姓名', '年龄', '老家']
        print(rows[1]) # ['张三', '33', '泉州']
        print(rows[2]) # ['王五', '22', '漳州']
        print(rows[3]) # ['赵四', '34', '厦门']

readCsv()

'''
写入csv文件，追加到最后一行
'''
def writeCsv():
    with open("./test.csv",'a') as f:
        row=['曹操','23','学生','黑龙江','5000']
        write=csv.writer(f)
        write.writerow(row)
        print("写入完毕！")

writeCsv()