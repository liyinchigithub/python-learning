#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：python-mysql-connector.py
# python操作数据库Mysql
# https://www.runoob.com/python3/python-mysql-connector.html
# https://www.runoob.com/python3/python3-mysql.html


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


'''
    执行select操作，使用fetchall()一次性取回所有的结果集
    fetchall()
'''
cmd = conn.cursor()
res=[]
@pytest.mark.skip
def test_select():
    # 执行一条原生的SQL语句，执行结果保存在cmd中，没有返回值
    cmd.execute("select name,age,address from student")
    # 可以使用fetchall()，获取所有的查询结果集，返回值为一个tuple，每一个元素是一个list
    global res
    res = cmd.fetchall()
    print("内部res：{}".format(res))# 输出：[('jack', 21, 'quanzhou'), ('tom', 23, 'xiamen'), ('lili', 24, 'zhangzhou'), ('Haru', 23, 'fuzhou')]
# test_select()
print("外部res：{}".format(res)) # 输出：[]  注意：单元测试这边还是输出空列表，但非单元测试这边会输出和内部res一样的内容

'''
    执行select操作，使用fetchone() 每次只取一条记录
    fetchone()
'''
@pytest.mark.skip
def test_select_one():
    cmd.execute("select name,age,address from student")
    # 使用fetchone()返回一条结果集，每调用一次之后，内部指针会指向下一条结果集
    print(cmd.fetchone()) # ('jack', 21, 'quanzhou')
    print(cmd.fetchone()) # ('tom', 23, 'xiamen')
    print(cmd.fetchone()) # ('lili', 24, 'zhangzhou')
'''
    执行select操作，使用fetchmany(num)指定每次返回的num条结果集
    fetchmany()
'''
@pytest.mark.test
def test_select_one():
    cmd.execute("select name,age,address from student")
    res1 = cmd.fetchmany(2)   # 指定返回2条记录 输出：[('jack', 21, 'quanzhou'), ('tom', 23, 'xiamen')]
    print(res1)
    res2 = cmd.fetchmany(1)   # 指定返回1条记录 输出：[('lili', 24, 'zhangzhou')]
    print(res2)