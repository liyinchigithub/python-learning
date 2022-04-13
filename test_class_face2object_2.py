#!/usr/bin/python3
# -*- coding: UTF-8 -*-


from cgi import print_form
import pytest
import sys


class computed_father_class(): # 括号是用来写类继承父类（基类）
    fa_a=0
    fa_b=0
    # 构造函数
    def __init__(self,fa_a,fa_b): # 构造函数入参，在类实例化时自动调用接收参数  例如：a=computed_father_class(1,2)
        self.fa_a=fa_a # 接收参数，传给当前类的属性
        self.fa_b=fa_b
    # 类的函数，入参必须是self
    def fa_sum(self):
        print("基类的方法fa_sum被调用")
        return (self.fa_a+self.fa_b)*2
    def fa_multiplication(self):
        print("基类的方法fa_multiplication被调用")
        return self.fa_a*self.fa_b



class computed(computed_father_class):#派生类（子类）computed 继承了基类（父类）所有属性和方法，在括号中写入父类名
    # 类变量（数据成员）
    a = 0
    b = 0

    def __init__(self, a, b):
        # 实例变量（数据成员）
        self.a = a
        self.b = b
         #  子类调用父类的构造函数
        computed_father_class.__init__(self,2,2)

    def sum(self):
        # 局部变量
        result = self.a+self.b
        c=self.a+self.b
        print("c是成员变量：{}".format(c))
        return result
    
    def sin_call_father_class(self):
        return computed_father_class.fa_sum(self) # TypeError: fa_sum() missing 1 required positional argument: 'self'
    
    def avg(self):
        return self.a/self.b


if __name__ == '__main__':
    print("test  class 是main")
else:
    print("被引入")
