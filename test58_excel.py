#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名:test58_excel.py
# 读写excel

import xlwt  # 写入excel
import xlrd  # 读取excel
from datetime import date, datetime

'''
    [读取excel]
    xlrd
'''

file = './file/user_monitor.xls'


def read_excel():
    wb = xlrd.open_workbook(filename=file)  # 打开文件
    print(wb.sheet_names())  # 获取所有表格名字                               输出：['Sheet1']  是一个列表

    sheet1 = wb.sheet_by_index(0)  # 通过索引获取表格
    sheet2 = wb.sheet_by_name('Sheet1')  # 通过名字获取表格
    print(sheet1, sheet2)# 获取表格内容                                      输出：Sheet  0:<Sheet1> Sheet  0:<Sheet1>
    print(sheet1.name, sheet1.nrows, sheet1.ncols)# 获取表格名称，行数，列数           输出：Sheet1 7 5  即表名为Sheet1，行数为7，列数为5

    rows = sheet1.row_values(2)  # 获取行内容
    cols = sheet1.col_values(3)  # 获取列内容
    print(rows)# 获取第三行内容                                              输出：['wangwu2', '王五2', 'wangwu2@qq.com', 2.0, 0.0] 是一个列表
    print(cols)# 获取第四列内容                                              输出：['role', 1.0, 2.0, 3.0, 1.0, 2.0, 3.0]  是一个列表，索引0为列名
     # 获取表格里的内容，三种方式
    print(sheet1.cell(1, 0).value) #            输出：wangwu1
    print(sheet1.cell_value(1, 0)) #            输出：wangwu1
    print(sheet1.row(1)[0].value) #             输出：wangwu1



'''
     [写入excel]
     xlwt   
'''


def write_excel():
    f = xlwt.Workbook() # 创建工作簿
    sheet1 = f.add_sheet('学生', cell_overwrite_ok=True) # 创建sheet
    row0 = ["姓名", "年龄", "出生日期", "爱好"]  # 列表表头
    colum0 = ["张三", "李四", "恋习Python", "小明", "小红", "无名"]# 列表内容
    # 写第一行
    for i in range(0, len(row0)):
        sheet1.write(0, i, row0[i], set_style('Times New Roman', 220, True))# 写入第一行，索引为0
        
    # 写第一列
    for i in range(0, len(colum0)):
        sheet1.write(i+1, 0, colum0[i], set_style('Times New Roman', 220, True))# 写入第一列，索引为0
        sheet1.write(1, 3, '2006/12/12')# 写入第一行，索引为0
        sheet1.write_merge(6, 6, 1, 3, '未知')    # 合并行单元格
        sheet1.write_merge(1, 2, 3, 3, '打游戏')  # 合并列单元格
        sheet1.write_merge(4, 5, 3, 3, '打篮球')  # 合并列单元格
    f.save('./file/writer_excel.xls')# 保存文件

'''
     [设置表格样式]
'''

def set_style(name, height, bold=False):
    style = xlwt.XFStyle()# 初始化样式
    font = xlwt.Font()# 
    font.name = name # 设置字体
    font.bold = bold #  设置是否加粗
    font.color_index = 4 #  设置字体颜色
    font.height = height # 设置字体大小
    style.font = font # 
    
    return style


if __name__ == '__main__':
    read_excel()
