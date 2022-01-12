
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test-pytest-param.py
# pytest 之p参数化 arametrize
# https://blog.51cto.com/u_10913485/2898631

'''
    Pytest使用@pytest.mark.parametrize装饰器来实现数据驱动测试的，也就是常说的参数化
    
    parametrize(self,argnames, argvalues, indirect=False, ids=None, scope=None)
    
    [argnames]:参数名

    [argvalues]:参数对应值，[类型必须为list] 如果只有一个参数，里面则是值的列表
    例如:
        @pytest.mark.parametrize("username", ["yy", "yy2", "yy3"])。
        如果有多个参数，则需要用元组来存放值，
        一个元组对应一组参数的值，如：@pytest.mark.parametrize("name,pwd", [("yy1", "123"), ("yy2", "123"), ("yy3", "123")])。

    [Indirect]:如果设置成True，则把传进来的参数当函数执行，而不是一个参数。

    [ids]:用例的ID，传一个字符串列表，用来标识每一个测试用例，自定义测试数据结果，增加可读性。

'''


import pytest

# 1.单个数据
data = ["小红", "小明"]


@pytest.mark.parametrize("name", data)
def test_demo(name):
    print("测试数据为{}".format(name))


# 2.一组数据（列表嵌套字典）
data_1 = [
    {"username": "admin1", "password": "123456"},
    {"username": "admin2", "password": "12345678"},
]


@pytest.mark.parametrize("data", data_1)
def test_login(data):
    print("账号:{},密码:{}".format(data["username"], data["password"]))


# 3.列表嵌套列表
data_1 = [
    ["admin1", "123456"],
    ["admin2", "12345678"],
]


@pytest.mark.parametrize("username,password", data_1)
def test_login(username, password):
    print("账号:{},密码:{}".format(username, password))


# 4.列表嵌套元组
data_1 = [
    ("admin1", "123456"),
    ("admin2", "12345678"),
]


@pytest.mark.parametrize("username,password", data_1)
def test_login(username, password):
    print("账号:{},密码:{}".format(username, password))


# 5.装饰函数
@pytest.mark.parametrize("username,password", [("admin01", "123456"), ("admin02", "12345678")])
def test_demo(username, password):
    print("用户名:{},密码:{}".format(username, password))

# 6.装饰类
@pytest.mark.parametrize("username,password", [("admin01", "123456"), ("admin02", "12345678")])
class TestDemo:
    def test_demo(self, username, password):
        print("用户名:{},密码:{}".format(username, password))
# 注意：装饰测试类时，类内所有的方法必须接收测试数据，否则会报错；装饰测试函数时比较灵活，如果函数不使用数据就可以不装饰。

# 7.多个参数化修饰器
username = ["admin1", "admin2", "admin3"]
password = ["123456", "1234567", "12345678"]

@pytest.mark.parametrize("uname", username)
@pytest.mark.parametrize("pwd", password)
def test_demo(uname, pwd):
    print("用户名:{},密码:{}".format(uname, pwd))

# 8.增加可读性（parametrize参数中的ids，可以标识每一个测试用例，自定义测试数据结果的显示，增加可读性。）


data_1 = [
    (1, 2, 3),
    (4, 5, 9)
]
ids = ["a:{}+b:{}=expect:{}".format(a, b, expect)for a, b, expect in data_1]


def add(a, b):
    return a + b


@pytest.mark.parametrize('a, b, expect', data_1, ids=ids)
def test_parametrize_1(a, b, expect):
    print('\n测试函数1测试数据为\n{}-{}'.format(a, b))
    assert add(a, b) == expect
