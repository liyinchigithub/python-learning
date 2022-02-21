#!/usr/bin/python3
# -*- coding: UTF-8 -*-


import pytest
import sys
import test_class_face2object_2

@pytest.mark.skip
def test_class_demo():
    # 实例化类对象
    obj=test_class_face2object_2.computed(1,2)
    # 实例化调用类属性和方法
    print("obj.sum()为：{}".format(obj.sum()))# 实例化对象调用类方法
    print("obj.avg()为：{}".format(obj.avg()))# 实例化对象调用类方法
    print("obj.a为：{}".format(obj.a))# 实例化对象调用类属性

@pytest.mark.test
def  test_sin_father_class():
       # 子类继承父类，调用父类方法
       result1 =test_class_face2object_2.computed(2,2).sin_call_father_class()
       # 子类继承父类，不调用父类方法，调用子类自己的方法
       result2 =test_class_face2object_2.computed(2,2).sum()
       print("子类调用父类函数fa_sum()为{}".format(result1));
       print("子类调用自己的函数sum()为{}".format(result2));
       # 重写（子类重写父类方法）
       

'''
    运行脚本：
    pytest test_class.py
'''