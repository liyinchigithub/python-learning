#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：python-mysql-connector.py
# python 操作数据库Mysql
# https://www.runoob.com/python3/python-mysql-connector.html
# https://www.runoob.com/python3/python3-mysql.html


'''
    [安装依赖]
    python -m pip install mysql-connector
'''


import mysql.connector
import pytest
import random


'''
    [初始化]
    数据库连接
'''
try:
    # 接收参数：user, password, host, port=3306, unix_socket and database
    # 返回一个MySQLConnection Object
    conn = mysql.connector.connect(
    host="127.0.0.1",       # 数据库主机地址
    port='3306',
    user="root",    # 数据库用户名
    passwd="lyc123456",   # 数据库密码
    database='test')
    print("数据库连接成功!")  # 输出：<mysql.connector.connection.MySQLConnection object at 0x7f91d16d3e50>
except ConnectionError as e:
    # 数据库操作都基于这个实例
    print("数据库连接失败:{}".format(e))  # 输出：<mysql.connector.connection.MySQLConnection object at 0x7f91d16d3e50>


'''
    [执行select操作]
    使用fetchall()  一次性取回所有的结果集
'''
cmd = conn.cursor()
res = []
@pytest.mark.test
def test_select_fetchall():
    # 执行一条原生的SQL语句，执行结果保存在cmd中，没有返回值
    sql="SELECT * FROM student"
    cmd.execute(sql)
    # 可以使用fetchall()，获取所有的查询结果集，返回值为一个tuple，每一个元素是一个list
    global res
    res = cmd.fetchall()
    # 输出：[('jack', 21, 'quanzhou'), ('tom', 23, 'xiamen'), ('lili', 24, 'zhangzhou'), ('Haru', 23, 'fuzhou')]
    print("test_select_fetchall res：{}".format(res))


'''
    [执行select操作]
    使用fetchone()  每次只取一条记录
'''
@pytest.mark.skip
def test_select_fetchone():
    sql="SELECT * FROM student"
    cmd.execute(sql)
    # 使用fetchone()返回一条结果集，每调用一次之后，内部指针会指向下一条结果集
    print(cmd.fetchone())  # ('jack', 21, 'quanzhou')
    print(cmd.fetchone())  # ('tom', 23, 'xiamen')
    print(cmd.fetchone())  # ('lili', 24, 'zhangzhou')


'''
    [执行select操作]
    使用fetchmany(num)  指定每次返回的num条结果集

'''


@pytest.mark.skip
def test_select_fetchmany():
    sql="SELECT * FROM student"
    cmd.execute(sql)
    # 指定返回2条记录 输出：[('jack', 21, 'quanzhou'), ('tom', 23, 'xiamen')]
    res1 = cmd.fetchmany(2)
    print(res1)
    res2 = cmd.fetchmany(1)   # 指定返回1条记录 输出：[('lili', 24, 'zhangzhou')]
    print(res2)


'''
    [执行insert操作]
    insert操作，也都是使用execute方法，只需要将要执行的sql语句传入
'''
@pytest.mark.test
def test_insert():
    r = random.randint(0, 100000)
    sql = "INSERT INTO student(id,name,age,address) VALUES(%s,%s,%s,%s)"
    val = (r, "kk", 21, "nanping")
    # 注意，在SQL中的占位符，统一写%s, 具体的类型，是在tuple中，传入的参数元素类型决定
    cmd.execute(sql,val)  # 使用预处理格式（占位符格式）
    conn.commit()  # [注意] 数据库修改后，需要使用mydb.commit()语句提交，不提交，修改不会生效。
    print("mysql insert :{}".format(cmd.rowcount))  # 输出：1 返回插入成功的数据数量
    print("mysql insert res:{}".format(res))  # 输出：None 没有返回值


'''
    [执行update操作]
    update操作，也都是使用execute方法，只需要将要执行的sql语句传入
'''
@pytest.mark.test
def test_update():
    sql = "UPDATE student SET age = %s, address = %s WHERE id = %s"
    val = (19, "wuhan", 1)
    cmd.execute(sql, val)
    conn.commit()  # [注意] 数据库修改后，需要使用mydb.commit()语句提交，不提交，修改不会生效。
    print(cmd.rowcount, " 条记录已更新")


'''
    [执行delete操作]
    delete操作，也都是使用execute方法，只需要将要执行的sql语句传入
'''
@pytest.mark.test
def test_delete():
    res = cmd.execute("DELETE FROM student WHERE name LIKE 'kk'".format(64932))
    conn.commit()  # [注意] 数据库修改后，需要使用mydb.commit()语句提交，不提交，修改不会生效。
    print(cmd.rowcount, " 条记录已更新")
