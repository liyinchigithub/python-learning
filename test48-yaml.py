#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名:test48-yaml.py
# Python PyYaml
# https://blog.csdn.net/rhx_qiuzhi/article/details/80153920
# https://www.cnblogs.com/ailiailan/p/11850857.html
import pytest
import yaml
import datetime
import pytz
import os
from ruamel import yaml

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

    顾名思义，用语言编写的文件就可以称之为YAML文件。
    
    PyYaml是Python的一个专门针对YAML文件操作的模块，使用起来非常简单,就像json、pickle一样，load、dump就足够我们使用了。
'''




'''
    load()示例：返回一个对象
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


'''
    load_all()示例
    [生成一个迭代器]
    如果string或文件包含几块yaml文档，可以使用yaml.load_all来解析全部的文档。
    yaml_test.yaml文件内容：
'''

@pytest.mark.test
def test_yaml():
    with open("./yaml/yaml_test.yaml", 'r', encoding='utf-8') as f:
        cfg = yaml.load_all(f, Loader=yaml.SafeLoader)
        for data in cfg:
            print(data)# 输出：{'name': 'qiyu', 'age': '20岁'}{'name': 'qingqing', 'age': '19岁'}



'''
    dump()示例：将一个python对象生成为yaml文档
'''




'''
    使用dump()传入参数，可以直接把内容写入到yaml文件：
'''




'''
    yaml.dump_all()示例：将多个段输出到一个文件中
'''




'''
为什么写入文件后的格式有的带1个“-”，有的带2个“-”？

为什么yaml文件读出来的的格式是List？
'''




'''
    YAML的[语法规则]和[]数据结构

    看完了以上4个简单的示例，现在就来总结下YAML语言的基本语法

    YAML 基本语法规则如下：
        1、大小写敏感
        2、使用缩进表示层级关系
        3、缩进时不允许使用Tab键，只允许使用空格。
        4、缩进的空格数目不重要，只要相同层级的元素左侧对齐即可
        5、# 表示注释，从这个字符一直到行尾，都会被解析器忽略，这个和python的注释一样
        6、列表里的项用"-"来代表，字典里的键值对用":"分隔
    
    知道了语法规则，现在来回答下上面的2个问题：

        1、带1个“-”表示不同的模块（单个数组或者字典），带2个“-”是因为数组中元素以“-”开始，加上表示不同模块的那一个“-”，呈现出来就是2个“-”
        2、因为yaml文件中包含多个模块（多个数组或者字典），读取出来的是这些模块的一个集合
        3、有且只有当yaml文件中只有1个字典时，读取出来的数据的类型也是字典
        
    YAML 支持的数据结构有3种：
        1、对象：键值对的集合
        2、数组：一组按次序排列的值，序列（sequence） 或 列表（list）
        3、纯量（scalars）：单个的、不可再分的值，如：字符串、布尔值、整数、浮点数、Null、时间、日期
        
    支持数据示例：
        yaml_test_data.yaml的内容：


'''


'''
    yaml_test_data.yaml的内容：
'''

@pytest.mark.test
def test_data_yaml():
        yaml_data = {
        "str": "Big River",
        "int": 1548,
        "float": 3.14,
        'boolean': True,
        "None": None,
        'time': datetime.datetime.now(tz=pytz.timezone('UTC')).isoformat(),
        'date': datetime.datetime.today()
    }

        with open('./yaml/yaml_test.yml', 'w') as f:
            y = yaml.dump(yaml_data, f)
            print(y)

        with open('./yaml/yaml_test.yml', 'r') as r:
            y1 = yaml.load(r, Loader=yaml.SafeLoader)
            print(y1)



'''
    [python对象生成yaml文档]

    1、yaml.dump()方法
'''
# @pytest.mark.test
def generate_yaml_doc(yaml_file):
        py_object = {'school': 'zhu',
                    'students': ['a', 'b']}
        file = open(yaml_file, 'w', encoding='utf-8')
        yaml.dump(py_object, file)
        file.close()

current_path = os.path.abspath(".")
yaml_path = os.path.join(current_path, "generate.yaml")
generate_yaml_doc(yaml_path)

'''
    [python对象生成yaml文档]

    2、使用ruamel模块中的yaml方法生成标准的yaml文档
'''
# @pytest.mark.test
def generate_yaml_doc_ruamel(yaml_file):
    py_object = {'school': 'zhu',
                 'students': ['a', 'b']}
    file = open(yaml_file, 'w', encoding='utf-8')
    yaml.dump(py_object, file, Dumper=yaml.RoundTripDumper)
    file.close()

current_path = os.path.abspath(".")
yaml_path = os.path.join(current_path, "generate.yaml")
generate_yaml_doc_ruamel(yaml_path)


'''
    使用ruamel模块中的yaml方法读取yaml文档（用法与单独import yaml模块一致）
'''
def get_yaml_data_ruamel(yaml_file):
    file = open(yaml_file, 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.Loader)
    file.close()
    print(data)

current_path = os.path.abspath(".")
yaml_path = os.path.join(current_path, "generate.yaml")
get_yaml_data_ruamel(yaml_path)



if __name__ == '__main__':
    print("yaml配置文件")