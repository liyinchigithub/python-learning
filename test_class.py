#!/usr/bin/python3
# -*- coding: UTF-8 -*-


import pytest
import sys
import test_class_face2object_2

@pytest.mark.test
def test_class_demo():
    # 实例化
    obj=test_class_face2object_2.computed(1,2)
    # 实例化调用类属性和方法
    print("obj.sum()为：{}".format(obj.sum()))
    print("obj.avg()为：{}".format(obj.avg()))
