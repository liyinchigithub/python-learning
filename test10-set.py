#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test10.py
# Python 集合
# https://www.runoob.com/python3/python3-set.html

import pytest

'''
集合（set）是一个无序的不重复元素序列。
可以使用大括号 { } 或者 set() 函数创建集合
注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

创建格式：
parame = {value01,value02,...}
或者
set(value)
'''


@pytest.mark.test
def test_create_set():
    set = {"a", "b", "c", "d"}  # 创建集合
    print("set:{}".format(set))  # set:{'d', 'b', 'c', 'a'}

    if "f" in set:  # 判断某个元素是否在集合中
        print("在集合中")
    else:
        print("不再集合中")


'''
集合的基本操作
1、添加元素
'''


@pytest.mark.test
def test_addSet():
    thisset = set(("Google", "Runoob", "Taobao"))  # 创建集合 set()
    thisset.add("Facebook")  # 添加元素到集合中
    print(thisset)


'''
2、删除元素
如果元素不存在，则会发生错误
'''


@pytest.mark.test
def test_delSet():
    thisset = set(("Google", "Runoob", "Taobao"))
    thisset.remove("Taobao")
    print(thisset)


'''
3、统计元素个数
'''


@pytest.mark.test
def test_countSet():
    thisset = set(("Google", "Runoob", "Taobao"))
    howLong = len(thisset)
    print("howLong:", howLong)


'''
4、清空集合
'''


@pytest.mark.test
def test_clearSet():
    thisset = set(("Google", "Runoob", "Taobao"))
    thisset.clear()
    print("thisset:", thisset)  # 输出：set()


'''
5、判断元素是否在集合中存在
'''


@pytest.mark.test
def test_isExisitSet():
    thisset = set(("Google", "Runoob", "Taobao"))
    isExisit = "Runoob" in thisset
    print("isExisit:", isExisit)  # 输出：set()


'''
   - 差集
   | 并集
   & 交集
   ^ 不同时存在
'''


@pytest.mark.test
def test_():
    a = set("adasdbcdef")
    b = set('adafgsgda')
    print(a)
    print(a-b)# a和b 差集
    print(a | b)# a和b 并集
    print(a & b)# a和b 交集
    print(a ^ b)# a和b 不同时存在的元素


'''
集合内置方法完整列表

方法	描述
add()	为集合添加元素
clear()	移除集合中的所有元素
copy()	拷贝一个集合
difference()	返回多个集合的差集
difference_update()	移除集合中的元素，该元素在指定的集合也存在。
discard()	删除集合中指定的元素
intersection()	返回集合的交集
intersection_update()	返回集合的交集。
isdisjoint()	判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
issubset()	判断指定集合是否为该方法参数集合的子集。
issuperset()	判断该方法的参数集合是否为指定集合的子集
pop()	随机移除元素
remove()	移除指定元素
symmetric_difference()	返回两个集合中不重复的元素集合。
symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
union()	返回两个集合的并集
update()	给集合添加元素
'''

'''
   命令行执行:pytest test10-set.py
'''
