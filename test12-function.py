#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test12-function.py
# Python 自定义函数函数
# https://www.runoob.com/python3/python3-function.html
import pytest
'''
函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。

函数能提高应用的模块性，和代码的重复利用率。你已经知道Python提供了许多内建函数，比如print()。但你也可以自己创建函数，这被叫做用户自定义函数。
'''

'''
定义一个函数
你可以定义一个由自己想要功能的函数，以下是简单的规则：

* 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
* 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
* 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
* 函数内容以冒号 : 起始，并且缩进。
* return [表达式] 结束函数，选择性地返回一个值给调用方，不带表达式的 return 相当于返回 None。
'''
@pytest.mark.test
def test_hello():
    print("Hello World!")


'''
更复杂点的应用，函数中带上参数变量
'''
# 封装一个自定义函数，比较两个入参大小
@pytest.mark.test
@pytest.mark.parametrize("a,b",[(4,5)])
def test_max(a, b):
    if a > b:
        return str(a)+"大于"+str(b)
    else:
        return str(a)+"小于"+str(b)


# 计算面积函数

def area(width, height):
    return width * height

@pytest.mark.test
@pytest.mark.parametrize("w,h",[("4","5")]) # 入参数据类型字符串转数值
def test_print_welcome(w,h):
    print("width =", int(w), " height =", int(h), " area =", area(int(w), int(h)))
 

'''
    不定长参数
    [示例]
    定义函数:
        def test_nolong(arg1,*vartuple):
            print(arg1)
            print(vartuple)\
                
    调用时test_nolong(1,2,3,4)
     输出:  arg1为1 vartuple为(2,3,4) 即元组
    
'''



'''
函数调用
定义一个函数：给了函数一个名称，指定了函数里包含的参数，和代码块结构。

这个函数的基本结构完成以后，你可以通过另一个函数调用执行，也可以直接从 Python 命令提示符执行。

如下实例调用了 printme() 函数：
'''

# 定义函数
@pytest.mark.test
@pytest.mark.parametrize("str",["我要调用用户自定义函数!","再次调用同一函数"])
def printme( str ):
   # 打印任何传入的字符串
   print (str)
   return
 


'''
    pytest test12-function.py
'''