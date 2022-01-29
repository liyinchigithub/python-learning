#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名:test48-yaml.py
# Python PyYaml
# https://blog.csdn.net/rhx_qiuzhi/article/details/80153920
# https://www.cnblogs.com/ailiailan/p/11850857.html
import pytest
import yaml
'''
    [安装依赖]
    pip install PyYaml
'''

'''
    [PyYaml]
    是Python的一个专门针对yaml文件操作的模块，使用起来非常简单。
'''

'''
    [YAML]
    YAML是专门用来写配置文件的语言，远比JSON格式方便。

    YAML语言的设计目标，就是方便人类读写。

    YAML是一种比XML和JSON更轻的文件格式，也更简单更强大，它可以通过缩进来表示结构，是不是听起来就和Python很搭？

    顾名思义，用语言编写的文件就可以称之为YAML文件。PyYaml是Python的一个专门针对YAML文件操作的模块，使用起来非常简单
'''
@pytest.mark.test
def test_():
    yaml_str = """
    name: 一条大河
    age: 1956
    job: Singer
    """

    y = yaml.load(yaml_str, Loader=yaml.SafeLoader)
    print(y)# 输出：{'name': '一条大河', 'age': 1956, 'job': 'Singer'}



if __name__ == '__main__':
    print("yaml配置文件")