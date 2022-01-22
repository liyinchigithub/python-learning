#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test-mysql.py
# 操作数据库Mysql
# https://www.runoob.com/python3/python-mysql-connector.html
# https://www.runoob.com/python3/python3-mysql.html


# python-mysql-connector

'''
    安装依赖
    python -m pip install mysql-connector
'''

import mysql.connector
import pytest

# 接收参数：user, password, host, port=3306, unix_socket and database
# 返回一个MySQLConnection Object
conn = mysql.connector.connect(
    host="127.0.0.1",       # 数据库主机地址
    port='3306',
    user="root",    # 数据库用户名
    passwd="lyc123456",   # 数据库密码
    database='test'
)
print(conn) # 输出：<mysql.connector.connection.MySQLConnection object at 0x7f91d16d3e50>

# 创建一个查询
cmd = conn.cursor()
res=[]
@pytest.mark.test
def test_select():
    # 执行一条原生的SQL语句，执行结果保存在cmd中，没有返回值
    cmd.execute("select name,age,address from student")
    # 可以使用fetchall()，获取所有的查询结果集，返回值为一个tuple，每一个元素是一个list
    global res
    res = cmd.fetchall()
    print("内部res：{}".format(res))# 输出：[('jack', 21, 'quanzhou'), ('tom', 23, 'xiamen'), ('lili', 24, 'zhangzhou'), ('Haru', 23, 'fuzhou')]
# test_select()
print("外部res：{}".format(res)) # 输出：[]  注意：单元测试这边还是输出空列表，但非单元测试这边会输出和内部res一样的内容
