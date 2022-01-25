#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
import sys
import time
import datetime
import json
from bunch import Bunch
import numpy as np


# 参考：https://blog.csdn.net/weixin_34366546/article/details/87985536

'''
    [文件夹遍历]
    遍历文件夹函数提供的功能和扩展，如下：
    返回文件的路径和名称；
    根据后缀名筛选文件；
    去除隐藏文件，即以“.”开头的文件；
'''

def traverse_dir_files(root_dir, ext=None):
    """
    列出文件夹中的文件, 深度遍历
    :param root_dir: 根目录
    :param ext: 后缀名
    :return: [文件路径列表, 文件名称列表]
    """
    names_list = []
    paths_list = []
    for parent, _, fileNames in os.walk(root_dir):
        for name in fileNames:
            if name.startswith('.'):  # 去除隐藏文件
                continue
            if ext:  # 根据后缀名搜索
                if name.endswith(tuple(ext)):
                    names_list.append(name)
                    paths_list.append(os.path.join(parent, name))
            else:
                names_list.append(name)
                paths_list.append(os.path.join(parent, name))
    paths_list, names_list = sort_two_list(paths_list, names_list)
    return paths_list, names_list


'''
    [文件夹创建]
    创建文件夹函数提供的功能和扩展，如下：
        当文件夹不存在时，创建文件夹；
        当文件夹存在时，根据参数，是否删除文件夹；
'''

def mkdir_if_not_exist(dir_name, is_delete=False):
    """
    创建文件夹
    :param dir_name: 文件夹
    :param is_delete: 是否删除
    :return: 是否成功
    """
    try:
        if is_delete:
            if os.path.exists(dir_name):
                shutil.rmtree(dir_name)
                print('[INFO] 文件夹 "%s" 存在, 删除文件夹.' % dir_name)
 
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
            print('[INFO] 文件夹 "%s" 不存在, 创建文件夹.' % dir_name)
        return True
    except Exception as e:
        print('[Exception] %s' % e)
        return False
    
'''
    [文件读取]
    文件读取函数提供的功能和扩展，如下：
        实现便捷地文件读取功能；
        当参数mode是one时，读取1行；
        当参数mode是more时，读取多行；
'''
def read_file(data_file, mode='more'):
    """
    读文件, 原文件和数据文件
    :return: 单行或数组
    """
    try:
        with open(data_file, 'r') as f:
            if mode == 'one':
                output = f.read()
                return output
            elif mode == 'more':
                output = f.readlines()
                return map(str.strip, output)
            else:
                return list()
    except IOError:
        return list()
    
'''
    [时间可读]
    可读时间函数提供的功能和扩展，如下：
    输入时间戳（如time.time()），输出可读时间str；
    输出格式是年-月-日 时:分:秒；
'''
def timestamp_2_readable(time_stamp):
    """
    时间戳转换为可读时间
    :param time_stamp: 时间戳，当前时间：time.time()
    :return: 可读时间字符串
    """
    return datetime.fromtimestamp(time_stamp).strftime('%Y-%m-%d %H:%M:%S')



    
'''
    [时间统计]
    时间统计函数提供的功能和扩展，如下：
    显示起始和结束时间；
    统计执行的秒数，可以用于统计单次耗时；
'''
def time_count():
    start_time = datetime.now()  # 起始时间
    print("[INFO] 当前时间: %s" % timestamp_2_readable(time.time()))
    
    time.sleep(10)
    
    print("[INFO] 结束时间: %s" % timestamp_2_readable(time.time()))
    elapsed_time = (datetime.now() - start_time).total_seconds()  # 终止时间
    print("[INFO] 耗时: %s (秒)" % elapsed_time)
 
'''
    [安全除法]
    安全除法函数提供的功能和扩展，如下：
    基本的除法功能；
    转换为浮点数（float）；
    避免除数为0，当除数为0时，直接返回0.0；
'''

def safe_div(x, y):
    """
    安全除法
    :param x: 被除数 
    :param y: 除数
    :return: 结果
    """
    x = float(x)
    y = float(y)
    if y == 0.0:
        return 0.0
    else:
        return x / y


'''
    [双列表排序]
    双列表排序函数提供的功能和扩展，如下：
        同时排序列表1和列表2；
        两个列表的对应顺序不变；
'''
def sort_two_list(list1, list2):
    """
    排序两个列表
    :param list1: 列表1
    :param list2: 列表2
    :return: 排序后的两个列表
    """
    list1, list2 = (list(t) for t in zip(*sorted(zip(list1, list2))))
    return list1, list2


'''
    [配置读取]
    配置读取函数提供的功能和扩展，如下：
        配置文件是JSON格式；
        配置文件转换为配置类和配置字典
'''

 
def get_config_from_json(json_file):
    """
    将配置文件转换为配置类
    :param json_file: json文件
    :return: 配置信息
    """
    with open(json_file, 'r') as config_file:
        config_dict = json.load(config_file)  # 配置字典
    config = Bunch(config_dict)  # 将配置字典转换为类
    return config, config_dict


'''
    [Numpy判空]
    空的NdArray可以用于异常处理；
    当NdArray的属性size值为0时，NdArray为空。
'''
def is_empty():

    a = np.array([])
    print(a.size) # 0


'''
    [脚本路径]
    当执行Python脚本时，路径未包含当前工程，需要强制指定文件夹位置（dirname），否则无法找到同工程中的其他类。
    以下是二层路径的实现，当层次较多时，嵌套多次os.path.dirname即可。
'''
def script_path():
    p = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if p not in sys.path:
        sys.path.append(p)
    '''

'''