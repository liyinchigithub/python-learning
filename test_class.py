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


'''
[如何从python中的其他文件夹导入类?]
common/src/validation/file1.py
在common / src / validation文件夹中，定义了“ _init_ ”。

common/test/validation/file2.py
common/test/validation/case/file3.py
在file2.py和file3.py中，我想从file1.py导入类。

我在file2.py和file3.py中给出以下行：

from file1 import class1  
我目前收到错误消息：

#ImportError: No module named file1
sys.path.append应该是什么？

解决办法：
第一种
点阵方式，例如：from  api.log import log
api文件夹下有个log.py log.py中封装log类，使用类方法log().方法名()
第二种
sys.path.append('/src/validation/')
from file1 import class1
'''