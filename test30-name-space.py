#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test30-name-space.py
# Python 命名空间
# https://www.runoob.com/python3/python3-namespace-scope.html
import sys
import pytest

'''
   [命名空间]3种命名空间
   [内置名称（built-in names）]， Python 语言内置的名称，比如函数名 abs、char 和异常名称 BaseException、Exception 等等。
   [全局名称（global names）]，模块中定义的名称，记录了模块的变量，包括函数、类、其它导入的模块、模块级的变量和常量。
   [局部名称（local names）]，函数中定义的名称，记录了函数的变量，包括函数的参数和局部定义的变量。（类中定义的也是）
'''


'''
   命名空间查找顺序:

   假设我们要使用变量 runoob，则 Python 的查找顺序为：[局部的命名空间去] -> [全局命名空间] -> [内置命名空间。]

   如果找不到变量 runoob，它将放弃查找并引发一个 [NameError] 异常:

   NameError: name 'runoob' is not defined。
   命名空间的生命周期：

   命名空间的生命周期取决于对象的作用域，如果对象执行完成，则该命名空间的生命周期就结束。

   因此，我们无法从外部命名空间访问内部命名空间的对象。


'''
# var1 是全局名称
var1 = 5


def some_func():

    # var2 是局部名称
    var2 = 6

    def some_inner_func():

        # var3 是内嵌的局部名称
        var3 = 7


'''
   [作用域]
   就是一个 Python 程序可以直接访问命名空间的正文区域。

   在一个 python 程序中，直接访问一个变量，会从内到外依次访问所有的作用域直到找到，否则会报未定义的错误。

   Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。

   变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python 的作用域一共有4种，分别是：

   有四种作用域：

   L（Local）：最内层，包含局部变量，比如一个函数/方法内部。
   E（Enclosing）：包含了非局部(non-local)也非全局(non-global)的变量。比如两个嵌套函数，一个函数（或类） A 里面又包含了一个函数 B ，那么对于 B 中的名称来说 A 中的作用域就为 nonlocal。
   G（Global）：当前脚本的最外层，比如当前模块的全局变量。
   B（Built-in）： 包含了内建的变量/关键字等，最后被搜索。
'''


g_count = 0  # 全局作用域


def outer():
    o_count = 1  # 闭包函数外的函数中

    def inner():
        i_count = 2  # 局部作用域


'''
   内置作用域是通过一个名为 builtin 的标准模块来实现的，但是这个变量名自身并没有放入内置作用域内，
   所以必须导入这个文件才能够使用它。在Python3.0中，可以使用以下的代码来查看到底预定义了哪些变量:
'''

import builtins
dir(builtins)

'''
   Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
   其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问
'''

'''
   Python 中只有模块/py文件（module），类（class）以及函数（def、lambda）才会引入新的作用域，
   其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问
'''




'''
   实例中 msg 变量定义在 if 语句块中，但[外部还是可以访问的]。
'''

if True:
   msg = 'I am from Runoob'
print(msg)

'''
   如果将 msg 定义在[函数中]，则它就是局部变量，[外部不能访问]：
'''
def test():
   msg_inner = 'I am from Runoob'
# print(msg_inner) # 会报错 msg_inner not definitions 从报错的信息上看，说明了 msg_inner 未定义，无法使用，因为它是局部变量，只有在函数内可以使用。



'''
   [全局变量]和[局部变量]
   定义在[函数内部]的变量拥有一个【局部作用域】，定义在[函数外]的拥有【全局作用域】。
   局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。
   调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。
   如下实例：
'''

total = 0 # total是一个全局变量
# 可写函数说明
def sum( arg1, arg2 ):
    #返回2个参数的和."
    total = arg1 + arg2 # total在这里是局部变量.
    print ("函数内是局部变量 : ", total)
    return total
 
#调用sum函数
sum( 10, 20 )
print ("函数外是全局变量 : ", total)

'''
   输出:
   函数内是局部变量 :  30
   函数外是全局变量 :  0
'''

'''
   [global] 和 [nonlocal]关键字
   当[内部作用域]想修改[外部作用域]的变量时，就要用到 global 和 nonlocal 关键字了。
   以下实例修改全局变量 num：
'''

num = 1# num是全局变量
def fun1():
    global num  # 需要使用 global 关键字声明，函数内使用全局变量
    print(num) # 此时num值还是1
    num = 123 # 改变全局变量的值
    print(num) # 此时num值是3
fun1()
print(num)# 此时num值是3

'''
   输出:
   1
   123
   123
'''

'''
   如果要[修改嵌套作用域]（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了，如下实例：
'''

def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明，此时num本身是在函数内局部，变成全局
        num = 100
        print(num)# 输出：100
    inner()
    print(num)# 输出：100
outer()

'''
   [错误]
   错误信息为局部作用域引用错误，因为 test 函数中的 a 使用的是局部，未定义，无法修改。
   修改 a 为全局变量：
   
   a = 10
   def test():
      a = a + 1 # 报错因为a在函数内是局部变量，未定义，要重新定义，却别与函数外的全局变量，虽然名称一样，但是一个全局变量一个函数内局部变量，函数内使用全局变量加global
      print(a)
   test()
'''


'''
   [正确]
   # 通过函数参数传递
   a = 10
   def test(a):
      a = a + 1
      print(a)
   test(a)
'''

'''
   [正确]
   # 使用global关键字
   a = 10
   def test():
      global a
      a = a + 1
      print(a)
   test()
'''