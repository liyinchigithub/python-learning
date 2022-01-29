#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名:test48-yaml.py
# Python PyYaml
# https://blog.csdn.net/rhx_qiuzhi/article/details/80153920
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