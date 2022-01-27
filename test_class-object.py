#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# test-class-object.py
# 封装类
# 其他python文件导入，类的实例化对象，进行引用类的方法和属性

from unittest import result


class test:
    # 构造函数
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def sum(self):
        return self.a+self.b

result=test(1,2).sum()# 实例化类的对象，并引用其自定义方法，入参在实例化便传入，构造函数会在内部自定义
print(result)
