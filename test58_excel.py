#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名:test58_excel.py
# 解析excel文件

from operator import le
from unittest import result
import xlwt  # 写入excel
import xlrd  # 读取excel
from datetime import date, datetime
import sys
from xlutils.copy import copy
'''
    [读取excel]
    xlrd
    注意：xlrd不支持xlsx格式
'''

file = './file/workbook_read.xls'

class Excel():

    def  __init__(self, file = './file/workbook_read.xls'):
        self.file = file
    
    def read_excel(self):
        print("read_excel:",self.file)
        wb = xlrd.open_workbook(filename=self.file)  # 打开文件
        print(wb.sheet_names())  # 获取工作簿所有表格名字                               输出：['Sheet1']  是一个列表
        sheet1 = wb.sheet_by_index(0)  # 通过索引获取表格（获取第一张表）
        # 定义空列表，用于存放遍历excel表内每一行数据
        result = []
        # 遍历表格的每一行
        for i in range(0, sheet1.nrows): # sheet1.nrows 表示总行数
            print(sheet1.row_values(i)) #  
            result.append(sheet1.row_values(i)) #  将每一行的数据添加到result列表中
        return result
    
        # sheet2 = wb.sheet_by_name('Sheet1')  # 通过名字获取表格,获取第一张表
        # print(sheet1) # 获取表格内容                                     输出：Sheet  0:<Sheet1>
        # print(sheet2)# 获取表格内容                                      输出：Sheet  0:<Sheet1>
        # print(sheet1.name, sheet1.nrows, sheet1.ncols)# 获取表格名称，行数，列数           输出：Sheet1 7 5  即表名为Sheet1，行数为7，列数为5

        # rows = sheet1.row_values(2)  # 获取行内容
        # cols = sheet1.col_values(3)  # 获取列内容
        # print(rows)# 获取第三行内容                                              输出：['wangwu2', '王五2', 'wangwu2@qq.com', 2.0, 0.0] 是一个列表
        # print(cols)# 获取第四列内容                                              输出：['role', 1.0, 2.0, 3.0, 1.0, 2.0, 3.0]  是一个列表，索引0为列名
        #  # 获取表格里的内容，三种方式
        # print(sheet1.cell(1, 0).value) #            输出：wangwu1
        # print(sheet1.cell_value(1, 0)) #            输出：wangwu1
        # print(sheet1.row(1)[0].value) #             输出：wangwu1
    '''
        [写入excel]
        xlwt
        https://pypi.org/project/xlwt/
        @param: sheet1_name:表名 
    '''


    def write_excel(self,sheet1_name):
        # 创建工作簿
        f = xlwt.Workbook() 
        # 创建sheet
        sheet1 = f.add_sheet(sheet1_name, cell_overwrite_ok=True) 
        # 列表表头
        row_header = ["username", "name", "age", "sex"] 
        # 待写入的数据
        data = [["lisi", "李四", "14", "boy"],["wangwu", "王五", "22", "girl"],["zhaoliu", "赵六", "33", "boy"]]
        # 写入表头
        for i in range(0,len(row_header)):
            sheet1.write(0, i,row_header[i], Excel().set_style0())
        # 写入数据（第二行开水）
        for row in range(1,len(data)):
            for clo in range(0,len(row_header)):
                # 参数：行，列，值，样式
                sheet1.write(row, clo,data[row][clo], Excel().set_style1())# 写入第一行，索引为0
        # 保存文件
        f.save(self.file)
        # 其他用法
        # for i in range(0, len(colum0)):
        #     sheet1.write(i+1, 0, colum0[i])# 写入第一列，索引为0
        #     sheet1.write(i+1, 0, colum0[i], Excel.set_style('Times New Roman', 220, True))# 写入第一列，索引为0
        #     sheet1.write(1, 3, '2006/12/12')# 写入第一行，索引为0
        #     sheet1.write_merge(6, 6, 1, 3, '未知')    # 合并行单元格
        #     sheet1.write_merge(1, 2, 3, 3, '打游戏')  # 合并列单元格
        #     sheet1.write_merge(4, 5, 3, 3, '打篮球')  # 合并列单元格
        #     sheet1.write(2, 2, xlwt.Formula("A3+B3"))# 表达式 = A3+B3

    '''
        [追加写入excel]
        @param: write_data: 待写入的数据 类型：字符串
        @param: row_num: 写入第几行 类型：字符串
        
    '''
    def write_excel_sign(self,write_data,row_num):
            rb = xlrd.open_workbook(self.file,formatting_info=True)
            r_sheet = rb.sheet_by_index(0) 
            r = r_sheet.nrows
            wb = copy(rb) 
            sheet = wb.get_sheet(0) 
            sheet.write(row_num,3,write_data)
            wb.save(self.file)
            print('Wrote successfully!')
            
            # # 创建工作簿
            # f = xlwt.Workbook() 
            # # 创建sheet
            # sheet1 = f.add_sheet(sheet1_name, cell_overwrite_ok=True) 
            # # 列表表头
            # row_header = ["legal_name", "ABN", "State", "Postal Code"]
            # # 待写入的数据
            # data = write_data
            # # 写入表头
            # for i in range(0,len(row_header)):
            #     sheet1.write(0, i,row_header[i], Excel().set_style0())
            # # 写入数据（第二行）
            # # 参数：行，列，值，样式
            # sheet1.write(row_num, 3,write_data, Excel().set_style1())# 写入第一行，索引为0
            # # 保存文件
            # f.save(self.file)


    '''
        [设置表格样式]
    '''

    def set_style0(self):
        style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
        num_format_str='#,##0.00')
        return style0
    def set_style1(self):
        style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
        return style1
    # def set_style(self,name, height, bold=False):
    #     style = xlwt.XFStyle()# 初始化样式
    #     font = xlwt.Font()# 
    #     font.name = name # 设置字体
    #     font.bold = bold #  设置是否加粗
    #     # font.color_index = 4 #  设置字体颜色
    #     font.height = height # 设置字体大小
    #     style.font = font # 
    #     return style
    
if __name__ == '__main__':
    pass
    # Excel().read_excel()
    Excel('./file/workbook_write.xls').write_excel("Sheet1")

