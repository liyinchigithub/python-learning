#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test-mysql.py
# 操作数据库Mysql
# https://www.runoob.com/python3/python-mysql-connector.html
# https://www.runoob.com/python3/python3-mysql.html


# python-mysql-connector

import mysql.connector

# 接收参数：user, password, host, port=3306, unix_socket and database
# 返回一个MySQLConnection Object
conn = mysql.connector.connect(
    host="127.0.0.1",       # 数据库主机地址
    port=3306,
    user="root",    # 数据库用户名
    passwd="lyc123456",   # 数据库密码
    database='test'
)
print(conn)

# 创建一个查询
cmd = conn.cursor()

# 执行一条原生的SQL语句，执行结果保存在cmd中，没有返回值
cmd.execute("select name,age,address from class")
# 可以使用fetchall()，获取所有的查询结果集，返回值为一个tuple，每一个元素是一个list
res = cmd.fetchall()
print(res)
print("type:"+type(res))

# PyMySQL
