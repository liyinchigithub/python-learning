#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test14.py
# Python 错误和异常
# https://www.runoob.com/python3/python3-errors-execptions.html
'''
Python 有两种错误很容易辨认：语法错误和异常。

Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。

[try/except]
异常捕捉可以使用 try/except 语句。

[try/except...else]
try/except 语句还有一个可选的 else 子句，如果使用这个子句，那么必须放在所有的 except 子句之后。
else 子句将在 try 子句没有发生任何异常的时候执行。
使用 else 子句比把所有的语句都放在 try 子句里面要好，这样可以避免一些意想不到，而 except 又无法捕获的异常。
异常处理并不仅仅处理那些直接发生在 try 子句中的异常，而且还能处理子句中调用的函数（甚至间接调用的函数）里抛出的异常。

[try-finally 语句]
try-finally 语句无论是否发生异常都将执行最后的代码。

[抛出异常]
Python 使用 raise 语句抛出一个指定的异常。

[用户自定义异常]
你可以通过创建一个新的异常类来拥有自己的异常。
异常类继承自 Exception 类，可以直接继承，或者间接继承

[定义清理行为]
try 语句还有另外一个可选的子句，它定义了无论在任何情况下都会执行的清理行为.

[try 语句按照如下方式工作]
首先，执行 try 子句（在关键字 try 和关键字 except 之间的语句）。
如果没有异常发生，忽略 except 子句，try 子句执行后结束。
如果在执行 try 子句的过程中发生了异常，那么 try 子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的 except 子句将被执行。
如果一个异常没有与任何的 except 匹配，那么这个异常将会传递给上层的 try 中。
一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常,最多只有一个分支会被执行。
except (RuntimeError, TypeError, NameError):
    pass
'''
import pytest
import sys


@pytest.mark.test
def test_raise_exception_():
    try:
        f = open('myfile.txt')
        s = f.readline()
        i=int(s.strip())
    except OSError as err:
        print("OSerror:{0}".format(err))
    except ValueError:
        print("Couldnotconvertdatatoaninteger.")
    except:
        print("Unexpectederror:", sys.exc_info()[0])
        raise
    else:
        print('这句话,在没有发生异常时，执行完try就会执行else块内容。')
    finally:
        print('这句话,无论异常是否发生都会执行。')
